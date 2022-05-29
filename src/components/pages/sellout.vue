<template>
  <div>
        <b-card v-if="price"> 
          <h3 v-if="this.sym !== 'USDT' && price && rialprice" style="float:right; color:#888" >قیمت ریالی : <a style="font:20px 'arial'">{{price.buy *rialprice[0].rial * 1.002}}</a></h3>
      <h3 v-if="this.sym !== 'USDT' && price" style="float:left; color:#888" >قیمت دلاری : <a style="font:20px 'arial'">{{(price.buy )}}</a></h3>

      <h3 v-if="this.sym === 'USDT' && price && rialprice" style="float:right; color:#888" >قیمت ریالی : <a style="font:20px 'arial'">{{price.buy *rialprice[0].rial * 0.996}}</a></h3>
      <h3 v-if="this.sym === 'USDT' && price" style="float:left; color:#888" >قیمت دلاری : <a style="font:20px 'arial'">{{(price.buy )}}</a></h3>
        </b-card>

            <b-card-header class="row no-gutters align-items-center">فروش</b-card-header>
        <div style="clear:both"></div>
    <b-card>
        <br><br>
        <h5 class="alert alert-danger" v-for="error in errors" v-bind:key="error">{{error}}</h5>
      <fieldset  class="demo-vertical-spacing-sm" >
        <form @submit.prevent="firstsubmit()">
        
        

         <input @input="search()" type="text" class="form-control half" placeholder="search ..." v-model="searchtxt" style="border-radius: 5px 5px 0 0; border-color:lightgrey!important">
          <div class="list half" style="height:150px; overflow-x:hidden ;overflow-y:scroll ; border: solid lightgrey .2px ; border-radius: 0 0 5px 5px" id="my-list-id">
            <button class=" curbtn " onMouseOver="this.style.background='rgba(150, 150, 150, 0.4)'" onMouseOut="this.style.background='rgba(0,0,0,0)'"   type="button"  style="height:50px; width: 100% ; background: none ;border-style: none; border-bottom: solid .2px lightgrey ;border-shadow:none margin:0 ; font: 15px 'arial';padding-left:10%"  @click="buttonchange('USDT')"  selected >USDT&emsp;<template style="margin:9px"><img style="width:32px;height:32px" :src="`/icons/color/usdt.svg`" :onerror="`javascript:this.src='/icons/color/usdt.png';`"  alt=""></template>   </button>
            <button class=" curbtn half" onMouseOver="this.style.background='rgba(150, 150, 150, 0.4)'" onMouseOut="this.style.background='rgba(0,0,0,0)'" v-for="(value , key) in leverage" v-bind:key="'n' + key" :id="key"  type="button"  style="height:50px; width: 100% ; background: none ;border-style: none; border-bottom: solid .2px lightgrey ;border-shadow:none margin:0 ; font: 15px 'arial';padding-left:10%"  @click="buttonchange(key.replace('USDT', ''))"  selected >{{key.replace('USDT', '')}}&emsp;<template style="margin:9px"><img style="width:32px;height:32px" :src="`/icons/color/${key.replace('USDT', '').toLowerCase()}.svg`" :onerror="`javascript:this.src='/icons/color/${key.replace('USDT', '').toLowerCase()}.png';`"  alt=""></template>   </button>
          </div><br><br>



          <h1 style="text-align:center; font-family:'arial'">{{sym}}</h1>




        <b-form-group label="" style="text-align:center">
        <img v-if="address" hidden id="qr" :src=" `https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=${address}`"><br>
          <label hidden for="address" id="addresslable">آدرس</label>
          <b-input hidden v-model="address" id="address" name="address" readonly></b-input>
          <b-card>
            <div class="input-group mb-3" style="direction:ltr ; margin:0">
              <div class="input-group-prepend">
                <span class="input-group-text" id="basic-addon1">|{{sym}}|</span>
              </div>
              <b-input @input="gettings()" @change="gettings()" step="any" required id="amount"  type="number" v-model="amount" />
            </div>
            <a style="text-align:center">معادل</a>
            <div class="input-group mb-3" style="direction:ltr ; margin:0">
              <div class="input-group-prepend">
                <span class="input-group-text" id="basic-addon1">|ریالی|</span>
              </div>
              <b-input @input="payings()" @change="payings()" required id="amount2"  type="number" v-model="getting" />
            </div>
          </b-card>
          <label hidden for="hash" id="hashlable">کد هش</label>
          <b-input hidden id="hash" v-model="hash" placeholder=" کد پیگیری - هش " />
        </b-form-group>
        <h5 style="float:right; color:#888" v-if="price && rialprice">دریافتی : <a  class="btn btn-dark" style="font:12px 'arial'; padding:5px 20px">{{getting}}</a></h5><br><br>
        <b-btn type="button" @click="firstsubmit()" value="درخواست فروش" id="firstsubmit" variant="dark"> مرحله بعد</b-btn>
        <b-btn hidden id="submit"  @click="submit()" variant="dark"> ثبت درخواست </b-btn>
      </form>
      </fieldset>
      </b-card><br><br>
    <b-card>
      <div style="margin:auto" id="tradingview_1be21"></div><br>

    </b-card><br>
    
        
  </div>
</template>

<script>
import axios from 'axios'
import Vue from 'vue'
import './tv'
import VueQr from 'vue-qr/src/packages/vue-qr.vue'
new Vue({
    components: {VueQr}
})
export default {
  name: 'pages-forums-list',
  metaInfo: {
    title: 'کیف ها'
  },
  components:{
    VueQr
  },
  updated (){
    this.getrial()
    this.getaddress()
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
    userfee: 0 ,
    amount: '',
    address: '',
    errors: [],
    leverage:[],
    leverageback: [],
    searchtxt: '',
    test:'ll',
    sym:'',
    hash: '',
    rialprice: 0,
    price: false,
    rial: 0,
    getting: 0
  }),
  methods: {
    gettings() {
      if((this.sym in this.leverage))
      {
        if(this.price){
          if(this.sym === 'USDT'){
            var prices = parseFloat(this.price.buy  * this.rialprice[0].rial) * this.userfee * 0.996
            this.getting = BigInt(parseInt(this.amount * prices))
          }else{
            var prices = parseFloat(this.price.buy  * this.rialprice[0].rial) * this.userfee * 1.002
            this.getting = BigInt(parseInt(this.amount * prices))
          }
      
        }
      }
    },
    payings() {
      if((this.sym in this.leverage))
      {
        if(this.price){
          if (this.sym === 'USDT'){
            var price = parseFloat(this.price.buy  * this.rialprice[0].rial) * this.userfee * 0.996
            this.amount = this.getting / price
          }else{
            var price = parseFloat(this.price.buy  * this.rialprice[0].rial) * this.userfee * 1.002
            this.amount = this.getting / price
          }
      
        }
      }
    },
    tv (a) {
      this.price = []
      if((this.sym in this.leverage))
      {
        this.getprice()
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
      this.getaddress()
      }
    },
    async getlev () {
      await axios
        .get('/cp_wallets')
        .then(response => {
          this.leverage = response.data
          this.leverageback = response.data
          this.checksym()
          this.search()
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
    },
    async getprice () {
      this.price = 0
      await axios
        .post('/cp_ticker' , {sym: this.sym})
        .then(response => {
          this.price = response.data
          setTimeout(() => {
            this.tv(false)
          }, 5000);
        })
    },
    async getaddress () {
     if(this.sym){
        await axios
        .post('/cp_address' , {sym: this.sym})
        .then(response => {
          this.address = response.data.coin_address
        })
     }
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
        .post('/cp_mg_main', {sym : this.sym} )
        .then(response => {
          this.rial = parseInt(response.data)
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
    async getuserfee () {
      await axios
        .get('/levelfee')
        .then(response => {
          this.userfee =  1 - (response.data[0].sell / 100)
        })
    },
    async submit () {
      this.$loading(true)
        var realprice = this.price.buy  * this.rialprice[0].rial
        var pricess = parseFloat(this.price.buy  * this.rialprice[0].rial) * this.userfee * 1.015
        var ramount = parseFloat(this.amount * pricess)
        var rramount = parseFloat(this.amount * realprice)
        await axios
        .post('/sellout', {ramount : ramount,camount :this.amount, currency : this.sym, hash:this.hash , rramount: rramount})
        .then(response => {
          this.$loading(false)
          if(response.data.error){
            document.getElementById('submit').disabled = false
            this.$swal(`<div class="swal2-icon swal2-error swal2-icon-show" style="display: flex;"><span class="swal2-x-mark"><span class="swal2-x-mark-line-left"></span><span class="swal2-x-mark-line-right"></span></span></div><h5>${response.data.error}</h5>`)
          }else{
            document.getElementById('submit').disabled = false
            this.$swal('<div class="swal2-header"><ul class="swal2-progress-steps" style="display: none;"></ul><div class="swal2-icon swal2-success swal2-icon-show" style="display: flex;"><div class="swal2-success-circular-line-left" style="background-color: rgb(255, 255, 255);"></div><span class="swal2-success-line-tip"></span> <span class="swal2-success-line-long"></span><div class="swal2-success-ring"></div> <div class="swal2-success-fix" style="background-color: rgb(255, 255, 255);"></div><div class="swal2-success-circular-line-right" style="background-color: rgb(255, 255, 255);"></div></div><img class="swal2-image" style="display: none;"><button type="button" class="swal2-close" aria-label="Close this dialog" style="display: none;">×</button></div>' + '<h5>درخواست فروش شما با موفقیت ثبت شد</h5>')
          }
          this.getrial()
        })
        .catch(error => {
          this.$loading(false)
        })
    },
    firstsubmit (){
      document.getElementById('amount').disabled = true
      document.getElementById('amount2').disabled = true
      document.getElementById('firstsubmit').hidden = true
      document.getElementById('submit').hidden = false
      document.getElementById('qr').hidden = false
      document.getElementById('hash').hidden = false
      document.getElementById('hash').required = true
      document.getElementById('hashlable').hidden = false
      document.getElementById('address').hidden = false
      document.getElementById('addresslable').hidden = false
      }
    },
    balanceset () {
      this.amount = parseFloat(this.rial)
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
@media (min-width: 768px) {
  .half{
    width:50%;
    margin:auto
  }
  }
</style>
