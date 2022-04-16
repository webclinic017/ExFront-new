<template>
  <div>
      <b-card no-body class="col-12">
          <b-card-header class="row no-gutters align-items-center cent">
            ایجاد تیکت
          </b-card-header>
          <b-card-body class="py-3 wallets">
            <form @submit.prevent="submit()">
              <b-input v-model="title" placeholder="موضوع"></b-input><br>
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
  },
  data: () => ({
    requests: [],
    tickets: [],
    text: '',
    title: ''
  }),
  forumPath: [
    { text: 'کیف ها', active: true }
  ],
  methods: {
    async submit () {
      await axios
        .put(`/adminpanel/subject` , {username: this.$route.params.id,subid : this.$route.params.id, title: this.title , text : this.text , pic : document.getElementById('file').file})
        .then(response => {
           this.$swal.fire({
              type: 'seccess',
              text: 'با موفقیت ارسال شد',

        })
        .then(()=>{
          const toPath = this.$route.go || '/dashboard'
          this.$router.push(toPath)
        })
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
