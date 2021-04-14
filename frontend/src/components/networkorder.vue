<template>
    <div id = "wrapper_networkorder">
        <div class="head">
            <el-row type="flex" justify="space-between">
                <div></div>
                <el-input v-model="search_info" style="display: inline-block; margin-top: 0px; width: 400px; height: 40px" placeholder="请输入搜索内容" suffix-icon="el-icon-search"></el-input>
            </el-row>
        </div>
        <div class="colwrapper">
            <div class="SiteData">
                <el-table :data="sitedata" style="width: 100%" maxheight="500px" height="530px" :header-cell-style="{'text-align':'center',fontSize: '15px'}" :cell-style="{fontSize:'15px'}" >
                <el-table-column type="expand">
                    <template slot-scope="props">
                        <el-row>
                            <el-col :span="12">
                                <div class="basic_info">
                                    <el-form label-position="left" inline class="table-expand">
                                        <el-form-item label="站点名称:" class="basic_info_item">
                                            <span style="font-size:16px">{{ props.row.site_name}}</span>
                                        </el-form-item>
                                        <el-form-item label="站点创建时间:" class="basic_info_item">
                                            <span style="font-size:16px">{{ props.row.create_time }}</span>
                                        </el-form-item>
                                        <el-form-item label="站点地址:" class="basic_info_item">
                                            <span style="font-size:16px">{{ props.row.site_address }}</span>
                                        </el-form-item>
                                        <el-form-item label="计费方式:" class="basic_info_item">
                                            <span style="font-size:16px">{{ props.row.billing_level }}</span>
                                        </el-form-item>
                                        <el-form-item label="虚拟网络需求:" class="basic_info_item">
                                            <span style="font-size:16px">{{ props.row.demand}}</span>
                                        </el-form-item>
                                    </el-form>
                                </div>
                            </el-col>
                            <el-col :span="12">
                                <div class="stepComponent">
                                    <div class="stepTitle">
                                        <div style="float: left; width:2px;height:20px; background:#219AFF;"></div>
                                        <span style="color:#99a9bf;font-size: 16px;">订单处理状态</span>
                                        <br>
                                    </div>
                                    <div class="networkorder">
                                        <el-steps :active="props.row.status" finish-status="success" process-status="finish" direction="vertical">
                                            <el-step title="提交订单">
                                                <template slot="description" >
                                                    <div class="step-row" v-if="props.row.status >= 1">
                                                        <table width="100%" border="0" cellspacing="0" cellpadding="0" class="processing_content">
                                                            <tr>
                                                                <td style="color:#98A6BE">
                                                                    <div class="processing_content_detail" style="float:left;width:70%"><span>用户&nbsp;&nbsp;<span style="color:#219AFF">{{props.row.user_name}}</span>&nbsp;&nbsp;提交了订单</span></div>
                                                                    <div class="processing_content_detail" style="float:right;"><span ><i class="el-icon-time"></i>&nbsp;&nbsp;{{props.row.create_time}}</span> </div>
                                                                </td>
                                                            </tr>
                                                        </table>
                                                    </div>
                                                </template>
                                            </el-step>
                                            <el-step title="运营工程师处理">
                                                <template slot="description" >
                                                    <div class="step-row">
                                                        <table width="100%" border="0" cellspacing="0" cellpadding="0" class="processing_content">
                                                            <br v-if="props.row.status == 0">
                                                            <br v-if="props.row.status == 0">
                                                            <tr v-if="props.row.status >= 1">
                                                                <td style="color:#98A6BE">
                                                                    <div class="processing_content_detail" style="float:left;width:70%" v-if="props.row.status == 1"><span>运营工程师正在处理订单……</span></div>
                                                                    <div class="processing_content_detail" style="float:left;width:70%" v-if="props.row.status >= 2"><span>运营工程师&nbsp;&nbsp;<span style="color:#219AFF">{{props.row.manager_name}}</span>&nbsp;&nbsp;处理了订单</span></div>
                                                                    <div class="processing_content_detail" style="float:right;" v-if="props.row.status >= 2"><span ><i class="el-icon-time"></i>&nbsp;&nbsp;{{props.row.manager_time}}</span> </div>
                                                                </td>
                                                            </tr>
                                                        </table>
                                                    </div>
                                                </template>
                                            </el-step>
                                            <el-step title="网络工程师处理">
                                                <template slot="description" >
                                                    <div class="step-row" >
                                                        <table width="100%" border="0" cellspacing="0" cellpadding="0" class="processing_content">
                                                            <br v-if="props.row.status == 1">
                                                            <br v-if="props.row.status == 1">
                                                            <tr v-if="props.row.status >= 2">
                                                                <td style="color:#98A6BE">
                                                                    <div class="processing_content_detail" style="float:left;width:70%" v-if="props.row.status == 2"><span>网络工程师正在处理订单……</span></div>
                                                                    <div class="processing_content_detail" style="float:left;width:70%" v-if="props.row.status >= 3"><span>网络工程师&nbsp;&nbsp;<span style="color:#219AFF">{{props.row.network_name}}</span>&nbsp;&nbsp;处理了订单</span></div>
                                                                    <div class="processing_content_detail" style="float:right;" v-if="props.row.status >= 3"><span ><i class="el-icon-time"></i>&nbsp;&nbsp;{{props.row.network_time}}</span> </div>
                                                                </td>
                                                            </tr>
                                                        </table>
                                                    </div>
                                                </template>
                                            </el-step>
                                        </el-steps>
                                    </div>
                                </div>
                            </el-col>
                        </el-row>
                        <el-row v-if="props.row.status == 3" style="margin-top: -50px;margin-left: 10px">
                            <h4 style="margin-left:20px;color:#666;font-size:16px;" v-if="props.row.status == 3">站点设备情况</h4>
                            <el-table v-if="props.row.status == 3" :cell-style="{color: '#666', fontFamily: 'Arial',fontSize:'15px'}" :data="props.row.eqs" :header-cell-style="{background:'#f0f9eb', fontFamily:'Helvetica',fontSize:'14px'}" style="width: 40%">                                
                                <el-table-column type="index" label="id" min-width="10%" align="center"></el-table-column>
                                <el-table-column prop="eq_name" label="设备名称" min-width="45%" align="center"></el-table-column>
                                <el-table-column prop="eq_status" label="设备状态" min-width="45%" align="center"></el-table-column>
                            </el-table>
                            <br>
                        </el-row>
                    </template>
                    </el-table-column>
                    <el-table-column prop= "site_name" label="站点名称" min-width="15%" align="center"></el-table-column>
                    <el-table-column prop= "create_time" label="站点创建时间" min-width="15%" align="center" ></el-table-column>
                    <el-table-column prop= "user_name" label="站点创建者" min-width="15%" align="center"></el-table-column>
                    <el-table-column prop= "site_address" label="站点地址" min-width="20%" align="center"></el-table-column>
                    <el-table-column prop= "demand" label="虚拟网络需求" min-width="20%" align="center"></el-table-column>
                    <!-- <el-table-column label="订单状态" min-width="35%" align="center">
                        <template slot-scope="scope">
                            <el-steps :active="scope.row.status" finish-status="success" process-status="finish" align-center>
                                <el-step description="提交订单"></el-step>
                                <el-step description="运营工程师"></el-step>
                                <el-step description="网络工程师"></el-step>
                            </el-steps>
                        </template>
                    </el-table-column> -->
                    <el-table-column label="操作" min-width="15%" align="center">
                        <template slot-scope="scope">
                            <el-button size="mini" @click="order_confirmation(scope.row)">处理订单</el-button>
                        </template>
                    </el-table-column>
                </el-table>
            </div>
        </div>
        <equipmentdialog :dialogVisible="equipmentdialog.dialogVisible" :path="equipmentdialog.path" @Dialog_cancel='Dialog_cancel' @Dialog_submit="Dialog_submit"></equipmentdialog>
    </div>
</template>

<script>

import axios from 'axios'
import equipmentdialog from "@/components/equipmentdialog"

export default{
    name: 'networkorder',
    components: { 
        equipmentdialog 
    },
    inject: ['reload'],
    data(){
        return{
            site_data: [],
            search_info: '',
            equipmentdialog:{
                dialogVisible: false,
                path: '',
            }
        }
    },
    created(){
        this.getdata()
    },
    methods: {
        getdata: function(){
            this.site_data= [],
            axios.get('/api/site/')
            .then((response)=>{
                var res = response.data
                var i = 0
                for(let item of res){
                    var item_demand = ''
                    if(item.demand_num >= 1){
                        item_demand += item.demand_1
                    }
                    if(item.demand_num >= 2){
                        item_demand  = item_demand + ',' + item.demand_2
                    }
                    if(item.demand_num >= 3){
                        item.demand = item_demand + ',' + item.demand_3
                    }
                    if(item.status == 2){
                        this.site_data.push({
                            site_index: i,
                            site_name: item.site_name,
                            site_address: item.site_address,
                            billing_level: (item.billing_level == 1)? '包月' : '包年',
                            demand: item_demand,
                            status: (item.status == 0)? 3: item.status,
                            user_name: item.user,
                            create_time: item.create_time.substring(0,10),
                            manager_name: item.manager_name,
                            manager_time: item.manager_time.substring(0,10),
                        })
                    }
                    i++                
                }
            })
        },
        order_confirmation: function(row){
            this.equipmentdialog.dialogVisible = true
            var pk = row.site_index
            this.equipmentdialog.path = "api/equipment/" + pk + "/"

        },
        Dialog_submit:function(){
            this.equipmentdialog.dialogVisible = false
            this.getdata()

        },
        Dialog_cancel:function(){
            this.equipmentdialog.dialogVisible = false
        },
    },
    computed: {
        sitedata(){
            const search_info = this.search_info
            if(search_info){
                return this.site_data.filter(data => {
                    let show = ["site_name","site_address", "billing_level", "demand"]
                    return show.some(key => {
                        return String(data[key]).toLowerCase().indexOf(search_info.toLowerCase()) > -1
                    })
                })
            }
            return this.site_data
        },
    }
}

</script>

<style scoped>
.head{
  padding: 0px 16px 10px 20px;
  margin: 5px;
}
.colwrapper {
  background-color: #ffffff;
  border-radius: 10px;
  padding: 16px;
  margin: 14px;
}
.SiteData {
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
.networkorder{
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
</style>
