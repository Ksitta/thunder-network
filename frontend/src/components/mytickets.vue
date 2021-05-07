<template>
    <div id = "wrapper_mytickets">
        <div class="head" style=" margin-bottom:-60px">
            <div class="head-title" style=" margin-bottom:-10px;margin-top:-35px;margin-left:20px">
              <h1 align="left" style="font-size:30px; margin-left:15px;">我的工单</h1>
            </div>
        </div>

        <div class="colwrapper">
            <div style="font-size: 20px">
            <el-tabs  stretch>
                <el-tab-pane label="全部" class="tickets_tablabel">
                    <div class="head">
                        <el-input v-model="search_info" style="display: inline-block; margin-top: 5px; margin-left: 0px; width: 100%; height: 40px" placeholder="默认按照问题描述搜索" suffix-icon="el-icon-search"></el-input>
                    </div>
                    <div class="TicketData">
                        <el-table :data="ticket_data" style="width: 100%" maxheight="500px" height="530px" :header-cell-style="{'text-align':'center',fontSize: '15px',background:'#eef1f6',color:'#606266'}" :cell-style="{fontSize:'15px'}" >
                            <el-table-column prop= "question" label="问题描述" min-width="41%" align="center"></el-table-column>
                            <el-table-column prop= "id" label="工单编号" min-width="8%" align="center"></el-table-column>
                            <el-table-column prop= "site_name" label="问题站点" min-width="10%" align="center"></el-table-column>
                            <el-table-column prop= "question_type" label="问题类型" min-width="10%" align="center"></el-table-column>
                            <el-table-column prop= "status" label="状态" min-width="11%" align="center"></el-table-column>
                            <el-table-column prop= "create_time" label="创建时间" min-width="10%" align="center"></el-table-column>
                            <el-table-column label="详情" min-width="10%" align="center">
                                <template slot-scope="scope">
                                    <el-button size="mini" type="primary" @click="order_confirmation(scope.row)" v-if="scope.row.status == '处理中'">查看</el-button>
                                    <el-button size="mini" type="success" @click="order_confirmation(scope.row)" v-if="scope.row.status == '已完成'">查看</el-button>
                                    <el-button size="mini" type="danger" @click="order_confirmation(scope.row)" v-if="scope.row.status == '待确认'">确认</el-button>
                                </template>
                            </el-table-column>
                        </el-table>
                    </div>
                </el-tab-pane>
                <el-tab-pane label="分类查询">
                    <div class="head">
                        <el-row>
                            <el-col :span="12">
                                    <div style="margin-top:-5px">
                                        <el-form>
                                        <el-form-item label="工单类型:" class = "select-label" style="margin-bottom:5px">
                                            <div class="checkbox-div">
                                            <el-checkbox-group v-model="checkquestion_type" size="small" style="margin-right: 270px;">
                                            <el-checkbox-button v-for="item in question_type" :label="item" :key="item">{{item}}</el-checkbox-button>
                                            </el-checkbox-group>
                                            </div>
                                        </el-form-item>
                                        <el-form-item label="工单状态:" class = "select-label">
                                            <el-checkbox-group v-model="checkstatus" size="small" style="margin-right: 250px;">
                                                <el-checkbox-button v-for="item in status" :label="item" :key="item">{{item}}</el-checkbox-button>
                                            </el-checkbox-group>
                                        </el-form-item>
                                        </el-form>
                                    </div>
                            </el-col>
                            <el-col :span="12">
                                <div></div>
                                <el-input v-model="search_info" style="display: inline-block; margin-top: 40px; margin-left: 150px; width: 400px; height: 40px" placeholder="默认按照问题描述搜索" suffix-icon="el-icon-search"></el-input>
                            </el-col>
                        </el-row>
                    </div>
                    <div class="TicketData">
                        <el-table :data="selected_data" style="width: 100%" maxheight="500px" height="530px" :header-cell-style="{'text-align':'center',fontSize: '15px',background:'#eef1f6',color:'#606266'}" :cell-style="{fontSize:'15px'}" >
                            <el-table-column prop= "question" label="问题描述" min-width="41%" align="center"></el-table-column>
                            <el-table-column prop= "id" label="工单编号" min-width="8%" align="center"></el-table-column>
                            <el-table-column prop= "site_name" label="问题站点" min-width="10%" align="center"></el-table-column>
                            <el-table-column prop= "question_type" label="问题类型" min-width="10%" align="center"></el-table-column>
                            <el-table-column prop= "status" label="状态" min-width="11%" align="center"></el-table-column>
                            <el-table-column prop= "create_time" label="创建时间" min-width="10%" align="center"></el-table-column>
                            <el-table-column label="详情" min-width="10%" align="center">
                                <template slot-scope="scope">
                                    <el-button size="mini" type="primary" @click="order_confirmation(scope.row)" v-if="scope.row.status == '处理中'">查看</el-button>
                                    <el-button size="mini" type="success" @click="order_confirmation(scope.row)" v-if="scope.row.status == '已完成'">查看</el-button>
                                    <el-button size="mini" type="danger" @click="order_confirmation(scope.row)" v-if="scope.row.status == '待确认'">确认</el-button>
                                </template>
                            </el-table-column>
                        </el-table>
                    </div>
                </el-tab-pane>
            </el-tabs>
            </div>
        </div>
        <ticketdialog :dialogVisible="ticketdialog.dialogVisible" :ticket_info="ticketdialog.ticket_info" :user="ticketdialog.user" @cancel='cancel' @submit="submit"></ticketdialog>
    </div>
</template>

<script>

import axios from 'axios'
import ticketdialog from '@/components/ticketdialog'

export default{
    name: 'tickets',
    components: {
        ticketdialog,
    },
    inject: ['reload'],
    data(){
        return{
            tickets_data: [],
            search_info: '',
            checkquestion_type: ['站点', '设备', 'WLAN'],
            question_type: ['站点', '设备', 'WLAN'],
            checkstatus: ['待确认','处理中','已完成'],
            status: ['待确认','处理中','已完成'],
            ticketdialog:{
                dialogVisible: false,
                ticket_info: {
                    question: "",
                    id: 0,
                    user: "",
                    site_name: "",
                    eq_name: "",
                    question_type: "",
                    status: "",
                    create_time: "",
                    answer: "",
                    network_name: "",
                    network_time: "",
                    close_time: "",
                    telephone: "",
                    email: "",
                },
                user: true
            },
        }
    },
    created(){
        this.getdata()
    },
    methods: {
        getdata: function(){
            this.tickets_data= [],
            axios.get('/api/ticket/')
            .then((response)=>{
                var res = response.data
                console.log(res)
                for(let item of res){
                    var answer = false
                    var finish = false
                    var type = ''
                    var status_string = ''
                    if(item.status == 0){
                        answer = true
                        finish = true
                        status_string = "已完成"
                    }else if(item.status == 2){
                        answer = true
                        status_string = "待确认"
                    }else{
                        status_string = "处理中"
                    }
                    if(item.question_type == 0){
                        type = "站点"
                    }
                    if(item.question_type == 1){
                        type = "设备"
                    }
                    if(item.question_type == 2){
                        type = "WLAN"
                    }
                    this.tickets_data.push({
                        question: item.question,
                        id: item.id,
                        user: item.user,
                        site_name: item.site_name,
                        eq_name: item.eq_name,
                        question_type: type,
                        status: status_string,
                        create_time: item.create_time.substring(0,10),
                        answer: item.answer,
                        network_name: item.network_name,
                        network_time: (answer)? item.network_time.substring(0,10) : '',
                        close_time: (finish)? item.close_time.substring(0,10) : '',
                        telephone: item.contact_details,
                        email: item.contact_email,
                    })
                }
            })
        },
        submit:function(){
            this.ticketdialog.dialogVisible = false
            this.getdata()
        },
        cancel:function(){
            this.ticketdialog.dialogVisible = false
        },
        order_confirmation: function(row){
            this.ticketdialog.dialogVisible = true;
                this.ticketdialog.ticket_info.question = row.question;
                this.ticketdialog.ticket_info.id = row.id;
                this.ticketdialog.ticket_info.user = row.user;
                this.ticketdialog.ticket_info.site_name= row.site_name;
                this.ticketdialog.ticket_info.eq_name= row.eq_name;
                this.ticketdialog.ticket_info.question_type= row.question_type;
                this.ticketdialog.ticket_info.status= row.status;
                this.ticketdialog.ticket_info.create_time= row.create_time;
                this.ticketdialog.ticket_info.answer= row.answer;
                this.ticketdialog.ticket_info.network_name= row.network_name;
                this.ticketdialog.ticket_info.network_time= row.network_time;
                this.ticketdialog.ticket_info.close_time= row.close_time;
                this.ticketdialog.ticket_info.telephone= row.telephone;
                this.ticketdialog.ticket_info.email= row.email;
            console.log(ticketdialog.ticket_info);
        },
    },
    computed: {
        ticket_data(){
            const search_info = this.search_info
            var status_data_0 = []
            var status_data_1 = []
            var status_data_2 = []
            var ticket_data = []
            for(let item of this.tickets_data){
                if (item.status == "已完成"){
                    status_data_0.push(item)
                }
                if (item.status == "处理中"){
                    status_data_1.push(item)
                }
                if (item.status == "待确认"){
                    status_data_2.push(item)
                }
            }
            ticket_data = ticket_data.concat(status_data_1)
            ticket_data = ticket_data.concat(status_data_2)
            ticket_data = ticket_data.concat(status_data_0)
            if(search_info){
                return ticket_data.filter(data => {
                    let show = ["question"]
                    return show.some(key => {
                        return String(data[key]).toLowerCase().indexOf(search_info.toLowerCase()) > -1
                    })
                })
            }
            return ticket_data
        },
        selected_data(){
            var site = false;
            var device = false;
            var WLAN = false;
            var status_0 = false;
            var status_1 = false;
            var status_2 = false;
            for(let item of this.checkquestion_type){
                if(item == "站点")  site = true;
                if(item == "设备") device = true;
                if(item == "WLAN") WLAN = true;
            }
            for(let item of this.checkstatus){
                if(item == "待确认") status_2 = true;
                if(item == "处理中") status_1 = true;
                if(item == "已完成") status_0 = true;
            }
            const search_info = this.search_info
            var status_data_0 = []
            var status_data_1 = []
            var status_data_2 = []
            var siteselected_data = []
            var selected_data = []
            for(let item of this.tickets_data){
                if (item.status == "已完成" && status_0 == true){
                    status_data_0.push(item)
                }
                if (item.status == "处理中" && status_1 == true){
                    status_data_1.push(item)
                }
                if (item.status == "待确认" && status_2 == true){
                    status_data_2.push(item)
                }
            }
            siteselected_data = siteselected_data.concat(status_data_1)
            siteselected_data = siteselected_data.concat(status_data_2)
            siteselected_data = siteselected_data.concat(status_data_0)
            for(let item of siteselected_data){
                if(site && item.question_type == "站点") selected_data.push(item);
                if(device && item.question_type == "设备") selected_data.push(item);
                if(WLAN && item.question_type == "WLAN") selected_data.push(item);
            }
            if(search_info){
                return selected_data.filter(data => {
                    let show = ["question"]
                    return show.some(key => {
                        return String(data[key]).toLowerCase().indexOf(search_info.toLowerCase()) > -1
                    })
                })
            }
            return selected_data
        },
    }
}

</script>

<style scoped>
.head{
  padding: 0px 0px 10px 0px;
}
.colwrapper {
  background-color: #ffffff;
  border-radius: 10px;
  padding: 16px;
  margin-top: 50px;
  margin-left: 20px;
  margin-right: 30px;
}
.propTicket {
    margin-top: 10px;
}
.el-table {
    border-radius: 5px;
}
.basic_info{
    width: 100%;
    padding: 10px 10px 10px 10px;
    margin: 10px 10px 10px 10px;
}
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

<style>
.table-expand {
    font-size: 0;
}
.table-expand label {
    width: 150px;
    color: #99a9bf;
    font-size: 16px;
}
.table-expand .el-form-item {
    margin-right: 10px;
    margin-bottom: 10px;
    width: 100%;
    font-size: 100%;
}
.select-label .el-form-item__label{
    color: #32536a;
    font-weight: bold;
    font-size: 15px;
}

</style>
