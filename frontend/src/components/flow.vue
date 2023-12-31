<template>
  <div id="wrapper_sitequery">
    <div class="colwrapper">
      <el-select v-model="site_selected" placeholder="请选择站点">
        <el-option
          v-for="item in site_list"
          :key="item.pk"
          :label="item.site_name"
          :value="item.pk"
          :disabled="item.disabled"
        >
        </el-option>
      </el-select>

      <el-select
        v-model="device_selected"
        :disabled="site_selected.length == 0"
        placeholder="请选择设备"
        clearable
      >
        <el-option
          v-for="item in device_list"
          :key="item.pk"
          :label="item.eq_name"
          :value="item.pk"
          :disabled="item.disabled"
        >
        </el-option>
      </el-select>

      <el-button v-on:click="query()" :disabled="site_selected.length == 0">查询</el-button>

      <div class="block" style="padding-top: 20px; padding-bottom: 5px">
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
        >
        </el-date-picker>
      </div>

      <el-divider content-position="center">请选择查询站点和设备，设备项留空以查询站点总流量</el-divider>
      
      <h1>流量使用数据</h1>

      <ve-line
        :data="chartData"
        :data-empty="dataEmpty"
        :loading="loading"
        :settings="chartSettings"
      ></ve-line>
    </div>

    <div class="colwrapper">
      <div>
        <el-table
          :data="chartData.rows"
          style="width: 100%"
          height="300px"
        >
          <el-table-column prop="time" label="时间" fixed></el-table-column>
          <el-table-column prop="up" label="上行流量（byte）"></el-table-column>
          <el-table-column prop="down" label="下行流量（byte）"></el-table-column>
        </el-table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import "v-charts/lib/style.css";

export default {
  name: "flow",
  data() {
    return {
      loading: false,
      chartSettings: {
        legendName: {
          'up': "上行流量（Byte）",
          'down': "下行流量（Byte）",
        }
      },
      chartData: {
        columns: ["time", "up", "down"],
        rows: [],
      },
      site_list: [],
      site_selected: "",
      device_selected: "",

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
    };
  },
  computed: {
    dataEmpty() {
      return this.chartData.rows.length == 0;
    },
    device_list() {
      if (this.site_selected.length == 0) return [];
      return this.site_list[this.site_selected].eqs;
    },
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
  },
  methods: {
    query: function () {
      if (this.query_interval == "") {
        this.$message.warning("请选择查询的日期范围");
        return;
      }

      let startdate = this.query_interval[0] / 1000;
      let enddate = this.query_interval[1] / 1000 + 86399;
      console.log(startdate);
      console.log(enddate);

      this.loading = true;
      this.chartData.rows = []
      axios.get("/api/flow/" + this.site_selected + "/", {
        params: {
          from_time: startdate,
          to_time: enddate,
        },
      }).then((response) => {
        let flow_data;
        if (this.device_selected.length == 0) {
          flow_data = response.data.site_flow.flow_data;
        } else {
          flow_data = response.data.eq_flows[this.device_selected].flow_data;
        }
        for (let item of flow_data) {
          this.chartData.rows.push({
            time: item.time,
            up: item.up,
            down: item.down,
          });
        }
        this.loading = false;
      });
    },
  },
};
</script>

<style scoped>
.colwrapper {
  background-color: #ffffff;
  border-radius: 10px;
  padding: 16px;
  margin: 14px;
}
.el-select {
  margin-left: 20px;
  margin-right: 20px;
}
.el-button {
  margin-left: 20px;
  margin-right: 20px;
}
.el-divider__text {
  color: #c0c4cc;
}
</style>