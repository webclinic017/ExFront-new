<template>
  <div>
     <div class="header bg-gradient-success py-7 py-lg-8 pt-lg-9">
      <b-container>
        <div class="header-body text-center mb-7">
          <b-row class="justify-content-center">
          </b-row>
        </div>
      </b-container>
      <div class="separator separator-bottom separator-skew zindex-100">
        <svg x="0" y="0" viewBox="0 0 2560 100" preserveAspectRatio="none" version="1.1"
             xmlns="http://www.w3.org/2000/svg">
          <polygon class="fill-default" points="2560 0 2560 100 0 100"></polygon>
        </svg>
      </div>
    </div>


      <b-card no-body style="width:80%;margin:10%;margin-top:-100px;text-align:center!important">

        <b-card-header style="text-align:center!important" class="row no-gutters align-items-center">
          <h3 style="text-align:center!important;width:100%!important">پرداخت شما با موفقیت انجام شد</h3>
        </b-card-header>

        <b-card-body style="text-align:center!important">
            تا {{timers}} ثانیه دیگر به سایت باز میگردید
        </b-card-body>

      </b-card>

  </div>
</template>

<script>
export default {
  name: 'pages-forums-list',
  metaInfo: {
    title: 'کیف ها'
  },
  mounted () {
    this.timer()
  },
  data: () => ({
    timers: 3,
  }),
  forumPath: [
    { text: 'کیف ها', active: true }
  ],
  methods: {
    timer () {
     setTimeout(() => {
       if(this.timers > 0){
         this.timers = this.timers - 1
          this.timer()
       }else{
        open('https://amizax.com/wallets')
          let a = document.createElement("a");
          document.body.appendChild(a);
          a.style = "display: none";
          a.href = 'https://amizax.com/wallets';
          a.click();
       }
     }, 1000);
    },
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
.left{
  float: left;
}
</style>
