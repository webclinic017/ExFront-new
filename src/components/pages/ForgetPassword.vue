<template>
  <div>
    <!-- Header -->
    <div class="header bg-gradient-success py-7 py-lg-8 pt-lg-9">
      <b-container>
        <div class="header-body text-center mb-7">
          <b-row class="justify-content-center">
          </b-row>
        </div>
      </b-container>
      <div class="separator separator-bottom separator-skew zindex-100">
        <svg x="0" y="0" viewBox="0 0 2560 100" preserveAspectRatio="none" version="1.1"
             xmlns="http://www.w3.org/2000/svg">
          <polygon class="fill-default" points="2560 0 2560 100 0 100"></polygon>
        </svg>
      </div>
    </div>
    <!-- Page content -->
    <b-container class="mt--9 pb-5" style="margin-top:-200px!important">
      <b-row class="justify-content-center">
        <b-col lg="5" md="7">
          <b-card no-body class="border-0 mb-0">
            <b-card-header class="bg-transparent pb-5"  ><br>
              <h2 style="text-align:center;width:100%;color:#888">بازیابی کلمه عبور</h2>
            </b-card-header>
            <b-card-body class="px-lg-5 py-lg-5">
              <div class="text-center text-muted mb-4">
              </div>
                  <form class="my-5">
        <b-form-group label="ایمیل :">
          <b-input v-model="Email" />
        </b-form-group>

        <div class="d-flex justify-content-between align-items-center m-0">
          <b-btn variant="dark" @click="submitForm"> ارسال لینک تغییر رمز</b-btn>
        </div>
      </form>
            </b-card-body>
          </b-card>
          <b-row class="mt-3">
            <b-col cols="6">
            </b-col>
            <b-col cols="6" class="text-right">
            <router-link style="color:#dcdcdc;float:left" to="/register"> ثبت نام کنید</router-link>
            </b-col>
          </b-row>
        </b-col>
      </b-row>
    </b-container>
    <footer style="height:100px">

    </footer>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'pages-authentication-login-v1',
  metaInfo: {
    title: 'Login v1 - Pages'
  },
  data: () => ({
    Email: '',
    msg: []
  }),
  mounted () {
    document.title = 'Log In | Exchange'
  },
  methods: {
    async  submitForm () {
      this.msg = []
      if (!this.Email) {
        this.msg.push('ایمیل را وارد کنید')
      }
      if (!this.msg.length) {
        const formData = {
          email: this.Email
        }
        await axios
          .post('/password_reset/', formData)
          .then(response => {
            this.$swal('<div class="swal2-header"><ul class="swal2-progress-steps" style="display: none;"></ul><div class="swal2-icon swal2-success swal2-icon-show" style="display: flex;"><div class="swal2-success-circular-line-left" style="background-color: rgb(255, 255, 255);"></div><span class="swal2-success-line-tip"></span> <span class="swal2-success-line-long"></span><div class="swal2-success-ring"></div> <div class="swal2-success-fix" style="background-color: rgb(255, 255, 255);"></div><div class="swal2-success-circular-line-right" style="background-color: rgb(255, 255, 255);"></div></div><img class="swal2-image" style="display: none;"><button type="button" class="swal2-close" aria-label="Close this dialog" style="display: none;">×</button></div>' + '<h5>با موفقیت به ایمیل شما ارسال شد.</h5>')
          })
          .catch(error => {
            this.$swal('<div class="swal2-icon swal2-error swal2-icon-show" style="display: flex;"><span class="swal2-x-mark"><span class="swal2-x-mark-line-left"></span><span class="swal2-x-mark-line-right"></span></span></div><h5>کاربری با ایمیل وارد شده موجود نیست</h5>')
            this.msg.push(error.response.data.error)
          })
      }
    }
  }
}
</script>
