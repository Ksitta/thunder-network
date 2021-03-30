import Vue from 'vue'
import App from './App.vue'
import './plugins/element.js'
import router from './router'
import store from './store'
import axios from 'axios'
import { MessageBox } from 'element-ui'
import {showFullScreenLoading, hideFullScreenLoading} from '../src/plugins/loading.js'

Vue.config.productionTip = false

axios.interceptors.request.use((config) => {
  showFullScreenLoading()
  if (sessionStorage.getItem('user_token')) {
    config.headers.Authorization = 'Bearer ' + sessionStorage.getItem('user_token')
  }
  return config;
}, (error) => {
  return Promise.reject(error);
});

let isRefreshing = false

axios.interceptors.response.use(success => {
  success
  hideFullScreenLoading()
}, error => {
  hideFullScreenLoading()
  if (error.response.status === 401 && error.response.data.code === "token_not_valid") {
    sessionStorage.setItem('user_token', '')
    const config = error.response.config
    if (!isRefreshing) {
      isRefreshing = true
      return axios.post('/api/user/refresh/', {
        refresh: sessionStorage.getItem('user_refresh')
      }).then(response => {
        let newtoken = response.data.access
        sessionStorage.setItem('user_token', newtoken)
        return axios(config)
      }).catch(function (error) {
        MessageBox.alert('长时间无操作，请重新登录！', '', {
          showClose: false,
          callback: function () {
            window.location.href = '/';
          }
        });
        return Promise.reject(error);
      }).finally(() => {
        isRefreshing = false
      })
    }
  }
  return Promise.reject(error);
});

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
