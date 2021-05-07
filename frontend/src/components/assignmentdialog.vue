<template>
    <div class="networkassignment">
        <el-dialog
                custom-class="assignmentdialog"
                class="assignment_dialog"
                style="text-align: center"
                title="分配网络工程师"
                :close-on-click-modal="false"
                :visible.sync="dialogVisible"
                :show-close= false
                width="40%"
                >
            <div class="submit_form">
                <el-form class="form" ref="form" label-width="100px" label-position="right">
                    <el-form-item label="网络工程师:" class = "label-style">
                        <!-- <el-input placeholder="请输入设备数量" v-model="eqs.eq_num" clearable size="medium" style="width: 90%;margin-left:-40px;"></el-input> -->
                        <el-select v-model="network_selected" placeholder="请选择" style="margin-right: 100px; width: 80%;">
                            <el-option
                            v-for="item in networks"
                            :key="item"
                            :label="item"
                            :value="item">
                            </el-option>
                        </el-select>                    
                    </el-form-item>
                </el-form> 
                <div class="footer-btn">
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
    name: "assignmentdialog",
    props: {
        dialogVisible: {
            type: Boolean,
            default: () => false
        },
        networks: {
            type: Array,
            default: () => []
        },
        path: {
            type: String,
            default: () => ''
        },
        network_selected: {
            type: String,
            default: () => ''
        },
    },
    data(){
        return{
        }
    },
    methods:{
        Submit:function(){
            console.log(this.path)
            axios.post(this.path, {
                network_name: this.network_selected,
            })
            .then(response => {
                console.log("response:",response)
                if(response.status === 200){
                    this.$message.success("处理成功！")
                    this.$emit('Dialog_submit')
                }else{
                    console.log(response.status)
                }
            }).catch (error => {
                this.$message.error("出错了！")
                console.log(error)
            })
        },
        cancel:function(){
            this.$emit('Dialog_cancel')
        }
    },
}
</script>

<style>
.assignmentdialog{
    border-radius: 20px;
}
.label-style .el-form-item__label{
    text-align: right;
}
.label-style .el-form-item__content{
    margin-left: 40px;
}

</style>
<style scoped>
.assignment_dialog {
    height: 100%;
}
.form{
    padding-bottom: 10px;
    margin-left: 15px;
}
.item {
    width: 90%;
}
.footer-btn{
    margin-top: 30px;
    text-align: right;
    margin-right: 45px;
}
</style>
