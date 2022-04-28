<template>
  <div>
    <div class="banb">
      <!-- Card stats -->
      
      <b-row style="top:110px ; position:absolute ; height:300px ; width:100%">
        <b-col style="background:none!important">
          <div class="mainban" style="height: 150px ;margin:auto; text-align:center">
            <h2 class="mainhead" style="">خرید و فروش امن بیت‌کوین و ارزهای دیجیتال</h2>
            <h2 class="mainsubhead" style="color:black">به بزرگترین بازار ارز دیجیتال ایران بپیوندید</h2>
          </div>
        </b-col>
      </b-row>
    </div>



          <b-input v-if="infoback2 && infoback && info" style="margin-top:5px;margin-bottom:5px" v-model="searchtext" placeholder="...جستجو"  @input="search()"></b-input>
          <table class="table " style="direction:rtl!important;margin:0">
          <thead>
            <tr>
              <th class="coin cent">نوع ارز</th>
              <th class="coin cent nnmobile"> قیمت دلاری</th>
              <th class="coin cent">قیمت خرید(ریال)</th>
              <th class="coin cent"> قیمت فروش(ریال)</th>
              <th v-if="false" class="coin cent nnmobile">عملیات</th>
            </tr>
          </thead>
          </table>
          <div class="table-responsive " style="margin-bottom:-20px; max-height:450px; overflow:auto ; background:white" >
        <table class="table " style="direction:rtl!important">
          <tbody v-if="info" style="font:20px 'arial'; max-height:320px" >
            <tr v-if="pp[2] && ('USDT').includes(searchtext.toUpperCase())">
              <td class="coin cent"><template class="wmobile"><img src="https://raw.githubusercontent.com/ErikThiart/cryptocurrency-icons/master/64/tether.png" alt=""></template><br>{{pp[2].id}}</td>
              <td class="coin cent nnmobile"><br>{{USDTprice}}</td>
              <td class="coin cent" style="color:green"><router-link :to="'/buy/' + pp[2].id" class="btn btn-light" style="width: 100% ; color:green!important">خرید فوری <hr style="margin:5px ; padding:0 ; border-color:green"> {{(USDTprice * rialprice ).toFixed(2)}}</router-link > </td>
              <td class="coin cent" style="color:red"><router-link :to="'/sell/' + pp[2].id"  class="btn btn-light" style="width: 100% ; color:red!important">فروش فوری <hr style="margin:5px ; padding:0 ; border-color:red"> {{(USDTprice * rialprice * 0.994).toFixed(2) }}</router-link > </td>
              <th v-if="false" class="coin cent nnmobile"><router-link :to="'/sell/' + pp[2].id" class="btn btn-dark" style="margin:3px"> فروش فوری</router-link> <router-link :to="'/buy/' + pp[2].id" class="btn btn-dark" style="margin:3px">خرید فروی</router-link></th>
            </tr>
            <tr v-for="(item,name,idx) in info" v-bind:key="idx+10000">
              <td v-if="(name.replace('USDT' , '') === 'BTC' | name.replace('USDT' , '') === 'ETH' | name.replace('USDT' , '') === 'TRX' | name.replace('USDT' , '') === 'DOGE' | name.replace('USDT' , '') === 'SHIB' | name.replace('USDT' , '') === 'BNB' | name.replace('USDT' , '') === 'BCH' | name.replace('USDT' , '') === 'XRP')" class="coin cent"><template class="wmobile"><img class="iconcur" :src="`/icons/color/${name.replace('USDT' , '').toLowerCase()}.svg`" onerror="javascript:this.src='`/icons/color/${name.replace('USDT' , '').toLowerCase()}.png';"  alt=""></template><br>{{name.replace('USDT' , '')}}</td>
              <td v-if="(name.replace('USDT' , '') === 'BTC' | name.replace('USDT' , '') === 'ETH' | name.replace('USDT' , '') === 'TRX' | name.replace('USDT' , '') === 'DOGE' | name.replace('USDT' , '') === 'SHIB' | name.replace('USDT' , '') === 'BNB' | name.replace('USDT' , '') === 'BCH' | name.replace('USDT' , '') === 'XRP')" class="coin cent nnmobile"  ><br> {{item.buy}}</td>
              <td v-if="(name.replace('USDT' , '') === 'BTC' | name.replace('USDT' , '') === 'ETH' | name.replace('USDT' , '') === 'TRX' | name.replace('USDT' , '') === 'DOGE' | name.replace('USDT' , '') === 'SHIB' | name.replace('USDT' , '') === 'BNB' | name.replace('USDT' , '') === 'BCH' | name.replace('USDT' , '') === 'XRP')" class="coin cent" style="color:green"><router-link :to="'/buy/' + name.replace('USDT' , '')"  class="btn btn-light" style="width: 100% ; color:green!important">خرید فوری <hr style="margin:5px ; padding:0 ; border-color:green"> {{(item.buy * 1.007 * rialprice).toFixed(2)}}</router-link > </td>
              <td v-if="(name.replace('USDT' , '') === 'BTC' | name.replace('USDT' , '') === 'ETH' | name.replace('USDT' , '') === 'TRX' | name.replace('USDT' , '') === 'DOGE' | name.replace('USDT' , '') === 'SHIB' | name.replace('USDT' , '') === 'BNB' | name.replace('USDT' , '') === 'BCH' | name.replace('USDT' , '') === 'XRP')" class="coin cent" style="color:red"><router-link :to="'/sell/' + name.replace('USDT' , '')"  class="btn btn-light" style="width: 100% ; color:red!important">فروش فوری <hr style="margin:5px ; padding:0 ; border-color:red"> {{(item.buy * 1.001  * rialprice).toFixed(2)}}</router-link > </td>
              <th v-if="false" class="coin cent nnmobile"><router-link :to="'/sell/' + name.replace('USDT' , '')" class="btn btn-dark" style="margin:3px"> فروش فوری</router-link> <router-link :to="'/buy/' + name.replace('USDT' , '')" class="btn btn-dark" style="margin:3px">خرید فروی</router-link></th>
            </tr>
            <tr v-for="(item,name,idx) in info" v-bind:key="idx + 'd'">   
              <td v-if="!(name.replace('USDT' , '') === 'BTC' | name.replace('USDT' , '') === 'ETH' | name.replace('USDT' , '') === 'TRX' | name.replace('USDT' , '') === 'DOGE' | name.replace('USDT' , '') === 'SHIB' | name.replace('USDT' , '') === 'BNB' | name.replace('USDT' , '') === 'BCH' | name.replace('USDT' , '') === 'XRP')"  class="coin cent"><template><img class="iconcur" :src="`/icons/color/${name.replace('USDT' , '').toLowerCase()}.svg`" onerror="javascript:this.src='`/icons/color/${name.replace('USDT' , '').toLowerCase()}.png';"  alt=""></template><br>{{name.replace('USDT' , '')}}</td>
              <td v-if="!(name.replace('USDT' , '') === 'BTC' | name.replace('USDT' , '') === 'ETH' | name.replace('USDT' , '') === 'TRX' | name.replace('USDT' , '') === 'DOGE' | name.replace('USDT' , '') === 'SHIB' | name.replace('USDT' , '') === 'BNB' | name.replace('USDT' , '') === 'BCH' | name.replace('USDT' , '') === 'XRP')"  class="coin cent nnmobile"><br> {{item.buy}}</td>
              <td v-if="!(name.replace('USDT' , '') === 'BTC' | name.replace('USDT' , '') === 'ETH' | name.replace('USDT' , '') === 'TRX' | name.replace('USDT' , '') === 'DOGE' | name.replace('USDT' , '') === 'SHIB' | name.replace('USDT' , '') === 'BNB' | name.replace('USDT' , '') === 'BCH' | name.replace('USDT' , '') === 'XRP')"  class="coin cent" style="color:green"><router-link :to="'/buy/' + name.replace('USDT' , '')"  class="btn btn-light" style="width: 100% ; color:green!important">خرید فوری <hr style="margin:5px ; padding:0 ; border-color:green"> {{(item.buy * 1.007 * rialprice).toFixed(2)}}</router-link > </td>
              <td v-if="!(name.replace('USDT' , '') === 'BTC' | name.replace('USDT' , '') === 'ETH' | name.replace('USDT' , '') === 'TRX' | name.replace('USDT' , '') === 'DOGE' | name.replace('USDT' , '') === 'SHIB' | name.replace('USDT' , '') === 'BNB' | name.replace('USDT' , '') === 'BCH' | name.replace('USDT' , '') === 'XRP')"  class="coin cent" style="color:red"><router-link  :to="'/sell/' + name.replace('USDT' , '')" class="btn btn-light" style="width: 100% ; color:red!important">فروش فوری <hr style="margin:5px ; padding:0 ; border-color:red"> {{(item.buy * 1.001  * rialprice).toFixed(2)}}</router-link > </td>
              <th v-if="false" class="coin cent nnmobile"><router-link :to="'/sell/' + name.replace('USDT' , '')" class="btn btn-dark" style="margin:3px"> فروش فوری</router-link> <router-link :to="'/buy/' + name.replace('USDT' , '')" class="btn btn-dark" style="margin:3px">خرید فروی</router-link></th>
            </tr>
          </tbody>
          <tfoot>
            <tr>
                <th colspan="5" class="cent d-md-none"><router-link to="/dashboard" class="btn btn-dark">خرید | فروش</router-link></th>
            </tr>
          </tfoot>
        </table>
        </div>
        

        <div class="col-12 d-none d-md-block" style="min-height:490px;background:#ffffff; padding:50px ; text-align:right">
          <h2 style="text-align:center">چرا آمیزاکس ؟</h2><hr>
          <div v-for="(item , idx) in bottom" v-bind:key="idx + 'e'" style="width:25% ; padding:2% ; height:100%;background:white ; margin:4% ; ; border-color: #ececec ; border-width:1px ; margin-top:0 ; float:left" class="cent">
            <img style="width:150px ;height:150px" :src="item.get_pic" alt="">
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
          
        </div><br><br>
        <h2 v-if="posts.length" style="background:#ffffff;height:40px; margin:0; padding:10px; text-align:center"><br> آخرین اخبار</h2>
        <h2 style="background:#ffffff;height:40px; margin:0; padding:10px"><br> </h2>
        <h2 style="background:#ffffff;height:40px; margin:0; padding:10px"><br> </h2>
        <hr style="background:#ffffff;height:40px; margin:0; padding:10px">
        
        
        
        <div class="d-none d-md-block" v-for="(item , idx) in posts" v-bind:key="idx + 'g'" style="background:white ; padding-bottom:60px;" >
                  <div   style="height:350px;background:rgb(244, 248, 249);width:80%;margin:auto;border-radius:10px;border:solid #dfdfdf .5px;  text-align:right">
                    <div style="width:40%; float:right ; height:100%; padding-top:0">
                      <img style="width:100%;height:100%;border-radius:0 10px 10px 0" :src="item.get_pic" alt="">
                    </div>
                    <div style="width:60%; float:left; height:100% ; padding:10%; padding-top:5%">
                      <h4>{{item.title}} </h4>
                      <hr>
                      <p>{{item.minitext}}</p>
                    </div>
                  </div>
                  </div>



          <div class="d-md-none " v-for="(item , idx) in posts" v-bind:key="idx + 'h'" style="background:white ; padding-bottom:60px;" >
                  <div   style="height:auto;background:rgb(244, 248, 249);width:80%;margin:auto;border-radius:10px;border:solid #dfdfdf .5px;  text-align:center">
                    <div style="width:100%;   height:100%; padding-top:0">
                      <img style="width:100%;height:100%;border-radius: 10px 10px  0  0 " :src="item.get_pic" alt="">
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
          <img style="width:60px; height:70px " src="/img/brand/ars.png"><h style="color:white;font-size:35px; font-weight:bold ; margin-right: 10px">آمیزاکس</h>
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
    },
    data() {
      return {
        posts: [],
        tops: [],
        lists: get().SNPair,
        bottom: [],
        pp:[],
        searchtxt: '',
        searchtext: '',
        infoback: {},
        infoback2: {},
        USDTprice: 0,
        rialprice: 0,
        sym : 'BTCUSDT',
        dashboardinfo : [],
        info: {},
        his: [],
        slides: [],
        slides2: []
      }
    },
    methods: {
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
          this.info = response.data
          this.infoback = response.data
          this.infoback2 = response.data
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
      var i = 0
      for (const item of Object.keys(this.infoback2)){
        var key = String(item)
        if(key.replace('USDT' , '').includes(this.searchtext.toUpperCase())){
          if(this.infoback2[item]){
            this.info[item] = this.infoback2[item]
          }
        }
      }
    },
    },
    beforeMount(){
      this.getc2()
      this.gettop()
      this.getusdtprice()
      this.getbottom()
      this.getposts()
      this.getrialprice()
      this.review()
    }
  };
</script>
<style>
.banb{
  background: url('/IMG_6384.PNG') no-repeat;
  background-size: 170% 100%;
  background-position-x:center;
  height:850px; 
  width:100%;
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
  font:48px 'yekan';
  color:black;
  font-weight:bolder
}
.mainban{
  width:65%
}
.coin{
  width:25%
}
.iconcur{
  width: 12%; 
  margin:5%
}
@media only screen and (max-width: 1024px) {
.nnmobile{
  display: none;
}
.mainhead{
  font:25px 'yekan';
  color:black;
  font-weight:bolder
}
.mainsubhead{
  font:18px 'yekan';
  color:black;
}
.banb{
  height:500px; 
  width:100%;
}
.mainban{
  width:95%;
  margin-top:-50px
}
.banb{
  background: url('/IMG_6384.PNG') no-repeat;
  background-size: 170% 100%;
  background-position-x:center;
  height:500px; 
  width:100%;
}
.coin{
  width:33%
}
td , th {
  padding: 0 !important;
}
.iconcur{
  width: 50%; 
  margin:5%
}
.btn{
  width: 90% !important;
  height:90%;
  margin:5%
}
}
</style>
