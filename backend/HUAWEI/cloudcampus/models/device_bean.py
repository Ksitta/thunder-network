# coding: utf-8

"""
    设备基本信息管理

    设备相关操作接口。 场景：对设备增删改查操作的第三方接口。

    OpenAPI spec version: 1.6.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DeviceBean(object):
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
        'id': 'str',
        'name': 'str',
        'esn': 'str',
        'device_model': 'str',
        'device_type': 'str',
        'status': 'str',
        'site_id': 'str',
        'mac': 'str',
        'ip': 'str',
        'ne_type': 'str',
        'version': 'str',
        'vendor': 'str',
        'description': 'str',
        'tenant_id': 'str',
        'tenant_name': 'str',
        'site_name': 'str',
        'create_time': 'str',
        'register_time': 'str',
        'modify_time': 'str',
        'startup_time': 'str',
        'tags': 'list[str]',
        'system_ip': 'str',
        'patch_version': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'esn': 'esn',
        'device_model': 'deviceModel',
        'device_type': 'deviceType',
        'status': 'status',
        'site_id': 'siteId',
        'mac': 'mac',
        'ip': 'ip',
        'ne_type': 'neType',
        'version': 'version',
        'vendor': 'vendor',
        'description': 'description',
        'tenant_id': 'tenantId',
        'tenant_name': 'tenantName',
        'site_name': 'siteName',
        'create_time': 'createTime',
        'register_time': 'registerTime',
        'modify_time': 'modifyTime',
        'startup_time': 'startupTime',
        'tags': 'tags',
        'system_ip': 'systemIp',
        'patch_version': 'patchVersion'
    }

    def __init__(self, id=None, name=None, esn=None, device_model=None, device_type=None, status='0', site_id=None, mac=None, ip=None, ne_type=None, version=None, vendor=None, description=None, tenant_id=None, tenant_name=None, site_name=None, create_time=None, register_time=None, modify_time=None, startup_time=None, tags=None, system_ip=None, patch_version=None):
        """
        DeviceBean - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._esn = None
        self._device_model = None
        self._device_type = None
        self._status = None
        self._site_id = None
        self._mac = None
        self._ip = None
        self._ne_type = None
        self._version = None
        self._vendor = None
        self._description = None
        self._tenant_id = None
        self._tenant_name = None
        self._site_name = None
        self._create_time = None
        self._register_time = None
        self._modify_time = None
        self._startup_time = None
        self._tags = None
        self._system_ip = None
        self._patch_version = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if esn is not None:
          self.esn = esn
        if device_model is not None:
          self.device_model = device_model
        if device_type is not None:
          self.device_type = device_type
        if status is not None:
          self.status = status
        if site_id is not None:
          self.site_id = site_id
        if mac is not None:
          self.mac = mac
        if ip is not None:
          self.ip = ip
        if ne_type is not None:
          self.ne_type = ne_type
        if version is not None:
          self.version = version
        if vendor is not None:
          self.vendor = vendor
        if description is not None:
          self.description = description
        if tenant_id is not None:
          self.tenant_id = tenant_id
        if tenant_name is not None:
          self.tenant_name = tenant_name
        if site_name is not None:
          self.site_name = site_name
        if create_time is not None:
          self.create_time = create_time
        if register_time is not None:
          self.register_time = register_time
        if modify_time is not None:
          self.modify_time = modify_time
        if startup_time is not None:
          self.startup_time = startup_time
        if tags is not None:
          self.tags = tags
        if system_ip is not None:
          self.system_ip = system_ip
        if patch_version is not None:
          self.patch_version = patch_version

    @property
    def id(self):
        """
        Gets the id of this DeviceBean.
        设备ID。

        :return: The id of this DeviceBean.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DeviceBean.
        设备ID。

        :param id: The id of this DeviceBean.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this DeviceBean.
        设备名称。

        :return: The name of this DeviceBean.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DeviceBean.
        设备名称。

        :param name: The name of this DeviceBean.
        :type: str
        """
        if name is not None and len(name) > 256:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `256`")

        self._name = name

    @property
    def esn(self):
        """
        Gets the esn of this DeviceBean.
        设备ESN号。

        :return: The esn of this DeviceBean.
        :rtype: str
        """
        return self._esn

    @esn.setter
    def esn(self, esn):
        """
        Sets the esn of this DeviceBean.
        设备ESN号。

        :param esn: The esn of this DeviceBean.
        :type: str
        """
        if esn is not None and len(esn) > 256:
            raise ValueError("Invalid value for `esn`, length must be less than or equal to `256`")

        self._esn = esn

    @property
    def device_model(self):
        """
        Gets the device_model of this DeviceBean.
        设备款型。

        :return: The device_model of this DeviceBean.
        :rtype: str
        """
        return self._device_model

    @device_model.setter
    def device_model(self, device_model):
        """
        Sets the device_model of this DeviceBean.
        设备款型。

        :param device_model: The device_model of this DeviceBean.
        :type: str
        """
        if device_model is not None and len(device_model) > 128:
            raise ValueError("Invalid value for `device_model`, length must be less than or equal to `128`")

        self._device_model = device_model

    @property
    def device_type(self):
        """
        Gets the device_type of this DeviceBean.
        设备类型，支持以下几种：“AR”、“AP”、“FW”或者“LSW”。

        :return: The device_type of this DeviceBean.
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """
        Sets the device_type of this DeviceBean.
        设备类型，支持以下几种：“AR”、“AP”、“FW”或者“LSW”。

        :param device_type: The device_type of this DeviceBean.
        :type: str
        """
        if device_type is not None and len(device_type) > 128:
            raise ValueError("Invalid value for `device_type`, length must be less than or equal to `128`")

        self._device_type = device_type

    @property
    def status(self):
        """
        Gets the status of this DeviceBean.
        设备状态，0---正常、1---告警、3---离线、4---未注册。

        :return: The status of this DeviceBean.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this DeviceBean.
        设备状态，0---正常、1---告警、3---离线、4---未注册。

        :param status: The status of this DeviceBean.
        :type: str
        """

        self._status = status

    @property
    def site_id(self):
        """
        Gets the site_id of this DeviceBean.
        设备所属站点的ID。

        :return: The site_id of this DeviceBean.
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """
        Sets the site_id of this DeviceBean.
        设备所属站点的ID。

        :param site_id: The site_id of this DeviceBean.
        :type: str
        """

        self._site_id = site_id

    @property
    def mac(self):
        """
        Gets the mac of this DeviceBean.
        设备MAC。

        :return: The mac of this DeviceBean.
        :rtype: str
        """
        return self._mac

    @mac.setter
    def mac(self, mac):
        """
        Sets the mac of this DeviceBean.
        设备MAC。

        :param mac: The mac of this DeviceBean.
        :type: str
        """

        self._mac = mac

    @property
    def ip(self):
        """
        Gets the ip of this DeviceBean.
        设备IP。

        :return: The ip of this DeviceBean.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """
        Sets the ip of this DeviceBean.
        设备IP。

        :param ip: The ip of this DeviceBean.
        :type: str
        """

        self._ip = ip

    @property
    def ne_type(self):
        """
        Gets the ne_type of this DeviceBean.
        设备款型。

        :return: The ne_type of this DeviceBean.
        :rtype: str
        """
        return self._ne_type

    @ne_type.setter
    def ne_type(self, ne_type):
        """
        Sets the ne_type of this DeviceBean.
        设备款型。

        :param ne_type: The ne_type of this DeviceBean.
        :type: str
        """

        self._ne_type = ne_type

    @property
    def version(self):
        """
        Gets the version of this DeviceBean.
        设备软件版本。

        :return: The version of this DeviceBean.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this DeviceBean.
        设备软件版本。

        :param version: The version of this DeviceBean.
        :type: str
        """

        self._version = version

    @property
    def vendor(self):
        """
        Gets the vendor of this DeviceBean.
        设备制造商。

        :return: The vendor of this DeviceBean.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this DeviceBean.
        设备制造商。

        :param vendor: The vendor of this DeviceBean.
        :type: str
        """

        self._vendor = vendor

    @property
    def description(self):
        """
        Gets the description of this DeviceBean.
        设备备注信息。

        :return: The description of this DeviceBean.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DeviceBean.
        设备备注信息。

        :param description: The description of this DeviceBean.
        :type: str
        """

        self._description = description

    @property
    def tenant_id(self):
        """
        Gets the tenant_id of this DeviceBean.
        租户ID。

        :return: The tenant_id of this DeviceBean.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """
        Sets the tenant_id of this DeviceBean.
        租户ID。

        :param tenant_id: The tenant_id of this DeviceBean.
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def tenant_name(self):
        """
        Gets the tenant_name of this DeviceBean.
        租户名称。

        :return: The tenant_name of this DeviceBean.
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        """
        Sets the tenant_name of this DeviceBean.
        租户名称。

        :param tenant_name: The tenant_name of this DeviceBean.
        :type: str
        """

        self._tenant_name = tenant_name

    @property
    def site_name(self):
        """
        Gets the site_name of this DeviceBean.
        站点名称。

        :return: The site_name of this DeviceBean.
        :rtype: str
        """
        return self._site_name

    @site_name.setter
    def site_name(self, site_name):
        """
        Sets the site_name of this DeviceBean.
        站点名称。

        :param site_name: The site_name of this DeviceBean.
        :type: str
        """

        self._site_name = site_name

    @property
    def create_time(self):
        """
        Gets the create_time of this DeviceBean.
        创建时间。

        :return: The create_time of this DeviceBean.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this DeviceBean.
        创建时间。

        :param create_time: The create_time of this DeviceBean.
        :type: str
        """

        self._create_time = create_time

    @property
    def register_time(self):
        """
        Gets the register_time of this DeviceBean.
        设备首次注册时间。

        :return: The register_time of this DeviceBean.
        :rtype: str
        """
        return self._register_time

    @register_time.setter
    def register_time(self, register_time):
        """
        Sets the register_time of this DeviceBean.
        设备首次注册时间。

        :param register_time: The register_time of this DeviceBean.
        :type: str
        """

        self._register_time = register_time

    @property
    def modify_time(self):
        """
        Gets the modify_time of this DeviceBean.
        修改时间。

        :return: The modify_time of this DeviceBean.
        :rtype: str
        """
        return self._modify_time

    @modify_time.setter
    def modify_time(self, modify_time):
        """
        Sets the modify_time of this DeviceBean.
        修改时间。

        :param modify_time: The modify_time of this DeviceBean.
        :type: str
        """

        self._modify_time = modify_time

    @property
    def startup_time(self):
        """
        Gets the startup_time of this DeviceBean.
        设备重启时间。

        :return: The startup_time of this DeviceBean.
        :rtype: str
        """
        return self._startup_time

    @startup_time.setter
    def startup_time(self, startup_time):
        """
        Sets the startup_time of this DeviceBean.
        设备重启时间。

        :param startup_time: The startup_time of this DeviceBean.
        :type: str
        """

        self._startup_time = startup_time

    @property
    def tags(self):
        """
        Gets the tags of this DeviceBean.
        设备标签列表。

        :return: The tags of this DeviceBean.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this DeviceBean.
        设备标签列表。

        :param tags: The tags of this DeviceBean.
        :type: list[str]
        """

        self._tags = tags

    @property
    def system_ip(self):
        """
        Gets the system_ip of this DeviceBean.
        系统IP地址。

        :return: The system_ip of this DeviceBean.
        :rtype: str
        """
        return self._system_ip

    @system_ip.setter
    def system_ip(self, system_ip):
        """
        Sets the system_ip of this DeviceBean.
        系统IP地址。

        :param system_ip: The system_ip of this DeviceBean.
        :type: str
        """
        if system_ip is not None and len(system_ip) > 64:
            raise ValueError("Invalid value for `system_ip`, length must be less than or equal to `64`")
        if system_ip is not None and len(system_ip) < 0:
            raise ValueError("Invalid value for `system_ip`, length must be greater than or equal to `0`")

        self._system_ip = system_ip

    @property
    def patch_version(self):
        """
        Gets the patch_version of this DeviceBean.
        设备补丁版本。

        :return: The patch_version of this DeviceBean.
        :rtype: str
        """
        return self._patch_version

    @patch_version.setter
    def patch_version(self, patch_version):
        """
        Sets the patch_version of this DeviceBean.
        设备补丁版本。

        :param patch_version: The patch_version of this DeviceBean.
        :type: str
        """
        if patch_version is not None and len(patch_version) > 256:
            raise ValueError("Invalid value for `patch_version`, length must be less than or equal to `256`")
        if patch_version is not None and len(patch_version) < 0:
            raise ValueError("Invalid value for `patch_version`, length must be greater than or equal to `0`")

        self._patch_version = patch_version

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
        if not isinstance(other, DeviceBean):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
