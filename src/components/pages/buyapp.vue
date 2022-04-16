<template>
  <div>
    <b-card>             
      <b-card-header>
        <h2>سفارش سایت صرافی</h2>
      </b-card-header><br>
      <h4>لطفا پکیج مورد نظر خود را انتخاب کرده و برای ورود به صفحه پرداخت بر روی دکمه تایید کلیک کنید</h4><br><br>
      <button id="1" @click="set(1)" style="width:30%;margin:1.6%;float:left" class="btn btn-secondary">
        
        <img style="width:100%" src="https://image.freepik.com/free-vector/people-creating-social-media-landing-page_52683-38062.jpg" alt=""><br><br>
        <h6>سفارش سایت <br>  <br> <br></h6>
        <h6>۳۰۰,۰۰۰,۰۰۰ ریال</h6>
      </button>
      <button id="2" @click="set(2)" style="width:30%;margin:1.6%;float:left" class="btn btn-secondary">
        
        <img style="width:100%" src="https://image.freepik.com/free-vector/designers-are-working-desing-web-page-web-design-user-interface-user-experience-content-organization_335657-4403.jpg" alt=""><br><br>
        <h6> سفارش سایت <br> + <br> اپ اندروید یا آی او اس</h6>
        <h6>۴۰۰,۰۰۰,۰۰۰ ریال</h6>
      </button>
      <button id="3" @click="set(3)" style="width:30%;margin:1.6%;float:left" class="btn btn-secondary">
        
        <img style="width:100%" src="https://image.freepik.com/free-vector/people-working-with-technology-isometric-design_52683-14119.jpg" alt=""><br><br>
        <h6> سفارش سایت <br> + <br> اپ اندروید و آی او اس</h6>
        <h6>۵۰۰,۰۰۰,۰۰۰ ریال</h6>
      </button><br><br>
      <button @click="submit" class="btn btn-dark" style="margin:auto">تایید</button>
    </b-card><br>
    
        
  </div>
</template>

<script>
import axios from 'axios'
import './tv'
import bFormSlider from 'vue-bootstrap-slider/es/form-slider';
import 'bootstrap-slider/dist/css/bootstrap-slider.css'

export default {
  name: 'pages-forums-list',
  metaInfo: {
    title: 'کیف ها'
  },
  updated (){
  },
  mounted () {
    document.title = ' AMIZAS Exchange |  سفارش سایت و اپ صرافی '
  },
  data: () => ({
    option: 0,
    link:''
  }),
  methods: {
    set(ids) {
      document.querySelectorAll('.btn').forEach(item =>{
        item.className = item.className.replace('success' , 'secondary')
      })
      document.getElementById(ids).className = document.getElementById(ids).className.replace('secondary' , 'success')
      this.option = ids
    },
    async submit () {
      this.$loading(true)
      await axios
        .post('/request2/', {option : this.option})
        .then(response => {
          this.$loading(false)
          this.link = response.data
          let a = document.createElement("a");
          document.body.appendChild(a);
          a.style = "display: none";
          a.href = this.link;
          a.click();
        })
    }
  },
  watch: {
    amount: {
        handler: function() {
            this.gettings();
        },
        deep: true
      },
    getting: {
        handler: function() {
            this.payings(); 
        },
        deep: true
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
.error{
    color:red
}
::-webkit-scrollbar {
  width: 5px;
}

/* Track */
::-webkit-scrollbar-track {
  box-shadow: inset 0 0 5px grey; 
  border-radius: 10px;
}
 
/* Handle */
::-webkit-scrollbar-thumb {
  background: darkgrey; 
  border-radius: 10px;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: grey; 
}
.form-control:focus {
  box-shadow: none;
}
</style>
