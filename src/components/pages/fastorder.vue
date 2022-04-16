<template>
  <div class="container px-0">

    <h1 class="text-center font-weight-bolder ">
     سفارش سریع
    </h1>
    <h3 class="text-center font-weight-bolder">{{tradename}}</h3>
   <br><br>
    <div class="row no-gutters  text-center" style="width:55% ;margin:auto">
    </div>
    <div class="row no-gutters  text-center" style="width:55% ;margin:auto">

      <div  v-if="!sell" class="d-flex col-md flex-column py-4 alert-success" style="padding:15px">
      <b-button style="position:absolute;width:45%; left:10px!important" @click="sell = false" variant="success">خرید</b-button>
      <b-button style="position:absolute;width:45%; right:10px!important" @click="sell = true" variant="danger">فروش</b-button>
      <div style="clear:both ;height:50px"></div>
      <br>
        <select @change="gettradeinfo()" placeholder="نوع ارز" v-model="currency" class="form-control" style="padding:5px;">
          <option value="0" disabled selected>نوع ارز را انتخاب کنید</option>
          <option v-for="(item, idx) in currencies" v-bind:key="idx" :value="`${item.id}`">{{item.get_bname}}</option>
          </select><br>
        <b-input @input="getbuytradeinfoamount()" v-model="amount" placeholder="مقدار "></b-input><br>
        <b-input @input="getbuytradeinfototal()" v-model="total" placeholder="مبلغ کل (ریالی) ">></b-input><br>
        <h5 style="width:100% ; text-align:right">حداکثر مقدار قابل خرید: <input class="hide" disabled v-model="maxsell"></h5>
        <h5 style="width:100% ; text-align:right">موجودی: <input class="hide" disabled v-model="sbalance"></h5>
        <h5 style="width:100% ; text-align:right">دریافتی شما: <input class="hide" disabled v-model="bgetting"></h5>
        <h5 style="width:100% ; text-align:right">قیمت تمام شده هر بیت‌کوین: <input class="hide" disabled v-model="bgettingprice"></h5>
        <b-btn variant="success">خرید</b-btn>
      </div>

      <div v-if="sell" class="d-flex col-md flex-column py-4 alert-danger" style="padding:15px">
      <b-button style="position:absolute;width:45%; left:10px!important" @click="sell = false" variant="success">خرید</b-button>
      <b-button style="position:absolute;width:45%; right:10px!important" @click="sell = true" variant="danger">فروش</b-button>
      <div style="clear:both ;height:50px"></div>
      <br>
        <select placeholder="نوع ارز" v-model="currency" class="form-control" style="padding:5px;">
          <option value="0" disabled selected>نوع ارز را انتخاب کنید</option>
          <option v-for="(item, idx) in currencies" v-bind:key="idx" :value="`${item.id}`">{{item.get_bname}}</option>
          </select><br>
        <b-input @input="getselltradeinfoamount()" v-model="amount" placeholder="مقدار "></b-input><br>
        <b-input @input="getselltradeinfototal()" v-model="total" placeholder="مبلغ کل (ریالی) "></b-input><br>
        <h5 style="width:100% ; text-align:right">حداکثر مقدار قابل خرید: <input class="hide" disabled v-model="maxbuy"></h5>
        <h5 style="width:100% ; text-align:right">موجودی: <input class="hide" disabled v-model="bbalance"></h5>
        <h5 style="width:100% ; text-align:right">دریافتی شما: <input class="hide" disabled v-model="sgetting"></h5>
        <h5 style="width:100% ; text-align:right">قیمت تمام شده هر بیت‌کوین: <input class="hide" disabled v-model="sgettingprice"></h5>
        <b-btn variant="danger">فروش</b-btn>
      </div>
    </div><br><br>
    <div style="height:150px"></div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'pages-pricing',
  metaInfo: {
    title: 'Pricing - Pages'
  },
  data: () => ({
    tradename: '',
    trade: '',
    currency: 1,
    load: false,
    id: 0,
    sell: false,
    maxbuy: 0,
    maxsell: 0,
    bgettingprice: 0,
    bbalance: 0,
    sbalance: 0,
    bgetting: 0,
    sgetting: 0,
    total: '',
    currencies: [],
    amount: '',
    timeout: 0
  }),
  mounted () {
    this.gettrade()
    this.getc()
    this.gettradeinfo()
  },
  methods: {
    async gettrade () {
      await axios
        .get('/maintrades')
        .then(response => {
          this.trade = response.data[0].brand
          this.tradename = response.data[0].name
          if (parseInt(this.$route.params.id) !== 3) {
            this.load = true
          }
        })
        .catch(() => {
        })
    },
    async gettradeinfo () {
      clearTimeout(this.timeout)
      if (this.currency !== 0) {
        await axios
          .get(`/fasttradesinfo/${this.currency}`)
          .then(response => {
            this.maxbuy = response.data.maxbuy
            this.maxsell = response.data.maxsell
            this.bbalance = response.data.bbalance
            this.sbalance = response.data.sbalance
            this.buytrades = response.data.buymaintrades
            this.selltrades = response.data.sellmaintrades
            if (parseInt(this.$route.params.id) !== 3) {
              this.load = true
            }
          })
        this.timeout = setTimeout(() => {
          this.gettradeinfo()
        }, 5000)
      }
    },
    getbuytradeinfototal () {
      var all = 0
      for (var item of this.selltrades) {
        all += item.amount * item.price
        if (all > this.total) {
          this.bgetting = this.total / item.price * 0.985
          this.amount = this.total / item.price
          this.bgettingprice = this.total / this.bgetting
          return
        }
      }
    },
    getbuytradeinfoamount () {
      var all = 0
      for (var item of this.selltrades) {
        all += item.amount
        if (all > this.amount) {
          this.bgetting = this.amount * 0.985
          this.total = this.amount * item.price
          this.bgettingprice = this.total / this.bgetting
          return
        }
      }
    },
    getselltradeinfototal () {
      var all = 0
      for (var item of this.buytrades) {
        all += item.amount * item.price
        if (all > this.total) {
          this.bgetting = this.total / item.price * 0.985
          this.amount = this.total / item.price
          this.bgettingprice = this.total / this.bgetting
          return
        }
      }
    },
    getselltradeinfoamount () {
      var all = 0
      for (var item of this.buytrades) {
        all += item.amount
        if (all > this.amount) {
          this.bgetting = this.amount * 0.985
          this.total = this.amount * item.price
          this.bgettingprice = this.total / this.bgetting
          return
        }
      }
    },
    async getc () {
      await axios
        .get('/maintrades')
        .then(response => {
          this.currencies = response.data
        })
    }
  },
  components: {
  }
}
</script>
<style>
.hide{
  background-color: rgba(255,255,255,0);
  border-style: hidden;
}
</style>
