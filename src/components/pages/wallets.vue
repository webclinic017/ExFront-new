<template>
  <div>
    <b-card v-if="allamount" id="all" style="padding:0!important">
      <b-card-header>
        <h2>مجموع دارایی</h2>
      </b-card-header>
    <GChart
      style="width:30%;margin:right:30%"
      type="PieChart"
      :options="options"
      :data="data"
    />    <br>
    <h2 style="text-align:center">مجموع دارایی به دلار : {{allamount.toFixed(2)}}</h2>
    <h2 style="text-align:center">مجموع دارایی به ریال : {{allamountrial}}</h2>
    </b-card>

    <br><br>
    <b-card no-body>
      <b-card-header>
          موجودی ریالی 
        </b-card-header>      
        <div class="table-responsive">
        <table class="table" style="direction:rtl!important">
          <thead>
            <tr>
              <th class="col-3">موجودی</th>
              <th class="col-9">عملیات</th>
            </tr>
          </thead>
        <tbody>
          <tr v-for="(section) in wallets2" v-bind:key="section.id">
                  <td style="width:15%;font-wieght:bold;font-family:'arial';font-size:20px"><router-link :to="`#`" class="text-big font-weight-semibold" >
                  {{section.amount}}
                  </router-link></td>
                  <td style="padding:0;font-family:'arial';font-size:14px"><router-link  :to="`/wallets/1/withdraw`" class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'">برداشت</router-link><router-link :to="`/transactions`"  class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'"> تاریخچه </router-link><router-link   :to="`/deposit`" class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'">واریز</router-link></td>
          </tr>
        </tbody>
        </table>
        </div>
    </b-card>

      <br><br>
      <b-card no-body>
      <b-card-header>
          کیف های ترید 
        </b-card-header>
      <input class="form-control" type="search" placeholder="search..." style="textalign:left;direction:ltr;font-family:'arial'" @input="search2()" v-model="searchtext"><br>
      
        <div class="table-responsive">
        <table class="table" style="direction:rtl!important">
          <thead>
            <tr>
              <th>Currency</th>
              <th>Available</th>
              <th>Operations</th>
            </tr>
          </thead>
        <tbody>
          <tr v-for="(section) in wallets" v-bind:key="section.id">
                  <td v-if="parseFloat(section.balance) !== 0 " style="width:15%;font-wieght:bold;font-family:'arial';font-size:20px"><router-link :to="`#`" class="text-big font-weight-semibold" >
                  <img style="width:48px" class="" :src="`/icons/color/${section.brand.toLowerCase()}.svg`" :onerror="`javascript:this.src='/icons/color/${section.brand.toLowerCase()}.png';`"  alt=""><br>{{section.brand}}
                  </router-link></td>
                  <td v-if="parseFloat(section.balance) !== 0" style="padding:20px;font-family:'arial';font-size:14px"> <router-link :to="`#`"><a v-if="(parseFloat(section.balance) === 0)">0</a> 
                  {{section.balance}}<br>
                  <div v-if="!(section.brand.includes('USD'))">
                  <a v-if="prices[section.brand + 'USDT']">{{(section.balance * prices[section.brand + 'USDT'].last).toFixed(2)}} USD</a><br>
                  <a v-if="prices[section.brand + 'USDT']">{{(section.balance * prices[section.brand + 'USDT'].last * rialprice).toFixed(0)}} ریال</a><br>
                  <a v-if="(!prices[section.brand + 'USDT'])"> در حال حاضر قیمت دلاری و <br> ریالی این ارز در دسترس نیست</a><br>
                  </div>
                  <div v-if="(section.brand.includes('USD'))">
                  <a >{{section.balance}} USD</a><br>
                  <a >{{(section.balance * rialprice).toFixed(0)}} ریال</a><br>
                  </div>
                  </router-link></td>
                  <td v-if="parseFloat(section.balance) !== 0" style="padding:0;font-family:'arial';font-size:14px"><router-link  :to="`/cpwallets/${section.name}/withdraw`" class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'">برداشت</router-link><router-link :to="`/cpwallets/${section.name}/history`"  class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'"> تاریخچه </router-link><router-link :to="`/buy/${section.brand}`"  class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'"> خرید </router-link><router-link :to="`/sell/${section.brand}`"  class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'"> فروش </router-link><router-link   :to="`/cpwallets/${section.name}/deposit`" class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'">واریز</router-link></td>
          </tr>
          <tr v-for="(section) in wallets" v-bind:key="section.name">
                  <td v-if="(section.brand == 'USDT' |section.brand == 'BTC' |section.brand == 'ETH' |section.brand == 'TRX' && (parseFloat(section.balance) === 0))" style="width:15%;font-wieght:bold;font-family:'arial';font-size:20px"><router-link :to="`#`" class="text-big font-weight-semibold" >
                  <img style="width:48px" class="" :src="`/icons/color/${section.brand.toLowerCase()}.svg`" :onerror="`javascript:this.src='/icons/color/${section.brand.toLowerCase()}.png';`"  alt=""><br>{{section.brand}}
                  </router-link></td>
                  <td v-if="(section.brand == 'USDT' |section.brand == 'BTC' |section.brand == 'ETH' |section.brand == 'TRX' && (parseFloat(section.balance) === 0))" style="padding:20px;font-family:'arial';font-size:14px"> <router-link :to="`#`"><a v-if="(parseFloat(section.balance) === 0)">0</a> {{section.balance}}</router-link></td>
                  <td v-if="(section.brand == 'USDT' |section.brand == 'BTC' |section.brand == 'ETH' |section.brand == 'TRX' && (parseFloat(section.balance) === 0))" style="padding:0;font-family:'arial';font-size:14px"><router-link  :to="`/cpwallets/${section.name}/withdraw`" class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'">برداشت</router-link><router-link :to="`/cpwallets/${section.name}/history`"  class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'"> تاریخچه </router-link><router-link :to="`/buy/${section.brand}`"  class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'"> خرید </router-link><router-link :to="`/sell/${section.brand}`"  class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'"> فروش </router-link><router-link   :to="`/cpwallets/${section.name}/deposit`" class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'">واریز</router-link></td>
          </tr>
          <tr v-for="(section) in wallets" v-bind:key="section.id">
                  <td v-if="!(section.brand == 'USDT' |section.brand == 'BTC' |section.brand == 'ETH' |section.brand == 'TRX') && (parseFloat(section.balance) === 0)" style="width:15%;font-wieght:bold;font-family:'arial';font-size:20px"><router-link :to="`#`" class="text-big font-weight-semibold" >
                  <img style="width:48px" class="" :src="`/icons/color/${section.brand.toLowerCase()}.svg`" :onerror="`javascript:this.src='/icons/color/${section.brand.toLowerCase()}.png';`"  alt=""><br>{{section.brand}}
                  </router-link></td>
                  <td v-if="!(section.brand == 'USDT' |section.brand == 'BTC' |section.brand == 'ETH' |section.brand == 'TRX') && (parseFloat(section.balance) === 0)" style="padding:20px;font-family:'arial';font-size:14px"> <router-link :to="`#`"><a v-if="(parseFloat(section.balance) === 0)">0</a> {{section.balance}}</router-link></td>
                  <td v-if="!(section.brand == 'USDT' |section.brand == 'BTC' |section.brand == 'ETH' |section.brand == 'TRX') && (parseFloat(section.balance) === 0)" style="padding:0;font-family:'arial';font-size:14px"><router-link  :to="`/cpwallets/${section.name}/withdraw`" class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'">برداشت</router-link><router-link :to="`/wallets/${section.name}/history`"  class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'"> تاریخچه </router-link><router-link :to="`/buy/${section.brand}`"  class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'"> خرید </router-link><router-link :to="`/sell/${section.brand}`"  class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'"> فروش </router-link><router-link   :to="`/cpwallets/${section.name}/deposit`" class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'">واریز</router-link></td>

          </tr>
        </tbody>
            </table>
        </div>
      </b-card>

  </div>
</template>

<script>
import axios from 'axios'
import { GChart } from "vue-google-charts";
export default {
  name: 'pages-forums-list',
  metaInfo: {
    title: 'کیف ها'
  },
  components:{
     GChart
  },
  mounted () {
    this.getprices()
    this.checklevel()
    this.getprice()
    this.getw()
    this.getprice2()
    this.getrialprice()
    this.inits()
  },
  data: () => ({
    currencies: [],
    withamount: [],
    allamount: 0,
    allamountrial: 0,
    wallets: [],
    wallets2: [],
    walletsback:[],
    usd: 250000,
    rialprice: 0,
    prices: [],
    prices2: [],
    searchtext: '',
    temp: {},
    data: [['Currency', 'Balance'],['',1]],
      options: {
        width: window.innerWidth /1.5,
        height: 400,
        pieHole: 0.6
      }
  }),
  forumPath: [
    { text: 'کیف ها', active: true }
  ],
  methods: {
    inits (){
      if(window.innerWidth > 600){
          this.options.width = parseInt(window.innerWidth /1.5)
      }else{
        this.options.width = parseInt(window.innerWidth /1.1)
      }
      window.addEventListener('resize' , ()=>{
        if(window.innerWidth > 600){
          this.options.width = parseInt(window.innerWidth /1.5)
        }else{
          this.options.width = parseInt(window.innerWidth /1.1)
        }
      })
    },
    async getrialprice () {
      window.addEventListener('resize', ()=>{
        this.options.width = window.innerWidth /2
      })
      await axios
        .get('/price' )
        .then(response => {
          this.rialprice = response.data[0].rial
        })
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
    async fasttorial (id) {
      await axios
        .get(`/fasttorial/${id}`)
        .then(response => {
          this.$swal.fire({
            title: 'آیا از تبدیل کل دارایی به مبلغ زیر اطمینان دارید؟',
            text: `مبلغ ریالی : ${response.data.price}‍‍‍`,
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: ' تایید ',
            cancelButtonText: ' لغو'
          }).then(result => {
            if (result.isConfirmed) {
              this.fasttorialconf(id)
            }
          })
        })
    },
    async fasttorialconf (id) {
      await axios
        .post(`/fasttorial/${id}`)
        .then(response => {
          location.reload()
        })
    },
    async getprices () {
      await axios
        .get(`/oltradeinfo3`)
        .then(response => {
          this.prices = response.data
          this.getw2()
        })
    },
    async getc () {
      await axios
        .get('/currencies')
        .then(response => {
          this.currencies = response.data
          var itemm
          for (itemm of this.currencies) {
            itemm.amount = 0
          }
          for (let index = 0; index < this.wallets2.length; index++) {
            if (this.currencies[this.wallets2[index].currency - 1]) {
              this.currencies[this.wallets2[index].currency - 1].amount = this.wallets2[index].amount
              this.currencies[this.wallets2[index].currency - 1].address = this.wallets2[index].address
            }
          }
        })
    },
    async getw () {
      await axios
        .get('/wallet')
        .then(response => {
          this.wallets2 = response.data
        }).then(() => {
          this.getc()
        })
    },
    async getprice () {
      await axios
        .get('/price')
        .then(response => {
          this.temp = response.data[0]
        })
        .catch(() => {
        })
    },
    getbrand (brand) {
      return this.temp[`${brand.toLowerCase()}`]
    },
    async getw2 () {
      await axios
        .get('/cp_wallets')
        .then(response => {
          this.wallets = response.data
          this.walletsback = response.data
          this.allamount = 0
          this.allamountrial = 0
          this.data = [['Currency', 'Balance']]
          for (const [key, value] of Object.entries(this.walletsback)){
            if(value.balance  > 0 && this.prices[value.brand + 'USDT'] !== null && value.brand !== 'USDT'){
              this.data.push([key + '($)' , parseInt(Number(value.balance) * Number(this.prices[value.brand + 'USDT'].last))])
              this.allamount = this.allamount + (Number(value.balance) * Number(this.prices[value.brand + 'USDT'].last))
              this.allamountrial = parseInt(this.allamountrial + (Number(value.balance) * Number(this.prices[value.brand + 'USDT'].last) * this.rialprice))
            }if (value.brand === 'USDT'){
              this.data.push([key + '($)' , parseInt(Number(value.balance) )])
              this.allamount = this.allamount + (Number(value.balance))
              this.allamountrial = parseInt(this.allamountrial +( Number(value.balance) * this.rialprice))
            }
          }
          
          var myEle = document.getElementById("all");
          if(myEle){
            this.options.width = document.querySelector('#all').clientWidth * .8
            window.addEventListener('resize', ()=>{
            this.options.width = document.querySelector('#all').clientWidth * .8
          })
          }
          
        }).then(() => {
        })
    },
    async getprice2 () {
      await axios
        .get('/price')
        .then(response => {
          this.temp = response.data[0]
        })
        .catch(() => {
        })
    },
    getbrand2 (brand) {
      return this.temp[`${brand.toLowerCase()}`]
    },
    search2 (){
      this.wallets = {}
      for (const [key, value] of Object.entries(this.walletsback)){
        if(key.includes(this.searchtext.toUpperCase())){
        this.wallets[key] = value        
        }
      }
    }
  },
}

</script>
<style>
.cent{
  text-align: center;
}
.btnfont{
  font-size: 12px;
  padding: 9px;
  margin: 2px;
}
td{
height: 90px;
text-align: center;
}
th{
text-align: center;
}
.wallets:hover{
  background: #efefff;
}
a{
  color:#888
}
@media only screen and (max-width: 1024px) {
.nmobile{
  display: none;
}
.walbtn{
height:30%;
width: 90%;
min-height: 30px;
float: left;
}
}
@media only screen and (min-width: 1024px) {
.walbtn{
position: relative;top: 35%
}
}
@media only screen and (max-width: 1275px) {
.nmobile{
  display: none;
}
}
</style>
