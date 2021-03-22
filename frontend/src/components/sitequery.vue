带边框表格，固定表头，流体高度，排序
<template>
    <div id = "wrapper_sitequery">
        <div class="SearchSite">
            <div style="display: inline-block">搜索：</div>
            <el-input v-model="search" style="display: inline-block; margin-right: 0px; width: 500px; height: 40px" placeholder="请输入搜索内容" suffix-icon="el-icon-search"></el-input>
        </div>
        <div class="SiteData">
            <el-table :data="siteData" style="width: 100%" max-height="600">
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
            datas: [{
                site_name: "site1",
                site_address: "清华大学",
                billing_level: '包月',
                demand_1: "Guest",
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
            search: '',
            sitedata: []
        }
    },
    created(){
        axios.get('/api/site/')
        .then((response)=>{
            var res = response.data.data
            for(let item of res){
                this.datas.push({
                    site_name: item.site_name,
                    site_address: item.site_address,
                    billing_level: (item.billing_level == 1)? '包月' : '包年',
                    demand_1: item.demand_1,
                    demand_2: item.demand_2,
                    demand_3: item.demand_3
                })
            }
        })
    },
    methods: {
    },
    computed: {
        siteData(){
            const search = this.search
            if(search){
                return this.datas.filter(data => {
                    return Object.keys(data).some(key => {
                        return String(data[key]).toLowerCase().indexOf(search) > -1
                    })
                })
            }
            return this.datas
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