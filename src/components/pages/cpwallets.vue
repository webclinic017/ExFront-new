<template>
  <div>

    <input class="form-control" type="search" placeholder="search..." style="textalign:left;direction:ltr;font-family:'arial'" @input="search()" v-model="searchtext"><br>
      <b-card no-body>
        <div class="table-responsive">
        <table class="table" style="direction:rtl!important">
          <thead>
            <tr>
              <th>Currency</th>
              <th>Available</th>
              <th>Operations</th>
            </tr>
          </thead>
        <tbody>
          <tr v-for="(section) in wallets" v-bind:key="section.name">
                  <td v-if="section.brand == 'USDT' |section.brand == 'BTC' |section.brand == 'ETH' |section.brand == 'TRX'" style="width:15%;font-wieght:bold;font-family:'arial';font-size:20px"><router-link :to="`/cpwallets/${section.name}`" class="text-big font-weight-semibold" >
                  {{section.brand}}
                  </router-link></td>
                  <td v-if="section.brand == 'USDT' |section.brand == 'BTC' |section.brand == 'ETH' |section.brand == 'TRX'" style="padding:20px;font-family:'arial';font-size:14px"> <router-link :to="`/cpwallets/${section.name}`"><a v-if="!section.balance">0</a> {{section.balance}}</router-link></td>
                  <td v-if="section.brand == 'USDT' |section.brand == 'BTC' |section.brand == 'ETH' |section.brand == 'TRX'" style="padding:0;font-family:'arial';font-size:14px"><router-link  :to="`/cpwallets/${section.name}/withdraw`" class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'">برداشت</router-link><router-link :to="`/cpwallets/${section.name}/history`"  class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'"> تاریخچه </router-link><router-link v-if="section.brand == 'USDT' |section.brand == 'BTC' |section.brand == 'ETH' |section.brand == 'TRX'"  :to="`/cpwallets/${section.name}/deposit`" class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'">واریز</router-link></td>
          </tr>
          <tr v-for="(section) in wallets" v-bind:key="section.id">
                  <td v-if="!(section.brand == 'USDT' |section.brand == 'BTC' |section.brand == 'ETH' |section.brand == 'TRX')" style="width:15%;font-wieght:bold;font-family:'arial';font-size:20px"><router-link :to="`/cpwallets/${section.name}`" class="text-big font-weight-semibold" >
                  {{section.brand}}
                  </router-link></td>
                  <td v-if="!(section.brand == 'USDT' |section.brand == 'BTC' |section.brand == 'ETH' |section.brand == 'TRX')" style="padding:20px;font-family:'arial';font-size:14px"> <router-link :to="`/cpwallets/${section.name}`"><a v-if="!section.balance">0</a> {{section.balance}}</router-link></td>
                  <td v-if="!(section.brand == 'USDT' |section.brand == 'BTC' |section.brand == 'ETH' |section.brand == 'TRX')" style="padding:0;font-family:'arial';font-size:14px"><router-link  :to="`/cpwallets/${section.name}/withdraw`" class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'">برداشت</router-link><router-link :to="`/wallets/${section.name}/history`"  class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'"> تاریخچه </router-link><router-link v-if="section.brand == 'USDT' |section.brand == 'BTC' |section.brand == 'ETH' |section.brand == 'TRX'"  :to="`/wallets/${section.name}/deposit`" class="btnfont btn btn-dark walbtn" style="font:16px 'Yekan'">واریز</router-link></td>
          </tr>
        </tbody>
            </table>
        </div>
      </b-card>

  </div>
</template>

<script>
import axios from 'axios'
import index from './index.vue'
export default {
  components: { index },
  name: 'pages-forums-list',
  metaInfo: {
    title: 'کیف ها'
  },
  mounted () {
    this.checklevel()
    this.getprice()
    this.getw()
  },
  data: () => ({
    currencies: [],
    wallets: [],
    walletsback: [],
    usd: 250000,
    temp: {},
    searchtext: ''
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
    async getw () {
      await axios
        .get('/cp_wallets')
        .then(response => {
          this.wallets = response.data
          this.walletsback = response.data
        }).then(() => {
        })
    },
    async getprice () {
      await axios
        .get('/')
        .then(response => {
          this.temp = response.data[0]
        })
        .catch(() => {
        })
    },
    getbrand (brand) {
      return this.temp[`${brand.toLowerCase()}`]
    },
    search (){
      this.wallets = {}
      for (const [key, value] of Object.entries(this.walletsback)){
        if(key.includes(this.searchtext.toUpperCase())){
        this.wallets[key] = value
        }
      }
    }
  },
}

</script>
<style>
.cent{
  text-align: center;
}
.btnfont{
  font-family: 'arial';
  font-size: 12px;
  padding: 9px;
  margin: 2px;
}
td{
min-height: 60px;
text-align: center;
}
th{
text-align: center;
}
.wallets:hover{
  background: #efefff;
}
a{
  color:#888
}
@media only screen and (max-width: 1024px) {
.nmobile{
  display: none;
}
.walbtn{
height:30%;
width: 90%;
min-height: 40px;
float: left;
}
}
@media only screen and (min-width: 1024px) {
.walbtn{
padding: 6px;
margin:20px 5px
}
}
@media only screen and (max-width: 1275px) {
.nmobile{
  display: none;
}
}
</style>
