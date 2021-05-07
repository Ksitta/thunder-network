import requests
import configparser
from backend.settings import nbi_name, nbi_pwd, nbi_host, nbi_port
from copy import deepcopy

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
    try:
        body = r.json()["success"]
        site_id = body[0]['id']
    except IndexError:
        return IndexError
    return site_id

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
    data['ssidAuth']['macAutoBinding'] = True
    data.update(item)
    headers = base_headers
    headers['X-AUTH-TOKEN'] = get_token()

    r = requests.post(post_ssid_url, headers=headers, json=data, verify=False)
    # # 解析SSID信息
    # print("8.【Post SSID】")
    # print("eeee:", post_ssid_url)
    # print(r.text)
    try:
        body = r.json()["data"]
        SSID_id = body['id']
    except KeyError:
        return KeyError
    # print("【success】：" + str(site_id))
    return SSID_id
    # 返回 SSID 的 id
#

# 限定为删除单个SSID
def delete_ssid(site_id, ssid_id):
    # 配置URL和Headers
    delete_ssid_url = HTTPS + nbi_host + ":" + nbi_port + SSID_URL + site_id + APSSI
    # 发起请求
    data = {
        "ids": [ssid_id]
    }
    headers = base_headers
    headers['X-AUTH-TOKEN'] = get_token()
    r = requests.delete(delete_ssid_url, headers=headers, json=data, verify=False)
    # 解析站点信息
    # print("10.【Delete SSID】")
    # print("【delete_ssid_url】：" + ssid_id)
    # print(r.text)
    try:
        body = r.json()["success"][0]
    except (IndexError, KeyError):
        return KeyError
    return body
