<template>
  <div>


      <b-card no-body class="col-12">

        <b-card-header class="row no-gutters align-items-center">
          <div class="col-4 cent">نام کاربری</div>
          <div class="col-4 cent">موضوع</div>
          <div class="col-4 cent">زمان ثبت</div>
        </b-card-header>

        <div v-for="section in requests" :key="section.title">
          <b-card-body class="py-3 wallets">

              <router-link :to="'tickets/' + section.id" class="row no-gutters align-items-center">
                <div class="col-4 cent">{{section.get_user}}</div>
                <div class="col-4 cent">{{section.title}}</div>
                <div class="col-4 cent">{{section.get_age}}</div>
              </router-link>
          </b-card-body>
        </div>
          <b-card-body v-if="!requests[0]" class="py-3 wallets">
            <h4 class="cent">تیکتی پیدا نشد</h4>
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
        .get('adminpanel/subject')
        .then(response => {
          this.requests = response.data
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
