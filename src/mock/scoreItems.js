
let score_items = {
  'rows|20': [{
    id: '@guid',
    release_date: {
      id: '@guid',
      "unit": {
        id: '@guid',
        "unit_name|1": ['一营一连', '一营二连', '一营三连', '二营四连', '二营五连', '二营六连', '二营七连'],
        unit_cate: "建制连队"
      },
      month_date: "@date(yyyy-MM-dd)",
      "month_score_basisunit|1-10": 0,
      "month_score_institunit|1-10": 0,
    },
    "scorer|1": ['基层', '机关'],
    "major_term|1": ['铁一般信仰', '铁一般信念', '机关专项检查', '其它',],
    "detail_cate|1": ['每季度', '每周', '每月', '半年', '一年', '即时性工作(扣分)'],
    "detail_name|1": ['加强党组织建设', '做好心理工作', '密切内外关系', '落实战备工作', '抓好军事训练', '建强四个队伍',],
    "max_score|1-20": 3,
    description: "@cparagraph(5,20)",
    unit_score: "0.0"
  }]
};


export default {
  'get|/api/score_items': score_items
  // options => {
  //   console.log(options)
  // }
  // score_items
}