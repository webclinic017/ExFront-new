<template>
  <div>
    <b-card v-if="sym && sym2  && price && price2"> 
      <h3 v-if="sym && sym2  && price && price2" style="float:right; color:#888" > قیمت نسبی ارز  ها: <a style="font:20px 'arial'">{{this.price.buy  / this.price2.buy }}</a></h3>
      </b-card>
        <b-card-header class="row no-gutters align-items-center">تبدیل</b-card-header>

           
        <div style="clear:both"></div>
    <b-card>
        <br><br>
        <h5 class="alert alert-danger" v-for="error in errors" v-bind:key="error">{{error}}</h5>
      <fieldset  class="demo-vertical-spacing-sm" >
        <div style="width:100%;text-align:center">
          <cryptoicon v-if="sym" :symbol="sym" style="text-align:center" size="32"  /><br>
        {{sym}}
        </div>

         <input @click="listshow" @input="search()" type="text" class="form-control" placeholder="search ..." v-model="searchtxt" style="border-radius: 5px 5px 0 0; border-color:lightgrey!important">
          <div class="list" style="height:150px; overflow-x:hidden ;overflow-y:scroll ; border: solid lightgrey .2px ; border-radius: 0 0 5px 5px" id="my-list-id">
            <button class=" curbtn" onMouseOver="this.style.background='rgba(150, 150, 150, 0.4)'" onMouseOut="this.style.background='rgba(0,0,0,0)'"   type="button"  style="height:50px; width: 100% ; background: none ;border-style: none; border-bottom: solid .2px lightgrey ;border-shadow:none margin:0 ; font: 15px 'arial';padding-left:10%"  @click="buttonchange('USDT')"  selected >USDT&emsp;<template style="margin:9px"><img style="width:32px;height:32px" :src="`/icons/color/usdt.svg`" :onerror="`javascript:this.src='/icons/color/usdt.png';`"  alt=""></template>   </button>
            <button class=" curbtn" onMouseOver="this.style.background='rgba(150, 150, 150, 0.4)'" onMouseOut="this.style.background='rgba(0,0,0,0)'" v-for="(value , key) in leverage" v-bind:key="'n' + key" :id="key"  type="button"  style="height:50px; width: 100% ; background: none ;border-style: none; border-bottom: solid .2px lightgrey ;border-shadow:none margin:0 ; font: 15px 'arial';padding-left:10%"  @click="buttonchange(key.replace('USDT', ''))"  selected >{{key.replace('USDT', '')}}&emsp;<template style="margin:9px"><img style="width:32px;height:32px" :src="`/icons/color/${key.replace('USDT', '').toLowerCase()}.svg`" :onerror="`javascript:this.src='/icons/color/${key.replace('USDT', '').toLowerCase()}.png';`"  alt=""></template>   </button>
          </div><br><br>

          <br><h4 style="text-align:center; width:100% ; clear:both">به</h4><br>
          <div style="width:100%;text-align:center">
            <cryptoicon v-if="sym2" :symbol="sym2" style="text-align:center" size="32"  /><br>
            {{sym2}}
          </div>
          

          <input @click="listshow2" @input="search2()" type="text" class="form-control" placeholder="search ..." v-model="searchtxt2" style="border-radius: 5px 5px 0 0; border-color:lightgrey!important">
          <div class="listtwo" style="height:150px; overflow-x:hidden ;overflow-y:scroll ; border: solid lightgrey .2px ; border-radius: 0 0 5px 5px" id="my-list-id">
            <button class=" curbtn" onMouseOver="this.style.background='rgba(150, 150, 150, 0.4)'" onMouseOut="this.style.background='rgba(0,0,0,0)'"   type="button"  style="height:50px; width: 100% ; background: rgba(0,0,0,0) ;border-style: none; border-bottom: solid .2px lightgrey ;border-shadow:none margin:0 ; font: 15px 'arial';padding-left:10%"  @click="buttonchange2('USDT')"  selected >USDT&emsp;<template style="margin:9px"><img style="width:32px;height:32px" :src="`/icons/color/usdt.svg`" :onerror="`javascript:this.src='/icons/color/usdt.png';`"  alt=""></template>   </button>
            <button class=" curbtn" onMouseOver="this.style.background='rgba(150, 150, 150, 0.4)'" onMouseOut="this.style.background='rgba(0,0,0,0)'" v-for="(value , key) in leverage2" v-bind:key="'n' + key + 'two'" :id="key + 'two'"  type="button"  style="height:50px; width: 100% ; background: rgba(0,0,0,0) ;border-style: none; border-bottom: solid .2px lightgrey ;border-shadow:none margin:0 ; font: 15px 'arial';padding-left:10%"  @click="buttonchange2(key.replace('USDT', ''))"  selected >{{key.replace('USDT', '')}}&emsp;<template style="margin:9px"><img style="width:32px;height:32px" :src="`/icons/color/${key.replace('USDT', '').toLowerCase()}.svg`" :onerror="`javascript:this.src='/icons/color/${key.replace('USDT', '').toLowerCase()}.png';`"  alt=""></template>   </button>
            <h2 v-if="!leverage" style="font-family:'arial'; text-align:center">موردی یافت نشد</h2>
          </div><br><br>

          <h1 v-if="sym && sym2" style="text-align:center; font-family:'arial'">{{sym}} - {{sym2}}</h1>




        <b-form-group label="">
       
           <b-card>
           <h5 style="float:right; color:#888" v-if="price">موجودی : <a @click="balanceset()" class="btn btn-dark" style="font:12px 'arial'; padding:5px 20px">{{rial}}</a>  {{sym}} </h5><br>
            <div class="input-group mb-3" style="direction:ltr ; margin:0">
              <div class="input-group-prepend">
                <span class="input-group-text" id="basic-addon1">|{{sym}}|</span>
              </div>
              <b-input step="any" required id="amount"  type="number" v-model="amount" />
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
                <b-form-slider step="0.000001" :ticks_tooltip="true" v-if="rial | rial === 0" :min="0.0000000" :max="rial" v-model="amount"></b-form-slider><br>
              </b-card>
              
            <br><h4 style="text-align:center; width:100% ; clear:both">معادل</h4><br>
            
            <b-card>
            <div class="input-group mb-3" style="direction:ltr ; margin:0">
              <div class="input-group-prepend">
                <span class="input-group-text" id="basic-addon1">|{{sym2}}|</span>
              </div>
              <b-input step="any" required id="amount"  type="number" v-model="getting" />
            </div>
              </b-card>

        </b-form-group>
        <h5 style="float:right; color:#888" v-if="price">دریافتی : <a  class="btn btn-dark" style="font:12px 'arial'; padding:5px 20px">{{getting}}</a></h5><br><br>
        <b-btn @click="submit()" id="submit" variant="dark">درخواست تبدیل</b-btn>
      </fieldset>
      </b-card><br><br>
  </div>
</template>

<script>
import axios from 'axios'
import bFormSlider from 'vue-bootstrap-slider/es/form-slider';
import 'bootstrap-slider/dist/css/bootstrap-slider.css'
import './tv'
export default {
  name: 'pages-forums-list',
  metaInfo: {
    title: 'کیف ها'
  },
  updated (){
    this.getrial()
  },
  mounted () {
    document.title = ' AMIZAS Exchange | شارژ حساب '
    this.checklevel()
    this.check()
    this.getc()
    this.getlev()
    this.getuserfee()
  },
  data: () => ({
    options: [],
    amount: '',
    errors: [],
    leverage:[],
    leverageback: [],
    leverage2:[],
    leverageback2: [],
    searchtxt: '',
    searchtxt2: '',
    sym:'',
    sym2:'',
    userfee: 0 ,
    price: [],
    rial: 1,
    price2: [],
    getting: 0,
    tvs: false,
  }),
  methods: {
    async getrial () {
      await axios
        .post('/cp_mg_main', {sym : this.sym} )
        .then(response => {
          this.rial = parseFloat(response.data)
          if ( parseFloat(response.data) < 0.0000001){
            this.rial = 0.0
          }
        })
    },
    checksym(){
      if(this.$route.params.symbol){
        setTimeout(() => {
          document.getElementById(this.$route.params.symbol).click()
        }, 1000)
      }
    },
    gettings() {
      if(this.sym && this.sym2){
        if((this.sym in this.leverage))
        {
          if(this.price){
        var prices = parseFloat(this.price.buy  / this.price2.buy ) * this.userfee * 1.015
        this.getting = parseFloat(this.amount * prices)
          }
        }
      }
    },
    payings() {
      if(this.sym && this.sym2){
        if((this.sym in this.leverage))
        {
          if(this.price){
            
        var price = parseFloat(this.price.buy  / this.price2.buy ) * this.userfee * 1.015
        this.amount = this.getting / price
          }
        }
      }
    },
    tv (a) {
      this.tvs = true
      if((this.sym in this.leverage))
      {
       this.getprice(true)
       this.getprice2()
      }
    },
    async getlev () {
      await axios
        .get('/cp_wallets')
        .then(response => {
          this.leverage = response.data
          this.leverageback = response.data
          this.leverage2 = response.data
          this.leverageback2 = response.data
          this.checksym()
          this.search()
          this.search2()
        })
    },
    async getprice (act) {
      await axios
        .post('/cp_ticker' , {sym: this.sym})
        .then(response => {
          this.price = response.data
          if(act) {
            setTimeout(() => {
              this.tv(false)
              if(this.sym && this.sym2){
                this.gettings()
              }
            }, 3000);
          }
        })
    },
    async getprice2 () {
      await axios
        .post('/cp_ticker' , {sym: this.sym2})
        .then(response => {
          this.price2 = response.data
        })
    },
    async getuserfee () {
      await axios
        .get('/levelfee')
        .then(response => {
          this.userfee =  1 - (response.data[0].exchange / 100)
        })
    },
    buttonchange(key) {
      this.searchtxt = ''
      document.querySelector('.list').hidden=true
      this.sym = key
      if(this.sym2){
        if(!this.tvs){
          this.tv(true)
        }
      }
      document.querySelectorAll('.curbtn').forEach(item => {
        item.style.background = '#ffffff'
      })
      this.search2()
      this.getrial()
    },
    buttonchange2(key) {
      this.searchtxt2 = ''
      document.querySelector('.listtwo').hidden=true
      this.sym2 = key
      if(this.sym){
        if(!this.tvs){
          this.tv(true)
        }
      }
      document.querySelectorAll('.curbtntwo').forEach(item => {
        item.style.background = '#ffffff'
      })
      this.search()
    },
    search(){
      if(this.searchtxt){
        document.querySelector('.list').hidden=false
      }
      this.leverage = {}
      for (const [key, value] of Object.entries(this.leverageback)){
        if(key !== this.sym2){
          if(key.includes(this.searchtxt.toUpperCase())){
          this.leverage[key] = value
          }
        }
      }
    },
    search2(){
      if(this.searchtxt2){
        document.querySelector('.listtwo').hidden=false
      }
      this.leverage2 = {}
      for (const [key, value] of Object.entries(this.leverageback2)){
        if(key !== this.sym){
          if(key.includes(this.searchtxt2.toUpperCase())){
          this.leverage2[key] = value
          }
        }
      }
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
    async submit () {
      this.$loading(true)
        await axios
        .post('/exchange', {camount :this.amount, camount2 :this.getting, currency : this.sym, currency2 : this.sym2})
        .then(response => {
          this.$loading(false)
          if(response.data.error){
            document.getElementById('submit').disabled = false
            this.$swal(`<div class="swal2-icon swal2-error swal2-icon-show" style="display: flex;"><span class="swal2-x-mark"><span class="swal2-x-mark-line-left"></span><span class="swal2-x-mark-line-right"></span></span></div><h5>${response.data.error}</h5>`)
          }else{
            document.getElementById('submit').disabled = false
            this.$swal('<div class="swal2-header"><ul class="swal2-progress-steps" style="display: none;"></ul><div class="swal2-icon swal2-success swal2-icon-show" style="display: flex;"><div class="swal2-success-circular-line-left" style="background-color: rgb(255, 255, 255);"></div><span class="swal2-success-line-tip"></span> <span class="swal2-success-line-long"></span><div class="swal2-success-ring"></div> <div class="swal2-success-fix" style="background-color: rgb(255, 255, 255);"></div><div class="swal2-success-circular-line-right" style="background-color: rgb(255, 255, 255);"></div></div><img class="swal2-image" style="display: none;"><button type="button" class="swal2-close" aria-label="Close this dialog" style="display: none;">×</button></div>' + '<h5>درخواست فروش شما با موفقیت ثبت شد</h5>')
          }
        })
        .catch(error => {
          this.$loading(false)
        })
    },
    listshow(){
      document.querySelector('.list').hidden = false
    },
    listshow2(){
      document.querySelector('.listtwo').hidden = false
    },
    balanceset () {
      this.amount = parseFloat(this.rial)
    }
      },
    watch: {
    amount: {
        handler: function() {
            this.gettings();
        },
        deep: true
      },
    sym: {
        handler: function() {
            this.gettings();
        },
        deep: true
      },
    sym2: {
        handler: function() {
          this.getprice(false)
          this.getprice2()
          this.gettings();
        },
        deep: true
      },
    getting: {
        handler: function() {
          this.getprice(false)
          this.getprice2()
          this.payings(); 
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
