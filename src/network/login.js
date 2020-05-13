import { request } from "./request"

export function getUserInfo(username, password) {
  return request({
    method: 'post',
    url: '/api/api-token-auth/',
    data: {
      username,
      password,
    }
  })
}
