import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
	state: {
    user_token: "" || sessionStorage.getItem('user_token'),
    user_refresh: "" || sessionStorage.getItem('user_refresh'),
    user_name: "" || sessionStorage.getItem('user_name'),
    user_type: "" || sessionStorage.getItem('user_type')
  },
  mutations: {
    newtoken (state, config) {
      console.log(config)
      sessionStorage.setItem('user_name', config.username)
      sessionStorage.setItem('user_token', config.access)
      sessionStorage.setItem('user_refresh', config.refresh)
      state.user_name = config.username
      state.user_token = config.access
      state.user_refresh = config.refresh
    },
    newtype (state, config) {
      sessionStorage.setItem('user_type', config.type)
      state.user_type = config.type
    }
  },
})

export default store