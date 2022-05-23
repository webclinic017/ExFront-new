<template>
  <div>


      <b-card no-body class="col-12" style="text-align:center">
        <b-card-header style="font-family:'arial'">
          <h3 class="col-12 cent">{{wallets.brand}}</h3>
        </b-card-header>
          <b-card-body class="py-3 wallets">
            <h4>
              Available <br>
              <div v-if="wallets.balance" class="col-12 cent"> {{wallets.balance.toFixed(6)}} <div v-if="!wallets.balance">0</div> </div>
            </h4>

          </b-card-body>
      </b-card>
      <b-card>
        <form @submit.prevent="submit()">
          <b-card-header class="row no-gutters align-items-center">
            <h2 class="row no-gutters align-items-center">برداشت</h2>
          </b-card-header>
        <div v-if="wallets.balance"><br><br>
        <select class="form-control" v-model="chain" @change="getfee()" style="font-family:'arial'">
          <option class="op" v-for="(item,name) in wallets.address" v-bind:key="name" :value="name" style="font-family:'arial'">{{name}}</option>
        </select><br>
          <h6> مبلغ درخواستی <a type="button" v-if="!wallets.balance > 0" @click="amountset()" class="btn btn-dark" style="background:white;padding:3px;color:#888s">  موجودی قابل انتقال : 0</a>  <a v-if="wallets.balance -( parseFloat(fee) + (parseFloat(fee)/2)) > 0" @click="amountset()" class="btn btn-dark" style="background:white;padding:3px;color:#888s">  موجودی قابل انتقال : {{wallets.balance}}</a></h6>
          <b-input class="" v-model="amountout"></b-input><br>
          <h6> آدرس ولت </h6>
          <b-input class="" v-model="walletout"></b-input><br>
          مبلغ دریافتی : <a  v-if="amountout - parseFloat(fee) < 0" @click="amountset()"  style="background:white;padding:3px;color:#888s;font-family:'arial'">     0</a>  <a style="background:white;padding:3px;color:#888s;font-family:'arial'" v-if="amountout - parseFloat(fee)  > 0" @click="amountset()"  >     {{amountout - parseFloat(fee)}}</a><br><br>
          <button id="withdraw" class="btn btn-dark">ثبت درخواست</button>
        </div>
        </form>
        <div id="withdraw"></div>
      </b-card>

        <b-card >
          <b-card-header class="row no-gutters align-items-center">
            <h2 class="row no-gutters align-items-center">واریز</h2>
          </b-card-header>

          <form @submit.prevent="submitdep" label="" style="text-align:center">
            <img v-if="address" id="qr" :src=" `https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=${address}`"><br><br><br>
            <select class="form-control" v-model="chain2" @change="getaddress()" style="font-family:'arial'">
              <option class="op" v-for="(item,name) in wallets.address" v-bind:key="name" :value="name" style="font-family:'arial'">{{name}}</option>
            </select><br>
            <label for="address" id="addresslable">آدرس</label>
            <b-input v-model="address" id="address" name="address" readonly></b-input>
            <br>
            <b-card>
              <label for="hash" id="hashlable">مقدار </label>
              <div class="input-group mb-3" style="direction:ltr ; margin:0">
                <div class="input-group-prepend">
                  <span class="input-group-text" id="basic-addon1">|{{sym}}|</span>
                </div>
                <b-input step="any" min="0.000000000001" required id="amount"  type="number" v-model="amountin" />
              </div>
               <label for="hash" id="hashlable">کد هش</label>
            <b-input id="hash" required v-model="hash" placeholder=" کد پیگیری - هش " />
            </b-card><br>
           
            <button class="btn btn-dark" type="submit"> ثبت واریز</button>
          </form>
          <div  id="deposit"></div>
        </b-card><br><br>

      <b-card>
        <h2 class="row no-gutters align-items-center">تاریخچه</h2><br>
         <div class="table-responsive " style="margin-bottom:-20px" >
        <table class="table table-light" style="direction:rtl!important">
          <thead class="" style="color:white!important;background:#888s">
            <tr>
              <th class="col-4 cent">مقدار</th>
              <th colspan="2" class="col-4 cent">زمان</th>
              <th class="col-4 cent ">نوع</th>
            </tr>
          </thead>
        <tbody v-if="history" >
          <tr v-for="(section, idx) in history" v-bind:key="idx">
              <td class="col-4 cent">{{section.amount}}</td>
              <td colspan="2" class="col-4 cent">{{new Date(section.time * 1000).toISOString().replace('T' , '   |   ').replace('Z' , '').replace('.000' , '')}}</td>
              <td class="col-4 cent" v-if="section.transfer_to" style="color:green">واریز</td>
              <td class="col-4 cent" v-if="!section.transfer_to" style="color:red">برداشت</td>
          </tr>
          


          <tr>
              <th colspan="2" style="color:white!important;background:#888s" class="col-6 cent">مجموع واریز</th>
              <th colspan="2" style="color:white!important;background:#888s" class="col-6 cent">مجموع برداشت</th>
            </tr>
            <tr>
              <td colspan="2" class="col-6 cent">{{dall}}</td>
              <td colspan="2" class="col-6 cent">{{wall}}</td>
            </tr>


        </tbody>
            </table>
        </div>
         <div id="history"></div>
      </b-card><br><br>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'pages-forums-list',
  metaInfo: {
    title: 'کیف ها'
  },
  beforeMount () {
    this.getw()
  },
  mounted () {
    this.checklevel()
    this.getw()
    this.gethis()
    this.goto()
  },
  updated () {
    
  },
  data: () => ({
    depfee : 0,
    mainwal: '',
    depwallets: [],
    walletout: '',
    amountout: 0,
    amountin: 0,
    address: '',
    hash: '',
    value: '',
    size: 200,
    currencies: {},
    wallets: [],
    fee : 0,
    chain: '',
    chain2: '',
    history:[],
    curs: {},
    wall: 0,
    dall: 0,
    sym: '',
  }),
  forumPath: [
    { text: 'کیف ها', active: true }
  ],
  methods: {
    async gethis () {
      const id = this.$route.params.id
      await axios
        .get(`/cp_history/${id}`)
        .then(response => {
          this.history = response.data.data
          for (var item of response.data.data){
            if(item.transfer_to){
              this.dall = this.dall + parseFloat(item.amount)
            }
            if(!item.transfer_to){
              this.wall = this.wall + parseFloat(item.amount)
            }
          }
        })
    },
    async getaddress () {
     if(this.chain2){
        await axios
        .post('/cp_address' , {sym: this.chain2})
        .then(response => {
          this.address = response.data.coin_address
        })
     }
    },
    async getw () {
      const id = this.$route.params.id
      await axios
        .get(`/cp_wallet/${id}`)
        .then(response => {
          this.wallets = response.data
        }).then(() => {
          this.getcurs()
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
    async getcurs (id) {
      await axios
        .get(`/currencies`)
        .then(response => {
          for (var item of response.data)
          if( item.brand === this.wallets.brand){
            this.curs[item.name] = item
          }
        })
    },
    async submit () {
      const id = this.chain
      await axios
        .post(`/cp_withdraw/${id}`, {amount: this.amountout , address: this.walletout})
        .then(data => {
          if (typeof data.data == 'string'){
            this.$swal(`<div class="swal2-icon swal2-error swal2-icon-show" style="display: flex;"><span class="swal2-x-mark"><span class="swal2-x-mark-line-left"></span><span class="swal2-x-mark-line-right"></span></span></div><h5>${data.data}</h5>`)
          } else {
            this.$swal('درخواست شما با موفقیت ثبت شد')
            this.amountout = 0
            this.walletout = ''
            this.getw()
          }
        })
    },
    async submitdep () {
      await axios
        .post(`/cp_deposit`, {amount: this.amountin, hash:this.hash, currency: this.$route.params.id})
        .then(data => {
          if (typeof data.data == 'string'){
            this.$swal(`<div class="swal2-icon swal2-error swal2-icon-show" style="display: flex;"><span class="swal2-x-mark"><span class="swal2-x-mark-line-left"></span><span class="swal2-x-mark-line-right"></span></span></div><h5>${data.data}</h5>`)
          } else {
            this.$swal('درخواست شما با موفقیت ثبت شد')
            this.amountin = 0
          }
        })
    },
    amountset () {
      this.amountout = this.wallets.balance
    },
    depamountset () {
      this.amountin = this.wallets.balance
    },
    goto () {
        document.querySelector(`#${this.$route.params.place}`).scrollIntoView({ behavior: 'smooth' })
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
.wallets:hover{
  background: #efefff;
}
.qr{
  width: 20%;
  margin-right: 40%;
  margin-top: 20px;
}
.address{
  margin:auto;
  text-align: center;
  margin-top: 10px;
  height: 65px;
  padding: 0;
}
.address h3{
  padding: 14px;
  white-space: nowrap;
  overflow-x: auto;
  overflow-y: hidden;
  height: 100%;
}
.addressbtn{
  float: left;
  height: 100%;
}
.address h3::-webkit-scrollbar {
  width: 1px;
}

.address h3::-webkit-scrollbar-track {
    box-shadow: inset 0 0 6px rgba(0,0,0,0.3);
    width: 3px;
    border-radius: 1px;
}

.address h3::-webkit-scrollbar-thumb {
    border-radius: 1px;
    box-shadow: inset 0 0 6px rgba(0,0,0,0.5);
    width: 3px;
}
.cent{
  margin:auto;
  text-align: center;
}
.nav-link {
  padding:15px;
  padding-left: 15px!important;
  text-align:center
}
input{
  font-family: 'arial';
}
</style>
