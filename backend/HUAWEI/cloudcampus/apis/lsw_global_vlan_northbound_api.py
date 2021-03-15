# coding: utf-8

"""
    交换机全局VLAN配置

    配置交换机全局VLAN 

    OpenAPI spec version: 1.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient
from .gettoken_api import GetTokenApi


class LSWGlobalVlanNorthboundApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        # config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            print('api_client cannot be None.')
            # if not config.api_client:
            #     config.api_client = ApiClient()
            # self.api_client = config.api_client

    def create_lsw_global_vlan_info(self, device_id, body, **kwargs):
        """
        创建交换机的全局VLAN配置
        ## 典型场景 ##    提供配置参数的接口，创建交换机的全局VLAN配置。 ## 接口功能 ##    创建交换机全局VLAN配置。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_lsw_global_vlan_info(device_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_id: 设备ID，格式为uuid格式。 (required)
        :param LswGlobalVlanDto body: 全局VLAN配置。 (required)
        :return: LswGlobalVlanResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_lsw_global_vlan_info_with_http_info(device_id, body, **kwargs)
        else:
            (data) = self.create_lsw_global_vlan_info_with_http_info(device_id, body, **kwargs)
            return data

    def create_lsw_global_vlan_info_with_http_info(self, device_id, body, **kwargs):
        """
        创建交换机的全局VLAN配置
        ## 典型场景 ##    提供配置参数的接口，创建交换机的全局VLAN配置。 ## 接口功能 ##    创建交换机全局VLAN配置。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_lsw_global_vlan_info_with_http_info(device_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_id: 设备ID，格式为uuid格式。 (required)
        :param LswGlobalVlanDto body: 全局VLAN配置。 (required)
        :return: LswGlobalVlanResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_lsw_global_vlan_info" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params) or (params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `create_lsw_global_vlan_info`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_lsw_global_vlan_info`")

        if 'device_id' in params and len(params['device_id']) > 36:
            raise ValueError("Invalid value for parameter `device_id` when calling `create_lsw_global_vlan_info`, length must be less than or equal to `36`")
        if 'device_id' in params and len(params['device_id']) < 36:
            raise ValueError("Invalid value for parameter `device_id` when calling `create_lsw_global_vlan_info`, length must be greater than or equal to `36`")

        collection_formats = {}

        path_params = {}
        if 'device_id' in params:
            path_params['deviceId'] = params['device_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/controller/campus/v1/networkservice/networkconfig/net/lswglobalvlan/devices/{deviceId}/globalvlan', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='LswGlobalVlanResponseDto',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_lsw_global_vlan_info(self, device_id, record_id, **kwargs):
        """
        删除交换机的全局VLAN配置
        ## 典型场景 ##    提供配置参数的接口，删除交换机的全局VLAN配置。 ## 接口功能 ##    删除交换机全局VLAN配置。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_lsw_global_vlan_info(device_id, record_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_id: 设备ID，格式为uuid格式。 (required)
        :param str record_id: VLAN ID，UUID格式。 (required)
        :return: LswGlobalVlanDelRespDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_lsw_global_vlan_info_with_http_info(device_id, record_id, **kwargs)
        else:
            (data) = self.delete_lsw_global_vlan_info_with_http_info(device_id, record_id, **kwargs)
            return data

    def delete_lsw_global_vlan_info_with_http_info(self, device_id, record_id, **kwargs):
        """
        删除交换机的全局VLAN配置
        ## 典型场景 ##    提供配置参数的接口，删除交换机的全局VLAN配置。 ## 接口功能 ##    删除交换机全局VLAN配置。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_lsw_global_vlan_info_with_http_info(device_id, record_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_id: 设备ID，格式为uuid格式。 (required)
        :param str record_id: VLAN ID，UUID格式。 (required)
        :return: LswGlobalVlanDelRespDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_id', 'record_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_lsw_global_vlan_info" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params) or (params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `delete_lsw_global_vlan_info`")
        # verify the required parameter 'record_id' is set
        if ('record_id' not in params) or (params['record_id'] is None):
            raise ValueError("Missing the required parameter `record_id` when calling `delete_lsw_global_vlan_info`")


        collection_formats = {}

        path_params = {}
        if 'device_id' in params:
            path_params['deviceId'] = params['device_id']
        if 'record_id' in params:
            path_params['recordId'] = params['record_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/controller/campus/v1/networkservice/networkconfig/net/lswglobalvlan/devices/{deviceId}/globalvlan/{recordId}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='LswGlobalVlanDelRespDto',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_lsw_global_vlan_infos(self, device_id, **kwargs):
        """
        查询交换机的全局VLAN配置
        ## 典型场景 ##    提供查询配置参数的接口，查询LSW的全局VLAN配置信息。 ## 接口功能 ##    查询全局VLAN配置。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_lsw_global_vlan_infos(device_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_id: 设备ID，格式为uuid格式 (required)
        :return: LswGlobalVlanAllRespDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_lsw_global_vlan_infos_with_http_info(device_id, **kwargs)
        else:
            (data) = self.get_lsw_global_vlan_infos_with_http_info(device_id, **kwargs)
            return data

    def get_lsw_global_vlan_infos_with_http_info(self, device_id, **kwargs):
        """
        查询交换机的全局VLAN配置
        ## 典型场景 ##    提供查询配置参数的接口，查询LSW的全局VLAN配置信息。 ## 接口功能 ##    查询全局VLAN配置。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_lsw_global_vlan_infos_with_http_info(device_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_id: 设备ID，格式为uuid格式 (required)
        :return: LswGlobalVlanAllRespDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_lsw_global_vlan_infos" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params) or (params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `get_lsw_global_vlan_infos`")


        collection_formats = {}

        path_params = {}
        if 'device_id' in params:
            path_params['deviceId'] = params['device_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/controller/campus/v1/networkservice/networkconfig/net/lswglobalvlan/devices/{deviceId}/globalvlan', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='LswGlobalVlanAllRespDto',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_lsw_global_vlan_info(self, device_id, body, **kwargs):
        """
        修改交换机的全局VLAN配置
        ## 典型场景 ##    提供配置参数的接口，修改交换机的全局VLAN配置。 ## 接口功能 ##    修改交换机全局VLAN配置。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_lsw_global_vlan_info(device_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_id: 设备ID，格式为uuid格式。 (required)
        :param LswGlobalVlanUpdateDto body: 交换机的全局VLAN配置。 (required)
        :return: LswGlobalVlanResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_lsw_global_vlan_info_with_http_info(device_id, body, **kwargs)
        else:
            (data) = self.update_lsw_global_vlan_info_with_http_info(device_id, body, **kwargs)
            return data

    def update_lsw_global_vlan_info_with_http_info(self, device_id, body, **kwargs):
        """
        修改交换机的全局VLAN配置
        ## 典型场景 ##    提供配置参数的接口，修改交换机的全局VLAN配置。 ## 接口功能 ##    修改交换机全局VLAN配置。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_lsw_global_vlan_info_with_http_info(device_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_id: 设备ID，格式为uuid格式。 (required)
        :param LswGlobalVlanUpdateDto body: 交换机的全局VLAN配置。 (required)
        :return: LswGlobalVlanResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_lsw_global_vlan_info" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params) or (params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `update_lsw_global_vlan_info`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_lsw_global_vlan_info`")


        collection_formats = {}

        path_params = {}
        if 'device_id' in params:
            path_params['deviceId'] = params['device_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/controller/campus/v1/networkservice/networkconfig/net/lswglobalvlan/devices/{deviceId}/globalvlan', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='LswGlobalVlanResponseDto',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
