<template>
    <div class="register">
        <el-container style="height:100%">
            <el-header height="80px">Header</el-header>
            <el-main>
                <div class="register_form">
                    <el-form class="form" rules="rules" ref="form" :model="form" label-width="70px">
                        <h3>注册</h3>
                        <el-form-item label="用户名" >
                            <el-input class="item" placeholder="请输入用户名" v-model="name"></el-input>
                        </el-form-item>
                        <el-form-item label="联系方式" >
                            <el-input class="item" placeholder="请输入电话或邮件" v-model="contact"></el-input>
                        </el-form-item>
                        <el-form-item label="地址" >
                            <el-input class="item" placeholder="请输入地址" v-model="address"></el-input>
                        </el-form-item>
                        <el-form-item label="密码" prop="password">
                            <el-input class="item" placeholder="请输入密码" v-model="password"></el-input>
                        </el-form-item>
                        <el-form-item label="确认密码" prop="repassword">
                            <el-input class="item" placeholder="请确认密码" v-model="repassword"></el-input>
                        </el-form-item>
                        <el-form-item>
                            <el-button type="primary" @click="Submit">提交</el-button>                
                        </el-form-item>
                    </el-form>
                </div>
            </el-main>
        </el-container>
    </div>
</template>

<script>
    export default{
        name: "register",
        data(){
            return{
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
                name: '',
                contact: '',
                address: '',
                password: '',
                repassword: ''
            }
        },
        methods:{
            Submit(){
                console.log('Submit successful')
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