//返回当前月份对应的季度月份数组
export function getQuarterMonths() {
  const yearNow = new Date().getFullYear()
  const quarter = {
    0: [yearNow+"-01", yearNow+"-02", yearNow+"-03"],
    1: [yearNow+"-04", yearNow+"-05", yearNow+"-06"],
    2: [yearNow+"-07", yearNow+"-08", yearNow+"-09"],
    3: [yearNow+"-10", yearNow+"-11", yearNow+"-12"],
  }
  const monthNow = new Date().getMonth()
  return quarter[parseInt(monthNow/3)]
}