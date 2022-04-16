<template>
  <div>

    <h4 class="d-flex flex-wrap justify-content-between align-items-center pt-3 mb-4">
      <div class="col-12 col-md-3 p-0 ">
      </div>
    </h4>

      <b-card no-body class="col-12">

        <b-card-header class="row no-gutters align-items-center">
          <div class="col-1 font-weight-bold">نوع ارز</div>
          <div class="d-none d-md-block col-11 text-muted">
            <div class="row no-gutters align-items-center">
              <div class="col-2 cent">موجودی</div>
              <div class="col-2 cent">موجودی ریالی</div>
                  <div class="col-1 cent"></div>
                  <div class="col-1 cent"></div>
                  <div class="col-3"></div>
                  <div class="col-1"></div>

            </div>
          </div>
        </b-card-header>

          <b-card-body class="py-3 wallets">

            <div class="row no-gutters align-items-center">
              <div class="col-1"><a href="javascript:void(0)" class="text-big font-weight-semibold">
                      <img :src="`http://arsdev.ir${currencies.pic}`" alt="" class="d-block ui-w-50 rounded-circle">
                      <div class="media-body flex-truncate ml-2">
                    </div></a></div>
              <div class="d-none d-md-block col-11">

                <div class="row no-gutters align-items-center">
                  <div class="col-2 cent">{{currencies.amount}}</div>
                  <div class="col-2 cent">{{currencies.amount}}</div>
                  <div class="col-1 cent"></div>
                  <div class="col-1 cent"></div>
                  <div class="col-3"></div>
                  <div class="col-1"></div>
              </div>
              </div>
            </div>

          </b-card-body>

      </b-card>
      <b-card id="deposit">
        <b-card-header class="row no-gutters align-items-center">واریز</b-card-header>
       
      </b-card><br><br>




      
      <b-card id="withdraw">
        <b-card-header class="row no-gutters align-items-center">برداشت</b-card-header>
        <div><br><br>
          <h6> آدرس ولت </h6>
          <b-input class="" v-model="walletout"></b-input><br>
          <h6>مبلغ درخواستی</h6>
          <b-input class="" v-model="walletout"></b-input><br>
          <button id="withdraw" class="btn btn-success">ثبت درخواست</button>
        </div>
      </b-card><br><br>

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
    this.checklevel()
    this.getw()
    this.goto()
  },
  data: () => ({
    walletout: 0,
    value: '',
    size: 200,
    currencies: {},
    wallets: []
  }),
  forumPath: [
    { text: 'کیف ها', active: true }
  ],
  methods: {
    async getc () {
      const id = this.$route.params.id
      await axios
        .get(`/currencies/${id}`)
        .then(response => {
          this.currencies = response.data[0]
          this.currencies.amount = 0
          this.currencies.amount = this.wallets[0].amount
          this.currencies.address = this.wallets[0].address
          this.value = this.wallets[0].address
        })
    },
    async getw () {
      const id = this.$route.params.id
      await axios
        .get(`/wallet/${id}`)
        .then(response => {
          this.wallets = response.data
        }).then(() => {
          this.getc()
        })
    },
    async checklevel () {
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
          else{
            this.createwallet()
          }
        })
    },
    async createwallet () {
      setTimeout(() => {
        this.getw()
      }, 1000)
      const id = this.$route.params.id
      await axios
        .post(`/wallet/${id}`)
        .then(() => {
        })
    },
    goto () {
      if('place' in this.$route.params){
         setTimeout(() => {
        document.querySelector(`#${this.$route.params.place}`).scrollIntoView({ behavior: 'smooth' })
      }, 1000)
      }
    },
    copyUrl() {
      var copyText = document.getElementById("myInput");

      copyText.select();
      copyText.setSelectionRange(0, 99999); /* For mobile devices */

      navigator.clipboard.writeText(copyText.value);

    }
  },
  
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
.qr{
  width: 20%;
  margin-right: 40%;
  margin-top: 20px;
}
.address{
  margin:auto;
  text-align: center;
  margin-top: 10px;
  height: 65px;
  padding: 0;
}
.address h3{
  padding: 14px;
  white-space: nowrap;
  overflow-x: auto;
  overflow-y: hidden;
  height: 100%;
}
.addressbtn{
  float: left;
  height: 100%;
}
.address h3::-webkit-scrollbar {
  width: 1px;
}

.address h3::-webkit-scrollbar-track {
    box-shadow: inset 0 0 6px rgba(0,0,0,0.3);
    width: 3px;
    border-radius: 1px;
}

.address h3::-webkit-scrollbar-thumb {
    border-radius: 1px;
    box-shadow: inset 0 0 6px rgba(0,0,0,0.5);
    width: 3px;
}
.cent{
  margin:auto;
  text-align: center;
}
</style>
