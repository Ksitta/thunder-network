import requests

# 配置北向用户信息及北向地址
nbi_name = "campusAc01@north.com"
nbi_pwd = "Uy5FgCjN2@"
host = "139.9.213.72"
port = "18002"

# 定义接口的URI
POST_TOKEN_URL = "/controller/v2/tokens"
GET_SITES_URL = "/controller/campus/v3/sites?pageIndex=0&pageSize=20"
POST_SITES_URL = "/controller/campus/v3/sites"
POST_SITE_SSID_URL = "/controller/campus/v3/networkconfig/site/"

def getToken():
    # 配置URL和Headers
    post_token_url = "https://" + host + ":" + port + POST_TOKEN_URL
    headers_post = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    # 发起请求，添加Json格式数据
    r = requests.post(post_token_url, headers=headers_post, json={"userName": nbi_name, "password": nbi_pwd},
                      verify=False)
    # 解析token_id
    token_id = r.json()['data']['token_id']
    print("1.【Get Token Id】")
    print("【post_token_url】：" + post_token_url)
    print("【token_id】：" + token_id)
    return token_id

def createSite(name):
    # 配置URL和Headers
    post_sites_url = "https://" + host + ":" + port + POST_SITES_URL
    headers_post = {'Content-Type': 'application/json', 'Accept': 'application/json', 'X-AUTH-TOKEN': getToken()}
    # 发起请求
    data = {
        "sites": [
            {
                "name": name
            }
        ]
    }
    r = requests.post(post_sites_url, headers=headers_post, json=data, verify=False)
    # 解析站点信息
    print("2.【Post Sites】")
    print("【post_sites_url】：" + post_sites_url)
    body = r.json()["success"]
    print("【success】：" + str(body[0]['id']))
    return body[0]['id']

#待完成。。。
def CreateSiteSSID(site_id, name):
    # 配置URL和Headers
    post_site_ssid_url = "https://" + host + ":" + port + POST_SITE_SSID_URL + site_id +"/apssi"
    headers_post = {'Content-Type': 'application/json', 'Accept': 'application/json', 'X-AUTH-TOKEN': getToken()}
    # 发起请求
    data = {
        "name" : name,
        "enable" : True,
        "connectionMode" : "bridge",
        "hidedEnable" : False,
        "maxUserNumber" : 10,
        "relativeRadios" : 3,
        "userSeparation" : False,
        "ssidAuth" : {
            "mode" : "ppsk",
            "pskEncryptType" : "wpa2",
            "securityKeyType" : "AES",
            "portal" : { "mode" : "portalDisable"	},
            "macAutoBinding" : True
        },
        "ssidPolicy" : {}
    }

    r = requests.post(post_site_ssid_url, headers=headers_post, json=data, verify=False)
    # 解析站点信息
    print("2.【Post Sites】")
    print("【post_site_ssid_url】：" + post_site_ssid_url)
    body = r.json()["success"]
    print("【success】：" + str(body[0]['id']))
    return body[0]['id']

'''
# 定义接口的URI
POST_TOKEN_URL = "/controller/v2/tokens"  
GET_SITES_URL = "/controller/campus/v3/sites?pageIndex=0&pageSize=20"  
# 配置URL和Headers  
post_token_url = "https://" + host + ":" + port + POST_TOKEN_URL  
headers_post = {'Content-Type': 'application/json', 'Accept': 'application/json'}  
# 发起请求，添加Json格式数据  
r = requests.post(post_token_url, headers=headers_post, json={"userName": nbi_name, "password": nbi_pwd}, verify=False)  
# 解析token_id  
token_id = r.json()['data']['token_id']  
print("1.【Get Token Id】")  
print("【post_token_url】："+post_token_url)  
print("【token_id】："+token_id)  
# 配置URL和Headers  
get_sites_url = "https://" + host + ":" + port + GET_SITES_URL  
headers_get = {'Content-Type': 'application/json', 'Accept': 'application/json', 'X-AUTH-TOKEN':token_id}  
# 发起请求  
r = requests.get(get_sites_url, headers=headers_get, verify=False)
# 解析站点信息  
print("2.【Get Sites Info】")
print("【get_sites_url】："+get_sites_url)
total_records = r.json()['totalRecords']
print("【total_records】："+str(total_records))
print(r.text)
'''