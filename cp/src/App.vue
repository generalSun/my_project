<template>
  <div id="app">
    <a-config-provider :locale="$t('language')">
      <a-layout id="layout-custom-trigger">
        <a-layout-sider v-model="collapsed" :trigger="null" collapsible>
          <div class="logo" />
          <NavView :navList="navList"></NavView>
        </a-layout-sider>
        <a-layout>
          <a-layout-header style="background: #fff; padding: 0">
            <LayoutHeader
              :collapsed="collapsed"
              @changeCllapsed="changeCllapsed"
            ></LayoutHeader>
          </a-layout-header>
          <a-layout-content
            :style="{
              margin: '12px 8px',
              padding: '12px',
              background: '#fff',
              minHeight: '280px',
              overflow: 'auto',
            }"
          >
            <router-view v-if="isRouterAlive" />
          </a-layout-content>
        </a-layout>
      </a-layout>
    </a-config-provider>
  </div>
</template>

<script>
// @ is an alias to /src
import NavView from "@/views/NavView.vue";
import LayoutHeader from "@/views/LayoutHeader.vue";
import { requestUrl, request } from "@/utils/Http.js";

export default {
  name: "App",
  components: {
    NavView,
    LayoutHeader,
  },
  data: function () {
    return {
      navList: [],
      isRouterAlive: true,
      collapsed: false,
    };
  },
  watch: {
    "$i18n.locale": function (newVal) {
      if (newVal == "zh") {
        this.$moment.locale("zh-cn");
      } else {
        this.$moment.locale("en");
      }
    },
  },
  provide() {
    return {
      reload: this.reload,
    };
  },
  created() {
    // 当 vm 实例 的 data 和 methods 初始化完毕后，vm实例会自动执行created 这个生命周期函数
    this.$router.push("/");
    request(requestUrl("api/navList/"), "get").then((response) => {
      this.navList = response.data;
    });
  },
  methods: {
    reload() {
      this.isRouterAlive = false;
      this.$nextTick(function () {
        this.isRouterAlive = true;
      });
    },
    changeCllapsed: function (collapsed) {
      this.collapsed = !collapsed;
    },
  },
};
</script>

<style lang="scss">
* {
  margin: 0;
  padding: 0;
}

body,
html {
  width: 100vw;
  height: 100vh;
}

#app {
  width: 100%;
  height: 100%;
  overflow: hidden;
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#layout-custom-trigger {
  width: 100%;
  height: 100%;
}

#layout-custom-trigger .logo {
  height: 32px;
  background: rgba(255, 255, 255, 0.2);
  margin: 16px;
}

// .ant-layout-header {
//   overflow: hidden;
// }
</style>
