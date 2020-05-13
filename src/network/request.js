import axios from 'axios'

export function request(config) {
  const instance = axios.create({
    // baseURL: 'http://28.76.41.95:80',
    baseURL: 'http://localhost:8010',
    timeout: '30000',
    // withCredentials: true,
  })

  // 网络请求拦截
  instance.interceptors.request.use(config => {
    return config
  }, err => {
    console.log(err)
    alert('出错啦！')
  })

  //后端响应拦截
  instance.interceptors.response.use(response => {
    //console.log(response.status)
    return response
  })

  return instance(config)
}