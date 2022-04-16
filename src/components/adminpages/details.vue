<template>
  <div>


      <b-card no-body class="col-12">

         <b-card-header class="row no-gutters align-items-center">
          <div class="col-4 cent">موضوع</div>
          <div class="col-5 cent">متن</div>
          <div class="col-2 cent">عملیات</div>
        </b-card-header>

         <div v-for="(section , idx) in pages" :key="idx">
          <b-card-body class="py-3 wallets" v-if="pages">
              <div class="row no-gutters align-items-center">
                <div class="col-4 cent">{{section.title}}</div>
                <div class="col-5 cent" style="font-size:12px;padding:4%"><textarea disabled style="width:100%" rows="6" :placeholder="section.text"></textarea></div>
                <div class="col-2 cent"><button @click="edit(section.id,section.text,section.title, section.minitext)" class="btn btn-warning" style="width:100%;font-size:12px;margin:0;padding: 20% 20% "><i class="fas fa-pen fa-2x"></i></button></div>
              </div>
          </b-card-body>
        </div>
          <b-card-body v-if="!pages.length" class="py-3 wallets">
            <h4 class="cent">صفحه ای پیدا نشد</h4>
          </b-card-body>

      </b-card><br>
      <div style="clear:both"></div><br>

      <b-card id="form" no-body class="col-12">
          <b-card-header class="row no-gutters align-items-center cent">
          </b-card-header>
          <b-card-body class="py-3 wallets">
            <form @submit.prevent="submit()" enctype="multipart/form-data">
              <input type="text" v-model="title" class="form-control" placeholder="تیتر"><br>
              <b-textarea v-model="text" placeholder="متن پیام" rows="8"></b-textarea><br>
              <input type="submit" class="btn btn-dark" value="ارسال" style="float:left">
            </form>
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
    this.getp()
  },
  data: () => ({
    postid: '',
    requests: [],
    pages:[],
    tickets: [],
    title: '',
    text: '',
    minitext: ''
  }),
  forumPath: [
    { text: 'کیف ها', active: true }
  ],
  methods: {
    goto () {
        document.querySelector(`#form`).scrollIntoView({ behavior: 'smooth' })
    },
    checkadmin (){
      if (!this.$store.state.isAdmin){
            this.$swal.fire({
              title: 'توجه',
              text: 'شما به این بخش دسترسی ندارید',
              icon: 'warning',
              showCancelButton: true,
              confirmButtonColor: '#3085d6',
              cancelButtonColor: '#d33',
              confirmButtonText: 'ورود ادمین',
              cancelButtonText: 'بازگشت به صفحه اصلی'
            }).then(result => {
              if (result.isConfirmed) {
                const toPath = this.$route.go || '/adminpanel/login'
                this.$router.push(toPath)
              }else {
                const toPath = this.$route.query.to || '/'
                this.$router.push(toPath)
              }
            })
      }
    },
    async getp () {
      await axios
        .get(`adminpanel/details`)
        .then(response => {
          this.pages = response.data
        })
    },
    async delet (id) {
      await axios
        .delete(`adminpanel/bottomsticker/${id}`)
        .then(response => {
          this.pages = response.data
        })
        setTimeout(() => {
            this.getp()
          }, 200)
    },
    edit (id, text, title, minitext) {
      this.postid = id
      this.text = text
      this.title = title
      this.goto()
    },
    async submit () {
      if ( this.postid ){
        const formdata = new FormData()
        formdata.append('id' , this.postid)
        formdata.append('text' , this.text)
        formdata.append('title' , this.title)
      await axios
        .put(`adminpanel/details` , formdata)
        .then(response => {
          setTimeout(() => {
            this.getp()
          }, 2000)
        })
      }else{
        const formdata = new FormData()
        formdata.append('text' , this.text)
        formdata.append('title' , this.title)
        formdata.append('position' , 'details')
      await axios
        .post(`adminpanel/details` , formdata)
        .then(response => {
          setTimeout(() => {
            this.getp()
          }, 2000)
        })
      }
      this.postid = ''
      this.text = ''
      this.title = ''
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
.left{
  float: left;
}
</style>
