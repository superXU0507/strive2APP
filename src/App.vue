<template>
  <v-app style="background: #E0E0E0">
    <router-view></router-view>
  </v-app>
</template>

<script>
import Index from "./views/Index";
import Login from "./views/Login";

export default {
  name: "App",
  data: () => ({}),
  methods: {},
  components: {
    Index,
    Login
  }
};
</script>

<style lang="sass">
  @import '../node_modules/typeface-roboto/index.css'
</style>