<template>
    <div class="ticketshow">
        <el-dialog
                custom-class="ticketdialog"
                class="ticket_dialog"
                style="text-align: center"
                title="工单详情"
                :close-on-click-modal="false"
                :visible.sync="dialogVisible"
                :show-close= false
                width="40%"
                >
            <div class="ticket_info" style="margin-top: -20px">
                <el-form class="form" label-width="120px" label-position="left">
                    <el-form-item label="工单编号:" class = "label_content1">
                        <span class="form_span">{{ticket_info.id}}</span>
                    </el-form-item>
                    <el-form-item label="提单人:" class = "label_content1">
                        <span class="form_span">{{ticket_info.user}}</span>
                    </el-form-item>
                    <el-form-item label="工单处理者:" class = "label_content1">
                        <span class="form_span">{{ticket_info.network_name}}</span>
                    </el-form-item>
                    <el-form-item label="问题所属站点:" class = "label_content1">
                        <span class="form_span">{{ticket_info.site_name}}</span>
                    </el-form-item>
                    <el-form-item label="问题类型:" class = "label_content1">
                        <span class="form_span">{{ticket_info.question_type}}</span>
                    </el-form-item>
                    <el-form-item label="问题设备:" class = "label_content1" v-if="ticket_info.question_type == '设备'" >
                        <span class="form_span">{{ticket_info.eq_name}}</span>
                    </el-form-item>
                    <el-form-item label="问题描述：" class = "label_content1" style="margin-top:10px;">
                        <!-- <span>{{ticket_info.question}}</span> -->
                        <el-input class="ticket_input" type="textarea" :rows="2"  v-model="ticket_info.question" readonly></el-input>
                    </el-form-item>
                    <el-form-item label="工单反馈：" class = "label_content1" v-if="(ticket_info.status != '处理中' && user) || (user == false)">
                        <!-- <span>{{ticket_info.question}}</span> -->
                        <el-input class="ticket_input" type="textarea" :rows="2"  v-model="ticket_info.answer" readonly v-if="user"></el-input>
                        <el-input class="ticket_input" type="textarea" :rows="2"  v-model="ticket_info.answer" v-if="!user"></el-input>
                    </el-form-item>
                    <el-form-item label="状态：" class = "label_content1" style="margin-top: 10px">
                        <el-steps :active="judge_active" align-center style="margin-left:-60px" finish-status="success" process-status="finish">
                        <el-step :title="`${ticket_info.user}提交工单`" :description="ticket_info.create_time"></el-step>
                        <el-step :title="`${ticket_info.network_name}处理工单`" :description="ticket_info.network_time"></el-step>
                        <el-step :title="`${ticket_info.user}确认反馈`" :description="ticket_info.close_time"></el-step>
                        </el-steps>                    
                    </el-form-item>
                    <el-form-item style="margin-left:250px">
                        <el-button type="primary" @click="cancel" size="medium" v-if="(ticket_info.status != '待确认' && user == true) || (user == false)">返回</el-button>
                        <el-button type="success" size="medium" @click="check() " v-if="ticket_info.status == '待确认' && user == true">确定</el-button>
                        <el-button type="success" size="medium" @click="answer() " v-if="ticket_info.status == '处理中' && user == false">提交</el-button>
                    </el-form-item>
                </el-form>
            </div>
        </el-dialog>
    </div>
</template>

<script>
import axios from "axios";

export default{
    name: "ticketdialog",
    props: {
        dialogVisible: {
            type: Boolean,
            default: () => false
        },
        ticket_info: {
            type: Object,
        },
        user: {
            type: Boolean,
            default: () => true
        }
    },
    data(){
        return{
        }
    },
    computed:{
        judge_active:function(){
            if(this.ticket_info.status == "已完成") return 3;
            if(this.ticket_info.status == "处理中") return 1;
            if(this.ticket_info.status == "待确认") return 2;
            return 1;
        },
    },
    methods:{
        cancel:function(){
            this.$emit('cancel')
        },
        check:function(){
            this.$emit('cancel')
            let submitinfo = {
                id: this.ticket_info.id,
                answer: this.ticket_info.answer,
            }
            axios.put('/api/ticket/', submitinfo)
            .then(response => {
                console.log("response:",response)
                if(response.status === 200){
                    this.$message.success("确认成功！")
                    this.$emit('submit')
                }else{
                    alert(response.status)
                }
            }).catch (error => {
                alert('error！')
                console.log(error)
            })
        },
        answer:function(){
            this.$emit('cancel')
            let submitinfo = {
                id: this.ticket_info.id,
                answer: this.ticket_info.answer,
            }
            axios.put('/api/ticket/', submitinfo)
            .then(response => {
                console.log("response:",response)
                if(response.status === 200){
                    this.$message.success("反馈成功！")
                    this.$emit('submit')
                }else{
                    alert(response.status)
                }
            }).catch (error => {
                alert('error！')
                console.log(error)
            })
        },
    },
}
</script>

<style>
.ticketdialog{
    border-radius: 20px;
}

.label_content1 .el-form-item__label{
    color: #32536a;
    font-weight: bold;
    font-size: 16px;
}

</style>
<style scoped>
.ticket_dialog {
    height: 100%;
}
.form{
    padding-bottom: 10px;
    margin-left: 15px;
}
.form_span{
    font-size: 16px;
    font-weight: bold;
    margin-right: 300px;
}
.hr_style{
  border: none; 
  border-top: 1px solid #DFE5EB; 
  margin-bottom:0px;
  margin-top: -20px;
}

/* .wlan_input{
    width: 80%;
    margin-right: 105px;
}

.footer-btn{
    margin-top: 30px;
    text-align: right;
    margin-right: 85px;
} */
</style>
