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
                width="50%"
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
                    <el-form-item label="联系电话:" class = "label_content1" v-if="ticket_info.telephone.length > 0">
                        <span class="form_span">{{ticket_info.telephone}}</span>
                    </el-form-item>
                    <el-form-item label="联系邮箱:" class = "label_content1" v-if="ticket_info.email.length > 0">
                        <span class="form_span">{{ticket_info.email}}</span>
                    </el-form-item>
                    <el-form-item label="问题设备:" class = "label_content1" v-if="ticket_info.question_type == '设备'" >
                        <span class="form_span">{{ticket_info.eq_name}}</span>
                    </el-form-item>
                    <el-form-item label="问题描述：" class="label_content1" style="margin-top:10px;">
                        <!-- <span>{{ticket_info.question}}</span> -->
                        <el-input class="ticket_input" type="textarea" :rows="2"  v-model="ticket_info.question" readonly></el-input>
                    </el-form-item>
                    <el-form-item label="工单反馈：" class="label_content1" v-if="(ticket_info.status != '处理中' && user) || (user == false)">
                        <!-- <span>{{ticket_info.question}}</span> -->
                        <el-input class="ticket_input" type="textarea" :rows="4"  v-model="ticket_info.answer" readonly v-if="user"></el-input>
                        <el-input class="ticket_input" type="textarea" :rows="4"  v-model="ticket_info.answer" v-if="!user"></el-input>
                    </el-form-item>
                    <el-form-item label="状态：" class = "label_content1" style="margin-top: 10px">
                        <!-- <el-steps  :active="judge_active" finish-status="success" process-status="finish" direction="vertical">
                            <el-step title="提交工单">
                                <template slot="description" >
                                    <div class="step-row">
                                        <table width="100%" border="0" cellspacing="0" cellpadding="0" class="processing_content">
                                            <tr>
                                                <td style="color:#98A6BE">
                                                    <div class="processing_content_detail" style="float:left;width:70%"><span>用户&nbsp;&nbsp;<span style="color:#219AFF">{{ticket_info.user}}</span>&nbsp;&nbsp;提交了工单</span></div>
                                                    <div class="processing_content_detail" style="float:right;"><span ><i class="el-icon-time"></i>&nbsp;&nbsp;{{ticket_info.create_time}}</span> </div>
                                                </td>
                                            </tr>
                                        </table>
                                    </div>
                                </template>
                            </el-step>
                            <el-step title="网络工程师处理">
                                <template slot="description" >
                                    <div class="step-row">
                                        <table width="100%" border="0" cellspacing="0" cellpadding="0" class="processing_content">
                                            <br v-if="ticket_info.status == '处理中'">
                                            <br v-if="ticket_info.status == '处理中'">
                                            <tr v-if="ticket_info.status == '待确认'||'已完成'">
                                                <td style="color:#98A6BE">
                                                    <div class="processing_content_detail" style="float:left;width:70%" v-if="ticket_info.status == '处理中'"><span>运营工程师&nbsp;&nbsp;<span style="color:#219AFF">{{ticket_info.network_name}}</span>&nbsp;&nbsp;正在处理订单……</span></div>
                                                    <div class="processing_content_detail" style="float:left;width:70%" v-if="props.row.status == '待确认' || '已完成'"><span>运营工程师&nbsp;&nbsp;<span style="color:#219AFF">{{ticket_info.network_name}}</span>&nbsp;&nbsp;处理了订单</span></div>
                                                    <div class="processing_content_detail" style="float:right;" v-if="props.row.status == '待确认' || '已完成'"><span ><i class="el-icon-time"></i>&nbsp;&nbsp;{{ticket_info.network_time}}</span> </div>
                                                </td>
                                            </tr>
                                        </table>
                                    </div>
                                </template>
                            </el-step>
                            <el-step title="用户确认反馈">
                                <template slot="description" >
                                    <div class="step-row" >
                                        <table width="100%" border="0" cellspacing="0" cellpadding="0" class="processing_content">
                                            <br v-if="ticket_info.status == '待确认'">
                                            <br v-if="ticket_info.status == '待确认'">
                                            <tr v-if="ticket_info.status == '已完成'">
                                                <td style="color:#98A6BE">
                                                    <div class="processing_content_detail" style="float:left;width:70%" v-if="ticket_info.status == '处理中'||'待确认'"><span>用户&nbsp;&nbsp;<span style="color:#219AFF">{{ticket_info.user}}</span>&nbsp;&nbsp;正在处理订单……</span></div>
                                                    <div class="processing_content_detail" style="float:left;width:70%" v-if="ticket_info.status == '已完成'"><span>用户&nbsp;&nbsp;<span style="color:#219AFF">{{ticket_info.user}}</span>&nbsp;&nbsp;确认了反馈，工单关闭</span></div>
                                                    <div class="processing_content_detail" style="float:right;" v-if="ticket_info.status == '已完成'"><span ><i class="el-icon-time"></i>&nbsp;&nbsp;{{ticket_info.close_time}}</span> </div>
                                                </td>
                                            </tr>
                                        </table>
                                    </div>
                                </template>
                            </el-step>
                        </el-steps> -->

                        <el-steps :active="judge_active" style="margin-left:-60px" finish-status="success" process-status="finish" align-center>
                        <el-step :title="`${ticket_info.user}提交工单`" :description="ticket_info.create_time"></el-step>
                        <el-step :title="`${ticket_info.network_name}处理工单`" :description="ticket_info.network_time"></el-step>
                        <el-step :title="`${ticket_info.user}确认反馈`" :description="ticket_info.close_time"></el-step>
                        </el-steps>                    
                    </el-form-item>
                    <el-form-item style="margin-left:300px">
                        <el-button type="primary" @click="cancel" size="medium" >返回</el-button>
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
    padding-left: 20px;
    padding-right: 40px;
    padding-top: 10px;
    padding-bottom: 10px;
    margin-left: 15px;
}
.form_span{
    font-size: 16px;
    font-weight: bold;
    margin-right: 350px;
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
.stepComponent{
    width: 100%;
    padding: 10px 10px 10px 10px;
    margin: 10px 10px 10px 10px;
}
.stepsTitle{
    margin: 10px 0px  10px  10px ;
}
.orderprocessing{
    /* font-size: 14px; */
    margin-left:10px;
    margin-right:0px;
    margin-top:10px;
}
.processing_content_detail{
    font: 15px;
    margin-left: 10px;
    margin-top: 0px;
    margin-bottom: 0px;
    width:100px;
    display:inline-block;
}
.step-row{
    min-width:500px;
    margin-bottom:10px;
    margin-top:0px;
}

</style>
