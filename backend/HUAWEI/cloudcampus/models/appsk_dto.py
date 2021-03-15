# coding: utf-8

"""
    站点内AP增值服务配置

    站点内AP增值服务配置北向接口，主要特性： * 查询站点内AP增值服务配置。 * 修改站点内AP增值服务配置。 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AppskDto(object):
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
        'enable_psk': 'bool',
        'last_update_time': 'str'
    }

    attribute_map = {
        'enable_psk': 'enablePsk',
        'last_update_time': 'lastUpdateTime'
    }

    def __init__(self, enable_psk=None, last_update_time=None):
        """
        AppskDto - a model defined in Swagger
        """

        self._enable_psk = None
        self._last_update_time = None

        if enable_psk is not None:
          self.enable_psk = enable_psk
        if last_update_time is not None:
          self.last_update_time = last_update_time

    @property
    def enable_psk(self):
        """
        Gets the enable_psk of this AppskDto.
        PSK使能。

        :return: The enable_psk of this AppskDto.
        :rtype: bool
        """
        return self._enable_psk

    @enable_psk.setter
    def enable_psk(self, enable_psk):
        """
        Sets the enable_psk of this AppskDto.
        PSK使能。

        :param enable_psk: The enable_psk of this AppskDto.
        :type: bool
        """

        self._enable_psk = enable_psk

    @property
    def last_update_time(self):
        """
        Gets the last_update_time of this AppskDto.
        最后一次更新时间。时间格式：UTC。

        :return: The last_update_time of this AppskDto.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        """
        Sets the last_update_time of this AppskDto.
        最后一次更新时间。时间格式：UTC。

        :param last_update_time: The last_update_time of this AppskDto.
        :type: str
        """

        self._last_update_time = last_update_time

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
        if not isinstance(other, AppskDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
