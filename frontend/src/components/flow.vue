<template>
    <div id = "wrapper_sitequery">
        <div class="colwrapper">
			<h1>流量使用数据</h1>
			<ve-line :data="chartData"></ve-line>
		</div>
		<div class="colwrapper">
			<div class="unfinished_SiteData">
                <el-table :data="unfinished_sitedata" style="width: 100%" @row-click="showDialog" maxheight="300px" height="300px">
                    <el-table-column prop= "date" label="日期" fixed ></el-table-column>
                    <el-table-column prop= "flow_data" label="流量数据"></el-table-column>
                </el-table>
            </div>
		</div>
    </div>
</template>

<script>

// import axios from 'axios'

export default{
    name: 'flow',
    data(){
        return{
			chartData: {
				columns: ['日期', '访问用户'],
				rows: [
					{ '日期': '2018-05-22', '访问用户': 32371, '下单用户': 19810 },
					{ '日期': '2018-05-23', '访问用户': 12328, '下单用户': 4398 },
					{ '日期': '2018-05-24', '访问用户': 92381, '下单用户': 52910 }
				]
			}
            // unfinished_data: [],
            // finished_data: [],
            // unfinished_search: '',
            // finished_search: '',
            // siteinfo:{site_address:""},
            // SiteDialog:{
            //     dialogVisible: false
            // }
        }
    },
    created(){
        // axios.get('/api/site/')
        // .then((response)=>{
        //     var res = response.data
        //     var i = 0
        //     for(let item of res){
        //         if(item.status == 1){
        //             this.unfinished_data.push({
        //                 site_index: i,
        //                 site_name: item.site_name,
        //                 site_address: item.site_address,
        //                 billing_level: (item.billing_level == 1)? '包月' : '包年',
        //                 demand_1: (item.demand_1 == '')? '无' : item.demand_1,
        //                 demand_2: (item.demand_2 == '')? '无' : item.demand_2,
        //                 demand_3: (item.demand_3 == '')? '无' : item.demand_3
        //             })
        //         }else{
        //             this.finished_data.push({
        //                 site_index: i,
        //                 site_name: item.site_name,
        //                 site_address: item.site_address,
        //                 billing_level: (item.billing_level == 1)? '包月' : '包年',
        //                 demand_1: (item.demand_1 == '')? '无' : item.demand_1,
        //                 demand_2: (item.demand_2 == '')? '无' : item.demand_2,
        //                 demand_3: (item.demand_3 == '')? '无' : item.demand_3
        //             })
        //         }
        //         i++
        //     }
        // })
    },
    // methods: {
        // showDialog: function(row){
        //     this.SiteDialog.dialogVisible = true
        //     var pk = row.site_index
        //     console.log(pk)
        //     var path = "/api/site/" + pk + "/"
        //     axios.get(path)
        //     .then((response)=>{
        //         var res=response.data
        //         console.log(res)
        //         this.siteinfo.site_name = res.site_name
        //         this.siteinfo.site_address = res.site_address
        //         this.siteinfo.billing_level = (res.billing_level == 1)? '包月' : '包年'
        //         this.siteinfo.demand_num = res.demand_num
        //         this.siteinfo.demand_1 = (res.demand_1 == '')? '无' : res.demand_1
        //         this.siteinfo.demand_2 = (res.demand_2 == '')? '无' : res.demand_2
        //         this.siteinfo.demand_3 = (res.demand_3 == '')? '无' : res.demand_3
        //         this.siteinfo.status = (res.status == 1)? '未处理':'处理'
        //         var eqs = res.eqs
        //         this.siteinfo.eqs = []
        //         for(let item of eqs){
        //             this.siteinfo.eqs.push({
        //                 eq_name: item.eq_name,
        //                 eq_status: (item.eq_status == 1)? '已部署' : '未部署'
        //             })
        //         }
        //         console.log(this.siteinfo)
        //     })

        // },
        // Dialog_cancel:function(){
        //     this.SiteDialog.dialogVisible = false
        // }
    // },
    // computed: {
    //     unfinished_sitedata(){
    //         const unfinished_search = this.unfinished_search
    //         if(unfinished_search){
    //             return this.unfinished_data.filter(data => {
    //                 return Object.keys(data).some(key => {
    //                     return String(data[key]).toLowerCase().indexOf(unfinished_search) > -1
    //                 })
    //             })
    //         }
    //         return this.unfinished_data
    //     },
    //     finished_sitedata(){
    //         const finished_search = this.finished_search
    //         if(finished_search){
    //             return this.finished_data.filter(data => {
    //                 return Object.keys(data).some(key => {
    //                     return String(data[key]).toLowerCase().indexOf(finished_search) > -1
    //                 })
    //             })
    //         }
    //         return this.finished_data
    //     }
    // }
}
</script>

<style scoped>
.colwrapper {
  background-color: #ffffff;
  border-radius: 10px;
  padding: 16px;
  margin: 14px;
}
</style>