# 考评系统
vue+django前后端分离，strive2web中为后端程序文件，其余为前端。

## 前言
受单位领导要求，为一项考评试点任务开发在线考评及后台管理系统，首次进行web开发，两个月边学边做，形成了这个简单的XXX考评系统。
>前端vue、后端django、数据库sqlite、服务器apache、图表Echarts

## 页面效果
首页，上方应用栏，左侧抽屉导航，主页面根据当前登录用户显示本年各季度详细得分等信息。

首页（游客），无排名信息，仅显示游客欢迎页面。

登录

排名，根据年度、季度、单位类型显示排名信息，上方为Echarts图表

历史打分，二阶导航入口进入的页面，能够显示当前登录单位过往为其他单位打分的历史。非本季度记录只能查看不能编辑。最上方下拉列表选择打分单位创建新的打分记录（在自评页面仅有自己单位）。绿色标签可以进行筛选

打分页面，日期选择期选择本季度月份进行打分。星星数根据各项最大分值确定，扣分项最大分值为0，需填入一个0或负数，否则输入框警告，且提交后会提示错误。提交后提示数据传输中，成功提交3秒后返回首页。

后台管理系统，就是django的admin管理页面。部份表有批量导出excel和从excel导入功能

# 前端开发
需要安装npm
### vue前端项目初始化、依赖下载
```
npm install
```

### 启动vue热编译开发服务
```
npm run serve
```

### vue打包和压缩
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

#后端开发
需要apache24服务器，python3.6环境，python依赖在requirement.txt中
```
pip install -r requirements.txt
```
为脱敏,数据库已被删除,需要重新建立.
```
python manage.py makemigrations
python manage.py migrate
```
启动开发服务器
```
python manage.py runserver
```
```
