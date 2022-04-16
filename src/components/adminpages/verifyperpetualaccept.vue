<template>
  <div>


      <b-card no-body class="col-12">

        <b-card-header class="row no-gutters align-items-center">
          <div class="col-6 cent">نام کاربری</div>
          <div class="col-6 cent">زمان ثبت</div>
        </b-card-header>

        <div v-for="section in requests" :key="section.title">
          <b-card-body class="py-3 wallets">

              <div class="row no-gutters align-items-center">
                <div class="col-6 cent">{{section.get_user}}</div>
                <div class="col-6 cent">{{section.get_age}}</div>
              </div>
          </b-card-body>
        </div>

      </b-card>


      <b-card no-body class="col-12">

        <b-card-header class="row no-gutters align-items-center">
          <div class="col-12 cent"> تایید درخواست</div>
        </b-card-header>

        <div v-for="section in requests" :key="section.title">
          <b-card-body class="py-3 wallets">
            <form @submit.prevent="submit()">
              <label >Name</label>
              <b-input required v-model="name" ></b-input>
              <label >API-KEY</label>
              <b-input required v-model="apikey"></b-input>
              <label >SECRET-KEY</label>
              <b-input required v-model="secretkey"></b-input><br><br>
              <input type="submit" class="btn btn-dark">
            </form>
          </b-card-body>
        </div>

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
    requests: [],
    apikey: '',
    secretkey: '',
    name : ''
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
        .post(`adminpanel/perpetualreq/${this.$route.params.id}`)
        .then(response => {
          this.requests = response.data
        })
    },
    async submit () {
      await axios
        .post(`adminpanel/perpetualreqccept` , {apikey: this.apikey , secretkey : this.secretkey , name: this.name , id : this.$route.params.id })
        .then(response => {
          const toPath = this.$route.go || '/adminpanel/verifyperpetual'
          this.$router.push(toPath)
        })
    },
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
