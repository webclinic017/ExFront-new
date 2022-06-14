<template>
  <div>
    
    <!-- Header -->
    <b-container class="" >
      <b-row >
        <b-col >
          <b-card no-body class="border-0 mb-0">
            <b-card-header class="bg-transparent" style="border-style:none" ><br>
                <img src="/img/logo.png" style="width:10%;margin-left:45%;margin-right:40%; clear:both" alt="">             
            </b-card-header>
            <b-tabs>
            <b-tab title="ورود" style="padding:10% 0">
              <Vcode style="direction:ltr" :show="isShow" @success="onSuccess" @close="onClose" successText="با موفقیت تایید شد" failText="موفق نشدید لطفا مجددا تلاش نمایید" sliderText="لطفا پازل را کامل نمایید" />
              <div class="text-center text-muted mb-4">
              </div>
                <form class="my-1">
        <b-form-group label="نام کاربری">
          <input v-model="username" class="form-control username" />
          <div class="invalid-tooltip">{{utool}}</div>
        </b-form-group>
        <b-form-group>
          <div slot="label" class="d-flex justify-content-between align-items-end">
            <div>کلمه عبور</div>
          </div>
          <input type="password" v-model="password" class="form-control pass" />
          <div class="invalid-tooltip">{{ptool}}</div>
        </b-form-group>

        <div class="d-flex justify-content-between align-items-center m-0">
          <b-btn variant="dark" id="submit" @click="submit">ورود</b-btn>
        </div><br>
        <b-row style="width:105% ; margin-right:-3%">
            <b-col >
            <router-link style="color:#444;float:left" to="/forgetpassword" >رمز عبور خود را فراموش کرده اید ؟</router-link>
            </b-col>
            <b-col  class="text-right">
            <router-link style="color:#444;float:left" to="/register"> ثبت نام کنید</router-link>
            </b-col>
          </b-row>
      </form>
            </b-tab>

            <b-tab title="ثبت نام" style="padding:7% 0">
              <Vcode style="direction:ltr" :show="RisShow" @success="RonSuccess" @close="RonClose" successText="با موفقیت تایید شد" failText="موفق نشدید لطفا مجددا تلاش نمایید" sliderText="لطفا پازل را کامل نمایید" />
              <form class="my-1">
        <b-form-group label="ایمیل">
          <input v-model="Remail" class="form-control Remail"/>
          <div class="invalid-tooltip">{{Retool}}</div>
        </b-form-group>
        <b-form-group>
          <div slot="label" class="d-flex justify-content-between align-items-end">
            <div>کلمه عبور</div>
          </div>
          <input type="password" v-model="Rpassword" class="form-control Rpass" />
          <div class="invalid-tooltip">{{Rptool}}</div>
          <p style="font-size:10px;margin:0">برای امنیت بیشتر توصیه میشود از سمبل ها استفاده کنید (#,@,&,...)</p>
        </b-form-group>
        <b-form-group>
          <div slot="label" class="d-flex justify-content-between align-items-end">
            <div>تکرار کلمه عبور</div>
          </div>
          <input type="password" v-model="Rrepassword" class="form-control Rrepass"/>
          <div class="invalid-tooltip">{{Rreptool}}</div>
        </b-form-group>

        <div class="d-flex justify-content-between align-items-center m-0">
          <b-card><input type="checkbox" @input="Rchecked()"> من بیش از ۱۸ سال سن دارم</b-card>
          
          <button class="btn btn-dark" type="button" id="submit2" disabled  @click="Rsubmit()">ثبت نام</button>

         
        </div>
      </form><br>
       <b-row class="mt-3">
            <router-link style="color:#444;text-align:center;width:100%" to="/login">وارد شوید</router-link>
          </b-row>
            </b-tab>
            </b-tabs>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>
<script>
import axios from 'axios'
import Vcode from "vue-puzzle-vcode";
export default {
  name: 'pages-authentication-login-v1',
  metaInfo: {
    title: 'Login v1 - Pages'
  },
  components: {
  Vcode
  },
  data: () => ({
    errors: [],
    errors2: [],
    ptool: '',
    utool: '',
    username: '',
    password: '',
    isShow: false,
    Rerrors: [],
    Rerrors2: [],
    Remail: '',
    Retool: '',
    Rutool: '',
    Rpassword: '',
    Rptool: '',
    Rrepassword: '',
    Rreptool: '',
    RisShow: false
  }),
  mounted () {
    document.title = ' AMIZAS Exchange | ورود '
  },
  methods: {
    Rsubmit() {
      this.RisShow = true;
    },

    RonSuccess(msg) {
      this.RisShow = false; // 通过验证后，需要手动关闭模态框
      this.RsubmitForm()
    },
    RonClose() {
      this.RisShow = false;
    },
    async Rsendmail() {
      await axios
          .post('/regemailverify/', {username:this.Remail.toLowerCase()})
          .then(response => {
            this.Rsendmail()
            this.$swal('<div class="swal2-header"><ul class="swal2-progress-steps" style="display: none;"></ul><div class="swal2-icon swal2-success swal2-icon-show" style="display: flex;"><div class="swal2-success-circular-line-left" style="background-color: rgb(255, 255, 255);"></div><span class="swal2-success-line-tip"></span> <span class="swal2-success-line-long"></span><div class="swal2-success-ring"></div> <div class="swal2-success-fix" style="background-color: rgb(255, 255, 255);"></div><div class="swal2-success-circular-line-right" style="background-color: rgb(255, 255, 255);"></div></div><img class="swal2-image" style="display: none;"><button type="button" class="swal2-close" aria-label="Close this dialog" style="display: none;">×</button></div>' + '<h5>ثبت نام شما با موفقیت انجام شد . لطفا برای تایید حساب ایمیل خود را چک کنید</h5>')
          })
    },
    Rchecked() {
      document.querySelector('#submit2').disabled = !document.querySelector('#submit2').disabled
    },
    async  RsubmitForm () {
      this.Rerrors = []
      this.Rerrors2 = []
      this.Rutool = ''
      this.Rptool = ''
      this.Rreptool = ''
      this.Retool = ''
      document.querySelector('.Rpass').className = document.querySelector('.Rpass').className.replace(' is-invalid', '')
      document.querySelector('.Rrepass').className = document.querySelector('.Rrepass').className.replace(' is-invalid', '')
      document.querySelector('.Remail').className = document.querySelector('.Remail').className.replace(' is-invalid', '')
      axios.defaults.headers.common.Authorization = ''
      localStorage.removeItem('token')
      this.$store.commit('removeToken')
      if (this.Rpassword === '') {
        document.querySelector('.Rpass').className += ' is-invalid'
        this.Rerrors2.push('1')
        this.Rptool = ' کلمه عبور را وارد نکرده اید'
      }
      if (this.Remail === '') {
        this.Rerrors2.push('1')
        document.querySelector('.Remail').className += ' is-invalid'
        this.Retool = ' ایمیل را وارد نکرده اید'
      } else {
        var x = this.Remail
        var atposition = x.indexOf('@')
        var dotposition = x.lastIndexOf('.')
        if (atposition < 1 || dotposition < atposition + 2 || dotposition + 2 >= x.length) {
          this.Rerrors2.push('1')
          document.querySelector('.Remail').className += ' is-invalid'
          this.Retool = 'فرمت ایمیل اشتباه است'
        } else {
          var horoof = /[\u0600-\u06FF]/
          if (horoof.test(this.username)) {
            this.errors2.push('1')
            document.querySelector('.Rusername').className += ' is-invalid'
            this.Rutool = 'ایمیل نمیتواند فارسی باشد'
          }
        }
      }
      if (this.Rrepassword === '') {
        this.errors2.push('1')
        document.querySelector('.Rrepass').className += ' is-invalid'
        this.Rreptool = ' تکرار کلمه عبور را وارد نکرده اید'
      }
      if (this.Rpassword !== '' && this.Rrepassword !== '' && this.Rpassword !== this.Rrepassword) {
        this.errors2.push('1')
        document.querySelector('.Rpass').className += ' is-invalid'
        document.querySelector('.Rrepass').className += ' is-invalid'
        this.Rptool = ' کلمه عبور با تکرار یکسان نیست'
        this.Rreptool = ' کلمه عبور با تکرار یکسان نیست'
      }
      if (this.Rerrors2.length === 0) {
        const formData = {
          username: this.Remail.toLowerCase(),
          email: this.Remail.toLowerCase(),
          password: this.Rpassword
        }
        await axios
          .post('/users/', formData)
          .then(response => {
            this.sendmail()
            setTimeout(() => {
              this.$modal.hide('modal')
              const toPath = this.$route.query.to || '/login'
              this.$router.push(toPath)
            }, 2000)
          })
          .catch(error => {
            if (error.response) {
              for (const property in error.response.data) {
                if (property === 'username') {
                  this.errors.push('این ایمیل قبلا برای ثبت نام دیگری استفاده شده است')
                } else if(property === 'password'){
                this.Rerrors.push(' کلمه عبور باید بیش از ۸ کاراکتر باشد ترکیبی از حروف و اعداد باشد و نمیتواند مشابه نام کاربری باشد')
              } else {
                  this.Rerrors.push(`${property}: ${error.response.data[property]}`)
                }
              }
            } else if (error.message) {
              this.Rerrors.push(error.message)
            }
          })
      }
      if (this.Rerrors.length) {
        var errors = this.errors
        var error = '<div class="swal2-icon swal2-error swal2-icon-show" style="display: flex;"><span class="swal2-x-mark"><span class="swal2-x-mark-line-left"></span><span class="swal2-x-mark-line-right"></span></span></div><h5>'
        for (var er = 0; er < errors.length; er++) {
          error += '\n' + errors
        }
        error += '</h5>'
        this.$swal(error)
      }
    },












    async smscode () {
      await axios
        .post('/loginsms', {'username':this.username.toLowerCase(), code: parseInt(document.getElementById('code').value)})
        .then(response => {
          setTimeout(() => {
            this.submitForm()
          }, 1000);
        })
        .catch(response => {
          this.$swal(`<div class="swal2-icon swal2-error swal2-icon-show" style="display: flex;"><span class="swal2-x-mark"><span class="swal2-x-mark-line-left"></span><span class="swal2-x-mark-line-right"></span></span></div><h5>${response.data}</h5>‍‍`)
        })
    },
    submit() {
      this.isShow = true;
    },

    onSuccess(msg) {
      this.isShow = false; // 通过验证后，需要手动关闭模态框
      this.submitForm()
    },
    onClose() {
      this.isShow = false;
    },
    async  submitForm () {
      document.querySelector('.username').className = document.querySelector('.username').className.replace(' is-invalid', '')
      document.querySelector('.pass').className = document.querySelector('.pass').className.replace(' is-invalid', '')
      this.errors = []
      axios.defaults.headers.common.Authorization = ''
      localStorage.removeItem('token')
      this.$store.commit('removeToken')
      this.errors = []
      if (this.username === '') {
        this.errors2.push('1')
        document.querySelector('.username').className += ' is-invalid'
        this.utool = 'نام کاربری را وارد نکرده اید'
      }
      if (this.password === '') {
        this.errors2.push('1')
        document.querySelector('.pass').className += ' is-invalid'
        this.ptool = ' کلمه عبور را وارد نکرده اید'
      } else if (this.password.length < 8) {
        this.ptool = ' کلمه عبور باید حداقل ۸ کاراکتر باشد '
      }
      if (this.errors2.length === 0) {
         this.username = this.username.replace(' ' , '').replace(' ' , '').replace(' ' , '').replace(' ' , '')
        const formData = {
          username: this.username.toLowerCase(),
          password: this.password
        }
        this.$loading(true)
        await axios
          .post('/login', formData)
          .then(response => {
            if(response.data !== 1){
              this.$modal.hide('modal')
              this.$loading(false)
              const token = response.data.auth_token
              this.$store.commit('setToken', token)
              axios.defaults.headers.common.Authorization = 'Token ' + token
              this.$store.state.isAuthenticated = true
              localStorage.setItem('token', token)
              const toPath = this.$route.go || '/dashboard'
              this.$router.push(toPath)
            }
            else{
              this.$loading(false)
              this.$swal({
                html: '<h3 style="text-align:center">کد تایید ارسال شده </h3> <input autocomplete="off" type="number" class="form-control" id="code">',
                confirmButtonClass: 'btn btn-success btn-fill',
                buttonsStyling: false
              }).then( () => {
                this.smscode()
            })
            }
          })
          .catch(error => {
            this.$loading(false)
            if (error.response) {
              for (const property in error.response.data) {
                if (property === 'non_field_errors') {
                  this.errors.push('نام کاربری یا کلمه عبور اشتباه است')
                } else {
                  this.errors.push(`${property}: ${error.response.data[property]}`)
                }
              }
            } else if (error.message) {
              this.errors.push(error.message)
            }
          })
      }
      if (this.errors.length) {
        this.$loading(false)
        console.log(this.errors)
        var errors = this.errors
        var error = '<div class="swal2-icon swal2-error swal2-icon-show" style="display: flex;"><span class="swal2-x-mark"><span class="swal2-x-mark-line-left"></span><span class="swal2-x-mark-line-right"></span></span></div><h5>'
        for (var er = 0; er < errors.length; er++) {
          error += '\n' + errors[er]
        }
        error += '</h5>'
        this.$swal(error)
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
</style>
