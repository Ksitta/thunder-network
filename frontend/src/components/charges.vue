<template>
  <div id="wrapper">
    <el-container class="container">
      <el-row :gutter="0" id="row_up">
        <el-col :span="16" class="left_col">
		
          <div class="colwrapper">

            <div class="block" style="padding-bottom: 20px">
              <h1>请选择查询区间</h1>
              <el-date-picker
                v-model="query_interval"
                type="daterange"
                align="center"
                unlink-panels
                range-separator="至"
                start-placeholder="开始日期"
                end-placeholder="结束日期"
                :picker-options="pickerOptions"
                value-format="timestamp"
                @change="query">
              </el-date-picker>
            </div>

          </div>

          <div class="colwrapper">
            <div class="block">
              <h1>流量费用信息</h1>
              <ve-line
                :data="linechartData"
                :data-empty="dataEmpty"
                :loading="chartLoading"
                :settings="linechartSettings"
              ></ve-line>
            </div>
          </div>  

          <div class="colwrapper">
            <div>
              <el-table
                :data="piechartData.rows"
                style="width: 100%"
                height="300px"
              >
                <el-table-column prop="site" label="站点" fixed></el-table-column>
                <el-table-column prop="charge" label="产生费用（元）"></el-table-column>
              </el-table>
            </div>
          </div>

          <!-- <div class="colwrapper">
            <h1>流量使用信息</h1>
            <ve-histogram
              :data="chartData"
              :settings="chartSettings">
            </ve-histogram>
          </div> -->

        </el-col>

        <el-col :span="8" class="right_col">
          <div class="colwrapper">

            <div style="color: #7792b1;">
              <p>
                <span style="font-size: 32px; line-height: 26px;">{{totalCharge}}</span>
                <span> 元</span>
              </p>
              <p>
                流量费用
                <i class="el-icon-coin"></i>
              </p>
              <el-button type="text" @click="mail(1)">寄送月度账单</el-button>
              <el-button type="text" @click="mail(2)">寄送年度账单</el-button>
            </div>

          </div>

          <div class="colwrapper">
            <h1>各站点流量费用占比</h1>
            <ve-pie
              :data="piechartData"
              :data-empty="dataEmpty"
              :loading="chartLoading"
              :settings="piechartSettings">
            </ve-pie>
          </div>
        </el-col>

      </el-row>
    </el-container>
  </div>
</template>

<script>

import axios from 'axios'
// import { Message } from 'element-ui';


export default {
  name: 'user_home',
  data() {
      return {
        pickerOptions: {
          shortcuts: [{
            text: '最近一周',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 7);
              picker.$emit('pick', [start, end]);
            }
          }, {
            text: '最近一个月',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 30);
              picker.$emit('pick', [start, end]);
            }
          }, {
            text: '最近三个月',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 90);
              picker.$emit('pick', [start, end]);
            }
          }]
        },
        query_interval: "",

        totalFlow: 0,

        chartLoading: false,
        linechartSettings : {
          legendName: {
            'charge': "费用（元）",
          },
          xAxisType: 'time',
        },
        piechartSettings : {
          roseType: 'radius',
          legendName: {
            'site': "站点",
            'charge': "费用",
          }
        },
        linechartData: {
          columns: ['time', 'charge'],
          rows: [
            // {'time': '2020-12-23', 'charge': 43},
          ],
        },
        piechartData: {
          columns: ['site', 'charge'],
          rows: [
          ]
        },
      }
  },
  methods: {
    query: function(value) {
      let startdate = value[0] / 1000;
      let enddate = value[1] / 1000 + 86399;
      console.log(startdate);
      console.log(enddate);
      this.totalFlow = 0;
      this.chartLoading = true;
      this.linechartData.rows = [];
      this.piechartData.rows = [];
      axios.get("/api/flow/", {
        params: {
          from_time: startdate,
          to_time: enddate,
        },
      }).then((response) => {
        console.log(response)
        let flow_data = response.data.flow_data;
        for (let item of flow_data) {
          this.totalFlow += parseInt(item.up) + parseInt(item.down)
          this.linechartData.rows.push({
            time: item.time,
            charge: 0.8 * (parseInt(item.up) + parseInt(item.down)) / 1024 / 1024 / 1024,
          });
        }
        let sites_flow = response.data.sites_flow;
        for (let item of sites_flow) {
          this.piechartData.rows.push({
            site: item.site_name,
            charge: (0.8 * (item.total_up + item.total_down)  / 1024 / 1024 / 1024).toFixed(2),
          });
        }
        this.chartLoading = false;
      });
    },
    mail(mory) {
      let hintmsg = "";
      if (mory == 1) {
        hintmsg = "将向您的邮箱寄送月度账单邮件，是否继续？";
      } else {
        hintmsg = "将向您的邮箱寄送年度账单邮件，是否继续？";
      }
      this.$confirm(hintmsg, '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        axios.post('/api/mail/', {
          mory: parseInt(mory)
        })
        .then((response) => {
          console.log(response);
          this.$message({
            type: 'success',
            message: '发送成功!'
          });
        })
        .catch((error) => {
          this.$message({
            type: 'error',
            message: '发送失败!'
          });
          console.log(error)
        });
      });
    },
  },
  props: {
    show: {
      type: Boolean,
      default: () => false,
    }
  },

  computed: {
    dataEmpty() {
      return this.linechartData.rows.length == 0;
    },
    totalCharge: function() {
      return (0.8 * this.totalFlow / 1024 / 1024 / 1024).toFixed(2);
    }
  },

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

#wrapper {
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

</style>
