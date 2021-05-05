<template>
    <div class="set_ssid">
        <el-dialog
                custom-class="ssiddialog"
                class="ssid_dialog"
                style="text-align: center"
                title="WLAN设置"
                :close-on-click-modal="false"
                :visible.sync="dialogVisible"
                :show-close= false
                width="40%"
                >
            <div class="wlan_set" style="margin-top: -20px">
                <el-form class="form" :rules="rules" ref="form" :model="wlan_info" label-width="120px" label-position="left">
                    <el-form-item label="WLAN:" class="label-style" required>
                        <el-switch v-model="wlan_info.enable" style="margin-right: 320px;"></el-switch>
                    </el-form-item>
                    <el-form-item label="WLAN名称:" class="label-style" prop="name">
                        <el-input class="wlan_input" v-model="wlan_info.name" placeholder="请输入网络名" maxlength="32" show-word-limit clearable size="medium"></el-input>
                    </el-form-item>
                    <el-form-item label="最大用户数:" class="label-style" prop="maxUserNumber">
                        <el-input class="wlan_input" v-model="wlan_info.maxUserNumber" placeholder="请输入最大用户数，不可超过512" size="medium" clearable></el-input>
                    </el-form-item>
                    <el-form-item label="射频类型:" class="label-style" prop="relativeRadios">
                        <el-select class="wlan_input" v-model="wlan_info.relativeRadios" size="medium">
                            <el-option 
                                v-for="item in radios_options" :key="item.value" :label="item.label" :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item label="用户隔离:" class="label-style" required>
                        <el-switch v-model="wlan_info.userSeparation" style="margin-right: 320px;"></el-switch>
                    </el-form-item>
                    <el-form-item label="SSID认证:" class="label-style" prop="mode">
                        <el-radio-group v-model="wlan_info.ssidAuth.mode" class="wlan_input" style="margin-left: -70px">
                            <el-radio label="open" class = "wlan-radio-style"></el-radio>
                            <el-radio label="psk" class = "wlan-radio-style"></el-radio>
                            <el-radio label="ppsk" class = "wlan-radio-style"></el-radio>
                        </el-radio-group>
                    </el-form-item>
                    <el-form-item label="SSID安全模式:" class="label-style" v-if="wlan_info.ssidAuth.mode == 'psk'" prop="pskEncryptType">
                        <el-radio-group v-model="wlan_info.ssidAuth.pskEncryptType" class="wlan_input" style="margin-left: -17px">
                            <el-radio label="wep" class = "psk-radio-style"></el-radio>
                            <el-radio label="wpa1AndWpa2" class = "psk-radio-style"></el-radio>
                            <el-radio label="wpa2" class = "psk-radio-style"></el-radio>
                        </el-radio-group>
                    </el-form-item>
                    <el-form-item label="SSID安全模式:" class="label-style" v-if="wlan_info.ssidAuth.mode == 'ppsk'" prop="pskEncryptType">
                        <el-radio-group v-model="wlan_info.ssidAuth.pskEncryptType" class="wlan_input" style="margin-left: -17px">
                            <el-radio label="wep" class = "psk-radio-style" disabled></el-radio>
                            <el-radio label="wpa1AndWpa2" class = "psk-radio-style"></el-radio>
                            <el-radio label="wpa2" class = "psk-radio-style"></el-radio>
                        </el-radio-group>
                    </el-form-item>
                    <el-form-item label="WIFI密码:" class="label-style" prop="securityKey">
                        <el-input class="wlan_input" v-model="wlan_info.ssidAuth.securityKey" placeholder="仅可接受字符串与数字，长度为5位" size="medium" type="password" clearable v-if="wlan_info.ssidAuth.pskEncryptType == 'wep'"></el-input>
                        <el-input class="wlan_input" v-model="wlan_info.ssidAuth.securityKey" placeholder="不接受问号与空格，长度为8-63位" size="medium" type="password" clearable v-if="wlan_info.ssidAuth.pskEncryptType != 'wep'"></el-input>
                    </el-form-item>
                    <el-form-item label="密码加密:" class="label-style" v-if="wlan_info.ssidAuth.pskEncryptType == 'wpa2'">  
                        <el-radio-group v-model="wlan_info.ssidAuth.securityKeyType" class="wlan_input" style="margin-left: -65px">
                            <el-radio label="AES" class = "radio-style" ></el-radio>
                            <el-radio label="AES-TKIP" class = "radio-style"></el-radio>
                            <el-radio label="TKIP" class = "radio-style"></el-radio>
                        </el-radio-group>
                    </el-form-item>
                <div class="footer-btn">
                    <el-button plain type="danger" @click="cancel" size="medium" >取消</el-button>
                    <el-button plain type="primary" size="medium" @click="Submit('form')">确定</el-button>
                    <!-- <el-button plain type="primary" size="medium" @click="cancel" v-if="check == 1">返回</el-button> -->
                </div>

                </el-form>
            </div>
        </el-dialog>
    </div>
</template>

<script>
import axios from "axios";

export default{
    name: "ssiddialog",
    props: {
        dialogVisible: {
            type: Boolean,
            default: () => false
        },
        path: {
            type: String,
            default: () => ''
        },
        wlan_info: {
            type: Object,
        },
        check: {
            type: Number,
            default: () => 0
        }
    },
    data(){
        // var passReg1 = /^[0-9A-Za-z]{5}$/
        // var validateKey = (rule, value, callback) => {
        //     if(!value) {
        //         return callback(new Error("密码不可为空！"))
        //     }
        //     else if(this.wlan_info.ssidAuth.pskEncryptType == 'wep' && !passReg1.test(value)) {
        //         callback(new Error("密码长度为5位,只能包含大小写字母和数字"))
        //     }
        //     else if(this.wlan_info.ssidAuth.pskEncryptType != 'wep'){
        //         if(value.length < 8 || value.length > 63){
        //             callback(new Error("密码长度限制为8-63位！"))
        //         }
        //         if(value.split(' ').join('').length != value.length){
        //             callback(new Error("密码中不得包含空格！"))
        //         }
        //         if(value.split('?').join('').length != value.length){
        //             callback(new Error("密码中不得包含问号！"))
        //         }
        //     }
        // }
        // var validateKeyType = (rule, value, callback) => {
        //     if(!value && this.wlan_info.ssidAuth.pskEncryptType == 'wpa2') {
        //         return callback(new Error("请选择密码加密方法！"))
        //     }
        // }
        // var validateEncryptType = (rule, value, callback) => {
        //     if(!value && this.wlan_info.ssidAuth.mode != 'open') {
        //         return callback(new Error("请选择密码加密方法！"))
        //     }
        // }
        return{
            radios_options: [
                {
                value: '1',
                label: '1 --- 2.4G(wlan-radio 0/0/0)',
                },
                {
                value: '2',
                label: '2 --- 5G(wlan-radio 0/0/1)',
                },
                {
                value: '3',
                label: '3 --- 2.4G(wlan-radio 0/0/0)&5G(wlan-radio 0/0/1)',
                },
                {
                value: '4',
                label: '4 --- 5G(wlan-radio 0/0/2)',
                },
                {
                value: '5',
                label: '5 --- 2.4G(wlan-radio 0/0/0)&5G(wlan-radio 0/0/2)',
                },
                {
                value: '6',
                label: '6 --- 5G(wlan-radio 0/0/1)&5G(wlan-radio 0/0/2)',
                },
                {
                value: '7',
                label: '7 --- 2.4G(wlan-radio 0/0/0)&5G(wlan-radio 0/0/1)&5G(wlan-radio 0/0/2)',
                },
                
            ],
            rules:{
                name: [{required: true, message: "WLAN不可为空！", trigger: 'blur'}],
                maxUserNumber: [{required: true, message: "最大用户数不可为空！", trigger: 'blur'}],
                relativeRadios: [{required: true, message: "请选择射频类型！", trigger: 'blur'}],
                // mode:  [{required: true, message: "请选择SSID认证模式！", trigger: 'blur'}],
                // pskEncryptType: [{required: true, validator: validateEncryptType, trigger: 'blur'}],
                // securityKey: [{required: true, validator: validateKey, trigger: 'blur'}],
                // securityKeyType: [{required: true, validator: validateKeyType, trigger: 'blur'}],
            },

        }
    },
    methods:{
        Submit:function(form){
            this.$refs[form].validate(valid => {
                if(valid){
                    this.$emit('ssiddialog_cancel')
                    let submitinfo = {
                        enable: this.wlan_info.enable,
                        name: this.wlan_info.name,
                        maxUserNumber: parseInt(this.wlan_info.maxUserNumber),
                        relativeRadios: parseInt(this.wlan_info.relativeRadios),
                        userSeparation: this.wlan_info.userSeparation,
                        ssidAuth:{
                            mode: this.wlan_info.ssidAuth.mode,
                            pskEncryptType: this.wlan_info.ssidAuth.pskEncryptType,
                            securityKey: this.wlan_info.ssidAuth.securityKey,
                            securityKeyType: this.wlan_info.ssidAuth.securityKeyType,
                        }
                    }
                    console.log('1',submitinfo)
                    axios.post(this.path, submitinfo)
                    .then(response => {
                        console.log("response:",response)
                        if(response.status === 201){
                            this.$message.success("提交成功！")
                            this.$emit('ssiddialog_submit')
                        }else{
                            alert(response.status)
                        }
                    }).catch (error => {
                        alert('error！')
                        console.log(error)
                    })
                }else{
                   console.log('error submit!') 
                   return false
                }
            })
        },
        cancel:function(){
            this.$emit('ssiddialog_cancel')
        }
    },
}
</script>

<style>
.ssiddialog{
    border-radius: 20px;
}
.radio-style .el-radio__label{
    font-size: 10px;
    width: 10px;
}
.wlan-radio-style .el-radio__label{
    font-size: 15px;
}
.psk-radio-style .el-radio__label{
    font-size: 13px;
}
.label-style .el-form-item__label{
    text-align: right;
}
.label-style .el-form-item__content{
    margin-left: 80px;
}

</style>
<style scoped>
.ssid_dialog {
    height: 100%;
}
.form{
    padding-bottom: 10px;
    margin-left: 15px;
}
.wlan_input{
    width: 80%;
    margin-right: 105px;
}

.footer-btn{
    margin-top: 30px;
    text-align: right;
    margin-right: 85px;
}
</style>
