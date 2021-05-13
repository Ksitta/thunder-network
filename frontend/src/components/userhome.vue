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
            <h1>流量使用信息</h1>
            <ve-histogram
              :data="chartData"
              :settings="chartSettings">
            </ve-histogram>
          </div>
        </el-col>

        <el-col :span="8" class="right_col">
          <div class="colwrapper">

            <div style="color: #7792b1;">
              <p>
                <span style="font-size: 32px; line-height: 26px;">{{totalFlow}}</span>
                <span> GB</span>
              </p>
              <p>
                今日流量
                <i class="el-icon-odometer"></i>
              </p>
            </div>

          </div>

          <div class="colwrapper">

            <!-- <h1>站点数据雷达图</h1> -->
            <ve-radar :data="radarChartData" :settings="radarChartSettings" :legend="legend" :title="title" :height="chartHeight"></ve-radar>

          </div>
        </el-col>

      </el-row>
    </el-container>
  </div>
</template>

<script>

import axios from 'axios'
import { Message } from 'element-ui';
import md5 from 'js-md5'


export default {
  name: 'user_home',
  data() {
      return {
        totalFlow: "/",
        chartLoading: false,
        chartSettings : {
          showLine: ['time', 'total'],
          legendName: {
            'up': "上行流量（Byte）",
            'down': "下行流量（Byte）",
            'total': "总流量（Byte）",
          },
        },
        radarChartSettings : {
          labelMap: {
            'site': '站点',
            'views': '访问量',
            'up': '上行流量',
            'down': '下行流量'
          },
        },
        title: {
          text: "\n\n站点流量数据雷达图",
          left: "center",
          textStyle: {
            fontSize: 16,
          },
        },
        legend : {
          bottom: "10",
        },
        chartHeight: '500px',
        chartData: {
          columns: ['time', 'up', 'down', 'total'],
          rows: [],
        },
        info: {
          username: "",
          contact_details: "",
          contact_email: "",
          contact_address: "",
          user_type: "",
        },
        radarChartData: {
          columns: ['site', 'views', 'up', 'down'],
          rows: [],
        }
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
    }
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
    }
  },

  mounted: function() {
    this.refresh()
  },

  created() {
    this.loading = true;
    axios.get("/api/flow/").then((response) => {
      let res = response.data;
      this.totalFlow = ((parseInt(res.total_up) + parseInt(res.total_down)) / 1024 / 1024 / 1024).toFixed(2);
      let flow_data = res.flow_data;
      for (let item of flow_data) {
        this.chartData.rows.push({
          time: item.time,
          up: item.up,
          down: item.down,
          total: item.up + item.down,
        });
      }
      let sites_flow = res.sites_flow;
      this.radarChartData.rows = []
      for (let item of sites_flow) {
        this.radarChartData.rows.push({
          site: item.site_name,
          up: item.total_up,
          down: item.total_down,
          views: item.view_counts,
        });
      }
      this.loading = false;
    });
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
