<template>
  <div>

  </div>
</template>
<script>
  // Charts
  import axios from 'axios'

  export default {
    components: {

    },
    data() {
      return {
        sym : 'BTCUSDT',
        dashboardinfo : [],
        reviews: [],
      }
    },
    methods: {
      tv () {
      if(this.sym == 'USDT'){
        new TradingView.widget(
        {
        "width": screen.width * .7,
        "height": 390,
        "symbol": `${this.sym}USD`,
        "timezone": "Etc/UTC",
        "theme": "light",
        "style": "1",
        "locale": "en",
        "hide_side_toolbar": false,
        "enable_publishing": false,
        "allow_symbol_change": true,
        "container_id": "tradingview_1be21"
      })
      }else{
        new TradingView.widget(
        {
        "width": screen.width * .7,
        "height": 390,
        "symbol": `${this.sym}USDT`,
        "timezone": "Etc/UTC",
        "theme": "light",
        "hide_side_toolbar": false,
        "style": "1",
        "locale": "en",
        "enable_publishing": false,
        "allow_symbol_change": true,
        "container_id": "tradingview_1be21"
      }
      )
      }
    },
      async get_history () {
      await axios
        .get('/pricehistory')
        .then(response => {
          for (item of response.data){
            alert(item)
          }
        })
        .catch(data => {
          
        })
    },
    async review () {
      await axios
        .get('adminpanel/review')
        .then(response => {
          this.reviews = response.data
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
    },
    mounted() {
      this.get_history()
      this.tv()
      this.get_info()
      this.review()
    }
  };
</script>
<style>
.el-table .cell{
  padding-left: 0px;
  padding-right: 0px;
}
</style>
