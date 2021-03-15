# coding: utf-8

"""
    室内地图信息查询

    室内地图第三方北向接口。 · 查询站点中所有楼栋基本信息 · 查询楼栋中所有楼层基本信息 · 查询楼栋中所有楼层详细信息 · 查询楼栋中楼层和设备布放信息 · 查询楼栋中楼层已布放设备详细信息 · 查询楼层已布放设备位置信息 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class QueryBuildingsResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'errcode': 'str',
        'errmsg': 'str',
        'data': 'list[BuildingDto]'
    }

    attribute_map = {
        'errcode': 'errcode',
        'errmsg': 'errmsg',
        'data': 'data'
    }

    def __init__(self, errcode=None, errmsg=None, data=None):
        """
        QueryBuildingsResponse - a model defined in Swagger
        """

        self._errcode = None
        self._errmsg = None
        self._data = None

        if errcode is not None:
          self.errcode = errcode
        if errmsg is not None:
          self.errmsg = errmsg
        if data is not None:
          self.data = data

    @property
    def errcode(self):
        """
        Gets the errcode of this QueryBuildingsResponse.
        错误码。

        :return: The errcode of this QueryBuildingsResponse.
        :rtype: str
        """
        return self._errcode

    @errcode.setter
    def errcode(self, errcode):
        """
        Sets the errcode of this QueryBuildingsResponse.
        错误码。

        :param errcode: The errcode of this QueryBuildingsResponse.
        :type: str
        """

        self._errcode = errcode

    @property
    def errmsg(self):
        """
        Gets the errmsg of this QueryBuildingsResponse.
        错误信息。

        :return: The errmsg of this QueryBuildingsResponse.
        :rtype: str
        """
        return self._errmsg

    @errmsg.setter
    def errmsg(self, errmsg):
        """
        Sets the errmsg of this QueryBuildingsResponse.
        错误信息。

        :param errmsg: The errmsg of this QueryBuildingsResponse.
        :type: str
        """

        self._errmsg = errmsg

    @property
    def data(self):
        """
        Gets the data of this QueryBuildingsResponse.
        楼栋列表。

        :return: The data of this QueryBuildingsResponse.
        :rtype: list[BuildingDto]
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this QueryBuildingsResponse.
        楼栋列表。

        :param data: The data of this QueryBuildingsResponse.
        :type: list[BuildingDto]
        """

        self._data = data

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, QueryBuildingsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
