import sys
import json
import time

#from ..src.cloudcampus import cloudcampus

from .cloudcampus.api_client import ApiClient
from .cloudcampus.configuration import Configuration

from .cloudcampus.apis.acl_template_nb_north_bound_api import AclTemplateNBNorthBoundApi
from .cloudcampus.apis.site_manager_api import SiteManagerApi
from .cloudcampus.apis.station_open_api_api import StationOpenApiApi
from .cloudcampus.apis.performance_open_api_api import PerformanceOpenApiApi


from .cloudcampus.models import AclDtoDetail,CreateSiteDtoData,CreateSiteDto,StationDataResp,DeviceTrafficStatisticResp

#from .cloudcampus.rest import ApiException

# init api
tenant_name = 'tenant@north.com'
tenant_pwd = 'password@'
host = '139.9.213.72'
port = '18002'
config = Configuration(host, port, tenant_name, tenant_pwd)
api_client = ApiClient(config)

def createSite(name):
    # 创建站点
    site_api = SiteManagerApi(api_client)
    site_data = CreateSiteDtoData(name, "description1")
    site_data_dto = CreateSiteDto([site_data])
    model = site_api.create_sites(site_data_dto)
    print('CREATE SITE : SUCCESS')
    print('response body :       ' + str(model))
    return model["data"][0]

"""
def main():
    # init api
    tenant_name = 'tenant@north.com'
    tenant_pwd = 'password@'
    host = '139.9.213.72'
    port = '18002'    
    config = Configuration(host, port, tenant_name, tenant_pwd)
    api_client = ApiClient(config)
   
    # 创建ACL
    acl_api = AclTemplateNBNorthBoundApi(api_client)
    name = "ACL6001"
    acl_number = "6001"
    description = "ACL"
    acl_type = "User"
    rule_list = [{'ip': '8.8.8.8/32', 'description': 'IP'}]

    acl_dto = AclDtoDetail(name, acl_number, description, acl_type, rule_list)

    try:
        print('ACL-BODY :       ' + acl_dto.to_str())
        model = acl_api.add_acl_template(acl_dto)
    except ApiException as e:
        print('CREATE ACL : SUCCESS')
        print('EXCEPT :       ' + str(e))
    else:
        print('CREATE ACL : SUCCESS')
        print('response body :       ' + str(model))

    # 创建站点
    site_api = SiteManagerApi(api_client)
    site_data = CreateSiteDtoData("Site02", "Tset Site", ['AP'])
    site_data_dto = CreateSiteDto([site_data])
    model = site_api.create_sites(site_data_dto)
    print('CREATE SITE : SUCCESS')
    print('response body :       ' + str(model))

    # 查询站点
    site_api = SiteManagerApi(api_client)
    model = site_api.query_sites(page_index=1, page_size=20, name = "Site01")
    print('QUERY SITE : SUCCESS')
    print('response body :       ' + str(model))

    site_id = model.data[0].id
    print('siteId:  ' + site_id)

    # 查询站点维度下终端用户信息
    station_api = StationOpenApiApi(api_client)
    try:

        model =  station_api.query_site_station_info(site_id, 1, 20)
    except ValueError as e :
        print('QUERY STATION INFO : SUCCESS')
        print('NO STATION INFO')
        print('EXCEPT :       ' + str(e))
    else:
        print('QUERY STATION INFO : SUCCESS')
        print('response body :       ' + str(model))
    finally:
        print('QUERY STATION INFO END')



    # 查询设备网络速率历史数据
    traffic_api = PerformanceOpenApiApi(api_client)
    try:
        t = int (time.mktime(time.localtime(time.time())))                
        model = traffic_api.query_network_traffic("site",site_id,"day", t-3600, t)
    except ValueError as e :
        print('QUERY DEVICE TRAFFIC : SUCCESS')
        print('NO DEVICE TRAFFIC')
        print('EXCEPT :       ' + str(e))
    else:
        print('QUERY DEVICE TRAFFIC : SUCCESS')
        print('response body :       ' + str(model))
    finally:
        print('QUERY DEVICE TRAFFIC END')

if __name__ == "__main__":
    sys.exit(main())
"""