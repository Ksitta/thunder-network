<template>
    <div class="orderrequest">
        <div class="login_form">
            <el-form class="form" ref="form" :model="form" label-width="80px">
                <h3>提交订单</h3>
                <br>
                <el-form-item label="站点名称" >
                    <el-input class="item" placeholder="请输入站点名称" v-model="info.site_name" clearable auto-complete="on"></el-input>
                </el-form-item>
                <el-form-item label="站点地址">
                    <el-input class="item" placeholder="请输入站点地址" v-model="info.site_address" clearable auto-complete="off"></el-input>
                </el-form-item>
                <el-form-item>                
                    <el-button type="primary" @click="Submit">提交</el-button>
                </el-form-item>
            </el-form>
            收到的信息：{{retinfo}}
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default{
    name: "orderrequest",
    data(){
        return{
            info:{
                site_name: "",
                site_address: "",
                billing_level: 1,
                demand_num: 0,
                demand_1: "",
                demand_2: "",
                demand_3: "",
            },
            retinfo: "",
        }
    },
    methods:{
        Submit:function(){
            console.log('submit!')
            axios.post("/api/submit/", {
                site_name: this.info.site_name,
                site_address: this.info.site_address,
                billing_level: this.info.billing_level,
                demand_num: this.info.demand_num,
                demand_1: this.info.demand_1,
                demand_2: this.info.demand_2,
                demand_3: this.info.demand_3,
            })
            .then(response => {
                console.log("response:",response)
                if(response.status === 201){
                    this.$message.success("提交成功！")
                    this.retinfo = response.data
                }else{
                    alert(response.status)
                }
            }).catch (error => {
                alert('error！')
                console.log(error)
            })
        },
    }
}
</script>

<style scoped>
/* .register{
    position: absolute;
    height: 100%;
    width: 100%;
} */
/* .el-header{
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 60px;
} */
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
    /* width: 40%; */
    margin-bottom: 20vh;
    background-color:white;
    border-radius: 2px;
    padding: 5% 3%;
}
.item{
    width: 75%;
}
</style>