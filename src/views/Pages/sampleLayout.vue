<template>
  <div class="main-content " style="width:100% ; position:absolute ; top:0" @scroll="scroll()">
    <base-nav style="width:100%;position:absolute" id="nav"
      :transparent="true"
      menu-classes="justify-content-end"
      class="navbar-horizontal navbar-main navbar-top navbar-dark"
      expand="lg"
    >

     <template style="width:100%">
       <div class="navbar-collapse-header">
         <b-row>
           <b-col cols="6" class="collapse-close">
             <button type="button" class="navbar-toggler" @click="showMenu = false">
               <span></span>
               <span></span>
             </button>
           </b-col>
         </b-row>
       </div>
       <b-navbar-brand to="/">
          <img style="width:40px; height:50px" src="/img/brand/ars.png">
        </b-navbar-brand>
      <b-navbar-nav  class="align-items-lg-center ml-lg-auto" >

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
        <b-navbar-nav style="margin-right:200px"  class="align-items-lg-center mr-lg-auto">
          <b-nav-item v-if="this.$store.state.isAuthenticated" to="/dashboard">
               <span class="nav-link-inner--text btn btn-light" style="background: none; padding: 7px 15px; color: #fff"> داشبورد </span>
           </b-nav-item>
           <b-nav-item v-if="this.$store.state.isAuthenticated" to="/logout">
               <span class="nav-link-inner--text btn btn-light" style="background: none; padding: 7px 15px; color: #fff"> خروج </span>
           </b-nav-item>
           <b-nav-item v-if="!this.$store.state.isAuthenticated" to="/register">
               <span class="nav-link-inner--text btn btn-light" style="background: none; padding: 7px 15px; color: #777"> ثبت نام </span>
           </b-nav-item>
           <b-nav-item v-if="!this.$store.state.isAuthenticated" to="/login" style="float:left">
               <span class="nav-link-inner--text btn btn-light" style="background: none; padding: 7px 15px; color: #777; margin-left:30px"> ورود </span>
           </b-nav-item>
       </b-navbar-nav>
       
     </template>
    </base-nav>

    <div class="main-content">
      <zoom-center-transition
        :duration="pageTransitionDuration"
        mode="out-in"
      >
        <router-view></router-view>
      </zoom-center-transition>
    </div>

  </div>
</template>
<script>
  import { BaseNav } from '@/components/';
  import { ZoomCenterTransition } from 'vue2-transitions';

  export default {
    components: {
      BaseNav,
      ZoomCenterTransition
    },
    props: {
      backgroundColor: {
        type: String,
        default: 'black'
      }
    },
    data() {
      return {
        showMenu: false,
        menuTransitionDuration: 250,
        pageTransitionDuration: 200,
        year: new Date().getFullYear(),
        pageClass: 'login-page'
      };
    },
    computed: {
      title() {
        return `${this.$route.name} Page`;
      }
    },
    mounted () {
      this.scroll()
    },
    methods: {
      scroll () {
      function myFunction() {
        if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
            document.querySelector("#nav").style.position = "fixed";
            document.querySelector("#nav").style.background = "rgb(0,0,0)";
        }
        else {
          document.querySelector("#nav").style.position = "absolute";
          document.querySelector("#nav").style.background = "rgb(0,0,0)";
        }
        setTimeout(() => {
            myFunction()
          }, 500)
        }
        myFunction()
    },
      toggleNavbar() {
        document.body.classList.toggle('nav-open');
        this.showMenu = !this.showMenu;
      },
      closeMenu() {
        document.body.classList.remove('nav-open');
        this.showMenu = false;
      },
      setBackgroundColor() {
        document.body.classList.add('bg-default');
      },
      removeBackgroundColor() {
        document.body.classList.remove('bg-default');
      },
      updateBackground() {
        if (!this.$route.meta.noBodyBackground) {
          this.setBackgroundColor();
        } else {
          this.removeBackgroundColor()
        }
      }
    },
    beforeDestroy() {
      this.removeBackgroundColor();
    },
    beforeRouteUpdate(to, from, next) {
      // Close the mobile menu first then transition to next page
      if (this.showMenu) {
        this.closeMenu();
        setTimeout(() => {
          next();
        }, this.menuTransitionDuration);
      } else {
        next();
      }
    },
    watch: {
      $route: {
        immediate: true,
        handler: function () {
          this.updateBackground()
        }
      }
    }
  };
</script>
<style lang="scss">
  $scaleSize: 0.8;
  @keyframes zoomIn8 {
    from {
      opacity: 0;
      transform: scale3d($scaleSize, $scaleSize, $scaleSize);
    }
    100% {
      opacity: 1;
    }
  }

  .main-content .zoomIn {
    animation-name: zoomIn8;
  }

  @keyframes zoomOut8 {
    from {
      opacity: 1;
    }
    to {
      opacity: 0;
      transform: scale3d($scaleSize, $scaleSize, $scaleSize);
    }
  }

  .main-content .zoomOut {
    animation-name: zoomOut8;
  }
  .navbar{
    font-family: 'Yekan'
  }
  .bg-black{
    background-color: black !important;
  }
</style>
