import datetime
import os
import numpy as np
import gym
from backtrader_plotting import Bokeh
from collections import defaultdict

import backtrader as bt
btind = bt.indicators
btfeeds = bt.feeds
btanlys = bt.analyzers
btstrge = bt.strategies

from backtrader.utils import num2date, date2num

class CerebroGym(bt.Cerebro):
    params = (
        ('runonce', False),
    )

    def _runnext(self, runstrats):
        '''
        Actual implementation of run in full next mode. All objects have its
        ``next`` method invoke on each data arrival
        '''
        self.runner = self._runnext_y(runstrats)

    def _runnext_y(self, runstrats):
        datas = sorted(self.datas,
                       key=lambda x: (x._timeframe, x._compression))
        datas1 = datas[1:]
        data0 = datas[0]
        d0ret = True

        rs = [i for i, x in enumerate(datas) if x.resampling]
        rp = [i for i, x in enumerate(datas) if x.replaying]
        rsonly = [i for i, x in enumerate(datas)
                  if x.resampling and not x.replaying]
        onlyresample = len(datas) == len(rsonly)
        noresample = not rsonly

        clonecount = sum(d._clone for d in datas)
        ldatas = len(datas)
        ldatas_noclones = ldatas - clonecount
        lastqcheck = False
        dt0 = date2num(datetime.datetime.max) - 2  # default at max
        while d0ret or d0ret is None:
            # if any has live data in the buffer, no data will wait anything
            newqcheck = not any(d.haslivedata() for d in datas)
            if not newqcheck:
                # If no data has reached the live status or all, wait for
                # the next incoming data
                livecount = sum(d._laststatus == d.LIVE for d in datas)
                newqcheck = not livecount or livecount == ldatas_noclones

            lastret = False
            # Notify anything from the store even before moving datas
            # because datas may not move due to an error reported by the store
            self._storenotify()
            if self._event_stop:  # stop if requested
                return
            self._datanotify()
            if self._event_stop:  # stop if requested
                return

            # record starting time and tell feeds to discount the elapsed time
            # from the qcheck value
            drets = []
            qstart = datetime.datetime.utcnow()
            for d in datas:
                qlapse = datetime.datetime.utcnow() - qstart
                d.do_qcheck(newqcheck, qlapse.total_seconds())
                drets.append(d.next(ticks=False))

            d0ret = any((dret for dret in drets))
            if not d0ret and any((dret is None for dret in drets)):
                d0ret = None

            if d0ret:
                dts = []
                for i, ret in enumerate(drets):
                    dts.append(datas[i].datetime[0] if ret else None)

                # Get index to minimum datetime
                if onlyresample or noresample:
                    dt0 = min((d for d in dts if d is not None))
                else:
                    dt0 = min((d for i, d in enumerate(dts)
                               if d is not None and i not in rsonly))

                dmaster = datas[dts.index(dt0)]  # and timemaster
                self._dtmaster = dmaster.num2date(dt0)
                self._udtmaster = num2date(dt0)

                # slen = len(runstrats[0])
                # Try to get something for those that didn't return
                for i, ret in enumerate(drets):
                    if ret:  # dts already contains a valid datetime for this i
                        continue

                    # try to get a data by checking with a master
                    d = datas[i]
                    d._check(forcedata=dmaster)  # check to force output
                    if d.next(datamaster=dmaster, ticks=False):  # retry
                        dts[i] = d.datetime[0]  # good -> store
                        # self._plotfillers2[i].append(slen)  # mark as fill
                    else:
                        # self._plotfillers[i].append(slen)  # mark as empty
                        pass

                # make sure only those at dmaster level end up delivering
                for i, dti in enumerate(dts):
                    if dti is not None:
                        di = datas[i]
                        rpi = False and di.replaying  # to check behavior
                        if dti > dt0:
                            if not rpi:  # must see all ticks ...
                                di.rewind()  # cannot deliver yet
                            # self._plotfillers[i].append(slen)
                        elif not di.replaying:
                            # Replay forces tick fill, else force here
                            di._tick_fill(force=True)

                        # self._plotfillers2[i].append(slen)  # mark as fill

            elif d0ret is None:
                # meant for things like live feeds which may not produce a bar
                # at the moment but need the loop to run for notifications and
                # getting resample and others to produce timely bars
                for data in datas:
                    data._check()
            else:
                lastret = data0._last()
                for data in datas1:
                    lastret += data._last(datamaster=data0)

                if not lastret:
                    # Only go extra round if something was changed by "lasts"
                    break

            # Datas may have generated a new notification after next
            self._datanotify()
            if self._event_stop:  # stop if requested
                return

            if d0ret or lastret:  # if any bar, check timers before broker
                self._check_timers(runstrats, dt0, cheat=True)

            self._brokernotify()
            if self._event_stop:  # stop if requested
                return

            if d0ret or lastret:  # bars produced by data or filters
                self._check_timers(runstrats, dt0, cheat=False)
                for strat in runstrats:
                    strat.act = yield strat._send_observations(), strat.info
                    strat.info.clear()
                    strat._next()
                    if self._event_stop:  # stop if requested
                        return

                    self._next_writers(runstrats)

        # Last notification chance before stopping
        self._datanotify()
        if self._event_stop:  # stop if requested
            return
        self._storenotify()
        if self._event_stop:  # stop if requested
            return

class GymMartingaleEnv(gym.Env):

    class GymStrategy(bt.Strategy):

        def __init__(self):
            self.last_order = None
            self.act = None
            self.info = defaultdict(str)
            
        def _add_info(self, key, txt):
            self.info[key] += txt

        def notify_order(self, order):
            if order.status in [order.Submitted, order.Accepted]:
                # Buy/Sell order submitted/accepted to/by broker - Nothing to do
                return

            # Check if an order has been completed
            # Attention: broker could reject order if not enough cash
            if order.status in [order.Completed]:
                if order.isbuy():
                    txt = 'BUY'
                elif order.issell():
                    txt = 'SELL'
                txt += ' EXECUTED at price: %.5f, with value: %.5f' % (order.executed.price, order.executed.value)
            elif order.status in [order.Canceled, order.Margin, order.Rejected]:
                txt = 'Order Canceled/Margin/Rejected'
            self._add_info('Broker', txt)

        def next(self):
            txt = ''
            pos_size = self.getposition(self.data).size
            action, order_value = self.act
            if pos_size * action < 0:
                txt = 'Close set'
                self.close()
            elif order_value != 0 and (pos_size == 0 or pos_size * action > 0):
                if action > 0:
                    self.buy(size=order_value)
                    txt = f'buy set with value={order_value}'
                else:
                    self.sell(size=order_value)
                    txt = f'sell set with value={order_value}'
                                     
            if txt:
                self._add_info('Orders', txt)
                                     

        def _send_observations(self):
            pos_size = self.getposition(self.data).size
            cash = self.broker.get_cash()
            value = self.broker.get_value()
            today = [
                getattr(self.data, name)[0] for name in ['open', 'high', 'low', 'close']
                ]
            observations = {
                'Asset Value':value,
                'Cash':cash,
                'Position Size':pos_size,
                'Position Step':None,
                'Price Candle':np.array(today),
            }
            return observations

    def __init__(self,
    data:btfeeds.GenericCSVData,
    *,
    max_step=5,
    init_cash=10_000,
    base_cash = 10,
    commission=0.000,
    leverage=1
    ):
        self.init_cash = init_cash
        self.last_value = init_cash + base_cash
        self.max_step = max_step
        self.current_step = 0
        self.share_steps = ss = tuple(2 ** a for a in range(max_step))
        self.share_size = init_cash / sum(ss)

        self.observation_space = gym.spaces.Dict({
            'Asset Value':gym.spaces.Box(
                low=0,
                high=np.inf,
                shape=(1,),
                dtype=np.float32),
            'Cash':gym.spaces.Box(
                low=0,
                high=np.inf,
                shape=(1,),
                dtype=np.float32),
            'Position Size':gym.spaces.Box(
                low= -np.inf,
                high=np.inf,
                shape=(1,),
                dtype=np.int32),
            'Position Step':gym.spaces.Discrete(max_step),
            'Price Candle':gym.spaces.Box(
                low=0,
                high=np.inf,
                shape=(4,),
                dtype=np.float32),
        })

        self.action_space = gym.spaces.Discrete(3, start=-1)
        # -1: make short position for first step and if in short add next step but
        # close positions if in long
        #  0: do nothing
        #  1: make long position for first step and if in long add next step but
        # close positions if in short



        self.cerebro = cerebro = CerebroGym()
        self.info = defaultdict(str)
        cerebro.broker.setcash(init_cash + base_cash)
        cerebro.broker.setcommission(
            commission=commission,
            leverage=leverage,
            margin=leverage,
        )
        cerebro.broker.set_shortcash = False
        # cerebro.broker.set_int2pnl = False
        # cerebro.broker.set_fundmode = True

        cerebro.addstrategy(self.GymStrategy)

        cerebro.adddata(data)

        cerebro.addobserver(
            bt.observers.BuySell,
            barplot=True,
            bardist=0.001)
        cerebro.addobserver(bt.observers.Cash)
        cerebro.addobserver(bt.observers.Value)
        cerebro.addobserver(bt.observers.Trades)
        cerebro.addobserver(bt.observers.DrawDown)
        cerebro.addobserver(bt.observers.FundValue)       

    def render(self, name='', output_mode='show'):
        if not name:
            try:
                os.makedirs('plots')
            except FileExistsError:
                pass
            name = 'plots/trades_plot.html'
        b = Bokeh(filename=name, style='bar', plot_mode='single', output_mode=output_mode)
        self.cerebro.plot(b, iplot=False)
        
    def reset(self):
        self.res = self.cerebro.run(stdstats=False)[0]
        strat_observations, self.info = self.cerebro.runner.send(None)
        strat_observations['Position Step'] = 0
        return strat_observations , self.info

    def step(self, action):
        command = self._make_command(action)
        try:
            self.observations = self._make_observations(command)
            reward = self._calc_reward()
            done = self._check_done()
            return self.observations, reward, done, self.info
        except StopIteration:
            self._add_info('data', 'There are no more candles')
            return self.observations, 0., True, self.info

    def _make_command(self, action):
        order_value = 0
        if action in [-1, 1]:
            if self.current_step < self.max_step:
                order_value = self.share_steps[self.current_step] * self.share_size
                self.current_step += 1
        return (action, order_value)

    def _make_observations(self, command):
        strat_observations, self.info = self.cerebro.runner.send(command)
        if strat_observations['Position Size'] == 0:
            self.current_step = 0
        strat_observations['Position Step'] = self.current_step
        return strat_observations

    def _calc_reward(self):
        current_value = self.observations['Asset Value']
        reward = current_value - self.last_value
        self.last_value = current_value
        return reward

    def _check_done(self):
        return self.observations['Asset Value'] < 0

    def _add_info(self, key, txt):
        self.info[key] += txt


csv_data_reader = btfeeds.GenericCSVData
TimeFrame = bt.TimeFrame

