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

            <el-menu-item index="2">
              <i class="el-icon-setting"></i>
              <span>订单查询</span>
            </el-menu-item>

            <el-menu-item index="3">
              <i class="el-icon-data-analysis"></i>
              <span>流量查询</span>
            </el-menu-item>

            <el-menu-item index="8">
              <i class="el-icon-bank-card"></i>
              <span>费用查询</span>
            </el-menu-item>

            <el-menu-item index="9">
              <i class="el-icon-edit-outline"></i>
              <span>新建工单</span>
            </el-menu-item>
            <el-menu-item index="10">
              <i class="el-icon-message"></i>
              <span>我的工单</span>
            </el-menu-item>

          </el-menu>

          <el-menu v-if="getIdentity == 1" background-color="#131720" style="height:100%" @select="menunav">
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

            <!-- 5 -->

          </el-menu>

          <el-menu v-if="getIdentity == 2" background-color="#131720" style="height:100%" @select="menunav">
            <!-- Menu -->
            <el-menu-item class="menu-homeitem"
              index="1"
              >
              <i class="el-icon-menu"></i>
              <span>主页</span>
            </el-menu-item>

            <el-menu-item class="menu-homeitem"
              index="6"
              >
              <i class="el-icon-s-claim"></i>
              <span>订单管理</span>
            </el-menu-item>

          </el-menu>

        </el-aside>

        <el-main>
          <!-- Main -->
          <userhome ref="userhome" v-bind:show="showpage.home" v-if="showHome == 0"></userhome>
          <managerhome ref="userhome" v-bind:show="showpage.home" v-if="showHome == 1"></managerhome>
          <engineerhome ref="userhome" v-bind:show="showpage.home" v-if="showHome == 2"></engineerhome>
          <sitequery ref="sitequery" v-bind:show="showpage.sitequery" v-if="showpage.sitequery"></sitequery>
          <accountsettings ref="accountsettings" v-bind:show="showpage.accountsettings" v-if="showpage.accountsettings"></accountsettings>
          <flow ref="flow" v-bind:show="showpage.flow" v-if="showpage.flow"></flow>
          <orderprocessing ref="orderprocessing" v-bind:show="showpage.orderprocessing" v-if="showpage.orderprocessing"></orderprocessing>
          <networkorder ref="networkorder" v-bind:show="showpage.networkorder" v-if="showpage.networkorder"></networkorder>
          <charges ref="charges" v-bind:show="showpage.charges" v-if="showpage.charges"></charges>
          <newtickets ref="newtickets" v-bind:show="showpage.newtickets" v-if="showpage.newtickets" @userinfoEdited="userinfoEdited"></newtickets>
          <mytickets ref="mytickets" v-bind:show="showpage.mytickets" v-if="showpage.mytickets"></mytickets>
        </el-main>
        <el-main class="loading-area" />
      </el-container>
    </el-container>
  </div>
</template>

<script>
import userhome from '@/components/userhome'
import managerhome from '@/components/managerhome'
import engineerhome from '@/components/engineerhome'
import sitequery from '@/components/sitequery'
import accountsettings from '@/components/accountsettings'
import orderprocessing from '@/components/orderprocessing'
import networkorder from '@/components/networkorder'
import flow from '@/components/flow'
import charges from '@/components/charges'
import newtickets from '@/components/newtickets'
import mytickets from '@/components/mytickets'

import axios from 'axios'

export default {
  name: 'index',

  components: {
    userhome,
    managerhome,
    engineerhome,
    sitequery,
    accountsettings,
    orderprocessing,
    networkorder,
    flow,
    charges,
    newtickets,
    mytickets,
  },

  data: function() {
    return {
      showpage: {
        home: true,
        sitequery: false,
        accountsettings: false,
        orderprocessing: false,
        networkorder: false,
        flow: false,
        charges: false,
        newtickets:false,
        mytickets:false,
      }
    }
  },

  methods: {
    allclear: function() {
      this.showpage.home = false
      this.showpage.accountsettings = false
      this.showpage.flow = false
      this.showpage.sitequery = false
      this.showpage.orderprocessing = false
      this.showpage.networkorder = false
      this.showpage.charges = false
      this.showpage.newtickets = false
      this.showpage.mytickets = false
    },
    menunav: function(idx) { // menu-item 的点击事件
      console.log(idx);
      this.allclear();
      if (idx === "1") {
        this.showpage.home = true
      }
      if (idx === "2") {
        this.showpage.sitequery = true
      }
      if (idx === "3") {
        this.showpage.flow = true
      }
      if (idx === "4") {
        this.showpage.orderprocessing = true
      }
      if (idx === "5") {
        0;
      }
      if (idx === "6") {
        this.showpage.networkorder = true
      }
      if (idx === "7") {
        0;
      }
      if (idx === "8") {
        this.showpage.charges = true
      }
      if (idx === "9") {
        this.showpage.newtickets = true
      }
      if (idx === "10") {
        this.showpage.mytickets = true
      }
    },
    userCommand: function(command) {
      console.log(command);
      if (command == "edit") {
        this.allclear();
        this.showpage.accountsettings = true
      }
      if (command == "quit") {
        sessionStorage.setItem('user_token', '')
        sessionStorage.setItem('user_refresh', '')
        sessionStorage.setItem('user_name', '')
        this.$router.push({path: "/login"})
      }
    },
    userinfoEdited: function(){
      this.allclear();
      this.showpage.mytickets = true
    },
    getUsertype: function() {
      axios.get('/api/user/profile/')
      .then((response) => {
        this.$store.commit('newtype', {
            type: response.data.user.user_type
        })
      })
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
    },
    showHome: function() {
      if (!this.showpage.home) return -1;
      if (this.$store.state.user_type == null) {
        this.getUsertype();
      }
      return this.$store.state.user_type == null ? -1 : this.$store.state.user_type;
    },
  }

}
</script>

<style>
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
</style>

<style scoped>

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

.loading-area {
  background: rgb(255, 255, 255, 0);
  pointer-events: none;
  top: 48px;
  left: 228px;
  right: 0px;
  bottom: 0px;
  position: absolute;
}

</style>