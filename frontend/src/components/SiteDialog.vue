<template>
    <el-dialog
            class="SiteDialog"
            style="text-align: center"
            title="订单详情"
            :close-on-click-modal="false"
            :visible.sync="dialogVisible"
            :show-close= false
            width="50%">
        <el-form label-width="200px">
            <el-form-item label="站点名称:">
                <span class="form_item">{{siteinfo.site_name}}</span>
            </el-form-item>
            <el-form-item label="站点地址:">
                <span class="form_item">{{siteinfo.site_address}}</span>
            </el-form-item>
            <el-form-item label="付费方式:">
                <span class="form_item">{{siteinfo.billing_level}}</span>
            </el-form-item>
            <el-form-item label="网络需求总数:">
                <span class="form_item">{{siteinfo.demand_num}}</span>
            </el-form-item>
            <el-form-item label="虚拟网络网络需求:">
                <span v-if="siteinfo.demand_num == 1" class="form_item">{{siteinfo.demand_1}}</span>
                <span v-if="siteinfo.demand_num == 2" class="form_item">{{siteinfo.demand_1}}, {{siteinfo.demand_2}}</span>
                <span v-if="siteinfo.demand_num == 3" class="form_item">{{siteinfo.demand_1}}, {{siteinfo.demand_2}}, {{siteinfo.demand_3}}</span>
            </el-form-item>
            <el-form-item label="订单处理进程:">
                <span class="form_item">{{siteinfo.status}}</span>
            </el-form-item>
            <p align= "center">网络设备详情：</p>
            <el-row>
                <el-col :offset="4"> 
                    <el-table :data="siteinfo.eqs" cell-style="padding:7px" style="width:70%" border>
                        <el-table-column type="index" align="center"></el-table-column>
                        <el-table-column prop="eq_name" label="设备名称" width="170"></el-table-column>
                        <el-table-column prop="eq_status" label="设备状态" width="170"></el-table-column>
                    </el-table>
                </el-col>
            </el-row>
            <!-- <div v-for="(eq, index) in siteinfo.eqs" :key="eq">
                <el-form-item :label="`网络设备${(index + 1)}名称：`"> 
                    <span class="form_item">{{eq.eq_name}}</span>
                </el-form-item>
                <el-form-item :label="`网络设备${(index + 1)}状态：`"> 
                    <span class="form_item">{{eq.eq_status}}</span>
                </el-form-item>
            </div> -->
            <!-- 该部分为form式网络信息 -->
            <!-- label中有变量前面要加冒号绑定 -->
            <br>
            <el-button v-on:click="cancel()">确定</el-button>
        </el-form>
    </el-dialog>
</template>
<script>
export default{
    name: "SiteDialog",
    props: {
        dialogVisible: {
            type: Boolean,
            default: () => false
        },
        siteinfo: {
            type: Object,
            default: () => {
                return {
                    site_name: '',
                    site_address: '',
                    billing_level: '',
                    demand_num: 0,
                    demand_1: '',
                    demand_2: '',
                    demand_3: '',
                    status: '',
                    eqs: []
                }
            }
        }
    },
    methods: {
        cancel:function(){
            console.log(this.siteinfo)
            this.$emit('Dialog_cancel')
        }
    }
}
</script>

