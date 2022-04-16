<template>
  <div>

    <base-header class="pb-6 pb-8 pt-10 pt-md-8 bg-light" style="background:url(https://papers.co/wallpaper/papers.co-vn41-bw-line-dark-art-abstract-pattern-29-wallpaper.jpg);background-size:100% 100%;height:450px">
      <!-- Card stats -->
      
      <b-row>
        <b-col style="background:none!important">
          <div style="width:65% ; height: 150px ;margin:auto; text-align:center">
            <div class="d-md-none" style="margin:50px"></div>
            <h2 style="font:45px 'arial';color:white">AMIZAX EXCHNGE</h2>
            <h2 style="color:white">Best Place To Learn And To Trade CryptoCurrencies</h2>
          </div>
        </b-col>
      </b-row>
    </base-header>



    <div class="d-md-none " style="width:100%; background:black; min-height:250px">
    <b-carousel indicators style="width:90%;margin:auto;margin-top:-170px;text-align:right; background:black">
    <b-carousel-slide v-for="(slide , idx) in slides2" v-bind:key="idx">
     <template v-slot:img>
      <b-row >
       <b-col id="slide" cols="12" md="4" class="mb-3">
        <b-card  :img-src="slide.get_pic" img-top no-body>
         <b-card-body>
          <b-card-title>{{slide.title}}</b-card-title>
           <b-card-text style="text-align:justify">
             {{slide.minitext}}
           </b-card-text>
         </b-card-body>
        </b-card>
       </b-col>
      </b-row>
     </template>
   </b-carousel-slide>
          </b-carousel>
          </div>



    <div class="d-none d-md-block" style="width:100%; background:black; height:430px">
    <b-carousel indicators style="width:90%;margin:auto;margin-top:-170px;text-align:right; background:black;border-radius:10px ">
    <b-carousel-slide v-for="(slide , idx) in slides" v-bind:key="idx" style=" height:410px;border-radius:10px">
     <template v-slot:img>
      <b-row>
       <b-col cols="12" md="4" class="mb-3" v-for="(imgsrc,idx) in slide"  v-bind:key="idx">
        <b-card :img-src="imgsrc.get_pic" img-top no-body style="height:410px">
         <b-card-body>
          <b-card-title>{{imgsrc.title}}</b-card-title>

           <b-card-text style="text-align:justify">
             {{imgsrc.minitext}}
           </b-card-text>
         </b-card-body>
        </b-card>
       </b-col>
      </b-row>
     </template>
   </b-carousel-slide>
          </b-carousel>
          </div>
        <div><br>
    <b-card id="page" v-if="page" style="border-radius:20px;margin:15%;margin-top:10%;width:70%;padding:0!important">
        <img :src="page.get_pic" style="width:100%;border-radius:20px 20px 0 0 " alt="">
      <b-card-body style="padding:8%;text-align:justify">
        <h3>{{page.title}}</h3><br><hr>
        <p>{{page.text}}</p>
      </b-card-body>
    </b-card>
  </div>

        <footer class="d-none d-md-block" style="background:black;color:white; text-align:right ;">
          <div class="col-12" style="height:250px">
            <div class="col-4" style="height:100% ; float:right ; padding:2%">
              <b-navbar-brand to="/">
          <img style="width:60px; height:70px " src="/img/brand/ars.png">
              </b-navbar-brand><br><br>
              <h5 style="color:white ; font-size:16px">بهترین مکان برای ترید</h5>
              </div>
            <div class="col-3" style="height:100% ; float:right ; padding:2%">
              <h5 style="color:white ; font-size:16px">خدمات ما</h5>
              <hr style="border-color:white">
              <router-link to="/pages/margin-trade"><h6 style="color:white ; font-size:12px">معاملات مرجین</h6></router-link>
              <router-link to="/pages/perpetual-trade"><h6 style="color:white ; font-size:12px">معاملات پرپشوال</h6></router-link>
              <router-link to="/pages/exchange"><h6 style="color:white ; font-size:12px"> اکسچینج</h6></router-link>
              <router-link to="/pages/buysell"><h6 style="color:white ; font-size:12px">خرید و فروش</h6></router-link>
              <router-link to="/pages/onlinetrading"><h6 style="color:white ; font-size:12px">تریدینگ لحظه ای </h6></router-link>
              </div>
            <div class="col-3" style="height:100% ; float:right ; padding:2%">
              <h5 style="color:white ; font-size:16px">درباره ما</h5>
              <hr style="border-color:white">
              <router-link to="/pages/group"><h6 style="color:white ; font-size:12px">اعضای شرکت</h6></router-link>
              <router-link to="/pages/history"><h6 style="color:white ; font-size:12px">تاریخچه</h6></router-link>
              <router-link to="/pages/line"><h6 style="color:white ; font-size:12px">زمینه فعالیت</h6></router-link>
              <router-link to="/pages/rules"><h6 style="color:white ; font-size:12px">قوانین و مقررات </h6></router-link>
              </div>
              <div class="col-2" style="height:100% ; float:right ; padding:2%">
              
              <h5 style="color:white ; font-size:16px">ارتباط با ما</h5>
              <hr style="border-color:white">
              <router-link to="/ticketadd"><h6 style="color:white ; font-size:12px">پشتیبانی آنلاین</h6></router-link>
              <router-link to="/contacts"><h6 style="color:white ; font-size:12px">تماس با ما</h6></router-link>
              </div>
          </div>
        </footer>


        <footer class="d-md-none" style="background:black;color:white; text-align:center ;">
          <div class="col-12" style="height:auto">
            <div class="col-12" style="height:100% ; padding:2%">
              <b-navbar-brand to="/" style="margin:0">
          <img style="width:60px; height:70px ; margin:auto" src="/img/brand/ars.png">
              </b-navbar-brand><br><br>
              <h5 style="color:white ; font-size:16px">بهترین مکان برای ترید</h5>
              </div>
            <div class="col-12" style="height:100% ; margin-top:80px ; padding:2%">
              <h5 style="color:white ; font-size:16px">خدمات ما</h5>
              <hr style="border-color:white">
              <router-link to="/pages/margin-trade"><h6 style="color:white ; font-size:12px">معاملات مرجین</h6></router-link>
              <router-link to="/pages/perpetual-trade"><h6 style="color:white ; font-size:12px">معاملات پرپشوال</h6></router-link>
              <router-link to="/pages/exchange"><h6 style="color:white ; font-size:12px"> اکسچینج</h6></router-link>
              <router-link to="/pages/buysell"><h6 style="color:white ; font-size:12px">خرید و فروش</h6></router-link>
              <router-link to="/pages/onlinetrading"><h6 style="color:white ; font-size:12px">تریدینگ لحظه ای </h6></router-link>

              </div>
            <div class="col-12" style="height:100% ; margin-top:80px ; padding:2%">
              <h5 style="color:white ; font-size:16px">درباره ما</h5>
              <hr style="border-color:white">
              <router-link to="/pages/group"><h6 style="color:white ; font-size:12px">اعضای شرکت</h6></router-link>
              <router-link to="/pages/history"><h6 style="color:white ; font-size:12px">تاریخچه</h6></router-link>
              <router-link to="/pages/line"><h6 style="color:white ; font-size:12px">زمینه فعالیت</h6></router-link>
              <router-link to="/pages/rules"><h6 style="color:white ; font-size:12px">قوانین و مقررات </h6></router-link>

              </div>
              <div class="col-12" style="height:100% ; margin-top:80px ; padding:2%">
              
              
              <h5 style="color:white ; font-size:16px">ارتباط با ما</h5>
              <hr style="border-color:white">
              <router-link to="/ticketadd"><h6 style="color:white ; font-size:12px">پشتیبانی آنلاین</h6></router-link>
              <router-link to="/contacts"><h6 style="color:white ; font-size:12px">تماس با ما</h6></router-link>              </div>
          </div>
        </footer>
  </div>
</template>
<script>
  // Charts
  import Vue from 'vue'
  import axios from 'axios'

  export default {
    components: {

    },
    mounted () {
      this.getpost()
      this.gettop()
    },
    data() {
      return {
        posts: [],
        tops: [],
        bottom: [],
        sym : 'BTCUSDT',
        dashboardinfo : [],
        info: [],
        uri: '',
        his: [],
        slides: [],
        slides2: []
      }
    },
    methods: {
      async getpost () {
        await axios
          .put('/otherpages' , {name: this.$route.params.page})
          .then(response => {
            this.page = response.data[0]
          })
      },
      async gettop () {
        await axios
          .get('/topsticker')
          .then(response => {
            var temp = []
            var i=0
            for(var j=3 ; j<=response.data.length ; j = j+3){
              temp.length = 0
              for(i ; i<j; i++){
                temp.push({get_pic:response.data[i].get_pic , title : response.data[i].title , text: response.data[i].text , minitext: response.data[i].minitext})
              }
              i = j
              this.slides.push(temp)
            }

            var temp2 = []
            var i=0
              for(i ; i<response.data.length; i++){
              this.slides2.push({get_pic:response.data[i].get_pic , title : response.data[i].title , text: response.data[i].text})
              }
          })
          
      },
    },
    beforeMount(){
      this.getpost()
      this.gettop()
    },
    watch:{
    $route (to, from){
        this.getpost()
        location.reload()
        Vue.$forceUpdate();
    }
  } 
  };
</script>
<style>
#page {
    white-space: pre-line;    
}
.card-img-top {
  height:160px
}
#page .card-body{
  padding:0
}
.el-table .cell{
  padding-left: 0px;
  padding-right: 0px;
}
.carousel-indicators > li {
 background-color: var(--primary);
 margin-top: 20px;
}
.cent{
  text-align: center;
}
@media only screen and (max-width: 1024px) {
.nmobile{
  display: none;
}
}
@media only screen and (max-width: 1275px) {
.nmobile{
  display: none;
}
}
</style>
