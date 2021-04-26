import requests
import configparser
import os
import json
from backend.settings import nbi_name, nbi_pwd, nbi_host, nbi_port
from copy import deepcopy
import json

HTTPS = "https://"
APPJSON = "application/json"
APSSI = "/apssid"

# 定义接口的URI
POST_TOKEN_URL = "/controller/v2/tokens"
GET_SITES_URL = "/controller/campus/v3/sites?pageIndex=0&pageSize=20"
SITES_URL = "/controller/campus/v3/sites"
DEVICES_URL = "/controller/campus/v3/devices"
SSID_URL = "/controller/campus/v3/networkconfig/site/"
RATE_URL = "/controller/campus/v1/performanceservice/basicperformance/networktraffic"
SITE_TERMINAL_URL = "/controller/campus/v1/performanceservice/basicperformance/station/sites/"
DEVICE_TERMINAL_URL = "/controller/campus/v1/performanceservice/basicperformance/station/device/"

base_headers = {'Content-Type': APPJSON, 'Accept': APPJSON}

def get_token():
    # 配置URL和Headers
    post_token_url = HTTPS + nbi_host + ":" + nbi_port + POST_TOKEN_URL
    token_headers = base_headers
    # 发起请求，添加Json格式数据
    r = requests.post(post_token_url, headers=token_headers, json={"userName": nbi_name, "password": nbi_pwd},
                      verify=False)
    # 解析token_id
    token_id = r.json()['data']['token_id']
    return token_id


"""
以下为站点创建、查询和删除的请求函数
"""

# 限定仅创建单个站点，仅限定名字？（反正其他信息在数据库里？
def create_site(name):
    # 配置URL和Headers
    post_sites_url = HTTPS + nbi_host + ":" + nbi_port + SITES_URL
    # 发起请求
    data = {
        "sites": [{"name": name}]
    }
    headers = base_headers
    headers['X-AUTH-TOKEN'] = get_token()
    r = requests.post(post_sites_url, headers=headers, json=data, verify=False)
    # 解析站点信息
    # print("【Post Sites】")
    try:
        body = r.json()["success"]
        site_id = body[0]['id']
    except IndexError:
        return IndexError
    # print("【success】：" + str(site_id))
    return site_id

# 限定为id精准查找
# def get_site(id):
#     # 配置URL和Headers
#     get_sites_url = HTTPS + nbi_host + ":" + nbi_port + GET_SITES_URL
#     # 发起请求
#     data = {
#         "id": id
#     }
#     headers = base_headers
#     headers['X-AUTH-TOKEN'] = get_token()
#     r = requests.get(get_sites_url, headers=headers, json=data, verify=False)
#     # 解析站点信息
#     print("3.【Get Sites Info】")
#     print("【get_sites_url】：" + get_sites_url)
#     print(r.text)
#     # 未写返回值

# 限定为删除单个站点
# def delete_site(id):
#     # 配置URL和Headers
#     delete_sites_url = HTTPS + nbi_host + ":" + nbi_port + SITES_URL
#     # 发起请求
#     data = {
#         "ids": [id]
#     }
#     headers = base_headers
#     headers['X-AUTH-TOKEN'] = get_token()
#     r = requests.delete(delete_sites_url, headers=headers, json=data, verify=False)
#     # 解析站点信息
#     print("4.【Delete Sites】")
#     print("【delete_sites_url】：" + delete_sites_url)
#     try:
#         body = r.json()["success"]
#     except KeyError:
#         print("EEEEEEEEEEEERROR!")
#         print(r.text)
#         return False
#     print("【success】：" + str(body))
#     return True
#     #未写返回值

"""
以下为设备创建、查询和删除的请求函数
"""

# 参数仍有问题
# def create_device(name, site_id):
#     # 配置URL和Headers
#     post_devices_url = HTTPS + nbi_host + ":" + nbi_port + DEVICES_URL
#     # 发起请求
#     data = {
#         "devices" : [
#             {
#                 "esn": "2102351BTJ0000000666",
#                 "name": name,
#                 "siteId": site_id,
#                 "description": "AR",
#                 "resourceId": "HUAWEI",
#                 "deviceModel": "AR161EW",
#                 #"systemIp": "192.168.1.1",
#                 #"ztpConfirm": True,
#                 #"role": ["Gateway"]
#             }
#         ]
#     }
#     headers = base_headers
#     headers['X-AUTH-TOKEN'] = get_token()
#     r = requests.post(post_devices_url, headers=headers, json=data, verify=False)
#     # 解析站点信息
#     print("5.【Post Devices】")
#     print("【post_devices_url】：" + post_devices_url)
#     print(r.text)
#     # 返回设备id
#
# # 限定为id查找, 不限定类型
# def get_device(site_id):
#     # 配置URL和Headers
#     get_devices_url = HTTPS + nbi_host + ":" + nbi_port + DEVICES_URL
#     # 发起请求
#     data = {
#         "siteid": site_id
#     }
#     headers = base_headers
#     headers['X-AUTH-TOKEN'] = get_token()
#     r = requests.get(get_devices_url, headers=headers, json=data, verify=False)
#     # 解析站点信息
#     print("6.【Get Devices Info】")
#     print("【get_devices_url】：" + get_devices_url)
#     print(r.text)
#     # 未写返回值
#
# # 限定为删除单个设备
# def delete_device(device_id):
#     # 配置URL和Headers
#     delete_devices_url = HTTPS + nbi_host + ":" + nbi_port + DEVICES_URL
#     # 发起请求
#     data = {
#         "deviceIds": [device_id]
#         #"reset": "true"
#     }
#     headers = base_headers
#     headers['X-AUTH-TOKEN'] = get_token()
#     r = requests.delete(delete_devices_url, headers=headers, json=data, verify=False)
#     # 解析站点信息
#     print("7.【Delete Devices】")
#     print("【delete_devices_url】：" + delete_devices_url)
#     print(r.text)
#     # 未写返回值

"""
以下为SSID创建、查询和删除的请求函数
"""

# # 参数仍存疑
def create_ssid(site_id, ssid_data):
    # 配置URL和Headers
    post_ssid_url = HTTPS + nbi_host + ":" + nbi_port + SSID_URL + site_id + APSSI
    # 发起请求
    data = deepcopy(ssid_data)
    item = {'connectionMode': "bridge",
            'hidedEnable': False,
            'ssidPolicy': {}
            }
    data['ssidAuth']['portal'] = {'mode': "portalDisable"}
    data.update(item)
    # data = {
    #     "name": data['name'],
    #     "enable": data['enable'],
    #     "connectionMode": "bridge",
    #     "hidedEnable": False,
    #     "maxUserNumber": data['maxUserNumber'],
    #     "relativeRadios": data['relativeRadios'],
    #     "userSeparation": data['userSeparation'],
    #     "ssidAuth": {
    #         "mode": "ppsk",
    #         "pskEncryptType": "wpa2",
    #         "securityKeyType": "AES",
    #         "portal": {"mode": "portalDisable"	},
    #         "macAutoBinding": True
    #     },
    #     "ssidPolicy": {}
    # }
    headers = base_headers
    headers['X-AUTH-TOKEN'] = get_token()
    print("hhhhhh:", data)
    print("json: ", json.dumps(data))
    r = requests.post(post_ssid_url, headers=headers, json=json.dumps(data), verify=False)
    # 解析站点信息
    print("8.【Post SSID】")
    print(r.text)
    try:
        body = r.json()["data"]
        SSID_id = body['id']
    except IndexError:
        return IndexError
    # print("【success】：" + str(site_id))
    return SSID_id
    # 返回 SSID 的 id
#
# # siteId查找
# def get_ssid(site_id):
#     # 配置URL和Headers
#     get_ssid_url = HTTPS + nbi_host + ":" + nbi_port + SSID_URL + site_id + APSSI
#     # 发起请求
#     headers = base_headers
#     headers['X-AUTH-TOKEN'] = get_token()
#     r = requests.get(get_ssid_url, headers=headers, verify=False)
#     # 解析站点信息
#     print("9.【Get SSID Info】")
#     print("【get_ssid_url】：" + get_ssid_url)
#     print(r.text)
#     # 未写返回值
#
# # 限定为删除单个SSID
# def delete_ssid(site_id, ssid_id):
#     # 配置URL和Headers
#     delete_ssid_url = HTTPS + nbi_host + ":" + nbi_port + SSID_URL + site_id + APSSI
#     # 发起请求
#     data = {
#         "ids": [ssid_id]
#         #"reset": "true"
#     }
#     headers = base_headers
#     headers['X-AUTH-TOKEN'] = get_token()
#     r = requests.delete(delete_ssid_url, headers=headers, json=data, verify=False)
#     # 解析站点信息
#     print("10.【Delete SSID】")
#     print("【delete_ssid_url】：" + delete_ssid_url)
#     print(r.text)
    # 未写返回值

"""
以下为查询速率、终端数的请求函数
"""
#
# def get_rate(mode, id, time_dimension, begin_time, end_time):
#     # 配置URL和Headers
#     get_rate_url = HTTPS + nbi_host + ":" + nbi_port + RATE_URL
#     # 发起请求
#     data = {
#         "mode": mode,
#         "id": id,
#         "timeDimension": time_dimension,
#         "beginTime": begin_time,
#         "endTime": end_time
#     }
#     r = requests.get(get_rate_url, headers=headers, json=data, verify=False)
#     # 解析站点信息
#     print("11.【Get Rate Info】")
#     print("【get_rate_url】：" + get_rate_url)
#     print(r.text)
#     # 未写返回值
#
# # 限定为全部设备的终端数
# def get_site_terminal(site_id, time_dimension, begin_time, end_time):
#     # 配置URL和Headers
#     get_site_terminal_url = HTTPS + nbi_host + ":" + nbi_port + SITE_TERMINAL_URL + site_id
#     # 发起请求
#     data = {
#         "timeDimension": time_dimension,
#         "beginTime": begin_time,
#         "endTime": end_time,
#         "deviceType": "ALL"
#     }
#     r = requests.get(get_site_terminal_url, headers=headers, json=data, verify=False)
#     # 解析站点信息
#     print("12.【Get Site Terminal Info】")
#     print("【get_site_terminal_url】：" + get_site_terminal_url)
#     print(r.text)
#     # 未写返回值
#
# # 限定为全部设备的终端数
# def get_device_terminal(device_id, time_dimension, begin_time, end_time):
#     # 配置URL和Headers
#     get_device_terminal_url = HTTPS + nbi_host + ":" + nbi_port + DEVICE_TERMINAL_URL + device_id
#     # 发起请求
#     data = {
#         "timeDimension": time_dimension,
#         "beginTime": begin_time,
#         "endTime": end_time,
#     }
#     r = requests.get(get_device_terminal_url, headers=headers, json=data, verify=False)
#     # 解析站点信息
#     print("13.【Get Device Terminal Info】")
#     print("【get_device_terminal_url】：" + get_device_terminal_url)
#     print(r.text)
#     # 未写返回值