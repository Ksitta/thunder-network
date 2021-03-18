<template>
  <div class="wrapper">
    <el-container style="height:100%;">
      <el-header height="80px">
        <!-- Header -->
        <img src="https://www.tsinghua.edu.cn/images/logo_1.svg" alt="logo" class="header-logo">
        <ul class="header-operations">
          <li>标题</li>
          <li>帮助</li>
        </ul>
      </el-header>

      <el-container>
        <el-aside width="240px">
          <!-- Aside -->
          
          <el-menu style="height:100%" @select="menunav">
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
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import userhome from '@/components/userhome'

export default {
  name: 'index',

  components: {
    userhome,
  },

  data: function() {
    return {
      showpage: {
        home: true,

      }
    }
  },

  methods: {
    menunav: function(idx) {
      console.log(idx);
      this.showpage.home = false

      if (idx === "1") {
        this.showpage.home = true
      }
      // menu-item 的点击事件
    },
  },

}
</script>

<style scoped>

.wrapper {
  position: absolute;
  height: 100%;
  width: 100%;
}

.el-header {
  background-color: rgb(77, 146, 214);
}

.header-operations {
  float: right;
  padding-right: 30px;
  height: 100%;
  margin: 0px;
}

.header-operations li {
  color: rgb(255, 255, 255);
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

</style>