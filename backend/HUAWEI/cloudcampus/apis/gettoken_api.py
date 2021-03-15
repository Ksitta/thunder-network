from datetime import datetime

from six import iteritems

from ..api_client import ApiClient
from ..configuration import Configuration


class GetTokenApi(object):
    tokenStr = None
    tokenTime = None
    sentTime = None

    def __init__(self, api_client=None):
        # config = Configuration()
        if api_client:
            self.api_client = api_client
        # else:
        #     if not config.api_client:
        #         config.api_client = ApiClient()
        #     self.api_client = config.api_client

    def getToken(self, **kwargs):
        """
        Create token
        Description:Get Token Id.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param body: Get token id. (required)
        :return: TokenDtoWrapper
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = False
        # config = Configuration(self.api_client)
        rest_info = {}
        rest_info['userName'] = self.api_client.config.username
        rest_info['password'] = self.api_client.config.password
        # auth_data = json.dumps(rest_info)

        response = {}

        if kwargs.get('callback'):
            response = self.getToken_with_http_info(rest_info, **kwargs)
        else:
            response = self.getToken_with_http_info(rest_info, **kwargs)

        return response

    def getToken_with_http_info(self, body, **kwargs):
        """
        Get token id.
        Description:Get token id.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param body: Create network entity. (required)
        :return: TokenDtoWrapper
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
                        " to method create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create`")

        collection_formats = {}

        resource_path = "/controller/v2/tokens"
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client. \
            select_header_accept(['application/json', 'application/xml'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client. \
            select_header_content_type(['application/json', 'application/xml'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='TokenDtoWrapper',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    # def getTokenData(self):
    #     global tokenData
    #     if tokenData:
    #         return tokenData
    #     else:
    #         tokenData = self.getToken().data
    #         return tokenData

    # @classmethod
    def getTokenId(cls):
        # global tokenStr
        # global tokenTime
        tokenApi = GetTokenApi()
        if cls.tokenStr != None and tokenApi.isExpired():
            cls.tokenStr = None
        if cls.tokenStr != None:
            return cls.tokenStr
        else:
            response = tokenApi.getToken()
            responseToken = response[0].data
            cls.tokenStr = responseToken.token_id
            cls.tokenTime = responseToken.expiredDate
            cls.sentTime = response[2]._container

            # header1 = response[2]._container
            # header2 = header1['Data']
            # header3 = header2[2]
            # header = header1.data

            return cls.tokenStr

    def isExpired(self):
        if self.tokenTime == None or "" == self.tokenTime:
            return False

        header2 = self.sentTime['date'][1]
        # header3 = header2.split(",", 2)[1]

        # header3 = 'Sat, 20 May 2017 09:05:10 GMT'

        index = header2.rindex(' ')
        current_str_on_server = header2[:index]
        timezone = header2[index + 1:]

        expired_str_on_server = '2017-05-20T10:45:10.353+00:00'
        expired_str_on_server = expired_str_on_server.replace(":", "")

        current_time_on_server = datetime.strptime(current_str_on_server, '%a, %d %b %Y %H:%M:%S')

        # current_time_on_server = timezone(timezone).localize(current_time_on_server)

        expired_time_on_server = datetime.strptime(self.tokenTime, '%Y-%m-%d %H:%M:%S')

        time = expired_time_on_server - current_time_on_server

        expired_time = datetime.now() + time

        return datetime.now() > expired_time

    @classmethod
    def getToken_id(response, getTokenResponse):
        responseToken = getTokenResponse[0].data
        token_id = responseToken.token_id
        # expiredDate = responseToken.expiredDate
        return token_id
