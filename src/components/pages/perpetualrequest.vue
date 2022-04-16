<template>
  <div>
    <b-card v-if="verified" no-body class="col-12">
        <b-card-header class="row no-gutters align-items-center cent" style="font-family:'arial'">
          <h2>   حساب پرپشوال شما تایید شده است یا درخواست ثبت کرده اید</h2>
        </b-card-header>

          <b-card-body class="py-3 cent">
            <router-link to="/dashboard" class="btn btn-danger"  style="margin:20px">بازگشت به داشبورد</router-link>
          </b-card-body>
      </b-card>

      <b-card v-if="!verified" no-body class="col-12">
        <b-card-header class="row no-gutters align-items-center cent" style="font-family:'arial'">
          <h2>ارسال درخواست تایید حساب پرپشوال</h2>
        </b-card-header>

          <b-card-body class="py-3 cent">
            <button @click="submit()" class="btn btn-success" style="margin:20px"> ارسال</button>
            <router-link to="/dashboard" class="btn btn-danger"  style="margin:20px">لغو</router-link>
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
    this.check()
    this.checklevel()
  },
  data: () => ({
    depfee : 0,
    mainwal: '',
    depwallets: [],
    verified: false,
    walletout: '',
    amountout: 0,
    amountin: 0,
    value: '',
    size: 200,
    currencies: {},
    wallets: [],
    fee : 0,
    chain: '',
    curs: {},
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
          else{
            this.createwallet(id)
          }
        })
    },
    async check () {
      const id = this.chain
      await axios
        .get('perpetualrequest')
        .then(data => {
          if (data.data === 2){
            this.verified = true
          } else {
            this.verified = false
          }
        })
    },
    async submit () {
      const id = this.chain
      await axios
        .post('perpetualrequest')
        .then(data => {
          this.$swal.fire({
              type: 'seccess',
              text: 'با موفقیت ثبت شد',
        })
        this.verified = true
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
.nav-link {
  padding:15px;
  padding-left: 15px!important;
  text-align:center
}
input{
  font-family: 'arial';
}
</style>
