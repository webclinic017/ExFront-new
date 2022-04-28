import datetime
import os
import numpy as np
import gym
from backtrader_plotting import Bokeh
from collections import defaultdict
from collections.abc import Iterable

import backtrader as bt
btind = bt.indicators
btfeeds = bt.feeds
btanlys = bt.analyzers
btstrge = bt.strategies

from backtrader.utils import num2date, date2num

csv_data_reader = btfeeds.GenericCSVData
TimeFrame = bt.TimeFrame

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
        

class BasicGymStrategy(bt.Strategy):
    
    @staticmethod
    def observation_space():
        return {
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
        'Price Candle':gym.spaces.Box(
            low=0,
            high=np.inf,
            shape=(4,),
            dtype=np.float32),
    }
    
    @staticmethod
    def action_space():
        return {}
    
    def __init__(self):
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
        raise NotImplementedError                                     

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
            'Price Candle':np.array(today),
        }
        return observations
    
    
class BasicGymEnv(gym.Env):

    def __init__(self,
    strategy:'BasicGymStrategy',
    data:btfeeds.GenericCSVData,
    *,
    init_cash=10_000,
    base_cash = 10,
    commission=0.000,
    leverage=1
    ):
        self.init_cash = init_cash
        self.last_value = init_cash + base_cash
        self.observation_space = gym.spaces.Dict(strategy.observation_space())
        self.action_space = gym.spaces.Dict(strategy.action_space())
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

        cerebro.addstrategy(strategy)

        cerebro.adddata(data)

        cerebro.addobserver(
            bt.observers.BuySell,
            barplot=False,
            bardist=0)
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
    
    @staticmethod
    def _tst_nan(x):
        if isinstance(x, Iterable):
            return any(np.isnan(x))
        else:
            return np.isnan(x)
    
    def reset(self):
        self.res = self.cerebro.run(stdstats=False)[0]
        has_nan = True
        while has_nan:
            strat_observations, self.info = self.cerebro.runner.send(None)
            has_nan = any(self._tst_nan(x) for x in strat_observations.values())
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
        return action

    def _make_observations(self, command):
        strat_observations, self.info = self.cerebro.runner.send(command)
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
        

class GridStrategy(BasicGymStrategy):
    
    @staticmethod
    def action_space():
        return {
            'Activate':gym.spaces.Discrete(2),
            #  0: grid deactive
            #  1: generates the grid and keeps it alive
            'mode':gym.spaces.Discrete(2),
            # 0: Arithmetic mode
            # 1: Geometric mode
            'Grid':gym.spaces.Discrete(9, start=2),
            # Number of Grids 2-10
            'each step investment amount':gym.spaces.Box(
                low= 0,
                high=np.inf,
                shape=(1,),
                dtype=np.float32),
            # The amount of capital that enters each grid line
            'Lower and Upper Prices':gym.spaces.Box(
                low=0,
                high=np.inf,
                shape=(2,),
                dtype=np.float32),
            # Lower Price should be lower than Upper Price to grid be generate
        }

    def __init__(self):
        super().__init__()
        self.orders = []
        self.steps = []
        self.size = 0

    def next(self):
        txt = ''
        orders_params = self.act
        if orders_params is None:
            return
        
        action = bool(orders_params['Activate'])
        if action and not len(self.orders):
            self.define_grid(orders_params)
            self.set_grid()
            txt = 'Grid Generated'
        elif action and len(self.orders):
            self.update_grid()
            txt = 'Grid Updated'
        elif not action and len(self.orders):
            self.cancel_grid()
            txt = 'Grid removed'                  
        if txt:
            self._add_info('Grid', txt)

    def update_grid(self):
        for order_inx, order in enumerate(self.orders):
            if order.status is order.Completed:
                lvl = order.created.price
                lvl_inx = self.steps.index(lvl)
                try:
                    if order.isbuy():
                            new_lvl = self.steps[lvl_inx + 1]
                            tmp = self.sell(exectype=bt.Order.Limit, price=new_lvl, size=self.size)
                    elif order.issell():
                            new_lvl = self.steps[lvl_inx - 1]
                            tmp = self.buy(exectype=bt.Order.Limit, price=new_lvl, size=self.size) 
                except IndexError:
                    self._add_info('Grid', 'Bad Grid Defined and call out of range lvl')
                self.orders[order_inx] = tmp

    def set_grid(self):
        first_sell = True
        for lvl in self.steps:
            tmp = None
            if lvl < self.data.close[0]:
                tmp = self.buy(exectype=bt.Order.Limit, price=lvl, size=self.size)
            elif first_sell:
                first_sell = False
            else:
                tmp = self.sell(exectype=bt.Order.Limit, price=lvl, size=self.size)

            if tmp is not None:
                self.orders.append(tmp)

    def cancel_grid(self):
        self.close()
        for order in self.orders:
            order.cancel()
        self.steps.clear()
        self.orders.clear()
        self.buy_lvl_limit = 0

    def define_grid(self, orders_params):
        mode = orders_params['mode']
        ngrid = orders_params['Grid']
        self.size = orders_params['each step investment amount'][0]
        low_p, up_p = orders_params['Lower and Upper Prices']
        if up_p > low_p:
            func = self.geometric_grid if mode else self.arithmetic_grid
            self.steps = func(ngrid, up_p, low_p)

    @staticmethod
    def geometric_grid(ngrid, up_p, low_p):
        ratio = (up_p / low_p) ** (1/(ngrid - 1))
        return [low_p * ratio ** i for i in range(ngrid)]

    @staticmethod
    def arithmetic_grid(ngrid, up_p, low_p):
        dif = (up_p - low_p) / (ngrid - 1.)
        return [low_p + i * dif for i in range(ngrid)]
    
    
class GridOrderObserver(bt.observer.Observer):
    buy_lines = tuple(f'b{i}' for i in range(10))  # tuple(f'line{a+1}' for a in range(10))
    sell_lines = tuple(f's{i}' for i in range(10))
    lines = buy_lines + sell_lines

    plotinfo = dict(plot=True, subplot=False, plotlinelabels=False)

    plotlines = {l:dict(marker='>', markersize=1.0, color='yellow', fillstyle='full') for l in sell_lines}
    plotlines.update({l:dict(marker='>', markersize=1.0, color='blue', fillstyle='full') for l in buy_lines})

    def next(self):
        n_b = n_s = 0
        try:
            for order in self._owner.orders:
                if order.isbuy() and n_b < len(self.buy_lines):
                    self.lines[n_b][0] = order.created.price
                    n_b += 1
                elif order.issell() and n_s < len(self.sell_lines):
                    n_s += 1
                    self.lines[-n_s][0] = order.created.price   
        except IndexError:
            pass
        
        
class GymGridStrategyEnv(BasicGymEnv):
    def __init__(self,
    strategy:'BasicGymStrategy',
    data:btfeeds.GenericCSVData,
    *,
    init_cash=10_000,
    base_cash = 10,
    commission=0.000,
    leverage=1
    ):
        super().__init__(
            strategy,
            data,
            init_cash=init_cash,
            base_cash=base_cash,
            commission=commission,
            leverage=leverage
        )
        self.cerebro.addobserver(GridOrderObserver)