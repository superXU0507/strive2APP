import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '@/store'
//import rank from '../mock/rank'

const Home = () => import('@/views/Home')
const Score = () => import('@/views/Score')
const Login = () => import('@/views/Login')
const Index = () => import('@/views/Index')
const ScoreList = () => import('@/views/ScoreList')
const Rank = () => import('@/views/Rank')


Vue.use(VueRouter)

const routes = [
  {
    path: '',
    redirect: '/index'
  },
  {
    path: '/login',
    component: Login
  },
  {
    path: '/index',
    component: Index,
    children: [
      {
        path: '',
        component: Home
      },
      {
        path: '/score-list/:cat',
        name: 'scoreList',
        component: ScoreList,
        meta: { requiresAuth: true }
      },
      {
        path: '/score',
        name: 'score',
        component: Score,
        // props: true,
        meta: { requiresAuth: true }
      },
      {
        path: '/rank',
        name: 'rank',
        component: Rank,
      }
    ]
  },
]
const router = new VueRouter({
  routes,
  mode: 'hash'
})

//每次跳转路由前判定用户是否登陆
router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (store.state.token) {
      next()
    } else {
      next('/login')
    }
  } else {
    next()
  }
});

export default router