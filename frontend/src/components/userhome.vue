<template>
  <div id="wrapper_userhome">
    <el-container class="container">
      <el-row :gutter="20" id="row_up">
        <el-col :span="8">
          <div class="useravatar">
            <el-avatar :size="150" src="https://bkimg.cdn.bcebos.com/pic/5ab5c9ea15ce36d3d53991f823ba2d87e950342a1be8"></el-avatar>
          </div>
        </el-col>
        <el-col :span="16">
          <div class="userinfo">
            <p>
              姓名：{{info.name}}
            </p>
            <p>
              联系电话：{{info.contact_details}}
            </p>
            <p>
              联系地址：{{info.contact_address}}
            </p>
            <p>
              联系邮箱：{{info.contact_email}}
            </p>
          </div>
        </el-col>
      </el-row>
    </el-container>
  </div>
</template>

<script>

import axios from 'axios'
import { Message } from 'element-ui';


export default {
  name: 'user_home',
  data() {
      return {
        info: {
          username: "User",
          contact_details: "",
          contact_email: "",
          contact_address: "",
        }
      }
  },
  methods: {
    refresh: function() {
      axios.get('/api/user/profile')
      .then((response) => {
        console.log(response.data)
      })
      .catch((error) => {
        console.log(error)
        Message({
          message: "获取用户信息失败",
          type: "error",
        });
      })
    }
  },
  props: {
    show: {
      type: Boolean,
      default: () => false,
    }
  },

  mounted: function() {
    this.refresh()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

#wrapper_userhome {
  height: 100%;
  width: 100%;
}

.container {
  height: 100%;
  margin: auto;
  padding: 60px;
  border-style: dashed;
}

#row_up {
  /* background-color: teal; */
  width: 100%;
  padding: 5%;
}

.userinfo {
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  font-size: 22px;
  padding-top: 20px;
  padding-bottom: 20px;
  padding-left: 60px;
  padding-right: 60px;
  text-align: left;
}

</style>
