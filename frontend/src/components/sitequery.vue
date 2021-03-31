<template>
    <div id = "wrapper_sitequery">
        <el-row type="flex" class="unfinished_SearchSite" justify="space-between">
            <div style="display: inline-block; padding: 10px;">未处理订单：</div>
            <el-input v-model="unfinished_search" style="display: inline-block; margin-top: 0px; width: 400px; height: 40px" placeholder="请输入搜索内容" suffix-icon="el-icon-search"></el-input>
        </el-row>
        <div class="unfinished_SiteData">
            <el-table :data="unfinished_sitedata" style="width: 100%" @row-click="showDialog">
                <el-table-column prop= "site_name" label="站点名称" width="180" fixed ></el-table-column>
                <el-table-column prop= "site_address" label="站点地址" width="360"></el-table-column>
                <el-table-column prop= "billing_level" label="计费方式" width="140"></el-table-column>
                <el-table-column prop= "demand_1" label="虚拟网络需求1" width="180"></el-table-column>
                <el-table-column prop= "demand_2" label="虚拟网络需求2" width="180"></el-table-column>
                <el-table-column prop= "demand_3" label="虚拟网络需求3" width="180"></el-table-column>
            </el-table>
        </div>
        <br>
        <el-row type="flex" class="finished_SearchSite" justify="space-between">
            <div style="display: inline-block; padding: 10px;">已处理订单：</div>
            <el-input v-model="finished_search" style="display: inline-block; margin-top: 0px; width: 400px; height: 40px" placeholder="请输入搜索内容" suffix-icon="el-icon-search"></el-input>
        </el-row>
        <div class="finished_SiteData">
            <el-table :data="finished_sitedata" style="width: 100%" @row-click="showDialog">
                <el-table-column prop= "site_name" label="站点名称" width="180" fixed ></el-table-column>
                <el-table-column prop= "site_address" label="站点地址" width="360"></el-table-column>
                <el-table-column prop= "billing_level" label="计费方式" width="140"></el-table-column>
                <el-table-column prop= "demand_1" label="虚拟网络需求1" width="180"></el-table-column>
                <el-table-column prop= "demand_2" label="虚拟网络需求2" width="180"></el-table-column>
                <el-table-column prop= "demand_3" label="虚拟网络需求3" width="180"></el-table-column>
            </el-table>
        </div>
        <SiteDialog :dialogVisible="SiteDialog.dialogVisible" @Dialog_cancel='Dialog_cancel' :siteinfo="siteinfo"></SiteDialog>
    </div>
</template>

<script>

import axios from 'axios'
import SiteDialog from "@/components/SiteDialog"

export default{
    name: 'site_query',
    components: {
        SiteDialog
    },
    data(){
        return{
            unfinished_data: [],
            finished_data: [],
            unfinished_search: '',
            finished_search: '',
            siteinfo:{site_address:""},
            SiteDialog:{
                dialogVisible: false
            }
        }
    },
    created(){
        axios.get('/api/site/')
        .then((response)=>{
            var res = response.data
            var i = 0
            for(let item of res){
                if(item.status == 1){
                    this.unfinished_data.push({
                        site_index: i,
                        site_name: item.site_name,
                        site_address: item.site_address,
                        billing_level: (item.billing_level == 1)? '包月' : '包年',
                        demand_1: (item.demand_1 == '')? '无' : item.demand_1,
                        demand_2: (item.demand_2 == '')? '无' : item.demand_2,
                        demand_3: (item.demand_3 == '')? '无' : item.demand_3
                    })
                }else{
                    this.finished_data.push({
                        site_index: i,
                        site_name: item.site_name,
                        site_address: item.site_address,
                        billing_level: (item.billing_level == 1)? '包月' : '包年',
                        demand_1: (item.demand_1 == '')? '无' : item.demand_1,
                        demand_2: (item.demand_2 == '')? '无' : item.demand_2,
                        demand_3: (item.demand_3 == '')? '无' : item.demand_3
                    })
                }
                i++
            }
        })
    },
    methods: {
        showDialog: function(row){
            this.SiteDialog.dialogVisible = true
            var pk = row.site_index
            console.log(pk)
            var path = "/api/site/" + pk + "/"
            axios.get(path)
            .then((response)=>{
                var res=response.data
                console.log(res)
                this.siteinfo.site_name = res.site_name
                this.siteinfo.site_address = res.site_address
                this.siteinfo.billing_level = (res.billing_level == 1)? '包月' : '包年'
                this.siteinfo.demand_num = res.demand_num
                this.siteinfo.demand_1 = (res.demand_1 == '')? '无' : res.demand_1
                this.siteinfo.demand_2 = (res.demand_2 == '')? '无' : res.demand_2
                this.siteinfo.demand_3 = (res.demand_3 == '')? '无' : res.demand_3
                this.siteinfo.status = (res.status == 1)? '未处理':'处理'
                var eqs = res.eqs
                this.siteinfo.eqs = []
                for(let item of eqs){
                    this.siteinfo.eqs.push({
                        eq_name: item.eq_name,
                        eq_status: (item.eq_status == 1)? '已部署' : '未部署'
                    })
                }
                console.log(this.siteinfo)
            })

        },
        Dialog_cancel:function(){
            this.SiteDialog.dialogVisible = false
        }
    },
    computed: {
        unfinished_sitedata(){
            const unfinished_search = this.unfinished_search
            if(unfinished_search){
                return this.unfinished_data.filter(data => {
                    return Object.keys(data).some(key => {
                        return String(data[key]).toLowerCase().indexOf(unfinished_search) > -1
                    })
                })
            }
            return this.unfinished_data
        },
        finished_sitedata(){
            const finished_search = this.finished_search
            if(finished_search){
                return this.finished_data.filter(data => {
                    return Object.keys(data).some(key => {
                        return String(data[key]).toLowerCase().indexOf(finished_search) > -1
                    })
                })
            }
            return this.finished_data
        }
    }
}
</script>

<style scoped>
.unfinished_SiteData {
    margin-top: 10px;
}
.finished_SiteData {
    margin-top: 10px;
}
</style>