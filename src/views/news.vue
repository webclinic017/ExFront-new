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

        <h2 style="background:#ffffff;height:40px; margin:0; padding:10px; text-align:center"><br> آخرین اخبار</h2>
        <h2 style="background:#ffffff;height:40px; margin:0; padding:10px"><br> </h2>
        <h2 style="background:#ffffff;height:40px; margin:0; padding:10px"><br> </h2>
        <hr style="background:#ffffff;height:40px; margin:0; padding:10px">
        
        
        
        <div class="d-none d-md-block" v-for="(item , idx) in posts" v-bind:key="idx" style="background:white ; padding-bottom:60px;" >
                  <div   style="height:350px;background:rgb(244, 248, 249);width:80%;margin:auto;border-radius:10px;border:solid #dfdfdf .5px;  text-align:right">
                    <div style="width:40%; float:right ; height:100%; padding-top:0">
                      <img style="width:100%;height:100%;border-radius:0 10px 10px 0" :src="item.get_pic" alt="">
                    </div>
                    <div style="width:60%; float:left; height:100% ; padding:10%; padding-top:5%">
                      <h4>{{item.title}} </h4>
                      <hr>
                      <p>{{item.minitext}}</p>
                    </div>
                  </div>
                  </div>



          <div class="d-md-none " v-for="(item , idx) in posts" v-bind:key="idx" style="background:white ; padding-bottom:60px;" >
                  <div   style="height:auto;background:rgb(244, 248, 249);width:80%;margin:auto;border-radius:10px;border:solid #dfdfdf .5px;  text-align:center">
                    <div style="width:100%;   height:100%; padding-top:0">
                      <img style="width:100%;height:100%;border-radius: 10px 10px  0  0 " :src="item.get_pic" alt="">
                    </div>
                    <div style="width:100%; height:100% ; padding:10%; padding-top:5%;  text-align:justify">
                      <h4>{{item.title}} ssss</h4>
                      <hr>
                      <p>{{item.minitext}}</p>
                    </div>
                  </div>
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
  import Trend from 'vuetrend'

  export default {
    components: {

    },
    data() {
      return {
        posts: [],
        tops: [],
        bottom: [],
        sym : 'BTCUSDT',
        dashboardinfo : [],
        info: [],
        his: [],
        slides: [],
        slides2: []
      }
    },
    methods: {
      async price () {
      localStorage.removeItem('uri')
      await axios
        .get('/indexprice')
        .then(response => {
          this.info = response.data
          setTimeout(() => {
            this.price()
          }, 5000)
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
    async getbottom () {
      await axios
        .get('/bottomsticker')
        .then(response => {
          this.bottom = response.data
        })
    },
    async review () {
      await axios
        .get('/review')
        .then(response => {
        })
    },
    async getposts () {
      await axios
        .get('/mainpageposts')
        .then(response => {
          this.posts = response.data
        })
    },
    async history () {
      await axios
        .get('/indexhistory')
        .then(response => {
          this.his = response.data
        })
    }
    },
    beforeMount(){
      this.price()
      this.history()
      this.gettop()
      this.getbottom()
      this.getposts()
      this.review()
    }
  };
</script>
<style>
.card-img-top {
  height:160px
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
