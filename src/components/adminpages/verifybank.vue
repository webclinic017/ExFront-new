<template>
  <div>


      <b-card no-body class="col-12 d-none d-md-block"><br>
        <h3>کارت بانکی</h3>
        <hr>

        <b-card-header class="row no-gutters align-items-center" style="background:#efefef">
          <div class="col-2 cent">نام کاربری</div>
          <div class="col-2 cent">نام</div>
          <div class="col-2 cent">نام خانوادگی</div>
          <div class="col-3 font-weight-bold cent">شماره کارت</div>
          <div class="col-3 cent">عملیات</div>

        </b-card-header>

        <div v-for="section in requests" :key="section.title">
          <b-card-body class="py-3 wallets">

            <div class="row no-gutters align-items-center">
              <div class="col-2 cent">{{section.get_user}}</div>
              <div class="col-2 cent">{{section.get_first}}</div>
              <div class="col-2 cent">{{section.get_last}}</div>
              <div class="col-3 cent">{{section.bankc}}</div>
              <div class="col-3 cent"><button class="btnfont btn btn-danger" @click="reject(section.get_user , section.bankc , section.id)">رد درخواست</button><button class="btnfont btn btn-success" @click="accept(section.get_user , section.bankc, section.id, section.get_image)"> تایید درخواست</button></div>
            </div>

          </b-card-body>
        </div>
        <b-card-body v-if="!requests[0]" class="py-3 wallets">
            <h4 class="cent">درخواستی پیدا نشد</h4>
          </b-card-body>

      </b-card><br><br>


      <b-card no-body class="col-12 d-none d-md-block"><br>
        <h3>حساب بانکی</h3>
        <hr>

        <b-card-header class="row no-gutters align-items-center" style="background:#efefef">
          <div class="col-2 cent">نام کاربری</div>
          <div class="col-2 cent">نام</div>
          <div class="col-2 cent">نام خانوادگی</div>
          <div class="col-3 font-weight-bold cent">شماره حساب</div>
              <div class="col-3 cent">عملیات </div>

        </b-card-header>

        <div v-for="section in requests2" :key="section.title">
          <b-card-body class="py-3 wallets">

            <div class="row no-gutters align-items-center">
              <div class="col-2 cent">{{section.get_user}}</div>
              <div class="col-2 cent">{{section.get_first}}</div>
              <div class="col-2 cent">{{section.get_last}}</div>
              <div class="col-3 cent" style="font:12px 'arial'">IR{{section.shebac}} <hr style="margin:0"> {{section.bankc}}</div>
              <div class="col-3 cent"><button class="btnfont btn btn-danger" @click="areject(section.get_user , section.bankc , section.id, section.shebac)">رد درخواست</button><button class="btnfont btn btn-success" @click="aaccept(section.get_user , section.bankc, section.id, section.shebac)"> تایید درخواست</button></div>
            </div>

          </b-card-body>
        </div>
        <b-card-body v-if="!requests2[0]" class="py-3 wallets">
            <h4 class="cent">درخواستی پیدا نشد</h4>
          </b-card-body>

      </b-card>

  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'pages-forums-list',
  metaInfo: {
    title: 'کیف ها'
  },
  mounted () {
    this.getc()
    this.getac()
  },
  data: () => ({
    requests: [],
    requests2: []
  }),
  forumPath: [
    { text: 'کیف ها', active: true }
  ],
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
    async getac () {
      await axios
        .get('adminpanel/bankaccounts')
        .then(response => {
          this.requests2 = response.data
        })
    },
    async aaccept (user, num, id, shebac) {
      await axios
        .post('adminpanel/bankaccounts', { user: user, number: num, shebac: shebac, status: 'True', id: id })
        .then(response => {
          this.$swal('<div class="swal2-header"><ul class="swal2-progress-steps" style="display: none;"></ul><div class="swal2-icon swal2-success swal2-icon-show" style="display: flex;"><div class="swal2-success-circular-line-left" style="background-color: rgb(255, 255, 255);"></div><span class="swal2-success-line-tip"></span> <span class="swal2-success-line-long"></span><div class="swal2-success-ring"></div> <div class="swal2-success-fix" style="background-color: rgb(255, 255, 255);"></div><div class="swal2-success-circular-line-right" style="background-color: rgb(255, 255, 255);"></div></div><img class="swal2-image" style="display: none;"><button type="button" class="swal2-close" aria-label="Close this dialog" style="display: none;">×</button></div>' + '<h5>درخواست با موفقیت تایید شد</h5>')
          location.reload()
        })
        .catch(error => {
          if (error.response) {
          } else if (error.message) {
          }
        })
    },
    async areject (user, num, id) {
      await axios
        .put('adminpanel/bankaccounts', { user: user, number: num, status: 'True', id: id })
        .then(response => {
          this.$swal('<div class="swal2-header"><ul class="swal2-progress-steps" style="display: none;"></ul><div class="swal2-icon swal2-success swal2-icon-show" style="display: flex;"><div class="swal2-success-circular-line-left" style="background-color: rgb(255, 255, 255);"></div><span class="swal2-success-line-tip"></span> <span class="swal2-success-line-long"></span><div class="swal2-success-ring"></div> <div class="swal2-success-fix" style="background-color: rgb(255, 255, 255);"></div><div class="swal2-success-circular-line-right" style="background-color: rgb(255, 255, 255);"></div></div><img class="swal2-image" style="display: none;"><button type="button" class="swal2-close" aria-label="Close this dialog" style="display: none;">×</button></div>' + '<h5>درخواست با موفقیت رد شد</h5>')
          setTimeout(() => {
            location.reload()
          }, 2000)
        })
        .catch(error => {
          if (error.response) {
          } else if (error.message) {
          }
        })
    },
    async getc () {
      await axios
        .get('adminpanel/bankcards')
        .then(response => {
          this.requests = response.data
        })
    },
    async accept (user, num, id, image) {
      await axios
        .post('adminpanel/bankcards', { user: user, number: num, status: 'True', id: id, image: image })
        .then(response => {
          this.$swal('<div class="swal2-header"><ul class="swal2-progress-steps" style="display: none;"></ul><div class="swal2-icon swal2-success swal2-icon-show" style="display: flex;"><div class="swal2-success-circular-line-left" style="background-color: rgb(255, 255, 255);"></div><span class="swal2-success-line-tip"></span> <span class="swal2-success-line-long"></span><div class="swal2-success-ring"></div> <div class="swal2-success-fix" style="background-color: rgb(255, 255, 255);"></div><div class="swal2-success-circular-line-right" style="background-color: rgb(255, 255, 255);"></div></div><img class="swal2-image" style="display: none;"><button type="button" class="swal2-close" aria-label="Close this dialog" style="display: none;">×</button></div>' + '<h5>درخواست با موفقیت تایید شد</h5>')
          location.reload()
        })
        .catch(error => {
          if (error.response) {
          } else if (error.message) {
          }
        })
    },
    async reject (user, num, id) {
      await axios
        .put('adminpanel/bankcards', { user: user, number: num, status: 'True', id: id })
        .then(response => {
          this.$swal('<div class="swal2-header"><ul class="swal2-progress-steps" style="display: none;"></ul><div class="swal2-icon swal2-success swal2-icon-show" style="display: flex;"><div class="swal2-success-circular-line-left" style="background-color: rgb(255, 255, 255);"></div><span class="swal2-success-line-tip"></span> <span class="swal2-success-line-long"></span><div class="swal2-success-ring"></div> <div class="swal2-success-fix" style="background-color: rgb(255, 255, 255);"></div><div class="swal2-success-circular-line-right" style="background-color: rgb(255, 255, 255);"></div></div><img class="swal2-image" style="display: none;"><button type="button" class="swal2-close" aria-label="Close this dialog" style="display: none;">×</button></div>' + '<h5>درخواست با موفقیت رد شد</h5>')
          setTimeout(() => {
            location.reload()
          }, 2000)
        })
        .catch(error => {
          if (error.response) {
          } else if (error.message) {
          }
        })
    }
  }
}

</script>
<style>
.cent{
  text-align: center;
}
.btnfont{
  font-size: 12px;
  padding: 9px;
  margin: 2px;
}
.wallets:hover{
  background: #efefff;
}
.left{
  float: left;
}
</style>
