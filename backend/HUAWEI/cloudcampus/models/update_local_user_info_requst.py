# coding: utf-8

"""
    本地用户配置管理

    本地用户配置北向接口，主要特性： · 查询本地用户配置 · 修改本地用户配置 · 创建本地用户配置 

    OpenAPI spec version: 1.2.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UpdateLocalUserInfoRequst(object):
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
        'password': 'str',
        'role': 'int',
        'service_type': 'list[str]'
    }

    attribute_map = {
        'password': 'password',
        'role': 'role',
        'service_type': 'serviceType'
    }

    def __init__(self, password=None, role=None, service_type=None):
        """
        UpdateLocalUserInfoRequst - a model defined in Swagger
        """

        self._password = None
        self._role = None
        self._service_type = None

        if password is not None:
          self.password = password
        if role is not None:
          self.role = role
        if service_type is not None:
          self.service_type = service_type

    @property
    def password(self):
        """
        Gets the password of this UpdateLocalUserInfoRequst.
        用户密码。

        :return: The password of this UpdateLocalUserInfoRequst.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this UpdateLocalUserInfoRequst.
        用户密码。

        :param password: The password of this UpdateLocalUserInfoRequst.
        :type: str
        """
        if password is not None and len(password) > 128:
            raise ValueError("Invalid value for `password`, length must be less than or equal to `128`")
        if password is not None and len(password) < 8:
            raise ValueError("Invalid value for `password`, length must be greater than or equal to `8`")

        self._password = password

    @property
    def role(self):
        """
        Gets the role of this UpdateLocalUserInfoRequst.
        用户角色（1---Monitor User，15---Manager User）。

        :return: The role of this UpdateLocalUserInfoRequst.
        :rtype: int
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this UpdateLocalUserInfoRequst.
        用户角色（1---Monitor User，15---Manager User）。

        :param role: The role of this UpdateLocalUserInfoRequst.
        :type: int
        """

        self._role = role

    @property
    def service_type(self):
        """
        Gets the service_type of this UpdateLocalUserInfoRequst.
        登录类型（\"http\"，\"ssh\"）。

        :return: The service_type of this UpdateLocalUserInfoRequst.
        :rtype: list[str]
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """
        Sets the service_type of this UpdateLocalUserInfoRequst.
        登录类型（\"http\"，\"ssh\"）。

        :param service_type: The service_type of this UpdateLocalUserInfoRequst.
        :type: list[str]
        """
        allowed_values = ["http", "ssh"]
        if not set(service_type).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `service_type` [{0}], must be a subset of [{1}]"
                .format(", ".join(map(str, set(service_type)-set(allowed_values))),
                        ", ".join(map(str, allowed_values)))
            )

        self._service_type = service_type

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
        if not isinstance(other, UpdateLocalUserInfoRequst):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
