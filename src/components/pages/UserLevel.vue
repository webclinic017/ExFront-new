<template>
  <div>
      <br><br><h3 style="text-align:center">تایید حساب کاربری</h3><br><br>
      <b-card>
        <b-card-body>

        </b-card-body>
        <b-card-body class="col-12">
          <button v-if="!idv" class="alert alert-secondary alerts " @click="tab('onec')">
            
            <img style="width:80%;max-height:60% " src="http://amizax.com/img/verify/id.png" alt=""><br>
              <h2>1</h2>
              اطاعات هویتی
             </button> 

          <button v-if="idv" class="alert alert-success alerts">
            
            <img style="width:80%;max-height:60% " src="http://amizax.com/img/verify/id.png" alt=""><br>
              <h2>1</h2>
              اطاعات هویتی
             </button> 

          <button v-if="!mobilev | !emailv | !isphone"  class="alert alert-secondary alerts" @click="tab('twoc')"> 

            <img style="width:80%;max-height:60% " src="http://amizax.com/img/verify/mobile.png" alt=""><br>
            <h2>2</h2>
             اطاعات تماس</button>

            <button  v-if="mobilev && emailv && isphone" class="alert alert-success alerts"  > 

            <img style="width:80%;max-height:60% " src="http://amizax.com/img/verify/mobile.png" alt=""><br>
            <h2>2</h2>
             اطاعات تماس</button>


          <button v-if="!melliv | !acceptv" @click="tab('threec')" class="alert alert-secondary alerts">

            <img style="width:80%;max-height:60% " src="http://amizax.com/img/verify/upload.png" alt=""><br>
            <h2>3</h2>
            ارسال مدارک</button> 

           <button v-if="melliv && acceptv" class="alert alert-success alerts">

            <img style="width:80%;max-height:60% " src="http://amizax.com/img/verify/upload.png" alt=""><br>
            <h2>3</h2>
            ارسال مدارک</button> 

            <button v-if="!bankv | !accountv" @click="tab('fivec')" class="alert alert-secondary alerts">
            <img style="width:80%;max-height:60% " src="http://amizax.com/img/verify/bank.png" alt=""><br>
            <h2>4</h2>
            اضافه کردن حساب بانکی</button> 

           <button v-if="bankv && accountv" class="alert alert-success alerts">
            <img style="width:80%;max-height:60% " src="http://amizax.com/img/verify/bank.png" alt=""><br>
            <h2>4</h2>
             اضافه کردن حساب بانکی</button> 


            <button v-if="!rulev" @click="tab('fourc')" class="alert alert-secondary alerts"> 
            <img style="width:80%;max-height:60% " src="http://amizax.com/img/verify/rules.png" alt=""><br>
            <h2>5</h2>
             قوانین و مقررات</button>


            <button v-if="rulev" class="alert alert-success alerts"> 
            <img style="width:80%;max-height:60% " src="http://amizax.com/img/verify/rules.png" alt=""><br>
            <h2></h2>
            <h2>5</h2>
             قوانین و مقررات</button>
         
         <button v-if="!coinv" class="alert alert-secondary alerts">
            <img style="width:80%;max-height:60% " src="http://amizax.com/img/verify/check.png" alt=""><br><br>
            <h2>6</h2>
            بررسی نهایی و تایید حساب</button> 

           <button v-if="coinv" class="alert alert-success alerts">
            <img style="width:80%;max-height:60% " src="http://amizax.com/img/verify/check.png" alt=""><br><br>
            <h2>6</h2>
            بررسی نهایی و تایید حساب</button> 


          <h2 style="text-align:center;color:green" v-if="fullverified">حساب شما تایید شده است</h2>
          <h2 style="text-align:center;width:100%;text-align:center" class="btn btn-info" v-if="mobilev && bankv && emailv && idv && rulev && melliv && accountv && acceptv && !coinv">  اطاعات شما تکمیل شده و حساب شما پس از بررسی کارشناسان ما تایید خواهد شد  </h2>
<br><br>
</b-card-body>
      </b-card><br><br>



      <b-card hidden  style="margin-bottom: 50px"  class="b-ver onec" id="idcard">
        <h4  id="idtitle">ثبت اطاعات هویتی</h4><br><br><br>
          <b-input style="width:74%;float:left;height:40px" type="text" class="mellinum" v-model="first_name" id="mell" placeholder="" /><label style="width:25%;height:40px"> نام</label>
          <b-input style="width:74%;float:left;height:40px" type="text" class="mellinum" v-model="last_name" id="mell" placeholder="" /><label style="width:25%;height:40px" >  نام خانوادگی</label>
          <b-input style="width:74%;float:left;height:40px" type="text" class="mellinum" v-model="address" id="mell" placeholder="" /><label style="width:25%;height:40px" > آدرس</label>
          <b-input style="width:74%;float:left;height:40px" maxlength="10" minlength="10" type="tel" class="mellinum" v-model="postal" id="mell" placeholder="" /><label style="width:25%;height:40px" > کد پستی</label>

          <br> <br>
          <a href="javascript:void(0)" @click="submit()" id="ebtn" class="small btn btn-dark" style="float:left">ثبت اطاعات</a>
        <b-card-body class="pb-2">

        </b-card-body>
      </b-card>


      <b-card hidden  style="margin-bottom: 50px"  class="b-ver  threec" id="mellicard">
        <b-card style="text-align:center" v-if="!melliv">
          
        <h4  id="mellititle">تایید کارت ملی</h4>
        <img v-if="melliphoto" style="width:50% ;margin-left:25%;margin-right:25%" :src="melliphoto" alt="">
          <b-form-group label=" "><br><br><br>
          <b-input style="width:74%;float:left" maxlength="10" minlength="10" type="tel" class="mellinum" v-model="mellinum" id="mell" placeholder="" /><label style="width:25%" for="mell">شماره کارت ملی</label>
          <div style="clear:both"></div><br>
            <input type="file" id="filemelli" />
            <a href="javascript:void(0)" @click="submitmelli()" class=" btn btn-dark" style="margin:20px"> ارسال کارت ملی برای تایید</a>

          </b-form-group>
        </b-card><br><br>
        <b-card style="text-align:center" v-if="!acceptv">

           <h4  id="accepttitle">  ارسال برگ پذیرش مقررات</h4><br>
           <img v-if="acceptphoto" style="width:50% ;margin-left:25%;margin-right:25%" :src="acceptphoto" alt=""><br>
          <b-form-group label=" "><br><br><br>
          <div style="clear:both"></div><br>
          <a class="btn btn-dark" target="_blank" href="https://www.amizax.com/img/verify/accept.jpg">نمونه تصویر</a><br>
            <input type="file" id="fileaccept" />
            <a href="javascript:void(0)" @click="submitaccept()" class=" btn btn-dark" style="margin:20px"> ارسال برگ پذیرش مقررات</a>

          </b-form-group>

        <b-card-body class="pb-2">

        </b-card-body>
        </b-card>
      </b-card>


      <b-card hidden style="margin-bottom: 50px" class="b-ver twoc" id="mobilecard">
        <h4  v-if="!mobilev" id="mobiletitle" >تایید شماره همراه</h4>
          <b-form-group  v-if="!mobilev" label=" "><br><br>
            <b-input placeholder="*********9" maxlength="10" v-model="number"  id="mno" /><br>
            <button @click="mobilesend();getstatus()" class="small btn btn-dark" id="mbtn"><a v-if="timerNum !== 60 && timerNum !== 0">{{ timerNum }}</a> ارسال کد</button>
             <b-input hidden  :placeholder="'کد ارسال شده'" v-model="mcode" id="mc"  />
            <a hidden @click="mobileverify()" href="javascript:void(0)" class="small btn btn-success" id="mcb">تایید شماره همراه</a>

          </b-form-group><br>

        <h4 v-if="!this.isphone" id="mobiletitle" >تایید شماره ثابت</h4>
          <b-form-group v-if="!this.isphone" label=" "><br><br>
            <b-input placeholder="***********" maxlength="11" v-model="phonenum"  id="mno" /><br>
            <a @click="addphone()" href="javascript:void(0)" class="small btn btn-success" id="mcb">ثبت شماره ثابت</a>

          </b-form-group><br>


        <h4  v-if="!emailv">تایید  آدرس ایمیل </h4><br><br>
          <b-form-group v-if="!emailv" label="">
            <b-input :placeholder="'آدرس ایمیل'" type="email" id="eno" v-model="email"  /><br>
            <button href="javascript:void(0)" @click="emailsend();getstatus2()" id="ebtn" class="small btn btn-dark"><a v-if="timerNum2 !== 60 && timerNum2 !== 0">{{ timerNum2 }}</a> ارسال کد</button>
            <b-input hidden :placeholder="'کد ارسال شده'" v-model="ecode" id="ec"  />
            <a hidden @click="emailverify()" href="javascript:void(0)" id="ecb" class="small btn btn-success">تایید  آدرس ایمیل </a>

          </b-form-group>
      </b-card>



      <b-card hidden  style="margin-bottom: 50px; text-align:center"  class="b-ver  fivec" id="acceptcard" >
        <form @submit.prevent="submitcard()" action="">
        <b-card id="addcard"  header="اضافه کردن حساب بانکی" header-tag="h6" class="mb-4">
      <fieldset  class="demo-vertical-spacing-sm">
        <b-form-group >
          <b-input maxlength="16" required style="text-align:center" minlength="16" type="text" class="cardnum" v-model="cardnumber" @change="checknum()" @focusout="checknum2()" @focus="checkback()" placeholder="شماره کارت بانکی" />
          <div class="invalid-tooltip">{{ctool}}</div>
          </b-form-group>
      </fieldset>
      <fieldset  class="demo-vertical-spacing-sm">
       <div class="input-group mb-3" style="direction:ltr">
  <div class="input-group-prepend">
    <span class="input-group-text" id="basic-addon1">IR</span>
  </div>
  <input type="text" required minlength="24" maxlength="24" v-model="shebanumber" style=";text-align:center" class="form-control" placeholder="شماره شبا" aria-label="Username" aria-describedby="basic-addon1">
</div>
      </fieldset>
      <fieldset  class="demo-vertical-spacing-sm">
        <b-form-group>
          <b-input style="text-align:center"  maxlength="16" minlength="16" type="tel" class="cardnum" v-model="accountnumber" placeholder=" شماره حساب (اختیاری)" />
          <div class="invalid-tooltip">{{ctool}}</div>
          </b-form-group>
          <b-btn type="submit" variant="dark"> اضافه کردن حساب </b-btn>
      </fieldset>
    </b-card><br><br>

        <b-card-body class="pb-2">

        </b-card-body></form>
      </b-card>


      <b-card hidden v-if="!rulev" style="margin-bottom: 50px"  class="b-ver  fourc" id="rulecard">
       
       <textarea readonly class="form-control" style="overflow:scroll" rows='10' v-model="rule">
       </textarea><br>
       <input type="checkbox" @click="rulecheck()">قوانین و مقررات را مطالعه کرده و قبول میکنم
       <br>
       <b-button @click="vrule()" id="rulebtn" disabled variant="success">تایید</b-button>
      </b-card>


  </div>
</template>

<script>
import VueStepProgressIndicator from 'vue-step-progress-indicator'
import axios from 'axios'


export default {
  name: 'pages-user-edit',
  metaInfo: {
    title: 'User edit - Pages'
  },
  components: {
    VueStepProgressIndicator,
  },
  data: () => ({
    errors: [],
    timer: null, 
    timer2: null, 
    phonenum : '',
    timerNum: 60 ,
    timerNum2: 60 ,
    disabled: false,
    process: 0,
    fullverified : false,
    idv: false,
    mobilev: false,
    emailv: false,
    rulev: false,
    shebanumber: '',
    acceptv: false,
    accountnumber:'',
    coinv: false,
    accountv: false,
    bankv : false,
    melliv: false,
    paperv: false,
    cardnumber: '',
    ctool: '',
    number: '',
    acceptphoto: '',
    melliphoto: '',
    mellinum: '',
    rule: '',
    first_name: '',
    isphone: false,
    last_name: '',
    address: '',
    postal: '',
    email: '',
    mcode: '',
    ecode: '',
    bv: 0,
    userData: {
      avatar: '5-small.png',
      name: '',
      username: '',
      email: '',
      company: '',
      verified: true,
      fullverified: false,
      status: 1,
      level: 0
    }
  }),
  created () {
    this.aa()
  },
  mounted () {
    this.get_user()
    this.check()
    this.verify()
    this.getrule()
    this.perpetual()
  },
  beforeDestroy() {
            clearInterval(this.timer);        
            this.timer = null;
        },
  methods: {
    rulecheck(){
      document.getElementById('rulebtn').disabled = false
    },
    getStatus() {
                this.loading(); // Start timer
                this.timer = setInterval(() => {  //Create timer
                    if (this.timerNum <= 0) { // Operation after setting timer time to 0
                        this.timer && this.clearTimer(); // off timer 
                        document.getElementById('mbtn').disabled = false
                    } else {
                        this.loading();
                    }
                }, 1000);
            },
            loading() { // Start timer
                this.timerNum -= 1; // Timer minus 1
                this.text = 'Acquisition(' + this.timerNum + ')';
            },
            clearTimer() {//Clear timer
                clearInterval(this.timer);
                this.timer = null;
            },
    getStatus2() {
                this.loading2(); // Start timer
                this.timer2 = setInterval(() => {  //Create timer
                    if (this.timerNum2 === 0) { // Operation after setting timer time to 0
                        this.timer2 && this.clearTimer2(); // off timer 
                        document.getElementById('ebtn').disabled = false
                    } else {
                        this.loading2();
                    }
                }, 1000);
            },
            loading2() { // Start timer
                this.timerNum2 -= 1; // Timer minus 1
                this.text2 = 'Acquisition(' + this.timerNum2 + ')';
            },
            clearTimer2() {//Clear timer
                clearInterval(this.timer2);
                this.timer2 = null;
            },
    async verify () {
      await axios
        .get('/verify')
        .then(response => {
          const data = response.data[0]
          this.mobilev = data.mobilev
          this.emailv = data.emailv
          this.melliv = data.melliv
          this.rulev = data.rulev
          this.phonenum = data.phonenum
          this.idv = data.idv
          this.coinv = data.coinv
          this.acceptv = data.acceptv
          this.bankv = data.bankv
          this.accountv = data.accountv
          this.melliphoto = data.get_melliphoto
          this.acceptphoto = data.get_acceptphoto
           if (!data.idv) {
            document.querySelector('#idcard').hidden = false
            document.querySelector('#idtitle').hidden = false
          } else if (!data.mobilev) {
            document.querySelector('#mobilecard').hidden = false
            document.querySelector('#mobiletitle').hidden = false
          } else if (!data.emailv) {
            document.querySelector('#mobilecard').hidden = false
            document.querySelector('#mobilecard').hidden = false
          } else if (!data.bankv) {
            if (this.bv) {
              document.querySelector('#bankcard').hidden = false
              document.querySelector('#banktitle').hidden = false
          } else if (!data.melliv) {
              document.querySelector('#mellicard').hidden = false
              document.querySelector('#mellititle').hidden = false
          } else if (!data.melliv) {
              document.querySelector('#mellicard').hidden = false
              document.querySelector('#mellititle').hidden = false
          }} else if (!data.rulev) {
            document.querySelector('#rulecard').hidden = false
          }
          if(data.mobilev && data.bankv && data.emailv && data.idv && data.rulev && data.melliv && data.coinv && data.accountv && data.acceptv){
            this.fullverified = true
          }
        })
    },
    async getrule () {
      await axios
        .get('/general')
        .then(response => {
          this.rule = response.data[0].rule
        })
    },
    check () {
      if (!this.$store.state.isAuthenticated) {
        const toPath = this.$route.query.to || '/login'
        this.$router.push(toPath)
      }
    },
    tab(id){
      document.querySelectorAll('.b-ver').forEach(item => {
        item.hidden = true
      })
      document.querySelector('.'+`${id}`).hidden = false
      this.goto(id)
    },
    goto (id) {
        document.querySelector('.'+`${id}`).scrollIntoView({ behavior: 'smooth' })
      },
    async aa () {
      await axios
        .get('/bankrequests').then(() => { this.bv = false }).catch(() => { this.bv = true })
    },
    async get_user () {
      await axios
        .get('/userinfo')
        .then(response => {
          this.userData.level = response.data[0].level
          this.isphone = response.data[0].phone
        })
    },
    async mobilesend () {
      if (parseInt(this.number[0]) === 0){
          this.$swal('<div class="swal2-icon swal2-error swal2-icon-show" style="display: flex;"><span class="swal2-x-mark"><span class="swal2-x-mark-line-left"></span><span class="swal2-x-mark-line-right"></span></span></div><h5>لطفا شماره موبایل را بدون صفر وارد کنید</h5>')
      }else if (this.number[0].includes('۰') | this.number[0].includes('۱') | this.number[0].includes('۲') | this.number[0].includes('۳') | this.number[0].includes('۴') | this.number[0].includes('۵') | this.number[0].includes('۶') | this.number[0].includes('۷۰') | this.number[0].includes('۸') | this.number[0].includes('۹')){
          this.$swal('<div class="swal2-icon swal2-error swal2-icon-show" style="display: flex;"><span class="swal2-x-mark"><span class="swal2-x-mark-line-left"></span><span class="swal2-x-mark-line-right"></span></span></div><h5>لطفا شماره موبایل را با اعداد لاتین وارد کنید</h5>')
      }
      else{
        await axios
        .put('/mobile-verify', { number: this.number })
        .then(response => {
          document.querySelector('#mno').hidden = true
          document.querySelector('#mbtn').disabled = true
          document.querySelector('#mc').hidden = false
          document.querySelector('#mcb').hidden = false
          this.$swal('<div class="swal2-header"><ul class="swal2-progress-steps" style="display: none;"></ul><div class="swal2-icon swal2-success swal2-icon-show" style="display: flex;"><div class="swal2-success-circular-line-left" style="background-color: rgb(255, 255, 255);"></div><span class="swal2-success-line-tip"></span> <span class="swal2-success-line-long"></span><div class="swal2-success-ring"></div> <div class="swal2-success-fix" style="background-color: rgb(255, 255, 255);"></div><div class="swal2-success-circular-line-right" style="background-color: rgb(255, 255, 255);"></div></div><img class="swal2-image" style="display: none;"><button type="button" class="swal2-close" aria-label="Close this dialog" style="display: none;">×</button></div>' + '<h5> کد با موفقیت ارسال شد</h5>')
        })
        .catch(response =>{
          console.log(response)
          this.$swal(`<div class="swal2-icon swal2-error swal2-icon-show" style="display: flex;"><span class="swal2-x-mark"><span class="swal2-x-mark-line-left"></span><span class="swal2-x-mark-line-right"></span></span></div><h5>${response.data}</h5>`)
        })
        this.getStatus()
      }
    },
    async mobileverify () {
      await axios
        .post('/mobile-verify', { code: this.mcode, number: this.number })
        .then(response => {
          this.verify()
          this.$swal('<div class="swal2-header"><ul class="swal2-progress-steps" style="display: none;"></ul><div class="swal2-icon swal2-success swal2-icon-show" style="display: flex;"><div class="swal2-success-circular-line-left" style="background-color: rgb(255, 255, 255);"></div><span class="swal2-success-line-tip"></span> <span class="swal2-success-line-long"></span><div class="swal2-success-ring"></div> <div class="swal2-success-fix" style="background-color: rgb(255, 255, 255);"></div><div class="swal2-success-circular-line-right" style="background-color: rgb(255, 255, 255);"></div></div><img class="swal2-image" style="display: none;"><button type="button" class="swal2-close" aria-label="Close this dialog" style="display: none;">×</button></div>' + '<h5> کد با موفقیت تایید شد</h5>')
        })
    },
    async perpetual () {
      await axios
        .post('perpetualrequest')
        .then(data => {
    })
    },
    async vrule () {
      await axios
        .get('/rulev')
        .then(response => {
          this.verify()
          this.$swal('<div class="swal2-header"><ul class="swal2-progress-steps" style="display: none;"></ul><div class="swal2-icon swal2-success swal2-icon-show" style="display: flex;"><div class="swal2-success-circular-line-left" style="background-color: rgb(255, 255, 255);"></div><span class="swal2-success-line-tip"></span> <span class="swal2-success-line-long"></span><div class="swal2-success-ring"></div> <div class="swal2-success-fix" style="background-color: rgb(255, 255, 255);"></div><div class="swal2-success-circular-line-right" style="background-color: rgb(255, 255, 255);"></div></div><img class="swal2-image" style="display: none;"><button type="button" class="swal2-close" aria-label="Close this dialog" style="display: none;">×</button></div>' + '<h5>  با موفقیت انجام شد</h5>')
        })
    },
    async emailsend () {
      document.querySelector('#ebtn').disabled = true
      await axios
        .put('/email-verify', { email: (this.email).toLowerCase().replace(' ', '').replace(' ', '') })
        .then(response => {
          document.querySelector('#eno').hidden = true
          document.querySelector('#ebtn').hidden = true
          document.querySelector('#ec').hidden = false
          document.querySelector('#ecb').hidden = false
          this.$swal('<div class="swal2-header"><ul class="swal2-progress-steps" style="display: none;"></ul><div class="swal2-icon swal2-success swal2-icon-show" style="display: flex;"><div class="swal2-success-circular-line-left" style="background-color: rgb(255, 255, 255);"></div><span class="swal2-success-line-tip"></span> <span class="swal2-success-line-long"></span><div class="swal2-success-ring"></div> <div class="swal2-success-fix" style="background-color: rgb(255, 255, 255);"></div><div class="swal2-success-circular-line-right" style="background-color: rgb(255, 255, 255);"></div></div><img class="swal2-image" style="display: none;"><button type="button" class="swal2-close" aria-label="Close this dialog" style="display: none;">×</button></div>' + '<h5> کد با موفقیت ارسال شد</h5>')
        })
        this.getStatus2()
    },
    async emailverify () {
      await axios
        .post('/email-verify', { code: this.ecode, email: this.email })
        .then(response => {
          this.verify()
          this.$swal('<div class="swal2-header"><ul class="swal2-progress-steps" style="display: none;"></ul><div class="swal2-icon swal2-success swal2-icon-show" style="display: flex;"><div class="swal2-success-circular-line-left" style="background-color: rgb(255, 255, 255);"></div><span class="swal2-success-line-tip"></span> <span class="swal2-success-line-long"></span><div class="swal2-success-ring"></div> <div class="swal2-success-fix" style="background-color: rgb(255, 255, 255);"></div><div class="swal2-success-circular-line-right" style="background-color: rgb(255, 255, 255);"></div></div><img class="swal2-image" style="display: none;"><button type="button" class="swal2-close" aria-label="Close this dialog" style="display: none;">×</button></div>' + '<h5> کد با موفقیت تایید شد</h5>')
        })
        .catch(response =>{
          this.$swal('<div class="swal2-icon swal2-error swal2-icon-show" style="display: flex;"><span class="swal2-x-mark"><span class="swal2-x-mark-line-left"></span><span class="swal2-x-mark-line-right"></span></span></div><h5>کد وارد شده معتبر نیست</h5>')
        })
    },
    async submitmelli () {
      this.errors = []
      this.errors2 = []
      if (this.amount === 0) {
        this.errors.push('لطفا مبلغ را وارد کنید')
      }
      if (!this.cardnumber) {
        this.errors.push('لطفا کارتی را انتخاب کنید')
      }
      const formdata = new FormData()
      formdata.append('mellic', this.mellinum)
      var img = document.getElementById('filemelli').files[0]
      formdata.append('melliimg', img, img.name)
      await axios
        .post('/verifymelli', formdata)
        .then(response => {
          this.verify()
          this.$swal('<div class="swal2-header"><ul class="swal2-progress-steps" style="display: none;"></ul><div class="swal2-icon swal2-success swal2-icon-show" style="display: flex;"><div class="swal2-success-circular-line-left" style="background-color: rgb(255, 255, 255);"></div><span class="swal2-success-line-tip"></span> <span class="swal2-success-line-long"></span><div class="swal2-success-ring"></div> <div class="swal2-success-fix" style="background-color: rgb(255, 255, 255);"></div><div class="swal2-success-circular-line-right" style="background-color: rgb(255, 255, 255);"></div></div><img class="swal2-image" style="display: none;"><button type="button" class="swal2-close" aria-label="Close this dialog" style="display: none;">×</button></div>' + '<h5> تصویر با موفقیت ثبت شد</h5>')
        })
        .catch(error => {
          if (error.response) {
            for (const property in error.response.data) {
              this.errors.push(`${property}: ${error.response.data[property]}`)
            }
          } else if (error.message) {
            this.errors.push(error.message)
          }
        })
    },
    async submitaccept () {
      const formdata = new FormData()
      var img = document.getElementById('fileaccept').files[0]
      formdata.append('acceptimg', img, img.name)
      await axios
        .post('/verifyaccept', formdata)
        .then(response => {
          this.verify()
          this.$swal('<div class="swal2-header"><ul class="swal2-progress-steps" style="display: none;"></ul><div class="swal2-icon swal2-success swal2-icon-show" style="display: flex;"><div class="swal2-success-circular-line-left" style="background-color: rgb(255, 255, 255);"></div><span class="swal2-success-line-tip"></span> <span class="swal2-success-line-long"></span><div class="swal2-success-ring"></div> <div class="swal2-success-fix" style="background-color: rgb(255, 255, 255);"></div><div class="swal2-success-circular-line-right" style="background-color: rgb(255, 255, 255);"></div></div><img class="swal2-image" style="display: none;"><button type="button" class="swal2-close" aria-label="Close this dialog" style="display: none;">×</button></div>' + '<h5> تصویر با موفقیت ثبت شد</h5>')
        })
        .catch(error => {
          if (error.response) {
            for (const property in error.response.data) {
              var errors = [`${property}: ${error.response.data[property]}`]
              var error = '<div class="swal2-icon swal2-error swal2-icon-show" style="display: flex;"><span class="swal2-x-mark"><span class="swal2-x-mark-line-left"></span><span class="swal2-x-mark-line-right"></span></span></div><h5>'
              for (var er = 0; er < errors.length; er++) {
                error += '\n' + errors
              }
              error += '</h5>'
              this.$swal(error)
            }
          } else if (error.message) {
            var errors = [error.message]
            var error = '<div class="swal2-icon swal2-error swal2-icon-show" style="display: flex;"><span class="swal2-x-mark"><span class="swal2-x-mark-line-left"></span><span class="swal2-x-mark-line-right"></span></span></div><h5>'
            for (var er = 0; er < errors.length; er++) {
              error += '\n' + errors
            }
            error += '</h5>'
            this.$swal(error)
          }
        })
    },
    async submit () {
      await axios
        .post('/userinfo', { name: this.name, postal: this.postal, address: this.address, first_name: this.first_name, last_name: this.last_name})
        .then(response => {
          this.verify()
          this.$swal('<div class="swal2-header"><ul class="swal2-progress-steps" style="display: none;"></ul><div class="swal2-icon swal2-success swal2-icon-show" style="display: flex;"><div class="swal2-success-circular-line-left" style="background-color: rgb(255, 255, 255);"></div><span class="swal2-success-line-tip"></span> <span class="swal2-success-line-long"></span><div class="swal2-success-ring"></div> <div class="swal2-success-fix" style="background-color: rgb(255, 255, 255);"></div><div class="swal2-success-circular-line-right" style="background-color: rgb(255, 255, 255);"></div></div><img class="swal2-image" style="display: none;"><button type="button" class="swal2-close" aria-label="Close this dialog" style="display: none;">×</button></div>' + '<h5> کد با موفقیت تایید شد</h5>')
        })
    },
    async addphone () {
      await axios
        .post('/addphone', { phonenum : this.phonenum})
        .then(response => {
          this.get_user()
          this.$swal('<div class="swal2-header"><ul class="swal2-progress-steps" style="display: none;"></ul><div class="swal2-icon swal2-success swal2-icon-show" style="display: flex;"><div class="swal2-success-circular-line-left" style="background-color: rgb(255, 255, 255);"></div><span class="swal2-success-line-tip"></span> <span class="swal2-success-line-long"></span><div class="swal2-success-ring"></div> <div class="swal2-success-fix" style="background-color: rgb(255, 255, 255);"></div><div class="swal2-success-circular-line-right" style="background-color: rgb(255, 255, 255);"></div></div><img class="swal2-image" style="display: none;"><button type="button" class="swal2-close" aria-label="Close this dialog" style="display: none;">×</button></div>' + '<h5> تلفن با موفقیت تایید شد</h5>')
        })
    },










    checkback () {
      if (this.cardnumber !== '') {
        this.cardnumber = parseInt(String(this.cardnumber).replace('-', '').replace('-', '').replace('-', ''))
      }
    },
    checknum () {
      if (String(this.cardnumber).length < 16) {
        this.errors2.push('1')
        document.querySelector('.cardnum').className += ' is-invalid'
        this.ctool = 'شماره کارت باید ۱۶ رقم باشد'
      } else {
        this.errors2 = []
        document.querySelector('.cardnum').className = document.querySelector('.cardnum').className.replace(' is-invalid', '')
        this.ctool = ''
        this.cardnumber = this.cardnumber.slice(0, 4) + '-' + this.cardnumber.slice(4, 8) + '-' + this.cardnumber.slice(8, 12) + '-' + this.cardnumber.slice(12, 16)
      }
    },
    checknum2 () {
      if (String(this.cardnumber).length === 16) {
        var card = String(this.cardnumber)
        this.cardnumber = card.slice(0, 4) + '-' + card.slice(4, 8) + '-' + card.slice(8, 12) + '-' + card.slice(12, 16)
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
            this.options.push([result, itemm.image])
          }
        })
    },
    async geta () {
      var itemm
      await axios
        .get('/bankaccounts')
        .then(response => {
          for (itemm of response.data) {
            var result = itemm.number
            this.accounts.push([result])
          }
        })
    },
    async submitcard () {
      this.errors = []
      this.errors2 = []
      if (this.amount === 0) {
        this.errors.push('لطفا مبلغ را وارد کنید')
      }
      if (!this.cardnumber) {
        this.errors.push('لطفا کارتی را انتخاب کنید')
      }
      var card = (this.cardnumber.replace('-', '').replace('-', '').replace('-', ''))
      const formdata = new FormData()
      formdata.append('bankc', card)
      await axios
        .post('/bankcards', formdata)
        .then(response => {
          this.submitaccount()
        })
        .catch(error => {
          if (error.response) {
            for (const property in error.response.data) {
              this.errors.push(`${property}: ${error.response.data[property]}`)
            }
          } else if (error.message) {
            this.errors.push(error.message)
          }
        })
    },
    async submitaccount () {
      this.errors = []
      this.errors2 = []
      var card = this.accountnumber
      var sheba = this.shebanumber
      await axios
        .post('/bankaccounts', { bankc: card , shebac: sheba })
        .then(response => {
          this.$swal('<div class="swal2-header"><ul class="swal2-progress-steps" style="display: none;"></ul><div class="swal2-icon swal2-success swal2-icon-show" style="display: flex;"><div class="swal2-success-circular-line-left" style="background-color: rgb(255, 255, 255);"></div><span class="swal2-success-line-tip"></span> <span class="swal2-success-line-long"></span><div class="swal2-success-ring"></div> <div class="swal2-success-fix" style="background-color: rgb(255, 255, 255);"></div><div class="swal2-success-circular-line-right" style="background-color: rgb(255, 255, 255);"></div></div><img class="swal2-image" style="display: none;"><button type="button" class="swal2-close" aria-label="Close this dialog" style="display: none;">×</button></div>' + '<h5> حساب با موفقیت ثبت شد</h5>')
        })
        .catch(error => {
          if (error.response) {
            for (const property in error.response.data) {
              this.errors.push(`${property}: ${error.response.data[property]}`)
            }
          } else if (error.message) {
            this.errors.push(error.message)
          }
        })
    },
    acard () {
      document.getElementById('aaddcard').hidden = true
      document.getElementById('addcard').hidden = false
    },
    aaccount () {
      document.getElementById('aaddaccount').hidden = true
      document.getElementById('addaccount').hidden = false
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
