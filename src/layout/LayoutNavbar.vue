<template>
  <b-navbar toggleable="lg" :variant="getLayoutNavbarBg()" class="layout-navbar align-items-lg-center container-p-x">

    <!-- Brand demo (see demo.css) -->
    <b-navbar-brand style="width:100%;padding:0 27%; text-align:center" to="/" class="app-brand demo d-lg-none py-0 mr-4">
        <img  src="/img/logo.png" style="width:32px ; height: 32px" alt="">
      <span class="app-brand-text demo font-weight-normal ml-2"><a style="color:rgb(206, 206, 206);font-size:22px; font-weight:bold ; margin-right: 10px">آمیزاکس</a></span>
    </b-navbar-brand>

    <!-- Sidenav toggle (see demo.css) -->
    <b-navbar-nav class="layout-sidenav-toggle d-lg-none align-items-lg-center mr-auto" v-if="sidenavToggle">
      <a class="nav-item nav-link px-0 mr-lg-4" href="javascript:void(0)" @click="toggleSidenav">
        <i class="fas fa-angle-double-left text-large align-middle" />
      </a>
    </b-navbar-nav>

    <b-navbar-toggle target="app-layout-navbar"></b-navbar-toggle>

    <b-collapse is-nav id="app-layout-navbar">
      <!-- Divider -->
      <hr class="d-lg-none w-100 my-2">


      <b-navbar-nav @click="seen()" class="align-items-lg-center ml-auto">
        <b-nav-item>
          <template >
            <div v-if="!darkness">
            <i  class="ion ion-md-moon navbar-icon align-middle" style="margin-left:12px ; margin-right:12px"  @click="darkswitch"></i>
            <span class="d-lg-none align-middle">&nbsp; Dark Mode</span>
            </div>
            <div v-else>
            <i class="ion ion-md-sunny navbar-icon align-middle" style="margin-left:12px ; margin-right:12px "  @click="darkswitch"></i>
            <span class="d-lg-none align-middle">&nbsp; Light Mode</span>
            </div>
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

          <b-dd-item href="/user"><i class="ion ion-ios-person text-lightest"></i> &nbsp; اطلاعات کاربری</b-dd-item>
          <b-dd-item href="/user-level"><i class="ion ion-ios-mail text-lightest"></i> &nbsp; تایید هویت</b-dd-item>
          <b-dd-item href="/user-security"><i class="ion ion-md-settings text-lightest"></i> &nbsp; امنیت</b-dd-item>
          <b-dd-divider />
          <b-dd-item href="/logout"><i class="ion ion-ios-log-out text-danger"></i> &nbsp; خروج</b-dd-item>
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
      tunseen: [],
      nunseen: []
    }
  },
  mounted(){
    this.pre()
  },
  computed:{
    darkness (){
      if (localStorage.getItem('themeSettingsStyle') === 'material'){
        return true
      }else{
        return false
      }
    }
  },
  methods: {
    darkswitch(){
      if(localStorage.getItem('themeSettingsStyle') === 'material'){
        themeSettings.setStyle('light')
      }else{
        themeSettings.setStyle('material')
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
