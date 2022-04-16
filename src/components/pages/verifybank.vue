<template>
  <div>


      <b-card no-body class="col-12">

        <b-card-header class="row no-gutters align-items-center">
          <div class="col-1 cent">نام کاربری</div>
          <div class="col-3 font-weight-bold cent">شماره کارت</div>
              <div class="col-5 cent">تصویر کارت</div>
              <div class="col-3"> </div>

        </b-card-header>

        <div v-for="section in requests" :key="section.title">
          <b-card-body class="py-3 wallets">

            <div class="row no-gutters align-items-center">
              <div class="col-1 cent">{{section.get_user}}</div>
              <div class="col-3 cent">{{section.bankc}}</div>
              <div class="col-5 cent"><a href="javascript:void(0)" class="text-big font-weight-semibold">
                      <a format="png" target="_blank" :href="`${section.get_image}`"><img :src="`${section.get_image}`" alt="" class="d-block image" style="width:20%!important;margin:auto"></a>
                      <div class="media-body flex-truncate ml-2">
                    </div></a></div>
                  <div class="col-3 left"><button class="btnfont btn btn-danger" @click="reject(section.get_user , section.bankc , section.id)">رد درخواست</button><button class="btnfont btn btn-success" @click="accept(section.get_user , section.bankc, section.id, section.get_image)"> تایید درخواست</button></div>
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
    this.checklevel()
  },
  data: () => ({
    requests: []
  }),
  forumPath: [
    { text: 'کیف ها', active: true }
  ],
  methods: {
    async checklevel (id) {
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
