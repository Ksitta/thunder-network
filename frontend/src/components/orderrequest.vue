<template>
    <div class="orderrequest">
        <div class="submit_form">
            <el-form class="form" ref="form" label-width="80px" label-position="left">
                <h3>提交订单</h3>
                <br>
                <el-form-item label="站点名称" >
                    <el-input class="item" placeholder="请输入站点名称" v-model="info.site_name" clearable auto-complete="on"></el-input>
                </el-form-item>
                <el-form-item label="站点地址">
                    <el-input class="item" placeholder="请输入站点地址" v-model="info.site_address" clearable auto-complete="off"></el-input>
                </el-form-item>
                <el-form-item label="计费方式">
                    <div style="padding-left: 20px; padding-right: 20px;">
                        <el-radio v-model="info.billing_level" label="1" border size="medium">按月计费</el-radio>
                        <el-radio v-model="info.billing_level" label="2" border size="medium">按年计费</el-radio>
                    </div>
                </el-form-item>

                <el-form-item
                v-for="(demand, index) in info.demands"
                :label="'网络需求' + (index + 1)"
                :key="demand.key"
                >
                <!-- :prop="'domains.' + index + '.value'"> -->
                    <el-input v-model="demand.value" class="demand_input"></el-input>
                    <el-button @click.prevent="removeDemand(demand)" class="demand_deletebtn">删除</el-button>
                </el-form-item>

                <el-form-item>
                    <!-- <el-button type="primary" @click="submitForm('dynamicValidateForm')">提交</el-button> -->
                    <el-button @click="addDemand" :disabled="fullDemands" style="margin-left: -80px;">新增虚拟网络需求</el-button>
                    <!-- <el-button @click="resetForm('dynamicValidateForm')">重置</el-button> -->
                </el-form-item>

                <el-form-item>
                    <el-button type="primary" @click="Submit" style="margin-left: -80px;">提交</el-button>
                </el-form-item>
            </el-form>
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
                billing_level: "",
                // demand_num: 0,
                demands: [{
                    value: ""
                }],
            },
        }
    },
    methods:{
        Submit:function(){
            let submitinfo = {
                site_name: this.info.site_name,
                site_address: this.info.site_address,
                billing_level: parseInt(this.info.billing_level),
                demand_num: this.info.demands.length,
                demand_1: "",
                demand_2: "",
                demand_3: "",
            }
            if (this.info.demands.length >= 1) {
                submitinfo.demand_1 = this.info.demands[0].value
            }
            if (this.info.demands.length >= 2) {
                submitinfo.demand_2 = this.info.demands[1].value
            }
            if (this.info.demands.length >= 3) {
                submitinfo.demand_3 = this.info.demands[2].value
            }
            console.log(submitinfo)
            axios.post("/api/submit/", submitinfo)
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
        addDemand: function() {
            this.info.demands.push({
                value: "",
                key: Date.now()
            })
        },
        removeDemand: function(demand) {
            let index = this.info.demands.indexOf(demand)
            if (index !== -1) {
                this.info.demands.splice(index, 1)
            }
        }
    },
    computed: {
        fullDemands: function() {
            return this.info.demands.length >= 3;
        }
    }

}
</script>

<style scoped>
.orderrequest {
    height: 100%;
}
.submit_form {
    /* background-color: #B3C0D1; */
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
}
.form {
    /* width: 40%; */
    /* margin-bottom: 20vh; */
    background-color:white;
    border-radius: 20px;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    padding: 20px 60px 10px 60px;
}
.item {
    width: 90%;
}
.demand_input {
    width: 50%;
}
.demand_deletebtn {
    margin-left: 30px;
}
</style>