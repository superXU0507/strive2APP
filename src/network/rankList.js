import { request } from "./request"

export function getRankList(unit_cate, year, season) {
  return request({
    method: 'get',
    url: '/api/rank/',
    params: {
      unit_cate, 
      year, 
      season
    }
  })
}