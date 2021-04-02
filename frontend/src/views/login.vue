<template>
    <div class="login">
        <el-container style="height:100%">
            <!-- <el-header height="80px">Header</el-header> -->
            <el-main>
                <div class="login_form">
                    <el-form class="form" ref="form" :model="form" label-width="60px">
                        <h3>登录</h3>
                        <br>
                        <el-form-item label="用户名" >
                            <el-input class="item" placeholder="请输入用户名" v-model="user.name" clearable auto-complete="on"></el-input>
                        </el-form-item>
                        <el-form-item label="密码">
                            <el-input class="item" placeholder="请输入密码" v-model="user.password" type="password" clearable auto-complete="off"></el-input>
                        </el-form-item>
                        <el-form-item label="身份">
                            <el-radio-group v-model="user.user_type">
                                <el-radio label="用户"></el-radio>
                                <el-radio label="运营工程师"></el-radio>
                            </el-radio-group>
                        </el-form-item>
                        <el-form-item style="margin-left: -60px;">
                            <el-button type="primary" @click="Register">注册</el-button>                
                            <el-button type="primary" @click="Login">登录</el-button>
                        </el-form-item>
                    </el-form>
                </div>
            </el-main>
        </el-container>
    </div>
</template>

<script>

import axios from 'axios'

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
                    password: this.user.password, //明文传输密码
                    user_type: (this.user.user_type == "用户")? 0 : 1,//身份传输
                })
                .then(response => {   
                    console.log("response.status:", response)
                    if(response.status === 200){
                        this.$store.commit('newtoken', {
                            username: this.user.name,
                            access: response.data.access,
                            refresh: response.data.refresh,
                        })
                        this.$router.push({path: "/index"})
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
.login_form{
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
    border-radius: 10px;
    padding: 5% 3%;
}
.item{
    width: 75%;
}
</style>