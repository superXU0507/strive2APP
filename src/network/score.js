import { request } from "./request"

export function getItems(unit_name, date, scorer) {
  return request({
    method: 'get',
    url: '/api/score_items',
    params: {
      unit_name,
      date,
      scorer,
    }
  })
}


export function updateScoreItems(data, token) {
  // console.log(data)
  return request({
    headers: {'Authorization': token},
    method: 'patch',
    url: '/api/score_items/',
    data: data,
  })
}
