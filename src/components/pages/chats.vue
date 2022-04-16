<template>
  <div class="container" style="background:none">
    <div class="row">
      <div>
        <div hidden class="card-footer text-muted" style=";z-index:1" id="emailadd">
              <form @submit.prevent="startChatSession">
                  <div class="row">
                      <div class="col-sm-12">
                      <input v-model="emailadd" required type="text" placeholder="آدرس ایمیل" />
                      </div><br>
                      <div class="col-sm-12">
                      <button class="btn btn-dark" style="width:100%">شروع چت</button>
                      </div>
                  </div>
              </form>
            </div>

        <div v-if="sessionStarted && !hide" id="chat-container" style="height:520px" class="card">
            
          <div class="card-header text-white text-center  subtle-blue-gradient" style="height:70px">
            پشتیبانی آنلاین<br><br>
            {{uri}}
            <button class="btn btn-danger" style="position:absolute;top:5px;right:5px;padding:0 7px;border-radius:50%!important" @click="hide = true">X</button>
          </div>
          

          <div class="card-body" style="height:200px">
            <div class="container chat-body" style=";width:100%;height:300px">
              <div class="row chat-section">
                <template>
                  <div class="col-sm-2">
                    <span  style="background:#007bff;font:25px 'arial';padding:10px;border-radius:50%;color:white"> {{'a'.toUpperCase()}} </span>
                  </div>
                  <div class="col-sm-7">
                    <span class="card-text speech-bubble speech-bubble-peer">
                      سلام چطور میتونیم کمکتون کنیم؟
                    </span>
                  </div>
                </template>
              </div>
              <div v-for="message in messages" :key="message.id" class="row chat-section">
                <template v-if="username === message.user.username | username === message.email">
                  <div style="width:80%">
                    <span style="width:70%" class="card-text speech-bubble speech-bubble-user float-right text-white subtle-blue-gradient">
                      {{ message.message }}
                    </span>
                  </div>
                  <div style="width:5%">
                  </div>
                </template>
                <template v-else>
                  <div class="col-sm-2">
                  </div>
                  <div class="col-sm-7">
                    <span class="card-text speech-bubble speech-bubble-peer">
                      {{ message.message }}
                    </span>
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
          <div v-if="!this.$store.state.isAdmin" class="chat-btn">
            <span  v-if="notread" style="width:22px;height:22px;border-radius:50%; background:red; position:absolute ;text-align:center; color:white ; font-family:'arial'">{{notread}}</span>
            <img @click="startChatSession" style="margin:10px;width:60px;height:60px" src="https://icon-library.com/images/chat-icon-png/chat-icon-png-22.jpg">
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
      notread:0,
      sessionStarted: false, messages: {}, message: '',uri: '',hide: this.$store.state.hide
    }
  },
  mounted () {
    this.hider()
  },

  created () {
      this.get_user ()
  },
  

  methods: {
      async get_user () {
      if(this.$store.state.isAuthenticated){
      await axios
        .get('chats/user' , {email : localStorage.getItem('email')})
        .then(response => {
          this.username = response.data.username
          this.uri = response.data.uri
          if (response.data.uri) {
            this.joinChatSession()
            this.sessionStarted = true
          }
        })
      }
      },
      hider () {
          this.$store.state.hide = true
          this.hide = this.$store.state.hide
      },
    async startChatSession () {
      document.querySelector('#emailadd').hidden = true
        if (this.sessionStarted){
            this.$store.state.hide = false
            this.chatseen()
            this.hide = this.$store.state.hide
            this.fetchChatSessionHistory()
        }
        else{
          if(this.$store.state.isAuthenticated){
            await axios
              .post('chats/')
              .then(data => data.data)
              .then(data => {
              this.sessionStarted = true
              this.uri = data.uri
            })
            .catch((response) => {
            })
          }else{
            if(localStorage.getItem('email')){
              await axios
              .post('chats/' , {email : localStorage.getItem('email')})
              .then(data => data.data)
              .then(data => {
              this.sessionStarted = true
              this.uri = data.uri
            })
            .catch((response) => {
            })
            }else if(this.emailadd){
              localStorage.setItem('email' , this.emailadd)
              this.startChatSession()
            }else{
              document.querySelector('#emailadd').hidden = false
            }
          }
          
        }
    },
    async postMessage (event) {
      if (this.$store.state.isAuthenticated){
        const data = {message: this.message}
        await axios
        .post(`chats/${this.uri}/messages/`, data) 
        .then(data => {
        this.messages.push(data.data)
        this.message = '' // clear the message after sending
      })
      .catch((response) => {
      })
      }else{
        alert(localStorage.getItem('email'))
        const data = {message: this.message , email : localStorage.getItem('email')}
        await axios
        .post(`chats/${this.uri}/messages/`, data) 
        .then(data => {
        this.messages.push(data.data)
        this.message = '' // clear the message after sending
      })
      .catch((response) => {
      })
      }
      
    },
    async chatseen (event) {
        await axios
        .get(`chats/${this.uri}/seen/`) 
        .then(data => {
          this.notread = 0
      })
      .catch((response) => {
      })
    },
    async joinChatSession () {
      await axios
      .patch(`chats/${this.uri}/`, {username: this.username})
        .then(data => {
            var user = ''
            if(data.data.members){
              for (var item of data.data.members) {
                  if (item.username === this.username){
                      user = item.username   
                  }
              }
            }
              

          if (user) {
            // The user belongs/has joined the session
            this.sessionStarted = true
            this.fetchChatSessionHistory()
          }
        })
    },

    async fetchChatSessionHistory () {
        await axios
      .get(`chats/${this.uri}/messages/`) 
      .then(data => {
        this.messages = data.data.messages
        var tempnotread = 0
        this.notread = data.data.notseen
        setTimeout(() => {
          this.fetchChatSessionHistory()
        }, 20000)
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
  color: #444444;
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