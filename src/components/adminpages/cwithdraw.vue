<template>
  <div>


      <b-card no-body class="col-12 d-none d-md-block">

        <b-card-header class="row no-gutters align-items-center">
          <div class="col-2 cent">نام کاربری</div>
          <div class="col-1 cent">نوع ارز </div>
          <div class="col-1 cent"> شبکه</div>
          <div class="col-2 cent">مقدار</div>
          <div class="col-1 cent">زمان ثبت</div>
          <div class="col-3 cent">آدرس</div>
          <div class="col-2 cent">عملیات</div>

        </b-card-header>

        <div v-for="section in requests" :key="section.title">
          <b-card-body class="py-3 wallets">

            <div class="row no-gutters align-items-center">
              <div class="col-2 cent">{{section.get_user}}</div>
              <div class="col-1 cent">{{section.get_currency}}</div>
              <div class="col-1 cent">{{section.chain}}</div>
              <div class="col-2 cent">{{section.amount}}</div>
              <div class="col-1 cent">{{section.get_age}}</div>
              <div class="col-3 cent" style="padding:10px"><input type="text" class="form-control" :value="section.address"></div>
                  <div class="col-2 cent"><button class="btnfont btn btn-danger" @click="reject(section.id)">رد درخواست</button><button class="btnfont btn btn-success" @click="accept(section.id)"> تایید درخواست</button></div>
            </div>

          </b-card-body>
        </div>

      </b-card>


      <div  class="d-md-none transm">
            <div v-if="requests">
              <b-card v-for="transaction in requests" v-bind:key="transaction" style="min-height:150px ; maring-bottom:10px ; padding:5px!important" class="row no-gutters align-items-center ">
                <div style="width:45% ;float:right">
              <h6  style=" height:50px ">نام کاربری</h6>
              <h6  style=" height:50px ">نوع ارز</h6>
              <h6  style=" height:50px ">شبکه</h6>
              <h6  style=" height:50px ">مقدار </h6>
              <h6  style=" height:50px ">زمان ثبت </h6>
              <h6  style=" height:50px ">آدرس </h6>
              </div>
              <div style="width:45% ;float:left">
              <h4  style=" height:50px ; text-align:left">{{transaction.get_user}}</h4>
              <h4  style=" height:50px ; text-align:left">{{transaction.get_currency}}</h4>
              <h4  style=" height:50px ; text-align:left">{{transaction.chain}}</h4>
              <h4  style=" height:50px ; text-align:left">{{transaction.amount}}</h4>
              <h5  style=" height:50px ; text-align:left">{{transaction.get_age}}</h5><br>
              </div>
              <div class="col-12 cent" style="padding:10px"><input type="text" class="form-control" :value="transaction.address"></div>
              <div class="col-12 cent"><button class="btnfont btn btn-danger" style="width:100%;float:left" @click="reject(section.id)">رد درخواست</button><button class="btnfont btn btn-success" style="width:100%;float:left" @click="accept(section.id)"> تایید درخواست</button></div>
                  </b-card><br>
            </div>
            <div v-if="!requests" class="cent">
              <h3>تراکنشی پیدا نشد</h3>
            </div>
      </div>

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
        .get('adminpanel/cwithdraw')
        .then(response => {
          this.requests = response.data
        })
    },
    async accept (id) {
      alert(id)
      await axios
        .post('adminpanel/cwithdraw', {id: id})
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
    async reject (id) {
      await axios
        .put('adminpanel/cwithdraw', {id: id })
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
