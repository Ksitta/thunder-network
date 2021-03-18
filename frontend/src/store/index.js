import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
	state: {
    user_token: "" || sessionStorage.getItem('user_token'),
    user_refresh: "" || sessionStorage.getItem('user_refresh'),
    user_name: "" || sessionStorage.getItem('user_name')
  },
  mutations: {
    newtoken (state, config) {
      sessionStorage.setItem('user_name', config.username)
      sessionStorage.setItem('user_token', config.access)
      sessionStorage.setItem('user_refresh', config.refresh)
      state.user_name = config.username
      state.user_token = config.access
      state.user_refresh = config.refresh
    }
  },
})

export default store