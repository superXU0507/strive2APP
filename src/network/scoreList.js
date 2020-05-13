import { request } from "./request"

export function getScoreList(unit_name, scorer, scorer_major_cate) {
  return request({
    method: 'get',
    url: '/api/history',
    params: {
      unit_name,
      scorer,
      scorer_major_cate,
    }
  })
}
