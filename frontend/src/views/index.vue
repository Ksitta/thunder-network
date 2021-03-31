<template>
  <div class="wrapper">
    <el-container style="height:100%;">
      <el-header height="80px">
        <!-- Header -->
        <a href="/">
          <img src="web-logo.png" alt="logo" class="header-logo">
        </a>

      <el-dropdown @command="userCommand">
        <span class="el-dropdown-link">
          {{getUsername}}
          <i class="el-icon-arrow-down el-icon--right"></i>
        </span>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item icon="el-icon-edit" command="edit">修改信息</el-dropdown-item>
          <el-dropdown-item icon="el-icon-s-operation" command="quit">退出登录</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>

        <!-- <ul class="header-operations">
          <li>标题</li>
          <li>帮助</li>
        </ul> -->
      </el-header>

      <el-container>
        <el-aside width="240px">
          <!-- Aside -->
          
          <el-menu background-color="#fbfcfe" style="height:100%" @select="menunav">
            <!-- Menu -->
            <el-menu-item
              index="1"
              >
              <i class="el-icon-menu"></i>
              <span>主页</span>
            </el-menu-item>

            <el-submenu index="2">
              <template slot="title">
                <i class="el-icon-message"></i>
                <span>订单</span>
              </template>
              <el-menu-item index="2-1">
                <i class="el-icon-document"></i>
                <span>新建订单</span>
              </el-menu-item>
              <el-menu-item index="2-2">
                <i class="el-icon-setting"></i>
                <span>订单查询</span>
              </el-menu-item>
            </el-submenu>

            <el-submenu index="3">
              <template slot="title">
                <i class="el-icon-s-platform"></i>
                <span>网络</span>
              </template>
              <el-menu-item index="3-1">
                <i class="el-icon-data-analysis"></i>
                <span>业务查询</span>
              </el-menu-item>
              <el-menu-item index="3-2">
                <i class="el-icon-data-analysis"></i>
                <span>设备查询</span>
              </el-menu-item>
            </el-submenu>

          </el-menu>

        </el-aside>

        <el-main>
          <!-- Main -->
          <userhome ref="userhome" v-bind:show="showpage.home" v-if="showpage.home"></userhome>
          <sitequery ref="sitequery" v-bind:show="showpage.sitequery" v-if="showpage.sitequery"></sitequery>
          <orderrequest ref="orderrequest" v-bind:show="showpage.orderrequest" v-if="showpage.orderrequest"></orderrequest>
          
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import userhome from '@/components/userhome'
import sitequery from '../components/sitequery.vue';
import orderrequest from '@/components/orderrequest'

export default {
  name: 'index',

  components: {
    userhome,
    sitequery,
    orderrequest,
  },

  data: function() {
    return {
      showpage: {
        home: true,
        sitequery: false,
        orderrequest: false
      }
    }
  },

  methods: {
    menunav: function(idx) { // menu-item 的点击事件
      console.log(idx);
      this.showpage.home = false
      this.showpage.orderrequest = false
      this.showpage.sitequery = false
      if (idx === "1") {
        this.showpage.home = true
      }
      if (idx === "2-1") {
        this.showpage.orderrequest = true
      }
      if(idx === "3-1") {
        this.showpage.sitequery = true
      }
    },
    userCommand: function(command) {
      console.log(command);
      if (command == "quit") {
        sessionStorage.setItem('user_token', '')
        sessionStorage.setItem('user_refresh', '')
        sessionStorage.setItem('user_name', '')
        this.$router.push({path: "/login"})
      }
    }
  },

  computed: {
    getUsername: function() {
      let name = this.$store.state.user_name;
      return name ? name : "Unknown User";
    }
  }

}
</script>

<style scoped>

.wrapper {
  position: absolute;
  height: 100%;
  width: 100%;
}

.el-header {
  background-color: rgb(188, 209, 233);
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.2);
  /* border-radius: 30px; */
}

.el-main {
  /* background-color: rgb(251, 252, 254); */
  background-color: #eef3fa;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.2);
  border-radius: 0px 30px 30px 0px;
}

.el-menu {
  /* background-color: rgb(238, 243, 250); */
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.2);
  border-radius: 30px 0px 0px 30px;
}

.el-menu-item {
  margin:10px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  border-radius: 20px;
}

.header-operations {
  float: right;
  padding-right: 30px;
  height: 100%;
  margin: 0px;
}

.header-operations li {
  /* color: rgb(255, 255, 255); */
  color: rgb(0, 0, 0);
  display: inline-block;
  vertical-align: middle;
  line-height: 80px;
  cursor: pointer;
  padding: 0px 20px;
}

.header-logo {
  height: 60px;
  margin: 10px;
  float: left;
}

.el-dropdown{
  float: right;
  margin-right: 20px;
  /* line-height: 80px; */
  margin-top: 32px;
  font-size: 16px;
}

.el-dropdown-link{
  /* color: white; */
  color: black;
  cursor: pointer;
  font-weight: bold;
}

</style>