<template>
  <v-fab-transition>
    <v-btn v-show="isShow" @click="backTop()" bottom color="pink" dark fab fixed right>
      <v-icon>mdi-chevron-up</v-icon>
    </v-btn>
  </v-fab-transition>
</template>

<script>
import * as easings from 'vuetify/es5/services/goto/easing-patterns'

export default {
  name: "BackTop",
  data() {
    return {
      isShow: false,
      target: 0,
      options: {
        duration: 600,
        offset: 0,
        easing: "easeInOutCubic"
      }
    };
  },
  props: {
    visibilityHeight: {
      // 纵向滑动多远距离出现滚动条
      type: Number,
      default: 100
    },
    backPosition: {
      // 返回顶部时，滚动到哪里（距离顶部的距离）
      type: Number,
      default: 0
    }
  },
  methods: {
    handleScroll() {
      this.isShow =
        (window.pageYOffset ||
          document.documentElement.scrollTop ||
          document.body.scrollTop) > this.visibilityHeight;
    },
    backTop() {
      this.$vuetify.goTo(this.target, this.options);
    }
  },
  mounted() {
    window.addEventListener("scroll", this.handleScroll);
  },
  beforeDestroy() {
    window.removeEventListener("scroll", this.handleScroll);
  }
};
</script>

<style scoped>
</style>