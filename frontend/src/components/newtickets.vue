<template>
    <div id="wrapper_newtickets">
        <div class="head" style=" margin-bottom:-60px">
            <div class="head-title" style=" margin-bottom:-10px;margin-top:-35px;margin-left:20px">
              <h1 align="left" style="font-size:30px; margin-left:15px;">新建工单</h1>
            </div>
            <div class="steps">
                <el-steps :active="judge_active" simple style="height:10px;" >
                <el-step title="选择问题所属站点" icon="el-icon-edit"></el-step>
                <el-step title="选择问题类型" icon="el-icon-edit"></el-step>
                <el-step title="新建工单" icon="el-icon-edit"></el-step>
                </el-steps>            
            </div>
        </div>
        <div class="colwrapper">
          <div class="ticket_info" style=" margin-bottom:30px;">
                <div class="body" style="padding:50px 30px 30px;">
                      <el-form class="form" ref="form" :model="form" label-width="150px">
                          <el-form-item label="问题所属站点:" class = "label_content" required>
                            <el-select class="ticket_input" v-model="ticket.site_pk" placeholder="请选择问题站点" clearable @change="businessTypeChange">
                            <el-option
                            v-for="item in site_list"
                            :key="item.pk"
                            :label="item.site_name"
                            :value="item.pk"
                            :disabled="item.disabled"
                            >
                            </el-option>
                            </el-select>
                          </el-form-item>
                        <hr class="hr_style">
                          <el-form-item label="问题类型:" class = "label_content" required>
                            <el-select class="ticket_input" v-model="ticket.question_type" placeholder="请选择问题类型" clearable @change="businessTypeChange">
                                <el-option
                                    v-for="item in question_list"
                                    :key="item.value" 
                                    :label="item.label" 
                                    :value="item.value"
                                    :disabled="item.disabled"
                                    >
                                </el-option>
                            </el-select>
                          </el-form-item>
                          <el-form-item label="问题设备:" class = "label_content" v-if="ticket.question_type == '2'">
                                <el-select class="ticket_input" v-model="ticket.eq_name" placeholder="请选择问题设备" clearable>
                                    <el-option
                                    v-for="item in device_list"
                                    :key="item.eq_name"
                                    :label="item.eq_name"
                                    :value="item.eq_name">
                                    </el-option>
                                </el-select>
                          </el-form-item>
                          <hr class="hr_style">
                          <el-form-item label="问题描述：" class = "label_content" required>
                                <el-input class="ticket_input" type="textarea" :rows="5" placeholder="请输入内容" v-model="ticket.question"></el-input>
                          </el-form-item>
                          <hr class="hr_style">
                         <el-form-item label="联系方式:" class="label_content">
                            <el-checkbox-group v-model="relationlist" style="margin-right:600px">
                                <el-checkbox label="工单留言" disabled></el-checkbox>
                                <el-checkbox label="电话"></el-checkbox>
                                <el-checkbox label="邮箱"></el-checkbox>
                            </el-checkbox-group>
                        </el-form-item>
                        <el-form-item label="电话：" class="label_content" v-if="(relationlist.length == 1 && relationlist[0] == '电话') || (relationlist.length == 2)">
                            <el-input class="ticket_input" placeholder="请输入联系电话" v-model="ticket.telephone"></el-input>
                        </el-form-item>
                        <el-form-item label="邮箱：" class="label_content" v-if="(relationlist.length == 1 && relationlist[0] == '邮箱') || (relationlist.length == 2)">
                            <el-input class="ticket_input" placeholder="请输入联系邮箱" v-model="ticket.email"></el-input>
                        </el-form-item>
                        <el-form-item style="margin-left: 150px;">
                            <el-button type="primary" @click="submit">新建工单</el-button>                
                        </el-form-item>
                      </el-form>
                </div>
          </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: "newtickets",
    data() {
        return{
            site_list: [],
            question_list: [
                {
                    value: '1',
                    label: '站点相关问题',
                },
                {
                    value: '2',
                    label: '设备相关问题',
                },
                {
                    value: '3',
                    label: 'WLAN相关问题',
                },
            ],
            relationlist:[],
            ticket:{
                site_pk: '',
                question: '',
                question_type: '',
                eq_name: '',
                telephone: '',
                email: '',
            }
        }
        
    },
    computed:{
        device_list() {
        if (this.ticket.site_pk.length == 0) return [];
        return this.site_list[this.ticket.site_pk].eqs;
        },
        judge_active:function(){
            if(this.ticket.question.length > 0) return 3;
            if(this.ticket.question_type.length > 0) return 2;
            if(this.ticket.site_pk.length > 0) return 1;
            return 0;
        }

    },
    created() { // generate site_list
    this.site_list = [];
        axios.get("/api/site/").then((response) => {
        let res = response.data;
        for (let index in res) {
            let item = res[index];
            if (item.status == 0) {
            let eqs = [];
            for (let idx in item.eqs) {
                eqs.push({
                eq_name: item.eqs[idx].eq_name,
                pk: idx,
                disabled: item.eqs[idx].eq_status != 1,
                });
            }
            this.site_list.push({
                site_name: item.site_name,
                pk: index,
                eqs: eqs,
                disabled: false,
            });
            } else {
            this.site_list.push({
                site_name: item.site_name,
                pk: index,
                disabled: true,
            });
            }
        }
        });
        axios.get('/api/user/profile/')
        .then((response) => {
          // console.log(response)
          this.ticket.telephone = response.data.user.contact_details
          this.ticket.email = response.data.user.contact_email
        })
        .catch((error) => {
          console.log(error)
        //   Message({
        //     message: "获取用户信息失败",
        //     type: "error",
        //   });
        })

    },
    methods:{
        businessTypeChange(item){
                this.$forceUpdate();
                console.log(item);
            },        
        submit:function(){
            let submitinfo = {
                question: this.ticket.question,
                question_type: (parseInt(this.ticket.question_type) - 1),
                site_name: this.site_list[this.ticket.site_pk].site_name,
                eq_name: this.ticket.eq_name,
                contact_details: ((this.relationlist.length == 1 && this.relationlist[0] == '电话') || (this.relationlist.length == 2))? this.ticket.telephone : '',
                contact_email: ((this.relationlist.length == 1 && this.relationlist[0] == '邮箱') || (this.relationlist.length == 2))? this.ticket.email : '',
            }
            console.log(submitinfo)
            axios.post("/api/ticket/", submitinfo)
            .then(response => {
                console.log("response:",response)
                if(response.status === 201){
                    this.$message.success("提交成功！")
                    this.$emit('userinfoEdited')
                }else{
                    console.log(response.status)
                }
            }).catch (error => {
                this.$message.error("出错了！")
                console.log(error)
            })
        },
    }

}
</script>



<style scoped>
.steps{
    margin-top: 0px;
  margin-left: 20px;
  margin-bottom: 0px;
  margin-right: 30px;
}
.colwrapper {
  background-color: #ffffff;
  border-radius: 10px;
  padding: 0px;
  margin-left: 20px;
  margin-bottom: 0px;
  margin-right: 30px;
  margin-top:70px;
  height: 700px;
}
.ticket_input{
    width: 60%;
    margin-right: 300px;
}
.label_style{
    color: #32536a;
    font-weight: thin;
    font-size: 18px;
    position:relative;
    bottom: 10px;;
}
.hr_style{
  border: none; 
  border-top: 1px solid #DFE5EB; 
  margin-bottom: 20px;
  margin-top: 20px;
}



</style>