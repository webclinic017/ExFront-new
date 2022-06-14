<template>
  <sidenav :orientation="orientation" :class="curClasses">

    <!-- Brand demo (see src/demo.css) -->
    <div class="app-brand demo" style="padding:18px" v-if="orientation !== 'horizontal'">
      <router-link   to="/" class="app-brand-text demo sidenav-text font-weight-normal ml-2">
      <img v-if="!ifname" src="/img/logo.png" style="width:32px ; height: 32px ; margin-right:-8px" alt="">
        <img v-if="ifname" src="/img/logo.png" style="width:32px ; height: 32px" alt="">
      <a v-if="ifname"><a style="color:white;font-size:22px; font-weight:bold ; margin-right: 10px">آمیزاکس</a></a> </router-link>
      <a href="javascript:void(0)" class="layout-sidenav-toggle sidenav-link text-large ml-auto" @click="toggleSidenav()">
        <i v-if="ifname" class="fas fa-angle-double-right"></i>
        <i v-else class="fas fa-angle-double-left"></i>
      </a>
    </div>
    <div class="sidenav-divider mt-0" v-if="orientation !== 'horizontal'"></div>

    <!-- Links -->
    <div class="sidenav-inner" :class="{ 'py-1': orientation !== 'horizontal' }">

      <!-- Dashboards -->
        <sidenav-router-link icon="ion ion-md-speedometer" to="/dashboard" :exact="true">داشبورد</sidenav-router-link>


      <sidenav-divider class="mb-1"/>
      <sidenav-header class="small font-weight-semibold">ناحیه کاربری</sidenav-header>

      <sidenav-router-link icon="ion ion-md-person" to="/user" :exact="true">اطلاعات کاربر</sidenav-router-link>
      <sidenav-router-link icon="ion ion-md-checkbox" to="/user-level" :exact="true"> تایید هویت</sidenav-router-link>
      <sidenav-router-link icon="ion ion-md-lock" to="/user-security" :exact="true"> امنیت</sidenav-router-link>
      
      
      
      <sidenav-divider class="mb-1"/>
      <sidenav-header class="small font-weight-semibold">مالی</sidenav-header>
      <sidenav-router-link icon="ion ion-logo-bitcoin" to="/wallets" :exact="true">کیف های من</sidenav-router-link>
      <sidenav-menu icon="ion ion-logo-usd"  to="/typography" :exact="true">
       <template slot="link-text">حسابداری</template>
        <sidenav-router-link class="small font-weight-semibold"  to="/deposit">واریز ریالی</sidenav-router-link>
        <sidenav-router-link class="small font-weight-semibold"  to="/wallets/1/withdraw">برداشت ریالی</sidenav-router-link>
        <sidenav-router-link class="small font-weight-semibold"  to="/transactions">تاریخچه واریز و برداشت</sidenav-router-link>
        <sidenav-router-link class="small font-weight-semibold"  to="/addcard">اضافه کردن کارت</sidenav-router-link>
      </sidenav-menu>
      <!-- UI elements -->

      <sidenav-divider class="mb-1"/>
            <sidenav-router-link icon="ion ion-md-swap" to="/exchange" :exact="true">اکسچینج</sidenav-router-link>
      <sidenav-divider class="mb-1"/>
      <sidenav-header class="small font-weight-semibold">خرید</sidenav-header>
      <sidenav-router-link icon="ion ion-md-cart" to="/buy-out" :exact="true"> خرید خارجی</sidenav-router-link>
      <sidenav-router-link icon="ion ion-md-cart" to="/buy" :exact="true"> خرید داخلی </sidenav-router-link>
      
      
      <sidenav-divider class="mb-1"/>
      <sidenav-header class="small font-weight-semibold">فروش</sidenav-header>
      <sidenav-router-link icon="ion ion-md-cart" to="/sell" :exact="true"> فروش داخلی </sidenav-router-link>
      <sidenav-router-link icon="ion ion-md-cart" to="/sell-out" :exact="true"> فروش خارجی </sidenav-router-link>
      


      <sidenav-divider class="mb-1"/>
      <sidenav-header class="small font-weight-semibold">سوابق معاملات</sidenav-header>
      <sidenav-router-link icon="ion ion-md-clock" to="/open-orders" :exact="true"> سفارشات باز داخلی</sidenav-router-link>
      <sidenav-router-link icon="ion ion-md-list-box" to="/history" :exact="true">تاریخچه سفارشات داخلی</sidenav-router-link>
      <sidenav-router-link icon="ion ion-md-clock" to="/open-orders-out" :exact="true">سفارشات باز خارجی</sidenav-router-link>
      <sidenav-router-link icon="ion ion-md-list-box" to="/history-out" :exact="true">تاریخچه سفارشات خارجی</sidenav-router-link>

      <sidenav-divider class="mb-1"/>


      <sidenav-divider class="mb-1"/>
      <sidenav-header class="small font-weight-semibold">معاملات لحظه ای</sidenav-header>
      <sidenav-router-link icon="ion ion-md-trending-up" to="/perpetual-trade/BTCUSDT" :exact="true">بازار پرپشوال</sidenav-router-link>
      <sidenav-router-link icon="ion ion-md-trending-up" to="/margin-trade/BTCUSDT" :exact="true"> بازار مارجین</sidenav-router-link>
      <!-- UI elements -->

      <sidenav-divider class="mb-1"/>
      <sidenav-router-link icon="ion ion-md-cart" to="/buyapp" :exact="true">سفارش سایت صرافی</sidenav-router-link>
      <sidenav-router-link icon="ion ion-md-exit" to="/logout" :exact="true"> خروج</sidenav-router-link>
      
    </div>
  </sidenav>
</template>

<script>
import { Sidenav, SidenavLink, SidenavRouterLink, SidenavMenu, SidenavHeader, SidenavBlock, SidenavDivider } from '@/vendor/libs/sidenav'

export default {
  name: 'app-layout-sidenav',
  components: {
    /* eslint-disable vue/no-unused-components */
    Sidenav,
    SidenavLink,
    SidenavRouterLink,
    SidenavMenu,
    SidenavHeader,
    SidenavBlock,
    SidenavDivider
    /* eslint-enable vue/no-unused-components */
  },
  data(){
    return {
      ifname: true
    }
  },

  props: {
    orientation: {
      type: String,
      default: 'vertical'
    }
  },

  computed: {
    curClasses () {
      let bg = this.layoutSidenavBg

      if (this.orientation === 'horizontal' && (bg.indexOf(' sidenav-dark') !== -1 || bg.indexOf(' sidenav-light') !== -1)) {
        bg = bg
          .replace(' sidenav-dark', '')
          .replace(' sidenav-light', '')
          .replace('-darker', '')
          .replace('-dark', '')
      }

      return `bg-${bg} ` + (
        this.orientation !== 'horizontal'
          ? 'layout-sidenav'
          : 'layout-sidenav-horizontal container-p-x flex-grow-0'
      )
    }
  },

  methods: {
    isMenuActive (url) {
      return this.$route.path.indexOf(url) === 0
    },

    isMenuOpen (url) {
      return this.$route.path.indexOf(url) === 0 && this.orientation !== 'horizontal'
    },

    toggleSidenav () {
      this.layoutHelpers.toggleCollapsed()
      this.ifname = !this.ifname
    }
  }
}
</script>
