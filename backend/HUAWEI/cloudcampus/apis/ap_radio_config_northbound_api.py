# coding: utf-8

"""
    AP设备射频配置

    AP设备射频配置第三方接口说明。 

    OpenAPI spec version: 1.1.1
    
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


class ApRadioConfigNorthboundApi(object):
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

    def get_device_radio_config(self, device_id, **kwargs):
        """
        查询AP设备射频配置信息
        ## 典型场景 ##  提供查询AP设备射频配置信息接口。<br> ## 接口功能 ##  查询AP设备射频配置信息。<br> ## 接口约束 ##  该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。<br>        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_device_radio_config(device_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_id: 设备ID，UUID格式。 (required)
        :return: ApDeviceRadioResponsesDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_device_radio_config_with_http_info(device_id, **kwargs)
        else:
            (data) = self.get_device_radio_config_with_http_info(device_id, **kwargs)
            return data

    def get_device_radio_config_with_http_info(self, device_id, **kwargs):
        """
        查询AP设备射频配置信息
        ## 典型场景 ##  提供查询AP设备射频配置信息接口。<br> ## 接口功能 ##  查询AP设备射频配置信息。<br> ## 接口约束 ##  该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。<br>        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_device_radio_config_with_http_info(device_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_id: 设备ID，UUID格式。 (required)
        :return: ApDeviceRadioResponsesDto
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
                    " to method get_device_radio_config" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params) or (params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `get_device_radio_config`")


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

        return self.api_client.call_api('/controller/campus/v3/networkconfig/device/{deviceId}/apradio/radios', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ApDeviceRadioResponsesDto',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_device_radio_config(self, device_id, ap_device_radio_api_dto, **kwargs):
        """
        修改AP设备射频配置信息
        ## 典型场景 ##  提供修改AP设备射频配置信息接口。<br>  ## 接口功能 ##  修改AP设备射频配置信息。<br>  ## 接口约束 ## 该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。<br> 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_device_radio_config(device_id, ap_device_radio_api_dto, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_id: 设备ID，UUID格式。 (required)
        :param ApDeviceRadioApiDto ap_device_radio_api_dto: 修改AP设备射频配置入参。 (required)
        :return: ApDeviceRadioResponsesDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_device_radio_config_with_http_info(device_id, ap_device_radio_api_dto, **kwargs)
        else:
            (data) = self.update_device_radio_config_with_http_info(device_id, ap_device_radio_api_dto, **kwargs)
            return data

    def update_device_radio_config_with_http_info(self, device_id, ap_device_radio_api_dto, **kwargs):
        """
        修改AP设备射频配置信息
        ## 典型场景 ##  提供修改AP设备射频配置信息接口。<br>  ## 接口功能 ##  修改AP设备射频配置信息。<br>  ## 接口约束 ## 该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。<br> 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_device_radio_config_with_http_info(device_id, ap_device_radio_api_dto, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_id: 设备ID，UUID格式。 (required)
        :param ApDeviceRadioApiDto ap_device_radio_api_dto: 修改AP设备射频配置入参。 (required)
        :return: ApDeviceRadioResponsesDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_id', 'ap_device_radio_api_dto']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_device_radio_config" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params) or (params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `update_device_radio_config`")
        # verify the required parameter 'ap_device_radio_api_dto' is set
        if ('ap_device_radio_api_dto' not in params) or (params['ap_device_radio_api_dto'] is None):
            raise ValueError("Missing the required parameter `ap_device_radio_api_dto` when calling `update_device_radio_config`")


        collection_formats = {}

        path_params = {}
        if 'device_id' in params:
            path_params['deviceId'] = params['device_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'ap_device_radio_api_dto' in params:
            body_params = params['ap_device_radio_api_dto']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/controller/campus/v3/networkconfig/device/{deviceId}/apradio/radios', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ApDeviceRadioResponsesDto',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
