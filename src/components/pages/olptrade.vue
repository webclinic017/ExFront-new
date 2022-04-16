<template>
  <div style="direction:ltr;overflow-x:auto;width:1275px;margin:auto" v-cloak id="trader"><br>
    <h4 class="d-flex flex-wrap justify-content-between align-items-center pt-3 mb-4">
      <div class="col-12 col-md-3 p-0 mb-3">
      </div>
    </h4>

    <div class="col-12">
      <b-card no-body class="mb-3 col-3 cardss" style=";height:450px;overflow:auto">
          <b-input v-model="searchtext" placeholder="...جستجو" style="top:0;position:absolute;height:40px; width: 100%;margin:auto;background:transparent;border-style:none;padding:10px;border-radius:0;border-bottom:solid;text-align:right" @input="search()"></b-input>
        <table style="top:40px;position:absolute;text-align:right; color:white;font:14px 'arial';width:100%" class="">
              <tr style="width:100%;background:rgba(0,0,0,0.4);box-sizing:border-box">
                  <th scope="col" style="width:50%">قیمت</th>
                  <th scope="col" style="width:50%">بازار</th>
              </tr>
              
          <tr v-for="(item,name) in info" v-bind:key="name" class="btn-cur" :id="`${name}`" @click="click(name)">
             <td style="width:50%"><a :href="`/perpetual-trade/${name}`"  style="color:white" @click="changeroute()" > {{info[name]}}</a></td>
             <td style="width:50%"><a :href="`/perpetual-trade/${name}`" style="color:white" @click="changeroute()" >{{name}}</a> </td>
          </tr>
          
          </table>
        <div>
          <b-card-body class="cardss py-3">
          </b-card-body>
        </div>

      </b-card>
      <div class="col-6" style="float:left;height:450px">
          <b-card no-body class="cardss" style="border-radius: 0!important;height:450px"><br>
            <div style="margin:auto" id="tradingview_1be21"></div>
        <div>
          <b-card-body class="py-3 cardss">
          </b-card-body>
        </div>

      </b-card>
      </div>
      <b-card no-body class="mb-3 col-3 cardss" style=";height:430px">
          <h5 style="width:100%;height:40px;background:black;padding:8px;text-align:center;color:#cacadc;margin:0">درخواست های خرید</h5>
          <table v-if="boardinfo.asks"  style="text-align:right; color:white;font:14px 'arial';" class="">
              <tr style="width:100%;background:rgba(0,0,0,0.4);box-sizing:border-box">
                  <th scope="col" style="width:30%">مجموع</th>
                  <th scope="col" style="width:30%">قیمت</th>
                  <th scope="col" style="width:30%">مقدار</th>
              </tr>
          <tr v-for="(item, idx) in boardinfo.asks.slice(0,10)" v-bind:key="idx">
            <td style="width:30%;">{{(item[1] * item[0]).toFixed(2)}}</td>
             <td @click="fillpos(item[0])" style="width:30%;color:green">{{item[0]}}</td>
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
      <b-card no-body class="mb-3 col-3 cardss" style=";height:470px;color:white">
                      <h4 style="font-family:'arial';width:100%;height:40px;background:black;padding:8px;text-align:center;color:#cacadc">موجودی</h4>
       <table v-if="balances"  >
          <tr v-for="(value, name) in balances" v-bind:key="name" style="font-family:'arial';font-size:12px">
             <td style="width:50%;text-align:left"> {{parseFloat(balances[name]).toFixed(4)}}</td>
             <td style="width:50%;text-align:right">{{name}}</td>
          </tr>
       </table>
      </b-card>
      <div class="col-6 " style="float:left;height:500px">
          <b-card no-body class="cardss" style="border-radius: 0!important;height:470px">
              <h4 style="font-family:'arial';width:100%;height:40px;background:black;padding:8px;text-align:center;color:#cacadc">پرپچوال</h4>
              <div style="font-family:'arial';width:100%;height:40px;background:none;padding:8px;text-align:center;color:#cacadc">
              <select v-model="lev" @change="adjustleverage()" name="" id="" class="form-control" style="width:15%; float:left">
                <option v-for="item in marketinfo.leverages" v-bind:key="item" :value="item">{{item}}X</option>
              </select>
                  <button style="float:right;background:none;border-color:grey;margin:5px;border-radius:3px;padding:3px;padding-left:15px;padding-right:15px;font-family:'arial'" id="limit" @click="tabact('limit')" class="btn btn-light tabss">Limit</button>
                  <button style="float:right;background:none;border-color:grey;margin:5px;border-radius:3px;padding:3px;padding-left:15px;padding-right:15px;font-family:'arial'" id="market" @click="tabact('market')" class="btn btn-light act tabss">Market</button>
                  <button style="float:right;background:none;border-color:grey;margin:5px;border-radius:3px;padding:3px;padding-left:15px;padding-right:15px;font-family:'arial'" id="stop-limit" @click="tabact('stop-limit')" class="btn btn-light tabss">Stop-Limit</button>
              </div><br>
              <div class="tabsss market">
              <div style="width:50%;height:350px;position:absolute;left:0;bottom:0;padding:15px;color:#cacadc" >
               <p><button class="btn btn-warning" style="padding-top : 0px;padding-bottom : 0px;background:none" v-if="balances" @click="mbbalance()">  {{parseFloat(balances.available).toFixed(9)}} USDT</button> : موجودی</p>
              <form @submit.prevent="mbuy()">
                <div class="input-group mb-3">
                  <div class="input-group-prepend" style="direction:rtl">
                    <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-left:none;border-right:none;border-radius:0;border-color:grey;font-family:'arial'; background:rgba(255,255,255,.2)">USDT</span>
                    <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-right:none;border-radius:0;border-color:grey;color:white;font-family:'arial'; background:rgba(255,255,255,.2)">Price</span>
                  </div>
                  <input readonly disabled placeholder="بهترین قیمت بازار" class="form-control" step="any" min="0" aria-label="Default" aria-describedby="inputGroup-sizing-default" type="number"  style="background:none; border-style:solid;border-radius:0;border-color:grey;text-align: right; background:rgba(255,255,255,.2)">
                </div>
                <div class="input-group mb-3">
                  <div class="input-group-prepend" style="direction:rtl">
                    <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-left:none;border-right:none;border-radius:0;border-color:grey;font-family:'arial'">USDT</span>
                    <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-right:none;border-radius:0;border-color:grey;color:white;font-family:'arial'">Amount</span>  
                  </div>
                    <input v-model="mb_amount" class="form-control" step="any" min="0" aria-label="Default" aria-describedby="inputGroup-sizing-default" type="number" style="background:none; border-style:solid;border-radius:0;border-color:grey;text-align: right;font-family:'arial'">
                </div>
                <p style=";font-family:'arial'">  {{mb_amount}}  USDT : مبلغ کل</p>
                <br>
                <input type="submit" value="خرید" class="btn btn-success" style="width:100%;border-radius:0">
              </form>
              </div>
              <div style="width:50%;height:350px;position:absolute;right:0;bottom:0;padding:15px;color:#cacadc">
               <p><button class="btn btn-warning" style="padding-top : 0px;padding-bottom : 0px;background:none" v-if="balances" @click="msbalance()"> {{parseFloat(balances.available).toFixed(9)}} USDT </button> : موجودی</p>
               <form @submit.prevent="msell()">
                 <div class="input-group mb-3">
  <div class="input-group-prepend" style="direction:rtl">
            <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-left:none;border-right:none;border-radius:0;border-color:grey;font-family:'arial'; background:rgba(255,255,255,.2)">USDT</span>
    <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-right:none;border-radius:0;border-color:grey;color:white;font-family:'arial'; background:rgba(255,255,255,.2)">Price</span>
  </div>
  <input readonly disabled placeholder="بهترین قیمت بازار" class="form-control" step="any" min="0" aria-label="Default" aria-describedby="inputGroup-sizing-default" type="number"  style="background:none; border-style:solid;border-radius:0;border-color:grey; text-align:right; background:rgba(255,255,255,.2)">
</div>
               
                              <div class="input-group mb-3">
  <div class="input-group-prepend" style="direction:rtl">
            <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-left:none;border-right:none;border-radius:0;border-color:grey;font-family:'arial'">USDT</span>
    <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-right:none;border-radius:0;border-color:grey;color:white;font-family:'arial'">Amount</span>  </div>
  <input v-model="ms_amount" class="form-control" step="any" min="0" aria-label="Default" aria-describedby="inputGroup-sizing-default" type="number" style="background:none; border-style:solid;border-radius:0;border-color:grey;text-align: right;font-family:'arial'">
</div>
<p style=";font-family:'arial'">  ~~ USDT : مبلغ کل</p>
<br>
<input type="submit" value="فروش" class="btn btn-danger" style="width:100%;border-radius:0">
               </form>
              </div>
              </div>
              <div class="tabsss limit" style="display:none">
              <div style="width:50%;height:350px;position:absolute;left:0;bottom:0;padding:15px;color:#cacadc" >
               <p><button class="btn btn-warning" style="padding-top : 0px;padding-bottom : 0px;background:none" @click="lbbalance()">  {{parseFloat(balances.available).toFixed(9)}} USDT</button> : موجودی</p>
              <form @submit.prevent="lbuy()">
                <div class="input-group mb-3">
                  <div class="input-group-prepend" style="direction:rtl">
                    <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-left:none;border-right:none;border-radius:0;border-color:grey;font-family:'arial'; ">USDT</span>
                    <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-right:none;border-radius:0;border-color:grey;color:white;font-family:'arial'; ">Price</span>
                  </div>
                  <input v-model="lb_price" class="form-control" step="any" min="0" aria-label="Default" aria-describedby="inputGroup-sizing-default" type="number"  style="background:none; border-style:solid;border-radius:0;border-color:grey;text-align: right;font-family:'arial'">
                </div>
                <div class="input-group mb-3">
                  <div class="input-group-prepend" style="direction:rtl">
                    <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-left:none;border-right:none;border-radius:0;border-color:grey;font-family:'arial'">USDT</span>
                    <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-right:none;border-radius:0;border-color:grey;color:white;font-family:'arial'">Amount</span>  
                  </div>
                    <input v-model="lb_amount" class="form-control" step="any" min="0" aria-label="Default" aria-describedby="inputGroup-sizing-default" type="number" style="background:none; border-style:solid;border-radius:0;border-color:grey;text-align: right;font-family:'arial'">
                </div>
                <p style=";font-family:'arial'">  {{lb_amount * lb_price}}  USDT : مبلغ کل</p>
                <br>
                <input type="submit" value="خرید" class="btn btn-success" style="width:100%;border-radius:0">
              </form>
              </div>
              <div style="width:50%;height:350px;position:absolute;right:0;bottom:0;padding:15px;color:#cacadc">
               <p><button class="btn btn-warning" style="padding-top : 0px;padding-bottom : 0px;background:none" @click="lsbalance()"> {{parseFloat(balances.available).toFixed(9)}} USDT </button> : موجودی</p>
               <form @submit.prevent="lsell()">
                 <div class="input-group mb-3">
  <div class="input-group-prepend" style="direction:rtl">
            <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-left:none;border-right:none;border-radius:0;border-color:grey;font-family:'arial'; ">USDT</span>
    <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-right:none;border-radius:0;border-color:grey;color:white;font-family:'arial'; ">Price</span>
  </div>
  <input v-model="ls_price" class="form-control" step="any" min="0" aria-label="Default" aria-describedby="inputGroup-sizing-default" type="number"  style="background:none; border-style:solid;border-radius:0;border-color:grey; text-align:right;font-family:'arial' ">
</div>
               
                              <div class="input-group mb-3">
  <div class="input-group-prepend" style="direction:rtl">
            <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-left:none;border-right:none;border-radius:0;border-color:grey;font-family:'arial'" >USDT</span>
    <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-right:none;border-radius:0;border-color:grey;color:white;font-family:'arial'">Amount</span>  </div>
  <input v-model="ls_amount" class="form-control" step="any" min="0" aria-label="Default" aria-describedby="inputGroup-sizing-default" type="number" style="background:none; border-style:solid;border-radius:0;border-color:grey;text-align: right;font-family:'arial'">
</div>
<p style=";font-family:'arial'"> {{ls_amount * ls_price}} USDT : مبلغ کل</p>
<br>
<input type="submit" value="فروش" class="btn btn-danger" style="width:100%;border-radius:0">
               </form>
              </div>
              </div>
              <div class="tabsss stop-limit" style="display:none">
              <div style="width:50%;height:350px;position:absolute;left:0;bottom:0;padding:15px;color:#cacadc" >
               <p><button class="btn btn-warning" style="padding-top : 0px;padding-bottom : 0px;background:none" @click="lsbbalance()">  {{parseFloat(balances.available).toFixed(9)}} USDT</button> : موجودی</p>
              <form @submit.prevent="lsbuy()">



                <div class="input-group mb-3">
                  <div class="input-group-prepend" style="direction:rtl">
                    <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-left:none;border-right:none;border-radius:0;border-color:grey;font-family:'arial'; ">USDT</span>
                    <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-right:none;border-radius:0;border-color:grey;color:white;font-family:'arial'; ">Stop</span>
                  </div>
                  <input v-model="lsb_stop" class="form-control" step="any" min="0" aria-label="Default" aria-describedby="inputGroup-sizing-default" type="number"  style="background:none; border-style:solid;border-radius:0;border-color:grey;text-align: right;font-family:'arial'">
                </div>



                <div class="input-group mb-3">
                  <div class="input-group-prepend" style="direction:rtl">
                    <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-left:none;border-right:none;border-radius:0;border-color:grey;font-family:'arial'">USDT</span>
                    <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-right:none;border-radius:0;border-color:grey;color:white;font-family:'arial'">Limit</span>  
                  </div>
                    <input v-model="lsb_limit" class="form-control" step="any" min="0" aria-label="Default" aria-describedby="inputGroup-sizing-default" type="number" style="background:none; border-style:solid;border-radius:0;border-color:grey;text-align: right;font-family:'arial'">
                </div>




                <div class="input-group mb-3">
                  <div class="input-group-prepend" style="direction:rtl">
                    <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-left:none;border-right:none;border-radius:0;border-color:grey;font-family:'arial'" >USDT</span>
                    <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-right:none;border-radius:0;border-color:grey;color:white;font-family:'arial'">Amount</span>  
                  </div>
                    <input v-model="lsb_amount" class="form-control" step="any" min="0" aria-label="Default" aria-describedby="inputGroup-sizing-default" type="number" style="background:none; border-style:solid;border-radius:0;border-color:grey;text-align: right;font-family:'arial'">
                </div>



                <p style=";font-family:'arial'">  {{lsb_amount * lsb_limit}}  USDT : مبلغ کل</p>
                <br>
                <input type="submit" value="خرید" class="btn btn-success" style="width:100%;border-radius:0">
              </form>
              </div>
              <div style="width:50%;height:350px;position:absolute;right:0;bottom:0;padding:15px;color:#cacadc">
               <p><button class="btn btn-warning" style="padding-top : 0px;padding-bottom : 0px;background:none" @click="lssbalance()"> {{parseFloat(balances.available).toFixed(9)}} USDT </button> : موجودی</p>
               <form @submit.prevent="lssell()">



                  <div class="input-group mb-3">
                    <div class="input-group-prepend" style="direction:rtl">
                      <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-left:none;border-right:none;border-radius:0;border-color:grey;font-family:'arial'; ">USDT</span>
                      <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-right:none;border-radius:0;border-color:grey;color:white;font-family:'arial'; ">Stop</span>
                    </div>
                    <input v-model="lss_stop" class="form-control" step="any" min="0" aria-label="Default" aria-describedby="inputGroup-sizing-default" type="number"  style="background:none; border-style:solid;border-radius:0;border-color:grey; text-align:right;font-family:'arial' ">
                  </div>


                                
                  <div class="input-group mb-3">
                    <div class="input-group-prepend" style="direction:rtl">
                      <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-left:none;border-right:none;border-radius:0;border-color:grey;font-family:'arial'">USDT</span>
                      <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-right:none;border-radius:0;border-color:grey;color:white;font-family:'arial'">Limit</span>  </div>
                    <input v-model="lss_limit" class="form-control" step="any" min="0" aria-label="Default" aria-describedby="inputGroup-sizing-default" type="number" style="background:none; border-style:solid;border-radius:0;border-color:grey;text-align: right;font-family:'arial'">
                  </div>




                  <div class="input-group mb-3">
                    <div class="input-group-prepend" style="direction:rtl">
                              <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-left:none;border-right:none;border-radius:0;border-color:grey;font-family:'arial'" >USDT</span>
                      <span class="input-group-text" id="inputGroup-sizing-default" style="background:none;border-right:none;border-radius:0;border-color:grey;color:white;font-family:'arial'">Amount</span>  </div>
                    <input v-model="lss_amount" class="form-control" step="any" min="0" aria-label="Default" aria-describedby="inputGroup-sizing-default" type="number" style="background:none; border-style:solid;border-radius:0;border-color:grey;text-align: right;font-family:'arial'">
                  </div>



                  <p style=";font-family:'arial'"> {{lss_amount * lss_limit}} USDT : مبلغ کل</p>
                  <br>
                  <input type="submit" value="فروش" class="btn btn-danger" style="width:100%;border-radius:0">
               </form>
              </div>
              </div>
      </b-card>
      </div>
      <b-card no-body class="mb-3 col-3 cardss" style=";height:510px;margin-top:-40px">
        <h1 style="width:100%;height:50px;background:rgba(0,0,0,0.4);padding:8px;text-align:left;color:#cacadc;margin:0;color:green">{{boardinfo.last}} <br></h1>
          <h5 style="width:100%;height:40px;background:black;padding:8px;text-align:center;color:#cacadc;margin:0">درخواست های فروش</h5>
          <table v-if="boardinfo.bids"  style="text-align:right; color:white;font:14px 'arial';" class="">
              <tr style="width:100%;background:rgba(0,0,0,0.4);box-sizing:border-box">
                  <th scope="col" style="width:30%">مجموع</th>
                  <th scope="col" style="width:30%">قیمت</th>
                  <th scope="col" style="width:30%">مقدار</th>
              </tr>
          <tr v-for="(item, idx) in boardinfo.bids.slice(0,10)" v-bind:key="idx">
            <td style="width:30%;">{{(item[1] * item[0]).toFixed(2)}}</td>
             <td @click="fillneg(item[0])" style="width:30%;color:red;font-family:'arial'">{{item[0]}}</td>
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
      <b-tabs no-body class="col-12 cardss" style="height:auto;margin-bottom:50px">
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
                  <th scope="col" style="width:16% ; text-align:center">عملیات</th>
              </tr>
              <tr v-for="(item,idx) in pending" v-bind:key="idx" style="height:100px;font-weight:bold">

                  <td style="width:12% ; text-align:center ; color:green" v-if="item.type == 'buy'">{{strftime("%m/%d/%y %H:%M:%S",item.create_time)}}</td>
                  <td style="width:12% ; text-align:center ; color:green" v-if="item.type == 'buy'">{{item.market}}</td>      
                  <td style="width:12% ; text-align:center ; color:green" v-if="item.type == 'buy'">{{item.order_type}}</td>
                  <td style="width:12% ; text-align:center ; color:green" v-if="item.type == 'buy'">{{String(item.type).replace('sell','فروش').replace('buy','خرید')}}</td>
                  <td style="width:12% ; text-align:center ; color:green" v-if="item.type == 'buy'">{{(parseFloat(item.left)).toFixed(2)}}</td>
                  <td style="width:12% ; text-align:center ; color:green" v-if="item.type == 'buy'">{{(parseFloat(item.amount) - parseFloat(item.left)).toFixed(2)}}</td>
                  <td style="width:12% ; text-align:center ; color:green" v-if="item.type == 'buy'">{{item.avg_price}}</td>


                  <td style="width:12% ; text-align:center ; color:red" v-if="item.type == 'sell'">{{strftime("%m/%d/%y %H:%M:%S",item.create_time)}}</td>
                  <td style="width:12% ; text-align:center ; color:red" v-if="item.type == 'sell'">{{item.market}}</td>      
                  <td style="width:12% ; text-align:center ; color:red" v-if="item.type == 'sell'">{{item.order_type}}</td>
                  <td style="width:12% ; text-align:center ; color:red" v-if="item.type == 'sell'">{{String(item.type).replace('sell','فروش').replace('buy','خرید')}}</td>
                  <td style="width:12% ; text-align:center ; color:red" v-if="item.type == 'sell'">{{(parseFloat(item.left)).toFixed(2)}}</td>
                  <td style="width:12% ; text-align:center ; color:red" v-if="item.type == 'sell'">{{(parseFloat(item.amount) - parseFloat(item.left)).toFixed(2)}}</td>
                  <td style="width:12% ; text-align:center ; color:red" v-if="item.type == 'sell'">{{item.avg_price}}</td>
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
      <b-tabs no-body class="col-12 cardss" style="height:auto;margin-bottom:50px">
        




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
export default {
  name: 'pages-forums-list',
  metaInfo: {
    title: 'Forum list - Pages'
  },
  data: () => ({
    coinex: '',
    lev: 3,
    searchtext: '',
    info: [],
    infoback: [],
    balance: 0,
    boardinfo: [],
    balances: [],
    b_price: 0,
    lb_amount: 0,
    ls_amount: 0,
    lb_price: 0,
    ls_price: 0,
    lsb_amount: 0,
    lss_amount: 0,
    lsb_stop: 0,
    lss_stop: 0,
    lsb_limit: 0,
    lss_limit: 0,
    mb_amount: 0,
    s_price: 0,
    ms_amount: 0,
    pending: [],
    spending: [],
    marketinfo: [],
    finished: [],
    sfinished: [],
    mid: 0,
    op: {
    }
  }),
  mounted () {
    this.check()
    this.checklevel()
    this.getc()
    this.getb()
    this.getbal()
    this.getsp()
    this.getsf()
    this.getmi()
  },
  updated () {
    this.alertremover()
  },
  components: {
  },
  methods: {
    fillneg(a) {
      this.lb_price = a
      this.lsb_price = a
    },
    fillpos(a) {
      this.ls_price = a
      this.lss_price = a
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
    alertremover () {
      document.querySelectorAll('.delete').forEach(item => {
            item.addEventListener('click' , () => {
              item.parentElement.remove()
            })
            setTimeout(() => {
              item.parentElement.remove()
            }, 3000);
          })
    },
    tv () {
      new TradingView.widget(
        {
        "width": 550,
        "height": 390,
        "symbol": `${this.$route.params.sym}`,
        "timezone": "Etc/UTC",
        "theme": "dark",
        "hide_side_toolbar": false,
        "style": "1",
        "locale": "en",
        "enable_publishing": false,
        "allow_symbol_change": true,
        "container_id": "tradingview_1be21"
      }
  );
    },
    async getp () {
      await axios
        .post('/cpp_pending', {sym: this.$route.params.sym})
        .then(response => {
          this.pending = response.data.data.records
          setTimeout(() => {
            this.getp()
          }, 5000)
        })
    },
    click (name) {
      document.getElementById(name).querySelector('a').click()
    },
    async getf () {
      await axios
        .post('/cpp_finished', {sym: this.$route.params.sym , mid: this.mid})
        .then(response => {
          this.finished = response.data.data.records
          setTimeout(() => {
            this.getf()
          }, 2000)
        })
    },
    async getsp () {
      await axios
        .post('/cpp_stop_pending', {sym: this.$route.params.sym})
        .then(response => {
          this.pending = response.data.data.records
          setTimeout(() => {
            this.getsp()
          }, 5000)
        })
    },
    async getmi () {
      await axios
        .get('/olpmarketinfo')
        .then(response => {
          for (var item of response.data.data){
            if (item.name === this.$route.params.sym){
              this.marketinfo = item
            }
          }
          setTimeout(() => {
            this.getsp()
          }, 5000)
        })
    },
    async getsf () {
      await axios
        .post('/cpp_stop_finished', {sym: this.$route.params.sym , mid: this.mid})
        .then(response => {
          this.finished = response.data.data.records
          setTimeout(() => {
            this.getsf()
          }, 2000)
        })
    },
    async getc () {
      await axios
        .get('/olptradeinfo')
        .then(response => {
          this.info = response.data
          this.infoback = response.data
        })
    },
    async getb () {
      await axios
        .post('/olpboardinfo',{sym: this.$route.params.sym})
        .then(response => {
          this.boardinfo = response.data.data
          setTimeout(() => {
              this.getb()
          }, 20)
        })
    },
    async getbal () {
      await axios
        .post('/cpp_balance')
        .then(response => {
          this.balances = response.data.data['USDT']
          this.getp()
          this.getf()
          this.tv()
        })
    },
    async getopen () {
      await axios
        .get('/cpp_open')
        .then(response => {
          this.balances = response
          this.balance = parseFloat(response.data.available).toFixed(10)
          setTimeout(() => {
              this.getb()
          }, 2000)
        })
    },
    async cpclose (market , id) {
      await axios
        .post('/cpp_close', { sym: market, id: parseInt(id), mid: this.mid })
        .then(response => {
          this.getp()
          this.getbal()
        })
    },
    async adjustleverage () {
      await axios
        .post('/cpp_adjustleverage', { leverage: this.lev , sym : this.$route.params.sym})
        .then(response => {
          toast({
            message: 'اهرم شما با موفقیت تغییر کرد',
            type: 'is-success',
            dismissible: true,
            animate: { in: 'fadeIn', out: 'fadeOut' },
          })
          localStorage.setItem(`${this.$route.params.sym}_leverage` , this.lev)
        })
    },
    async msell () {
      await axios
        .post('/cpp_market_order', { sym: this.$route.params.sym, type: 1, amount: this.ms_amount })
        .then(response => {
          toast({
            message: 'با موفقیت انجام شد',
            type: 'is-success',
            dismissible: true,
            animate: { in: 'fadeIn', out: 'fadeOut' },
          })
          this.getp()
          this.getbal()
        })
    },
    async mbuy () {
      await axios
        .post('/cpp_market_order', {  sym: this.$route.params.sym, type: 2, amount: this.mb_amount})
        .then(response => {
          if (response.code !== 0){
            var message = response.data.message
            if (message.includes('balance')){
              message = 'موجودی کافی نیست'
            }
            toast({
            message: message,
            type: 'is-danger',
            dismissible: true,
            animate: { in: 'fadeIn', out: 'fadeOut' },
          })
          return
          }
          toast({
            message: 'با موفقیت انجام شد',
            type: 'is-success',
            dismissible: true,
            animate: { in: 'fadeIn', out: 'fadeOut' },
          })
          this.getp()
          this.getbal()
        })
        .catch(response =>{
        })
    },
    async lsell () {
      await axios
        .post('/cpp_limit_order', { sym: this.$route.params.sym, type: 1, amount: this.ls_amount, price: this.ls_price})
        .then(response => {
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
          this.getbal()
        })
    },
    async lbuy () {
      await axios
        .post('/cpp_limit_order', {  sym: this.$route.params.sym, type: 2, amount: this.lb_amount,  price: this.lb_price })
        .then(response => {
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
          this.getbal()
        })
    },
    async lssell () {
      await axios
        .post('/cpp_stop_limit_order', { sym: this.$route.params.sym, type: 1, amount: this.lss_amount, price: this.lss_limit, stop_price: this.lss_stop})
        .then(response => {
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
          this.getbal()
        })
    },
    async lsbuy () {
      await axios
        .post('/cpp_stop_limit_order', {  sym: this.$route.params.sym, type: 2, amount: this.lsb_amount,  price: this.lsb_limit, stop_price: this.lsb_stop})
        .then(response => {
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
          this.getbal()
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
      await axios
        .post('/cpp_cancel_order', {  sym: this.$route.params.sym, id:id })
        .then(response => {
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
          this.getbal()
        })
    },
    async scancel (id) {
      await axios
        .post('/cpp_stop_cancel_order', {  sym: this.$route.params.sym, id:id })
        .then(response => {
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
          this.getbal()
        })
    },
    msbalance () {
      this.ms_amount = (parseFloat(this.balances.available) - 0.0000005).toFixed(6)
    },
    mbbalance () {
      this.mb_amount = (parseFloat(this.balances.available) - 0.0000005).toFixed(6)
    },
    lsbalance () {
      this.ls_amount = (parseFloat(this.balances.available) - 0.0000005).toFixed(6)
    },
    lbbalance () {
      this.lb_amount = (parseFloat(this.balances.available) - 0.0000005).toFixed(6)
    },
    lssbalance () {
      this.lss_amount = (parseFloat(this.balances.available) - 0.0000005).toFixed(6)
    },
    lsbbalance () {
      this.lsb_amount = (parseFloat(this.balances.available) - 0.0000005).toFixed(6)
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
</style>
