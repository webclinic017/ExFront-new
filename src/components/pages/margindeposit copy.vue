<template>
  <div>

    <h4 class="d-flex flex-wrap justify-content-between align-items-center pt-3 mb-4">
    </h4>
    <h4>انتقال تتر به حساب مرجین</h4>
        <b-card  class="mb-4 arscard">
            <h5 class="alert alert-danger" v-for="error in errors" v-bind:key="error">{{error}}</h5>
      <fieldset class="demo-vertical-spacing-sm">
        <b-form-group>
          <label style="width:20%" > حساب تتر</label>
          <b-select style="float:left;width:80%;font-family:'arial'" plain v-model="usdtaccount">
            <option v-for="(item, idx) of usdt" v-bind:key="idx" style="padding:10px;text-align:left;font-size:20px;height:30px" :value="item[1]">
              {{item.get_currency}} - ({{item.amount}}USDT)
            </option>
          </b-select>
          <div style="clear:both"></div>
        </b-form-group>
        <b-form-group label="">
          <b-input style="width:80%;float:left;font-family:'arial'" step="any" type="number" v-model="amount" placeholder="" /><label style="width:20%">مقدار</label>
        </b-form-group>
        <div style="clear:both"></div>
        <div style="clear:both"></div><br>
        <b-btn @click="submit()" style="float:left" variant="dark">انتقال به حساب مرجین</b-btn>
      </fieldset>
    </b-card><br><br>


    <h4>انتقال بین حساب اصلی و حساب های معاملاتی مرجین</h4>
    <b-card  class="mb-4 arscard">


      <button style="width:40%;margin:5%" id="negative" @click="tabact('negative')" class="btn btn-dark act tabss">به حساب معاملاتی</button>
      <button style="width:40%;margin:5%" id="positive" @click="tabact('positive')" class="btn btn-dark tabss">از حساب معاملاتی</button><br><br>



    <fieldset class="demo-vertical-spacing-sm tabsss negative">
        <b-form-group>
          <p style="margin-right:20%">موجودی : <button style="padding:2px 30px;" class="btn btn-light">{{balance}}</button></p>
          <label style="width:20%" >از</label>
          <b-input style="width:80%;float:left;font-family:'arial'" readonly value="حساب اصلی"></b-input>
          <div style="clear:both"></div>
        </b-form-group>
        <b-form-group label="">
          <b-input style="width:80%;float:left;font-family:'arial'" step="any" type="number" v-model="amount1" placeholder="" /><label style="width:20%">مقدار</label>
        </b-form-group>
        <div style="clear:both"></div>
        <b-form-group>
          <label style="width:20%" >به</label>
          <b-select style="float:left;width:80%;font-family:'arial'" plain v-model="toaccount1">
            <option v-for="(item, idx) of to" v-bind:key="idx" style="padding:10px;text-align:left;font-size:20px;height:30px" :value="item[1]">
              {{item[0]}}
            </option>
          </b-select>
          <div style="clear:both"></div>
        </b-form-group><br>
        <div style="clear:both"></div><br>
        <b-btn @click="submitform1()" style="float:left" variant="dark">انتقال به حساب معاملاتی</b-btn>
      </fieldset>




      <fieldset class="demo-vertical-spacing-sm tabsss positive" style="display:none">
        <b-form-group>
          <p style="margin-right:20%">موجودی : <button style="padding:2px 30px;" class="btn btn-light">{{coinbalance}}</button></p>
          <label style="width:20%" >از</label>
          <b-select style="float:left;width:80%;font-family:'arial'" plain v-model="fromaccount2" @change="getcoinbalance(fromaccount2)">
            <option v-for="(item, index) of from" v-bind:key="index" style="padding:10px;text-align:left;font-size:20px;height:30px" :value="item[1]">
              {{item[0]}}
            </option>
          </b-select>
          <div style="clear:both"></div>
        </b-form-group>
        <b-form-group label="">
          <b-input style="width:80%;float:left;font-family:'arial'" step="any" type="number" v-model="amount2" placeholder="" /><label style="width:20%">مقدار</label>
        </b-form-group>
        <div style="clear:both"></div>
        <b-form-group>
          <label style="width:20%" >به</label>
          <b-input style="width:80%;float:left;font-family:'arial'" readonly value="حساب اصلی"></b-input>
          <div style="clear:both"></div>
        </b-form-group><br>
        <div style="clear:both"></div><br>
        <b-btn @click="submitform2()" style="float:left" variant="dark">انتقال به حساب اصلی</b-btn>
      </fieldset>
    </b-card>

  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'pages-forums-list',
  metaInfo: {
    title: 'کیف ها'
  },
  mounted () {
    document.title = ' AMIZAS Exchange | شارژ حساب مرجین'
    this.checklevel()
    this.check()
    this.getmargin()
    this.getusdt()
    this.getbalance()
  },
  data: () => ({
    options: [],
    amount: 0.0,
    amount1: 0.0,
    amount2: 0.0,
    cardnumber: 0,
    errors: [],
    errors1: [],
    errors2: [],
    to: [],
    usdt: [],
    from: [['حساب اصلی' , 0]],
    balance : 0,
    coinbalance: 0,
    fromaccount1: 0,
    toaccount1: 0,
    fromaccount2: 0,
    toaccount2: 0,
    usdtaccount: [],

  }),
  methods: {
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
    async submitform1 () {
      this.errors1 = []
      if (this.amount1 === 0) {
        this.errors.push('لطفا مبلغ را وارد کنید')
      }
      if (!this.toaccount1) {
        this.errors1.push('لطفا حساب مرجین را انتخاب کنید')
      }
      await axios
        .post('/cp_transfer' , {from_account: this.fromaccount1 , to_account: this.toaccount1,amount: this.amount1 , coin_type:'USDT'})
        .then(response => {
        })
    },
    async submitform2 () {
      this.errors2 = []
      if (this.amount2 === 0) {
        this.errors2.push('لطفا مبلغ را وارد کنید')
      }
      if (!this.fromaccount2) {
        this.errors2.push('لطفا حساب مرجین را انتخاب کنید')
      }
      await axios
        .post('/cp_transfer' , {from_account: this.fromaccount2 , to_account: this.toaccount2,amount: this.amount2 , coin_type:'USDT'})
        .then(response => {
        })
    },
    async getmargin () {
      var itemm
      await axios
        .get('/cp_mg_market')
        .then(response => {
          this.to = response.data
          this.from = response.data
        })
    },
    async getusdt () {
      var itemm
      await axios
        .get('/cp_mg_usdt')
        .then(response => {
          this.usdt = response.data
        })
    },
    async getbalance () {
      var itemm
      await axios
        .get('/cp_mg_main')
        .then(response => {
          this.balance = response.data
        })
    },
    async getcoinbalance (sym) {
      for (var item of this.from){
        if (parseInt(item[1]) === parseInt(sym)){
          sym = item[0]
        }
      }
      await axios
        .post('/cp_balance', {sym : sym})
        .then(response => {
          this.coinbalance = response.data['balance']['buy_type']
        })
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
  }
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
.act{
  background-color: white!important;;
  color: black;
}
.act:hover{
  color: black;
}
</style>
