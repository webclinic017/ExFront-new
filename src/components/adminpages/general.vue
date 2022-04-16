<template>
  <div>
    <h4 class="font-weight-bold py-3 mb-4">
      اطلاعات سایت  <span class="text-muted"></span>
    </h4>

    <b-tabs class="nav-tabs-top nav-responsive-sm">
      <b-tab title="اطلاعات کاربری" active>
        <b-card-body>

        </b-card-body>
        <hr class="border-light m-0">
        <b-card-body class="pb-2">
          <div class="input-icons">
          <b-form-group >
            <label style="width:15%">نام سایت</label>
            <b-input style="width:85%; float:left" v-model="name" class="mb-1 input-field" />
            <div class="clear"></div>
          </b-form-group>
          <b-form-group >
            <label> آدرس ایمیل</label>
            <b-input v-model="email" class="mb-1 input-field" />
            <div class="clear"></div>
          </b-form-group>

          <b-form-group >
            <label for="">آدرس تلگرام</label>
            <b-input v-model="telegram" class="input-field"/>
            <div class="clear"></div>
          </b-form-group>

          <b-form-group label="">
            <label for="">آدرس اینستاگرام </label>
            <b-input v-model="instagram"  class="input-field"/>
            <div class="clear"></div>
          </b-form-group>

          <b-form-group label="">
            <label for="">شماره واتس اپ</label>
            <b-input v-model="whatsapp" maxlength="10" placeholder="*********9" @input="ptoe()" class="mb-1 input-field" />
            <div class="clear"></div>
          </b-form-group>

          <b-form-group label="">
            <label for="">شماره تماس</label>
            <b-input v-model="telephone" maxlength="11" placeholder="*********9" @input="ptoe()" class="mb-1 input-field" />
            <div class="clear"></div>
          </b-form-group>

          <b-form-group label="">
            <label for=""> لوگو</label>
            <input type="file" id="file" @input="ptoe()" class="mb-1 input-field">
            <div class="clear"></div>
          </b-form-group>
          </div>
           <b-btn variant="dark" style="float:left" @click="submit()">ثبت اطلاعات</b-btn>
           <div class="clear"></div>
        </b-card-body><br><br>
        <b-card-body class="pb-2">

        </b-card-body>
        <div class="table-responsive">
        </div>
      </b-tab>
      <b-tab title="مقررات">
        <b-card-body>

        </b-card-body>
        <hr class="border-light m-0">
        <b-card-body class="pb-2">

          <b-form-group  label="">
            <label for=""> قوانین و مقررات </label>
            <b-textarea v-model="rule" class="mb-1 optool" ></b-textarea>
            <div class="clear"></div>
          </b-form-group>

        <b-btn variant="success" style="float:left" @click="submitrule()">ثبت قوانین</b-btn> <br><br>
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
    file: '',
    email: '',
    errors: [],
    errors2: [],
    ctool: '',
    opass: '',
    pass: '',
    rpass: '',
    cerrors: [],
    name: '',
    mobile: '',
    ptool: '',
    optool: '',
    rptool: '',
    telegram: '',
    instagram: '',
    whatsapp: '',
    telephone: '',
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
    async get_general () {
      await axios
        .get('adminpanel/general')
        .then(response => {
          response = response.data[0]
          this.name = response['name']
          this.email = response['email']
          this.telegram = response['telegram']
          this.instagram = response['instagram']
          this.whatsapp = response['whatsapp']
          this.telephone = response['telephone']
          this.rule = response['rule']
        })
        .catch(error => {
        })
    },
    async submit () {
      this.errors = []
      const formData = {
        logo : document.getElementById('file').files[0],
        name: this.name,
        email: this.email,
        mobile: this.mobile,
        whatsapp: this.whatsapp,
        telegram: this.telegram,
        instagram: this.instagram,
        telephone: this.telephone,
      }
      await axios
        .post('adminpanel/general', formData)
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
    async submitrule () {
      const formData = {
        rule: this.rule,
      }
      await axios
        .post('adminpanel/general', formData)
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
