# coding: utf-8

"""
    设备BootROM密码配置

    设备BootROM密码配置第三方接口。

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class BootRomDto(object):
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
        'passwd': 'str'
    }

    attribute_map = {
        'passwd': 'passwd'
    }

    def __init__(self, passwd=None):
        """
        BootRomDto - a model defined in Swagger
        """

        self._passwd = None

        if passwd is not None:
          self.passwd = passwd

    @property
    def passwd(self):
        """
        Gets the passwd of this BootRomDto.
        1、密码长度必须在8-80位。 2、密码必须满足复杂度，即至少包含英文大写字母（A~Z）、英文小写字母（a~z）、数字（0~9）、特殊字符（如！、@、#、$、%）等中的三种，不允许包含'、?和空格。 3、密码中不能包含两个以上连续的相同字符。 

        :return: The passwd of this BootRomDto.
        :rtype: str
        """
        return self._passwd

    @passwd.setter
    def passwd(self, passwd):
        """
        Sets the passwd of this BootRomDto.
        1、密码长度必须在8-80位。 2、密码必须满足复杂度，即至少包含英文大写字母（A~Z）、英文小写字母（a~z）、数字（0~9）、特殊字符（如！、@、#、$、%）等中的三种，不允许包含'、?和空格。 3、密码中不能包含两个以上连续的相同字符。 

        :param passwd: The passwd of this BootRomDto.
        :type: str
        """
        if passwd is not None and len(passwd) > 80:
            raise ValueError("Invalid value for `passwd`, length must be less than or equal to `80`")
        if passwd is not None and len(passwd) < 8:
            raise ValueError("Invalid value for `passwd`, length must be greater than or equal to `8`")

        self._passwd = passwd

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
        if not isinstance(other, BootRomDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
