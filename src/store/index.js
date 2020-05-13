import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

import { getUserInfo } from "@/network/login";

const store = new Vuex.Store({
  state: {
    token: localStorage.getItem('token') || '',
    user: {
      unitName: localStorage.getItem('unitName') || '',
      userCate: localStorage.getItem('userCate') || '',
      userMajorCate: localStorage.getItem('userMajorCate') || '',
      unitId: localStorage.getItem('userId') || '',
      userImg: localStorage.getItem('userImg') || '',
      cate: localStorage.getItem('cate') || '',
    }
  },
  mutations: {
    //请求成功时更新token、unitCate、unitName值
    auth_sucess(state, payload) {
      const { token, userCate, unitName, userMajorCate, unitId, userImg, cate } = payload
      state.token = token
      if (userCate === '基层') {
        state.user.userCate = unitName
        localStorage.setItem('userCate', state.user.userCate)
      } else {
        state.user.userCate = userMajorCate
      }
      state.user.unitName = unitName
      state.user.userMajorCate = userMajorCate
      state.user.unitId = unitId
      state.user.userImg = userImg
      state.user.cate = cate
    },
    //请求失败时
    auth_error(state) {

    },
    //注销
    logOut(state) {
      state.token = ''
      state.user = {}
      localStorage.removeItem('token')
      localStorage.removeItem('userCate')
      localStorage.removeItem('unitName')
      localStorage.removeItem('userMajorCate')
      localStorage.removeItem('userImg')
      localStorage.removeItem('cate')
    }
  },
  actions: {
    //登陆
    logIn(context, payload) {
      return new Promise((resolve, reject) => {
        const { username, password } = payload
        getUserInfo(username, password).then(res => {
          const token = res.data.token
          const userCate = res.data.user_cate
          const unitName = res.data.unit_name
          const unitId = res.data.unit_id
          const userMajorCate = res.data.user_major_cate
          const userImg = res.data.image
          const cate = res.data.cate
          localStorage.setItem('token', token)
          localStorage.setItem('userCate', userCate)
          localStorage.setItem('unitName', unitName)
          localStorage.setItem('userMajorCate', userMajorCate)
          localStorage.setItem('userImg', userImg)
          localStorage.setItem('cate', cate)
          context.commit('auth_sucess', { token, userCate, unitName, unitId, userMajorCate, userImg, cate })
          resolve('登录成功')
        }).catch(error => {
          reject(error)
        })
      })
    },
  }
})

export default store