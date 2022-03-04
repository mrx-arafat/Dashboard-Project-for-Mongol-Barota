import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
Vue.use(VueRouter)

import {
  store
} from './store'
import {
  routes
} from './routes'

Vue.config.productionTip = false

const router = new VueRouter({
  mode: 'history',
  routes
});


new Vue({
  render: h => h(App),
  store,
  router
}).$mount('#app')
