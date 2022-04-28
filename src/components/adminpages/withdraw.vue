<template>
  <div>


      <b-card  class="col-12 d-none d-md-block">

        <b-card-header class="row no-gutters align-items-center">
          <div class="col-3 cent">نام کاربری</div>
          <div class="col-2 cent">مقدار</div>
          <div class="col-2 cent">زمان ثبت</div>
          <div class="col-4 cent"> حساب </div>
          <div class="col-1 cent"></div>

        </b-card-header>

        <div v-for="section in requests" :key="section.title">
          <b-card-body>

            <div class="row no-gutters align-items-center">
              <div class="col-3 cent" style="font: 12px 'arial'">{{section.get_user}}</div>
              <div class="col-2 cent" style="font: 12px 'arial'">{{section.amount}}</div>
              <div class="col-2 cent" style="font: 12px 'Yekan'">{{section.get_age}}</div>
              <div class="col-4 cent" style="font: 12px 'arial'">
                شماره شبا  <br>
                {{section.get_sheba}} <br>
                شماره حساب  <br>
                {{section.get_number}} <br>
                <a @click="cards(section.user)" style="cursor:pointer; color:#888">لیست کارت ها</a>
              </div>
              <div class="col-1 cent"><button class="btnfont btn btn-danger" style="width:100%;float:left" @click="reject(section.id)">رد </button><button class="btnfont btn btn-success" style="width:100%;float:left" @click="accept(section.id)"> تایید </button></div>
            </div>

          </b-card-body>
        </div>

      </b-card>


      <div  class="d-md-none transm">
            <div v-if="requests">
              <b-card v-for="transaction in requests" v-bind:key="transaction" style="min-height:150px ; maring-bottom:10px ; padding:5px!important" class="row no-gutters align-items-center ">
                <div style="width:35% ;float:right">
                  <h6  style=" height:50px ">نام کاربری</h6>
                  <h6  style=" height:50px ">مقدار</h6>
                  <h6  style=" height:50px ">زمان ثبت</h6>
                  <h6  style=" height:50px ">شبا </h6>
                  <h6  style=" height:50px ">شماره حساب </h6>
                </div>
              <div style="width:55% ;float:left">
                <h4  style=" height:50px ; text-align:left ; font: 12px 'arial'">{{transaction.get_user}}</h4>
                <h4  style=" height:50px ; text-align:left ; font: 12px 'arial'">{{transaction.amount}}</h4>
                <h4  style=" height:50px ; text-align:left ; font: 12px 'Yekan'">{{transaction.get_age}}</h4>
                <h4  style=" height:50px ; text-align:left ; font: 12px 'arial'">{{transaction.get_sheba}}</h4>
                <h5  style=" height:50px ; text-align:left ; font: 12px 'arial'">{{transaction.get_number}}</h5><br>
              </div>
              <div class="col-12 cent"><button class="btnfont btn btn-danger" style="width:100%;float:left" @click="reject(section.id)">رد درخواست</button><button class="btnfont btn btn-success" style="width:100%;float:left" @click="accept(section.id)"> تایید درخواست</button></div>
                  </b-card><br>
            <div v-if="!requests" class="cent">
              <h3>تراکنشی پیدا نشد</h3>
            </div>
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
        .get('adminpanel/withdraw')
        .then(response => {
          this.requests = response.data
        })
    },
    async cards(user) {
      await axios
        .get('adminpanel/cards' ,{user: user})
        .then(response => {
          this.cards = response.data
          this.$swal(response.data)
        })
    },
    async accept (id) {
      alert(id)
      await axios
        .post('adminpanel/withdraw', {id: id})
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
        .delete(`adminpanel/withdraw/${id}`)
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
.card-body{
  padding:0
}
</style>
