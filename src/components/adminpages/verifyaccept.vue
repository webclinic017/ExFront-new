<template>
  <div>

      <b-card no-body class="col-12 d-none d-md-block">

        <b-card-header class="row no-gutters align-items-center">
          <div class="col-1 cent">نام کاربری</div>
              <div class="col-6 cent">تصویر کارت</div>
              <div class="col-5"> </div>

        </b-card-header>

        <div v-for="section in requests" :key="section.title" class="">
          <b-card-body class="py-3 wallets ">

            <div class="row no-gutters align-items-center">
              <div class="col-1 cent">{{section.get_user}}</div>
              <div class="col-6 cent"><a href="javascript:void(0)" class="text-big font-weight-semibold">
                      <a format="png" target="_blank" :href="`${section.get_image}`"><img :src="`${section.get_image}`" alt="" class="d-block image" style="width:20%!important;margin:auto"></a>
                      <div class="media-body flex-truncate ml-2">
                    </div></a></div>
                  <div class="col-5 left"><button class="btnfont btn btn-danger" @click="reject(section.get_user_id , section.id)">رد درخواست</button><button class="btnfont btn btn-success" @click="accept(section.get_user_id , section.id)"> تایید درخواست</button></div>
            </div>

          </b-card-body>
        </div>
        <b-card-body v-if="!requests[0]" class="py-3 wallets">
            <h4 class="cent">درخواستی پیدا نشد</h4>
          </b-card-body>

      </b-card>


      <b-card no-body class="col-12 d-md-none mob">

        <div v-for="section in requests" :key="section.title" class="">
          <b-card-body class="py-3 wallets ">
            <img style="width:100%" :src="`${section.get_image}`" alt=""><br><br>
            <div style="width:45% ;float:right">
              <h4 style=" height:50px " >نام : </h4>
              <button style="" class="btnfont btn btn-success" @click="accept(section.get_user_id , section.id)"> تایید درخواست</button>
            </div>
            <div style="width:45% ;float:left">
              <h4 style=" height:50px ; text-align:left ">{{section.get_user}}</h4>
              <button class="btnfont btn btn-danger" @click="reject(section.get_user_id , section.id)">رد درخواست</button>
            </div>
          </b-card-body>
        </div>
        <b-card-body v-if="!requests[0]" class="py-3 wallets">
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
  },
  data: () => ({
    requests: []
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
    async getc () {
      await axios
        .get('adminpanel/verifyaccept')
        .then(response => {
          this.requests = response.data
        })
    },
    async accept (user, id) {
      await axios
        .post('adminpanel/verifyaccept', { user: user, id: id })
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
    async reject (user, id) {
      await axios
        .put('adminpanel/verifyaccept', { user: user, id: id })
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
.mob .card-body{
  padding:0;
  width:95%;
  margin:2.5%;
}
</style>
