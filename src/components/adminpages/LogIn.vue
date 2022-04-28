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
              <h2 style="text-align:center;width:100%;color:#888">ورود</h2>
            </b-card-header>
            <b-card-body class="px-lg-5 py-lg-5">
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
          <b-btn variant="dark" @click="submitForm">ورود</b-btn>
        </div>
      </form>
            </b-card-body>
          </b-card>
          <b-row class="mt-3">
            <b-col cols="6">
            <router-link style="color:#dcdcdc;float:left" to="/forgetpassword" class="d-block small">رمز عبور خود را فراموش کرده اید ؟</router-link>
            </b-col>
            <b-col cols="6" class="text-right">
            <router-link style="color:#dcdcdc;float:left" to="/register"> ثبت نام کنید</router-link>
            </b-col>
          </b-row>
        </b-col>
      </b-row>
    </b-container>
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
    errors: [],
    errors2: [],
    ptool: '',
    utool: '',
    username: '',
    password: ''
  }),
  mounted () {
    document.title = ' AMIZAS Exchange | ورود '
  },
  methods: {
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
        const formData = {
          username: this.username.toLowerCase(),
          password: this.password
        }
        await axios
          .post('/token/login', formData)
          .then(response => {
            const token = response.data.auth_token
            this.$store.commit('setToken', token)
            axios.defaults.headers.common.Authorization = 'Token ' + token
            this.$store.state.isAuthenticated = true
            localStorage.setItem('token', token)
            const toPath = this.$route.go || '/adminpanel'
            this.$router.push(toPath)
          })
          .catch(error => {
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
