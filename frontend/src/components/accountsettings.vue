<template>
  <div id="wrapper_accountsettings">
        <div class="head" style=" margin-bottom:10px">
            <div class="head-title" style=" margin-bottom:-10px;margin-top:-20px;margin-left:20px">
              <h1 align="left" style="font-size:40px;">Account Settings</h1>
            </div>
            <div class="head-description" style=" margin-left:20px; margin-top:-45px">
              <span style="color: grey; float:left; font-size:16px;line-height:24px">View and update your account details, profile and more.</span>
            </div>
        </div>
        <div class="colwrapper">
          <div class="basic_info" style=" margin-bottom:30px;">
              <div class="basic_title" style="padding:10px 20px;">
                <div class="title">
                <h3 align="left" style="color:black;">Basic info</h3>
                <!-- <el-tag>{{identity}}</el-tag> -->
                <hr>
                </div>
                <div class="body" style="padding:24px 30px 30px;">
                  <div class="info_detail" style="float:left">
                    <div class="info_col">
                      <el-form class="form" ref="form" :model="form" label-width="70px">
                          <el-form-item label="用户名:" class = "label_content">
                              <el-input class="input_content" v-model="user.username" :disabled="true" suffix-icon="el-icon-lock"></el-input>
                          </el-form-item>
                          <hr class="hr_style">
                          <el-form-item label="邮箱:" class = "label_content">
                              <el-input class="input_content" v-model="user.contact_email" :disabled="true"></el-input>
                          </el-form-item>
                      </el-form>
                    </div>
                  </div>
                  <div class="profile">
                    <label class="label_style">Profile Image</label>
                    <el-avatar shape="circle" :size="90" :src="avatar_src"></el-avatar>
                  </div>
                </div>
              </div>
          </div>
        </div>
        <div class="colwrapper1">
          <div class="login_info" style=" margin-bottom:30px;">
              <div class="login_title" style="padding:10px 20px;">
                <div class="title">
                <h3 align="left" style="color:black;">Login info</h3>
                <hr>
                </div>
                <div class="body" style="padding:24px 30px 30px;">
                  <div class="info_detail" style="float:left">
                    <div class="info_col">
                      <el-form class="form" ref="form" :model="form" label-width="70px">
                          <el-form-item label="邮箱:" class = "label_content">
                              <el-input class="input_content" v-model="user.contact_email" suffix-icon="el-icon-edit"></el-input>
                          </el-form-item>
                          <hr class="hr_style">
                          <el-form-item label="电话:" class = "label_content">
                              <el-input class="input_content" v-model="user.contact_details" suffix-icon="el-icon-edit"></el-input>
                          </el-form-item>
                          <hr class="hr_style">
                          <el-form-item label="地址:" class = "label_content">
                              <el-input class="input_content" v-model="user.contact_address" suffix-icon="el-icon-edit"></el-input>
                          </el-form-item>
                          <!-- <hr class="hr_style">
                          <el-form-item label="密码:" class = "label_content">
                              <el-input class="input_content" v-model="user.password" type="password"></el-input>
                          </el-form-item> -->
                        <el-form-item style="margin-left: 400px;">
                            <el-button type="primary" @click="submit">确认修改</el-button>                
                        </el-form-item>
                      </el-form>
                    </div>
                  </div>
                </div>
              </div>
          </div>
        </div>
  </div>
</template>

<script>

import axios from 'axios'
import { Message } from 'element-ui';
import md5 from 'js-md5'

export default{
    name: "accountsettings",
    data(){
        return{
            user:{}
        }
    },
    created(){
      this.getdata()
    },
    methods:{
      getdata: function(){
        axios.get('/api/user/profile/')
        .then((response) => {
          this.user.username = response.data.user.username
          this.user.contact_details = response.data.user.contact_details
          this.user.contact_email = response.data.user.contact_email
          this.user.contact_address = response.data.user.contact_address
          this.user.user_type = response.data.user.user_type
        })
        .catch((error) => {
          console.log(error)
          Message({
            message: "获取用户信息失败",
            type: "error",
          });
        })
      },
      submit: function(){
        axios.put("api/user/edit/", 
        {
          username: this.user.username,
          contact_details: this.user.contact_details,
          contact_email: this.user.contact_email,
          contact_address: this.user.contact_address,
        })
        .then(response => {   
            console.log("response.status:", response)
            if(response.status === 200){
                this.getdata()
            }
        }).catch(error => {
            this.$message.error("修改信息失败！")
            console.log(error)
        })
      },
    },
    computed: {
      identity: function() {
        if (this.user.user_type == "0") return "用户";
        if (this.user.user_type == "1") return "运营工程师";
        if (this.user.user_type == "2") return "网络工程师";
        return "";
      },
    avatar_src: function() {
      return "https://sdn.geekzu.org/avatar/" + md5(this.user.contact_email);
    }
    }

}
</script>

<style scoped>
.colwrapper {
  background-color: #ffffff;
  border-radius: 10px;
  padding: 0px;
  margin-left: 20px;
  margin-bottom: 0px;
  margin-right: 30px;
  margin-top:90px;
  height: 300px;
}
.colwrapper1 {
  background-color: #ffffff;
  border-radius: 10px;
  padding: 0px;
  margin-left: 20px;
  margin-bottom: 0px;
  margin-right: 30px;
  margin-top:40px;
  height: 450px;
}
.info_detail{
   width: 60%;
   float: left;
   position: relative;
   min-height: 1px;
   padding-right: 15px;
   padding-left: 15px;
   box-sizing: border-box;
}
.profile{
   width: 25%;
   float: left;
   position: relative;
   min-height: 1px;
   padding-right: 15px;
   padding-left: 60px;
   box-sizing: border-box;
}
.input_content >>> .el-input__inner{
  font-size: 16px!important;
  color:rgb(37, 36, 36)!important;
  font-family: cursive!important;  
  border-color: #a9c0ee;   
   
}
.hr_style{
  border: none; 
  border-top: 1px solid #DFE5EB; 
  margin-bottom: 20px;
  margin-top: 20px;
}
.label_style{
    color: #32536a;
    font-weight: thin;
    font-size: 18px;
    position:relative;
    bottom: 10px;;
}
</style>
<style>
.label_content .el-form-item__label{
    color: #32536a;
    font-weight: bold;
    font-size: 16px;
}

</style>
