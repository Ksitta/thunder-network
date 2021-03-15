# coding: utf-8

"""
    TACACS模板管理

    TACACS模板配置北向接口，主要特性：  * 创建tacacs模板。 * 修改tacacs模板。 * 查询tacacs模板。 * 删除tacacs模板。 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TacacsTmplCommonInfoDto(object):
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
        'name': 'str',
        'description': 'str',
        'master_authen_server_ip': 'str',
        'master_authen_server_port': 'int',
        'slave_authen_server_ip': 'str',
        'slave_authen_server_port': 'int',
        'master_author_server_ip': 'str',
        'master_author_server_port': 'int',
        'slave_author_server_ip': 'str',
        'slave_author_server_port': 'int',
        'master_acc_server_ip': 'str',
        'master_acc_server_port': 'int',
        'slave_acc_server_ip': 'str',
        'slave_acc_server_port': 'int',
        'include_domain': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'master_authen_server_ip': 'masterAuthenServerIp',
        'master_authen_server_port': 'masterAuthenServerPort',
        'slave_authen_server_ip': 'slaveAuthenServerIp',
        'slave_authen_server_port': 'slaveAuthenServerPort',
        'master_author_server_ip': 'masterAuthorServerIp',
        'master_author_server_port': 'masterAuthorServerPort',
        'slave_author_server_ip': 'slaveAuthorServerIp',
        'slave_author_server_port': 'slaveAuthorServerPort',
        'master_acc_server_ip': 'masterAccServerIp',
        'master_acc_server_port': 'masterAccServerPort',
        'slave_acc_server_ip': 'slaveAccServerIp',
        'slave_acc_server_port': 'slaveAccServerPort',
        'include_domain': 'includeDomain'
    }

    def __init__(self, name=None, description=None, master_authen_server_ip=None, master_authen_server_port=None, slave_authen_server_ip=None, slave_authen_server_port=None, master_author_server_ip=None, master_author_server_port=None, slave_author_server_ip=None, slave_author_server_port=None, master_acc_server_ip=None, master_acc_server_port=None, slave_acc_server_ip=None, slave_acc_server_port=None, include_domain=None):
        """
        TacacsTmplCommonInfoDto - a model defined in Swagger
        """

        self._name = None
        self._description = None
        self._master_authen_server_ip = None
        self._master_authen_server_port = None
        self._slave_authen_server_ip = None
        self._slave_authen_server_port = None
        self._master_author_server_ip = None
        self._master_author_server_port = None
        self._slave_author_server_ip = None
        self._slave_author_server_port = None
        self._master_acc_server_ip = None
        self._master_acc_server_port = None
        self._slave_acc_server_ip = None
        self._slave_acc_server_port = None
        self._include_domain = None

        if name is not None:
          self.name = name
        if description is not None:
          self.description = description
        if master_authen_server_ip is not None:
          self.master_authen_server_ip = master_authen_server_ip
        if master_authen_server_port is not None:
          self.master_authen_server_port = master_authen_server_port
        if slave_authen_server_ip is not None:
          self.slave_authen_server_ip = slave_authen_server_ip
        if slave_authen_server_port is not None:
          self.slave_authen_server_port = slave_authen_server_port
        if master_author_server_ip is not None:
          self.master_author_server_ip = master_author_server_ip
        if master_author_server_port is not None:
          self.master_author_server_port = master_author_server_port
        if slave_author_server_ip is not None:
          self.slave_author_server_ip = slave_author_server_ip
        if slave_author_server_port is not None:
          self.slave_author_server_port = slave_author_server_port
        if master_acc_server_ip is not None:
          self.master_acc_server_ip = master_acc_server_ip
        if master_acc_server_port is not None:
          self.master_acc_server_port = master_acc_server_port
        if slave_acc_server_ip is not None:
          self.slave_acc_server_ip = slave_acc_server_ip
        if slave_acc_server_port is not None:
          self.slave_acc_server_port = slave_acc_server_port
        if include_domain is not None:
          self.include_domain = include_domain

    @property
    def name(self):
        """
        Gets the name of this TacacsTmplCommonInfoDto.
        名称（不支持$&?=+%][^_,#\"相关特殊字符）。

        :return: The name of this TacacsTmplCommonInfoDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TacacsTmplCommonInfoDto.
        名称（不支持$&?=+%][^_,#\"相关特殊字符）。

        :param name: The name of this TacacsTmplCommonInfoDto.
        :type: str
        """
        if name is not None and len(name) > 32:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `32`")
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this TacacsTmplCommonInfoDto.
        描述。

        :return: The description of this TacacsTmplCommonInfoDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this TacacsTmplCommonInfoDto.
        描述。

        :param description: The description of this TacacsTmplCommonInfoDto.
        :type: str
        """
        if description is not None and len(description) > 128:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `128`")

        self._description = description

    @property
    def master_authen_server_ip(self):
        """
        Gets the master_authen_server_ip of this TacacsTmplCommonInfoDto.
        主认证服务器IP地址。

        :return: The master_authen_server_ip of this TacacsTmplCommonInfoDto.
        :rtype: str
        """
        return self._master_authen_server_ip

    @master_authen_server_ip.setter
    def master_authen_server_ip(self, master_authen_server_ip):
        """
        Sets the master_authen_server_ip of this TacacsTmplCommonInfoDto.
        主认证服务器IP地址。

        :param master_authen_server_ip: The master_authen_server_ip of this TacacsTmplCommonInfoDto.
        :type: str
        """

        self._master_authen_server_ip = master_authen_server_ip

    @property
    def master_authen_server_port(self):
        """
        Gets the master_authen_server_port of this TacacsTmplCommonInfoDto.
        主认证服务器端口。

        :return: The master_authen_server_port of this TacacsTmplCommonInfoDto.
        :rtype: int
        """
        return self._master_authen_server_port

    @master_authen_server_port.setter
    def master_authen_server_port(self, master_authen_server_port):
        """
        Sets the master_authen_server_port of this TacacsTmplCommonInfoDto.
        主认证服务器端口。

        :param master_authen_server_port: The master_authen_server_port of this TacacsTmplCommonInfoDto.
        :type: int
        """
        if master_authen_server_port is not None and master_authen_server_port > 65535:
            raise ValueError("Invalid value for `master_authen_server_port`, must be a value less than or equal to `65535`")
        if master_authen_server_port is not None and master_authen_server_port < 1:
            raise ValueError("Invalid value for `master_authen_server_port`, must be a value greater than or equal to `1`")

        self._master_authen_server_port = master_authen_server_port

    @property
    def slave_authen_server_ip(self):
        """
        Gets the slave_authen_server_ip of this TacacsTmplCommonInfoDto.
        备认证服务器IP地址。

        :return: The slave_authen_server_ip of this TacacsTmplCommonInfoDto.
        :rtype: str
        """
        return self._slave_authen_server_ip

    @slave_authen_server_ip.setter
    def slave_authen_server_ip(self, slave_authen_server_ip):
        """
        Sets the slave_authen_server_ip of this TacacsTmplCommonInfoDto.
        备认证服务器IP地址。

        :param slave_authen_server_ip: The slave_authen_server_ip of this TacacsTmplCommonInfoDto.
        :type: str
        """

        self._slave_authen_server_ip = slave_authen_server_ip

    @property
    def slave_authen_server_port(self):
        """
        Gets the slave_authen_server_port of this TacacsTmplCommonInfoDto.
        备认证服务器端口。

        :return: The slave_authen_server_port of this TacacsTmplCommonInfoDto.
        :rtype: int
        """
        return self._slave_authen_server_port

    @slave_authen_server_port.setter
    def slave_authen_server_port(self, slave_authen_server_port):
        """
        Sets the slave_authen_server_port of this TacacsTmplCommonInfoDto.
        备认证服务器端口。

        :param slave_authen_server_port: The slave_authen_server_port of this TacacsTmplCommonInfoDto.
        :type: int
        """
        if slave_authen_server_port is not None and slave_authen_server_port > 65535:
            raise ValueError("Invalid value for `slave_authen_server_port`, must be a value less than or equal to `65535`")
        if slave_authen_server_port is not None and slave_authen_server_port < 1:
            raise ValueError("Invalid value for `slave_authen_server_port`, must be a value greater than or equal to `1`")

        self._slave_authen_server_port = slave_authen_server_port

    @property
    def master_author_server_ip(self):
        """
        Gets the master_author_server_ip of this TacacsTmplCommonInfoDto.
        主授权服务器IP地址。

        :return: The master_author_server_ip of this TacacsTmplCommonInfoDto.
        :rtype: str
        """
        return self._master_author_server_ip

    @master_author_server_ip.setter
    def master_author_server_ip(self, master_author_server_ip):
        """
        Sets the master_author_server_ip of this TacacsTmplCommonInfoDto.
        主授权服务器IP地址。

        :param master_author_server_ip: The master_author_server_ip of this TacacsTmplCommonInfoDto.
        :type: str
        """

        self._master_author_server_ip = master_author_server_ip

    @property
    def master_author_server_port(self):
        """
        Gets the master_author_server_port of this TacacsTmplCommonInfoDto.
        主授权服务器端口。

        :return: The master_author_server_port of this TacacsTmplCommonInfoDto.
        :rtype: int
        """
        return self._master_author_server_port

    @master_author_server_port.setter
    def master_author_server_port(self, master_author_server_port):
        """
        Sets the master_author_server_port of this TacacsTmplCommonInfoDto.
        主授权服务器端口。

        :param master_author_server_port: The master_author_server_port of this TacacsTmplCommonInfoDto.
        :type: int
        """
        if master_author_server_port is not None and master_author_server_port > 65535:
            raise ValueError("Invalid value for `master_author_server_port`, must be a value less than or equal to `65535`")
        if master_author_server_port is not None and master_author_server_port < 1:
            raise ValueError("Invalid value for `master_author_server_port`, must be a value greater than or equal to `1`")

        self._master_author_server_port = master_author_server_port

    @property
    def slave_author_server_ip(self):
        """
        Gets the slave_author_server_ip of this TacacsTmplCommonInfoDto.
        备授权服务器IP地址。

        :return: The slave_author_server_ip of this TacacsTmplCommonInfoDto.
        :rtype: str
        """
        return self._slave_author_server_ip

    @slave_author_server_ip.setter
    def slave_author_server_ip(self, slave_author_server_ip):
        """
        Sets the slave_author_server_ip of this TacacsTmplCommonInfoDto.
        备授权服务器IP地址。

        :param slave_author_server_ip: The slave_author_server_ip of this TacacsTmplCommonInfoDto.
        :type: str
        """

        self._slave_author_server_ip = slave_author_server_ip

    @property
    def slave_author_server_port(self):
        """
        Gets the slave_author_server_port of this TacacsTmplCommonInfoDto.
        备授权服务器端口。

        :return: The slave_author_server_port of this TacacsTmplCommonInfoDto.
        :rtype: int
        """
        return self._slave_author_server_port

    @slave_author_server_port.setter
    def slave_author_server_port(self, slave_author_server_port):
        """
        Sets the slave_author_server_port of this TacacsTmplCommonInfoDto.
        备授权服务器端口。

        :param slave_author_server_port: The slave_author_server_port of this TacacsTmplCommonInfoDto.
        :type: int
        """
        if slave_author_server_port is not None and slave_author_server_port > 65535:
            raise ValueError("Invalid value for `slave_author_server_port`, must be a value less than or equal to `65535`")
        if slave_author_server_port is not None and slave_author_server_port < 1:
            raise ValueError("Invalid value for `slave_author_server_port`, must be a value greater than or equal to `1`")

        self._slave_author_server_port = slave_author_server_port

    @property
    def master_acc_server_ip(self):
        """
        Gets the master_acc_server_ip of this TacacsTmplCommonInfoDto.
        主计费服务器IP地址。

        :return: The master_acc_server_ip of this TacacsTmplCommonInfoDto.
        :rtype: str
        """
        return self._master_acc_server_ip

    @master_acc_server_ip.setter
    def master_acc_server_ip(self, master_acc_server_ip):
        """
        Sets the master_acc_server_ip of this TacacsTmplCommonInfoDto.
        主计费服务器IP地址。

        :param master_acc_server_ip: The master_acc_server_ip of this TacacsTmplCommonInfoDto.
        :type: str
        """

        self._master_acc_server_ip = master_acc_server_ip

    @property
    def master_acc_server_port(self):
        """
        Gets the master_acc_server_port of this TacacsTmplCommonInfoDto.
        主计费服务器端口。

        :return: The master_acc_server_port of this TacacsTmplCommonInfoDto.
        :rtype: int
        """
        return self._master_acc_server_port

    @master_acc_server_port.setter
    def master_acc_server_port(self, master_acc_server_port):
        """
        Sets the master_acc_server_port of this TacacsTmplCommonInfoDto.
        主计费服务器端口。

        :param master_acc_server_port: The master_acc_server_port of this TacacsTmplCommonInfoDto.
        :type: int
        """
        if master_acc_server_port is not None and master_acc_server_port > 65535:
            raise ValueError("Invalid value for `master_acc_server_port`, must be a value less than or equal to `65535`")
        if master_acc_server_port is not None and master_acc_server_port < 1:
            raise ValueError("Invalid value for `master_acc_server_port`, must be a value greater than or equal to `1`")

        self._master_acc_server_port = master_acc_server_port

    @property
    def slave_acc_server_ip(self):
        """
        Gets the slave_acc_server_ip of this TacacsTmplCommonInfoDto.
        备计费服务器IP地址。

        :return: The slave_acc_server_ip of this TacacsTmplCommonInfoDto.
        :rtype: str
        """
        return self._slave_acc_server_ip

    @slave_acc_server_ip.setter
    def slave_acc_server_ip(self, slave_acc_server_ip):
        """
        Sets the slave_acc_server_ip of this TacacsTmplCommonInfoDto.
        备计费服务器IP地址。

        :param slave_acc_server_ip: The slave_acc_server_ip of this TacacsTmplCommonInfoDto.
        :type: str
        """

        self._slave_acc_server_ip = slave_acc_server_ip

    @property
    def slave_acc_server_port(self):
        """
        Gets the slave_acc_server_port of this TacacsTmplCommonInfoDto.
        备计费服务器端口。

        :return: The slave_acc_server_port of this TacacsTmplCommonInfoDto.
        :rtype: int
        """
        return self._slave_acc_server_port

    @slave_acc_server_port.setter
    def slave_acc_server_port(self, slave_acc_server_port):
        """
        Sets the slave_acc_server_port of this TacacsTmplCommonInfoDto.
        备计费服务器端口。

        :param slave_acc_server_port: The slave_acc_server_port of this TacacsTmplCommonInfoDto.
        :type: int
        """
        if slave_acc_server_port is not None and slave_acc_server_port > 65535:
            raise ValueError("Invalid value for `slave_acc_server_port`, must be a value less than or equal to `65535`")
        if slave_acc_server_port is not None and slave_acc_server_port < 1:
            raise ValueError("Invalid value for `slave_acc_server_port`, must be a value greater than or equal to `1`")

        self._slave_acc_server_port = slave_acc_server_port

    @property
    def include_domain(self):
        """
        Gets the include_domain of this TacacsTmplCommonInfoDto.
        向Tacacs服务器发起认证的用户名是否包含域名。

        :return: The include_domain of this TacacsTmplCommonInfoDto.
        :rtype: bool
        """
        return self._include_domain

    @include_domain.setter
    def include_domain(self, include_domain):
        """
        Sets the include_domain of this TacacsTmplCommonInfoDto.
        向Tacacs服务器发起认证的用户名是否包含域名。

        :param include_domain: The include_domain of this TacacsTmplCommonInfoDto.
        :type: bool
        """

        self._include_domain = include_domain

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
        if not isinstance(other, TacacsTmplCommonInfoDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
