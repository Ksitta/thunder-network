# coding: utf-8

"""
    RADIUS模板管理

    RADIUS模板配置第三方北向接口说明。 

    OpenAPI spec version: 1.0.1
    
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


class RadiusTemplateNorthboundApi(object):
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

    def create_radius_template(self, body, **kwargs):
        """
        创建RADIUS模板
        ## 典型场景 ##    创建RADIUS模板。 ## 接口功能 ##    RADIUS模板创建接口。 ## 接口约束 ##    该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_radius_template(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateRadiusTempDto body: RADIUS服务器模板信息。 (required)
        :return: CreateRadiusTempResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_radius_template_with_http_info(body, **kwargs)
        else:
            (data) = self.create_radius_template_with_http_info(body, **kwargs)
            return data

    def create_radius_template_with_http_info(self, body, **kwargs):
        """
        创建RADIUS模板
        ## 典型场景 ##    创建RADIUS模板。 ## 接口功能 ##    RADIUS模板创建接口。 ## 接口约束 ##    该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_radius_template_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateRadiusTempDto body: RADIUS服务器模板信息。 (required)
        :return: CreateRadiusTempResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_radius_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_radius_template`")


        collection_formats = {}

        path_params = {}

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

        return self.api_client.call_api('/controller/campus/v1/networkservice/networkconfig/profile/radius', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CreateRadiusTempResponseDto',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_radius_template(self, body, **kwargs):
        """
        删除RADIUS模板
        ## 典型场景 ##    删除RADIUS模板信息。 ## 接口功能 ##    RADIUS模板删除接口。 ## 接口约束 ##    该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_radius_template(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param DeleteRadiusTempDto body: RADIUS服务器模板ID列表。 (required)
        :return: DeleteRadiusTempResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_radius_template_with_http_info(body, **kwargs)
        else:
            (data) = self.delete_radius_template_with_http_info(body, **kwargs)
            return data

    def delete_radius_template_with_http_info(self, body, **kwargs):
        """
        删除RADIUS模板
        ## 典型场景 ##    删除RADIUS模板信息。 ## 接口功能 ##    RADIUS模板删除接口。 ## 接口约束 ##    该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_radius_template_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param DeleteRadiusTempDto body: RADIUS服务器模板ID列表。 (required)
        :return: DeleteRadiusTempResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_radius_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `delete_radius_template`")


        collection_formats = {}

        path_params = {}

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

        return self.api_client.call_api('/controller/campus/v1/networkservice/networkconfig/profile/radius/batch-delete', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DeleteRadiusTempResponseDto',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_radius_template(self, **kwargs):
        """
        查询RADIUS模板
        ## 典型场景 ##    查询RADIUS模板列表信息。 ## 接口功能 ##    RADIUS模板查询接口。 ## 接口约束 ##    该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_radius_template(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_size: 每页大小。
        :param int page_index: 页码。
        :return: GetRadiusTempResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_radius_template_with_http_info(**kwargs)
        else:
            (data) = self.get_radius_template_with_http_info(**kwargs)
            return data

    def get_radius_template_with_http_info(self, **kwargs):
        """
        查询RADIUS模板
        ## 典型场景 ##    查询RADIUS模板列表信息。 ## 接口功能 ##    RADIUS模板查询接口。 ## 接口约束 ##    该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_radius_template_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_size: 每页大小。
        :param int page_index: 页码。
        :return: GetRadiusTempResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'page_index']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_radius_template" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))
        if 'page_index' in params:
            query_params.append(('pageIndex', params['page_index']))

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

        return self.api_client.call_api('/controller/campus/v1/networkservice/networkconfig/profile/radius', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='GetRadiusTempResponseDto',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_radius_template(self, id, body, **kwargs):
        """
        修改RADIUS模板
        ## 典型场景 ##    修改RADIUS模板。 ## 接口功能 ##    RADIUS模板修改接口。 ## 接口约束 ##    该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_radius_template(id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: RADIUS服务器模板ID，UUID格式。 (required)
        :param UpdateRadiusTempDto body: RADIUS服务器模板信息。 (required)
        :return: UpdateRadiusTempResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_radius_template_with_http_info(id, body, **kwargs)
        else:
            (data) = self.update_radius_template_with_http_info(id, body, **kwargs)
            return data

    def update_radius_template_with_http_info(self, id, body, **kwargs):
        """
        修改RADIUS模板
        ## 典型场景 ##    修改RADIUS模板。 ## 接口功能 ##    RADIUS模板修改接口。 ## 接口约束 ##    该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_radius_template_with_http_info(id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: RADIUS服务器模板ID，UUID格式。 (required)
        :param UpdateRadiusTempDto body: RADIUS服务器模板信息。 (required)
        :return: UpdateRadiusTempResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_radius_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_radius_template`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_radius_template`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

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

        return self.api_client.call_api('/controller/campus/v1/networkservice/networkconfig/profile/radius/{id}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='UpdateRadiusTempResponseDto',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
