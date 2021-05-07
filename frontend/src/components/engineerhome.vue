<template>
  <div id="wrapper_userhome">
    <el-container class="container">
      <el-row :gutter="0" id="row_up">
        <el-col :span="16" class="left_col">
          <div class="colwrapper">
            <div class="userinfo">
              <div style="display:flex; justify-content: start;">
                <el-avatar shape="square" :size="100" :src="avatar_src"></el-avatar>
                <div class="usergreet">
                  <div>
                    <span style="font-size: 40px; vertical-align: middle;">
                      {{info.username}}
                    </span>
                    <el-tag style="vertical-align: middle;">{{identity}}</el-tag>
                  </div>
                  <div style="color: #333850; font-size: 12px; padding-top: 5px;">
                    email: {{info.contact_email}}
                  </div>
                </div>
              </div>
              <hr class="divider"/>
            </div>
          </div>

          <div class="colwrapper">
            <h1>工单信息</h1>
                    <div class="TicketData">
                        <el-table :data="ticket_data" style="width: 100%" maxheight="350px" height="350px" :header-cell-style="{'text-align':'center',fontSize: '13px',background:'#eef1f6',color:'#606266'}" :cell-style="{fontSize:'13px'}" :row-style="{height:0+'px'}" >
                            <el-table-column prop= "question" label="问题描述" min-width="35%" align="center"></el-table-column>
                            <el-table-column prop= "id" label="编号" min-width="8%" align="center"></el-table-column>
                            <el-table-column prop= "site_name" label="站点" min-width="10%" align="center"></el-table-column>
                            <el-table-column prop= "question_type" label="类型" min-width="10%" align="center"></el-table-column>
                            <el-table-column prop= "status" label="状态" min-width="11%" align="center"></el-table-column>
                            <el-table-column prop= "create_time" label="创建时间" min-width="15%" align="center"></el-table-column>
                            <el-table-column label="详情" min-width="11%" align="center">
                                <template slot-scope="scope">
                                    <el-button size="mini" type="danger" @click="order_confirmation(scope.row)" v-if="scope.row.status == '处理中'">处理</el-button>
                                    <el-button size="mini" type="primary" @click="order_confirmation(scope.row)" v-if="scope.row.status == '待确认'">查看</el-button>
                                    <el-button size="mini" type="success" @click="order_confirmation(scope.row)" v-if="scope.row.status == '已完成'">查看</el-button>
                                </template>
                            </el-table-column>
                        </el-table>
                    </div>
          <ticketdialog :dialogVisible="ticketdialog.dialogVisible" :ticket_info="ticketdialog.ticket_info" :user="ticketdialog.user" @cancel='cancel' @submit="submit"></ticketdialog>
          </div>
        </el-col>

        <el-col :span="8" class="right_col">
          <div class="colwrapper">

            <div style="color: #7792b1;">
              <p>
                <span style="font-size: 32px; line-height: 26px;">{{ordercount}}</span>
              </p>
              <p>
                待处理订单数
                <i class="el-icon-s-order"></i>
              </p>
            </div>

          </div>
        </el-col>

      </el-row>
    </el-container>
  </div>
</template>

<script>

import axios from 'axios'
import { Message } from 'element-ui';
import ticketdialog from '@/components/ticketdialog'
import md5 from 'js-md5'


export default {
  name: 'engineerhome',
  components: {
      ticketdialog,
  },
  data() {
      return {
        ordercount: 0,
        info: {
          username: "",
          contact_details: "",
          contact_email: "",
          contact_address: "",
          user_type: "",
        },
        tickets_data: [],
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
            },
            user: false
        },
      }
  },
  methods: {
    refresh: function() {
      console.log('refresh userhome!')
      axios.get('/api/user/profile/')
      .then((response) => {
        console.log(response)
        console.log(response.data.user)
        this.info.username = response.data.user.username
        this.info.contact_details = response.data.user.contact_details
        this.info.contact_email = response.data.user.contact_email
        this.info.contact_address = response.data.user.contact_address
        this.info.user_type = response.data.user.user_type
        this.$store.commit('newtype', {
            type: this.info.user_type
        })
      })
      .catch((error) => {
        console.log(error)
        Message({
          message: "获取用户信息失败",
          type: "error",
        });
      })
    },
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
                })
            }
        })
    },
    submit:function(){
        this.ssiddialog.dialogVisible = false
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
        console.log(ticketdialog.ticket_info);
    },
  },
  props: {
    show: {
      type: Boolean,
      default: () => false,
    }
  },

  computed: {
    identity: function() {
      if (this.info.user_type == "0") return "用户";
      if (this.info.user_type == "1") return "运营工程师";
      if (this.info.user_type == "2") return "网络工程师";
      return "";
    },
    avatar_src: function() {
      return "https://sdn.geekzu.org/avatar/" + md5(this.info.contact_email);
    },
    ticket_data(){
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
        return ticket_data
    },
  },

  mounted: function() {
    this.refresh();
    this.getdata();
  },

  created() {
    this.ordercount = 0;
    axios.get('/api/site/')
    .then((response)=>{
      var res = response.data
      console.log(res)
      for(let item of res){
          if(item.status == 2) {
            this.ordercount += 1;
          }
      }
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

#wrapper_userhome {
  height: 100%;
  width: 100%;
}

.container {
  height: 100%;
}

.colwrapper {
  background-color: #ffffff;
  border-radius: 10px;
  padding: 16px;
  margin: 14px;
}

#row_up {
  width: 100%;
}

.userinfo {
  overflow: auto;
  padding: 20px;
  text-align: left;
}

.el-avatar {
  margin-right: 10px;
  box-shadow: rgba(0,6,36,0.25) 0px 26px 24px -16px,rgba(0,6,36,0.3) 0px 16px 24px -18px,rgba(0,6,36,0.07) 0px 0px 10px 0px;
}

.usergreet {
  padding-left: 20px;
  flex: 1;
}

.divider {
  background-color:#dfe5eb;
  border: none;
  min-height: 1px;
  margin-top: 0px;
  margin-left: 120px;
}

.el-tag {
  font-size: 12px;
  font-weight: bold;
}

</style>
