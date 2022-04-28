<template>
  <div>
  <br>
    <h1 style="text-align:center">{{user.id}} - {{$route.params.id}}</h1>
    <br>
    <div>
      <b-card no-body class="col-12">
        <b-card-header style="cursor:pointer" @click="tab('one')" >
          <h3>اطاعات کاربر</h3>
        </b-card-header>
        <b-card-body id="one" hidden v-if="userinfo">
          <label for="">نام</label>
          <b-input :value="userinfo.first_name"></b-input>
          <label for="">نام خانوادگی</label>
          <b-input :value="userinfo.last_name"></b-input>
          <label for="">کد ملی</label>
          <b-input :value="userinfo.get_melli"></b-input>
          <label for="">موبایل</label>
          <b-input :value="userinfo.mobile"></b-input>
          <label for="">تلفن ثابت</label>
          <b-input :value="userinfo.phone"></b-input>
          <label for="">آدرس</label>
          <b-input :value="userinfo.address"></b-input>
        </b-card-body>
      </b-card><br><br>

      <b-card no-body class="col-12">
        <b-card-header style="cursor:pointer" @click="tab('six')" >
          <h3> تایید هویت</h3>
        </b-card-header>
        <b-card-body id="six" hidden v-if="userinfo">
          <button v-if="!verify.idv" class="alert alert-secondary alerts ">
            
            <img style="width:80%;max-height:60% " src="https://amizax.com/img/verify/id.png" alt=""><br>
              <h2>1</h2>
              اطاعات هویتی
             </button> 

          <button v-if="verify.idv" class="alert alert-success alerts">
            
            <img style="width:80%;max-height:60% " src="https://amizax.com/img/verify/id.png" alt=""><br>
              <h2>1</h2>
              اطاعات هویتی
             </button> 

          <button v-if="!verify.mobilev | !verify.emailv | !verify.isphone"  class="alert alert-secondary alerts" > 

            <img style="width:80%;max-height:60% " src="https://amizax.com/img/verify/mobile.png" alt=""><br>
            <h2>2</h2>
             اطاعات تماس</button>

            <button  v-if="verify.mobilev && verify.emailv && verify.isphone" class="alert alert-success alerts"  > 

            <img style="width:80%;max-height:60% " src="https://amizax.com/img/verify/mobile.png" alt=""><br>
            <h2>2</h2>
             اطاعات تماس</button>


          <button v-if="!verify.melliv | !verify.acceptv" class="alert alert-secondary alerts">

            <img style="width:80%;max-height:60% " src="https://amizax.com/img/verify/upload.png" alt=""><br>
            <h2>3</h2>
            ارسال مدارک</button> 

           <button v-if="verify.melliv && verify.acceptv" class="alert alert-success alerts">

            <img style="width:80%;max-height:60% " src="https://amizax.com/img/verify/upload.png" alt=""><br>
            <h2>3</h2>
            ارسال مدارک</button> 

            <button v-if="!verify.bankv | !verify.accountv" class="alert alert-secondary alerts">
            <img style="width:80%;max-height:60% " src="http://amizax.com/img/verify/bank.png" alt=""><br>
            <h2>4</h2>
            اضافه کردن حساب بانکی</button> 

           <button v-if="verify.bankv && verify.accountv" class="alert alert-success alerts">
            <img style="width:80%;max-height:60% " src="https://amizax.com/img/verify/bank.png" alt=""><br>
            <h2>4</h2>
             اضافه کردن حساب بانکی</button> 


            <button v-if="!verify.rulev" class="alert alert-secondary alerts"> 
            <img style="width:80%;max-height:60% " src="http://amizax.com/img/verify/rules.png" alt=""><br>
            <h2>5</h2>
             قوانین و مقررات</button>


            <button v-if="verify.rulev" class="alert alert-success alerts"> 
            <img style="width:80%;max-height:60% " src="https://amizax.com/img/verify/rules.png" alt=""><br>
            <h2></h2>
            <h2>5</h2>
             قوانین و مقررات</button>
         
         <button v-if="!verify.coinv" class="alert alert-secondary alerts">
            <img style="width:80%;max-height:60% " src="https://amizax.com/img/verify/check.png" alt=""><br><br>
            <h2>6</h2>
            بررسی نهایی و تایید حساب</button> 

           <button v-if="verify.coinv" class="alert alert-success alerts">
            <img style="width:80%;max-height:60% " src="https://amizax.com/img/verify/check.png" alt=""><br><br>
            <h2>6</h2>
            بررسی نهایی و تایید حساب</button> 


            <br><br>
            <img style="width:50%;margin-right:25%;margin-left:25%" :src="verify.get_melliphoto" alt="">
            <img style="width:50%;margin-right:25%;margin-left:25%" :src="verify.get_acceptphoto" alt="">

            

<br><br>
        </b-card-body>
      </b-card><br><br>

      <b-card no-body class="col-12">
        <b-card-header style="cursor:pointer" @click="tab('two')">
          <h3>عملیات</h3>
        </b-card-header>
        <b-card-body hidden id="two" class="col-12" v-if="user"> 
        <b-button style="width:100%; margin:0" class="cent" v-if="user.is_active && !user.is_admin" variant="warning" @click="block(item.id)">مسدود کردن حساب</b-button>
        <b-button style="width:100%; margin:0" class="cent" v-if="!user.is_active && !user.is_admin" variant="light" @click="block(item.id)">فعال کردن حساب</b-button>
        <b-button style="width:100%; margin:0" class="cent" v-if="user.is_admin" disabled variant="dark" @click="block(item.id)">مدیر</b-button><br><br>
        <router-link style="width:100%; margin:0" class="cent btn btn-info" :to=" user.username + '/ticketadd'">ارسال پیام</router-link>
        <br><br>
          <div class="alert alert-dark" variant="success">
            <table class="table" style="border:transparent">
            <th class="col-4" style="border:transparent"><h3  style="color:white">سطح کاربر:</h3></th>
            <th class="col-1" style="border:transparent"><h3  style="color:white">{{user.level}}</h3></th>
            <th class="col-4" style="border:transparent">
              <input type="number" v-model="levelchangevalue" class="form-control" name="" id="">            </th>
            <th class="col-3" style="border:transparent">
              <button @click="levelchange()" class="btn btn-secondary"> تغییر</button>
            </th>
            
            </table>

          </div>
          <div class="alert alert-dark" variant="success">

             <table class="table" style="border:transparent">
            <th class="col-4" style="border:transparent"><h3 style="color:white"> کلمه عبور:</h3></th>
            <th class="col-1" style="border:transparent"></th>
            <th class="col-4" style="border:transparent"><input type="password" v-model="passchangevalue" class="form-control"></th>
            <th class="col-3" style="border:transparent">

                 <button @click="passchange()" class="btn btn-secondary"> تغییر</button>
            </th>
            
            </table>
          </div>  
        </b-card-body>

      </b-card><br><br>




      <b-card no-body class="col-12">
        <b-card-header style="cursor:pointer" @click="tab('three')">
          <h3>موجودی کیف پول ها</h3>
        </b-card-header>
        <b-card-body id="three" hidden>
        <div class="table-responsive">
          <table class="table" style="direction:rtl!important">
            <thead>
              <tr>
                <th style="width:25% ; text-align:right">نوع ارز</th>
                <th style="width:25% ; text-align:right">موجودی</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(section, idx) in currencies" v-bind:key="idx">
                <td style="width:20% ; text-align:right"><router-link :to="`/wallets/${section.id}`" class="text-big font-weight-semibold">
                <h2>{{section.name}}</h2>
                </router-link></td>
                <td style="width:25% ; text-align:right" v-if="section.id === 1" > <router-link :to="`/wallets/${section.id}`"> دارایی:<br><a style="font-family:'aria'">{{section.amount.toFixed(0)}}</a> </router-link></td>
                <td style="padding:20px; width:25% ; text-align:right" v-if="section.id !== 1" > <router-link :to="`/wallets/${section.id}`">دارایی:<br> <a style="font-family:'aria'">{{section.amount}}</a> <br>ریالی:<br><a style="font-family:'aria'"> {{(section.amount * getbrand(section.brand) * getbrand('usd')).toFixed(0)}} </a></router-link></td>
              </tr>
            </tbody>
          </table>
        </div>
        </b-card-body>

      </b-card><br><br>
      








      <b-card no-body class="col-12" style="max-height:500px;overflow:auto">
        <b-card-header style="cursor:pointer" @click="tab('four')">
          <h3>موجودی حساب ترید</h3>
        </b-card-header>
        <b-card-body id="four" hidden>
        <div class="table-responsive">
        <table class="table" style="direction:rtl!important">
          <thead>
            <tr>
              <th>Currency</th>
              <th>Available</th>
              <th>Frozen</th>
            </tr>
          </thead>
        <tbody>
          <tr v-for="(section) in wallets2" v-bind:key="section.id">
                  <td v-if="section.balance.available " style="width:15%;font-wieght:bold;font-family:'arial';font-size:20px"><router-link :to="`#`" class="text-big font-weight-semibold" >
                  {{section.brand}}
                  </router-link></td>
                  <td v-if="section.balance.available" style="padding:20px;font-family:'arial';font-size:14px"> <router-link :to="`#`"><a v-if="!section.balance.available">0</a> 
                  {{section.balance.available}}<br>
                  <div v-if="!(section.brand.includes('USD'))">
                  <a v-if="prices[section.brand + 'USDT']">{{(section.balance.available * prices[section.brand + 'USDT'].last).toFixed(2)}} USD</a><br>
                  <a v-if="prices[section.brand + 'USDT']">{{(section.balance.available * prices[section.brand + 'USDT'].last * rialprice).toFixed(0)}} ریال</a><br>
                  <a v-if="(!prices[section.brand + 'USDT'])"> در حال حاضر قیمت دلاری و <br> ریالی این ارز در دسترس نیست</a><br>                  </div>
                  <div v-if="(section.brand.includes('USD'))">
                  <a >{{section.balance.available}} USD</a><br>
                  <a >{{(section.balance.available * rialprice).toFixed(0)}} ریال</a><br>
                  </div>
                  </router-link></td>
                  <td v-if="section.balance.available " style="padding:20px;font-family:'arial';font-size:14px"> <router-link :to="`#`"><a v-if="!section.balance.frozen">0</a> {{section.balance.frozen}}</router-link></td>
          </tr>
          <tr v-for="(section) in wallets2" v-bind:key="section.name">
                  <td v-if="section.brand == 'USDT' |section.brand == 'BTC' |section.brand == 'ETH' |section.brand == 'TRX' && !section.balance.available" style="width:15%;font-wieght:bold;font-family:'arial';font-size:20px"><router-link :to="`#`" class="text-big font-weight-semibold" >
                  {{section.brand}}
                  </router-link></td>
                  <td v-if="section.brand == 'USDT' |section.brand == 'BTC' |section.brand == 'ETH' |section.brand == 'TRX' && !section.balance.available" style="padding:20px;font-family:'arial';font-size:14px"> <router-link :to="`#`"><a v-if="!section.balance.available">0</a> {{section.balance.available}}</router-link></td>
                  <td v-if="section.brand == 'USDT' |section.brand == 'BTC' |section.brand == 'ETH' |section.brand == 'TRX' && !section.balance.available" style="padding:20px;font-family:'arial';font-size:14px"> <router-link :to="`#`"><a v-if="!section.balance.frozen">0</a> {{section.balance.frozen}}</router-link></td>
          </tr>
          <tr v-for="(section) in wallets2" v-bind:key="section.id">
                  <td v-if="!(section.brand == 'USDT' |section.brand == 'BTC' |section.brand == 'ETH' |section.brand == 'TRX') && !section.balance.available" style="width:15%;font-wieght:bold;font-family:'arial';font-size:20px"><router-link :to="`#`" class="text-big font-weight-semibold" >
                  {{section.brand}}
                  </router-link></td>
                  <td v-if="!(section.brand == 'USDT' |section.brand == 'BTC' |section.brand == 'ETH' |section.brand == 'TRX') && !section.balance.available" style="padding:20px;font-family:'arial';font-size:14px"> <router-link :to="`#`"><a v-if="!section.balance.available">0</a> {{section.balance.available}}</router-link></td>
                  <td v-if="!(section.brand == 'USDT' |section.brand == 'BTC' |section.brand == 'ETH' |section.brand == 'TRX') && !section.balance.available" style="padding:20px;font-family:'arial';font-size:14px"> <router-link :to="`#`"><a v-if="!section.balance.frozen">0</a> {{section.balance.frozen}}</router-link></td>

          </tr>
        </tbody>
            </table>
        </div>
        </b-card-body>
      </b-card><br><br>






       <b-card no-body class="col-12" style="min-height:300px;max-height:500px">
        <b-card-header style="cursor:pointer" @click="tab('five')">
           <h2 >تاریخچه حساب ترید</h2>
        </b-card-header>
        <b-card-body id="five" hidden>
         <div class="table-responsive " style="margin-bottom:-20px" >
        <table class="table table-light" style="direction:rtl!important; padding:10px">
          <thead class="" style="color:white!important;background:#888">
            <tr>
              <th class="col-3 cent">نوع ارز</th>
              <th class="col-3 cent">مقدار</th>
              <th class="col-3 cent">زمان</th>
              <th class="col-3 cent">نوع</th>
            </tr>
          </thead>
        <tbody v-if="history" >
          <tr v-for="(section, idx) in history" v-bind:key="idx">
              <td class="col-3 cent">{{section.coin_type}}</td>
              <td class="col-3 cent">{{section.amount}}</td>
              <td class="col-3 cent">{{new Date(section.time * 1000).toISOString().replace('T' , '   |   ').replace('Z' , '').replace('.000' , '')}}</td>
              <td class="col-3 cent" v-if="section.transfer_to" style="color:green">واریز</td>
              <td class="col-3 cent" v-if="!section.transfer_to" style="color:red">برداشت</td>
          </tr>
          <tr>
              <th colspan="6" class="col-12 cent d-md-none"><button class="btn btn-dark">خرید | فروش</button></th>
          </tr>
        


        </tbody>
            </table>
        </div>
        <div style="clear:both"></div>
        </b-card-body>
      </b-card><br><br>


    </div>

  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'pages-forums-list',
  metaInfo: {
    title: 'Forum list - Pages'
  },
  data: () => ({
    user: [],
    currencies: [],
    wallets: [],
    wallets2: [],
    walletsback2: [],
    temp2:{},
    prices: [],
    prices2: [],
    rialprice: 0,
    passchangevalue:'',
    usd: 250000,
    temp: {},
    verify:[],
    history:[],
    levelchangevalue: 0
  }),
  mounted () {
    this.getusers()
    this.getprice()
    this.getw()
    this.getprice2()
    this.getprices()
    this.getrialprice()
  },
  beforeMount () {
    this.getusers()
    this.getprice()
    this.getw()
    this.getprice2()
  },
  beforeCreate () {
  },
  methods: {
    async getprices () {
      await axios
        .get(`/oltradeinfo`)
        .then(response => {
          this.prices = response.data
        })
    },
    async getrialprice () {
      await axios
        .get('/price' )
        .then(response => {
          this.rialprice = response.data[0].rial
        })
    },
    tab (id) {
      if(document.querySelector(`#${id}`).hidden === true){
        document.querySelector(`#${id}`).hidden = false
      }else{
        document.querySelector(`#${id}`).hidden = true
      }
    },

    async gethis () {
      const id = false
      await axios
        .get(`adminpanel/cp_history/${this.user.id}`)
        .then(response => {
          this.history = response.data.data
        })
    },




    async levelchange () {
      await axios
        .post('/adminpanel/levelchange', {username: this.$route.params.id , level: this.levelchangevalue})
        .then(response => {
          this.$swal('<div class="swal2-header"><ul class="swal2-progress-steps" style="display: none;"></ul><div class="swal2-icon swal2-success swal2-icon-show" style="display: flex;"><div class="swal2-success-circular-line-left" style="background-color: rgb(255, 255, 255);"></div><span class="swal2-success-line-tip"></span> <span class="swal2-success-line-long"></span><div class="swal2-success-ring"></div> <div class="swal2-success-fix" style="background-color: rgb(255, 255, 255);"></div><div class="swal2-success-circular-line-right" style="background-color: rgb(255, 255, 255);"></div></div><img class="swal2-image" style="display: none;"><button type="button" class="swal2-close" aria-label="Close this dialog" style="display: none;">×</button></div>' + '<h5>. با موفقیت انجام شد </h5>')
          this.getusers()
        }).then(() => {
        })
    },



    async passchange () {
      await axios
        .post('/adminpanel/changepass', {username: this.$route.params.id , pass: this.passchangevalue})
        .then(response => {
          this.$swal('<div class="swal2-header"><ul class="swal2-progress-steps" style="display: none;"></ul><div class="swal2-icon swal2-success swal2-icon-show" style="display: flex;"><div class="swal2-success-circular-line-left" style="background-color: rgb(255, 255, 255);"></div><span class="swal2-success-line-tip"></span> <span class="swal2-success-line-long"></span><div class="swal2-success-ring"></div> <div class="swal2-success-fix" style="background-color: rgb(255, 255, 255);"></div><div class="swal2-success-circular-line-right" style="background-color: rgb(255, 255, 255);"></div></div><img class="swal2-image" style="display: none;"><button type="button" class="swal2-close" aria-label="Close this dialog" style="display: none;">×</button></div>' + '<h5>. با موفقیت انجام شد </h5>')
          this.getusers()
        }).then(() => {
        })
    },


    async getw2 () {
      await axios
        .post(`adminpanel/cp_wallet/${this.user.id}`)
        .then(response => {
          this.wallets2 = response.data
          this.walletsback2 = response.data
        }).then(() => {
        })
    },
    async getprice2 () {
      await axios
        .get('/price')
        .then(response => {
          this.temp2 = response.data[0]
        })
        .catch(() => {
        })
    },
    getbrand2 (brand) {
      return this.temp[`${brand.toLowerCase()}`]
    },
    search (){
      this.wallets2 = {}
      for (const [key, value] of Object.entries(this.walletsback2)){
        if(key.includes(this.searchtext.toUpperCase())){
        this.wallets2[key] = value        
        }
      }
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
    async getc () {
      await axios
        .get('/currencies')
        .then(response => {
          this.currencies = response.data
          var itemm
          for (itemm of this.currencies) {
            itemm.amount = 0
          }
          for (let index = 0; index < this.wallets.length; index++) {
            if (this.currencies[this.wallets[index].currency - 1]) {
              this.currencies[this.wallets[index].currency - 1].amount = this.wallets[index].amount
              this.currencies[this.wallets[index].currency - 1].address = this.wallets[index].address
            }
          }
        })
    },
    async getw () {
      await axios
        .get(`/adminpanel/wallets/${this.$route.params.id}`)
        .then(response => {
          this.wallets = response.data
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







    checkadmin (){
      if (!this.$store.state.isAdmin){
            this.$swal.fire({
              title: 'توجه',
              text: 'شما به این بخش دسترسی ندارید',
              icon: 'warning',
              showCancelButton: true,
              confirmButtonColor: '#3085d6',
              cancelButtonColor: '#d33',
              confirmButtonText: 'ورود ادمین',
              cancelButtonText: 'بازگشت به صفحه اصلی'
            }).then(result => {
              if (result.isConfirmed) {
                const toPath = this.$route.go || '/adminpanel/login'
                this.$router.push(toPath)
              }else {
                const toPath = this.$route.query.to || '/'
                this.$router.push(toPath)
              }
            })
      }
    },
    async getusers () {
      await axios
        .get(`/adminpanel/user/${this.$route.params.id}`)
        .then(data => {
          this.user = data.data[0]
          this.levelchangevalue = data.data[0].level
          this.getuserinfo()
          this.getverify()
          this.getw2()
          this.gethis()
        })
    },
    async getuserinfo () {
      await axios
        .get(`/adminpanel/userinfo/${this.user.id}`)
        .then(data => {
          this.userinfo = data.data[0]
        })
    },
    async getverify () {
      await axios
        .get(`/adminpanel/verify/${this.user.id}`)
        .then(data => {
          this.verify = data.data[0]
        })
    },
    async block (id) {
      await axios
        .post('/adminpanel/user', { act: 1, id: id })
        .then(() => {
          this.$swal('<div class="swal2-header"><ul class="swal2-progress-steps" style="display: none;"></ul><div class="swal2-icon swal2-success swal2-icon-show" style="display: flex;"><div class="swal2-success-circular-line-left" style="background-color: rgb(255, 255, 255);"></div><span class="swal2-success-line-tip"></span> <span class="swal2-success-line-long"></span><div class="swal2-success-ring"></div> <div class="swal2-success-fix" style="background-color: rgb(255, 255, 255);"></div><div class="swal2-success-circular-line-right" style="background-color: rgb(255, 255, 255);"></div></div><img class="swal2-image" style="display: none;"><button type="button" class="swal2-close" aria-label="Close this dialog" style="display: none;">×</button></div>' + '<h5>     انجام شد .</h5>')
          location.reload()
        })
    },
    balance (input) {
      if (String(input).length > 3) {
        var item = String(input)
        var last = item.length % 3
        var out = item.slice(0, last) + ','
        for (var i = 0; i < parseInt(item.length / 3) - 1; i++) {
          out = out + item.slice(last + (i * 3), last + ((i + 1) * 3)) + ','
        }
        out = out + item.slice(last + ((parseInt(item.length / 3) - 1) * 3), last + (((parseInt(item.length / 3) - 1) + 1) * 3))
        return out
      } else {
        return input
      }
    }
  }
}
</script>
<style>
.center{
  text-align: center;
}
.smallin{
  width: 30%;
  margin: auto;
}
.alerts{
  width:30%;height:250px;margin:auto;float:right;margin:1.5%; margin-top:0;margin-left:1.5%
}
h2{
  color: grey;
}
@media only screen and (max-width: 1024px) {
.alerts{
  width:100%;height:auto;margin:auto;margin:1.5%; margin-top:0;margin-left:1.5%
}
}
</style>
