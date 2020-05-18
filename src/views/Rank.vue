<template>
  <v-container style="background: #E0E0E0">
    <v-row no-gutters>
      <v-col :cols="12">
        <v-card :style="{height:'450px'}">
          <v-card-title>{{this.year}}年 第{{this.season}}季度 {{this.unitCate}} 排名情况柱状图</v-card-title>
          <div id="BarChart" :style="{width:'100%',height:'90%'}"></div>
        </v-card>
      </v-col>
      <v-col :cols="12">
        <v-card>
          <v-data-table
            :headers="headers"
            :items="rankList"
            :sort-by="['totalScore']"
            :sort-desc="[true]"
            class="elevation-1"
            :loading="loading"
            loading-text="加载数据中，请稍侯"
            hide-default-footer
            disable-pagination
          >
            <template v-slot:header="{ props: { headers } }">
              <thead>
                <tr>
                  <th :colspan="headers.length/3">
                    <v-select :items="years" v-model="year" filled label="年" dense></v-select>
                  </th>
                  <th :colspan="headers.length/3">
                    <v-select :items="seasons" v-model="season" filled label="季度" dense></v-select>
                  </th>
                  <th :colspan="headers.length/3">
                    <v-select :items="unitCates" v-model="unitCate" filled label="单位" dense></v-select>
                  </th>
                </tr>
              </thead>
            </template>
          </v-data-table>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { getRankList } from "@/network/rankList";
let echarts = require('echarts');
require('echarts/lib/chart/bar')
require('echarts/lib/component/tooltip');
require('echarts/lib/component/title');

export default {
  name: "Rank",
  data() {
    return {
      headers: [
        {
          text: "单位",
          align: "start",
          sortable: false,
          value: "unitName"
        },
        { text: "铁一般信仰(自查/机关)", value: "totalBelief" },
        { text: "铁一般信念(自查/机关)", value: "tottalFaith" },
        { text: "铁一般纪律(自查/机关)", value: "totalDiscipline" },
        { text: "铁一般担当(自查/机关)", value: "totalResponsible" },
        { text: "专项检查", value: "totalSpecial" },
        { text: "综合检查", value: "totalComprenhensive" },
        { text: "阶段加分", value: "totalOther" },
        { text: "总分", value: "totalScore" }
      ],
      rankList: [],
      year: new Date().getFullYear(),
      years: [
        new Date().getFullYear() - 2,
        new Date().getFullYear() - 1,
        new Date().getFullYear()
      ],
      unitCate: "建制连队",
      unitCates: ["建制连队", "建制营", "非建制单位", "机关股室"],
      season: 1,
      seasons: [1, 2, 3, 4],
      loading: true,
      unitList: [],
      unitScore: []
    };
  },
  computed: {},
  watch: {
    year: function(newYear, oldYear) {
      this.getRankList();
    },
    season: function(newSeason, oldSeason) {
      this.getRankList();
    },
    unitCate: function(newUnitCate, oldUnitCate) {
      this.getRankList();
    }
  },
  methods: {
    getRankList() {
      this.loading = true;
      this.unitList = [];
      this.unitScore = [];
      let basis = ["建制连队", "非建制单位"];
      getRankList(this.unitCate, this.year, this.season).then(res => {
        this.loading = false;
        this.rankList = res.data.map(item => {
        // this.rankList = res.data.rows.map(item => {
          let r = {};
          if (basis.indexOf(this.unitCate) > -1) {
            r.totalBelief =
              item.total_belief_basis + "/" + item.total_belief_instit;
            r.tottalFaith =
              item.total_faith_basis + "/" + item.total_faith_instit;
            r.totalDiscipline =
              item.total_discipline_basis + "/" + item.total_discipline_instit;
            r.totalResponsible =
              item.total_responsible_basis +
              "/" +
              item.total_responsible_instit;
            r.totalSpecial = item.total_special;
            r.totalComprenhensive = item.total_comprenhensive;
          } else {
            r.totalInstitself = item.total_institself;
            r.totalBasisevaluate = item.total_basisevaluate;
            r.totalLeaderevaluate = item.total_leaderevaluate;
          }
          r.unitName = item.unit_name;
          this.unitList.push(item.unit_name);
          r.totalOther = item.total_other;
          r.totalScore = item.total_score;
          this.unitScore.push(Number(item.total_score));
          return r;
        });
      }).then(() => {
        this.drawBar();
      });
      if (basis.indexOf(this.unitCate) === -1) {
        console.log(this.unitCate);
        if (this.unitCate === "建制营") {
          this.headers = [
            {
              text: "单位",
              value: "unitName"
            },
            { text: "阶段加分", value: "totalOther" },
            { text: "总分", value: "totalScore" },
          ];
        } else {
          this.headers = [
            {
              text: "单位",
              align: "start",
              sortable: false,
              value: "unitName"
            },
            { text: "机关自查", value: "totalInstitself" },
            { text: "基层测评", value: "totalBasisevaluate" },
            { text: "领导打分", value: "totalLeaderevaluate" },
            { text: "阶段加分", value: "totalOther" },
            { text: "总分", value: "totalScore" }
          ];
        }
      } else {
        this.headers = [
          {
            text: "单位",
            align: "start",
            sortable: false,
            value: "unitName"
          },
          { text: "铁一般信仰(自查/机关)", value: "totalBelief" },
          { text: "铁一般信念(自查/机关)", value: "tottalFaith" },
          { text: "铁一般纪律(自查/机关)", value: "totalDiscipline" },
          { text: "铁一般担当(自查/机关)", value: "totalResponsible" },
          { text: "专项检查", value: "totalSpecial" },
          { text: "综合检查", value: "totalComprenhensive" },
          { text: "阶段加分", value: "totalOther" },
          { text: "总分", value: "totalScore" }
        ];
      }
    },
    drawBar() {
      let BarChart = echarts.init(document.getElementById('BarChart'));
      BarChart.setOption({
        title: {
          text: '',
          subtext: ''
        },
        grid: {
          left: '15%',
          bottom: '35%'
        },
        tooltip: {
          trigger: 'axis'
        },
        toolbox: {
          show: true,
          right: '5%',
          feature: {
            magicType: {type: ['bar', 'line']},
            restore: {},
            saveAsImage: {}
          }
        },
        xAxis: {
          type: 'category',
          boundaryGap: false,
          data: this.unitList,
          axisLabel: {  
            interval:0,  
            rotate:40  
          }  
        },
        yAxis: {
          type: 'value',
          axisLabel: {
            formatter: '{value}'
          }
        },
        series: [
          {
            name: '季度总分',
            type: 'bar',
            data: this.unitScore,
            barWidth: '50%',
            markPoint: {
              data: [
                {type: 'max', name: '最高'},
                {type: 'min', name: '最低'}
              ]
            },
          },
        ]
      });
    }
  },
  created() {
    this.getRankList();
  }
};
</script>

<style scoped>
</style>