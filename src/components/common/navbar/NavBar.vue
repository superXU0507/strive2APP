<template>
  <div>
    <v-navigation-drawer 
      v-model="drawer" 
      :clipped="$vuetify.breakpoint.lgAndUp" 
      app
    >
      <v-list dense>
        <v-container fluid>
          <v-row>
            <v-col :cols="12">
              <v-card
                max-width="700"
                outlined
              >
                  <v-img
                    class="white--text align-end" 
                    src="@/assets/img3.jpg"
                  >
                    <v-card-title>边防第三五一团</v-card-title>
                    <!-- <v-card-subtitle>人民解放军77643部队</v-card-subtitle> -->
                  </v-img>
              </v-card>
            </v-col>
          </v-row>
        </v-container>
        <v-divider></v-divider>
        <template v-for="item in items">
          <v-list-group
            v-if="item.children"
            :key="item.text"
            v-model="item.model"
            :prepend-icon="item.disabled ? item['icon-alt'] : item.icon "
            append-icon
            :disabled="item.disabled"
            color="light-blue darken-2"
            no-action
          >
            <template v-slot:activator>
              <v-list-item-content>
                <v-list-item-title>{{ item.text }}</v-list-item-title>
              </v-list-item-content>
            </template>
            <v-list-item v-for="(child, i) in item.children" :key="i" :to="child.to" link>
              <v-list-item-action v-if="child.icon">
                <v-icon>{{ child.icon }}</v-icon>
              </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>{{child.text}}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-group>
          <v-list-item v-else :key="item.text" :to="item.to" color="light-blue darken-2" link>
            <v-list-item-action>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>{{ item.text }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </template>
      </v-list>
    </v-navigation-drawer>

    <!-- <v-app-bar :clipped-left="$vuetify.breakpoint.lgAndUp" app color="blue darken-3" dark> -->
      <v-app-bar
      :clipped-left="$vuetify.breakpoint.lgAndUp"
      app
      fixed
      color="blue darken-3"
      dark
      shrink-on-scroll
      prominent
      short
      src="@/assets/img3.jpg"
      class="text-center"
      >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title style="width: 300px" class="ml-0 pl-4">
        <span class="hidden-sm-and-down">"双争"考评系统</span>
      </v-toolbar-title>
      <v-spacer />
      <!-- <v-chip > -->
      <v-btn icon v-if="user.unitName" @click="logOut()">
        <v-icon>mdi-logout</v-icon>
      </v-btn>
      <v-btn icon v-else @click="logIn()">
        <v-icon>mdi-login</v-icon>
      </v-btn>
      <v-avatar v-show="user.userImg">
        <!-- <v-icon dark>mdi-account-circle</v-icon> -->
        <img :src="user.userImg" :alt="user.unitName" />
      </v-avatar>
      {{user.unitName}}
      <!-- </v-chip> -->
    </v-app-bar>
  </div>
</template>

<script>
// import store from "@/store";

export default {
  name: "NavBar",
  data: () => ({
    drawer: null
  }),
  components: {},
  methods: {
    logOut() {
      this.$store.commit("logOut");
    },
    logIn() {
      this.$router.push("/login");
    }
  },
  computed: {
    items() {
      //导航列表
      let items = [];
      //一级导航:主页
      let item_index = { icon: "mdi-home", text: "主页", to: "/index" };
      //一级导航:排名
      let item_rank = { icon: "mdi-poll", text: "排名", to: "/rank" };
      //一级导航栏:机关
      let item_instit = {
        icon: "mdi-plus",
        "icon-alt": "mdi-cancel",
        text: "机关",
        disabled: false,
        model: false,
        children: [
          {
            icon: "mdi-account-arrow-left",
            text: "机关自查",
            to: { name: "scoreList", params: { cat: "self" } }
          },
          {
            icon: "mdi-account-arrow-right",
            text: "双向测评",
            to: { name: "scoreList", params: { cat: "others" } }
          }
        ]
      };
      //一级导航栏:基层
      let item_basis = {
        icon: "mdi-plus",
        "icon-alt": "mdi-cancel",
        text: "基层",
        disabled: false,
        model: false,
        children: [
          {
            icon: "mdi-account-arrow-left",
            text: "基层自查",
            to: { name: "scoreList", params: { cat: "self" } }
            // {
            //   name: "score",
            //   params: {
            //     unit_name: store.state.user.unitName || "",
            //     scorer: "基层"
            //   }
            // }
          },
          {
            icon: "mdi-account-arrow-right",
            text: "双向测评",
            to: { name: "scoreList", params: { cat: "others" } }
          }
        ]
      };
      item_instit.disabled = this.$store.state.user.userMajorCate !== "机关";
      item_instit.model = !(this.$store.state.user.userMajorCate !== "机关");
      item_basis.disabled = this.$store.state.user.userMajorCate !== "基层";
      item_basis.model = !(this.$store.state.user.userMajorCate !== "基层");
      items.push(item_index);
      items.push(item_rank);
      items.push(item_instit);
      items.push(item_basis);
      return items;
    },
    user() {
      return this.$store.state.user;
    }
  }
};
</script>

<style scoped>
</style>