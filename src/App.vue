<template>
  <div>
    
    <div id="app" >
      
      <router-view :key="$route.fullPath"/>
      
      <div style="border-radius:20px" class="chat-box">
      <chat/>
    </div>
    </div>
  </div>
</template>

<style src="./style.scss" lang="scss"></style>

<script>
import chat from './components/pages/chats.vue'
import login from './views/Pages/Login.vue'
import _themeSettings from './vendor/libs/theme-settings/theme-settings'
import themeSettings from '@/vendor/libs/theme-settings/theme-settings.js'

import axios from 'axios'
export default {
  components: {
    chat,
    login
  },
  name: 'app',
  metaInfo: {
    title: 'Index',
    titleTemplate: '%s - Appwork'
  },
  beforeCreate(){
    themeSettings.setTheme('air')
    if(localStorage.getItem('themeSettingsRtl') === 'true'){
    }
    else{
      localStorage.setItem('themeSettingsRtl', true)
      window.location.reload()
    }

    document.body.classList.remove('app-loading')
    this.$store.commit('initializeStore')
    const token = this.$store.state.token
    if (token) {
      axios.defaults.headers.common.Authorization = 'Token ' + token
      this.$store.state.isAuthenticated = true
    } else {
      axios.defaults.headers.common.Authorization = ''
    }
  },
  updated () {
    setTimeout(() => document.body.classList.remove('app-loading'), 1)
  }
}
</script>
<style lang="scss">
@font-face {
    font-family: 'Yekan';
    src: url('https://cdn.fontcdn.ir/Font/Persian/Yekan/Yekan.eot');
    src: url('https://cdn.fontcdn.ir/Font/Persian/Yekan/Yekan.eot?#iefix') format('embedded-opentype'),
		 url('https://cdn.fontcdn.ir/Font/Persian/Yekan/Yekan.woff') format('woff'),
		 url('https://cdn.fontcdn.ir/Font/Persian/Yekan/Yekan.ttf') format('truetype');
    font-weight: normal;
}
@font-face {
    font-family: 'Yekan';
    src: url('https://cdn.fontcdn.ir/Font/Persian/Yekan/Yekan-Bold.eot');
    src: url('https://cdn.fontcdn.ir/Font/Persian/Yekan/Yekan-Bold.eot?#iefix') format('embedded-opentype'),
		 url('https://cdn.fontcdn.ir/Font/Persian/Yekan/Yekan-Bold.woff') format('woff'),
		 url('https://cdn.fontcdn.ir/Font/Persian/Yekan/Yekan-Bold.ttf') format('truetype');
    font-weight: bold;
}
.vm--modal{
  left:0!important
}
.swal2-header{
  margin-bottom: 70px;
}
.theme-settings-open-btn{
  display: none!important
}
body{
  font-family: 'Yekan'!important;
  direction: rtl!important;
  text-align: right;
}
a , h1 ,h2 ,h3 ,h4 ,h5 ,h6 ,span, p{
  color:#888
}
.arscard{
  background-color: #ffff;
}
.chat-btn{
  position:fixed;left:20px;bottom:20px;width:80px;height:80px;background:#ffffff;border-radius:50%;
}
.chat-box{
  position:fixed;
  left:1%;
  bottom:3%;
  width:25%;
  border-radius: 5%;
  z-index: 1;
}
.chat-btn:hover{
  cursor: pointer;
}
.badge-secondary{background-color:#8897aa;color:#fff}.badge-secondary[href]:focus,.badge-secondary[href]:hover{background-color:#818fa2;color:#fff;text-decoration:none}.btn .badge-secondary{background:#8897aa!important;border-color:#8897aa!important;color:#fff!important}.badge-outline-secondary{background-color:transparent;box-shadow:inset 0 0 0 1px #8897aa;color:#8897aa}.badge-outline-secondary[href]:focus,.badge-outline-secondary[href]:hover{color:#8897aa;text-decoration:none}.btn .badge-outline-secondary{background-color:transparent!important;box-shadow:inset 0 0 0 1px #8897aa!important;color:#8897aa!important}.badge-success{background-color:#02bc77;color:#fff}.badge-success[href]:focus,.badge-success[href]:hover{background-color:#02b371;color:#fff;text-decoration:none}.btn .badge-success{background:#02bc77!important;border-color:#02bc77!important;color:#fff!important}.badge-outline-success{background-color:transparent;box-shadow:inset 0 0 0 1px #02bc77;color:#02bc77}.badge-outline-success[href]:focus,.badge-outline-success[href]:hover{color:#02bc77;text-decoration:none}.btn .badge-outline-success{background-color:transparent!important;box-shadow:inset 0 0 0 1px #02bc77!important;color:#02bc77!important}.badge-info{background-color:#28c3d7;color:#fff}.badge-info[href]:focus,.badge-info[href]:hover{background-color:#26b9cc;color:#fff;text-decoration:none}.btn .badge-info{background:#28c3d7!important;border-color:#28c3d7!important;color:#fff!important}.badge-outline-info{background-color:transparent;box-shadow:inset 0 0 0 1px #28c3d7;color:#28c3d7}.badge-outline-info[href]:focus,.badge-outline-info[href]:hover{color:#28c3d7;text-decoration:none}.btn .badge-outline-info{background-color:transparent!important;box-shadow:inset 0 0 0 1px #28c3d7!important;color:#28c3d7!important}.badge-warning{background-color:#ffd950;color:#665720}.badge-warning[href]:focus,.badge-warning[href]:hover{background-color:#f2ce4c;color:#665720;text-decoration:none}.btn .badge-warning{background:#ffd950!important;border-color:#ffd950!important;color:#665720!important}.badge-outline-warning{background-color:transparent;box-shadow:inset 0 0 0 1px #ffd950;color:#ffd950}.badge-outline-warning[href]:focus,.badge-outline-warning[href]:hover{color:#ffd950;text-decoration:none}.btn .badge-outline-warning{background-color:transparent!important;box-shadow:inset 0 0 0 1px #ffd950!important;color:#ffd950!important}.badge-danger{background-color:#d9534f;color:#fff}.badge-danger[href]:focus,.badge-danger[href]:hover{background-color:#ce4f4b;color:#fff;text-decoration:none}.btn .badge-danger{background:#d9534f!important;border-color:#d9534f!important;color:#fff!important}.badge-outline-danger{background-color:transparent;box-shadow:inset 0 0 0 1px #d9534f;color:#d9534f}.badge-outline-danger[href]:focus,.badge-outline-danger[href]:hover{color:#d9534f;text-decoration:none}.btn .badge-outline-danger{background-color:transparent!important;box-shadow:inset 0 0 0 1px #d9534f!important;color:#d9534f!important}.badge-dark{background-color:#fff;color:#666}.badge-dark[href]:focus,.badge-dark[href]:hover{background-color:#f2f2f2;color:#666;text-decoration:none}.btn .badge-dark{background:#fff!important;border-color:#fff!important;color:#666!important}.badge-outline-dark{background-color:transparent;box-shadow:inset 0 0 0 1px #fff;color:#fff}.badge-outline-dark[href]:focus,.badge-outline-dark[href]:hover{color:#fff;text-decoration:none}.btn .badge-outline-dark{background-color:transparent!important;box-shadow:inset 0 0 0 1px #fff!important;color:#fff!important}.badge-default{background-color:hsla(0,0%,100%,.1);color:#fff}.badge-default[href]:focus,.badge-default[href]:hover{background-color:hsla(0,0%,100%,.13);color:#fff;text-decoration:none}.btn .badge-default{background:hsla(0,0%,100%,.1)!important;border-color:hsla(0,0%,100%,.1)!important;color:#fff!important}.badge-outline-default{background-color:transparent;box-shadow:inset 0 0 0 1px hsla(0,0%,100%,.1);color:#fff}.badge-outline-default[href]:focus,.badge-outline-default[href]:hover{color:#fff;text-decoration:none}.btn .badge-outline-default{background-color:transparent!important;box-shadow:inset 0 0 0 1px hsla(0,0%,100%,.1)!important;color:#fff!important}.badge.badge-dot{display:inline-block;background: blue;margin:0;padding:0;width:.7em;height:.7em;border-radius:50%;vertical-align:middle}.badge.indicator{position:absolute;top:auto;display:inline-block;margin:0;-webkit-transform:translate(-50%,25%);transform:translate(-50%,25%)}[dir=rtl] .badge.indicator{-webkit-transform:translate(50%,25%);transform:translate(50%,25%)}.badge.indicator:not(.badge-dot){padding:0 .2em;font-size:.6em;line-height:1.2em;-webkit-transform:translate(-50%,-10%);transform:translate(-50%,-10%)}[dir=rtl] .badge.indicator:not(.badge-dot){-webkit-transform:translate(50%,-10%);transform:translate(50%,-10%)}[data-trigger=hover]{outline:0}.dropdown-menu{margin:.125rem 0;box-shadow:0 1px 15px rgba(0,0,0,.2);-webkit-animation:dropdownAnimation .1s;animation:dropdownAnimation .1s}[dir=rtl] .dropdown-menu{text-align:right}.mega-dropdown>.dropdown-menu{left:0!important;right:0!important}.dropdown-menu .list-group-item{border-color:#4d4f54}.mega-dropdown{position:static!important}.dropdown-item{line-height:1.54}.dropdown-menu .badge[class*=" float-"],.dropdown-menu .badge[class^=float-]{position:relative;top:.071em}.dropdown-toggle-hide-arrow>.dropdown-toggle:after,.dropdown-toggle-hide-arrow>.dropdown-toggle:before,.dropdown-toggle.hide-arrow:after,.dropdown-toggle.hide-arrow:before{display:none}.dropdown-menu>li:not(.dropdown-item)>a:not(.dropdown-item){display:block;clear:both;padding:.438rem 1.25rem;width:100%;border:0;background:none;color:#fff;text-align:inherit;white-space:nowrap;font-weight:400;line-height:1.54}.dropdown-menu>li:not(.dropdown-item)>a:not(.dropdown-item):focus,.dropdown-menu>li:not(.dropdown-item)>a:not(.dropdown-item):hover{background-color:hsla(0,0%,100%,.06);color:#fff;text-decoration:none}.dropdown-menu>li:not(.dropdown-item).active>a:not(.dropdown-item),.dropdown-menu>li:not(.dropdown-item)>a:not(.dropdown-item):active{background-color:#6610f2;color:#fff;text-decoration:none}.dropdown-menu>li:not(.dropdown-item).disabled>a:not(.dropdown-item){background-color:transparent;color:#66696d}.dropleft .dropdown-toggle:before,.dropright .dropdown-toggle:after{vertical-align:middle}[dir=rtl] .dropdown-toggle:after{margin-right:.5em;margin-left:0}[dir=rtl] .dropleft .dropdown-toggle:before,[dir=rtl] .dropright .dropdown-toggle:after{display:none}[dir=rtl] .dropleft .dropdown-toggle:after{content:"";display:inline-block;margin-right:.5em;margin-left:0;margin-top:-.21em;width:.42em;height:.42em;border:1px solid;border-top:0;border-right:0;-webkit-transform:rotate(45deg);transform:rotate(45deg)}[dir=rtl] .dropright .dropdown-toggle:before{content:"";display:inline-block;margin-right:0;margin-left:.5em;vertical-align:middle;margin-top:-.21em;width:.42em;height:.42em;border:1px solid;border-top:0;border-left:0;-webkit-transform:rotate(-45deg);transform:rotate(-45deg)}.dropdown-toggle-split:after,.dropdown-toggle-split:before{margin-right:0!important;margin-left:0!important}.dropdown-menu .dropdown-toggle{position:relative}.dropdown-menu .dropdown-toggle:after{display:none}.dropdown-menu .dropdown-toggle>.dropdown-item,.dropdown-menu .dropdown-toggle>li[role=presentation]>.dropdown-item{position:relative;cursor:default}@media (max-width:767px){.dropdown-menu .dropdown-menu{position:static;display:block;margin:0;padding-left:1.25rem;width:100%;border-width:0;border-radius:0;box-shadow:none}[dir=rtl] .dropdown-menu .dropdown-menu{padding-right:1.25rem;padding-left:0}}@media (min-width:768px){.dropdown-menu .dropdown-toggle>.dropdown-item:after,.dropdown-menu .dropdown-toggle>li[role=presentation]>.dropdown-item:after{content:"";position:absolute;top:50%;right:.625rem;display:block;width:.375rem;height:.375rem;border:1px solid #a8a9ab;border-top:0;border-left:0;-webkit-transform:rotate(-45deg) translateY(-50%);transform:rotate(-45deg) translateY(-50%)}[dir=rtl] .dropdown-menu .dropdown-toggle>.dropdown-item:after,[dir=rtl] .dropdown-menu .dropdown-toggle>li[role=presentation]>.dropdown-item:after{right:auto;left:.625rem;-webkit-transform:rotate(45deg) translateY(-50%) scaleX(-1);transform:rotate(45deg) translateY(-50%) scaleX(-1)}.dropdown-menu .dropdown-toggle:hover>.dropdown-item:not(.disabled),.dropdown-menu .dropdown-toggle:hover>li[role=presentation]>.dropdown-item:not(.disabled){background:hsla(0,0%,100%,.06);color:#fff}.dropdown-menu .dropdown-toggle:hover>.dropdown-item:not(.disabled)+.dropdown-menu,.dropdown-menu .dropdown-toggle:hover>li[role=presentation]+.dropdown-menu{display:block}.dropdown-menu .dropdown-menu{top:0;left:100%}.dropdown-menu-right .dropdown-menu{right:100%;left:auto}}[dir=rtl] .nav{padding-right:0}.nav-link{line-height:1.54}.nav-link.disabled{border-color:transparent!important;background:transparent!important;color:#66696d!important}.nav .nav-item,.nav .nav-link,.tab-pane,.tab-pane .card-body{outline:none!important}.nav-pills .nav-link:not(.active),.nav-tabs .nav-link:not(.active){color:#a8a9ab}.nav-pills .nav-link:not(.active):focus,.nav-pills .nav-link:not(.active):hover,.nav-tabs .nav-link:not(.active):focus,.nav-tabs .nav-link:not(.active):hover{color:#fff}.nav-pills:not(.nav-fill):not(.nav-justified) .nav-link,.nav-tabs:not(.nav-fill):not(.nav-justified) .nav-link{margin-right:.125rem}[dir=rtl] .nav-pills:not(.nav-fill):not(.nav-justified) .nav-link,[dir=rtl] .nav-tabs:not(.nav-fill):not(.nav-justified) .nav-link{margin-right:0;margin-left:.125rem}.nav-pills .nav-link .badge,.nav-tabs .nav-link .badge{position:relative;top:-1px}

.navbar{
    font-family: 'calibri';
    font-weight:bold
  }
input{
  font-family: 'arial';
}
.transm .card-body {
  padding:5px;
  width:100%
}
.transm .card {
  padding-top: 15px;
  margin-bottom: 25px;
  background-image: linear-gradient(to bottom right, white, #efefef);
}
::-webkit-scrollbar {
  width: 6px;
}

/* Track */
::-webkit-scrollbar-track {
  background: #f1f1f1; 
}
 
/* Handle */
::-webkit-scrollbar-thumb {
  background: #888; 
  border-radius:3px;
}


/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: #555; 
}
.d-inline-block {
  width:90%!important;
  margin-right:5%!important
}
.slider-horizontal{
  width:90%!important;
  margin-right:5%!important
}
.slider-handle{
  background-color: #888!important;
  background-image: -webkit-gradient(linear,left top,left bottom,from(#888),to(#333))!important;
}
@media only screen and (max-width: 1024px) {
.chat-box{
  position:fixed;
  left:0!important;
  bottom:0%;
  width:35%;
  border-radius: 5%;
  z-index: 1;
}
}
@media only screen and (max-width: 600px) {
.chat-box{
  position:fixed;
  left:0!important;
  bottom:0%;
  width:100%;
  border-radius: 5%;
  z-index: 1;
}
}

</style>