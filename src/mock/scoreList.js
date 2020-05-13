let scoreList ={
  'rows|20': [{
    id: '@guid',
    'unit_name|1': ['机步营机步一连', '赤通拉喀边防连', '米古边防四连', '布棕边防连', '机步营炮兵连'],
    unit_cate: '建制连队',
    scorer: '基层',
    "date|1": ['2020-04', '2020-02', '2020-01', '2020-03', '2020-05', '2020-06', '2020-12'],
    major_term: [
      { '铁一般信仰': '4.0' },
      { '铁一般信念': '1.5' },
      { '铁一般纪律': '2.0' },
      { '铁一般担当': '1.0' },
    ]
  }]
}


export default {
  'get|/api/history': scoreList
  // options => {
  //   console.log(options)
  // }
  // scoreList
}