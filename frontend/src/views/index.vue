<template>
  <div class="wrapper">
    <el-container style="height:100%;">
      <el-header height="48px">
        <!-- Header -->
        <!-- <a href="/">
          <img src="web-logo.png" alt="logo" class="header-logo">
        </a> -->
        <a href="/" id="title-a">
          <span class="title">
            Thunder Network
          </span>
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
        <el-aside width="228px">
          <!-- Aside -->
          
          <el-menu v-if="getIdentity == 0" background-color="#131720" @select="menunav">
            <!-- Menu -->
            <div style="vertical-align: middle;">
            <el-menu-item class="menu-homeitem" index="1">
              <i class="el-icon-menu"></i>
              <span>主页</span>
            </el-menu-item>
            </div>

            <el-menu-item index="3-1">
              <i class="el-icon-setting"></i>
              <span>订单查询</span>
            </el-menu-item>

            <el-menu-item index="2-1">
              <i class="el-icon-data-analysis"></i>
              <span>业务查询</span>
            </el-menu-item>

            <!-- <el-submenu index="2">
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
            </el-submenu> -->

          </el-menu>

          <el-menu v-if="getIdentity == 1" background-color="#fbfcfe" style="height:100%" @select="menunav">
            <!-- Menu -->
            <el-menu-item class="menu-homeitem"
              index="1"
              >
              <i class="el-icon-menu"></i>
              <span>主页</span>
            </el-menu-item>

            <el-menu-item class="menu-homeitem"
              index="4"
              >
              <i class="el-icon-s-claim"></i>
              <span>订单管理</span>
            </el-menu-item>

          </el-menu>

        </el-aside>

        <el-main class="loading-area">
          <!-- Main -->
          <userhome ref="userhome" v-bind:show="showpage.home" v-if="showpage.home"></userhome>
          <sitequery ref="sitequery" v-bind:show="showpage.sitequery" v-if="showpage.sitequery"></sitequery>
          <accountsettings ref="accountsettings" v-bind:show="showpage.accountsettings" v-if="showpage.accountsettings"></accountsettings>
          <orderprocessing ref="orderprocessing" v-bind:show="showpage.orderprocessing" v-if="showpage.orderprocessing"></orderprocessing>
          <networkorder ref="networkorder" v-bind:show="showpage.networkorder" v-if="showpage.networkorder"></networkorder>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import userhome from '@/components/userhome'
import sitequery from '@/components/sitequery'
import accountsettings from '@/components/accountsettings'
import orderprocessing from '@/components/orderprocessing'
import networkorder from '@/components/networkorder'

export default {
  name: 'index',

  components: {
    userhome,
    sitequery,
    accountsettings,
    orderprocessing,
    networkorder,
  },

  data: function() {
    return {
      showpage: {
        home: true,
        sitequery: false,
        accountsettings: false,
        orderprocessing: false,
        networkorder: false,
      }
    }
  },

  methods: {
    menunav: function(idx) { // menu-item 的点击事件
      console.log(idx);
      this.showpage.home = false
      this.showpage.accountsettings = false
      this.showpage.sitequery = false
      this.showpage.orderprocessing = false
      this.showpage.networkorder = false
      if (idx === "1") {
        this.showpage.home = true
      }
      if (idx === "2-1") {
        this.showpage.networkorder = true
      }
      if(idx === "3-1") {
        this.showpage.sitequery = true
      }
      if(idx === "4") {
        this.showpage.orderprocessing = true
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
    },
    getIdentity: function() {
      let user_type = this.$store.state.user_type;
      return user_type;
    }
  }

}
</script>

<style scoped>

/* 滚动条样式修改 */
::-webkit-scrollbar {
  width: 7px;
  height: 5px;
  border-radius:15px;
  -webkit-border-radius:  15px;
}
::-webkit-scrollbar-track-piece {
  background-color: #ffff;
  border-radius:15px;
  -webkit-border-radius:  15px;
}
::-webkit-scrollbar-thumb:vertical {
  height: 5px;
  background-color: rgba(144, 147, 153, 0.5);
  border-radius: 15px;
  -webkit-border-radius:  15px;
}
::-webkit-scrollbar-thumb:horizontal {
  width: 7px;
  background-color: rgba(144, 147, 153, 0.5);
  border-radius:  15px;  
  -webkit-border-radius: 15px;
}

.wrapper {
  position: absolute;
  height: 100%;
  width: 100%;
}

.el-header {
  background-color: #ffffff;
  box-shadow: 0 1px 5px 0 rgba(41,85,115,.21);
  z-index: 2000;
}

.el-main {
  background-color: #dfe5eb;
  top: 48px;
  left: 228px;
  right: 0px;
  bottom: 0px;
  position: absolute;
}

/* .el-submenu {
  margin: 10px;
  box-shadow: 0 2px 12px 0 rgba(0,0,0,.1);
  border-radius: 30px;
} */

.el-menu {
  height: 100%;
  border: 0px;
}

.el-menu-item {
  height: 40px;
  line-height: 40px;
  text-align: start;
  color: #ffffff;
  font-weight: 600;
  margin-top: 6px;
}

.menu-homeitem {
  margin-top: 12px;
}

#titlea:active {
  color: black;
}

.title {
  color: black;
  line-height: 48px;
  float: left;
  font-weight: 800;
}

.header-logo {
  height: 44px;
  margin-top: 2px;
  margin-bottom: 2px;
  margin-left: 0px;
  float: left;
}

.el-dropdown{
  float: right;
  margin-right: 20px;
  /* line-height: 48px; */
  margin-top: 16px;
  font-size: 16px;
}

.el-dropdown-link{
  color: black;
  cursor: pointer;
  font-weight: bold;
}

</style>