<template>
  <b-navbar style="position:fixed;width:100%" toggleable="lg" :variant="getLayoutNavbarBg()" class="layout-navbar align-items-lg-center container-p-x">
    
    <!-- Brand demo (see demo.css) -->
    <b-navbar-brand to="/" class="app-brand demo py-0 mr-4 pc">
        <img  src="/img/logo.png" style="width:32px ; height: 32px" alt="">
      <span class="app-brand-text demo font-weight-normal ml-2">AMIZAX</span>
    </b-navbar-brand>
    <b-navbar-brand to="/" class="app-brand demo py-0  mob">
        <img  src="/img/logo.png" style="width:32px ; height: 32px" alt="">
      <span class="app-brand-text demo font-weight-normal ml-2">AMIZAX</span>
    </b-navbar-brand>

    <b-navbar-toggle style="position:absolute; top:5px ; right:5px" target="app-layout-navbar2"></b-navbar-toggle>

    <b-collapse is-nav id="app-layout-navbar2">
      <!-- Divider -->
      <hr class="d-lg-none w-100 my-2">
      <b-navbar-nav style="text-align:center"  class="align-items-lg-center ml-lg-auto" >

           <b-nav-item to="/news">
               <span class="nav-link-inner--text" style="color:#cecece"> اخبار </span>
           </b-nav-item>
           <b-nav-item to="/margin-trade/BTCUSDT">
               <span class="nav-link-inner--text" style="color:#cecece"> بازار مارجین </span>
           </b-nav-item>
           <b-nav-item to="/perpetual-trade/BTCUSDT">
               <span class="nav-link-inner--text" style="color:#cecece">بازار پرپشوال</span>
           </b-nav-item>
           <b-nav-item to="/wallets">
               <span class="nav-link-inner--text" style="color:#cecece">کیف های من </span>
           </b-nav-item>
           <b-nav-item to="/aboutus">
               <span class="nav-link-inner--text" style="color:#cecece">  درباره ما </span>
           </b-nav-item>
       </b-navbar-nav>
        <b-navbar-nav style="margin-right"  class="align-items-lg-center mr-lg-auto">
          <b-nav-item v-if="this.$store.state.isAuthenticated" to="/dashboard">
               <span class="nav-link-inner--text btn btn-dark" style=" padding: 7px 15px"> داشبورد </span>
           </b-nav-item>
           
       </b-navbar-nav>

    </b-collapse>
    

    <b-navbar-toggle style="position:absolute; top:5px ; left:5px" target="app-layout-navbar"></b-navbar-toggle>

    <b-collapse is-nav id="app-layout-navbar">
      <!-- Divider -->
      <hr class="d-lg-none w-100 my-2">


      <b-navbar-nav @click="seen()" class="align-items-lg-center ml-auto">
        <b-nav-item>
          <template >
            <i v-if="!darkness" class="ion ion-md-moon navbar-icon align-middle" style="margin-left:12px ; margin-right:12px"  @click="darkswitch"></i>
            <i v-else class="ion ion-md-sunny navbar-icon align-middle" style="margin-left:12px ; margin-right:12px "  @click="darkswitch"></i>
          </template>
        </b-nav-item>
        <b-nav-item-dropdown v-if="$store.state.isAuthenticated" no-caret :right="!isRtlMode" class="demo-navbar-notifications mr-lg-3">
          <template slot="button-content" @click="seen()">
            <i @click="seen()" class="ion ion-md-notifications-outline navbar-icon align-middle"></i>
            <span v-if="nunseen" class="badge badge-primary badge-dot indicator"></span>
            <span class="d-lg-none align-middle">&nbsp; Notifications</span>
          </template>

          <b-list-group style="max-height:480px ; overflow-y:auto" flush>
            <b-list-group-item v-for="(item, idx) in notification" v-bind:key="idx + 'n'" href="javascript:void(0)" class="media d-flex align-items-center">
              <div class="ui-icon ui-icon-sm ion ion-md-notifications-outline bg-secondary border-0 text-white"></div>
              <div class="media-body line-height-condenced ml-3">
                <div class="text-body" style="font-weight:normal; font-family:'yekan'; font-size: 16">{{item.title}}</div>
                <div class="text-light small mt-1">
                  {{item.text}}
                </div>
                <div class="text-light small mt-1">{{item.get_age}}</div>
              </div>
            </b-list-group-item>
          </b-list-group>

          <a v-if="!notification.length" href="javascript:void(0)" class="d-block text-center text-light small p-2 my-1">No Notification Yet</a>
        </b-nav-item-dropdown>

        <b-nav-item-dropdown @click="read()" v-if="$store.state.isAuthenticated" no-caret :right="!isRtlMode" class="demo-navbar-messages mr-lg-3">
          <template slot="button-content" @click="read()">
            <i @click="read()" class="ion ion-ios-mail navbar-icon align-middle"></i>
            <span v-if="tunseen" class="badge badge-primary badge-dot indicator"></span>
            <span class="d-lg-none align-middle">&nbsp; Messages</span>
          </template>

          <b-list-group flush>
            <b-list-group-item v-for="(item, idx) in tickets" v-bind:key="idx + 't'" href="javascript:void(0)" class="media d-flex align-items-center">
              <i class="ion ion-ios-mail navbar-icon align-middle"></i>
              <div class="media-body ml-3">
                <div class="text-body line-height-condenced">{{item.title}}</div>
                <div class="text-light small mt-1">
                  {{item.text}}
                </div><br>
                <div class="text-light small mt-1">
                  {{item.get_age}}
                </div>
              </div>
            </b-list-group-item>
            <a v-if="!tickets.length" href="javascript:void(0)" class="text-center text-light font-weight-bold p-3">No Tickets Yet</a>
          </b-list-group>
            <a href="/ticketadd" style="margin:0!important" class="bg-primary text-white d-block text-center small p-2 my-1">New Ticket</a>
        </b-nav-item-dropdown>

        <!-- Divider -->
        <div class="nav-item d-none d-lg-block text-big font-weight-light line-height-1 opacity-25 mr-3 ml-1">|</div>

        <b-nav-item-dropdown v-if="$store.state.isAuthenticated" :right="!isRtlMode" class="demo-navbar-user">
          <template slot="button-content">
            <span class="d-inline-flex flex-lg-row-reverse align-items-center align-middle">
              <i style="font-size:32px" class="ion ion-ios-person text-light"></i>
            </span>
          </template>

          <b-dd-item><i class="ion ion-ios-person text-lightest"></i> &nbsp; My profile</b-dd-item>
          <b-dd-item><i class="ion ion-ios-mail text-lightest"></i> &nbsp; Messages</b-dd-item>
          <b-dd-item><i class="ion ion-md-settings text-lightest"></i> &nbsp; Account settings</b-dd-item>
          <b-dd-divider />
          <b-dd-item><i class="ion ion-ios-log-out text-danger"></i> &nbsp; Log Out</b-dd-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
import axios from 'axios'
import themeSettings from '@/vendor/libs/theme-settings/theme-settings.js'

export default {
  name: 'app-layout-navbar',

  props: {
    sidenavToggle: {
      type: Boolean,
      default: true
    }
  },
  data(){
    return {
      notification: [],
      tickets: [],
    }
  },
  mounted(){
    this.pre()
  },
  computed:{
    darkness (){
      if (localStorage.getItem('themeSettingsStyle') === 'dark'){
        return true
      }else{
        return false
      }
    }
  },
  methods: {
    darkswitch(){
      if(localStorage.getItem('themeSettingsStyle') === 'dark'){
        themeSettings.setStyle('light')
      }else{
        themeSettings.setStyle('dark')
      }
    },
    pre(){
      if(this.$store.state.isAuthenticated){
        this.get_notifications()
        this.get_tickets()
      }
    },
    async get_notifications () {
      await axios
        .get('/notifications')
        .then(response => {
          this.notification = response.data.reverse()
          var i = 0
          for (var item in response.data) {
            if (!response.data[i].seen) {
              this.nunseen = true
            }
            item.reverse()
            i++
          }
        })
        .catch(() => {
        })
    },
    async get_tickets () {
      await axios
        .get('/subject')
        .then(response => {
          this.tickets = response.data.reverse()
          var i = 0
          for (var item in response.data) {
            if (!response.data[i].read) {
              this.tunseen = true
            }
            item.reverse()
            i++
          }
        })
        .catch(() => {
        })
    },
    async read () {
      await axios
        .put('/subject')
        .then(response => {
          this.tunseen = false
        })
        .catch(() => {
        })
    },
    async seen () {
      await axios
        .post('/notifications')
        .then(response => {
          this.nunseen = false
        })
        .catch(() => {
        })
    },
    toggleSidenav () {
      this.layoutHelpers.toggleCollapsed()
    },

    getLayoutNavbarBg () {
      return this.layoutNavbarBg
    }
  }
}
</script>
<style>
.mob{
  display: none;
}
.pc{
  display: flex;
}
@media screen and (max-width: 768px) {
.mob{
  display: flex;
  margin: auto!important;
}
.mob a{
  margin: 0!important;
}

.pc{
  display: none;
}
}
</style>