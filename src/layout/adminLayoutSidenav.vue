<template>
  <sidenav :orientation="orientation" :class="curClasses">

    <!-- Brand demo (see src/demo.css) -->
    <div class="app-brand demo" v-if="orientation !== 'horizontal'">
      <img v-if="!ifname" src="/img/logo.png" style="width:48px ; height: 48px ; margin-right:10px" alt="">
        <img v-if="ifname" src="/img/logo.png" style="width:32px ; height: 32px" alt="">
      <router-link v-if="ifname" to="/" class="app-brand-text demo sidenav-text font-weight-normal ml-2">AMIZAX</router-link>
      <a href="javascript:void(0)" class="layout-sidenav-toggle sidenav-link text-large ml-auto" @click="toggleSidenav()">
        <i class="ion ion-md-menu align-middle"></i>
      </a>
    </div>
    <div class="sidenav-divider mt-0" v-if="orientation !== 'horizontal'"></div>

    <!-- Links -->
    <div class="sidenav-inner" :class="{ 'py-1': orientation !== 'horizontal' }">

      <!-- Dashboards -->
        <sidenav-router-link icon="ion ion-md-speedometer" to="/dashboard" :exact="true">داشبورد</sidenav-router-link>


      <sidenav-divider class="mb-1"/>
      <sidenav-header class="small font-weight-semibold">امور مالی</sidenav-header>









      <sidenav-router-link icon="ion ion-md-quote" to="/adminpanel/profit" :exact="true">تاریخچه درآمد ها</sidenav-router-link>
      <sidenav-router-link icon="ion ion-md-quote" to="/adminpanel/transactions" :exact="true"> تاریخچه برداشت و واریز</sidenav-router-link>
      <sidenav-router-link icon="ion ion-md-quote" to="/adminpanel/withdraw" :exact="true"> برداشت ریالی</sidenav-router-link>
      <sidenav-router-link icon="ion ion-md-quote" to="/adminpanel/cptransactions" :exact="true"> تاریخچه حساب ترید</sidenav-router-link>


      <sidenav-menu icon="ion ion-md-quote"  :exact="true">
        <template slot="link-text"> برداشت از کوینکس</template>
        <sidenav-router-link  to="/adminpanel/cwithdraw" :exact="true"> درخواست های برداشت</sidenav-router-link>
        <sidenav-router-link  to="/adminpanel/rcwithdraw" :exact="true"> درخواست های رد شده</sidenav-router-link>
        <sidenav-router-link  to="/adminpanel/ccwithdraw" :exact="true"> درخواست های انجام شده</sidenav-router-link>
      </sidenav-menu>


      <sidenav-menu icon="ion ion-md-quote"  :exact="true">
        <template slot="link-text"> خرید از داخلی Amizax</template>
        <sidenav-router-link  to="/adminpanel/buy" :exact="true"> درخواست ها </sidenav-router-link>
        <sidenav-router-link  to="/adminpanel/buydone" :exact="true">   رد شده</sidenav-router-link>
        <sidenav-router-link  to="/adminpanel/buyreject" :exact="true">   انجام شده</sidenav-router-link>
      </sidenav-menu>


      <sidenav-menu icon="ion ion-md-quote"  :exact="true">
        <template slot="link-text"> فروش از داخلی Amizax</template>
        <sidenav-router-link  to="/adminpanel/sellset" :exact="true"> تایید قیمت</sidenav-router-link>
        <sidenav-router-link  to="/adminpanel/selldone" :exact="true"> انجام شده</sidenav-router-link>
      </sidenav-menu>


      <sidenav-menu icon="ion ion-md-quote"  :exact="true">
        <template slot="link-text"> اکسچینج</template>
        <sidenav-router-link  to="/adminpanel/exchange" :exact="true"> درخواست ها </sidenav-router-link>
        <sidenav-router-link  to="/adminpanel/exchangedone" :exact="true">   رد شده</sidenav-router-link>
        <sidenav-router-link  to="/adminpanel/exchangereject" :exact="true">   انجام شده</sidenav-router-link>
      </sidenav-menu>


      <sidenav-menu icon="ion ion-md-quote"  :exact="true">
        <template slot="link-text"> درخواست های واریز</template>
        <sidenav-router-link  to="/adminpanel/deposit" :exact="true"> درخواست ها </sidenav-router-link>
        <sidenav-router-link  to="/adminpanel/depositdone" :exact="true">   رد شده</sidenav-router-link>
        <sidenav-router-link  to="/adminpanel/depositreject" :exact="true">   انجام شده</sidenav-router-link>
      </sidenav-menu>

      
      <sidenav-divider class="mb-1"/>
      <sidenav-header class="small font-weight-semibold">خرید و فروش از کیف های خارج از سایت</sidenav-header>
      <sidenav-router-link icon="ion ion-md-quote" to="/adminpanel/buy-out" :exact="true"> خرید از AMIZAX</sidenav-router-link>
      <sidenav-router-link icon="ion ion-md-quote" to="/adminpanel/sell-out" :exact="true"> فروش به AMIZAX</sidenav-router-link>
      <sidenav-router-link icon="ion ion-md-quote" to="/adminpanel/open-orders-out" :exact="true">سفارشات باز</sidenav-router-link>
      <sidenav-router-link icon="ion ion-md-quote" to="/adminpanel/history-out" :exact="true">تاریخچه سفارشات</sidenav-router-link>


      <sidenav-divider class="mb-1"/>
      <sidenav-header class="small font-weight-semibold">امور کاربران</sidenav-header>
      <sidenav-router-link icon="ion ion-md-quote" to="/adminpanel/users" :exact="true">کاربران</sidenav-router-link>
      <sidenav-menu icon="ion ion-md-quote"  :exact="true">
        <template slot="link-text"> درخواست های تایید</template>
        <sidenav-router-link  to="/adminpanel/verifybank" :exact="true"> بانک</sidenav-router-link>
        <sidenav-router-link  to="/adminpanel/verifymelli" :exact="true">   کارت ملی</sidenav-router-link>
        <sidenav-router-link  to="/adminpanel/verifyaccept" :exact="true">   برگ پذیرش قوانین</sidenav-router-link>
        <sidenav-router-link  to="/adminpanel/verifyperpetual" :exact="true">   حساب پرپشوال</sidenav-router-link>
      </sidenav-menu>
      <!-- UI elements -->

      <sidenav-divider class="mb-1"/>
      <sidenav-header class="small font-weight-semibold">پشتیبانی</sidenav-header>
      <sidenav-router-link icon="ion ion-md-quote" to="/adminpanel/tickets" :exact="true">تیکت ها</sidenav-router-link>
      <sidenav-router-link icon="ion ion-md-quote" to="/adminpanel/chats" :exact="true"> چت</sidenav-router-link>

      <sidenav-divider class="mb-1"/>
      <sidenav-header class="small font-weight-semibold">تنظیمات</sidenav-header>
      <sidenav-router-link icon="ion ion-md-quote" to="/adminpanel/general-settings" :exact="true">تنظیمات عمومی</sidenav-router-link>
      <sidenav-router-link icon="ion ion-md-quote" to="/adminpanel/userlevel-settings" :exact="true"> تنظیمات سطح کاربر</sidenav-router-link>


      <sidenav-divider class="mb-1"/>
      <sidenav-header class="small font-weight-semibold">پیکره بندی</sidenav-header>
      <sidenav-menu icon="ion ion-md-quote"  :exact="true">
        <template slot="link-text"> صفحه اصلی</template>
        <sidenav-router-link  to="/adminpanel/main-page-top-stickers" :exact="true"> برچسب های بالا</sidenav-router-link>
        <sidenav-router-link  to="/adminpanel/main-page-bottom-stickers" :exact="true">   برچسب های پایین</sidenav-router-link>
        <sidenav-router-link  to="/adminpanel/main-page-posts" :exact="true">   پست ها</sidenav-router-link>
      </sidenav-menu>
      <sidenav-router-link icon="ion ion-md-quote" to="/adminpanel/other-pages" :exact="true">صفحات جانبی</sidenav-router-link>
      <sidenav-router-link icon="ion ion-md-quote" to="/adminpanel/details" :exact="true"> توضیحات</sidenav-router-link>




      <sidenav-divider class="mb-1"/>
      <sidenav-router-link icon="ion ion-md-quote" to="/logout" :exact="true"> خروج</sidenav-router-link>
      
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

  props: {
    orientation: {
      type: String,
      default: 'vertical'
    }
  },

  data(){
    return {
      ifname: true,
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
