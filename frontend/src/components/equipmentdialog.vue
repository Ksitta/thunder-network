<template>
    <div class="networkorder_process">
        <el-dialog
                custom-class="equipmentdialog"
                class="equipment_dialog"
                style="text-align: center"
                title="创建设备"
                :close-on-click-modal="false"
                :visible.sync="dialogVisible"
                :show-close= false
                width="40%"
                >
            <div class="submit_form">
                <el-form class="form" ref="form" label-width="80px" label-position="left">
                    <el-form-item label="设备数量:" class = "label-style">
                        <el-input type="number" v-if="num_quantify == false" placeholder="请输入设备数量" v-model="eqs.eq_num" clearable size="medium" style="width: 90%;margin-left:-40px;" @input="quantify"></el-input>
                        <el-input type="number" v-if="num_quantify == true" v-model="eqs.eq_num" clearable size="medium" style="width: 90%;margin-left:-40px;" disabled></el-input>
                    </el-form-item>
                </el-form> 
                <div v-for="(eq, index) in eqs.eq_list" :key="eq.key" class="add-row">
                    <span class="label-span1">设备名称:</span>
                    <el-input v-model="eq.eq_name" size="mini" style="width:40%;" />
                    <span class="label-span">设备状态:</span>
                        <el-radio-group v-model="eq.eq_status" style="width:40%; margin-right: 5px;">
                            <el-radio label="开启" class = "radio-style"></el-radio>
                            <el-radio label="关闭" class = "radio-style"></el-radio>
                        </el-radio-group>
                    <el-button class="delete-btn" v-if="eqs.eq_list.length >= 1" size="mini" icon="el-icon-delete" type="danger" plain @click.prevent="removeRow(eq,index)" style="margin-right:20px;"></el-button>
                </div>
                <div class="footer-btn">
                    <el-button type="warning" size="mini" @click="addRow">增加设备</el-button>
                    <el-button type="danger" @click="cancel" size="mini">取消</el-button>
                    <el-button type="success" size="mini" @click="Submit">确定</el-button>
                </div>
            </div>
        </el-dialog>
    </div>
</template>

<script>
import axios from "axios";

export default{
    name: "equipmentdialog",
    props: {
        dialogVisible: {
            type: Boolean,
            default: () => false
        },
        path: {
            type: String,
            default: () => ''
        },
        eqs: {
            type: Object,
        },
        num_quantify: {
            type: Boolean,
            default: () => false
        }
    },
    data(){
        return{
        }
    },
    methods:{
        quantify: function(){
            if(this.eqs.eq_num != 0){
                this.num_quantify = true
            }
            for(var i = 0; i < this.eqs.eq_num; i++){
                this.pushdata()
            }
        },
        addRow: function(){
            this.pushdata()
            this.num_quantify = true
            this.eqs.eq_num++
        },
        pushdata: function(){
            this.eqs.eq_list.push({
                eq_name: "",
                eq_status: "",
                key: Date.now()
            })
        },
        removeRow: function(eq, index){
            index = this.eqs.eq_list.indexOf(eq)
            if (index !== -1) {
                this.eqs.eq_list.splice(index, 1)
            }
            this.eqs.eq_num--
        },
        Submit:function(){
            var correct = true
            var filled = true
            for (let eq of this.eqs.eq_list){
                if(eq.eq_name == "" | eq.eq_status == ""){
                    filled = false;
                    break
                }
            }
            if(this.eqs.eq_list.length != this.eqs.eq_num){
                this.$message.warning("设备数量不匹配！");
                correct = false;
            }else if(!filled){
                this.$message.warning("请填写完整设备信息！");
                correct = false;
            }
            if(correct){
                this.$emit('Dialog_cancel')
                let submiteqs = {
                    eq_num : parseInt(this.eqs.eq_num),
                    eq_list: []
                }
                for (let eq of this.eqs.eq_list){
                    submiteqs.eq_list.push({
                        eq_name: eq.eq_name,
                        eq_status: (eq.eq_status == "开启")? 1 : 2,
                    })
                }
                console.log('1',submiteqs)
                axios.post(this.path, submiteqs)
                .then(response => {
                    console.log("response:",response)
                    if(response.status === 201){
                        this.$message.success("提交成功！")
                        this.$emit('Dialog_submit')
                    }else{
                        alert(response.status)
                    }
                }).catch (error => {
                    alert('error！')
                    console.log(error)
                })
            }
        },
        cancel:function(){
            this.$emit('Dialog_cancel')
        }
    },
}
</script>

<style>
.equipmentdialog{
    border-radius: 20px;
}
.radio-style .el-radio__label{
    font-size: 10px;
    width: 10px;
}
.label-style .el-form-item__label{
    text-align: right;
}
.label-style .el-form-item__content{
    margin-left: 40px;
}

</style>
<style scoped>
.equipment_dialog {
    height: 100%;
}
.form{
    padding-bottom: 10px;
    margin-left: 15px;
}
.item {
    width: 90%;
}
.add-row{
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-evenly;
    padding-bottom: 5px;
    margin-right: 25px;
}
.label-span{
    width: 120px;
    padding-right: 5px;
    padding-left: 5px;
    text-align: right;
}
.label-span1{
    width: 120px;
    padding-right: 15px;
    padding-left: 5px;
    text-align: right;
}

.delete-btn{
    height: 28px;
    margin-left: 10px;
}
.el-icon-delete{
    display: block;
    padding-top: 0px;
}
.footer-btn{
    margin-top: 30px;
    text-align: right;
    margin-right: 45px;
}
</style>
