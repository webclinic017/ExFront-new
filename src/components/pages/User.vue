<template>
  <div>
    <h4 class="font-weight-bold py-3 mb-4">
      اطلاعات کاربری  <span class="text-muted"> {{username}}</span>
    </h4>

    <b-tabs class="nav-tabs-top nav-responsive-sm">
      <b-tab title="اطلاعات کاربری" active>
        <b-card-body>

        </b-card-body>
        <hr class="border-light m-0">
        <b-card-body class="pb-2">
          <div class="input-icons">
          <b-form-group >
            <label style="width:15%">نام کاربری</label>
             <i class="fas fa-check-circle icon"></i>
            <b-input style="width:85%; float:left" :readonly="true" v-model="username" class="mb-1 input-field" />
            <div class="clear"></div>
          </b-form-group>
          <b-form-group >
            <label> آدرس ایمیل</label>
             <i v-if="verify.email" class="fas fa-check-circle icon"></i>
            <b-input :readonly="true" v-model="email" class="mb-1 input-field" />
            <div class="clear"></div>
          </b-form-group>

          <b-form-group >
            <label for="">نام</label>
             <i v-if="verify.melli" class="fas fa-check-circle icon"></i>
            <b-input v-model="firstname" class="input-field"/>
            <div class="clear"></div>
          </b-form-group>

          <b-form-group label="">
            <label for="">نام خانوادگی</label>
             <i v-if="verify.melli" class="fas fa-check-circle icon"></i>
            <b-input v-model="lastname"  class="input-field"/>
            <div class="clear"></div>
          </b-form-group>

          <b-form-group label="">
            <label for="">شماره همراه</label>
             <i v-if="verify.mobile" class="fas fa-check-circle icon"></i>
            <b-input v-model="mobile" maxlength="10" placeholder="*********9" @input="ptoe()" class="mb-1 input-field" />
            <div class="clear"></div>
          </b-form-group>
          </div>
           <b-btn variant="dark" style="float:left" @click="submit()">ثبت اطلاعات کاربری</b-btn>
           <div class="clear"></div>
        </b-card-body><br><br>
        <b-card-body class="pb-2">

        </b-card-body>
        <div class="table-responsive">
        </div>
      </b-tab>
      <b-tab title="تغییر کلمه عبور">
        <b-card-body>

        </b-card-body>
        <hr class="border-light m-0">
        <b-card-body class="pb-2">

          <b-form-group  label="">
            <label for="">کلمه عبور قبلی</label>
            <b-input v-model="opass" type="password" class="mb-1 optool" />
            <div class="invalid-tooltip">{{optool}}</div>
            <div class="clear"></div>
          </b-form-group>
          <b-form-group  label="">
            <label for="">کلمه عبور جدید</label>
            <b-input v-model="pass" type="password" class="mb-1 ptool" />
            <div class="invalid-tooltip">{{ptool}}</div>
            <div class="clear"></div>
          </b-form-group>

          <b-form-group  label="">
            <label for="">تکرار کلمه عبور</label>
            <b-input type="password" v-model="rpass" class="rptool" />
            <div class="invalid-tooltip">{{rptool}}</div>
            <div class="clear"></div>
          </b-form-group>

        <b-btn variant="success" style="float:left" @click="submitpass()">تغییر کلمه عبور</b-btn> <br><br>
        </b-card-body>
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
    <b-card >
      <table class="table col-12">
      <tr>
        <h4 class="th" colspan="2">  کارت های بانکی شما</h4>
        <hr>
      </tr>
      <tr  v-for="card in options" v-bind:key="card[0]">
      <td style="width:50%" class="left"><img :src="`http://127.0.0.1:8000${card[1]}`" alt="" style="width:30%;float:right"></td>
      <td style="width:50%" colspan="6" class="left">{{card[0]}}</td>
      <div style="clear:both"></div>
      <hr>
      </tr>
      </table>
    </b-card><br>
        <button @click="acard()" id="aaddcard" class="btn btn-success">اضافه کردن کارت بانکی جدید</button><br><br><br><br>
        <b-card id="addcard" hidden header="اضافه کردن کارت بانکی" header-tag="h6" class="mb-4">
      <fieldset  class="demo-vertical-spacing-sm">
        <b-form-group label="شماره کارت بانکی">
          <b-input maxlength="16" minlength="16" type="tel" class="cardnum" v-model="cardnumber" @change="checknum()" @focusout="checknum2()" @focus="checkback()" placeholder="شماره کارت بانکی" />
          <div class="invalid-tooltip">{{ctool}}</div>
          </b-form-group>
          <b-form-group label="عکس کارت بانکی">
          <input type="file" id="file" class="btn btn-success">
        </b-form-group>
        <b-btn @click="csubmit()" variant="dark"> اضافه کردن کارت </b-btn>
      </fieldset>
    </b-card><br><br>
    <b-card >
      <table class="table col-12">
        <h4 class="th" colspan="2">  حساب های بانکی شما</h4>
        <hr>
      <tr  v-for="card in accounts" v-bind:key="card[0]">
      <td style="width:50%" class="left"><img :src="`http://127.0.0.1:8000${card[1]}`" alt="" style="width:30%;float:right"></td>
      <td style="width:50%" colspan="6" class="left">{{card[0]}}</td>
      <div style="clear:both"></div>
      <hr>
      </tr>
      </table>
    </b-card><br><br>
    <button @click="aaccount()" class="btn btn-success" id="aaddaccount">اضافه کردن حساب بانکی جدید</button>
        <b-card id="addaccount" hidden header="اضافه کردن حساب بانکی" header-tag="h6" class="mb-4">
      <fieldset  class="demo-vertical-spacing-sm">
        <b-form-group label="شماره حساب بانکی">
          <b-input maxlength="16" minlength="16" type="tel" class="cardnum" v-model="accountnumber" placeholder="شماره حساب بانکی" />
          <div class="invalid-tooltip">{{ctool}}</div>
          </b-form-group>
        <b-btn @click="submitaccount()" variant="dark"> اضافه کردن حساب بانکی </b-btn>
      </fieldset>
    </b-card><br><br>
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
    options: [],
    accounts: [],
    file: '',
    email: '',
    cardnumber: '',
    accountnumber: '',
    errors: [],
    errors2: [],
    ctool: '',
    opass: '',
    pass: '',
    rpass: '',
    cerrors: [],
    username: '',
    firstname: '',
    lastname: '',
    mobile: '',
    ptool: '',
    optool: '',
    rptool: '',
    verify: {
      mobile: false,
      email: false,
      melli: false,
      bank: false
    }
  }),
  mounted () {
    this.checklevel()
    this.get_user()
    this.check()
    this.getc()
    this.geta()
    this.verified()
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
    async verified () {
      await axios
        .get('/verify')
        .then(response => {
          const data = response.data[0]
          this.verify.mobile = data.mobilev
          this.verify.email = data.emailv
          this.verify.melli = data.melliv
          this.verify.bank = data.bankv
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
    async csubmit () {
      this.cerrors = []
      this.errors2 = []
      if (this.amount === 0) {
        this.cerrors.push('لطفا مبلغ را وارد کنید')
      }
      if (!this.cardnumber) {
        this.cerrors.push('لطفا کارتی را انتخاب کنید')
      }
      var card = parseInt(this.cardnumber.replace('-', '').replace('-', '').replace('-', ''))
      const formdata = new FormData()
      formdata.append('bankc', card)
      var img = document.getElementById('file').files[0]
      formdata.append('bankimg', img, img.name)
      await axios
        .post('/bankcards', formdata)
        .then(response => {

        })
        .catch(error => {
          if (error.response) {
            for (const property in error.response.data) {
              this.cerrors.push(`${property}: ${error.response.data[property]}`)
            }
          } else if (error.message) {
            this.cerrors.push(error.message)
          }
        })
    },
    async submitaccount () {
      this.cerrors = []
      this.errors2 = []
      var card = parseInt(this.accountnumber)
      await axios
        .post('/bankaccounts', { bankc: card })
        .then(response => {

        })
        .catch(error => {
          if (error.response) {
            for (const property in error.response.data) {
              this.cerrors.push(`${property}: ${error.response.data[property]}`)
            }
          } else if (error.message) {
            this.cerrors.push(error.message)
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
    async get_user () {
      await axios
        .get('/user')
        .then(response => {
          this.username = response.data[0].username
          this.email = response.data[0].email
        })
      await axios
        .get('/userinfo')
        .then(response => {
          this.firstname = response.data[0].first_name
          this.lastname = response.data[0].last_name
          this.mobile = response.data[0].mobile
        })
    },
    async submit () {
      this.errors = []
      const formData = {
        first_name: this.firstname,
        last_name: this.lastname,
        mobile: this.mobile
      }
      await axios
        .post('/userinfo', formData)
        .then(response => {
          this.$swal('<div class="swal2-header"><ul class="swal2-progress-steps" style="display: none;"></ul><div class="swal2-icon swal2-success swal2-icon-show" style="display: flex;"><div class="swal2-success-circular-line-left" style="background-color: rgb(255, 255, 255);"></div><span class="swal2-success-line-tip"></span> <span class="swal2-success-line-long"></span><div class="swal2-success-ring"></div> <div class="swal2-success-fix" style="background-color: rgb(255, 255, 255);"></div><div class="swal2-success-circular-line-right" style="background-color: rgb(255, 255, 255);"></div></div><img class="swal2-image" style="display: none;"><button type="button" class="swal2-close" aria-label="Close this dialog" style="display: none;">×</button></div>' + '<h5>ثبت اطاعات شما با موفقیت انجام شد . </h5>')
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
    ptoe () {
      this.mobile = this.mobile.replace('۱', '1').replace('۲', '2').replace('۳', '3').replace('۴', '4').replace('۵', '5').replace('۶', '6').replace('۷', '7').replace('۸', '8').replace('۹', '9').replace('۰', '0')
    },
    async submitpass () {
      document.querySelector('.ptool').className = document.querySelector('.ptool').className.replace(' is-invalid', '')
      document.querySelector('.optool').className = document.querySelector('.optool').className.replace(' is-invalid', '')
      document.querySelector('.rptool').className = document.querySelector('.rptool').className.replace(' is-invalid', '')

      this.errors = []
      if (this.pass.length < 8) {
        this.errors.push('کلمه عبور باید حداقل ۸ کاراکتر باشد')
        this.ptool = 'کلمه عبور باید حداقل ۸ کاراکتر باشد'
        document.querySelector('.ptool').className += ' is-invalid'
      }
      if (this.pass.length === 0) {
        this.errors.push('کلمه عبور را وارد کنید')
        this.ptool = 'کلمه عبور را وارد کنید'
        document.querySelector('.ptool').className += ' is-invalid'
      }
      if (this.rpass.length < 8) {
        this.errors.push('کلمه عبور باید حداقل ۸ کاراکتر باشد')
        this.rptool = 'کلمه عبور باید حداقل ۸ کاراکتر باشد'
        document.querySelector('.rptool').className += ' is-invalid'
      }
      if (this.rpass.length === 0) {
        this.errors.push('کلمه عبور را وارد کنید')
        this.rptool = 'کلمه عبور را وارد کنید'
        document.querySelector('.rptool').className += ' is-invalid'
      }
      if (this.opass.length < 8) {
        this.errors.push('کلمه عبور باید حداقل ۸ کاراکتر باشد')
        this.optool = 'کلمه عبور باید حداقل ۸ کاراکتر باشد'
        document.querySelector('.optool').className += ' is-invalid'
      }
      if (this.opass.length === 0) {
        this.errors.push('کلمه عبور را وارد کنید')
        this.optool = 'کلمه عبور را وارد کنید'
        document.querySelector('.optool').className += ' is-invalid'
      }
      const formData = {
        opassword: this.opass,
        password: this.pass,
        repassword: this.rpass
      }
      if (!this.errors.length) {
        await axios
          .post('/uresetpass', formData)
          .then(response => {
            this.$swal('<div class="swal2-header"><ul class="swal2-progress-steps" style="display: none;"></ul><div class="swal2-icon swal2-success swal2-icon-show" style="display: flex;"><div class="swal2-success-circular-line-left" style="background-color: rgb(255, 255, 255);"></div><span class="swal2-success-line-tip"></span> <span class="swal2-success-line-long"></span><div class="swal2-success-ring"></div> <div class="swal2-success-fix" style="background-color: rgb(255, 255, 255);"></div><div class="swal2-success-circular-line-right" style="background-color: rgb(255, 255, 255);"></div></div><img class="swal2-image" style="display: none;"><button type="button" class="swal2-close" aria-label="Close this dialog" style="display: none;">×</button></div>' + '<h5>تغییر کلمه عبور شما با موفقیت انجام شد . </h5>')
          })
          .catch(error => {
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(`${property}: ${error.response.data[property]}`)
              }
            } else if (error.error) {
              this.errors.push(error.error)
            }
          })
        if (this.errors.length) {
          var errors = this.errors
          var error = '<div class="swal2-icon swal2-error swal2-icon-show" style="display: flex;"><span class="swal2-x-mark"><span class="swal2-x-mark-line-left"></span><span class="swal2-x-mark-line-right"></span></span></div><h5>'
          for (var er = 0; er < errors.length; er++) {
            error += '\n' + errors
          }
          error += '</h5>'
          this.$swal(error)
        }
      }
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
