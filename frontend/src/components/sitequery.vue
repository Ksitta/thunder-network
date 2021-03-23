<template>
    <div id = "wrapper_sitequery">
        <el-row type="flex" class="unfinished_SearchSite" justify="space-between">
            <div style="display: inline-block">未处理订单：</div>
            <el-input v-model="unfinished_search" style="display: inline-block; margin-top: 0px; width: 400px; height: 40px" placeholder="请输入搜索内容" suffix-icon="el-icon-search"></el-input>
        </el-row>
        <div class="unfinished_SiteData">
            <el-table :data="unfinished_sitedata" style="width: 100%" max-height="400" height="300">
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
            <div style="display: inline-block">已处理订单：</div>
            <el-input v-model="finished_search" style="display: inline-block; margin-top: 0px; width: 400px; height: 40px" placeholder="请输入搜索内容" suffix-icon="el-icon-search"></el-input>
        </el-row>
        <div class="finished_SiteData">
            <el-table :data="finished_sitedata" style="width: 100%" max-height="400" height="300">
                <el-table-column prop= "site_name" label="站点名称" width="180" fixed ></el-table-column>
                <el-table-column prop= "site_address" label="站点地址" width="360"></el-table-column>
                <el-table-column prop= "billing_level" label="计费方式" width="140"></el-table-column>
                <el-table-column prop= "demand_1" label="虚拟网络需求1" width="180"></el-table-column>
                <el-table-column prop= "demand_2" label="虚拟网络需求2" width="180"></el-table-column>
                <el-table-column prop= "demand_3" label="虚拟网络需求3" width="180"></el-table-column>
            </el-table>
        </div>
    </div>
</template>

<script>

import axios from 'axios'

export default{
    name: 'site_query',
    data(){
        return{
            unfinished_data: [{
                    site_name: "site1",
                    site_address: "清华大学",
                    billing_level: '包月',
                    demand_1: "Visitor",
                    demand_2: "Management",
                    demand_3: "",
                },
                {
                    site_name: "site2",
                    site_address: "清华大学",
                    billing_level: '包年',
                    demand_1: "Guest",
                    demand_2: "Management",
                    demand_3: "",
                }
            ],
            finished_data: [{
                    site_name: "site1",
                    site_address: "清华大学",
                    billing_level: '包月',
                    demand_1: "Visitor",
                    demand_2: "Management",
                    demand_3: "",
                },
                {
                    site_name: "site2",
                    site_address: "清华大学",
                    billing_level: '包年',
                    demand_1: "Guest",
                    demand_2: "Management",
                    demand_3: "",
                }
            ],
            unfinished_search: '',
            finished_search: '',
        }
    },
    created(){
        axios.get('/api/site/')
        .then((response)=>{
            var res = response.data.data
            for(let item of res){
                if(item.status == 1){
                    this.unfinished_data.push({
                        site_name: item.site_name,
                        site_address: item.site_address,
                        billing_level: (item.billing_level == 1)? '包月' : '包年',
                        demand_1: item.demand_1,
                        demand_2: item.demand_2,
                        demand_3: item.demand_3
                    })
                }else{
                    this.finished_data.push({
                        site_name: item.site_name,
                        site_address: item.site_address,
                        billing_level: (item.billing_level == 1)? '包月' : '包年',
                        demand_1: item.demand_1,
                        demand_2: item.demand_2,
                        demand_3: item.demand_3
                    })
                }
            }
        })
    },
    methods: {
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
.SearchSite{
    position: relative;
    right: 0px;
}
</style>