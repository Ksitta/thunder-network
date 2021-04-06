<template>
  <div id="wrapper_userhome">
    <el-container class="container">
      <el-row :gutter="20" id="row_up">
        <el-col :span="8">
          <div class="useravatar">
            <el-avatar :size="150" src="user.jfif"></el-avatar>
          </div>
        </el-col>
        <el-col :span="16">
          <div class="userinfo">
            <p>
              <span style="font-size: 40px;">
                您好
              </span>
              <span>
                ，{{info.username}}
              </span>
              <el-tag>{{identity}}</el-tag>
            </p>
            <el-divider></el-divider>
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
          username: "",
          contact_details: "",
          contact_email: "",
          contact_address: "",
          user_type: "",
        }
      }
  },
  methods: {
    refresh: function() {
      console.log('refresh userhome!')
      axios.get('/api/user/profile/')
      .then((response) => {
        console.log(response)
        console.log(response.data.user)
        this.info.username = response.data.user.username
        this.info.contact_details = response.data.user.contact_details
        this.info.contact_email = response.data.user.contact_email
        this.info.contact_address = response.data.user.contact_address
        this.info.user_type = response.data.user.user_type
        this.$store.commit('newtype', {
            type: this.info.user_type
        })
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

  computed: {
    identity: function() {
      if (this.info.user_type == "0") return "用户";
      if (this.info.user_type == "1") return "运营工程师";
      if (this.info.user_type == "2") return "网络工程师";
      return "";
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
  /* border-style: dashed; */
}

#row_up {
  /* background-color: teal; */
  width: 100%;
  padding: 5%;
}

.userinfo {
  background-color: rgb(251, 252, 254);
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  font-size: 22px;
  padding-top: 20px;
  padding-bottom: 20px;
  padding-left: 60px;
  padding-right: 60px;
  text-align: left;
}

.el-tag {
  font-size: 12px;
  font-weight: bold;
}

</style>
