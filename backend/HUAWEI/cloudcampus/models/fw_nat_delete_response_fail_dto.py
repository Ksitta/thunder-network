# coding: utf-8

"""
    防火墙设备NAT配置

    防火墙设备NAT配置第三方接口。

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class FwNatDeleteResponseFailDto(object):
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
        'errmsg': 'str'
    }

    attribute_map = {
        'errcode': 'errcode',
        'errmsg': 'errmsg'
    }

    def __init__(self, errcode=None, errmsg=None):
        """
        FwNatDeleteResponseFailDto - a model defined in Swagger
        """

        self._errcode = None
        self._errmsg = None

        if errcode is not None:
          self.errcode = errcode
        if errmsg is not None:
          self.errmsg = errmsg

    @property
    def errcode(self):
        """
        Gets the errcode of this FwNatDeleteResponseFailDto.
        错误码。

        :return: The errcode of this FwNatDeleteResponseFailDto.
        :rtype: str
        """
        return self._errcode

    @errcode.setter
    def errcode(self, errcode):
        """
        Sets the errcode of this FwNatDeleteResponseFailDto.
        错误码。

        :param errcode: The errcode of this FwNatDeleteResponseFailDto.
        :type: str
        """
        if errcode is not None and len(errcode) > 64:
            raise ValueError("Invalid value for `errcode`, length must be less than or equal to `64`")
        if errcode is not None and len(errcode) < 0:
            raise ValueError("Invalid value for `errcode`, length must be greater than or equal to `0`")

        self._errcode = errcode

    @property
    def errmsg(self):
        """
        Gets the errmsg of this FwNatDeleteResponseFailDto.
        错误信息。

        :return: The errmsg of this FwNatDeleteResponseFailDto.
        :rtype: str
        """
        return self._errmsg

    @errmsg.setter
    def errmsg(self, errmsg):
        """
        Sets the errmsg of this FwNatDeleteResponseFailDto.
        错误信息。

        :param errmsg: The errmsg of this FwNatDeleteResponseFailDto.
        :type: str
        """
        if errmsg is not None and len(errmsg) > 256:
            raise ValueError("Invalid value for `errmsg`, length must be less than or equal to `256`")
        if errmsg is not None and len(errmsg) < 0:
            raise ValueError("Invalid value for `errmsg`, length must be greater than or equal to `0`")

        self._errmsg = errmsg

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
        if not isinstance(other, FwNatDeleteResponseFailDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
