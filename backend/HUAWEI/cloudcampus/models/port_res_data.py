# coding: utf-8

"""
    实体资源北向接口

    实体资源条件查询。 

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PortResData(object):
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
        'neip': 'str',
        'nename': 'str',
        'nedn': 'str',
        'portdn': 'str',
        'framedn': 'str',
        'slotdn': 'str',
        'subslotdn': 'str',
        'frameno': 'int',
        'slotno': 'int',
        'subslotno': 'int',
        'portindex': 'int',
        'portno': 'int',
        'descr': 'str',
        'name': 'str',
        'adminstatus': 'int',
        'operstatus': 'int',
        'ifindex': 'int',
        'iftype': 'int',
        'ipaddress': 'str',
        'ipnetmask': 'str',
        'ifspeed': 'str'
    }

    attribute_map = {
        'neip': 'neip',
        'nename': 'nename',
        'nedn': 'nedn',
        'portdn': 'portdn',
        'framedn': 'framedn',
        'slotdn': 'slotdn',
        'subslotdn': 'subslotdn',
        'frameno': 'frameno',
        'slotno': 'slotno',
        'subslotno': 'subslotno',
        'portindex': 'portindex',
        'portno': 'portno',
        'descr': 'descr',
        'name': 'name',
        'adminstatus': 'adminstatus',
        'operstatus': 'operstatus',
        'ifindex': 'ifindex',
        'iftype': 'iftype',
        'ipaddress': 'ipaddress',
        'ipnetmask': 'ipnetmask',
        'ifspeed': 'ifspeed'
    }

    def __init__(self, neip=None, nename=None, nedn=None, portdn=None, framedn=None, slotdn=None, subslotdn=None, frameno=None, slotno=None, subslotno=None, portindex=None, portno=None, descr=None, name=None, adminstatus=None, operstatus=None, ifindex=None, iftype=None, ipaddress=None, ipnetmask=None, ifspeed=None):
        """
        PortResData - a model defined in Swagger
        """

        self._neip = None
        self._nename = None
        self._nedn = None
        self._portdn = None
        self._framedn = None
        self._slotdn = None
        self._subslotdn = None
        self._frameno = None
        self._slotno = None
        self._subslotno = None
        self._portindex = None
        self._portno = None
        self._descr = None
        self._name = None
        self._adminstatus = None
        self._operstatus = None
        self._ifindex = None
        self._iftype = None
        self._ipaddress = None
        self._ipnetmask = None
        self._ifspeed = None

        if neip is not None:
          self.neip = neip
        if nename is not None:
          self.nename = nename
        if nedn is not None:
          self.nedn = nedn
        if portdn is not None:
          self.portdn = portdn
        if framedn is not None:
          self.framedn = framedn
        if slotdn is not None:
          self.slotdn = slotdn
        if subslotdn is not None:
          self.subslotdn = subslotdn
        if frameno is not None:
          self.frameno = frameno
        if slotno is not None:
          self.slotno = slotno
        if subslotno is not None:
          self.subslotno = subslotno
        if portindex is not None:
          self.portindex = portindex
        if portno is not None:
          self.portno = portno
        if descr is not None:
          self.descr = descr
        if name is not None:
          self.name = name
        if adminstatus is not None:
          self.adminstatus = adminstatus
        if operstatus is not None:
          self.operstatus = operstatus
        if ifindex is not None:
          self.ifindex = ifindex
        if iftype is not None:
          self.iftype = iftype
        if ipaddress is not None:
          self.ipaddress = ipaddress
        if ipnetmask is not None:
          self.ipnetmask = ipnetmask
        if ifspeed is not None:
          self.ifspeed = ifspeed

    @property
    def neip(self):
        """
        Gets the neip of this PortResData.
        设备IP地址（通过，分隔）。

        :return: The neip of this PortResData.
        :rtype: str
        """
        return self._neip

    @neip.setter
    def neip(self, neip):
        """
        Sets the neip of this PortResData.
        设备IP地址（通过，分隔）。

        :param neip: The neip of this PortResData.
        :type: str
        """

        self._neip = neip

    @property
    def nename(self):
        """
        Gets the nename of this PortResData.
        设备名称。

        :return: The nename of this PortResData.
        :rtype: str
        """
        return self._nename

    @nename.setter
    def nename(self, nename):
        """
        Sets the nename of this PortResData.
        设备名称。

        :param nename: The nename of this PortResData.
        :type: str
        """

        self._nename = nename

    @property
    def nedn(self):
        """
        Gets the nedn of this PortResData.
        设备dn。

        :return: The nedn of this PortResData.
        :rtype: str
        """
        return self._nedn

    @nedn.setter
    def nedn(self, nedn):
        """
        Sets the nedn of this PortResData.
        设备dn。

        :param nedn: The nedn of this PortResData.
        :type: str
        """

        self._nedn = nedn

    @property
    def portdn(self):
        """
        Gets the portdn of this PortResData.
        端口dn。

        :return: The portdn of this PortResData.
        :rtype: str
        """
        return self._portdn

    @portdn.setter
    def portdn(self, portdn):
        """
        Sets the portdn of this PortResData.
        端口dn。

        :param portdn: The portdn of this PortResData.
        :type: str
        """

        self._portdn = portdn

    @property
    def framedn(self):
        """
        Gets the framedn of this PortResData.
        机框dn。

        :return: The framedn of this PortResData.
        :rtype: str
        """
        return self._framedn

    @framedn.setter
    def framedn(self, framedn):
        """
        Sets the framedn of this PortResData.
        机框dn。

        :param framedn: The framedn of this PortResData.
        :type: str
        """

        self._framedn = framedn

    @property
    def slotdn(self):
        """
        Gets the slotdn of this PortResData.
        单板dn。

        :return: The slotdn of this PortResData.
        :rtype: str
        """
        return self._slotdn

    @slotdn.setter
    def slotdn(self, slotdn):
        """
        Sets the slotdn of this PortResData.
        单板dn。

        :param slotdn: The slotdn of this PortResData.
        :type: str
        """

        self._slotdn = slotdn

    @property
    def subslotdn(self):
        """
        Gets the subslotdn of this PortResData.
        子卡dn。

        :return: The subslotdn of this PortResData.
        :rtype: str
        """
        return self._subslotdn

    @subslotdn.setter
    def subslotdn(self, subslotdn):
        """
        Sets the subslotdn of this PortResData.
        子卡dn。

        :param subslotdn: The subslotdn of this PortResData.
        :type: str
        """

        self._subslotdn = subslotdn

    @property
    def frameno(self):
        """
        Gets the frameno of this PortResData.
        机框序号。

        :return: The frameno of this PortResData.
        :rtype: int
        """
        return self._frameno

    @frameno.setter
    def frameno(self, frameno):
        """
        Sets the frameno of this PortResData.
        机框序号。

        :param frameno: The frameno of this PortResData.
        :type: int
        """

        self._frameno = frameno

    @property
    def slotno(self):
        """
        Gets the slotno of this PortResData.
        单板序号。

        :return: The slotno of this PortResData.
        :rtype: int
        """
        return self._slotno

    @slotno.setter
    def slotno(self, slotno):
        """
        Sets the slotno of this PortResData.
        单板序号。

        :param slotno: The slotno of this PortResData.
        :type: int
        """

        self._slotno = slotno

    @property
    def subslotno(self):
        """
        Gets the subslotno of this PortResData.
        子卡序号。

        :return: The subslotno of this PortResData.
        :rtype: int
        """
        return self._subslotno

    @subslotno.setter
    def subslotno(self, subslotno):
        """
        Sets the subslotno of this PortResData.
        子卡序号。

        :param subslotno: The subslotno of this PortResData.
        :type: int
        """

        self._subslotno = subslotno

    @property
    def portindex(self):
        """
        Gets the portindex of this PortResData.
        端口索引。

        :return: The portindex of this PortResData.
        :rtype: int
        """
        return self._portindex

    @portindex.setter
    def portindex(self, portindex):
        """
        Sets the portindex of this PortResData.
        端口索引。

        :param portindex: The portindex of this PortResData.
        :type: int
        """

        self._portindex = portindex

    @property
    def portno(self):
        """
        Gets the portno of this PortResData.
        端口编号。

        :return: The portno of this PortResData.
        :rtype: int
        """
        return self._portno

    @portno.setter
    def portno(self, portno):
        """
        Sets the portno of this PortResData.
        端口编号。

        :param portno: The portno of this PortResData.
        :type: int
        """

        self._portno = portno

    @property
    def descr(self):
        """
        Gets the descr of this PortResData.
        端口描述。

        :return: The descr of this PortResData.
        :rtype: str
        """
        return self._descr

    @descr.setter
    def descr(self, descr):
        """
        Sets the descr of this PortResData.
        端口描述。

        :param descr: The descr of this PortResData.
        :type: str
        """

        self._descr = descr

    @property
    def name(self):
        """
        Gets the name of this PortResData.
        端口名称。

        :return: The name of this PortResData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PortResData.
        端口名称。

        :param name: The name of this PortResData.
        :type: str
        """

        self._name = name

    @property
    def adminstatus(self):
        """
        Gets the adminstatus of this PortResData.
        管理状态。

        :return: The adminstatus of this PortResData.
        :rtype: int
        """
        return self._adminstatus

    @adminstatus.setter
    def adminstatus(self, adminstatus):
        """
        Sets the adminstatus of this PortResData.
        管理状态。

        :param adminstatus: The adminstatus of this PortResData.
        :type: int
        """

        self._adminstatus = adminstatus

    @property
    def operstatus(self):
        """
        Gets the operstatus of this PortResData.
        操作状态。

        :return: The operstatus of this PortResData.
        :rtype: int
        """
        return self._operstatus

    @operstatus.setter
    def operstatus(self, operstatus):
        """
        Sets the operstatus of this PortResData.
        操作状态。

        :param operstatus: The operstatus of this PortResData.
        :type: int
        """

        self._operstatus = operstatus

    @property
    def ifindex(self):
        """
        Gets the ifindex of this PortResData.
        接口索引。

        :return: The ifindex of this PortResData.
        :rtype: int
        """
        return self._ifindex

    @ifindex.setter
    def ifindex(self, ifindex):
        """
        Sets the ifindex of this PortResData.
        接口索引。

        :param ifindex: The ifindex of this PortResData.
        :type: int
        """

        self._ifindex = ifindex

    @property
    def iftype(self):
        """
        Gets the iftype of this PortResData.
        端口类型。

        :return: The iftype of this PortResData.
        :rtype: int
        """
        return self._iftype

    @iftype.setter
    def iftype(self, iftype):
        """
        Sets the iftype of this PortResData.
        端口类型。

        :param iftype: The iftype of this PortResData.
        :type: int
        """

        self._iftype = iftype

    @property
    def ipaddress(self):
        """
        Gets the ipaddress of this PortResData.
        端口IP地址。

        :return: The ipaddress of this PortResData.
        :rtype: str
        """
        return self._ipaddress

    @ipaddress.setter
    def ipaddress(self, ipaddress):
        """
        Sets the ipaddress of this PortResData.
        端口IP地址。

        :param ipaddress: The ipaddress of this PortResData.
        :type: str
        """

        self._ipaddress = ipaddress

    @property
    def ipnetmask(self):
        """
        Gets the ipnetmask of this PortResData.
        端口子网掩码。

        :return: The ipnetmask of this PortResData.
        :rtype: str
        """
        return self._ipnetmask

    @ipnetmask.setter
    def ipnetmask(self, ipnetmask):
        """
        Sets the ipnetmask of this PortResData.
        端口子网掩码。

        :param ipnetmask: The ipnetmask of this PortResData.
        :type: str
        """

        self._ipnetmask = ipnetmask

    @property
    def ifspeed(self):
        """
        Gets the ifspeed of this PortResData.
        端口速率（bps）。

        :return: The ifspeed of this PortResData.
        :rtype: str
        """
        return self._ifspeed

    @ifspeed.setter
    def ifspeed(self, ifspeed):
        """
        Sets the ifspeed of this PortResData.
        端口速率（bps）。

        :param ifspeed: The ifspeed of this PortResData.
        :type: str
        """

        self._ifspeed = ifspeed

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
        if not isinstance(other, PortResData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
