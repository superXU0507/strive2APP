let testList = {
  'rows|10': [{
    id: '@guid',
    name: '@color',
    'age|20-30': 23,
    'job|1': ['前端工程师', '后端工程师', 'UI工程师', '需求工程师']
  }]
};
export default {
  'get|/parameter/test': testList
}