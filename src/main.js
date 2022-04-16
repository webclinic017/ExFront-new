import globals from './globals'
import Vue from 'vue';
import App from './App.vue';
import DashboardPlugin from './plugins/dashboard-plugin';

import axios from 'axios';
import BootstrapVue from 'bootstrap-vue';
import VueSweetalert2 from 'vue-sweetalert2'
import 'sweetalert2/dist/sweetalert2.min.css'
import Vuex from 'vuex'
import * as bulmaToast from 'bulma-toast'
import VueLoading from 'vuejs-loading-plugin'
import bFormSlider from 'vue-bootstrap-slider';
import Vue2Filters from 'vue2-filters'
import IconCrypto from "vue-cryptocurrency-icons";
import Cryptoicon from 'vue-cryptoicon';
import icon from 'vue-cryptoicon/src/icons';


Vue.config.productionTip = false

bulmaToast.setDefaults({
  duration: 100,
  position: 'bottom-right',
  closeOnClick: false,
})

// Global RTL flag
Vue.mixin({
  data: globals
})

// router setup
import router from './router';
// plugin setup

axios.defaults.baseURL = 'http://49.12.106.65/api/v1/'


Cryptoicon.add(icon);
Vue.use(Cryptoicon);
Vue.use(BootstrapVue)
Vue.use(Vue2Filters)
Vue.use(Vuex)
Vue.use(IconCrypto);
Vue.use(bFormSlider)
Vue.use(DashboardPlugin);

const store = new Vuex.Store({
  state: {
    brands: [''],
    amount: [0],
    dark : false
  },
  mutations: {
    initializeStore (state) {
      if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
      } else {
        state.token = ''
        state.isAuthenticated = false
      }
      if (localStorage.getItem('admin')) {
        state.Admin = localStorage.getItem('admin')
        state.isAdmin = true
      } else {
        state.Admin = ''
        state.isAdmin = false
      }
    },
    setToken (state, token) {
      state.token = token
      state.isAuthenticated = true
    },
    clearbrands (state) {
      state.brands = []
      state.amount = []
    },
    appendbrands (state, brand) {
      state.brands.push(brand)
    },
    appendamount (state, amount) {
      state.amount.push(amount)
    },
    setAdmin (state, admin) {
      state.Admin = admin
      state.isAdmin = true
    },
    removeToken (state) {
      state.token = ''
      state.isAuthenticated = false
    },
    removeAdmin (state) {
      state.Admin = ''
      state.isAdmin = false
    }
  },
  actions: {
  },
  modules: {
  }
})
Vue.directive('click-outside', {/* code */});
/* eslint-disable no-new */
setTimeout(() => {
  new Vue({
    el: '#app',
    render: h => h(App),
    router,
    store,
    components: { App },
    template: '<App/>'
  });
}, 1500);
Vue.use(VueSweetalert2);

Vue.use(VueLoading , {
  text: 'لطفا کمی صبر کنید', 
  background: 'rgba(0,0,0,0.5)',
})

import IdleVue from "idle-vue";

const eventsHub = new Vue();

Vue.use(IdleVue, {
  eventEmitter: eventsHub,
  store,
  idleTime: 1800000, // 3 seconds
  startAtIdle: false
});