<template>
  <v-content>
    <v-container class="fill-height" fluid :style="{backgroundImage: 'url(' + bgPath + ')' }">
      <v-row align="center" justify="center">
        <v-col cols="12" sm="8" md="4">
          <v-card class="elevation-12">
            <v-toolbar color="red" dark flat>
              <v-toolbar-title>登录</v-toolbar-title>
              <v-spacer />
            </v-toolbar>
            <v-card-text>
              <v-form ref="form" v-model="valid" lazy-validation>
                <v-text-field
                  v-model="username"
                  label="用户名"
                  name="login"
                  type="text"
                  :rules="usernameRules"
                  required
                />
                <v-text-field
                  v-model="password"
                  id="password"
                  label="密码"
                  name="password"
                  type="password"
                  :rules="passwordRules"
                  required
                />
              </v-form>
            </v-card-text>
            <v-card-actions>
              <v-spacer />
              <p>{{errorMessage}}</p>
              <v-btn :disabled="!valid" color="primary" @click="logIn">提交</v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-content>
</template>

<script>
import bgPath from "@/assets/img2.jpg"
export default {
  name: "Login",
  data() {
    return {
      valid: true,
      username: "",
      password: "",
      usernameRules: [v => !!v || "请填写用户名"],
      passwordRules: [v => !!v || "请填写密码"],
      errorMessage: "",
      bgPath: bgPath
    };
  },
  methods: {
    logIn() {
      const username = this.username;
      const password = this.password;
      const payload = {
        username,
        password
      };
      if (this.$refs.form.validate()) {
        this.$store
          .dispatch("logIn", payload)
          .then(res => {
            console.log(res);
            this.$router.go(-1);
          })
          .catch(error => {
            console.log(error);
            console.log(error.response);
          });
      }
    }
  },
  components: {},
  mounted() {}
};
</script>

<style scoped>

</style>