<template>
  <v-container>
    <v-list two-line>
      <v-list-item>
        <v-list-item-content>
          <v-form ref="form" v-model="valid" lazy-validation>
            <v-autocomplete
              v-model="unitName"
              :items="unitNames"
              :rules="rules"
              color="white"
              label="单位"
              auto-select-first
            ></v-autocomplete>
          </v-form>
        </v-list-item-content>
        <v-list-item-action>
          <v-tooltip top>
            <template v-slot:activator="{ on }">
              <v-btn icon v-on="on" color="green" @click="validate" :disabled="!valid">
                <v-icon>mdi-plus-circle-outline</v-icon>
              </v-btn>
            </template>
            <span>新增</span>
          </v-tooltip>
        </v-list-item-action>
      </v-list-item>
      <template v-for="score in scoreList">
        <v-list-item :key="score.id" v-show="score.isShow">
          <v-list-item-content>
            <v-list-item-title>
              <v-chip class="ma-2" label outlined @click="scoreFilter(score.year, 0)">
                <v-avatar left v-if="typeIndexs.indexOf(0) > -1">
                  <v-icon>mdi-check-bold</v-icon>
                </v-avatar>
                {{score.year}}
              </v-chip>
              <v-chip class="ma-2" label outlined @click="scoreFilter(score.month, 1)">
                <v-avatar left v-if="typeIndexs.indexOf(1) > -1">
                  <v-icon>mdi-check-bold</v-icon>
                </v-avatar>
                {{score.month}}
              </v-chip>
              <v-chip class="ma-2" label outlined @click="scoreFilter(score.unitName, 2)">
                <v-avatar left v-if="typeIndexs.indexOf(2) > -1">
                  <v-icon>mdi-check-bold</v-icon>
                </v-avatar>
                {{score.unitName}}
              </v-chip>
            </v-list-item-title>
            <v-list-item-subtitle>
              <v-chip
                v-for="(cate, i) in score.majorTerm"
                :key="i"
                class="ma-2"
                color="teal"
                label
                text-color="white"
              >{{Object.keys(cate)[0]}} {{cate[Object.keys(cate)[0]]}}</v-chip>
            </v-list-item-subtitle>
          </v-list-item-content>
          <v-list-item-action>
            <v-tooltip top>
              <template v-slot:activator="{ on }">
                <v-btn icon>
                  <v-icon
                    color="blue"
                    v-on="on"
                    @click="getScoreItems(score.unitName, score.date, [score.date], 'view')"
                  >mdi-eye-circle</v-icon>
                </v-btn>
              </template>
              <span>查看</span>
            </v-tooltip>
          </v-list-item-action>
          <!-- <v-list-item-action>
            <v-tooltip top>
              <template v-slot:activator="{ on }">
                <v-btn icon>
                  <v-icon
                    color="green"
                    v-on="on"
                    @click="getScoreItems(score.unitName, '')"
                  >mdi-plus-circle-outline</v-icon>
                </v-btn>
              </template>
              <span>添加</span>
            </v-tooltip>
          </v-list-item-action> -->
          <v-list-item-action>
            <v-tooltip top>
              <template v-slot:activator="{ on }">
                <!-- <v-btn v-if="isQuarterMonths(score.date)" icon> -->
                <v-btn icon>
                  <v-icon
                    color="red"
                    v-on="on"
                    @click="getScoreItems(score.unitName, score.date, [score.date], 'update')"
                  >mdi-pencil</v-icon>
                </v-btn>
              </template>
              <span>修改</span>
            </v-tooltip>
            <!-- <v-tooltip v-else top>
              <template v-slot:activator="{ on }">
                <v-btn icon>
                  <v-icon color="grey" v-on="on">mdi-pencil</v-icon>
                </v-btn>
              </template>
              <span>您无法修改上个季度的评测结果</span>
            </v-tooltip>-->
          </v-list-item-action>
        </v-list-item>
        <v-divider class="mx-4" inset v-show="score.isShow"></v-divider>
      </template>
    </v-list>
  </v-container>
</template>

<script>
import { getScoreList } from "@/network/scoreList";
import { getQuarterMonths } from "@/common";

export default {
  name: "ScoreList",
  data() {
    return {
      //存储筛选条件的索引值数组
      typeIndexs: [],
      //存储筛选条件的对象（固定顺序）
      vals: { 0: "", 1: "", 2: "" },
      scoreList: [],
      //所有被打分对象
      unitNames: [],
      unitName: "",
      valid: true,
      //搜索框验证规则
      rules: [v => !!v || "请输入单位名称"]
    };
  },
  computed: {},
  methods: {
    validate() {
      if (this.$refs.form.validate())
        this.getScoreItems(this.unitName, "", [
          "2020-01",
          "2020-02",
          "2020-03",
          "2020-04",
          "2020-05",
          "2020-06",
          "2020-12"
        ]);
      // this.getScoreItems(this.unitName, '', this.getQuarterMonths())
    },
    //返回当前月份所处的季度的所有月份
    getQuarterMonths() {
      return getQuarterMonths();
    },
    isQuarterMonths(date) {
      return getQuarterMonths().indexOf(date) > -1;
    },
    scoreFilter(val, index) {
      let i = this.typeIndexs.indexOf(index);
      //如果索引值存在，则删除；没有，则添加。
      if (i > -1) {
        this.typeIndexs.splice(i, 1);
      } else {
        this.typeIndexs.push(index);
      }
      let types = ["year", "month", "unitName"];
      //如果筛选条件值存在，则删除；没有，则添加。
      if (this.vals[index]) this.vals[index] = "";
      else this.vals[index] = val;
      this.scoreList = this.scoreList.map(item => {
        //生成多条件筛选的bool对象（如f1&&f2&&f3...）
        let filters = this.typeIndexs.reduce((acc, cur) => {
          return acc && item[types[cur]] === this.vals[cur];
        }, true);
        if (filters) item.isShow = true;
        else item.isShow = false;
        return item;
      });
    },
    getScoreList() {
      let cat = this.$route.params.cat;
      let scorer = "";
      let unitName = "";
      let scoreMajorCate = "";
      let storeUnitName = this.$store.state.user.unitName;
      let storeUserMajorCate = this.$store.state.user.userMajorCate;
      let major_cate_or = { 基层: "机关", 机关: "基层" };
      if (cat === "self") {
        scorer = storeUserMajorCate;
        unitName = storeUnitName;
        scoreMajorCate = storeUserMajorCate;
      } else {
        scorer = this.$store.state.user.userCate;
        scoreMajorCate = major_cate_or[storeUserMajorCate];
      }
      getScoreList(unitName, scorer, scoreMajorCate)
        .then(res => {
          this.unitNames = [];
          this.scoreList = res.data.map(item => {
          // this.scoreList = res.data.rows.map(item => {
              let score = {};
              score.unitName = item.unit_name;
              this.unitNames.push(item.unit_name);
              score.majorTerm = item.major_term;
              score.date = item.date;
              score.year = item.date.split("-")[0] + "年";
              score.month = String(Number(item.date.split("-")[1])) + "月";
              score.isShow = true;
              return score;
            })
            .filter(item => {
              let filterScoreValue = item.majorTerm.reduce((acc, cur) => {
                return acc || cur[Object.keys(cur)[0]] > 0;
              }, false);
              return filterScoreValue;
            });
          this.unitNames = [...new Set(this.unitNames)];
        })
        .catch(e => {
          console.log(e);
        });
    },
    getScoreItems(unitName, date, allowedDates, type) {
      this.$router.push({
        path: "/score",
        query: {
          unitName,
          date: date,
          allowedDates: allowedDates,
          cat: this.$route.params.cat,
          type
        }
      });
    }
  },
  watch: {
    //响应路由参数变化以便重新请求数据
    $route(to, from) {
      this.getScoreList();
    }
  },
  mounted() {
    console.log("created");
    this.getScoreList();
  },
  components: {}
};
</script>

<style scoped>
</style>