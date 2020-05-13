import {request} from "./request"

export function getHistoryRank(unit_name) {
  return request({
    method: 'get',
    url: '/api/history_rank',
    params: {
      unit_name,
    }
  })
}