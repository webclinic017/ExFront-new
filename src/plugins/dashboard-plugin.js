
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

// asset imports

export default {
  install(Vue) {
    Vue.use(BootstrapVue);
    Vue.use(IconsPlugin);
  }
};
