<template>
    <div class="register">
        <el-container style="height:100%">
            <!-- <el-header height="80px">Header</el-header> -->
            <el-main>
                <div class="register_form">
                    <el-form class="form" :rules="rules" ref="form" :model="user" label-width="80px">
                        <h3>注册</h3>
                        <br>
                        <el-form-item label="用户名" prop="username">
                            <el-input class="item" placeholder="请输入用户名" v-model="user.username" clearable auto-complete="off"></el-input>
                        </el-form-item>
                        <el-form-item label="电话" prop="contact_details" >
                            <el-input class="item" placeholder="请输入电话" v-model="user.contact_details" clearable auto-complete="off"></el-input>
                        </el-form-item>
                        <el-form-item label="邮箱" prop="contact_email">
                            <el-input class="item" placeholder="请输入邮箱" v-model="user.contact_email" clearable auto-complete="off"></el-input>
                        </el-form-item>
                        <el-form-item label="地址" prop="contact_address">
                            <el-input class="item" placeholder="请输入地址" v-model="user.contact_address" clearable auto-complete="off"></el-input>
                        </el-form-item>
                        <el-form-item label="设置密码" prop="password">
                            <el-input class="item" placeholder="请设置密码" v-model="user.password" type="password" clearable auto-complete="off"></el-input>
                        </el-form-item>
                        <el-form-item label="确认密码" prop="cpassword">
                            <el-input class="item" placeholder="请确认密码" v-model="user.cpassword" type="password" clearable auto-complete="off"></el-input>
                        </el-form-item>
                        <el-form-item>
                            <el-button type="primary" @click="Submit('form')">提交</el-button>                
                        </el-form-item>
                    </el-form>
                </div>
            </el-main>
        </el-container>
    </div>
</template>
// 密码可尝试强弱进度条，确认密码

<script>

import axios from "axios";

export default{
    name: "register",
    data(){
        var nameReg = /^(?![^A-Za-z]+$)(?![^0-9]+$)[0-9A-Za-z_]{4,15}$/
        var validateUsername = (rule, value, callback) => {
            if(value === "") {
                return callback(new Error("用户名不可为空！"));
            }
            else if(!nameReg.test(value)) {
                callback(new Error("用户名要求为数字、字母、下划线的组合，数字和字母必须存在，长度为4-15个字符"))
            }else {
                callback()
            }
        }

        var phoneReg = /^1[3|4|5|7|8][0-9]{9}$/
        var validatePhone = (rule, value, callback) => {
            if(!value) {
                return callback(new Error("电话号码不可为空！"))
            }
            else if(!phoneReg.test(value)) {
                callback(new Error("请输入有效的联系电话！"))
            }else {
                callback()
            }
        }

        var mailReg = /^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/
        var validateMail = (rule, value, callback) => {
            if(!value) {
                return callback(new Error("邮箱不可为空！"))
            }
            else if(!mailReg.test(value)) {
                callback(new Error("请输入有效的邮箱！"))
            }else {
                callback()
            }
        }

        var passReg = /^[a-zA-Z]\w{6,18}$/
        var validatePass = (rule, value, callback) => {
            if(!value) {
                return callback(new Error("密码不可为空！"))
            }
            else if(!passReg.test(value)) {
                callback(new Error("密码以字母开头,长度在8~18之间,只能包含字母、数字和下划线"))
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
            else if(value !== this.user.password) {
                callback(new Error("两次输入密码不一致！"))
            }else{
                callback()
            }
        }

        return{
            user:{
                username: '',
                contact_details: '',
                contact_email: '',
                contact_address: '',
                password: '',
                cpassword: '',
            },

            rules:{
                username: [{required: true, validator: validateUsername, trigger: 'blur'}],
                contact_details: [{required: true, validator: validatePhone, trigger: 'blur'}],
                contact_email: [{required: true, validator: validateMail, trigger: 'blur'}],
                contact_address: [{required: true, message: "地址不可为空！", trigger: 'blur'}],
                password: [{required: true, validator: validatePass, trigger: 'blur'}],
                cpassword: [{required: true, validator: validateCPass, trigger: 'blur'}],
            },

        }
    },
    methods:{
        Submit:function(form){
            this.$refs[form].validate(valid => {
                if (valid){
                    axios.post("/api/user/", {
                    username: this.user.username,
                    contact_details: this.user.contact_details,
                    contact_email: this.user.contact_email, 
                    contact_address: this.user.address,
                    password: this.user.password, //明文传输密码
                    })
                    .then(response => {
                        console.log("response:",response)
                        if(response.status === 201){
                            this.$router.push({path: "/login"})
                        }else{
                            alert("您输入的用户名已存在！")
                        }
                    }).catch (error => {
                        console.log(error)
                    })
                }else{
                   console.log('error submit!') 
                   return false
                }
            })
        },
    }
}
</script>

<style scoped>
.register{
    position: absolute;
    height: 100%;
    width: 100%;
}
.el-header{
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 60px;
}
.el-main{
    padding: 0;
}
.register_form{
    background-color: #B3C0D1;
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
}
.form{
    width: 40%;
    margin-bottom: 20vh;
    background-color:white;
    border-radius: 2px;
    padding: 5% 3%;
}
.item{
    width: 75%;
}
</style>