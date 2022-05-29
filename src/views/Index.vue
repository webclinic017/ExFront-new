<template>
  <div>
    <div class="ban">
      <!-- Card stats -->
      
      <b-row style="top:100px ; position:absolute ; height:300px ; width:100% ; margin:0 ; padding:0">
        <b-col style="background:none!important ; margin:0 ; padding:0">
          <div class="mainban" style="height: 150px ;margin:auto; text-align:center">
            <div style=" border-radius: 20px;"><br><br>
              <h2 class="mainhead" style="color:#cecece ; text-shadow: black 1.5px 1.5px">خرید و فروش امن بیت‌کوین و ارزهای دیجیتال</h2>
              <h2 class="mainsubhead" style="color:#898989 ; text-shadow: black 0.5px 0.5px">به بزرگترین بازار ارز دیجیتال ایران بپیوندید</h2><br><br>
            </div><br>
            <div style="direction:rtl ; width:90%; margin-right:5%!important; margin-left:5%!important" ><br>
                <button class="btn btn-success" type="button" style="width:100%">هم اکنون ثبت نام کنید</button>
            </div>
          </div>
        </b-col>

      </b-row>
    </div>



          <b-input v-if="infoback2 && infoback && info" style="margin-top:5px;margin-bottom:5px" v-model="searchtext" placeholder="...جستجو"  @input="search()"></b-input>
          <button style="margin-top:10px ; margin-bottom:15px" class="btn btn-dark" @click="sorted = true ;sorter('vol')">حجم بازار</button>
          <button style="margin-top:10px ; margin-bottom:15px" class="btn btn-dark" @click="sorted = true ;sorter('buy')">بیشترین قیمت</button>
          <button style="margin-top:10px ; margin-bottom:15px" class="btn btn-dark" @click="sorted = true ;sorter('change')">میزان رشد</button>

          <br>
          <table class="table " style="direction:rtl!important;margin:0; max-height:350px">
          <thead>
            <tr>
              <th class=" cent">نوع ارز</th>
              <th class=" cent omobile"> قیمت </th>
              <th class=" cent nmobile"> قیمت دلاری</th>
              <th class=" cent nmobile">قیمت خرید(ریال)</th>
              <th class=" cent nmobile"> قیمت فروش(ریال)</th>
              <th class=" cent nmobile"> 24 ساعت گذشته</th>
              <th class=" cent">عملیات</th>
            </tr>
          </thead>
          <tbody v-if="info && (!sorted)" style="font:20px 'arial'; max-height:320px" >
            <tr v-for="(item,name,idx) in info" v-bind:key="idx+100001">
              <td v-if="(name.replace('USDT' , '') === 'USDT')" class=" cent"><template class=""><br class="omobile"><br class="omobile"><img style="width:48px" src="https://raw.githubusercontent.com/ErikThiart/cryptocurrency-icons/master/64/tether.png" alt=""></template><br>{{'USDT'}}</td>
              <td v-if="(name.replace('USDT' , '') === 'USDT')" class=" cent"><br><a > {{USDTprice}}<br></a><hr style="margin:0!important" class="omobile"> <a class="omobile">خرید : <br>{{(USDTprice * rialprice ).toFixed(2)}} <br> فروش :‌ <br>{{(USDTprice * rialprice * 0.994).toFixed(2) }} </a> </td>
              <td v-if="(name.replace('USDT' , '') === 'USDT')" class=" cent nmobile" style="color:green"><br>  {{(USDTprice * rialprice ).toFixed(2)}} </td>
              <td v-if="(name.replace('USDT' , '') === 'USDT')" class=" cent nmobile" style="color:red"><br>  {{(USDTprice * rialprice * 0.994).toFixed(2) }} </td>
              <td v-if="(name.replace('USDT' , '') === 'USDT')" class=" cent nmobile" style="color:red"><br>  - </td>
              <th v-if="(name.replace('USDT' , '') === 'USDT')" style="padding-top:25px" class=" cent"><router-link :to="'/sell/' + 'USDT'" class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'"> فروش </router-link> <router-link :to="'/buy/' + 'USDT'" class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'">خرید </router-link><router-link   :to="`/cpwallets/${'USDT'}/deposit`" class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'">واریز</router-link><router-link   :to="`/cpwallets/${'USDT'}/withdraw`" class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'">برداشت</router-link></th>
            </tr>
            <tr v-for="(item,name,idx) in info" v-bind:key="idx+10000">
              <td v-if="(name.replace('USDT' , '') === 'BTC' | name.replace('USDT' , '') === 'ETH' | name.replace('USDT' , '') === 'TRX' | name.replace('USDT' , '') === 'DOGE' | name.replace('USDT' , '') === 'SHIB' | name.replace('USDT' , '') === 'BNB' | name.replace('USDT' , '') === 'BCH' | name.replace('USDT' , '') === 'XRP')" class=" cent"><template class=""><br class="omobile"><br class="omobile"><img style="width:48px" class="" :src="`/icons/color/${name.replace('USDT' , '').toLowerCase()}.svg`" :onerror="`javascript:this.src='/icons/color/${name.replace('USDT' , '').toLowerCase()}.png';`"  alt=""></template><br>{{name.replace('USDT' , '')}}</td>
              <td v-if="(name.replace('USDT' , '') === 'BTC' | name.replace('USDT' , '') === 'ETH' | name.replace('USDT' , '') === 'TRX' | name.replace('USDT' , '') === 'DOGE' | name.replace('USDT' , '') === 'SHIB' | name.replace('USDT' , '') === 'BNB' | name.replace('USDT' , '') === 'BCH' | name.replace('USDT' , '') === 'XRP')" class=" cent"  ><br><a > {{item.buy}}<br></a><hr style="margin:0!important" class="omobile"> <a class="omobile">خرید : <br>{{(item.buy * 1.007 * rialprice).toFixed(0)}} <br> فروش :‌ <br>{{(item.buy * 1.001  * rialprice).toFixed(0)}}</a> </td>
              <td v-if="(name.replace('USDT' , '') === 'BTC' | name.replace('USDT' , '') === 'ETH' | name.replace('USDT' , '') === 'TRX' | name.replace('USDT' , '') === 'DOGE' | name.replace('USDT' , '') === 'SHIB' | name.replace('USDT' , '') === 'BNB' | name.replace('USDT' , '') === 'BCH' | name.replace('USDT' , '') === 'XRP')" class=" cent nmobile" style="color:green"><br> {{(item.buy * 1.007 * rialprice).toFixed(0)}}</td>
              <td v-if="(name.replace('USDT' , '') === 'BTC' | name.replace('USDT' , '') === 'ETH' | name.replace('USDT' , '') === 'TRX' | name.replace('USDT' , '') === 'DOGE' | name.replace('USDT' , '') === 'SHIB' | name.replace('USDT' , '') === 'BNB' | name.replace('USDT' , '') === 'BCH' | name.replace('USDT' , '') === 'XRP')" class=" cent nmobile" style="color:red"><br> {{(item.buy * 1.001  * rialprice).toFixed(0)}}</td>
              <td v-if="(name.replace('USDT' , '') === 'BTC' | name.replace('USDT' , '') === 'ETH' | name.replace('USDT' , '') === 'TRX' | name.replace('USDT' , '') === 'DOGE' | name.replace('USDT' , '') === 'SHIB' | name.replace('USDT' , '') === 'BNB' | name.replace('USDT' , '') === 'BCH' | name.replace('USDT' , '') === 'XRP')" class=" cent nmobile" style="color:red"><br><a v-if="(parseFloat(item.change)).toFixed(1) > 0" style="color:green"> {{(parseFloat(item.change)).toFixed(1).toString().replace('-', '')}} </a><a v-if="(parseFloat(item.change)).toFixed(1) < 0" style="color:red"> {{(parseFloat(item.change)).toFixed(1).toString().replace('-', '')}} </a> <a v-if="!(parseFloat(item.change))">-</a> </td>
              <th style="padding-top:25px" v-if="(name.replace('USDT' , '') === 'BTC' | name.replace('USDT' , '') === 'ETH' | name.replace('USDT' , '') === 'TRX' | name.replace('USDT' , '') === 'DOGE' | name.replace('USDT' , '') === 'SHIB' | name.replace('USDT' , '') === 'BNB' | name.replace('USDT' , '') === 'BCH' | name.replace('USDT' , '') === 'XRP')" class=" cent"><router-link :to="'/sell/' + name.replace('USDT' , '')" class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'"> فروش </router-link> <router-link :to="'/buy/' + name.replace('USDT' , '')" class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'">خرید </router-link><router-link   :to="`/cpwallets/${name.replace('USDT' , '')}/deposit`" class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'">واریز</router-link><router-link   :to="`/cpwallets/${name.replace('USDT' , '')}/withdraw`" class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'">برداشت</router-link></th>
            </tr>
            <tr v-for="(item,name,idx) in info" v-bind:key="idx + 'd'">   
              <td v-if="name.replace('USDT' , '') !== 'USDT' && !(name.replace('USDT' , '') === 'BTC' | name.replace('USDT' , '') === 'ETH' | name.replace('USDT' , '') === 'TRX' | name.replace('USDT' , '') === 'DOGE' | name.replace('USDT' , '') === 'SHIB' | name.replace('USDT' , '') === 'BNB' | name.replace('USDT' , '') === 'BCH' | name.replace('USDT' , '') === 'XRP') | name.replace('USDT' , '') "  class=" cent"><template><br class="omobile"><br class="omobile"><img style="width:48px" class="" :src="`/icons/color/${name.replace('USDT' , '').toLowerCase()}.svg`" :onerror="`javascript:this.src='/icons/color/${name.replace('USDT' , '').toLowerCase()}.png';`"  alt=""></template><br>{{name.replace('USDT' , '')}}mm</td>
              <td v-if="name.replace('USDT' , '') !== 'USDT' && !(name.replace('USDT' , '') === 'BTC' | name.replace('USDT' , '') === 'ETH' | name.replace('USDT' , '') === 'TRX' | name.replace('USDT' , '') === 'DOGE' | name.replace('USDT' , '') === 'SHIB' | name.replace('USDT' , '') === 'BNB' | name.replace('USDT' , '') === 'BCH' | name.replace('USDT' , '') === 'XRP') | name.replace('USDT' , '') "  class=" cent"><br  class="nmobile"><br> <a >{{item.buy}}<br></a><hr style="margin:0!important" class="omobile"> <a class="omobile">خرید :<br> {{(item.buy * 1.007 * rialprice).toFixed(0)}} <br> فروش :‌ <br>{{(item.buy * 1.001  * rialprice).toFixed(0)}}</a> </td>
              <td v-if="name.replace('USDT' , '') !== 'USDT' && !(name.replace('USDT' , '') === 'BTC' | name.replace('USDT' , '') === 'ETH' | name.replace('USDT' , '') === 'TRX' | name.replace('USDT' , '') === 'DOGE' | name.replace('USDT' , '') === 'SHIB' | name.replace('USDT' , '') === 'BNB' | name.replace('USDT' , '') === 'BCH' | name.replace('USDT' , '') === 'XRP') | name.replace('USDT' , '') "  class=" cent nmobile" style="color:green"><br>{{(item.buy * 1.007 * rialprice).toFixed(0)}} </td>
              <td v-if="name.replace('USDT' , '') !== 'USDT' && !(name.replace('USDT' , '') === 'BTC' | name.replace('USDT' , '') === 'ETH' | name.replace('USDT' , '') === 'TRX' | name.replace('USDT' , '') === 'DOGE' | name.replace('USDT' , '') === 'SHIB' | name.replace('USDT' , '') === 'BNB' | name.replace('USDT' , '') === 'BCH' | name.replace('USDT' , '') === 'XRP') | name.replace('USDT' , '') "  class=" cent nmobile" style="color:red"><br> {{(item.buy * 1.001  * rialprice).toFixed(0)}} </td>
              <td v-if="name.replace('USDT' , '') !== 'USDT' && !(name.replace('USDT' , '') === 'BTC' | name.replace('USDT' , '') === 'ETH' | name.replace('USDT' , '') === 'TRX' | name.replace('USDT' , '') === 'DOGE' | name.replace('USDT' , '') === 'SHIB' | name.replace('USDT' , '') === 'BNB' | name.replace('USDT' , '') === 'BCH' | name.replace('USDT' , '') === 'XRP') | name.replace('USDT' , '') "  class=" cent nmobile" style="color:red"><br><a v-if="(parseFloat(item.change)).toFixed(1) > 0" style="color:green"> {{(parseFloat(item.change)).toFixed(1).toString().replace('-', '')}} </a><a v-if="(parseFloat(item.change)).toFixed(1) < 0" style="color:red" > {{(parseFloat(item.change)).toFixed(1).toString().replace('-', '')}} </a><a v-if="!(parseFloat(item.change))">-</a>  </td>
              <th style="padding-top:25px" v-if="name.replace('USDT' , '') !== 'USDT' && !(name.replace('USDT' , '') === 'BTC' | name.replace('USDT' , '') === 'ETH' | name.replace('USDT' , '') === 'TRX' | name.replace('USDT' , '') === 'DOGE' | name.replace('USDT' , '') === 'SHIB' | name.replace('USDT' , '') === 'BNB' | name.replace('USDT' , '') === 'BCH' | name.replace('USDT' , '') === 'XRP') | name.replace('USDT' , '') === 'USDT'" class=" cent"><router-link :to="'/sell/' + name.replace('USDT' , '')" class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'"> فروش </router-link> <router-link :to="'/buy/' + name.replace('USDT' , '')" class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'">خرید </router-link><router-link   :to="`/cpwallets/${name.replace('USDT' , '')}/deposit`" class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'">واریز</router-link><router-link   :to="`/cpwallets/${name.replace('USDT' , '')}/withdraw`" class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'">برداشت</router-link></th>
            </tr>
          </tbody>
          <tbody v-if="info3 && (sorted)" style="font:20px 'arial'; max-height:320px" >

            <tr v-for="(item,name,idx) in sortedinfo" v-bind:key="idx+10000">
              <td v-if="name.replace('USDT' , '') !== 'USDT'" class=" cent"><template class=""><br class="omobile"><br class="omobile"><img style="width:48px" class="" :src="`/icons/color/${name.replace('USDT' , '').toLowerCase()}.svg`" :onerror="`javascript:this.src='/icons/color/${name.replace('USDT' , '').toLowerCase()}.png';`"  alt=""></template><br>{{name.replace('USDT' , '')}}</td>
              <td v-if="name.replace('USDT' , '') !== 'USDT'" class=" cent"  ><br><a > {{item.buy}}<br></a><hr style="margin:0!important" class="omobile"> <a class="omobile">خرید : <br>{{(item.buy * 1.007 * rialprice).toFixed(0)}} <br> فروش :‌ <br>{{(item.buy * 1.001  * rialprice).toFixed(0)}}</a> </td>
              <td v-if="name.replace('USDT' , '') !== 'USDT'" class=" cent nmobile" style="color:green"><br> {{(item.buy * 1.007 * rialprice).toFixed(0)}}</td>
              <td v-if="name.replace('USDT' , '') !== 'USDT'" class=" cent nmobile" style="color:red"><br> {{(item.buy * 1.001  * rialprice).toFixed(0)}}</td>
              <td v-if="name.replace('USDT' , '') !== 'USDT'" class=" cent nmobile" style="color:red"><br><a v-if="(parseFloat(item.change)).toFixed(1) > 0" style="color:green"> {{(parseFloat(item.change)).toFixed(1).toString().replace('-', '')}} </a><a v-if="(parseFloat(item.change)).toFixed(1) < 0" style="color:red"> {{(parseFloat(item.change)).toFixed(1).toString().replace('-', '')}} </a> <a v-if="!(parseFloat(item.change))">-</a> </td>
              <th v-if="name.replace('USDT' , '') !== 'USDT'" style="padding-top:25px" class=" cent"><router-link :to="'/sell/' + name.replace('USDT' , '')" class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'"> فروش </router-link> <router-link :to="'/buy/' + name.replace('USDT' , '')" class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'">خرید </router-link><router-link   :to="`/cpwallets/${name.replace('USDT' , '')}/deposit`" class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'">واریز</router-link><router-link   :to="`/cpwallets/${name.replace('USDT' , '')}/withdraw`" class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'">برداشت</router-link></th>

              <td v-if="name.replace('USDT' , '') === 'USDT'" class=" cent"><template class=""><br class="omobile"><br class="omobile"><img style="width:48px" src="https://raw.githubusercontent.com/ErikThiart/cryptocurrency-icons/master/64/tether.png" alt=""></template><br>{{'USDT'}}</td>
              <td v-if="name.replace('USDT' , '') === 'USDT'" class=" cent"><br><a > {{USDTprice}}<br></a><hr style="margin:0!important" class="omobile"> <a class="omobile">خرید : <br>{{(USDTprice * rialprice ).toFixed(2)}} <br> فروش :‌ <br>{{(USDTprice * rialprice * 0.994).toFixed(2) }} </a> </td>
              <td v-if="name.replace('USDT' , '') === 'USDT'" class=" cent nmobile" style="color:green"><br> {{(USDTprice * rialprice ).toFixed(2)}} </td>
              <td v-if="name.replace('USDT' , '') === 'USDT'" class=" cent nmobile" style="color:red"><br> {{(USDTprice * rialprice * 0.994).toFixed(2) }} </td>
              <td v-if="name.replace('USDT' , '') === 'USDT'" class=" cent nmobile" style="color:red"><br> - </td>
              <th v-if="name.replace('USDT' , '') === 'USDT'" style="padding-top:25px" class=" cent"><router-link :to="'/sell/' + 'USDT'" class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'"> فروش </router-link> <router-link :to="'/buy/' + 'USDT'" class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'">خرید </router-link><router-link   :to="`/cpwallets/${'USDT'}/deposit`" class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'">واریز</router-link><router-link   :to="`/cpwallets/${'USDT'}/withdraw`" class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'">برداشت</router-link></th>
            </tr>
          </tbody>
        </table>
        <br><br><br>
        

        <div class="col-12 d-none d-md-block" style="min-height:490px; padding:50px ; text-align:right">
          <h2 style="text-align:center">چرا آمیزاکس ؟</h2><br><br>
          <div v-for="(item , idx) in bottom" v-bind:key="idx + 'e'" style="width:25% ; padding:2% ; height:100%; margin:4% ; ; border-color: #ececec ; border-width:1px ; margin-top:0 ; float:left" class="cent">
            <img style="width:180px ;height:180px" :src="item.get_pic" alt=""><br><br>
            <h4 class="cent">{{item.title}}</h4><br>
            <p>{{item.minitext}}</p>
          </div>
        </div>

        <div class="col-12 d-md-none " style="min-height:auto;background:#ffffff; padding:50px ; text-align:right">
          <h2 style="text-align:center">چرا آمیزاکس ؟</h2><hr>
          <div v-for="(item , idx) in bottom" v-bind:key="idx + 'f'" style="width:100% ; padding:2% ; background:white ; margin:auto ; margin-bottom:4% ; ; border-color: #ececec ; border-width:1px ; margin-top:0" class="cent">
            <img style="width:150px " :src="item.get_pic" alt="">
            <h4 class="cent">{{item.title}}</h4><br>
            <p >{{item.minitext}}</p>
          </div>
          
        </div><br><br><br><br>
        <h2 v-if="posts.length" style="height:40px; margin:0; padding:10px; text-align:center"><br> آخرین اخبار</h2>
        <h2 style="height:40px; margin:0; padding:10px"><br> </h2>
        <h2 style="height:40px; margin:0; padding:10px"><br> </h2>
        <br style="height:40px; margin:0; padding:10px"><br>
        
        
        
        <div class="d-none d-md-block" v-for="(item , idx) in posts" v-bind:key="idx + 'g'" style=" padding-bottom:60px;" >
                  <div   style="height:350px;;width:80%;margin:auto;border:solid rgba(125,125,125,0.5) .5px;  text-align:right">
                    <div style="width:40%; float:right ; height:100%; padding-top:0">
                      <img style="width:100%;height:100%;" :src="item.get_pic" alt="">
                    </div>
                    <div style="width:60%; float:left; height:100% ; padding:10%; padding-top:5%">
                      <h4>{{item.title}} </h4>
                      <hr>
                      <p>{{item.minitext}}</p>
                    </div>
                  </div>
                  </div>



          <div class="d-md-none " v-for="(item , idx) in posts" v-bind:key="idx + 'h'" style=" padding-bottom:60px;" >
                  <div   style="height:auto;;width:80%;margin:auto;border:solid rgba(125,125,125,0.5) .5px;  text-align:center">
                    <div style="width:100%;   height:100%; padding-top:0">
                      <img style="width:100%;height:100%;" :src="item.get_pic" alt="">
                    </div>
                    <div style="width:100%; height:100% ; padding:10%; padding-top:5%;  text-align:justify">
                      <h4>{{item.title}} ssss</h4>
                      <hr>
                      <p>{{item.minitext}}</p>
                    </div>
                  </div>
                  </div>

        <footer class="d-none d-md-block" style="background:#222;color:white; text-align:right ;">
          <div class="col-12" style="height:250px">
            <div class="col-4" style="height:100% ; float:right ; padding:2%">
              <b-navbar-brand to="/">
          <img style="width:60px; height:70px " src="/img/brand/ars.png"><a style="color:white;font-size:35px; font-weight:bold ; margin-right: 10px">آمیزاکس</a>
              </b-navbar-brand><br><br>
              </div>
            <div class="col-3" style="height:100% ; float:right ; padding:2%">
              <h3 style="color:white ; font-size:25px">خدمات ما</h3>
              <br>
              <router-link to="/pages/margin-trade"><h6 style="color:grey ; font-size:14px">معاملات مرجین</h6></router-link>
              <router-link to="/pages/perpetual-trade"><h6 style="color:grey ; font-size:14px">معاملات پرپشوال</h6></router-link>
              <router-link to="/pages/exchange"><h6 style="color:grey ; font-size:14px"> اکسچینج</h6></router-link>
              <router-link to="/pages/buysell"><h6 style="color:grey ; font-size:14px">خرید و فروش</h6></router-link>
              <router-link to="/pages/onlinetrading"><h6 style="color:grey ; font-size:14px">تریدینگ لحظه ای </h6></router-link>
              </div>
            <div class="col-3" style="height:100% ; float:right ; padding:2%">
              <h3 style="color:white ; font-size:25px">درباره ما</h3>
              <br>
              <router-link to="/pages/group"><h6 style="color:grey ; font-size:14px">اعضای شرکت</h6></router-link>
              <router-link to="/pages/history"><h6 style="color:grey ; font-size:14px">تاریخچه</h6></router-link>
              <router-link to="/pages/line"><h6 style="color:grey ; font-size:14px">زمینه فعالیت</h6></router-link>
              <router-link to="/pages/rules"><h6 style="color:grey ; font-size:14px">قوانین و مقررات </h6></router-link>
              </div>
              <div class="col-2" style="height:100% ; float:right ; padding:2%">
              
              <h3 style="color:white ; font-size:25px">ارتباط با ما</h3>
              <br>
              <router-link to="/ticketadd"><h6 style="color:grey ; font-size:14px">پشتیبانی آنلاین</h6></router-link>
              <router-link to="/contacts"><h6 style="color:grey ; font-size:14px">تماس با ما</h6></router-link>
              </div>
          </div>
        </footer>


        <footer class="d-md-none" style="background:#222;color:white; text-align:center ;">
          <div class="col-12" style="height:auto">
            <div class="col-12" style="height:100% ; padding:2%">
              <b-navbar-brand to="/" style="margin:0">
          <img style="width:60px; height:70px ; margin:auto" src="/img/brand/ars.png">
              </b-navbar-brand><br><br>
              <h3 style="color:white ; font-size:25px">بهترین مکان برای ترید</h3>
              </div>
            <div class="col-12" style="height:100% ; margin-top:80px ; padding:2%">
              <h3 style="color:white ; font-size:25px">خدمات ما</h3>
              <br>
              <router-link to="/pages/margin-trade"><h6 style="color:grey ; font-size:14px">معاملات مرجین</h6></router-link>
              <router-link to="/pages/perpetual-trade"><h6 style="color:grey ; font-size:14px">معاملات پرپشوال</h6></router-link>
              <router-link to="/pages/exchange"><h6 style="color:grey ; font-size:14px"> اکسچینج</h6></router-link>
              <router-link to="/pages/buysell"><h6 style="color:grey ; font-size:14px">خرید و فروش</h6></router-link>
              <router-link to="/pages/onlinetrading"><h6 style="color:grey ; font-size:14px">تریدینگ لحظه ای </h6></router-link>

              </div>
            <div class="col-12" style="height:100% ; margin-top:80px ; padding:2%">
              <h3 style="color:white ; font-size:25px">درباره ما</h3>
              <br>
              <router-link to="/pages/group"><h6 style="color:grey ; font-size:14px">اعضای شرکت</h6></router-link>
              <router-link to="/pages/history"><h6 style="color:grey ; font-size:14px">تاریخچه</h6></router-link>
              <router-link to="/pages/line"><h6 style="color:grey ; font-size:14px">زمینه فعالیت</h6></router-link>
              <router-link to="/pages/rules"><h6 style="color:grey ; font-size:14px">قوانین و مقررات </h6></router-link>

              </div>
              <div class="col-12" style="height:100% ; margin-top:80px ; padding:2%">
              
              
              <h3 style="color:white ; font-size:25px">ارتباط با ما</h3>
              <br>
              <router-link to="/ticketadd"><h6 style="color:grey ; font-size:14px">پشتیبانی آنلاین</h6></router-link>
              <router-link to="/contacts"><h6 style="color:grey ; font-size:14px">تماس با ما</h6></router-link>              </div>
          </div>
        </footer>
  </div>
</template>
<script>
  // Charts
  import Vue from 'vue'
  import axios from 'axios'
  import Trend from 'vuetrend'
  import cryptocurrencies from 'cryptocurrencies'
  import { cryptoSymbol } from 'crypto-symbol'
  import LayoutNavbar from './../layout/LayoutNavbar'

  const { get } = cryptoSymbol({})
  // Components
  import BaseProgress from '@/components/BaseProgress';
  import StatsCard from '@/components/Cards/StatsCard';

  // Tables
  import SocialTrafficTable from './Dashboard/SocialTrafficTable';
  import PageVisitsTable from './Dashboard/PageVisitsTable';
  Vue.use(Trend)
  export default {
    components: {
      BaseProgress,
      StatsCard,
      PageVisitsTable,
      SocialTrafficTable,
      LayoutNavbar
    },
    computed:{
      sortedinfo: function() {
        const sortable = Object.fromEntries(
        Object.entries(this.info3).sort((a,b) =>{
          return parseFloat(b[1][this.currentSort]) - parseFloat(a[1][this.currentSort])
        })
      );
      console.log(Object.entries(this.info3))
      console.log(sortable)
      return sortable
      }
    },
    data: () => ({
        posts: [],
        tops: [],
        lists: get().SNPair,
        bottom: [],
        pp:[],
        searchtxt: '',
        searchtext: '',
        info: {},
        info2:{},
        info3: {},
        sorted : false,
        infoback: {},
        infoback2: {},
        infoback3: {},
        USDTprice: 0,
        currentSort:'vol',
        currentSortDir:'asc',
        rialprice: 0,
        sym : 'BTCUSDT',
        dashboardinfo : [],
        info: {},
        his: [],
        slides: [],
        slides2: []
    }),
    methods: {
      sorter(s) {
        if(s === this.currentSort) {
          this.currentSortDir = this.currentSortDir==='asc'?'desc':'asc';
        }
        this.currentSort = s;
      },
      async getusdtprice () {
      await axios
        .post('/cp_ticker' , {sym: 'USDT'})
        .then(response => {
          this.USDTprice = response.data.buy
          setTimeout(() => {
          }, 5000);
        })
    },
      async price () {
      localStorage.removeItem('uri')
      await axios
        .get('/indexprice')
        .then(response => {
          if(response.data.length > 0){
            this.pp = response.data
          }
          setTimeout(() => {
            this.price()
          }, 5000)
        })
    },
      async getrialprice () {
      await axios
        .get('/price' )
        .then(response => {
          this.rialprice = response.data[0].rial
        })
      },
    async getc () {
      await axios
        .get('/oltradeinfo3')
        .then(response => {
          response.data['USDTUSDT'] = 
          {
            "vol": 124160000000,
            "low": 3.2100,
            "open": 3.9851,
            "high": 4.1786,
            "last": 340.90767210002036,
            "buy": 3.4059,
            "buy_amount": 52.21796592,
            "sell": 3.4229,
            "sell_amount": 18.67342051
          }
          this.infoback = response.data
          if(!this.searchtext){
            this.info = response.data
          }else{
            this.search()
          }
          setTimeout(() => {
            this.getc()
          }, 5000)
        })
    },
    async getc2 () {
      await axios
        .get('/oltradeinfo3')
        .then(response => {
          response.data['USDTUSDT'] = 
          {
            "vol": 124160000000,
            "low": 3.2100,
            "open": 3.9851,
            "high": 4.1786,
            "last": 340.90767210002036,
            "buy": 3.4059,
            "buy_amount": 52.21796592,
            "sell": 3.4229,
            "sell_amount": 18.67342051
          }
          Object.assign(this.info, response.data)
          Object.assign(this.info3, response.data)
          Object.assign(this.infoback, response.data)
          Object.assign(this.infoback2, response.data)
          Object.assign(this.infoback3, response.data)
          this.getc()
        })
    },
    async gettop () {
      await axios
        .get('/topsticker')
        .then(response => {
          var temp = []
          var i=0
          for(var j=3 ; j-3 <=response.data.length ; j = j+3){
            temp = []
            for(i ; i<j; i++){
              if(response.data[i]){
                temp.push({get_pic:response.data[i].get_pic , title : response.data[i].title , text: response.data[i].text , minitext: response.data[i].minitext})
              }
            }
            i = j
            if(temp.length){
              if ( temp.length < 3){
                for(var f = 0 ; f < (3 - temp.length); f++){
                  temp.push({get_pic:response.data[f].get_pic , title : response.data[f].title , text: response.data[f].text , minitext: response.data[f].minitext})
                }
              }
              this.slides.push(temp)
            }
          }
          console.log(this.slides)
          var temp2 = []
          var i=0
            for(i ; i<response.data.length; i++){
             this.slides2.push({get_pic:response.data[i].get_pic , title : response.data[i].title , text: response.data[i].text})
            }
        })
        
    },
    async getbottom () {
      await axios
        .get('/bottomsticker')
        .then(response => {
          this.bottom = response.data
        })
    },
    async review () {
      await axios
        .get('/review')
        .then(response => {
        })
    },
    async getposts () {
      await axios
        .get('/mainpageposts')
        .then(response => {
          this.posts = response.data
        })
    },
    async history () {
      await axios
        .get('/indexhistory')
        .then(response => {
          this.his = response.data
        })
    },
    search () {
      this.info = {}
      for (const item of Object.keys(this.infoback2)){
        var key = String(item)
        if(key.replace('USDT' , '').includes(this.searchtext.toUpperCase())){
          if(this.infoback2[item]){
            this.info[item] = this.infoback2[item]
          }
        }
      }

      this.info3 = {}
      for (const item of Object.keys(this.infoback3)){
        var key = String(item)
        if(key.replace('USDT' , '').includes(this.searchtext.toUpperCase())){
          if(this.infoback3[item]){
            this.info3[item] = this.infoback3[item]
          }
        }
      }
    },
    },
    beforeMount(){
      this.getusdtprice()
      this.getc2()
      this.gettop()
      this.getbottom()
      this.getposts()
      this.getrialprice()
      this.review()
    }
  };
</script>
<style>
.ban{
  background-color: black;
  background: url(https://img.freepik.com/free-vector/smooth-white-wave-background_52683-55288.jpg?t=st=1653504682~exp=1653505282~hmac=6b2082001ebf577a66d33422bc039cb4370db5ee4b4a28d8b2e1c8263d19c3c3&w=740);
  background-size: 100% 100%;
  background-position-x:center;
  
  height:635px; 
  width:100%;
  opacity: .9;
  margin:0
}
.card-img-top {
  height:160px
}
.el-table .cell{
  padding-left: 0px;
  padding-right: 0px;
}
.carousel-indicators > li {
 background-color: var(--primary);
 margin-top: 20px;
}
.cent{
  text-align: center;
}
.mainhead{
  font:42px 'yekan';
  color:#ececec;
  font-weight:bolder
}
.mainban{
  width:100%;
  height: 510px!important;
  padding: 3%;
  color:#ececec
}
.omobile{
  display : none;
  font-size:16px
}
@media only screen and (max-width: 1023px) {
.mainhead{
  font:25px 'yekan';
  color:#ececec;
  font-weight:bolder
}
.mainsubhead{
  font:18px 'yekan';
  color:#ececec;
}
.ban{
  height:500px; 
  width:100%;
}
.mainban{
  width:95%;
  margin-top:-50px;
  height:auto!important;
  padding: 3%;
}
.ban{
  background: url('/IMG_6384.PNG') no-repeat;
  background-size: 100% 100%;
  background-position-x:center;
  height:500px; 
  width:100%;
}
td , th {
  padding: 0 !important;
}
.btn{
  width: 90% !important;
  height:90%;
  margin:5%
}
.nmobile{
  display : none
}
.omobile{
  display : block
}
}
</style>
