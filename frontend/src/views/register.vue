<template>
    <div class="register">
        <el-container style="height:100%">
            <!-- <el-header height="80px">Header</el-header> -->
            <el-main>
                <div class="register_form">
                    <el-form class="form" rules="rules" ref="form" :model="form" label-width="70px">
                        <h3>注册</h3>
                        <br>
                        <el-form-item label="用户名" >
                            <el-input class="item" placeholder="请输入用户名" v-model="user.name" clearable auto-complete="off"></el-input>
                        </el-form-item>
                        <el-form-item label="联系方式" >
                            <el-input class="item" placeholder="请输入电话或邮件" v-model="user.contact" clearable auto-complete="off"></el-input>
                        </el-form-item>
                        <el-form-item label="地址" >
                            <el-input class="item" placeholder="请输入地址" v-model="user.address" clearable auto-complete="off"></el-input>
                        </el-form-item>
                        <el-form-item label="密码" prop="password">
                            <el-input class="item" placeholder="请输入密码" v-model="user.password" type="password" clearable auto-complete="off"></el-input>
                        </el-form-item>
                        <!-- <el-form-item label="确认密码" prop="repassword">
                            <el-input class="item" placeholder="请确认密码" v-model="repassword" type="password" clearable auto-complete="off"></el-input>
                        </el-form-item> -->
                        <el-form-item>
                            <el-button type="primary" @click="Submit">提交</el-button>                
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
        return{
            //缺失：密码输入规范
            // rules:{
            //     password: [{
            //         required:true, message:'创建密码', trigger:'blur'
            //     }],
            //     repassword:[{
            //         required:true, message:'确认密码', trigger:'blur'
            //     },{
            //         validator:(rule, value, callback)=>{
            //             if(value === ''){
            //                 callback(new Error('请再次输入密码'))
            //             }else if(value != this.password){
            //                 callback(new Error('两次输入密码不一致'))
            //             }else{
            //                 callback()
            //             }
            //         },trigger: 'blur'
            //     }]
            // },
            user:{
                name: '',
                contact: '',
                address: '',
                password: '',
            },
            // repassword: ''
        }
    },
    methods:{
        Submit:function(){
            if(!this.user.name){
                this.$message.error("请输入用户名！")
                return
            // }else if(!this.user.contact){
            //     this.$message.error("请输入联系方式")
            //     return
            // }else if(this.user.contact != null){ //是否要输入电话或邮箱两种联系方式？
            //     var reg= "^(([a-zA-Z0-9_\\-\\.]+)@((\\[[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.)|(([a-zA-Z0-9\\-]+\\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})) | ((13[0-9]|15[0-9]|153|15[6-9]|180|18[23]|18[5-9])\\d{8})$"
            //     if(!this.user.contact.matches(reg)){
            //         this.$message.error("请输入有效的联系方式!")
            //         return
            //     }
            }else if(!this.user.address){
                this.$message.error("请输入联系地址！")
                return
            }else if(!this.user.password){
                this.$message.error("请输入密码！")
                return
            }else{
                axios.post("/api/user/register/", {
                    username: this.user.name,
                    password: this.user.password, //明文传输密码
                    contact_details: this.user.contact,
                    contact_email: 'thunder@thunder.com', // TODO：缺少输入框
                    contact_address: this.user.address,
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
            }
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