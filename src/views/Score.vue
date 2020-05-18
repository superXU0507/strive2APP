<template>
  <v-container>
    <v-row justify="center">
      <v-col class="text-center" cols="12">
        <v-date-picker
          v-model="date"
          :allowed-dates="isAllowedDates()"
          full-width
          :landscape="$vuetify.breakpoint.smAndUp"
          type="month"
          class="mt-4"
          locale="zh-cn"
          color="red"
        ></v-date-picker>
      </v-col>
    </v-row>
    <v-skeleton-loader
      :loading="loading"
      type="table-tbody"
      :transition="transition"
    >
      <v-list shaped two-line>
        <v-list-item-group color="red">
          <v-list-item v-for="(item, i) in score_items" :key="i" v-show="item.isShow">
            <v-list-item-content>
              <v-list-item-title>
                <v-tooltip bottom>
                  <template v-slot:activator="{ on }">
                    <v-list-item-title v-text="item.description" v-on="on" />
                  </template>
                  <span>{{ item.description }}</span>
                </v-tooltip>
              </v-list-item-title>
              <v-list-item-subtitle>
                <v-chip
                  class="ma-2"
                  color="red"
                  label
                  text-color="white"
                  v-show="score_items[i].unit_score"
                  @click="filterScoreItems('已填', 0)"
                >
                  <v-avatar left v-if="typeIndexs.indexOf(0) > -1">
                    <v-icon>mdi-check-bold</v-icon>
                  </v-avatar>
                  <v-icon left>mdi-check-circle-outline</v-icon>已填
                </v-chip>
                <v-chip
                  class="ma-2"
                  label
                  v-show="!score_items[i].unit_score"
                  @click="filterScoreItems('未填', 0)"
                >
                  <v-avatar left v-if="typeIndexs.indexOf(0) > -1">
                    <v-icon>mdi-check-bold</v-icon>
                  </v-avatar>
                  <v-icon left>mdi-alpha-x-circle-outline</v-icon>未填
                </v-chip>
                <v-chip
                  class="ma-2"
                  color="teal"
                  label
                  text-color="white"
                  @click="filterScoreItems(item.major_term, 1)"
                >
                  <v-avatar left v-if="typeIndexs.indexOf(1) > -1">
                    <v-icon>mdi-check-bold</v-icon>
                  </v-avatar>
                  <v-icon left>mdi-label</v-icon>
                  {{item.major_term}}
                </v-chip>
                <v-chip
                  class="ma-2"
                  color="teal"
                  label
                  text-color="white"
                  @click="filterScoreItems(item.detail_name, 2)"
                >
                  <v-avatar left v-if="typeIndexs.indexOf(2) > -1">
                    <v-icon>mdi-check-bold</v-icon>
                  </v-avatar>
                  <v-icon left>mdi-label</v-icon>
                  {{item.detail_name}}
                </v-chip>
                <v-chip
                  class="ma-2"
                  color="teal"
                  label
                  text-color="white"
                  @click="filterScoreItems(item.detail_cate, 3)"
                >
                  <v-avatar left v-if="typeIndexs.indexOf(3) > -1">
                    <v-icon>mdi-check-bold</v-icon>
                  </v-avatar>
                  <v-icon left>mdi-label</v-icon>
                  {{item.detail_cate}}
                </v-chip>
              </v-list-item-subtitle>
            </v-list-item-content>
            <!-- <v-list-item-content  class="flex-grow-1 flex-shrink-1">
            <v-rating
              v-model="score_items[i].unit_score"
              :length="item.max_score"
              background-color="grey darken-1"
              half-increments
              empty-icon="$ratingFull"
              hover
              :color="item.detail_cate === '即时性工作(扣分)'?'red':'blue'"
              @input="updateProgress"
              :readonly="actionType"
              :small="item.max_score>5"
            />
            
            </v-list-item-content>-->
            <v-list-item-icon>
              <v-rating v-if="item.detail_cate!='即时性工作(扣分)'"
                class="text-wrap"
                v-model="score_items[i].unit_score"
                :length="item.max_score"
                background-color="grey darken-1"
                half-increments
                empty-icon="$ratingFull"
                hover
                :small="item.max_score>7"
                color="red"
                @input="updateProgress"
                :readonly="actionType"
                clearable
              ></v-rating>
              <v-text-field v-else-if="item.detail_cate==='即时性工作(扣分)'"
                v-model="score_items[i].unit_score"
                label="请输入扣分"
                :rules="[rules.score]"
                placeholder=""
                outlined
                :readonly="actionType"
              ></v-text-field>
              <!-- <v-rating v-else-if="item.detail_cate==='即时性工作(扣分)'"
                class="text-wrap"
                v-model="score_items[i].unit_score"
                length="5"
                background-color="grey darken-1"
                half-increments
                empty-icon="$ratingFull"
                hover
                :small="item.max_score>7"
                color="red"
                @input="updateProgress"
                :readonly="actionType"
                clearable
              ></v-rating> -->
            </v-list-item-icon>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-skeleton-loader>
    <v-row>
      <v-col class="text-center">
        <v-btn v-show="!loading" large color="red" dark @click="handleDialog">提交</v-btn>
        <v-dialog v-model="dialog" persistent max-width="290">
          <v-card>
            <v-card-title class="headline">还有未打分的项，是否离开页面</v-card-title>
            <v-card-text>您还有{{s_len - r_len}}项未填写！若点是将会离开页面并提交已经打过分的项；点否将会继续填写未打分项。</v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="green darken-1" text @click="filterScoreItems('未填', 0)">否</v-btn>
              <v-btn color="green darken-1" text @click="updateScoreItems">是</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-dialog v-model="dialog_process" persistent max-width="290">
          <v-card>
            <v-card-title>提交中</v-card-title>
            <v-card-text>{{ process_text }}。</v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="green darken-1" text @click="dialog_process=false">关闭</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-col>
    </v-row>
    <v-snackbar
      v-model="snackbar_success"
      color='success'
    >
      提交成功，3秒后跳转到首页。
      <v-btn
        color="pink"
        snackbar_text
        @click="snackbar_success=false"
      >
        关闭
      </v-btn>
    </v-snackbar>
    <v-progress-linear
      v-model="rated_progress"
      color="light-red"
      value="45"
      rounded
      striped
      height="15"
      fixed
      bottom
      reactive
    >
      <template v-slot="{ value }">
        <strong>{{ Math.ceil(value) }}%</strong>
      </template>
    </v-progress-linear>
  </v-container>
</template>

<script>
import { getItems, updateScoreItems } from "@/network/score";
export default {
  name: "Score",
  data() {
    return {
      reFresh:true,
      date: this.$route.query.date || new Date().toISOString().substr(0, 7),
      pickerDate: null,
      score_items: [], //请求过来的原始score_items数据
      s_items: [], //精简版细项列表，只包含id和unit_score，用于批量更新评分
      rated_progress: 0,
      snackbar_success: false,
      dialog_process: false,
      allowedDates: this.$route.query.allowedDates,
      actionType: true,
      //存储筛选条件的索引值数组
      typeIndexs: [],
      //存储筛选条件的对象（固定顺序）
      vals: { 0: "", 1: "", 2: "", 3: "" },
      loading: true,
      transition: "scale-transition",
      dialog: false,
      rules: {
        score: value => {
          const pattern = /^((-[1-9]\d*)|(0?))$/
          return pattern.test(value) || '必须输入负分或零分'
        },
      },
      process_text: '数据传输需要一定时间，请耐心等待。'
    };
  },
  computed: {
    //返回score_items数组的长度
    s_len() {
      return this.score_items.length;
    },
    //返回对象属性unit_score不为0的数组的长度
    r_len() {
      return this.score_items.filter(item => item.unit_score).length;
    }
  },
  methods: {
    isAllowedDates() {
      return val => this.allowedDates.indexOf(val) > -1;
    },
    logOut() {
      this.$store.commit("logOut");
      this.$router.push("/login");
    },
    //获取评测表的相应细项
    getScoreItems(date) {
      const endOfQuarters = ["2020-03", "2020-06", "2020-09", "2020-12"];
      let cat = this.$route.query.cat;
      if (this.$route.query.type === "view") this.activiewonType = true;
      else this.actionType = false;
      //被打分者为路由传递过来的参数
      let unitName = this.$route.query.unitName;
      let scorer = "";
      if (cat === "self") scorer = this.$store.state.user.userMajorCate;
      else if (cat === "others") scorer = this.$store.state.user.userCate;
      console.log(unitName, scorer)
      // getItems(unitName, date, this.$store.state.user.userCate).then(res => {
      getItems(unitName, date, scorer).then(res => {
        //发布时应改为
        this.score_items = res.data;
        // this.score_items = res.data.rows;
        this.loading = false;
        //为score_items数组每一个对象添加isShow属性,并将返回的字符串型unit_score转为number
        this.score_items = this.score_items.map(item => {
          item.unit_score = Number(item.unit_score);
          item["isShow"] = true;
          return item;
        }).filter((item) => {
          if (item.detail_cate === "每季度") {
            if (endOfQuarters.indexOf(this.date) === -1) 
              return false;
          } else if (item.detail_cate === "半年") {
            if (this.date !== "2020-06" && this.date !== "2020-12")
              return false;
          } else if (item.detail_cate === "一年") {
            if (this.date !== "2020-12") 
              return false;
          }
          return true;
        });
      });
    },
    handleDialog() {
      if (this.r_len === this.s_len) {
        this.dialog_process = true;
        this.updateScoreItems();
      }
      else {
        this.dialog = true;
      }
    },
    //批量更新评测表
    updateScoreItems() {
      this.dialog = false;
      this.dialog_process = true;
      this.s_items = this.score_items
        .filter(item => item.unit_score !== 0)
        .map(item => {
          let s_item = {};
          s_item["id"] = item.id;
          s_item["unit_score"] = String(item.unit_score);
          return s_item;
        });
      updateScoreItems(this.s_items, "Token  " + this.$store.state.token).then(res => {
        if (res.data.status === 200) {
          this.dialog_process = false;
          this.snackbar_success = true;
          setTimeout(() => {
            this.$router.push("/index");
          }, 3000);
        } else if (res.data.status === 2) {
          this.process_text = res.data.msg;
        }
      });
    },
    //根据标签进行score_items的筛选
    filterScoreItems(val, index) {
      this.dialog = false
      let i = this.typeIndexs.indexOf(index);
      //如果索引值存在，则删除；没有，则添加。
      if (i > -1) {
        this.typeIndexs.splice(i, 1);
      } else {
        this.typeIndexs.push(index);
      }
      let types = ["unit_score", "major_term", "detail_name", "detail_cate"];
      //如果筛选条件值存在，则删除；没有，则添加。
      if (this.vals[index]) this.vals[index] = "";
      else this.vals[index] = val;
      if (this.typeIndexs.indexOf(0) > -1) {
        if (val === "已填") {
          this.score_items = this.score_items.map(item => {
            if (!item.unit_score) item.isShow = false;
            return item;
          });
        } else if (val === "未填") {
          this.score_items = this.score_items.map(item => {
            if (item.unit_score) item.isShow = false;
            return item;
          });
        }
        return;
      }
      this.score_items = this.score_items.map(item => {
        //生成多条件筛选的bool对象（如f1&&f2&&f3...）
        let filters = this.typeIndexs.reduce((acc, cur) => {
          return acc && item[types[cur]] === this.vals[cur];
        }, true);
        if (filters) item.isShow = true;
        else item.isShow = false;
        return item;
      });
    },
    //根据打分项来更新打分进度
    updateProgress() {
      this.rated_progress = Math.ceil((this.r_len / this.s_len) * 100);
    }
  },
  watch: {
    //响应路由参数变化以便重新请求数据
    $route(to, from) {
      if(to.query.cat!==from.query.cat){
        this.cat = this.$route.query.cat
      }
      this.getScoreItems(this.date);
    },
    //响应日期变化以便重新请求数据
    date(newDate, oldDate) {
      this.score_items=[]
      this.getScoreItems(this.date);
    }
  },
  created() {
    this.getScoreItems(this.date);
  },
};
</script>

<style scoped>
.v-list-item__icon {
  max-width: 30%;
}
</style>