//返回当前月份对应的季度月份数组
export function getQuarterMonths() {
  const quarter = {
    0: ["2020-01", "2020-02", "2020-03"],
    1: ["2020-04", "2020-05", "2020-06"],
    2: ["2020-07", "2020-08", "2020-09"],
    3: ["2020-10", "2020-11", "2020-12"],
  }
  const monthNow = new Date().getMonth()
  return quarter[parseInt(monthNow/3)]
}