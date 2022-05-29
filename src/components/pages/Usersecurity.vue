<template>
  <div>

    <b-tabs class="nav-tabs-top nav-responsive-sm">
      <b-tab title="امنیت کاربری" active>
        <b-card-body>

        </b-card-body>
        <h3>ورود چند عاملی</h3>
        <hr class="border-light m-0">
        <b-card-body class="pb-2">
          <hr>
           <input type="checkbox" id="sms" v-if="details.smsverify" variant="dark" style="float:right" checked>
           <input type="checkbox" id="sms" v-if="!details.smsverify" variant="dark" style="float:right">   ورود چند عاملی (اس ام اس)
           <div class="clear"></div>
          <hr>
                  <img v-if="details.get_otp" id="qr" :src="'https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=' + details.get_otp"><br>

          <br>
           <input disabled id="google" type="checkbox" v-if="details.googleverify" variant="dark" style="float:right" checked>
           <input disabled id="google" type="checkbox" v-if="!details.googleverify" variant="dark" style="float:right">   ورود چند عاملی (گوگل)
           <div class="clear"></div>
          <hr>
           <input disabled id="email" type="checkbox" v-if="details.emailverify" variant="dark" style="float:right" checked>
           <input disabled id="email" type="checkbox" v-if="!details.emailverify" variant="dark" style="float:right">   ورود چند عاملی (ایمیل)
           <div class="clear"></div><br><br>
           <button @click="submit()" class="btn btn-dark">ثبت</button>
        </b-card-body><br><br>
        <b-card-body class="pb-2">

        </b-card-body>
        <div class="table-responsive">
        </div>
      </b-tab>
    </b-tabs>

    <div class="text-right mt-3">
    </div>

    <h4 class="d-flex flex-wrap justify-content-between align-items-center pt-3 mb-4">
      <div class="col-12 col-md-3 p-0 ">
      </div>
    </h4>
      </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'pages-user-edit',
  metaInfo: {
    title: 'User edit - Pages'
  },
  data: () => ({
    timer: null, 
    buttonText : 'Poll for order payment status',
    timerNum: 60 ,
    disabled: false,
    details: [],
    code: ''
  }),
  mounted () {
    this.get_general()
  },
  beforeCreate () {
    this.$store.commit('initializeStore')
    const token = this.$store.state.token
    if (token) {
      axios.defaults.headers.common.Authorization = 'Token ' + token
      this.$store.state.isAuthenticated = true
    } else {
      axios.defaults.headers.common.Authorization = ''
    }
  },
  
  methods: {
    async get_general () {
      await axios
        .get('/userinfo')
        .then(response => {
          this.details = response.data[0] 
        })
        .catch(error => {
        })
    },
    async submit(){
      var sms = this.details.smsverify
      var google = this.details.googleverify
      var email = this.details.emailverify
      if(document.querySelector('#sms').checked){
        sms = true
      }else{
        sms = false
      }
      if(document.querySelector('#google').checked){
        google = true
      }else{
        google = false
      }
      if(document.querySelector('#email').checked){
        email = true
      }else{
        email = false
      }
      await axios
      .put('/userinfo' , {smsverify: sms, googleverify: google, emailverify: email} )
        .then(response => {
          this.$swal('<div class="swal2-header"><ul class="swal2-progress-steps" style="display: none;"></ul><div class="swal2-icon swal2-success swal2-icon-show" style="display: flex;"><div class="swal2-success-circular-line-left" style="background-color: rgb(255, 255, 255);"></div><span class="swal2-success-line-tip"></span> <span class="swal2-success-line-long"></span><div class="swal2-success-ring"></div> <div class="swal2-success-fix" style="background-color: rgb(255, 255, 255);"></div><div class="swal2-success-circular-line-right" style="background-color: rgb(255, 255, 255);"></div></div><img class="swal2-image" style="display: none;"><button type="button" class="swal2-close" aria-label="Close this dialog" style="display: none;">×</button></div>' + '<h5>  با موفقیت انجام شد</h5>')
        })
        .catch(error => {
        })
    }
  }
}
</script>
<style>
.invalid-tooltip{
  position: relative;
  top:0;
  background-color: rgba(0, 0, 0, 0);
  color: red;
  text-align: left;
}
.input-icons i {
left:7%;
position: absolute;
}
.input-icons {
width: 100%;
margin-bottom: 10px;
}
.icon {
padding: 10px;
min-width: 40px;
}
.input-field {
width: 100%;
padding: 10px;
text-align: center;
}
label{
  width:15%;
}
.input-field{
  width: 85%;
  float: left;
}
.clear{
  clear: both;
}
</style>
