<template>
  <div class="tr">
      <b-card  class="col-12 d-none d-md-block">

        <b-card-header class="row no-gutters align-items-center">
          <div class="col-1 font-weight-bold"></div>
            <div class="d-none d-md-block col-10 text-muted">
              <div class="row no-gutters align-items-center">
                <div class="col-5" style="text_align:right">کاربر</div>
                <div class="col-3 cent">زمان</div>
                <div class="col-2 cent">نوع</div>
                <div class="col-2 cent">مقدار </div>
            </div>
          </div>
        </b-card-header>

        
          <b-card-body class="py-3">
            <div v-if="transactions">
              <div class="row no-gutters align-items-center">
                <div class="col-1"><a href="javascript:void(0)" class="text-big font-weight-semibold"><div class="media align-items-center">
                        <img :src="`img/avatars/`" alt="" class="d-block ui-w-50 rounded-circle">
                        <div class="media-body flex-truncate ml-2">
                        </div>
                      </div></a></div>
                <div class="d-none d-md-block col-10">

                  <div v-for="transaction in transactions" v-bind:key="transaction" class="row no-gutters align-items-center">
                    <div class="col-5" style="text_align:right">{{transaction.get_user}}</div>
                    <div class="col-3 cent">{{transaction.date}}</div>
                    <div class="col-2 cent" v-if="transaction.act === 1" style="color:green">{{String(transaction.act).replace('1', 'واریز')}}</div>
                    <div class="col-2 cent" v-if="transaction.act === 2" style="color:red">{{String(transaction.act).replace('2', 'برداشت')}}</div>
                    <div class="col-2 cent">{{transaction.amount}}</div>
                    <hr>
                  </div>

                </div>
              </div>
            </div>
            <div v-if="!transactions" class="cent">
              <h3>تراکنشی پیدا نشد</h3>
            </div>
          </b-card-body>
      </b-card>
      <b-card  class="d-md-none ">
            <div v-if="transactions">
              <b-card v-for="transaction in transactions" v-bind:key="transaction" style="min-height:150px" class="row no-gutters align-items-center">
                <div style="width:45% ;float:right">
              <h2  style=" min-height:80px; text-align:center ">کاربر</h2>
              <h2  style=" min-height:80px; text-align:center ">زمان</h2>
              <h2  style=" min-height:80px; text-align:center ">نوع</h2>
              <h2  style=" min-height:80px; text-align:center ">مقدار </h2>
              </div>
              <div style="width:45% ;float:left">
              <h2  style=" min-height:80px; text-align:center ">{{transaction.get_user}}</h2>
              <h2  style=" min-height:80px; text-align:center ">{{transaction.date}}</h2>
              <h2  style=" min-height:80px; text-align:center  ; color:green" v-if="transaction.act === 1" >{{String(transaction.act).replace('1', 'واریز')}}</h2>
              <h2  style=" min-height:80px; text-align:center  ; color:red" v-if="transaction.act === 2" >{{String(transaction.act).replace('2', 'برداشت')}}</h2>
              <h2  style=" min-height:80px; text-align:center ">{{transaction.amount}}</h2>
              </div>
                  </b-card><br>
            <div v-if="!transactions" class="cent">
              <h3>تراکنشی پیدا نشد</h3>
            </div>
            </div>
      </b-card>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'pages-forums-list',
  metaInfo: {
    title: 'Forum list - Pages'
  },
  data: () => ({
    transactions: [],
    forumPath: [
      { text: ' سفارشات باز', active: true }
    ],

    sectionsData: [{
      title: ' شناسه',
      forums: [{
        title: 'Getting started',
        threads: 12,
        replies: 34,
        lastUpdate: {
          date: '1d',
          thread: { title: 'Aliquam et velit vel nisi egestas pulvinar sit amet ac tellus' },
          user: { avatar: 'btc.png', name: 'Leon Wilson' }
        }
      }, {
        title: 'Announcements',
        threads: 43,
        replies: 112,
        lastUpdate: {
          user: { avatar: 'btc.png', name: 'Allie Rodriguez' }
        }
      }]
    }]
  }),
  mounted () {
    this.check()
    this.checklevel()
    this.gettransactions()
  },
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
    async gettransactions (id) {
      await axios
        .get('/adminpanel/transactions')
        .then(response => {
          console.log(response)
          this.transactions = response.data
        })
    },
    check () {
      if (!this.$store.state.isAuthenticated) {
        const toPath = this.$route.query.to || '/login'
        this.$router.push(toPath)
      }
    }
  }
}
</script>
<style>
.cent{
  text-align: center;
}
.tr .card-body{
  padding:0;
  width:100%
}
</style>
