<template>
  <div class="container" style="background:none">
    <h1 v-if="messages[0]" style="text-align:center">{{messages[0].user.username}}</h1>
    <div class="row">
      <div style="width:90%;margin:auto">

        <div v-if="sessionStarted" id="chat-container" style="height:520px;width:100%" class="card">
            
          <div class="card-header text-white text-center  subtle-blue-gradient" style="height:70px">
            پشتیبانی آنلاین<br><br>
          </div>
          
          <div class="card-body" style="height:200px; width:100%">
            <div class="container chat-body" style=";width:100%;padding:5%;height:300px">
              <div v-for="message in messages" :key="message.id" class="row chat-section" style="padding:5%">
                <template v-if="username === message.user.username">
                  <div class="text-white; subtle-blue-gradient" style="padding-top:14px;background:#00aaff;border-radius:50%;width:50px;height:50px ; float:right ; text-align:center">
                    <span  style="text-align:center;color:white;font-family:'Yekan'">
                      شما</span>
                  </div>
                  <div style="width:75%; float:left">
                    <span style="float:left!important; width:95%" class="card-text speech-bubble speech-bubble-user float-left text-white subtle-blue-gradient">
                      {{ message.message }}
                    </span>
                  </div>
                </template>
                <template style="direction:ltr!important" v-else>
                  <div style="width:75%; float:right;padding-top:16px">
                    <span style="float:right!important; width:95%" class="card-text speech-bubble speech-bubble-peer float-right text-dark">
                      {{ message.message }}
                    </span>
                  </div>
                  <div class="text-white; subtle-blue-gradient" style="margin-top:14px;padding-top:14px;background:#00aaff;border-radius:50%;width:50px;height:50px ; float:left; text-align:center">
                    <span  style="text-align:center;color:white;font-family:'Yekan'">
                      کاربر</span>
                  </div>
                </template>
              </div>
            </div>
          </div>

          <div class="card-footer text-muted" style=";z-index:1">
            <form @submit.prevent="postMessage">
                <div class="row">
                    <div class="col-sm-12">
                    <input v-model="message" type="text" placeholder="متن پیام ..." />
                    </div><br>
                    <div class="col-sm-12">
                    <button class="btn btn-dark" style="width:100%">Send</button>
                    </div>
                </div>
            </form>
          </div>
        </div>

        <div v-else>
          <div class="chat-btn">
  <img  style="margin:10px;width:60px;height:60px" src="https://icon-library.com/images/chat-icon-png/chat-icon-png-22.jpg">
  </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios'
const $ = window.jQuery

export default {
  data () {
    return {
      sessionStarted: false, messages: {}, message: '',hide: this.$store.state.hide
    }
  },
  mounted () {
    this.chatseen()
  },

  created () {
      this.get_user ()
  },
  

  methods: {
    async chatseen (event) {
      const data = {message: this.message}
        await axios
        .get(`chats/${this.$route.params.uri}/seen/`) 
        .then(data => {
          this.notread = 0
      })
      .catch((response) => {
      })
    },
      async get_user () {
      if(this.$store.state.isAuthenticated){
      await axios
        .get('chats/user')
        .then(response => {
          this.username = response.data.username
          this.uri = response.data.uri
          this.joinChatSession()
          this.sessionStarted = true
        })
      }
      },
    async postMessage (event) {
      const data = {message: this.message}
        await axios
        .post(`chats/${this.$route.params.uri}/adminmessages/`, data) 
        .then(data => {
        this.messages.push(data.data)
        this.message = '' // clear the message after sending
      })
      .catch((response) => {
      })
    },
    joinChatSession () {
            this.sessionStarted = true
            this.fetchChatSessionHistory()
    },

    async fetchChatSessionHistory () {
        await axios
      .get(`chats/${this.$route.params.uri}/messages/`) 
      .then(data => {
        this.messages = data.data.messages
        setTimeout(() => {
          this.fetchChatSessionHistory()
        }, 3000)
      })
    }
  }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}

.btn {
  border-radius: 0 !important;
}

.card-footer input[type="text"] {
  background-color: #ffffff;
  color: #888;
  padding: 7px;
  font-size: 13px;
  border: 2px solid #cccccc;
  width: 100%;
  height: 38px;
}

.card-header a {
  text-decoration: underline;
}

.card-body {
  background-color: #ddd;
}

.chat-body {
  margin-top: -15px;
  margin-bottom: -5px;
  height: 380px;
  overflow-y: auto;
}

.speech-bubble {
  display: inline-block;
  position: relative;
  border-radius: 0.4em;
  padding: 10px;
  background-color: #fff;
  font-size: 14px;
}

.subtle-blue-gradient {
  background: linear-gradient(45deg,#004bff, #007bff);
}

.speech-bubble-user:after {
  content: "";
  position: absolute;
  right: 4px;
  top: 10px;
  width: 0;
  height: 0;
  border: 20px solid transparent;
  border-left-color: #007bff;
  border-right: 0;
  border-top: 0;
  margin-top: -10px;
  margin-right: -20px;
}

.speech-bubble-peer:after {
  content: "";
  position: absolute;
  left: 3px;
  top: 10px;
  width: 0;
  height: 0;
  border: 20px solid transparent;
  border-right-color: #ffffff;
  border-top: 0;
  border-left: 0;
  margin-top: -10px;
  margin-left: -20px;
}

.chat-section:first-child {
  margin-top: 10px;
}

.chat-section {
  margin-top: 15px;
}

.send-section {
  margin-bottom: -20px;
  padding-bottom: 10px;
}
</style>