<template>
    <div class="login">
        <el-container style="height:100%">
            <el-header height="80px">Header</el-header>
            <el-main>
                <div class="login_form">
                    <el-form class="form" ref="form" :model="form" label-width="60px">
                        <el-form-item label="用户名" >
                            <el-input class="item" placeholder="请输入用户名" v-model="name"></el-input>
                        </el-form-item>
                        <el-form-item label="密码">
                            <el-input class="item" placeholder="请输入密码" v-model="password"></el-input>
                        </el-form-item>
                        <el-form-item label="身份">
                            <el-radio-group v-model="identity">
                                <el-radio label="用户"></el-radio>
                                <el-radio label="运营工程师"></el-radio>
                            </el-radio-group>
                        </el-form-item>
                        <el-form-item>
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
    export default{
        name: "login",
        data(){
            return{
                name: '',
                password: '',
                identity:''
            }
        },
        methods:{
            Login(){
                console.log('Login successful')
            },
            Register(){
                console.log('skip to registration page')
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
    border-radius: 2px;
    padding: 5% 3%;
}
.item{
    width: 75%;
}
</style>