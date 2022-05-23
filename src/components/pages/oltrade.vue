<template>
  <div  style="direction:ltr;overflow-x:auto;width:100%;margin:auto; margin-top:70px" v-cloak id="trader">
    <div class="col-12">
      <b-card id="p1" no-body class="mb-3 cardss" style=";height:450px;overflow:auto ; width:24% ; margin-right:1%">
          <b-input v-model="searchtext" placeholder="...جستجو" style="top:0;position:absolute;height:40px; width: 100%;margin:auto;background:transparent;border-style:none;padding:10px;border-radius:0;border-bottom:solid;text-align:right" @input="search()"></b-input>
        <table style="top:40px;position:absolute;text-align:left; color:white;font:14px 'arial';width:100%" class="">
              <tr style="width:100%;background:rgba(0,0,0,0.4);box-sizing:border-box">
                                  <th scope="col" style="width:50%">بازار</th>

                  <th scope="col" style="width:50%">قیمت</th>
              </tr>
              
          <tr v-for="(item,name,idx) in info" v-bind:key="idx" class="btn-cur" :id="`${name}`" @click="click(name)">
                         <td v-if="leverage" style="width:50%"><a :href="`/margin-trade/${name}`" style="color:white" @click="changeroute()" >{{name}} <a style="border-style:solid;border-width:1px;padding:3px;border-color:orange;color:orange;border-radius:5px">{{leverage[name]['leverage']}}X</a></a> </td>
             <td style="width:50%"><a :href="`/margin-trade/${name}`"  style="color:white" @click="changeroute()" > {{item.last}}</a></td>
          </tr>
          
          </table>
        <div>
          <b-card-body class="cardss py-3">
          </b-card-body>
        </div>

      </b-card>
      <div id="p2" class="" style="float:left;height:450px;width:49%; margin-right:1%">
          <b-card no-body class="cardss" style="border-radius: 0!important;height:450px"><br>
            <div style="margin:auto" id="tradingview_1be21"></div>
        <div>
          <b-card-body class="py-3 cardss">
          </b-card-body>
        </div>

      </b-card>
      </div>
      <b-card id="p3" no-body class="mb-3 cardss" style=";height:495px; width:24%; margin-right:1%">
          <h5 style="width:100%;height:40px;background:black;padding:8px;text-align:center;color:#cacadc;margin:0">درخواست های خرید</h5>
          <table v-if="boardinfo.asks"  style="text-align:right; color:white;font:14px 'arial';" class="">
              <tr style="width:100%;background:rgba(0,0,0,0.4);box-sizing:border-box">
                  <th scope="col" style="width:30%">مجموع</th>
                  <th scope="col" style="width:30%">قیمت</th>
                  <th scope="col" style="width:30%">مقدار</th>
              </tr>
          <tr v-for="(item, idx) in boardinfo.bids.slice(0,10)" v-bind:key="idx">
            <td style="width:30%;">{{(item[1] * item[0]).toFixed(2)}}</td>
             <td @click="fillpos(item[0])" style="width:30%;color:green;cursor:pointer">{{item[0]}}</td>
             <td style="width:30%;">{{item[1]}}</td>
          </tr>
          </table>
        <div>
          <b-card-body class="py-3 cardss">
          </b-card-body>
        </div>

      </b-card>
    </div>









    <div style="clear:both"></div>
    <div class="col-12 ">
      <b-card id="p4" no-body class="mb-3  cardss" style=";height:550px;color:white;margin-top:-20px ; width:24%; margin-right:1%">
                      <h4 style="font-family:'arial';width:100%;height:40px;background:black;padding:8px;text-align:center;color:#cacadc">موجودی</h4>
       <table v-if="balances.data"  >
          <tr style="font-family:'arial';font-size:12px">
             <td style="width:50%;text-align:left"> {{parseFloat(balances.data.leverage).toFixed(4)}}</td>
             <td style="width:50%;text-align:right">Leverage</td>
          </tr>
          <tr style="font-family:'arial';font-size:12px">
             <td style="width:50%;text-align:left"> {{parseFloat(balances.data.balance.buy_type).toFixed(4)}}</td>
             <td  style="width:50%;text-align:right">{{balances.data.buy_asset_type}}-Balance </td>
          </tr>
          <tr style="font-family:'arial';font-size:12px">
             <td style="width:50%;text-align:left"> {{parseFloat(balances.data.balance.sell_type).toFixed(4)}}</td>
             <td style="width:50%;text-align:right">{{balances.data.sell_asset_type}}-Balance </td>
          </tr>
          <tr style="font-family:'arial';font-size:12px">
             <td style="width:50%;text-align:left"> {{parseFloat(balances.data.frozen.buy_type).toFixed(4)}}</td>
             <td style="width:50%;text-align:right">{{balances.data.buy_asset_type}}-Frozen </td>
          </tr>
          <tr style="font-family:'arial';font-size:12px">
             <td style="width:50%;text-align:left"> {{parseFloat(balances.data.frozen.sell_type).toFixed(4)}}</td>
             <td style="width:50%;text-align:right">{{balances.data.sell_asset_type}}-Frozen </td>
          </tr>
          <tr style="font-family:'arial';font-size:12px">
             <td style="width:50%;text-align:left"> {{parseFloat(balances.data.loan.buy_type).toFixed(4)}}</td>
             <td style="width:50%;text-align:right">{{balances.data.buy_asset_type}}-Loan </td>
          </tr>
          <tr style="font-family:'arial';font-size:12px">
             <td style="width:50%;text-align:left"> {{parseFloat(balances.data.loan.sell_type).toFixed(4)}}</td>
             <td style="width:50%;text-align:right">{{balances.data.sell_asset_type}}-Loan </td>
          </tr>
          <tr style="font-family:'arial';font-size:12px">
             <td style="width:50%;text-align:left"> {{parseFloat(balances.data.interest.buy_type).toFixed(4)}}</td>
             <td style="width:50%;text-align:right">{{balances.data.buy_asset_type}}-Interest </td>
          </tr>
          <tr style="font-family:'arial';font-size:12px">
             <td style="width:50%;text-align:left"> {{parseFloat(balances.data.interest.sell_type).toFixed(4)}}</td>
             <td style="width:50%;text-align:right">{{balances.data.sell_asset_type}}-Interest </td>
          </tr>
          <tr style="font-family:'arial';font-size:12px">
             <td style="width:50%;text-align:left"> {{parseFloat(balances.data.can_transfer.buy_type).toFixed(4)}}</td>
             <td style="width:50%;text-align:right">{{balances.data.buy_asset_type}}-can transfer </td>
          </tr>
          <tr style="font-family:'arial';font-size:12px">
             <td style="width:50%;text-align:left"> {{parseFloat(balances.data.can_transfer.sell_type).toFixed(4)}}</td>
             <td style="width:50%;text-align:right">{{balances.data.sell_asset_type}}-can transfer </td>
          </tr>
          <tr style="font-family:'arial';font-size:12px">
             <td style="width:50%;text-align:left"> {{parseFloat(liquidation).toFixed(6)}}</td>
             <td style="width:50%;text-align:right">liquidation_price </td>
          </tr>
       </table>
      </b-card>



      <div id="p5" class="" style="float:left;height:580px;margin-top:-20px ; width:49%; margin-right:1%">
          <b-card id="p5-sub" no-body class="cardss" style="border-radius: 0!important;height:550px">
              <h4 style="font-family:'arial';width:100%;height:40px;background:black;padding:6px;text-align:center;color:#cacadc">مرجین</h4>
              <div style="font-family:'arial';margin-top:-10px;width:100%;height:60px;background:rgba(0,0,0,.2);padding:8px;text-align:center;color:#cacadc">
                  <button style="float:left;background:none;border-color:grey;margin:5px;border-radius:3px;padding:3px;padding-left:15px;padding-right:15px;font-family:'arial'"  class="btn btn-light nbile" @click="borrow()">Borrow</button>
                  <button style="float:left;background:none;border-color:grey;margin:5px;border-radius:3px;padding:3px;padding-left:15px;padding-right:15px;font-family:'arial'"  class="btn btn-light nbile" @click="repay()">Repay</button>
                  <button style="float:left;background:none;border-color:grey;margin:5px;border-radius:3px;padding:3px;padding-left:15px;padding-right:15px;font-family:'arial'"  class="btn btn-light nbile" @click="transfer()">Transfer</button>
                    <p v-if="balances.data" style="float:right;background:none;border-color:grey;margin:5px;border-radius:3px;padding:3px;padding-left:15px;padding-right:15px;font:12px 'arial'"  class="alert alert-light"> دارایی لحظه ای<br>{{livebalance.toFixed(4)}} {{balances.data.buy_asset_type}} </p>
                    <p v-if="balances.data" style="float:right;background:none;border-color:grey;margin:5px;border-radius:3px;padding:3px;padding-left:15px;padding-right:15px;font:12px 'arial'"  class="alert alert-light">  قیمت لیکوییدیشن <br>{{liquidation}} {{balances.data.buy_asset_type}} </p>
              </div><br>
              <div style="clear:both"></div>
              <div style="font-family:'arial';width:100%;height:40px;background:none;padding:8px;text-align:center;color:#cacadc">
              <button class="btn btn-warning nbile" style="padding-top : 0px;padding-bottom : 0px;background:none;float:left" v-if="balances.data" disabled>  {{balances.data.leverage}}X</button>
                  <button style="float:right;background:none;border-color:grey;margin:5px;border-radius:3px;padding:3px;padding-left:15px;padding-right:15px;font-family:'arial'" id="limit" @click="tabact('limit')" class="btn btn-light tabss">Limit</button>
                  <button style="float:right;background:none;border-color:grey;margin:5px;border-radius:3px;padding:3px;padding-left:15px;padding-right:15px;font-family:'arial'" id="market" @click="tabact('market')" class="btn btn-light act tabss">Market</button>
                  <button style="float:right;background:none;border-color:grey;margin:5px;border-radius:3px;padding:3px;padding-left:15px;padding-right:15px;font-family:'arial'" id="stop-limit" @click="tabact('stop-limit')" class="btn btn-light tabss">Stop-Limit</button>
              </div><br>
              <div style="clear:both"></div>
              <div class="tabsss market">
                <div class="hundbile" style="width:50%;height:385px;position:absolute;left:0;bottom:0;padding:15px;color:#cacadc" >
                <p><button class="btn btn-warning" style="padding-top : 0px;padding-bottom : 0px;background:none" v-if="balances.data" @click="mbbalance()">  {{parseFloat(this.balances.data.balance.buy_type)}} {{balances.data.buy_asset_type}}</button> : موجودی</p>
                <form @submit.prevent="mbuy()">
                  <div class="input-group mb-3">
                    <div class="input-group-prepend" style="direction:rtl">
                      <span v-if="balances.data" class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-left:none;border-right:none;border-radius:0;border-color:grey;font-family:'arial'; background:rgba(255,255,255,.2)">{{balances.data.buy_asset_type}}</span>
                      <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-right:none;border-radius:0;border-color:grey;color:white;font-family:'arial'; background:rgba(255,255,255,.2)">Price</span>
                    </div>
                    <input readonly disabled placeholder="بهترین قیمت بازار" class="form-control" step="any" aria-label="Default" aria-describedby="inputGroup-sizing-default" type="number"  style="background:none; border-style:solid;border-radius:0;border-color:grey;text-align: right; background:rgba(255,255,255,.2)">
                  </div>
                  <div class="input-group mb-3">
                    <div class="input-group-prepend" style="direction:rtl">
                      <span v-if="balances.data" class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-left:none;border-right:none;border-radius:0;border-color:grey;font-family:'arial'">{{balances.data.buy_asset_type}}</span>
                      <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-right:none;border-radius:0;border-color:grey;color:white;font-family:'arial'">Amount</span>  
                    </div>
                      <input v-if="leverage[$route.params.sym]" v-model="mb_amount" class="form-control"  :max="leverage[$route.params.sym]['smax']" step="any" aria-label="Default" aria-describedby="inputGroup-sizing-default" type="number" style="background:none; border-style:solid;border-radius:0;border-color:grey;text-align: right;font-family:'arial'">
                  </div>
                  <table style="width:98%;margin-left:2%">
                    <tr>
                      <td style="text-align:center; color:white ; font: 12px 'arial'">0%</td>
                      <td style="text-align:center; color:white ; font: 12px 'arial'">25%</td>
                      <td style="text-align:center; color:white ; font: 12px 'arial'">50%</td>
                      <td style="text-align:center; color:white ; font: 12px 'arial'">75%</td>
                      <td style="text-align:center; color:white ; font: 12px 'arial'">100%</td>
                    </tr>
                  </table>
                  <b-form-slider :step="0.00000001" :ticks_tooltip="true" v-if="balances.data" :min="0.00" :max="parseFloat(balances.data.balance.buy_type)" v-model="mb_amount"></b-form-slider>
                  <p v-if="balances.data" style=";font-family:'arial'">  {{mb_amount}}  {{balances.data.buy_asset_type}} : مبلغ کل</p>
                  <br>
                  <input type="submit" value="خرید" class="btn btn-success" style="width:100%;border-radius:0">
                </form>
                </div>





                <div class="hundbile" style="width:50%;height:385px;position:absolute;right:0;bottom:0;padding:15px;color:#cacadc">
                  <p><button class="btn btn-warning" style="padding-top : 0px;padding-bottom : 0px;background:none" v-if="balances.data" @click="msbalance()"> {{(balances.data.balance.sell_type)}} {{balances.data.sell_asset_type}} </button> : موجودی</p>
                  <form @submit.prevent="msell()">
                    <div class="input-group mb-3">
                      <div class="input-group-prepend" style="direction:rtl">
                        <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-left:none;border-right:none;border-radius:0;border-color:grey;font-family:'arial'; background:rgba(255,255,255,.2)">USDT</span>
                        <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-right:none;border-radius:0;border-color:grey;color:white;font-family:'arial'; background:rgba(255,255,255,.2)">Price</span>
                      </div>
                      <input readonly disabled placeholder="بهترین قیمت بازار" class="form-control" step="any" aria-label="Default" aria-describedby="inputGroup-sizing-default" type="number"  style="background:none; border-style:solid;border-radius:0;border-color:grey; text-align:right; background:rgba(255,255,255,.2)">
                    </div>
                    <div class="input-group mb-3">
                      <div class="input-group-prepend" style="direction:rtl">
                        <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-left:none;border-right:none;border-radius:0;border-color:grey;font-family:'arial'" v-if="balances.data">{{balances.data.sell_asset_type}}</span>
                        <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-right:none;border-radius:0;border-color:grey;color:white;font-family:'arial'">Amount</span>  
                      </div>
                        <input v-if="leverage[$route.params.sym]" v-model="ms_amount"  :max="parseFloat(leverage[$route.params.sym]['bmax'])" class="form-control" step="any" aria-label="Default" aria-describedby="inputGroup-sizing-default" type="number" style="background:none; border-style:solid;border-radius:0;border-color:grey;text-align: right;font-family:'arial'">
                    </div>
                    <table style="width:98%;margin-left:2%">
                      <tr>
                        <td style="text-align:center; color:white ; font: 12px 'arial'">0%</td>
                        <td style="text-align:center; color:white ; font: 12px 'arial'">25%</td>
                        <td style="text-align:center; color:white ; font: 12px 'arial'">50%</td>
                        <td style="text-align:center; color:white ; font: 12px 'arial'">75%</td>
                        <td style="text-align:center; color:white ; font: 12px 'arial'">100%</td>
                      </tr>
                    </table>
                    <b-form-slider :step="0.00000001" :ticks_tooltip="true" v-if="balances.data" :min="0.0000000" :max="parseFloat(balances.data.balance.sell_type)" v-model="ms_amount"></b-form-slider>
                    <p style=";font-family:'arial'">  ~~ USDT : مبلغ کل</p>
                    <br>
                    <input type="submit" value="فروش" class="btn btn-danger" style="width:100%;border-radius:0">
                  </form>
                </div>
              </div>





              <div class="tabsss limit" style="display:none">
                  <div class="hundbile" style="width:50%;height:385px;position:absolute;left:0;bottom:0;padding:15px;color:#cacadc" >
                    <p><button class="btn btn-warning" style="padding-top : 0px;padding-bottom : 0px;background:none" v-if="balances.data" @click="lbbalance()">  {{balances.data.balance.buy_type}} {{balances.data.buy_asset_type}}</button> : موجودی</p>
                    <form @submit.prevent="lbuy()">
                      <div class="input-group mb-3">
                        <div class="input-group-prepend" style="direction:rtl">
                          <span v-if="balances.data" class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-left:none;border-right:none;border-radius:0;border-color:grey;font-family:'arial'; ">{{balances.data.buy_asset_type}}</span>
                          <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-right:none;border-radius:0;border-color:grey;color:white;font-family:'arial'; ">Price</span>
                        </div>
                        <input v-model="lb_price" class="form-control" @input="lb_allset" step="any" aria-label="Default" aria-describedby="inputGroup-sizing-default" type="number"  style="background:none; border-style:solid;border-radius:0;border-color:grey;text-align: right;font-family:'arial'">
                      </div>
                      <div class="input-group mb-3">
                        <div class="input-group-prepend" style="direction:rtl">
                          <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-left:none;border-right:none;border-radius:0;border-color:grey;font-family:'arial'" v-if="balances.data">{{balances.data.sell_asset_type}}</span>
                          <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-right:none;border-radius:0;border-color:grey;color:white;font-family:'arial'">Amount</span>  
                        </div>
                          <input v-if="leverage[$route.params.sym]" @input="lb_allset" v-model="lb_amount"  :max="parseFloat(leverage[$route.params.sym]['bmax'])" class="form-control" step="any" aria-label="Default" aria-describedby="inputGroup-sizing-default" type="number" style="background:none; border-style:solid;border-radius:0;border-color:grey;text-align: right;font-family:'arial'">
                      </div>
                      <table style="width:98%;margin-left:2%">
                    <tr>
                      <td style="text-align:center; color:white ; font: 12px 'arial'">0%</td>
                      <td style="text-align:center; color:white ; font: 12px 'arial'">25%</td>
                      <td style="text-align:center; color:white ; font: 12px 'arial'">50%</td>
                      <td style="text-align:center; color:white ; font: 12px 'arial'">75%</td>
                      <td style="text-align:center; color:white ; font: 12px 'arial'">100%</td>
                    </tr>
                  </table>
                  <b-form-slider :step="0.00000001" :ticks_tooltip="true" v-if="balances.data" :min="0.00" @slide-stop="lbslide" :max="parseFloat(balances.data.balance.buy_type)" v-model="lb_all"></b-form-slider>
                      <p v-if="balances.data" style=";font-family:'arial'">  {{lb_all}}  {{balances.data.buy_asset_type}} : مبلغ کل</p>
                      <br>
                      <input type="submit" value="خرید" class="btn btn-success" style="width:100%;border-radius:0">
                    </form>
                  </div>
                  <div class="hundbile" style="width:50%;height:385px;position:absolute;right:0;bottom:0;padding:15px;color:#cacadc">
                    <p><button class="btn btn-warning" style="padding-top : 0px;padding-bottom : 0px;background:none" v-if="balances.data" @click="lsbalance()"> {{balances.data.balance.sell_type}} {{balances.data.sell_asset_type}} </button> : موجودی</p>
                    <form @submit.prevent="lsell()">
                      <div class="input-group mb-3">
                      <div class="input-group-prepend" style="direction:rtl">
                          <span v-if="balances.data" class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-left:none;border-right:none;border-radius:0;border-color:grey;font-family:'arial'; ">{{balances.data.buy_asset_type}}</span>
                        <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-right:none;border-radius:0;border-color:grey;color:white;font-family:'arial'; ">Price</span>
                      </div>
                      <input v-model="ls_price" class="form-control" step="any" aria-label="Default" aria-describedby="inputGroup-sizing-default" type="number"  style="background:none; border-style:solid;border-radius:0;border-color:grey; text-align:right;font-family:'arial' ">
                    </div>
                
                      <div class="input-group mb-3">
                        <div class="input-group-prepend" style="direction:rtl">
                          <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-left:none;border-right:none;border-radius:0;border-color:grey;font-family:'arial'" v-if="balances.data">{{balances.data.sell_asset_type}}</span>
                          <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-right:none;border-radius:0;border-color:grey;color:white;font-family:'arial'">Amount</span>  
                        </div>
                        <input v-if="leverage[$route.params.sym]" v-model="ls_amount"  :max="parseFloat(leverage[$route.params.sym]['bmax'])" class="form-control" step="any" aria-label="Default" aria-describedby="inputGroup-sizing-default" type="number" style="background:none; border-style:solid;border-radius:0;border-color:grey;text-align: right;font-family:'arial'">
                      </div>
                      <table style="width:98%;margin-left:2%">
                    <tr>
                      <td style="text-align:center; color:white ; font: 12px 'arial'">0%</td>
                      <td style="text-align:center; color:white ; font: 12px 'arial'">25%</td>
                      <td style="text-align:center; color:white ; font: 12px 'arial'">50%</td>
                      <td style="text-align:center; color:white ; font: 12px 'arial'">75%</td>
                      <td style="text-align:center; color:white ; font: 12px 'arial'">100%</td>
                    </tr>
                  </table>
                  <b-form-slider :step="0.00000001" :ticks_tooltip="true" v-if="balances.data" :min="0.000000000" :max="parseFloat(balances.data.balance.sell_type)" v-model="ls_amount"></b-form-slider>
                      <p v-if="balances.data" style=";font-family:'arial'"> {{ls_amount * ls_price}} {{balances.data.buy_asset_type}} : مبلغ کل</p>
                      <br>
                      <input type="submit" value="فروش" class="btn btn-danger" style="width:100%;border-radius:0">
                    </form>
                  </div>
              </div>



              <div class="tabsss stop-limit" style="display:none">
              <div class="hundbile" style="width:50%;height:385px;position:absolute;left:0;bottom:0;padding:15px;color:#cacadc" >
               <p><button class="btn btn-warning" style="padding-top : 0px;padding-bottom : 0px;background:none" v-if="balances.data" @click="lsbbalance()">  {{balances.data.balance.buy_type}} {{balances.data.buy_asset_type}}</button> : موجودی</p>
              <form @submit.prevent="lsbuy()">



                <div class="input-group mb-3">
                  <div class="input-group-prepend" style="direction:rtl">
                    <span v-if="balances.data" class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-left:none;border-right:none;border-radius:0;border-color:grey;font-family:'arial'; ">{{balances.data.buy_asset_type}}</span>
                    <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-right:none;border-radius:0;border-color:grey;color:white;font-family:'arial'; ">Stop</span>
                  </div>
                  <input v-model="lsb_stop" class="form-control" step="any" aria-label="Default" aria-describedby="inputGroup-sizing-default" type="number"  style="background:none; border-style:solid;border-radius:0;border-color:grey;text-align: right;font-family:'arial'">
                </div>



                <div class="input-group mb-3">
                  <div class="input-group-prepend" style="direction:rtl">
                    <span v-if="balances.data" class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-left:none;border-right:none;border-radius:0;border-color:grey;font-family:'arial'">{{balances.data.buy_asset_type}}</span>
                    <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-right:none;border-radius:0;border-color:grey;color:white;font-family:'arial'">Limit</span>  
                  </div>
                    <input v-model="lsb_limit" class="form-control" step="any" aria-label="Default" aria-describedby="inputGroup-sizing-default" type="number" style="background:none; border-style:solid;border-radius:0;border-color:grey;text-align: right;font-family:'arial'">
                </div>




                <div class="input-group mb-3">
                  <div class="input-group-prepend" style="direction:rtl">
                    <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-left:none;border-right:none;border-radius:0;border-color:grey;font-family:'arial'" v-if="balances.data">{{balances.data.sell_asset_type}}</span>
                    <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-right:none;border-radius:0;border-color:grey;color:white;font-family:'arial'">Amount</span>  
                  </div>
                    <input v-if="leverage[$route.params.sym]" v-model="lsb_amount"  :max="parseFloat(leverage[$route.params.sym]['bmax'])" class="form-control" step="any" aria-label="Default" aria-describedby="inputGroup-sizing-default" type="number" style="background:none; border-style:solid;border-radius:0;border-color:grey;text-align: right;font-family:'arial'">
                </div>
                <table style="width:98%;margin-left:2%">
                    <tr>
                      <td style="text-align:center; color:white ; font: 12px 'arial'">0%</td>
                      <td style="text-align:center; color:white ; font: 12px 'arial'">25%</td>
                      <td style="text-align:center; color:white ; font: 12px 'arial'">50%</td>
                      <td style="text-align:center; color:white ; font: 12px 'arial'">75%</td>
                      <td style="text-align:center; color:white ; font: 12px 'arial'">100%</td>
                    </tr>
                  </table>
                  <b-form-slider :step="0.00000001" :ticks_tooltip="true" v-if="balances.data" @silde-stop="lsbslide" :min="0.00" :max="parseFloat(balances.data.balance.buy_type)" v-model="lsb_all"></b-form-slider>



                <p v-if="balances.data" style=";font-family:'arial'">  {{lsb_all}}  {{balances.data.buy_asset_type}} : مبلغ کل</p>
                <br>
                <input type="submit" value="خرید" class="btn btn-success" style="width:100%;border-radius:0">
              </form>
              </div>
              <div class="hundbile" style="width:50%;height:385px;position:absolute;right:0;bottom:0;padding:15px;color:#cacadc">
               <p><button class="btn btn-warning" style="padding-top : 0px;padding-bottom : 0px;background:none" v-if="balances.data" @click="lssbalance()"> {{balances.data.balance.sell_type}} {{balances.data.sell_asset_type}} </button> : موجودی</p>
               <form @submit.prevent="lssell()">



                  <div class="input-group mb-3">
                    <div class="input-group-prepend" style="direction:rtl">
                      <span v-if="balances.data" class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-left:none;border-right:none;border-radius:0;border-color:grey;font-family:'arial'; ">{{balances.data.buy_asset_type}}</span>
                      <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-right:none;border-radius:0;border-color:grey;color:white;font-family:'arial'; ">Stop</span>
                    </div>
                    <input v-model="lss_stop" class="form-control" step="any" aria-label="Default" aria-describedby="inputGroup-sizing-default" type="number"  style="background:none; border-style:solid;border-radius:0;border-color:grey; text-align:right;font-family:'arial' ">
                  </div>


                                
                  <div class="input-group mb-3">
                    <div class="input-group-prepend" style="direction:rtl">
                      <span v-if="balances.data" class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-left:none;border-right:none;border-radius:0;border-color:grey;font-family:'arial'">{{balances.data.buy_asset_type}}</span>
                      <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-right:none;border-radius:0;border-color:grey;color:white;font-family:'arial'">Limit</span>  </div>
                    <input v-model="lss_limit" class="form-control" step="any" aria-label="Default" aria-describedby="inputGroup-sizing-default" type="number" style="background:none; border-style:solid;border-radius:0;border-color:grey;text-align: right;font-family:'arial'">
                  </div>




                  <div class="input-group mb-3">
                    <div class="input-group-prepend" style="direction:rtl">
                              <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-left:none;border-right:none;border-radius:0;border-color:grey;font-family:'arial'" v-if="balances.data">{{balances.data.sell_asset_type}}</span>
                      <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-right:none;border-radius:0;border-color:grey;color:white;font-family:'arial'">Amount</span>  </div>
                    <input v-if="leverage[$route.params.sym]" v-model="lss_amount"  :max="parseFloat(leverage[$route.params.sym]['bmax'])" class="form-control" step="any" aria-label="Default" aria-describedby="inputGroup-sizing-default" type="number" style="background:none; border-style:solid;border-radius:0;border-color:grey;text-align: right;font-family:'arial'">
                  </div>
                  <table style="width:98%;margin-left:2%">
                    <tr>
                      <td style="text-align:center; color:white ; font: 12px 'arial'">0%</td>
                      <td style="text-align:center; color:white ; font: 12px 'arial'">25%</td>
                      <td style="text-align:center; color:white ; font: 12px 'arial'">50%</td>
                      <td style="text-align:center; color:white ; font: 12px 'arial'">75%</td>
                      <td style="text-align:center; color:white ; font: 12px 'arial'">100%</td>
                    </tr>
                  </table>
                  <b-form-slider :step="0.00000001" :ticks_tooltip="true" v-if="balances.data" :min="0.000000000" :max="parseFloat(balances.data.balance.sell_type)" v-model="lss_amount"></b-form-slider>



                  <p v-if="balances.data" style=";font-family:'arial'"> {{lss_amount * lss_limit}} {{balances.data.buy_asset_type}} : مبلغ کل</p>
                  <br>
                  <input type="submit" value="فروش" class="btn btn-danger" style="width:100%;border-radius:0">
               </form>
              </div>
              </div>
      </b-card>
      </div>
      <b-card id="p6" no-body class="mb-3 cardss" style=";height:570px;margin-top:-40px ; width:24%; margin-right:1%">
        <h1 style="width:100%;height:60px;background:rgba(0,0,0,0.4);padding:8px;text-align:left;color:#cacadc;margin:0;color:green">{{boardinfo.last}} <br></h1>
          <h5 style="width:100%;height:40px;background:black;padding:8px;text-align:center;color:#cacadc;margin:0">درخواست های فروش</h5>
          <table v-if="boardinfo.bids"  style="text-align:right; color:white;font:14px 'arial';" class="">
              <tr style="width:100%;background:rgba(0,0,0,0.4);box-sizing:border-box">
                  <th scope="col" style="width:30%">مجموع</th>
                  <th scope="col" style="width:30%">قیمت</th>
                  <th scope="col" style="width:30%">مقدار</th>
              </tr>
          <tr v-for="(item, idx) in boardinfo.asks.slice(0,10)" v-bind:key="idx">
            <td style="width:30%;">{{(item[1] * item[0]).toFixed(2)}}</td>
             <td @click="fillneg(item[0])" style="width:30%;color:red;font-family:'arial';cursor:pointer">{{item[0]}}</td>
             <td style="width:30%;">{{item[1]}}</td>
          </tr>
          </table>
        <div>
          <b-card-body class="py-3">
          </b-card-body>
        </div>

      </b-card>
    </div>
    
    <div style="clear:both"></div>
    <div class="col-12"  id="hist">
      <b-tabs no-body class="col-12 cardss nbile" style="height:auto;margin-bottom:50px">
        <b-tab title="سفارشات باز" style="width:100%">
        <h5 style="width:100%;height:4px;background:black;padding:0px;text-align:center;color:#cacadc;margin:0"></h5>
          <table style="text-align:right; color:white;font:14px 'arial';width:100%" class="">
              <tr style="width:100%;background:rgba(0,0,0,0.4);box-sizing:border-box">
                  <th scope="col" style="width:12% ; text-align:center">زمان معامله</th>
                  <th scope="col" style="width:12% ; text-align:center">قرارداد</th>
                  <th scope="col" style="width:12% ; text-align:center">نوع</th>
                  <th scope="col" style="width:12% ; text-align:center">جهت</th>
                  <th scope="col" style="width:12% ; text-align:center">انجام نشده</th>
                  <th scope="col" style="width:12% ; text-align:center">انجام شده</th>
                  <th scope="col" style="width:12% ; text-align:center">میانگین قیمت</th>
                  <th scope="col" style="width:7% ; text-align:center">قیمت</th>
                  <th scope="col" style="width:16% ; text-align:center">عملیات</th>
              </tr>
              <tr v-for="(item,idx) in pending" v-bind:key="idx" style="height:100px;font-weight:bold">

                  <td style="width:11% ; text-align:center ; color:green" v-if="item.type == 'buy'">{{strftime("%m/%d/%y %H:%M:%S",item.create_time)}}</td>
                  <td style="width:11% ; text-align:center ; color:green" v-if="item.type == 'buy'">{{item.market}}</td>      
                  <td style="width:11% ; text-align:center ; color:green" v-if="item.type == 'buy'">{{item.order_type}}</td>
                  <td style="width:11% ; text-align:center ; color:green" v-if="item.type == 'buy'">{{String(item.type).replace('sell','فروش').replace('buy','خرید')}}</td>
                  <td style="width:11% ; text-align:center ; color:green" v-if="item.type == 'buy'">{{(parseFloat(item.left))}}</td>
                  <td style="width:11% ; text-align:center ; color:green" v-if="item.type == 'buy'">{{(parseFloat(item.amount) - parseFloat(item.left))}}</td>
                  <td style="width:11% ; text-align:center ; color:green" v-if="item.type == 'buy'">{{item.avg_price}}</td>
                  <td style="width:7% ; text-align:center ; color:green" v-if="item.type == 'buy'">{{item.price}}</td>



                  <td style="width:11% ; text-align:center ; color:red" v-if="item.type == 'sell'">{{strftime("%m/%d/%y %H:%M:%S",item.create_time)}}</td>
                  <td style="width:11% ; text-align:center ; color:red" v-if="item.type == 'sell'">{{item.market}}</td>      
                  <td style="width:11% ; text-align:center ; color:red" v-if="item.type == 'sell'">{{item.order_type}}</td>
                  <td style="width:11% ; text-align:center ; color:red" v-if="item.type == 'sell'">{{String(item.type).replace('sell','فروش').replace('buy','خرید')}}</td>
                  <td style="width:11% ; text-align:center ; color:red" v-if="item.type == 'sell'">{{(parseFloat(item.left))}}</td>
                  <td style="width:11% ; text-align:center ; color:red" v-if="item.type == 'sell'">{{(parseFloat(item.amount) - parseFloat(item.left))}}</td>
                  <td style="width:11% ; text-align:center ; color:red" v-if="item.type == 'sell'">{{item.avg_price}}</td>
                  <td style="width:7% ; text-align:center ; color:red" v-if="item.type == 'sell'">{{item.price}}</td>
                  <td style="width:16% ; text-align:center ; color:red"><button class="btn btn-danger" @click="cancel(item.id)">لغو سفارش</button></td>
              </tr>
              <tr v-if="!pending" style="height:100px">
                <th colspan="9" style="text-align:center">موردی یافت نشد</th>
              </tr>
          </table>
      </b-tab>
      <b-tab title="(استاپ) سفارشات باز" style="height:auto;margin-bottom:50px;width:100%">
        <h5 style="width:100%;height:4px;background:black;padding:0px;text-align:center;color:#cacadc;margin:0"></h5>
          <table style="text-align:right; color:white;font:14px 'arial';width:100%" class="">
              <tr style="width:100%;background:rgba(0,0,0,0.4);box-sizing:border-box">
                  <th scope="col" style="width:12% ; text-align:center">زمان معامله</th>
                  <th scope="col" style="width:12% ; text-align:center">قرارداد</th>
                  <th scope="col" style="width:12% ; text-align:center">نوع</th>
                  <th scope="col" style="width:12% ; text-align:center">جهت</th>
                  <th scope="col" style="width:12% ; text-align:center">قیمت</th>
                  <th scope="col" style="width:12% ; text-align:center"> قیمت استاپ</th>
                  <th scope="col" style="width:12% ; text-align:center"> مقدار</th>
                  <th scope="col" style="width:16% ; text-align:center">عملیات</th>
              </tr>
              <tr v-for="(item,idx) in spending" v-bind:key="idx" style="height:100px;font-weight:bold">

                  <td style="width:12% ; text-align:center ; color:green" v-if="item.type == 'buy'">{{strftime("%m/%d/%y %H:%M:%S",item.create_time)}}</td>
                  <td style="width:12% ; text-align:center ; color:green" v-if="item.type == 'buy'">{{item.market}}</td>      
                  <td style="width:12% ; text-align:center ; color:green" v-if="item.type == 'buy'">{{item.order_type}}</td>
                  <td style="width:12% ; text-align:center ; color:green" v-if="item.type == 'buy'">{{String(item.type).replace('sell','فروش').replace('buy','خرید')}}</td>
                  <td style="width:12% ; text-align:center ; color:green" v-if="item.type == 'buy'">{{item.price}}</td>
                  <td style="width:12% ; text-align:center ; color:green" v-if="item.type == 'buy'">{{item.stop_price}}</td>
                  <td style="width:12% ; text-align:center ; color:green" v-if="item.type == 'buy'">{{item.amount}}</td>


                  <td style="width:12% ; text-align:center ; color:red" v-if="item.type == 'sell'">{{strftime("%m/%d/%y %H:%M:%S",item.create_time)}}</td>
                  <td style="width:12% ; text-align:center ; color:red" v-if="item.type == 'sell'">{{item.market}}</td>      
                  <td style="width:12% ; text-align:center ; color:red" v-if="item.type == 'sell'">{{item.order_type}}</td>
                  <td style="width:12% ; text-align:center ; color:red" v-if="item.type == 'sell'">{{String(item.type).replace('sell','فروش').replace('buy','خرید')}}</td>
                  <td style="width:12% ; text-align:center ; color:red" v-if="item.type == 'sell'">{{item.price}}</td>
                  <td style="width:12% ; text-align:center ; color:red" v-if="item.type == 'sell'">{{item.stop_price}}</td>
                  <td style="width:12% ; text-align:center ; color:red" v-if="item.type == 'sell'">{{item.amount}}</td>
                  <td style="width:16% ; text-align:center ; color:red"><button class="btn btn-danger" @click="scancel(item.order_id)">لغو سفارش</button></td>
              </tr>
              <tr v-if="!spending" style="height:100px">
                <th colspan="9" style="text-align:center">موردی یافت نشد</th>
              </tr>
          </table>
      </b-tab>
      </b-tabs>
      <b-tabs no-body class="col-12 cardss nbile" style="height:auto;margin-bottom:50px">
        




          <b-tab title="سابقه سفارشات" class="cardss">
        <div style="width:100%;height:1px;background:black;padding:2px;text-align:center;color:#cacadc;margin:0"></div>          
          <table style="text-align:right; color:white;font:14px 'arial';width:100%" class="">
              <tr style="width:100%;background:rgba(0,0,0,0.4);box-sizing:border-box">
                  <th scope="col" style="width:14% ; text-align:center">زمان معامله</th>
                  <th scope="col" style="width:14% ; text-align:center">مقدار</th>
                  <th scope="col" style="width:14% ; text-align:center">میانگین قیمت</th>
                  <th scope="col" style="width:14% ; text-align:center">قرارداد</th>
                  <th scope="col" style="width:14% ; text-align:center">نوع</th>
                  <th scope="col" style="width:14% ; text-align:center">باقی مانده</th>
              </tr>
              <tr v-if="!finished" style="height:100px">
                <th  colspan="7" style="text-align:center">موردی یافت نشد</th>
              </tr>
              <tr v-for="(item,idx) in finished" v-bind:key="idx" style="height:100px;font-weight:bold">
                  <td style="width:14% ; text-align:center ; color:red" v-if="item.type == 'sell'">{{Date(item.create_time)}}</td>
                  <td style="width:14% ; text-align:center ; color:red" v-if="item.type == 'sell'">{{item.deal_amount}}</td>
                  <td style="width:14% ; text-align:center ; color:red" v-if="item.type == 'sell'">{{parseFloat(item.avg_price).toFixed(2)}}</td>
                  <td style="width:14% ; text-align:center ; color:red" v-if="item.type == 'sell'">{{item.market}}</td>
                  <td style="width:14% ; text-align:center ; color:red" v-if="item.type == 'sell'">{{String(item.type).replace('sell','فروش').replace('buy','خرید')}}</td>

                  <td style="width:14% ; text-align:center ; color:red" v-if="item.type == 'sell'">{{item.left}}</td>
                  



                  <td style="width:14% ; text-align:center ; color:green" v-if="item.type == 'buy'">{{Date(item.create_time)}}</td>
                  <td style="width:14% ; text-align:center ; color:green" v-if="item.type == 'buy'">{{item.deal_amount}}</td>
                  <td style="width:14% ; text-align:center ; color:green" v-if="item.type == 'buy'">{{parseFloat(item.avg_price).toFixed(2)}}</td>
                  <td style="width:14% ; text-align:center ; color:green" v-if="item.type == 'buy'">{{item.market}}</td>
                  <td style="width:14% ; text-align:center ; color:green" v-if="item.type == 'buy'">{{String(item.type).replace('sell','فروش').replace('buy','خرید')}}</td>
                  <td style="width:14% ; text-align:center ; color:green" v-if="item.type == 'buy'">{{item.left}}</td>
              </tr>
          </table>
          </b-tab>
           <b-tab title="(استاپ) سابقه سفارشات" class="cardss">
        <div style="width:100%;height:1px;background:black;padding:2px;text-align:center;color:#cacadc;margin:0"></div>          
          <table style="text-align:right; color:white;font:14px 'arial';width:100%" class="">
              <tr style="width:100%;background:rgba(0,0,0,0.4);box-sizing:border-box">
                  <th scope="col" style="width:14% ; text-align:center">زمان معامله</th>
                  <th scope="col" style="width:14% ; text-align:center">مقدار</th>
                  <th scope="col" style="width:14% ; text-align:center">میانگین قیمت</th>
                  <th scope="col" style="width:14% ; text-align:center">قرارداد</th>
                  <th scope="col" style="width:14% ; text-align:center">نوع</th>
                  <th scope="col" style="width:14% ; text-align:center">باقی مانده</th>
              </tr>
              <tr v-if="!finished" style="height:100px">
                <th  colspan="7" style="text-align:center">موردی یافت نشد</th>
              </tr>
              <tr v-for="(item,idx) in sfinished" v-bind:key="idx" style="height:100px;font-weight:bold">
                  <td style="width:14% ; text-align:center ; color:red" v-if="item.type == 'sell'">{{Date(item.create_time)}}</td>
                  <td style="width:14% ; text-align:center ; color:red" v-if="item.type == 'sell'">{{item.deal_amount}}</td>
                  <td style="width:14% ; text-align:center ; color:red" v-if="item.type == 'sell'">{{parseFloat(item.avg_price).toFixed(2)}}</td>
                  <td style="width:14% ; text-align:center ; color:red" v-if="item.type == 'sell'">{{item.market}}</td>
                  <td style="width:14% ; text-align:center ; color:red" v-if="item.type == 'sell'">{{String(item.type).replace('sell','فروش').replace('buy','خرید')}}</td>

                  <td style="width:14% ; text-align:center ; color:red" v-if="item.type == 'sell'">{{item.left}}</td>
                  



                  <td style="width:14% ; text-align:center ; color:green" v-if="item.type == 'buy'">{{Date(item.create_time)}}</td>
                  <td style="width:14% ; text-align:center ; color:green" v-if="item.type == 'buy'">{{item.deal_amount}}</td>
                  <td style="width:14% ; text-align:center ; color:green" v-if="item.type == 'buy'">{{parseFloat(item.avg_price).toFixed(2)}}</td>
                  <td style="width:14% ; text-align:center ; color:green" v-if="item.type == 'buy'">{{item.market}}</td>
                  <td style="width:14% ; text-align:center ; color:green" v-if="item.type == 'buy'">{{String(item.type).replace('sell','فروش').replace('buy','خرید')}}</td>
                  <td style="width:14% ; text-align:center ; color:green" v-if="item.type == 'buy'">{{item.left}}</td>
              </tr>
          </table>
          </b-tab>



      </b-tabs>
    </div>
    <div style="clear:both"></div>
    <div class="col-12">
    </div>
    

  </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'
import './tv'
import bFormSlider from 'vue-bootstrap-slider/es/form-slider';
import 'bootstrap-slider/dist/css/bootstrap-slider.css'
export default {
  name: 'pages-forums-list',
  metaInfo: {
    title: 'Forum list - Pages'
  },
  updated(){
  },
  data: () => ({
    coinex: '',
    value: 5,
    searchtext: '',
    info: [],
    infoback: [],
    balance: 0,
    boardinfo: [],
    balances: [],
    borrowamount : 0,
    borrowcoin: '',
    b_price: 0,
    lb_amount: 0,
    lb_all: 0,
    ls_amount: 0,
    lb_price: 0,
    ls_price: 0,
    lsb_amount: 0,
    lss_amount: 0,
    lsb_stop: 0,
    lss_stop: 0,
    lsb_limit: 0,
    lsb_all: 0,
    transa: '',
    transb: '',
    transamount: 0,
    lss_limit: 0,
    mb_amount: 0,
    s_price: 0,
    ms_amount: 0,
    transresult : '',
    tvwidth: 550,
    pending: [],
    spending: [],
    repaybuymax: 0,
    repaysellmax: 0,
    repaybuymax2: 0,
    repaysellmax2: 0,
    repayamount: 0,
    repaycoin: '',
    finished: [],
    alert2: '',
    liquidation: 0,
    sfinished: [],
    mid: 0,
    leverage: [],
    wallets: [],
    transfrom: 0,
    livebalance:0,
    op: {
    },
  }),
  beforeMount(){
    this.check()
    this.checklevel()
  },
  mounted () {
    this.getbal(true)
    this.getc()
    this.getb()
    this.getlev()
    this.getw()
    this.tv()
  },
  beforeCreate () {
  },
  components: {
  },
  watch: {
    alert2: (val)=>{
      alert(val)
    },
    lb_all: {
        handler: function() {
            this.lbslide();
        },
        deep: true
      },
    lsb_all: {
        handler: function() {
            this.lsbslide();
        },
        deep: true
      }
  },
  methods: {
    liqu() {
     this.liquidation = ((this.repaybuymax2 * 1.0185 + Number(this.balances.data.interest.buy_type) - Number(this.balances.data.balance.buy_type))/(Number(this.balances.data.balance.sell_type) - Number(this.balances.data.interest.sell_type) - this.repaysellmax2 * 1.0185)).toFixed(6)
     if(this.liquidation <= 0){
       this.liquidation = '--'
     }
    },
    async livebalances(){
      await axios
        .post('/cp_borrowlist' , {market: this.$route.params.sym})
        .then(response => {
          var allbalance = Number(this.balances.data.balance.buy_type) + (Number(this.balances.data.balance.sell_type) * Number(this.info[this.$route.params.sym].last))
          var repaybuymax = 0
          var repaysellmax = 0
          this.repaybuymax2 = 0
          this.repaysellmax2 = 0
          for (var item of response.data.data){
            if(item.coin_type === this.balances.data.buy_asset_type){
              repaybuymax += Number(item.unflat_amount)
              this.repaybuymax2 += Number(item.unflat_amount)
            }else {
              repaysellmax += Number(item.unflat_amount)
              this.repaysellmax2 += Number(item.unflat_amount)
            }
          }
          this.livebalance = allbalance - (repaybuymax + (repaysellmax * Number(this.info[this.$route.params.sym].last)))
          this.liqu()
      })
    },
    lb_allset(){
      this.lb_all = this.lb_price * this.lb_amount
    },
    lsb_allset(){
      this.lsb_all = this.lsb_limit * this.lsb_amount
    },
    lsb_allset(){
      this.lsb_all = this.lb_price * this.lb_amount
    },
    fillneg(a) {
      this.lb_price = a
      this.lsb_limit = a
    },
    fillpos(a) {
      this.ls_price = a
      this.lss_limit = a
    },
    async getw () {
      await axios
        .get('/cp_wallets')
        .then(response => {
          this.wallets = response.data
        }).then(() => {
        })
    },
    check () {
      if (!this.$store.state.isAuthenticated) {
        const toPath = this.$route.query.to || '/login'
        this.$router.push(toPath)
      }
    },
    async checklevel (id) {
      await axios
        .get('/userinfo')
        .then(response => {
          if (response.data[0].level === 0) {
            this.$swal.fire({
              title: 'توجه',
              text: 'برای استفاده از این بخش ابتدا احراز هویت را کامل کنید',
              icon: 'warning',
              showCancelButton: true,
              confirmButtonColor: '#3085d6',
              cancelButtonColor: '#d33',
              confirmButtonText: 'شروع تایید هویت',
              cancelButtonText: 'بعدا انجام میدهم'
            }).then(result => {
              if (result.isConfirmed) {
                const toPath = this.$route.query.to || '/user-level'
                this.$router.push(toPath)
              }else {
                const toPath = this.$route.query.to || '/dashboard'
                this.$router.push(toPath)
              }
            })
          }
        })
    },
    tv () {      
      if(window.innerWidth < 1024){
        this.tvwidth = parseInt(window.innerWidth * .9)
      }else{
        this.tvwidth = parseInt(window.innerWidth / 2.3)
      }
      window.addEventListener('resize' ,() => {
        var fun = this.tv
        var timeOutFunctionId;

        function workAfterResizeIsDone() {
            fun()
        }

        window.addEventListener("resize", function() {

            clearTimeout(timeOutFunctionId);

            timeOutFunctionId = setTimeout(workAfterResizeIsDone, 500);
        });
        
      })
      new TradingView.widget(
        {
        "width": this.tvwidth,
        "height": 390,
        "symbol": `COINEX:${this.$route.params.sym}`,
        "timezone": "Etc/UTC",
        "theme": "dark",
        "style": "1",
        "locale": "en",
        "hide_side_toolbar": false,
        "enable_publishing": false,
        "allow_symbol_change": true,
        "container_id": "tradingview_1be21"
      }
  );
    },
    async getp () {
      await axios
        .post('/cp_pending', {sym: this.$route.params.sym , mid: this.mid})
        .then(response => {
          this.pending = response.data.data
          setTimeout(() => {
            this.getp()
          }, 5000)
        })
    },
    async getsp () {
      await axios
        .post('/cp_stop_pending', {sym: this.$route.params.sym , mid: this.mid})
        .then(response => {
          this.spending = response.data.data
          setTimeout(() => {
            this.getsp()
          }, 5000)
        })
    },
    async getlev () {
      await axios
        .get('/leverages')
        .then(response => {
          this.leverage = response.data
        })
    },
    click (name) {
      document.getElementById(name).querySelector('a').click()
    },
    async getf () {
      await axios
        .post('/cp_finished', {sym: this.$route.params.sym , mid: this.mid})
        .then(response => {
          this.finished = response.data.data
          setTimeout(() => {
            this.getf()
          }, 2000)
        })
    },
    async getsf () {
      await axios
        .post('/cp_stop_finished', {sym: this.$route.params.sym , mid: this.mid})
        .then(response => {
          this.sfinished = response.data.data
          setTimeout(() => {
            this.getf()
          }, 2000)
        })
    },
    async getc () {
      await axios
        .get('/oltradeinfo')
        .then(response => {
          this.info = response.data
          this.infoback = response.data
        })
    },
    async getb () {
      await axios
        .post('/olboardinfo',{sym: this.$route.params.sym , mid: this.mid})
        .then(response => {
          this.boardinfo = response.data
          setTimeout(() => {
              this.getb()
          }, 20)
        })
    },
    async getbal (a) {
      await axios
        .post('/cp_balance',{sym: this.$route.params.sym , mid: this.mid})
        .then(response => {
          this.balances = response
          this.balance = parseFloat(response.data.available).toFixed(10)
          this.mid = response.data['account_id']
          this.getp()
          this.getsp()
          this.getf()
          this.getborrowlist()
          this.livebalances()
          if(a){
            setTimeout(() => {
              this.getbal(true)
            }, 5000);
          }
        })
    },
    async getopen () {
      await axios
        .get('/cp_open')
        .then(response => {
          this.balances = response
          this.balance = parseFloat(response.data.available).toFixed(10)
          setTimeout(() => {
              this.getb()
              this.getbal(false)
          }, 2000)
        })
    },
    async cpclose (market , id) {
      await axios
        .post('/cp_close', { market: market, id: parseInt(id), mid: this.mid })
        .then(response => {
          this.getp()
          this.getbal(false)
        })
    },
    async msell () {
      this.$loading(true)
      await axios
        .post('/cp_market_order', { market: this.$route.params.sym, type: 'sell', amount: (this.ms_amount - 0.000000005).toFixed(8), mid : this.mid })
        .then(response => {
          this.$loading(false)
          toast({
            message: 'با موفقیت انجام شد',
            type: 'is-success',
            dismissible: true,
            animate: { in: 'fadeIn', out: 'fadeOut' },
          })
          document.querySelectorAll('.delete').forEach(item => {
            item.addEventListener('click' , () => {
              item.parentElement.remove()
            })
            setTimeout(() => {
              item.parentElement.remove()
            }, 3000);
          })
          this.getp()
          this.getbal(false)
        }).catch(()=>{
          this.$loading(false)
        })
    },
    async mbuy () {
      this.$loading(true)
      await axios
        .post('/cp_market_order', {  market: this.$route.params.sym, type: 'buy', amount: (this.mb_amount - 0.000000005).toFixed(8), mid : this.mid })
        .then(response => {
          this.$loading(false)
          toast({
            message: 'با موفقیت انجام شد',
            type: 'is-success',
            dismissible: true,
            animate: { in: 'fadeIn', out: 'fadeOut' },
          })
          document.querySelectorAll('.delete').forEach(item => {
            item.addEventListener('click' , () => {
              item.parentElement.remove()
            })
            setTimeout(() => {
              item.parentElement.remove()
            }, 3000);
          })
          this.getp()
          this.getbal(false)
        }).catch(()=>{
            this.$loading(false)
          })
    },
    async lsell () {
      this.$loading(true)
      await axios
        .post('/cp_limit_order', { market: this.$route.params.sym, type: 'sell', amount: (this.ls_amount - 0.000000005).toFixed(8), price: this.ls_price, mid: this.mid })
        .then(response => {
          this.$loading(false)
          toast({
            message: 'با موفقیت انجام شد',
            type: 'is-success',
            dismissible: true,
            animate: { in: 'fadeIn', out: 'fadeOut' },
          })
          document.querySelectorAll('.delete').forEach(item => {
            item.addEventListener('click' , () => {
              item.parentElement.remove()
            })
            setTimeout(() => {
              item.parentElement.remove()
            }, 3000);
          })
          this.getp()
          this.getbal(false)
        }).catch(()=>{
          this.$loading(false)
        })
    },
    async lbuy () {
      this.$loading(true)
      await axios
        .post('/cp_limit_order', {  market: this.$route.params.sym, type: 'buy', amount: ((this.lb_amount) - 0.000000005).toFixed(8) ,  price: this.lb_price, mid : this.mid })
        .then(response => {
          this.$loading(false)
          toast({
            message: 'با موفقیت انجام شد',
            type: 'is-success',
            dismissible: true,
            animate: { in: 'fadeIn', out: 'fadeOut' },
          })
          document.querySelectorAll('.delete').forEach(item => {
            item.addEventListener('click' , () => {
              item.parentElement.remove()
            })
            setTimeout(() => {
              item.parentElement.remove()
            }, 3000);
          })
          this.getp()
          this.getbal(false)
        }).catch(()=>{
          this.$loading(false)
        })
    },
    async lssell () {
      this.$loading(true)
      await axios
        .post('/cp_stop_limit_order', { market: this.$route.params.sym, type: 'sell', amount: (this.lss_amount - 0.000000005).toFixed(8), price: this.lss_limit, stop_price: this.lss_stop, mid : this.mid })
        .then(response => {
          this.$loading(false)
          toast({
            message: 'با موفقیت انجام شد',
            type: 'is-success',
            dismissible: true,
            animate: { in: 'fadeIn', out: 'fadeOut' },
          })
          document.querySelectorAll('.delete').forEach(item => {
            item.addEventListener('click' , () => {
              item.parentElement.remove()
            })
            setTimeout(() => {
              item.parentElement.remove()
            }, 3000);
          })
          this.getp()
          this.getbal(false)
        }).catch(()=>{
          this.$loading(false)
        })
    },
    async lsbuy () {
      this.$loading(true)
      await axios
        .post('/cp_stop_limit_order', {  market: this.$route.params.sym, type: 'buy', amount: (this.lsb_amount - 0.000000005).toFixed(8),  price: this.lsb_limit, stop_price: this.lsb_stop, mid : this.mid })
        .then(response => {
          this.$loading(false)
          toast({
            message: 'با موفقیت انجام شد',
            type: 'is-success',
            dismissible: true,
            animate: { in: 'fadeIn', out: 'fadeOut' },
          })
          document.querySelectorAll('.delete').forEach(item => {
            item.addEventListener('click' , () => {
              item.parentElement.remove()
            })
            setTimeout(() => {
              item.parentElement.remove()
            }, 3000);
          })
          this.getp()
          this.getbal(false)
        }).catch(()=>{
          this.$loading(false)
        })
    },
    search () {
      this.info = {}
      var i = 0
      for (const [key, value] of Object.entries(this.infoback))
        if(key.replace('USDT' , '').includes(this.searchtext.toUpperCase())){
          this.info[key] = value
        }
    },
    async cancel (id) {
      this.$loading(true)
      await axios
        .post('/cp_cancel_order', {  market: this.$route.params.sym, id:id })
        .then(response => {
          this.$loading(false)
          toast({
            message: 'با موفقیت انجام شد',
            type: 'is-success',
            dismissible: true,
            animate: { in: 'fadeIn', out: 'fadeOut' },
          })
          document.querySelectorAll('.delete').forEach(item => {
            item.addEventListener('click' , () => {
              item.parentElement.remove()
            })
            setTimeout(() => {
              item.parentElement.remove()
            }, 3000);
          })
          this.getp()
          this.getbal(false)
        })
    },
    async scancel (id) {
      this.$loading(true)
      await axios
        .post('/cp_stop_cancel_order', {  market: this.$route.params.sym, id:id , mid : this.mid})
        .then(response => {
          this.$loading(false)
          toast({
            message: 'با موفقیت انجام شد',
            type: 'is-success',
            dismissible: true,
            animate: { in: 'fadeIn', out: 'fadeOut' },
          })
          document.querySelectorAll('.delete').forEach(item => {
            item.addEventListener('click' , () => {
              item.parentElement.remove()
            })
            setTimeout(() => {
              item.parentElement.remove()
            }, 3000);
          })
          this.getp()
          this.getbal(false)
          this.getsp()
        })
    },
    msbalance () {
      if(parseFloat(this.balances.data.balance.sell_type).toFixed(7) - 0.0000001 <= 0){
        this.ms_amount = 0
      }else{
        this.ms_amount = parseFloat(this.balances.data.balance.sell_type).toFixed(7) - 0.0000001
      }
    },
    mbbalance () {
      if(parseFloat(this.balances.data.balance.buy_type).toFixed(2) - 0.01 <= 0){
        this.mb_amount = 0
      }else{
        this.mb_amount = parseFloat(this.balances.data.balance.buy_type)
      }
    },
    lsbalance () {
      if(parseFloat(this.balances.data.balance.sell_type).toFixed(7) - 0.0000001 <= 0){
        this.ls_amount = 0
      }else{
        this.ls_amount = parseFloat(this.balances.data.balance.sell_type).toFixed(7) - 0.0000001
      }
    },
    lbbalance () {
      if(parseFloat(this.balances.data.balance.buy_type).toFixed(2) - 0.01 <= 0){
        this.lb_all = 0
      }else{
        this.lb_all = parseFloat(this.balances.data.balance.buy_type)}
    },
    lbslide () {
      if(this.lb_price){
        this.lb_amount = this.lb_all / this.lb_price
      }
    },
    lsbslide () {
      if(this.lsb_limit){
        this.lsb_amount = this.lsb_all / this.lsb_limit
      }
    },
    lssbalance () {
      if(parseFloat(this.balances.data.balance.sell_type).toFixed(7) - 0.0000001 <= 0){
        this.lss_amount = 0
      }else{
        this.lss_amount = parseFloat(this.balances.data.balance.sell_type).toFixed(7) - 0.0000001
      }
    },
    lsbbalance () {
      if(parseFloat(this.balances.data.balance.buy_type).toFixed(2) - 0.01 <= 0){
        this.lsb_all = 0
      }else{
        this.lsb_all = parseFloat(this.balances.data.balance.buy_type)
      }
    },
    tabact(id) {
      document.querySelectorAll('.tabss').forEach(item => {
        item.className = item.className.replace(' act' , '')
      })
      document.querySelectorAll('.tabsss').forEach(item => {
        item.style.display = 'none'
      })
      document.getElementById(id).className += ' act'
      document.querySelector(`.${id}`).style.display= 'block'
    },
    async getborrowlist () {
    await axios
    .post('/cp_borrowlist' , {market: this.$route.params.sym})
    .then(response => {
      this.repaybuymax = 0
      this.repaysellmax = 0
      for (var item of response.data.data){
        if(item.coin_type === this.balances.data.buy_asset_type){
          this.repaybuymax += Number(item.unflat_amount)
        }else {
          this.repaysellmax += Number(item.unflat_amount)
        }
      }
    })
    },
    transchange(){
    },
    transfer () {
      setTimeout(() => {
        document.querySelector('#transamount').addEventListener('change' , ()=>{
          this.transamount = document.querySelector('#transamount').value
        })
        document.querySelector('#aaaa').addEventListener('change', ()=>{
          this.transa = document.querySelector('#aaaa').value
          if (document.querySelector('#aaaa').value === '2'){
            if(document.querySelector('#bbbb').value === this.balances.data.buy_asset_type){

              document.querySelector('#transbal').innerHTML = this.balances.data.can_transfer.buy_type
            }
            if(document.querySelector('#bbbb').value === this.balances.data.sell_asset_type){

              document.querySelector('#transbal').innerHTML =  this.balances.data.can_transfer.sell_type
            }
          }if (document.querySelector('#aaaa').value === '1'){
            if(document.querySelector('#bbbb').value === this.balances.data.buy_asset_type){
              if(this.wallets[this.balances.data.buy_asset_type]['balance'].available){
                document.querySelector('#transbal').innerHTML =  this.wallets[this.balances.data.buy_asset_type]['balance'].available
              }else{
                document.querySelector('#transbal').innerHTML =  0
              }
              
            }
            if(document.querySelector('#bbbb').value === this.balances.data.sell_asset_type){
              if(this.wallets[this.balances.data.sell_asset_type]['balance'].available){
                document.querySelector('#transbal').innerHTML =  this.wallets[this.balances.data.sell_asset_type]['balance'].available
              }else{
                document.querySelector('#transbal').innerHTML =  0
              }
              
            }
          }
        })
        document.querySelector('#bbbb').addEventListener('change', ()=>{
          this.transb = document.querySelector('#bbbb').value
          if (document.querySelector('#aaaa').value === '2'){
            if(document.querySelector('#bbbb').value === this.balances.data.buy_asset_type){

              document.querySelector('#transbal').innerHTML = this.balances.data.can_transfer.buy_type
            }
            if(document.querySelector('#bbbb').value === this.balances.data.sell_asset_type){

              document.querySelector('#transbal').innerHTML =  this.balances.data.can_transfer.sell_type
            }
          }if (document.querySelector('#aaaa').value === '1'){
            if(document.querySelector('#bbbb').value === this.balances.data.buy_asset_type){
              if(this.wallets[this.balances.data.buy_asset_type].balance){
                document.querySelector('#transbal').innerHTML =  this.wallets[this.balances.data.buy_asset_type].balance.toFixed(6)
              }else{
                document.querySelector('#transbal').innerHTML =  0
              }
              
            }
            if(document.querySelector('#bbbb').value === this.balances.data.sell_asset_type){
              if(this.wallets[this.balances.data.sell_asset_type].balance){
                document.querySelector('#transbal').innerHTML =  this.wallets[this.balances.data.sell_asset_type].balance.toFixed(6)
              }else{
                document.querySelector('#transbal').innerHTML =  0
              }
              
            }
          }
        })
        document.querySelector('#transbal').addEventListener('click', ()=>{
          document.querySelector('#transamount').value = document.querySelector('#transbal').innerHTML
          this.transamount = document.querySelector('#transamount').value
        })
      }, 500);
      this.$swal.fire({
        title: 'Transfer',
        html:'<select id="aaaa" ' +'" class="form-control">' + '<option value="" disabled selected>سمت انتقال</option>' + `<option value="1">از asset</option>` + `<option value="2">به asset</option>` + '</select>' + '<br>' + '<select id="bbbb" class="form-control">'+ '<option value="" disabled selected>نوع کوین</option>' + `<option value="${this.balances.data.buy_asset_type}">${this.balances.data.buy_asset_type}</option>` + `<option value="${this.balances.data.sell_asset_type}">${this.balances.data.sell_asset_type}</option>` + '</select>' + '<br>'+ 'موجودی:'+ '<a class="btn btn-dark" style="padding: 0px 30px;margin:2px ; font-family: arial " href="#" id="transbal"></a>' +'<input id="transamount" placeholder="مبلغ" class="form-control"></input>',
        showCancelButton: true,
        confirmButtonText: 'تایید',
        cancelButtonText: 'لغو',
        showLoaderOnConfirm: true,
        },
        )
        .then((result) => {
          if (result.isConfirmed) {
            this.submittransfer()
          }
        }
      )
    },
    async submittransfer () {
      var from_account = 0
      var to_account = 0
    if(this.transa === '1' ){
      to_account = parseInt(this.balances.data.account_id)
    }
    if(this.transa === '2' ){
      from_account = parseInt(this.balances.data.account_id)
    }
    const formData = {
          fa: from_account ,
          ta: to_account,
          amount: this.transamount ,
          coin:this.transb
        }
    await axios
      .post('/cp_transfer' , formData)
      .then(response => {
        this.getw()
        this.getbal(false)
          if(!response.data){
            toast({
            message: 'با موفقیت انجام شد',
            type: 'is-success',
            dismissible: true,
            animate: { in: 'fadeIn', out: 'fadeOut' },
          })
          document.querySelectorAll('.delete').forEach(item => {
            item.addEventListener('click' , () => {
              item.parentElement.remove()
            })
            setTimeout(() => {
              item.parentElement.remove()
            }, 3000);
          })
          this.getp()
          this.getbal(false)
          }
        }).catch(data =>{
          console.log(data.response.data)
          toast({
            message: `${data.response.data}`,
            type: 'is-danger',
            dismissible: true,
            animate: { in: 'fadeIn', out: 'fadeOut' },
          })
          document.querySelectorAll('.delete').forEach(item => {
            item.addEventListener('click' , () => {
              item.parentElement.remove()
            })
            setTimeout(() => {
              item.parentElement.remove()
            }, 3000);
          })
        })
  },
    borrow () {
      var allbalance = Number(this.balances.data.can_transfer.buy_type) + (Number(this.balances.data.can_transfer.sell_type) * Number(this.info[this.$route.params.sym].last))
      var maxbuy = (this.livebalance * parseFloat(this.balances.data.leverage) * 0.80 )- this.repaybuymax - (this.repaysellmax * this.info[this.$route.params.sym].last)
      var maxsell = (maxbuy / this.info[this.$route.params.sym].last)
      setTimeout(() => {
        document.querySelector('#bbbbb').addEventListener('change', ()=>{

            this.borrowcoin = document.querySelector('#bbbbb').value

            if(document.querySelector('#bbbbb').value === this.balances.data.buy_asset_type){

              document.querySelector('#borrowmax').innerHTML = maxbuy
            }
            if(document.querySelector('#bbbbb').value === this.balances.data.sell_asset_type){

              document.querySelector('#borrowmax').innerHTML =  maxsell
          }
        })
        document.querySelector('#borrowmax').addEventListener('click', ()=>{
          document.querySelector('#borrowamount').value = document.querySelector('#borrowmax').innerHTML
          this.borrowamount = document.querySelector('#borrowamount').value
        })
        document.querySelector('#borrowamount').addEventListener('change', ()=>{
          this.borrowamount = document.querySelector('#borrowamount').value
        })
      }, 500);
      this.$swal.fire({
        title: 'Borrow',
        html:'<select id="bbbbb" class="form-control">' + '<option value="" disabled selected>نوع کوین</option>' + `<option value="${this.balances.data.buy_asset_type}">${this.balances.data.buy_asset_type}</option>` + `<option value="${this.balances.data.sell_asset_type}">${this.balances.data.sell_asset_type}</option>` + '</select>' + '<br>'+ 'بیشترین مقدار قابل دریافت:'+ '<a class="btn btn-dark" style="padding: 0px 30px;margin:2px" href="#" id="borrowmax"></a>' +'<input id="borrowamount" placeholder="مبلغ" class="form-control"></input>',
        showCancelButton: true,
        confirmButtonText: 'تایید',
        cancelButtonText: 'لغو',
        showLoaderOnConfirm: true,
        },
        )
        .then((result) => {
          if (result.isConfirmed) {

            this.submitborrow().then(()=>{
             
            })
          }
        }
      )
    },
    async submitborrow () {
    await axios
    .post('/cp_borrow' , {amount: this.borrowamount , coin:this.borrowcoin , market: this.$route.params.sym})
    .then(response => {
          if(response.data.loan_id){
            toast({
            message: 'با موفقیت انجام شد',
            type: 'is-success',
            dismissible: true,
            animate: { in: 'fadeIn', out: 'fadeOut' },
          })
          document.querySelectorAll('.delete').forEach(item => {
            item.addEventListener('click' , () => {
              item.parentElement.remove()
            })
            setTimeout(() => {
              item.parentElement.remove()
            }, 3000);
          })
          this.getp()
          this.getbal(false)
          }else{
            toast({
            message: response.data,
            type: 'is-danger',
            dismissible: true,
            animate: { in: 'fadeIn', out: 'fadeOut' },
          })
          document.querySelectorAll('.delete').forEach(item => {
            item.addEventListener('click' , () => {
              item.parentElement.remove()
            })
            setTimeout(() => {
              item.parentElement.remove()
            }, 3000);
          })
          }
        })
  },
    repay () {
      var maxbuyrepay = this.repaybuymax
      var maxsellrepay = this.repaysellmax
      setTimeout(() => {
        document.querySelector('#bbbbbb').addEventListener('change', ()=>{

            this.repaycoin = document.querySelector('#bbbbbb').value

            if(document.querySelector('#bbbbbb').value === this.balances.data.buy_asset_type){

              document.querySelector('#repaymax').innerHTML = maxbuyrepay
            }
            if(document.querySelector('#bbbbbb').value === this.balances.data.sell_asset_type){

              document.querySelector('#repaymax').innerHTML =  maxsellrepay
          }
        })
        document.querySelector('#repaymax').addEventListener('click', ()=>{
          document.querySelector('#repayamount').value = document.querySelector('#repaymax').innerHTML
          this.repayamount = document.querySelector('#repayamount').value
        })
        document.querySelector('#repayamount').addEventListener('change', ()=>{
          this.repayamount = document.querySelector('#repayamount').value
        })
      }, 500);
      this.$swal.fire({
        title: 'Repay',
        html:'<select id="bbbbbb" class="form-control">' + '<option value="" disabled selected>نوع کوین</option>' + `<option value="${this.balances.data.buy_asset_type}">${this.balances.data.buy_asset_type}</option>` + `<option value="${this.balances.data.sell_asset_type}">${this.balances.data.sell_asset_type}</option>` + '</select>' + '<br>'+ 'بیشترین مقدار باز پرداخت:'+ '<a class="btn btn-dark" style="padding: 0px 30px;margin:2px" href="#" id="repaymax"></a>' +'<input id="repayamount" placeholder="مبلغ" class="form-control"></input>',
        showCancelButton: true,
        confirmButtonText: 'تایید',
        cancelButtonText: 'لغو',
        showLoaderOnConfirm: true,
        },
        )
        .then((result) => {
          if (result.isConfirmed) {

            this.submitrepay().then(()=>{
             
            })
          }
        }
      )
    },
    async submitrepay () {
    await axios
    .post('/cp_repay' , {amount: this.repayamount , coin:this.repaycoin , market: this.$route.params.sym})
    .then(response => {
          if(!response.data){
            toast({
            message: 'با موفقیت انجام شد',
            type: 'is-success',
            dismissible: true,
            animate: { in: 'fadeIn', out: 'fadeOut' },
          })
          document.querySelectorAll('.delete').forEach(item => {
            item.addEventListener('click' , () => {
              item.parentElement.remove()
            })
            setTimeout(() => {
              item.parentElement.remove()
            }, 3000);
          })
          this.getp()
          this.getbal(false)
          }else{
            toast({
            message: response.data,
            type: 'is-danger',
            dismissible: true,
            animate: { in: 'fadeIn', out: 'fadeOut' },
          })
          document.querySelectorAll('.delete').forEach(item => {
            item.addEventListener('click' , () => {
              item.parentElement.remove()
            })
            setTimeout(() => {
              item.parentElement.remove()
            }, 3000);
          })
          }
        })
  },
    strftime(sFormat, date) {
      if (!(date instanceof Date)) date = new Date();
      var nDay = date.getDay(),
        nDate = date.getDate(),
        nMonth = date.getMonth(),
        nYear = date.getFullYear(),
        nHour = date.getHours(),
        aDays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
        aMonths = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        aDayCount = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334],
        isLeapYear = function() {
          if ((nYear&3)!==0) return false;
          return nYear%100!==0 || nYear%400===0;
        },
        getThursday = function() {
          var target = new Date(date);
          target.setDate(nDate - ((nDay+6)%7) + 3);
          return target;
        },
        zeroPad = function(nNum, nPad) {
          return ('' + (Math.pow(10, nPad) + nNum)).slice(1);
        };
      return sFormat.replace(/%[a-z]/gi, function(sMatch) {
        return {
          '%a': aDays[nDay].slice(0,3),
          '%A': aDays[nDay],
          '%b': aMonths[nMonth].slice(0,3),
          '%B': aMonths[nMonth],
          '%c': date.toUTCString(),
          '%C': Math.floor(nYear/100),
          '%d': zeroPad(nDate, 2),
          '%e': nDate,
          '%F': date.toISOString().slice(0,10),
          '%G': getThursday().getFullYear(),
          '%g': ('' + getThursday().getFullYear()).slice(2),
          '%H': zeroPad(nHour, 2),
          '%I': zeroPad((nHour+11)%12 + 1, 2),
          '%j': zeroPad(aDayCount[nMonth] + nDate + ((nMonth>1 && isLeapYear()) ? 1 : 0), 3),
          '%k': '' + nHour,
          '%l': (nHour+11)%12 + 1,
          '%m': zeroPad(nMonth + 1, 2),
          '%M': zeroPad(date.getMinutes(), 2),
          '%p': (nHour<12) ? 'AM' : 'PM',
          '%P': (nHour<12) ? 'am' : 'pm',
          '%s': Math.round(date.getTime()/1000),
          '%S': zeroPad(date.getSeconds(), 2),
          '%u': nDay || 7,
          '%V': (function() {
                  var target = getThursday(),
                    n1stThu = target.valueOf();
                  target.setMonth(0, 1);
                  var nJan1 = target.getDay();
                  if (nJan1!==4) target.setMonth(0, 1 + ((4-nJan1)+7)%7);
                  return zeroPad(1 + Math.ceil((n1stThu-target)/604800000), 2);
                })(),
          '%w': '' + nDay,
          '%x': date.toLocaleDateString(),
          '%X': date.toLocaleTimeString(),
          '%y': ('' + nYear).slice(2),
          '%Y': nYear,
          '%z': date.toTimeString().replace(/.+GMT([+-]\d+).+/, '$1'),
          '%Z': date.toTimeString().replace(/.+\((.+?)\)$/, '$1')
        }[sMatch] || sMatch;
      });
    }
}
}
</script>
<style>
.cent{
  text-align: center;
}
.mb-3{
    border-radius: 0;
    float:left;
    box-sizing: border-box;
}
.cardss{
    background:#1d2134;
    box-sizing: border-box;
    padding: 0;
}
th{
    padding: 10px;
}
td{
    padding:10px
}
p{
  font-size: 14px;
  margin-bottom: 0;
  margin-top: 5px;
}
#trader .nav-link{
height:99%;
background: rgba(0, 0, 0, 0)!important;
border-radius: 0!important;
border-style: none!important;
padding: 10px 30px!important;
color: white!important;
}
#trader .nav-link.active{
background: #1d202e!important;
border-radius: 0!important;
border-style: none!important;
padding: 10px 30px!important;
color: white!important;
}
#hist ul{
  border-style: none!important;
  background: #33374f!important;
}
.btn-cur{
  width: 100%;
  height: 100%;
}
.btn-cur:hover{
  background-color: grey;
  cursor: pointer;
}
.act{
  background-color: white!important;;
  color: black;
}
.act:hover{
  color: black;
}
.nbile{
    display: block;
  }
.obile{
  display: none ;
}
@media only screen and (max-width: 1024px) {
  #p1 {
    width: 100%!important;
    height:130px!important
  }
  #p2{
    width: 100%!important;
    margin-bottom: 20px
  }
  #p3{
    display: none;
  }
  #p4{
    display: none;
  }
  #p5{
    width:100%!important
  }
  #p6{
    display: none;
  }
  
}
@media only screen and (max-width: 600px) {
  #p5{
    width: 100%!important;
    height:900px!important
  }
  #p5-sub{
    height:900px!important
  }
  .hundbile{
    width:100%!important;
    position:relative!important;
    height: auto!important;
  }
  .nbile{
    display: none;
  }
  .obile{
    display: block;
  }
}
</style>
<style lang="scss">
.notification {
  background-color: whitesmoke;
  border-radius: 4px;
  position: relative;
  padding: 1.25rem 2.5rem 1.25rem 1.5rem;
  margin:5px
}

.notification a:not(.button):not(.dropdown-item) {
  color: currentColor;
  text-decoration: underline;
}

.notification strong {
  color: currentColor;
}

.notification code,
.notification pre {
  background: white;
}

.notification pre code {
  background: transparent;
}

.notification > .delete {
  right: 0.5rem;
  position: absolute;
  top: 0.5rem;
}

.notification .title,
.notification .subtitle,
.notification .content {
  color: currentColor;
}

.notification.is-white {
  background-color: white;
  color: #0a0a0a;
}

.notification.is-black {
  background-color: #0a0a0a;
  color: white;
}

.notification.is-light {
  background-color: whitesmoke;
  color: rgba(0, 0, 0, 0.7);
}

.notification.is-dark {
  background-color: #363636;
  color: #fff;
}

.notification.is-primary {
  background-color: #00d1b2;
  color: #fff;
}

.notification.is-primary.is-light {
  background-color: #ebfffc;
  color: #00947e;
}

.notification.is-link {
  background-color: #485fc7;
  color: #fff;
}

.notification.is-link.is-light {
  background-color: #eff1fa;
  color: #3850b7;
}

.notification.is-info {
  background-color: #3e8ed0;
  color: #fff;
}

.notification.is-info.is-light {
  background-color: #eff5fb;
  color: #296fa8;
}

.notification.is-success {
  background-color: #48c78e;
  color: #fff;
}

.notification.is-success.is-light {
  background-color: #effaf5;
  color: #257953;
}

.notification.is-warning {
  background-color: #ffe08a;
  color: rgba(0, 0, 0, 0.7);
}

.notification.is-warning.is-light {
  background-color: #fffaeb;
  color: #946c00;
}

.notification.is-danger {
  background-color: #f14668;
  color: #fff;
}

.notification.is-danger.is-light {
  background-color: #feecf0;
  color: #cc0f35;
}
.delete, .modal-close {
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  -moz-appearance: none;
  -webkit-appearance: none;
  background-color: rgba(10, 10, 10, 0.2);
  border: none;
  border-radius: 9999px;
  cursor: pointer;
  pointer-events: auto;
  display: inline-block;
  flex-grow: 0;
  flex-shrink: 0;
  font-size: 0;
  height: 20px;
  max-height: 20px;
  max-width: 20px;
  min-height: 20px;
  min-width: 20px;
  outline: none;
  position: relative;
  vertical-align: top;
  width: 20px;
}

.delete::before, .modal-close::before, .delete::after, .modal-close::after {
  background-color: white;
  content: "";
  display: block;
  left: 50%;
  position: absolute;
  top: 50%;
  transform: translateX(-50%) translateY(-50%) rotate(45deg);
  transform-origin: center center;
}

.delete::before, .modal-close::before {
  height: 2px;
  width: 50%;
}

.delete::after, .modal-close::after {
  height: 50%;
  width: 2px;
}

.delete:hover, .modal-close:hover, .delete:focus, .modal-close:focus {
  background-color: rgba(10, 10, 10, 0.3);
}

.delete:active, .modal-close:active {
  background-color: rgba(10, 10, 10, 0.4);
}

.is-small.delete, .is-small.modal-close {
  height: 16px;
  max-height: 16px;
  max-width: 16px;
  min-height: 16px;
  min-width: 16px;
  width: 16px;
}

.is-medium.delete, .is-medium.modal-close {
  height: 24px;
  max-height: 24px;
  max-width: 24px;
  min-height: 24px;
  min-width: 24px;
  width: 24px;
}

.is-large.delete, .is-large.modal-close {
  height: 32px;
  max-height: 32px;
  max-width: 32px;
  min-height: 32px;
  min-width: 32px;
  width: 32px;
}
.d-inline-block {
  width:90%!important;
  margin-right:5%!important
}
.slider-horizontal{
  width:90%!important;
  margin-right:5%!important
}
.slider-handle .min-slider-handle{
  background-color: grey!important;
}
</style>
