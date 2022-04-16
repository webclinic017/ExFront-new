<template>
  <div class="container px-0">

    <h1 class="text-center font-weight-bolder ">
      بازار اصلی
    </h1>
    <h3 class="text-center font-weight-bolder">{{tradename}}</h3>
    <VueTradingView v-if="id !== 3 && load " :options="{
      symbol: `${trade}`,
      theme: 'light',
      hide_side_toolbar: false,
      allow_symbol_change: true,
      details: true,
      calendar: true
    }"/>
    <br><br>
    <div class="row no-gutters  text-center" style="width:90% ;margin:auto">

      <div class="d-flex col-md flex-column py-4 alert-success" style="padding:15px">
        <b-input placeholder="مقدار" @input="bchecktotal()" v-model="bamount"></b-input><br>
        <b-input placeholder="قیمت" @input="bchecktotal()" v-model="bprice"></b-input><br>
        <b-input readonly placeholder="مجموع" v-model="btotal"></b-input><br>
        <h5 style="width:100% ; text-align:right"> موجودی: {{sbalance}}  </h5>
        <h5 style="width:100% ; text-align:right">پایین‌ترین پیشنهاد فروش: {{smin}} <button @click="entsmin()" class="btn btn-dark btnn">انتخاب</button> </h5>
        <b-btn @click="buysubmit()"  variant="success">خرید</b-btn>
      </div>

       <div style="width:5%">
      </div>

      <div class="d-flex col-md flex-column py-4 alert-danger" style="padding:15px">
        <b-input placeholder="مقدار" @input="schecktotal()" v-model="samount"></b-input><br>
        <b-input placeholder="قیمت" @input="schecktotal()" v-model="sprice"></b-input><br>
        <b-input readonly placeholder="مجموع" v-model="stotal"></b-input><br>
        <h5 style="width:100% ; text-align:right">موجودی: {{bbalance}} </h5>
        <h5 style="width:100% ; text-align:right">بالاترین پیشنهاد خرید: {{bmax}} <button @click="entbmax()" class="btn btn-dark btnn">انتخاب</button></h5>
        <b-btn @click="sellsubmit()" variant="danger">فروش</b-btn>
      </div>
    </div><br><br>

    <div class="row no-gutters  text-center" style="width:90% ;margin:auto">

       <div class="d-flex col-md flex-column py-4 alert-danger" style="padding:0!important">
         <h4 style="text-align:center; width:100%; height:40px;padding:5px;margin:0" class="btn-danger">پیشنهاد های فروش</h4>
          <table class="table table-striped">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">قیمت</th>
      <th scope="col">مقدار</th>
      <th scope="col">مبلغ کل</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="(item , idx) in selltrades" v-bind:key="idx">
      <th scope="row">{{idx+1}}</th>
      <td>{{item.price}}</td>
      <td>{{item.amount}}</td>
      <td>{{item.amount * item.price}}</td>
    </tr>
  </tbody>
</table>
      </div>

 <div style="width:5%">
      </div>

      <div class="d-flex col-md flex-column py-4 alert-success" style="padding:0!important">
         <h4 style="text-align:center; width:100%; height:40px;padding:5px;margin:0" class="btn-success">پیشنهاد های خرید</h4>
          <table class="table table-striped">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">قیمت</th>
      <th scope="col">مقدار</th>
      <th scope="col">مبلغ کل</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="(item , idx) in buytrades" v-bind:key="idx">
      <th scope="row">{{idx+1}}</th>
      <td>{{item.price}}</td>
      <td>{{item.amount}}</td>
      <td>{{item.amount * item.price}}</td>
    </tr>
  </tbody>
</table>
      </div>

    </div>
    <div style="height:150px"></div>
  </div>
</template>

<script>
import axios from 'axios'
import VueTradingView from 'vue-trading-view'
export default {
  name: 'pages-pricing',
  metaInfo: {
    title: 'Pricing - Pages'
  },
  data: () => ({
    tradename: '',
    trade: '',
    sbalance: 0,
    bbalance: 0,
    bmax: 0,
    smin: 0,
    load: false,
    id: 0,
    buytrades: [],
    selltrades: [],
    bamount: '',
    samount: '',
    bprice: '',
    sprice: '',
    btotal: 0,
    stotal: 0
  }),
  mounted () {
    document.title = ' AMIZAS Exchange | بازار حرفه ای '
    this.checklevel()
    this.gettrade()
    this.gettradebuyorders()
    this.gettradesellorders()
    this.gettradeinfo()
  },
  methods: {
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
          else{
            this.createwallet(id)
          }
        })
    },
    async gettrade () {
      await axios
        .post(`/protrades/${this.$route.params.id}`)
        .then(response => {
          this.trade = String(response.data[0].brand)
          this.tradename = response.data[0].name
          if (parseInt(this.$route.params.id) !== 3) {
            this.load = true
          }
        })
        .catch(() => {
        })
    },
    async sellsubmit () {
      const formData = {
        price: this.sprice,
        amount: this.samount
      }
      await axios
        .post(`/protradesellorders/${this.$route.params.id}`, formData)
        .then(response => {
          location.reload()
        })
        .catch(error => {
          this.$swal('<div class="swal2-icon swal2-error swal2-icon-show" style="display: flex;"><span class="swal2-x-mark"><span class="swal2-x-mark-line-left"></span><span class="swal2-x-mark-line-right"></span></span></div><h5>موجودی کافی نیست</h5>')
        })
    },
    async buysubmit () {
      const formData = {
        price: this.bprice,
        amount: this.bamount
      }
      await axios
        .post(`/protradebuyorders/${this.$route.params.id}`, formData)
        .then(response => {
          location.reload()
        })
        .catch(() => {
          this.$swal('<div class="swal2-icon swal2-error swal2-icon-show" style="display: flex;"><span class="swal2-x-mark"><span class="swal2-x-mark-line-left"></span><span class="swal2-x-mark-line-right"></span></span></div><h5>موجودی کافی نیست</h5>')
        })
    },
    async gettradebuyorders () {
      await axios
        .get(`/protradebuyorders/${this.$route.params.id}`)
        .then(response => {
          this.buytrades = response.data
        })
        .catch(() => {
        })
    },
    async gettradesellorders () {
      await axios
        .get(`/protradesellorders/${this.$route.params.id}`)
        .then(response => {
          this.selltrades = response.data
        })
        .catch(() => {
        })
    },
    async gettradeinfo () {
      await axios
        .get(`/protradesinfo/${this.$route.params.id}`)
        .then(response => {
          this.sbalance = response.data.sbalance.toFixed(0)
          this.bbalance = response.data.bbalance
          this.bmax = response.data.bmax
          this.smin = response.data.smin
        })
        .catch(() => {
        })
    },
    entsmin () {
      this.bprice = this.smin
    },
    entbmax () {
      this.sprice = this.bmax
    },
    bchecktotal () {
      this.btotal = this.bprice * this.bamount
    },
    schecktotal () {
      this.stotal = this.sprice * this.samount
    }
  },
  components: {
    VueTradingView
  }
}
</script>
<style>
tr{
  border-color:black!important
}
th{
  font-size: 18px;
}
.btnn{
  padding:2px;
  margin-top: 8px;
  margin-right:10px;
}
</style>
