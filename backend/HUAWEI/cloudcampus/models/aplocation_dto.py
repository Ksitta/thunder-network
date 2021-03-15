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


class AplocationDto(object):
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
        'ap_location_enable': 'bool',
        'ap_location': 'str'
    }

    attribute_map = {
        'ap_location_enable': 'apLocationEnable',
        'ap_location': 'apLocation'
    }

    def __init__(self, ap_location_enable=None, ap_location=None):
        """
        AplocationDto - a model defined in Swagger
        """

        self._ap_location_enable = None
        self._ap_location = None

        if ap_location_enable is not None:
          self.ap_location_enable = ap_location_enable
        if ap_location is not None:
          self.ap_location = ap_location

    @property
    def ap_location_enable(self):
        """
        Gets the ap_location_enable of this AplocationDto.
        用于标识AP安装位置信息开关是否打开。

        :return: The ap_location_enable of this AplocationDto.
        :rtype: bool
        """
        return self._ap_location_enable

    @ap_location_enable.setter
    def ap_location_enable(self, ap_location_enable):
        """
        Sets the ap_location_enable of this AplocationDto.
        用于标识AP安装位置信息开关是否打开。

        :param ap_location_enable: The ap_location_enable of this AplocationDto.
        :type: bool
        """

        self._ap_location_enable = ap_location_enable

    @property
    def ap_location(self):
        """
        Gets the ap_location of this AplocationDto.
        AP安装位置信息。当apLocationEnable为true时，apLocation必填。

        :return: The ap_location of this AplocationDto.
        :rtype: str
        """
        return self._ap_location

    @ap_location.setter
    def ap_location(self, ap_location):
        """
        Sets the ap_location of this AplocationDto.
        AP安装位置信息。当apLocationEnable为true时，apLocation必填。

        :param ap_location: The ap_location of this AplocationDto.
        :type: str
        """
        if ap_location is not None and len(ap_location) > 63:
            raise ValueError("Invalid value for `ap_location`, length must be less than or equal to `63`")
        if ap_location is not None and len(ap_location) < 1:
            raise ValueError("Invalid value for `ap_location`, length must be greater than or equal to `1`")
        if ap_location is not None and not re.search('[a-zA-Z0-9\\x5f\\x2d\\x40\\x2e]{1,}', ap_location):
            raise ValueError("Invalid value for `ap_location`, must be a follow pattern or equal to `/[a-zA-Z0-9\\x5f\\x2d\\x40\\x2e]{1,}/`")

        self._ap_location = ap_location

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
        if not isinstance(other, AplocationDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
