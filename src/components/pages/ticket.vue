<template>
  <div>


      <b-card no-body class="col-12">

        <b-card-header class="row no-gutters align-items-center">
          <div class="col-4 cent">نام کاربری</div>
          <div class="col-4 cent">موضوع</div>
          <div class="col-4 cent">زمان ثبت</div>
        </b-card-header>

        <div v-for="section in requests" :key="section.title">
          <b-card-body class="py-3 wallets">

              <router-link :to="'ticket/' + section.id" class="row no-gutters align-items-center">
                <div class="col-4 cent">{{section.get_user}}</div>
                <div class="col-4 cent">{{section.title}}</div>
                <div class="col-4 cent">{{section.get_age}}</div>
              </router-link>
          </b-card-body>
        </div>
          <b-card-body v-if="!requests[0]" class="py-3 wallets">
            <h4 class="cent">تیکتی پیدا نشد</h4>
          </b-card-body>

      </b-card>

      <div v-for="section in tickets" :key="section.title">
      <b-card no-body class="col-12">
          <b-card-header class="row no-gutters align-items-center">
            <div class="col-4 right"> {{section.get_user}}</div>
            <div class="col-4 cent"></div>
            <div class="col-4 cent">{{section.get_age}} </div>
          </b-card-header>
          <b-card-body class="py-3 wallets">

              <router-link :to="'ticket/' + section.id" class="row no-gutters align-items-center">
                <h3>{{section.title}}</h3>
                <h5 style="width:100%">{{section.text}}</h5><br><br><br>
                <div style="max-width:50%; margin:auto">
                <img v-if="section.pic" :src="section.get_pic" style="width:100%">
                </div>
              </router-link>
          </b-card-body>
      </b-card>
      </div>


      <b-card no-body class="col-12">
          <b-card-header class="row no-gutters align-items-center cent">
            پاسخ به تیکت
          </b-card-header>
          <b-card-body class="py-3 wallets">
            <form @submit.prevent="submit()">
              <b-textarea v-model="text" placeholder="متن پیام" rows="8"></b-textarea><br>
              <input id="file" type="file"><br><br>
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
    this.gets()
  },
  data: () => ({
    requests: [],
    tickets: [],
    text: ''
  }),
  forumPath: [
    { text: 'کیف ها', active: true }
  ],
  methods: {
    async gets () {
      await axios
        .post(`adminpanel/subject/${this.$route.params.id}`)
        .then(response => {
          this.requests = response.data
          this.gett()
        })
    },
    async gett () {
      await axios
        .get(`adminpanel/ticket/${this.$route.params.id}`)
        .then(response => {
          this.tickets = response.data
        })
    },
    async submit () {
      await axios
        .post(`adminpanel/ticket` , {subid : this.$route.params.id , text : this.text , pic : document.getElementById('file').file})
        .then(response => {
          setTimeout(() => {
            this.gett()
          }, 2000)
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
.left{
  float: left;
}
</style>
