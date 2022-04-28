<template>
  <div>

    <!-- Page content -->
    <b-container class="" style="margin: 20px">
      <!-- Table -->
      <b-row class="justify-content-center">
        <b-col lg="6" md="8" >
          <b-card no-body class=" border-0">
            <b-card-header class="bg-transparent pb-5"><br>
              <h2 style="text-align:center;width:100%;color:#888">ثبت نام</h2>
            </b-card-header>
            <b-card-body class="px-lg-5 py-lg-5">
              <Vcode style="direction:ltr" :show="isShow" @success="onSuccess" @close="onClose" successText="با موفقیت تایید شد" failText="موفق نشدید لطفا مجددا تلاش نمایید" sliderText="لطفا پازل را کامل نمایید" />
              <form class="my-1">
        <b-form-group label="ایمیل">
          <input v-model="email" class="form-control email"/>
          <div class="invalid-tooltip">{{etool}}</div>
        </b-form-group>
        <b-form-group>
          <div slot="label" class="d-flex justify-content-between align-items-end">
            <div>کلمه عبور</div>
          </div>
          <input type="password" v-model="password" class="form-control pass" />
          <div class="invalid-tooltip">{{ptool}}</div>
          <p style="font-size:10px;margin:0">برای امنیت بیشتر توصیه میشود از سمبل ها استفاده کنید (#,@,&,...)</p>
        </b-form-group>
        <b-form-group>
          <div slot="label" class="d-flex justify-content-between align-items-end">
            <div>تکرار کلمه عبور</div>
          </div>
          <input type="password" v-model="repassword" class="form-control repass"/>
          <div class="invalid-tooltip">{{reptool}}</div>
        </b-form-group>

        <div class="d-flex justify-content-between align-items-center m-0">
          <b-card><input type="checkbox" @input="checked()"> من بیش از ۱۸ سال سن دارم</b-card>
          
          <button class="btn btn-dark" type="button" id="submit" disabled  @click="submit()">ثبت نام</button>
        </div>
      </form>
            </b-card-body>
          </b-card>
          <b-row class="mt-3">
            <router-link style="color:#dcdcdc;text-align:center;width:100%" to="/login">وارد شوید</router-link>
          </b-row>
        </b-col>
      </b-row>
    </b-container>
    <footer style="height:100px">

    </footer>
  </div>
</template>
<script>
import Vcode from "vue-puzzle-vcode";
import axios from 'axios'
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
    email: '',
    etool: '',
    utool: '',
    password: '',
    ptool: '',
    repassword: '',
    reptool: '',
    isShow: false
  }),
  mounted () {
    document.title = 'Log In | Exchange'
  },
  methods: {
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
    async sendmail() {
      await axios
          .post('/regemailverify/', {username:this.email.toLowerCase()})
          .then(response => {
            this.sendmail()
            this.$swal('<div class="swal2-header"><ul class="swal2-progress-steps" style="display: none;"></ul><div class="swal2-icon swal2-success swal2-icon-show" style="display: flex;"><div class="swal2-success-circular-line-left" style="background-color: rgb(255, 255, 255);"></div><span class="swal2-success-line-tip"></span> <span class="swal2-success-line-long"></span><div class="swal2-success-ring"></div> <div class="swal2-success-fix" style="background-color: rgb(255, 255, 255);"></div><div class="swal2-success-circular-line-right" style="background-color: rgb(255, 255, 255);"></div></div><img class="swal2-image" style="display: none;"><button type="button" class="swal2-close" aria-label="Close this dialog" style="display: none;">×</button></div>' + '<h5>ثبت نام شما با موفقیت انجام شد . لطفا برای تایید حساب ایمیل خود را چک کنید</h5>')
          })
    },
    checked() {
      document.querySelector('#submit').disabled = !document.querySelector('#submit').disabled
    },
    async  submitForm () {
      this.errors = []
      this.errors2 = []
      this.utool = ''
      this.ptool = ''
      this.reptool = ''
      this.etool = ''
      document.querySelector('.pass').className = document.querySelector('.pass').className.replace(' is-invalid', '')
      document.querySelector('.repass').className = document.querySelector('.repass').className.replace(' is-invalid', '')
      document.querySelector('.email').className = document.querySelector('.email').className.replace(' is-invalid', '')
      axios.defaults.headers.common.Authorization = ''
      localStorage.removeItem('token')
      this.$store.commit('removeToken')
      if (this.password === '') {
        document.querySelector('.pass').className += ' is-invalid'
        this.errors2.push('1')
        this.ptool = ' کلمه عبور را وارد نکرده اید'
      }
      if (this.email === '') {
        this.errors2.push('1')
        document.querySelector('.email').className += ' is-invalid'
        this.etool = ' ایمیل را وارد نکرده اید'
      } else {
        var x = this.email
        var atposition = x.indexOf('@')
        var dotposition = x.lastIndexOf('.')
        if (atposition < 1 || dotposition < atposition + 2 || dotposition + 2 >= x.length) {
          this.errors2.push('1')
          document.querySelector('.email').className += ' is-invalid'
          this.etool = 'فرمت ایمیل اشتباه است'
        } else {
          var horoof = /[\u0600-\u06FF]/
          if (horoof.test(this.username)) {
            this.errors2.push('1')
            document.querySelector('.username').className += ' is-invalid'
            this.utool = 'ایمیل نمیتواند فارسی باشد'
          }
        }
      }
      if (this.repassword === '') {
        this.errors2.push('1')
        document.querySelector('.repass').className += ' is-invalid'
        this.reptool = ' تکرار کلمه عبور را وارد نکرده اید'
      }
      if (this.password !== '' && this.repassword !== '' && this.password !== this.repassword) {
        this.errors2.push('1')
        document.querySelector('.pass').className += ' is-invalid'
        document.querySelector('.repass').className += ' is-invalid'
        this.ptool = ' کلمه عبور با تکرار یکسان نیست'
        this.reptool = ' کلمه عبور با تکرار یکسان نیست'
      }
      if (this.errors2.length === 0) {
        const formData = {
          username: this.email.toLowerCase(),
          email: this.email.toLowerCase(),
          password: this.password
        }
        await axios
          .post('/users/', formData)
          .then(response => {
            this.sendmail()
            setTimeout(() => {
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
                this.errors.push(' کلمه عبور باید بیش از ۸ کاراکتر باشد ترکیبی از حروف و اعداد باشد و نمیتواند مشابه نام کاربری باشد')
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
