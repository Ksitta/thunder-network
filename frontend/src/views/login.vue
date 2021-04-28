<template>
    <div class="login">
        <el-container style="height:100%">
            <el-main>
                <div class="login_form">
                    <el-form class="form" ref="form" :model="form" label-width="70px">
                        <h3>登录</h3>
                        <br>
                        <el-form-item label="用户名:" class = "whiteItem">
                            <el-input class="item" placeholder="请输入用户名" v-model="user.name" clearable auto-complete="on"></el-input>
                        </el-form-item>
                        <el-form-item label="密码:" class = "whiteItem">
                            <el-input class="item" placeholder="请输入密码" v-model="user.password" type="password" clearable auto-complete="off"></el-input>
                        </el-form-item>
                        <el-form-item label="身份:" class = "whiteItem">
                            <el-radio-group v-model="user.user_type">
                                <el-radio label="0" class = "whiteItem">用户</el-radio>
                                <el-radio label="1" class = "whiteItem">运营工程师</el-radio>
                                <el-radio label="2" class = "whiteItem">网络工程师</el-radio>
                            </el-radio-group>
                        </el-form-item>
                        <el-form-item style="margin-left: -60px;">
                            <el-button type="register" disabled="true" @click="Register">注册</el-button>                
                            <el-button type="login" @click="Login">登录</el-button>
                        </el-form-item>
                    </el-form>
                </div>
            </el-main>
        </el-container>
    </div>
</template>

<script>

import axios from 'axios'
import md5 from 'js-md5'

export default{
    name: "login",
    data(){
        return{
            user:{
                name: '',
                password: '',
                user_type:''
            }
        }
    },
    methods:{
        Login:function(){
            console.log('Login successful')
            if(!this.user.name){
                this.$message.error("请输入用户名！")
                return
            }else if(!this.user.password){
                this.$message.error("请输入密码！")
                return
            }else if(!this.user.user_type){
                this.$message.error("请选择身份！")
                return
            }else{
                axios.post("/api/user/token/",{
                    username: this.user.name,
                    password: md5(this.user.password),
                    user_type: this.user.user_type,
                })
                .then(response => {   
                    console.log("response.status:", response)
                    if(response.status === 200){
                        this.$store.commit('newtoken', {
                            username: this.user.name,
                            access: response.data.access,
                            refresh: response.data.refresh,
                        })
                        this.$router.push({path: "/"})
                    }
                }).catch(error => {
                    this.$message.error("您输入的用户名或密码错误！")
                    console.log(error)
                })
            }
        },
        Register:function(){
            console.log('skip to registration page')
            this.$router.push({path: '/register'})
        }
    }
}
</script>

<style scoped>
.login{
    background:url("../assets/bg6.jpg");
    width: 100%;
    height: 100%;
    position:fixed;
    background-size:100% 100%;
}
.el-main{
    padding: 0;
}
.login_form{
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
}
.form{
    width: 400px;
    margin-bottom: 20vh;
    margin-right: 5vh;
    background-color: rgba(0, 0, 0, 0.3);
    border-radius: 10px;
    padding: 1% 1%;
    position: relative;
    left: 400px;
    top: 60px;
}
.item{
    width: 75%;
}
</style>
<style>
h3{
    color: white;
    position: relative;
    left: 5px;
    top: 10px;
    font-size: 150%;
}
.whiteItem .el-form-item__label{
    color: white;
    font-weight: bold;
    font-size: 100%;
}
.whiteItem .el-radio__label{
    color:white;
}
.whiteItem .el-radio{
    margin-right: 15px;
}
.el-button--register{
    position: relative;
    left: 25px;
    top: -5px;
    background: transparent;
    color: white;
}
.el-button--login{
    position: relative;
    left: 35px;
    top: -5px;
    background: transparent;
    color: white;
}

</style>