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
              <div class="basic_title" style="padding:10px 15px;">
                <div class="title" style="padding:0px 20px;">
                  <h3 align=left style="color:black;">Basic info</h3>
                  <!-- <span style="font-size: 24px; margin-left:-900px;font-weight:bold;color:black;">
                    Basic info
                  </span> -->
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
                    <div>
                    <label class="label_style">Profile Avatar</label>
                    </div>
                    <el-avatar shape="circle" :size="90" :src="avatar_src"></el-avatar>
                  </div>
                </div>
              </div>
          </div>
        </div>
        <div class="colwrapper1">
          <div class="login_info" style=" margin-bottom:30px;">
              <div class="login_title" style="padding:10px 15px;">
                <div class="title" style="padding:0px 20px;">
                  <h3 align=left style="color:black;">Login info</h3>
                  <!-- <span style="font-size: 24px;margin-left:-900px; font-weight:bold;color:black;">
                    Login info
                  </span> -->
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
        <div class="colwrapper1">
          <div class="login_info" style=" margin-bottom:30px;">
              <div class="login_title" style="padding:10px 15px;">
                <div class="title" style="padding:0px 20px;">
                  <h3 align=left style="color:black;">Password</h3>
                  <!-- <span style="font-size: 24px;margin-left:-900px; font-weight:bold;color:black;">
                    Login info
                  </span> -->
                <hr>
                </div>
                <div class="body" style="padding:24px 30px 30px;">
                  <div class="info_detail" style="float:left">
                    <div class="info_col">
                      <el-form class="form" :rules="rules" ref="form" :model="user" label-width="120px">
                          <el-form-item label="原密码:" class = "label_content">
                              <el-input type="password" class="input_content" v-model="user.oldpswd" suffix-icon="el-icon-edit"></el-input>
                          </el-form-item>
                          <hr class="hr_style">
                          <el-form-item label="新密码:" prop="newpswd" class = "label_content">
                              <el-input type="password" class="input_content" v-model="user.newpswd" suffix-icon="el-icon-edit"></el-input>
                          </el-form-item>
                          <hr class="hr_style">
                          <el-form-item label="确认新密码:" prop="cnewpswd" class = "label_content">
                              <el-input type="password" class="input_content" v-model="user.cnewpswd" suffix-icon="el-icon-edit"></el-input>
                          </el-form-item>
                          <!-- <hr class="hr_style">
                          <el-form-item label="密码:" class = "label_content">
                              <el-input class="input_content" v-model="user.password" type="password"></el-input>
                          </el-form-item> -->
                        <el-form-item style="margin-left: 350px;">
                            <el-button type="primary" @click="submit_pswd('form')">确认修改</el-button>                
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
        var passReg = /^\w{6,18}$/
        var validatePass = (rule, value, callback) => {
            if(!value) {
                return callback(new Error("密码不可为空！"))
            }
            else if(!passReg.test(value)) {
                callback(new Error("密码长度在6~18之间,只能包含大小写字母、数字和下划线"))
            }else{
                if(this.cpassword !== "") {
                    this.$refs.form.validateField("cpassword") 
                }callback()
            }
        }

        var validateCPass = (rule, value, callback) => {
            if(!value) {
                return callback(new Error("请输入确认密码！"))
            }
            else if(value !== this.user.newpswd) {
                callback(new Error("两次输入密码不一致！"))
            }else{
                callback()
            }
        }

        return{
            user:{
              username: "",
              contact_details: "",
              contact_email: "",
              contact_address: "",
              user_type: "",
              oldpswd: "",
              newpswd: "",
              cnewpswd: "",
            },
            rules:{
                newpswd: [{required: true, validator: validatePass, trigger: 'blur'}],
                cnewpswd: [{required: true, validator: validateCPass, trigger: 'blur'}],
            },
        }
    },
    created(){
      this.getdata()
      // console.log(this.user)
    },
    methods:{
      getdata: function(){
        axios.get('/api/user/profile/')
        .then((response) => {
          // console.log(response)
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
        // console.log(this.user)
      },
      submit: function(){
        this.$confirm('确认修改信息?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.$emit('userinfoEdited')
          axios.put("api/user/edit/", 
          {
            username: this.user.username,
            contact_details: this.user.contact_details,
            contact_email: this.user.contact_email,
            contact_address: this.user.contact_address,
          })
          .then(response => {   
              console.log("response.status:", response)
              if(response.status === 204){
                  this.$message.success("信息修改成功！");
                  this.getdata()
              }
          }).catch(error => {
              this.$message.error("修改信息失败！")
              console.log(error)
          })
        });
      },
      submit_pswd: function(form) {
        this.$refs[form].validate(valid => {
          if (valid){
            this.$confirm('确认修改密码?', '提示', {
              confirmButtonText: '确定',
              cancelButtonText: '取消',
              type: 'warning'
            }).then(() => {
              this.$emit('userinfoEdited')
              axios.post("api/user/edit/", {
                old_password: md5(this.user.oldpswd),
                password: md5(this.user.newpswd),
              })
              .then(response => {
                console.log("response.status:", response)
                  if(response.status === 201){
                    this.$message.success("密码修改成功！");
                  }
              }).catch(error => {
                if (error.response.status == 400) {
                  this.$message.error("原密码错误！");
                } else {
                  this.$message.error("修改密码失败！");
                }
                console.log(error)
              })
            });
          }
        });
      }
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
