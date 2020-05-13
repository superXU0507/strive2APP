<template>
  <v-container fluid>
    <v-row dense>
      <v-col :cols="6">
        <v-alert
          border="bottom"
          colored-border
          type="warning"
          elevation="2"
        >
          <p><b>注意！</b></p>
          <p>本站仍在<b>建设中</b>，请向<b>组织纪检股</b>提出您的宝贵意见。</p>
        </v-alert>
      </v-col>
      <v-col :cols="12">
        <v-card>
          <v-card-title><b>边防第三五一团“双争”考评系统</b></v-card-title>
          <v-card-text>欢迎使用“双争”考评系统，请通过右上方登录按钮登录，通过左侧导航入口查看排名或进行考评。</v-card-text>
        </v-card>
      </v-col>
      <v-col :cols="6">
        <v-row dense>
          <v-col :cols="12">
            <v-card
              v-if="this.loginState===true"
            >
              <v-card-title><b>欢迎, {{ this.$store.state.user.unitName }}</b></v-card-title>
              <v-card-text><p>贵单位本季度“双争”考评排名为:</p>
                           <p><b>{{this.$store.state.user.cate}}</b>第<b>{{this.selfRank[0]}}</b>名。</p>
              </v-card-text>
            </v-card>
            <v-alert
              v-else-if="this.loginState===false"
              border="bottom"
              colored-border
              type="warning"
              elevation="2"
            >
              <p><b>请登录</b></p>
              <p>游客您好。</p>
            </v-alert>
          </v-col>
          <v-col :cols="12">
            <v-card v-if="this.loginState===true">
              <v-card-title><b>排名数据上次更新时间</b></v-card-title>
              <v-card-text>
                <p>{{this.fullDate}}</p>
                <p>{{this.fullTime}}</p>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-col>

      <v-col :cols="6">
        <v-row dense>
          <v-col :cols="12">
            <v-card v-if="this.loginState===true" :style="{height:'320px'}">
              <v-card-title><b>{{this.$store.state.user.unitName}} {{this.date.getFullYear()}}年各季度双争考评成绩</b></v-card-title>
              <div id="lineChart" :style="{width:'100%',height:'90%'}"></div>       
            </v-card>
          </v-col>
        </v-row>
      </v-col>
      <v-col :cols="12">
        <v-card>
          <v-card-title><b>“双争”考评数据管理系统</b></v-card-title>
          <v-card-text><a href="http://28.76.41.95/admin">管理员可从此处进入后台数据库管理系统</a></v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { getHistoryRank } from "@/network/home";
let echarts = require('echarts');
require('echarts/lib/chart/bar')
require('echarts/lib/component/tooltip');
require('echarts/lib/component/title');
export default {
  name: "Home",
  data: () => ({
    date: new Date(),
    selfRank: [],
    updateTime: ['yyyy-mm-dd HH:MM'],
    historyRank: [],
    lineData: [],
    seasonScore: [],
    belief_basis: [],
    faith_basis: [],
    discipline_basis: [],
    responsible_basis: [],
    belief_instit: [],
    faith_instit: [],
    discipline_instit: [],
    responsible_instit: [],
    special: [],
    comprenhensive: [],
    institself: [],
    basisevaluate: [],
    leaderevaluate: [],
    other: [],
    // seasonScore:[11, 11, 15, 13],
    // faithScore_basis:[1, -2, 2, 5],
  }),
  computed: {
    loginState() {
      return this.$store.state.token!==""
    },
    fullDate() {
      let a = this.updateTime;
      if (a.length > 1) {
        a.shift()
        return a[0].split(" ")[0].replace(/(\d{4})-(\d{2})-(\d{2})/g,'$1年$2月$3日')
      } else {
        return a[0].split(" ")[0].replace(/(\d{4})-(\d{2})-(\d{2})/g,'$1年$2月$3日')
      }
    },
    fullTime() {
      let a = this.updateTime;
      if (a.length > 1) {
        a.shift()
        return a[0].split(" ")[1].replace(/(\d{2}):(\d{2})/g,'$1时$2分')
      } else {
        return a[0].split(" ")[1].replace(/(\d{2}):(\d{2})/g,'$1时$2分')
      }
    }
  },
  components: {},
  methods: {
    HistoryRank() {
      if (this.$store.state.token!=="") {
        let unitName = this.$store.state.user.unitName;
        getHistoryRank(unitName).then(res => {
          this.historyRank = res.data;
          if (this.$store.state.user.userMajorCate === '基层') {
            this.historyRank = this.historyRank.map(item => {
              this.lineData=[
                              '铁一般信仰(自查)',
                              '铁一般信念(自查)',
                              '铁一般纪律(自查)',
                              '铁一般担当(自查)',
                              '铁一般信仰(机关)',
                              '铁一般信念(机关)',
                              '铁一般纪律(机关)',
                              '铁一般担当(机关)',
                              '专项检查',
                              '综合检查',
                              '阶段加分',
                              '季度总分',
                            ];
              this.seasonScore.push(Number(item.total_score));
              this.belief_basis.push(Number(item.total_belief_basis));
              this.faith_basis.push(Number(item.total_faith_basis));
              this.discipline_basis.push(Number(item.total_discipline_basis));
              this.responsible_basis.push(Number(item.total_responsible_basis));
              this.belief_instit.push(Number(item.total_belief_instit));
              this.faith_instit.push(Number(item.total_faith_instit));
              this.discipline_instit.push(Number(item.total_discipline_instit));
              this.responsible_instit.push(Number(item.total_responsible_instit));
              this.special.push(Number(item.total_special));
              this.comprenhensive.push(Number(item.total_comprenhensive));
              this.other.push(Number(item.total_other));
              this.selfRank.push(item.season_rank);
              this.updateTime.push(item.update_time);
            });
        } else if (this.$store.state.user.userMajorCate === '机关') {
          this.historyRank = this.historyRank.map(item => {
            this.lineData=[
                            '机关自查',
                            '基层测评',
                            '领导打分',
                            '阶段加分',
                            '季度总分',
                          ];
            this.seasonScore.push(Number(item.total_score));
            this.institself.push(Number(item.total_institself));
            this.basisevaluate.push(Number(item.total_basisevaluate));
            this.leaderevaluate.push(Number(item.total_leaderevaluate));
            this.other.push(Number(item.total_other));
            this.selfRank.push(item.season_rank);
            this.updateTime.push(item.update_time);
          });
        }
      }).then(v => {
        if (this.loginState) {
          this.drawLine();//是用户则绘制折线图
        }
      });
      }
    },
    drawLine(){
      let lineChart = echarts.init(document.getElementById('lineChart'));
      // 绘制图表
      if (this.$store.state.user.userMajorCate === '基层') {
        lineChart.setOption({
          grid: {
            top: '20%'
          },
          title: {
            text: '',
            subtext: ''
          },
          tooltip: {
            trigger: 'axis'
          },
          legend: {
            type: 'scroll',
            top: '0%',
            left: '5%',
            right: '5%',
            data: this.lineData
          },
          toolbox: {
            show: true,
            top: '8%',
            right: '5%',
            feature: {
              magicType: {type: ['line', 'bar']},
              restore: {},
              saveAsImage: {}
            }
          },
          xAxis: {
            type: 'category',
            boundaryGap: false,
            data: ['第一季度','第二季度','第三季度','第四季度']
          },
          yAxis: {
            type: 'value',
            axisLabel: {
              formatter: '{value}'
            }
          },
          series: [
            {
              name:'季度总分',
              type:'line',
              data:this.seasonScore.reverse(),
              markPoint: {
                data: [
                  {type: 'max', name: '最高'},
                  {type: 'min', name: '最低'}
                ]
              },
            },
            {
              name:'铁一般信仰(自查)',
              type:'line',
              data:this.belief_basis.reverse(),
              markPoint: {
                data: [
                  {type: 'max', name: '最高'},
                  {type: 'min', name: '最低'}
                ]
              },
            },
            {
              name:'铁一般信念(自查)',
              type:'line',
              data:this.faith_basis.reverse(),
              markPoint: {
                data: [
                  {type: 'max', name: '最高'},
                  {type: 'min', name: '最低'}
                ]
              },
            },
            {
              name:'铁一般纪律(自查)',
              type:'line',
              data:this.discipline_basis.reverse(),
              markPoint: {
                data: [
                  {type: 'max', name: '最高'},
                  {type: 'min', name: '最低'}
                ]
              },
            },
            {
              name:'铁一般担当(自查)',
              type:'line',
              data:this.responsible_basis.reverse(),
              markPoint: {
                data: [
                  {type: 'max', name: '最高'},
                  {type: 'min', name: '最低'}
                ]
              },
            },
            {
              name:'铁一般信仰(机关)',
              type:'line',
              data:this.belief_instit.reverse(),
              markPoint: {
                data: [
                  {type: 'max', name: '最高'},
                  {type: 'min', name: '最低'}
                ]
              },
            },
            {
              name:'铁一般信念(机关)',
              type:'line',
              data:this.faith_instit.reverse(),
              markPoint: {
                data: [
                  {type: 'max', name: '最高'},
                  {type: 'min', name: '最低'}
                ]
              },
            },
            {
              name:'铁一般纪律(机关)',
              type:'line',
              data:this.discipline_instit.reverse(),
              markPoint: {
                data: [
                  {type: 'max', name: '最高'},
                  {type: 'min', name: '最低'}
                ]
              },
            },
            {
              name:'铁一般担当(机关)',
              type:'line',
              data:this.responsible_instit.reverse(),
              markPoint: {
                data: [
                  {type: 'max', name: '最高'},
                  {type: 'min', name: '最低'}
                ]
              },
            },
            {
              name:'专项检查',
              type:'line',
              data:this.special.reverse(),
              markPoint: {
                data: [
                  {type: 'max', name: '最高'},
                  {type: 'min', name: '最低'}
                ]
              },
            },
            {
              name:'综合检查',
              type:'line',
              data:this.comprenhensive.reverse(),
              markPoint: {
                data: [
                  {type: 'max', name: '最高'},
                  {type: 'min', name: '最低'}
                ]
              },
            },
            {
              name:'阶段加分',
              type:'line',
              data:this.other.reverse(),
              markPoint: {
                data: [
                  {type: 'max', name: '最高'},
                  {type: 'min', name: '最低'}
                ]
              },
            }
          ]
        });
      } else if (this.$store.state.user.userMajorCate === '机关') {
        lineChart.setOption({
          grid: {
            top: '20%'
          },
          title: {
            text: '',
            subtext: ''
          },
          tooltip: {
            trigger: 'axis'
          },
          legend: {
            type: 'scroll',
            top: '0%',
            left: '5%',
            right: '5%',
            data: this.lineData
          },
          toolbox: {
            show: true,
            top: '8%',
            right: '5%',
            feature: {
              magicType: {type: ['line', 'bar']},
              restore: {},
              saveAsImage: {}
            }
          },
          xAxis: {
            type: 'category',
            boundaryGap: false,
            data: ['第一季度','第二季度','第三季度','第四季度']
          },
          yAxis: {
            type: 'value',
            axisLabel: {
              formatter: '{value}'
            }
          },
          series: [
            {
              name:'季度总分',
              type:'line',
              data:this.seasonScore.reverse(),
              markPoint: {
                data: [
                  {type: 'max', name: '最高'},
                  {type: 'min', name: '最低'}
                ]
              },
            },
            {
              name:'机关自查',
              type:'line',
              data:this.institself.reverse(),
              markPoint: {
                data: [
                  {type: 'max', name: '最高'},
                  {type: 'min', name: '最低'}
                ]
              },
            },
            {
              name:'基层测评',
              type:'line',
              data:this.basisevaluate.reverse(),
              markPoint: {
                data: [
                  {type: 'max', name: '最高'},
                  {type: 'min', name: '最低'}
                ]
              },
            },
            {
              name:'领导打分',
              type:'line',
              data:this.leaderevaluate.reverse(),
              markPoint: {
                data: [
                  {type: 'max', name: '最高'},
                  {type: 'min', name: '最低'}
                ]
              },
            },
            {
              name:'阶段加分',
              type:'line',
              data:this.other.reverse(),
              markPoint: {
                data: [
                  {type: 'max', name: '最高'},
                  {type: 'min', name: '最低'}
                ]
              },
            }
          ]
        });
      }
    }
  },
  watch: {},
  created (){
    this.HistoryRank();
  },
  mounted (){}
};
</script>

<style scoped>
.nav-drawer {
  top: 65px !important;
}
</style>