<template>
  <div class="authentication-wrapper authentication-1 px-4">
    <div class="authentication-inner py-5">

      <!-- Logo -->
      <div class="d-flex justify-content-center align-items-center">
        <div class="ui-w-60">
          <div class="w-100 position-relative" style="padding-bottom: 54%">
            <svg class="w-100 h-100 position-absolute" viewBox="0 0 148 80" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><defs><linearGradient id="a" x1="46.49" x2="62.46" y1="53.39" y2="48.2" gradientUnits="userSpaceOnUse"><stop stop-opacity=".25" offset="0"></stop><stop stop-opacity=".1" offset=".3"></stop><stop stop-opacity="0" offset=".9"></stop></linearGradient><linearGradient id="e" x1="76.9" x2="92.64" y1="26.38" y2="31.49" xlink:href="#a"></linearGradient><linearGradient id="d" x1="107.12" x2="122.74" y1="53.41" y2="48.33" xlink:href="#a"></linearGradient></defs><path class="fill-dark" transform="translate(-.1)" d="M121.36,0,104.42,45.08,88.71,3.28A5.09,5.09,0,0,0,83.93,0H64.27A5.09,5.09,0,0,0,59.5,3.28L43.79,45.08,26.85,0H.1L29.43,76.74A5.09,5.09,0,0,0,34.19,80H53.39a5.09,5.09,0,0,0,4.77-3.26L74.1,35l16,41.74A5.09,5.09,0,0,0,94.82,80h18.95a5.09,5.09,0,0,0,4.76-3.24L148.1,0Z"></path><path transform="translate(-.1)" d="M52.19,22.73l-8.4,22.35L56.51,78.94a5,5,0,0,0,1.64-2.19l7.34-19.2Z" fill="url(#a)"></path><path transform="translate(-.1)" d="M95.73,22l-7-18.69a5,5,0,0,0-1.64-2.21L74.1,35l8.33,21.79Z" fill="url(#e)"></path><path transform="translate(-.1)" d="M112.73,23l-8.31,22.12,12.66,33.7a5,5,0,0,0,1.45-2l7.3-18.93Z" fill="url(#d)"></path></svg>
          </div>
        </div>
      </div>
      <!-- / Logo -->
      <!-- Form -->
      <form class="my-5">
        <b-form-group label="موبایل">
          <input v-model="tel" class="form-control email"/>
          <div class="invalid-tooltip">{{etool}}</div>
        </b-form-group>
        <b-form-group>
          <div slot="label" class="d-flex justify-content-between align-items-end">
            <div>کلمه عبور</div>
          </div>
          <input type="password" v-model="password" class="form-control pass" />
          <div class="invalid-tooltip">{{ptool}}</div>
        </b-form-group>
        <b-form-group>
          <div slot="label" class="d-flex justify-content-between align-items-end">
            <div>تکرار کلمه عبور</div>
          </div>
          <input type="password" v-model="repassword" class="form-control repass"/>
          <div class="invalid-tooltip">{{reptool}}</div>
        </b-form-group>

        <div class="d-flex justify-content-between align-items-center m-0">
          <b-btn variant="dark" @click="submitForm">Sign In</b-btn>
        </div>
      </form>
      <!-- / Form -->

      <div class="text-center text-muted">
        قبلا ثبت نام کرده اید ؟ <router-link to="/login">وارد شوید</router-link>
      </div>

    </div>
  </div>
</template>

<!-- Page -->
<style src="@/vendor/styles/pages/authentication.scss" lang="scss"></style>

<script>
import axios from 'axios'
export default {
  name: 'pages-authentication-login-v1',
  metaInfo: {
    title: 'ورود'
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
    reptool: ''
  }),
  mounted () {
    document.title = 'ثبت نام | AMIZAS Exchange'
  },
  methods: {
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
            this.$swal('<div class="swal2-header"><ul class="swal2-progress-steps" style="display: none;"></ul><div class="swal2-icon swal2-success swal2-icon-show" style="display: flex;"><div class="swal2-success-circular-line-left" style="background-color: rgb(255, 255, 255);"></div><span class="swal2-success-line-tip"></span> <span class="swal2-success-line-long"></span><div class="swal2-success-ring"></div> <div class="swal2-success-fix" style="background-color: rgb(255, 255, 255);"></div><div class="swal2-success-circular-line-right" style="background-color: rgb(255, 255, 255);"></div></div><img class="swal2-image" style="display: none;"><button type="button" class="swal2-close" aria-label="Close this dialog" style="display: none;">×</button></div>' + '<h5>ثبت نام شما با موفقیت انجام شد . به صفحه ورود منتقل میشوید</h5>')
            setTimeout(() => {
              const toPath = this.$route.query.to || '/login'
              this.$router.push(toPath)
            }, 2000)
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
