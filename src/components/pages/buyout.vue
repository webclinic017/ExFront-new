<template>
  <div>
        <b-card v-if="price">              
      <h3 style="float:right; color:#888" v-if="price && rialprice && this.sym !== 'USDT'">قیمت : <a style="font:20px 'arial'">{{price.buy *rialprice[0].rial * 1.007}}</a></h3>
      <h3 style="float:left; color:#888" v-if="price && this.sym !== 'USDT'">قیمت دلاری : <a style="font:20px 'arial'">{{(price.buy )}}</a></h3>

      <h3 style="float:right; color:#888" v-if="price && rialprice && this.sym === 'USDT'">قیمت : <a style="font:20px 'arial'">{{price.buy *rialprice[0].rial }}</a></h3>
      <h3 style="float:left; color:#888" v-if="price && this.sym === 'USDT'">قیمت دلاری : <a style="font:20px 'arial'">{{(price.buy )}}</a></h3></b-card>
    <b-card>
              <b-card-header class="row no-gutters align-items-center">خرید</b-card-header>

        <br><br>
        <h5 class="alert alert-danger" v-for="error in errors" v-bind:key="error">{{error}}</h5>
      <fieldset  class="demo-vertical-spacing-sm">
        <form @submit.prevent="submit()">
        <p style="margin:0">نوع ارز:</p>
        
        
        <input @input="search()" type="text" class="form-control" placeholder="search ..." v-model="searchtxt" style="border-radius: 5px 5px 0 0; border-color:lightgrey!important">
          <div class="list" style="height:150px; overflow-x:hidden ;overflow-y:scroll ; border: solid lightgrey .2px ; border-radius: 0 0 5px 5px" id="my-list-id">
            <button class=" curbtn" onMouseOver="this.style.background='rgba(150, 150, 150, 0.4)'" onMouseOut="this.style.background='rgba(0,0,0,0)'"   type="button"  style="height:50px; width: 100% ; background: none ;border-style: none; border-bottom: solid .2px lightgrey ;border-shadow:none margin:0 ; font: 15px 'arial';padding-left:10%"  @click="buttonchange('USDT')"  selected >USDT&emsp;<template style="margin:9px"><img style="width:32px;height:32px" :src="`/icons/color/usdt.svg`" :onerror="`javascript:this.src='/icons/color/usdt.png';`"  alt=""></template>   </button>
            <button class=" curbtn" onMouseOver="this.style.background='rgba(150, 150, 150, 0.4)'" onMouseOut="this.style.background='rgba(0,0,0,0)'" v-for="(value , key) in leverage" v-bind:key="'n' + key" :id="key"  type="button"  style="height:50px; width: 100% ; background: none ;border-style: none; border-bottom: solid .2px lightgrey ;border-shadow:none margin:0 ; font: 15px 'arial';padding-left:10%"  @click="buttonchange(key.replace('USDT', ''))"  selected >{{key.replace('USDT', '')}}&emsp;<template style="margin:9px"><img style="width:32px;height:32px" :src="`/icons/color/${key.replace('USDT', '').toLowerCase()}.svg`" :onerror="`javascript:this.src='/icons/color/${key.replace('USDT', '').toLowerCase()}.png';`"  alt=""></template>   </button>
          </div><br><br>



          <h1 style="text-align:center; font-family:'arial'">{{sym}}</h1>



          <p style="margin:0">شبکه ارز:</p>
          <select v-if="wallets" class="form-control" v-model="chain" @change="getfee()" style="font-family:'arial'">
          <option class="op" v-for="(item,name) in wallets.address" v-bind:key="name" :value="name" style="font-family:'arial'">{{name}}</option>
        </select><br>

        <b-form-group label="">
          <b-card>
        <h5 style="float:right; color:#888" v-if="price && rialprice">موجودی : <a @click="balanceset()" class="btn btn-dark" style="font:12px 'arial'; padding:5px 20px ">{{rial}}</a> ریال </h5>
            <div class="input-group mb-3" style="direction:ltr ; margin:0">
              <div class="input-group-prepend">
                <span class="input-group-text" id="basic-addon1">|ریالی|</span>
              </div>
              <b-input autocomplete="off" step="any" min="1000000" @click="setin(1)" required id="amount"  type="number" v-model="amount" />
            </div>
                        <table style="width:98%">
                <tr>
                  <td style="text-align:center; color:#888 ; font: 12px 'arial'">0%</td>
                  <td style="text-align:center; color:#888 ; font: 12px 'arial'">25%</td>
                  <td style="text-align:center; color:#888 ; font: 12px 'arial'">50%</td>
                  <td style="text-align:center; color:#888 ; font: 12px 'arial'">75%</td>
                  <td style="text-align:center; color:#888 ; font: 12px 'arial'">100%</td>
                </tr>
              </table>
                <b-form-slider :ticks_tooltip="true" v-if="rial | rial === 0" :min="0" :max="rial" v-model="amount"></b-form-slider><br>
          </b-card>
            <h4 style="text-align:center">معادل</h4>
            <b-card>
            <div class="input-group mb-3" style="direction:ltr ; margin:0">
              <div class="input-group-prepend">
                <span class="input-group-text" id="basic-addon1">|{{sym}}|</span>
              </div>
              <b-input @click="setin(2)" autocomplete="off" required id="amount2"  type="text" v-model="getting" />
            </div>
        </b-card>
          <a style="font-size:12px">حداقل میزان خرید ۱۰۰۰,۰۰۰ ریال میباشد</a>
          <p style="margin:0"> آدرس:</p>
          <b-input autocomplete="off" type="text" v-model="address" placeholder=" آدرس " />
        </b-form-group>
        <h5 style="float:right; color:#888" v-if="price && rialprice">هزینه جا به جایی : <a class="btn btn-dark" style="font:12px 'arial'; padding:5px 20px "> {{ parseInt(fee * price.buy  * rialprice[0].rial * 1.07)}} ریال</a></h5><br><br>
        <h5 style="float:right; color:#888" v-if="price && rialprice">دریافتی : <a v-if="getting > 0" class="btn btn-dark" style="font:12px 'arial'; padding:5px 20px ">{{getting}}</a><a v-else class="btn btn-dark" style="font:12px 'arial'; padding:5px 20px ">0</a></h5><br><br>
        <b-btn type="submit" id="submit" variant="dark">درخواست خرید</b-btn>
        </form>
      </fieldset>
      </b-card>
      <br>
    <b-card>
      <div style="margin:auto" id="tradingview_1be21"></div><br>
    </b-card><br>
    
        
  </div>
</template>

<script>
import axios from 'axios'
import './tv'
import { keys } from 'd3'
import bFormSlider from 'vue-bootstrap-slider/es/form-slider';
import 'bootstrap-slider/dist/css/bootstrap-slider.css'
export default {
  name: 'pages-forums-list',
  metaInfo: {
    title: 'کیف ها'
  },
  mounted () {
    document.title = ' AMIZAS Exchange | شارژ حساب '
    this.checklevel()
    this.check()
    this.getc()
    this.getlev()
    this.getrialprice()
    this.getrial()
    this.getuserfee()
  },
  data: () => ({
    options: [],
    fee: 0,
    userfee: 0 ,
    amount: '',
    errors: [],
    leverage:[],
    address: '',
    wallets:[],
    searchtxt: '',
    leverageback:[],
    sym:'',
    rialprice: 0,
    price: 0,
    rial: 0,
    getting: 0,
    in: '',
  }),
  methods: {
    setin(ii){
      this.in = ii
    },
    gettings() {
      if((this.sym in this.leverage))
      {
      if(this.price){
        var pricess = parseFloat(this.price.buy  * this.rialprice[0].rial) * this.userfee * 1.07
        if(this.amount/pricess > parseFloat(this.fee)){
          if (this.amount < 1000000){
            this.getting = 0
          }else{
            if(this.sym === 'USDT'){
              this.getting = ((this.amount / parseFloat(this.price.buy  * this.rialprice[0].rial) * this.userfee) ) - parseFloat(this.fee)
            }else{
              this.getting = ((this.amount / pricess) - parseFloat(this.fee))
            }
            
          }
        }
      }
      }
    },
    payings() {
      if((this.sym in this.leverage))
      {
        if(this.price){
          if(this.sym === 'USDT'){
            var price = parseFloat(this.price.buy  * this.rialprice[0].rial) * this.userfee
            this.amount = ((parseFloat(this.getting) + parseFloat(this.fee)) * price) 
          }else{
            var price = parseFloat(this.price.buy  * this.rialprice[0].rial) * this.userfee * 1.07
            this.amount = ((parseFloat(this.getting) + parseFloat(this.fee)) * price)
          }
      
        }
      }
    },
    async getw () {
      const id = this.sym
      await axios
        .post(`/cp_wallet/${id}`)
        .then(response => {
          this.wallets = response.data
        }).then(() => {
        })
    },
    tv (a) {
      if((this.sym in this.leverage))
      {
      this.getprice()
      this.getw()
      if(a) { 
        if(this.sym == 'USDT'){
        new TradingView.widget(
        {
        "width": screen.width * .7,
        "height": 390,
        "symbol": `${this.sym}USD`,
        "timezone": "Etc/UTC",
        "theme": "light",
        "style": "1",
        "locale": "en",
        "hide_side_toolbar": false,
        "enable_publishing": false,
        "allow_symbol_change": true,
        "container_id": "tradingview_1be21"
      })
      }else{
        new TradingView.widget(
        {
        "width": screen.width * .7,
        "height": 390,
        "symbol": `${this.sym}USDT`,
        "timezone": "Etc/UTC",
        "theme": "light",
        "hide_side_toolbar": false,
        "style": "1",
        "locale": "en",
        "enable_publishing": false,
        "allow_symbol_change": true,
        "container_id": "tradingview_1be21"
      }
      )
      }
      }
    }
    },
    async getlev () {
      await axios
        .get('/cp_wallets')
        .then(response => {
          this.leverage = response.data
          this.leverageback = response.data
          this.search()
        })
    },
    async getprice () {
      await axios
        .post('/cp_ticker' , {sym: this.sym})
        .then(response => {
          this.price = response.data
          console.log(response.data)
          setTimeout(() => {
            this.tv(false)
          }, 5000);
        })
    },
    async getrialprice () {
      await axios
        .get('/price' )
        .then(response => {
          this.rialprice = response.data
        })
    },
    async getrial () {
      await axios
        .get('/wallet/1' )
        .then(response => {
          this.rial = parseInt(response.data[0].amount)
        })
    },
    async checklevel () {
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
    check () {
      if (!this.$store.state.isAuthenticated) {
        const toPath = this.$route.query.to || '/login'
        this.$router.push(toPath)
      }
    },
    async getc () {
      var itemm
      await axios
        .get('/bankcards')
        .then(response => {
          for (itemm of response.data) {
            var no = String(itemm.number)
            var result = no.slice(0, 4) + '-' + no.slice(4, 8) + '-' + no.slice(8, 12) + '-' + no.slice(12, 16)
            this.options.push(result)
          }
        })
    },
    async getfee () {
      if(!this.chain){
      this.chain = document.querySelector('.op').value
      }
      const id = this.chain
      await axios
        .get(`/cp_currencies/${id}`)
        .then(response => {
          this.fee = response.data[0].withdraw_tx_fee
        }).then(() => {
        })
    },
    async submit () {
      this.$loading(true)
      this.errors = []
      if (!(this.sym in this.leverage)){
        this.$swal(`<div class="swal2-icon swal2-error swal2-icon-show" style="display: flex;"><span class="swal2-x-mark"><span class="swal2-x-mark-line-left"></span><span class="swal2-x-mark-line-right"></span></span></div><h5>لطفا ارزی را از لیست انتخاب کنید</h5>`)
        return false
      }
      
      var realprice = parseFloat(this.price.buy  * this.rialprice[0].rial)
      var camount = this.getting
      var rramount = parseFloat(camount * realprice)
      await axios
        .post('/buyout', {ramount : parseInt(this.amount),camount :camount, currency : this.chain, address: this.address, rramount : rramount})
        .then(response => {
          this.$loading(false)
          if(response.data.error){
            document.getElementById('submit').disabled = false
            this.$swal(`<div class="swal2-icon swal2-error swal2-icon-show" style="display: flex;"><span class="swal2-x-mark"><span class="swal2-x-mark-line-left"></span><span class="swal2-x-mark-line-right"></span></span></div><h5>${response.data.error}</h5>`)
          }else{
            document.getElementById('submit').disabled = false
            this.$swal('<div class="swal2-header"><ul class="swal2-progress-steps" style="display: none;"></ul><div class="swal2-icon swal2-success swal2-icon-show" style="display: flex;"><div class="swal2-success-circular-line-left" style="background-color: rgb(255, 255, 255);"></div><span class="swal2-success-line-tip"></span> <span class="swal2-success-line-long"></span><div class="swal2-success-ring"></div> <div class="swal2-success-fix" style="background-color: rgb(255, 255, 255);"></div><div class="swal2-success-circular-line-right" style="background-color: rgb(255, 255, 255);"></div></div><img class="swal2-image" style="display: none;"><button type="button" class="swal2-close" aria-label="Close this dialog" style="display: none;">×</button></div>' + '<h5>درخواست خرید شما با موفقیت ثبت شد</h5>')
          }
          this.getrial()
        })
        .catch(error => {
          this.$loading(false)
        })
    },
    balanceset () {
      this.amount = parseFloat(this.rial)
    },
    async getuserfee () {
      await axios
        .get('/levelfee')
        .then(response => {
          this.userfee = (response.data[0].buy / 100) + 1
        })
    },
      buttonchange(key) {
      document.querySelector('.list').hidden=true
      this.sym = key
      this.tv(true)
      document.querySelectorAll('.curbtn').forEach(item => {
        item.style.background = '#ffffff'
      })
    },
    search(){
      document.querySelector('.list').hidden=false
      this.leverage = {}
      for (const [key, value] of Object.entries(this.leverageback)){
        if(key.includes(this.searchtxt.toUpperCase())){
        this.leverage[key] = value
        }
      }
    }
  }, 
  watch: {
    amount: {
        handler: function() {
          if(this.in !== 2){
            this.gettings();
          }
        },
        deep: true
      },
    getting: {
        handler: function() {
          if(this.in !== 1){
            this.payings(); 
          }
        },
        deep: true
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
.error{
    color:red
}
</style>
