<template>
  <div>
    
  </div>
</template>
<script>
  // Charts
  import axios from 'axios'
  import './tv'

  export default {
    components: {

    },
    data() {
      return {
        referalid: '',
        sym : 'BTCUSDT',
        dashboardinfo : [],
        leverage : [],
        currenciescount: 0,
      }
    },
    methods: {
      tv () {
      new TradingView.widget(
        {
        "width": screen.width * .7,
        "height": 390,
        "symbol": `${this.sym}`,
        "timezone": "Etc/UTC",
        "theme": "light",
        "style": "1",
        "locale": "en",
        "enable_publishing": false,
        "allow_symbol_change": true,
        "container_id": "tradingview_1be21"
      }
  );
    },
      async get_history () {
      await axios
        .get('/pricehistory')
        .then(response => {
          for (item of response.data){
          }
        })
        .catch(data => {
          
        })
    },
    async currencies () {
      await axios
        .get('/cp_mg_main')
        .then(response => {
          console(response)
          for (item of response.data){
            this.currenciescount = response.data.length
          }
        })
        .catch(data => {
          
        })
    },
    async get_info () {
      await axios
        .get('/dashboardinfo')
        .then(response => {
          this.dashboardinfo = response.data[0]
        })
    },
    async getlev () {
      await axios
        .get('/leverages')
        .then(response => {
          this.leverage = response.data
        })
    },
    async get_user () {
      await axios
        .get('/userinfo')
        .then(response => {
          this.referalid = response.data[0].get_referal
          console.log(response)
        })
    },
    },
    mounted() {

    }
  };
</script>
<style>
.el-table .cell{
  padding-left: 0px;
  padding-right: 0px;
}
</style>
