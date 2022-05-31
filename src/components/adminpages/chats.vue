<template >
  <div >


      <b-card no-body class="col-12">

        <b-card-header class="row no-gutters align-items-center">
          چت های تازه


        </b-card-header>
        <b-input @input="search()" v-model="searchtxt" placeholder="Search ..."></b-input>
          <b-card-body class="py-3 wallets">
            <div class="row no-gutters align-items-center" >
              <div class="col-4 cent">نام کاربری</div>
              <div class="col-4 cent">آی دی چت</div>
              <div class="col-4 cent">خوانده نشده</div>
            </div>
            <hr>
            <router-link :to="'chats/' + item.uri" class="dd row no-gutters align-items-center" v-for="(item,idx) in requests" v-bind:key="idx" style="min-height:70px">

              <div v-if="item.get_user" class="col-4 cent">{{item.get_user}}</div>
              <div v-if="!item.get_user" class="col-4 cent">{{item.email}}</div>
              <div class="col-4 cent">{{item.uri}}</div>
              <div v-if="item.get_seen" class="col-4 cent"> <a   style="margin:-10px;width:22px;height:22px;border-radius:50%; background:red; position:absolute ;text-align:center; color:white ; font-family:'arial'">{{item.get_seen}}</a> </div>
              <div v-if="!item.get_seen" class="col-4 cent"> <a   style="margin:-10px;width:22px;height:22px;border-radius:50%; background:green; position:absolute ;text-align:center; color:white ; font-family:'arial'">{{item.get_seen}}</a> </div>
            </router-link>
          </b-card-body>

      </b-card><br><br>
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
    this.getc()
  },
  data: () => ({
    requests: [],
    requestsback: [],
    searchtxt: '',
  }),
  forumPath: [
    { text: 'کیف ها', active: true }
  ],
  methods: {
    async getc () {
      await axios
        .get('chats/adminchat')
        .then(response => {
          this.requests = response.data
          this.requestsback = response.data
        })
    },
    
    search () {
      this.requests = []
      for (item of this.requestsback){
        if(item.get_user.includes(this.searchtxt)){
          this.requests.push(item)
        }
      }
    }
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
.dd:hover{
  background-color: #888;
  color:white
}
</style>
