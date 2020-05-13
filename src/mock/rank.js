let rankList = {
  'rows|20': [{
    "unit_id": "@guid",
    "unit_name|1": ['机步营机步一连', '赤通拉喀边防连', '米古边防四连', '布棕边防连', '机步营炮兵连'],
    unit_cate: "建制连队",
    // "unit_cate|1": ['建制连队', '建制营', '非建制单位', '机关股室'],
    "total_belief_basis|1-10": 3.5, //基层打的“铁一般信仰”分，展示用，仅基层有此项
    "total_faith_basis|1-10": 20.0, //基层打的“铁一般信念”分，展示用，仅基层有此项
    "total_discipline_basis|1-10": 0, //基层打的“铁一般纪律”分，展示用，仅基层有此项
    "total_responsible_basis|1-10": 0,//基层打的“铁一般担当”分，展示用，仅基层有此项
    "total_belief_instit|1-10": 0, //机关打的“铁一般信仰”分，展示用，仅基层有此项
    "total_faith_instit|1-10": 0, //机关打的“铁一般信念”分，展示用，仅基层有此项
    "total_discipline_instit|1-10": 0, //机关打的“铁一般纪律”分，展示用，仅基层有此项
    "total_responsible_instit|1-10": 0, //机关打的“铁一般担当”分，展示用，仅基层有此项
    "total_special|1-10": 0, //机关专项检查”分数，展示用，仅基层有此项
    "total_comprenhensive|1-10": 0, //机关综合检查”分，展示用，仅基层有此项
    "total_institself|1-10": 0, //机关自查”分数，展示用，仅机关有此
    "total_basisevaluate|1-10": 0, //基层测评”分数，展示用，仅机关有此项
    "total_leaderevaluate|1-10": 0, //领导打分”分数，展示用，仅机关有此项
    "total_score|1-15": 9.4 //总分

  }]
}


export default {
  'get|/api/rank': rankList
  // options => {
  //   console.log(options)
  // }
  // scoreList
}