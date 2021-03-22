import requests
import configparser
import os
import json
from backend.settings import nbi_name, nbi_pwd, nbi_host, nbi_port

# cf = configparser.ConfigParser()
# cf.read("/network_config/config.txt")

# 配置北向用户信息及北向地址
# nbi_name = str(cf.get('nce', 'NBI_NAME'))
# nbi_pwd = str(cf.get('nce', 'NBI_PWD'))
# nbi_host = "139.9.213.72"
# nbi_port = "18002"

# 定义接口的URI
POST_TOKEN_URL = "/controller/v2/tokens"
GET_SITES_URL = "/controller/campus/v3/sites?pageIndex=0&pageSize=20"
SITES_URL = "/controller/campus/v3/sites"
DEVICES_URL = "/controller/campus/v3/devices"
SSID_URL = "/controller/campus/v3/networkconfig/site/"
RATE_URL = "/controller/campus/v1/performanceservice/basicperformance/networktraffic"
SITE_TERMINAL_URL = "/controller/campus/v1/performanceservice/basicperformance/station/sites/"
DEVICE_TERMINAL_URL = "/controller/campus/v1/performanceservice/basicperformance/station/device/"


def getToken():
    # 配置URL和Headers
    post_token_url = "https://" + nbi_host + ":" + nbi_port + POST_TOKEN_URL
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    # 发起请求，添加Json格式数据
    r = requests.post(post_token_url, headers=headers, json={"userName": nbi_name, "password": nbi_pwd},
                      verify=False)
    # 解析token_id
    print(r.text)
    token_id = r.json()['data']['token_id']
    print("1.【Get Token Id】")
    print("【post_token_url】：" + post_token_url)
    print("【token_id】：" + token_id)
    return token_id

"""
以下为站点创建、查询和删除的请求函数
"""

# 限定仅创建单个站点，仅限定名字？（反正其他信息在数据库里？
def createSite(name):
    # 配置URL和Headers
    x = getToken()
    post_sites_url = "https://" + nbi_host + ":" + nbi_port + SITES_URL
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'X-AUTH-TOKEN': getToken()}
    # 发起请求
    data = {
        "sites": [{"name": name}]
    }
    r = requests.post(post_sites_url, headers=headers, json=data, verify=False)
    # 解析站点信息
    print("2.【Post Sites】")
    print("【post_sites_url】：" + post_sites_url)
    body = r.json()["success"]
    print("【success】：" + str(body[0]['id']))
    return body[0]['id']

# 限定为id精准查找
def getSite(id):
    # 配置URL和Headers
    get_sites_url = "https://" + nbi_host + ":" + nbi_port + GET_SITES_URL
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'X-AUTH-TOKEN': getToken()}
    # 发起请求
    data = {
        "id": id
    }
    r = requests.get(get_sites_url, headers=headers, json=data, verify=False)
    # 解析站点信息
    print("3.【Get Sites Info】")
    print("【get_sites_url】：" + get_sites_url)
    #total_records = r.json()['totalRecords']
    #print("【total_records】：" + str(total_records))
    #print(r.text)
    #未写返回值

# 限定为删除单个站点
def deleteSite(id):
    # 配置URL和Headers
    delete_sites_url = "https://" + nbi_host + ":" + nbi_port + SITES_URL
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'X-AUTH-TOKEN': getToken()}
    # 发起请求
    data = {
        "ids": [id]
    }
    r = requests.delete(delete_sites_url, headers=headers, json=data, verify=False)
    # 解析站点信息
    print("4.【Delete Sites】")
    print("【delete_sites_url】：" + delete_sites_url)
    #total_records = r.json()['totalRecords']
    #print("【total_records】：" + str(total_records))
    #print(r.text)
    #未写返回值

"""
以下为设备创建、查询和删除的请求函数
"""

# 参数仍有问题
def createDevice(name, siteId):
    # 配置URL和Headers
    post_devices_url = "https://" + nbi_host + ":" + nbi_port + DEVICES_URL
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'X-AUTH-TOKEN': getToken()}
    # 发起请求
    data = {
        "devices" : [
            {
                "esn": "2102351BTJ0000000666",
                "name": name,
                "siteId": siteId,
                "description": "AR",
                "resourceId": "HUAWEI",
                "deviceModel": "AR161EW",
                #"systemIp": "192.168.1.1",
                #"ztpConfirm": True,
                #"role": ["Gateway"]
            }
        ]
    }

    r = requests.post(post_devices_url, headers=headers, json=data, verify=False)
    # 解析站点信息
    print("5.【Post Devices】")
    print("【post_devices_url】：" + post_devices_url)
    #body = r.json()["success"]
    #print("【success】：" + str(body[0]['id']))
    #return body[0]['id']
    # 返回设备id

# 限定为id查找, 不限定类型
def getDevice(siteId):
    # 配置URL和Headers
    get_devices_url = "https://" + nbi_host + ":" + nbi_port + DEVICES_URL
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'X-AUTH-TOKEN': getToken()}
    # 发起请求
    data = {
        "siteid": siteId
    }
    r = requests.get(get_devices_url, headers=headers, json=data, verify=False)
    # 解析站点信息
    print("6.【Get Devices Info】")
    print("【get_devices_url】：" + get_devices_url)
    #total_records = r.json()['totalRecords']
    #print("【total_records】：" + str(total_records))
    #print(r.text)
    #未写返回值

# 限定为删除单个设备
def deleteDevice(deviceId):
    # 配置URL和Headers
    delete_devices_url = "https://" + nbi_host + ":" + nbi_port + DEVICES_URL
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'X-AUTH-TOKEN': getToken()}
    # 发起请求
    data = {
        "deviceIds": [id]
        #"reset": "true"
    }
    r = requests.delete(delete_devices_url, headers=headers, json=data, verify=False)
    # 解析站点信息
    print("7.【Delete Devices】")
    print("【delete_devices_url】：" + delete_devices_url)
    #total_records = r.json()['totalRecords']
    #print("【total_records】：" + str(total_records))
    #print(r.text)
    #未写返回值

"""
以下为SSID创建、查询和删除的请求函数
"""

# 参数仍存疑
def CreateSSID(siteId, name):
    # 配置URL和Headers
    post_ssid_url = "https://" + nbi_host + ":" + nbi_port + SSID_URL + siteId +"/apssi"
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'X-AUTH-TOKEN': getToken()}
    # 发起请求
    data = {
        "name": name,
        "enable": True,
        "connectionMode": "bridge",
        "hidedEnable": False,
        "maxUserNumber": 10,
        "relativeRadios": 3,
        "userSeparation": False,
        "ssidAuth": {
            "mode": "ppsk",
            "pskEncryptType": "wpa2",
            "securityKeyType": "AES",
            "portal": {"mode": "portalDisable"	},
            "macAutoBinding": True
        },
        "ssidPolicy": {}
    }

    r = requests.post(post_ssid_url, headers=headers, json=data, verify=False)
    # 解析站点信息
    print("8.【Post SSID】")
    print("【post_ssid_url】：" + post_ssid_url)
    #body = r.json()["success"]
    #print("【success】：" + str(body[0]['id']))
    #return body[0]['id']
    # 返回 SSID 的 id

# siteId查找
def getSSID(siteId):
    # 配置URL和Headers
    get_ssid_url = "https://" + nbi_host + ":" + nbi_port + SSID_URL + siteId +"/apssi"
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'X-AUTH-TOKEN': getToken()}
    # 发起请求
    r = requests.get(get_ssid_url, headers=headers, verify=False)
    # 解析站点信息
    print("9.【Get SSID Info】")
    print("【get_ssid_url】：" + get_ssid_url)
    #total_records = r.json()['totalRecords']
    #print("【total_records】：" + str(total_records))
    #print(r.text)
    #未写返回值

# 限定为删除单个SSID
def deleteSSID(siteId, SSID_id):
    # 配置URL和Headers
    delete_ssid_url = "https://" + nbi_host + ":" + nbi_port + SSID_URL + siteId +"/apssi"
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'X-AUTH-TOKEN': getToken()}
    # 发起请求
    data = {
        "ids": [SSID_id]
        #"reset": "true"
    }
    r = requests.delete(delete_ssid_url, headers=headers, json=data, verify=False)
    # 解析站点信息
    print("10.【Delete SSID】")
    print("【delete_ssid_url】：" + delete_ssid_url)
    #total_records = r.json()['totalRecords']
    #print("【total_records】：" + str(total_records))
    #print(r.text)
    #未写返回值

"""
以下为查询速率、终端数的请求函数
"""

def getRate(mode, id, timeDimension, beginTime, endTime):
    # 配置URL和Headers
    get_rate_url = "https://" + nbi_host + ":" + nbi_port + RATE_URL
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'X-AUTH-TOKEN': getToken()}
    # 发起请求
    data = {
        "mode": mode,
        "id": id,
        "timeDimension": timeDimension,
        "beginTime": beginTime,
        "endTime": endTime
    }
    r = requests.get(get_rate_url, headers=headers, json=data, verify=False)
    # 解析站点信息
    print("11.【Get Rate Info】")
    print("【get_rate_url】：" + get_rate_url)
    #total_records = r.json()['totalRecords']
    #print("【total_records】：" + str(total_records))
    #print(r.text)
    #未写返回值

# 限定为全部设备的终端数
def getSiteTerminal(siteId, timeDimension, beginTime, endTime):
    # 配置URL和Headers
    get_site_terminal_url = "https://" + nbi_host + ":" + nbi_port + SITE_TERMINAL_URL + siteId
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'X-AUTH-TOKEN': getToken()}
    # 发起请求
    data = {
        "timeDimension": timeDimension,
        "beginTime": beginTime,
        "endTime": endTime,
        "deviceType": "ALL"
    }
    r = requests.get(get_site_terminal_url, headers=headers, json=data, verify=False)
    # 解析站点信息
    print("12.【Get Site Terminal Info】")
    print("【get_site_terminal_url】：" + get_site_terminal_url)
    #total_records = r.json()['totalRecords']
    #print("【total_records】：" + str(total_records))
    #print(r.text)
    #未写返回值

# 限定为全部设备的终端数
def getDeviceTerminal(deviceId, timeDimension, beginTime, endTime):
    # 配置URL和Headers
    get_device_terminal_url = "https://" + nbi_host + ":" + nbi_port + DEVICE_TERMINAL_URL + deviceId
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'X-AUTH-TOKEN': getToken()}
    # 发起请求
    data = {
        "timeDimension": timeDimension,
        "beginTime": beginTime,
        "endTime": endTime
    }
    r = requests.get(get_device_terminal_url, headers=headers, json=data, verify=False)
    # 解析站点信息
    print("13.【Get Device Terminal Info】")
    print("【get_device_terminal_url】：" + get_device_terminal_url)
    #total_records = r.json()['totalRecords']
    #print("【total_records】：" + str(total_records))
    #print(r.text)
    #未写返回值
