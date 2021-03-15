# coding: utf-8

"""
    拓扑管理

    拓扑管理第三方北向接口。 1、查询LACP LAG信息 2、查询LLDP信息 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class EthTrunkInterfacesDto(object):
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
        'if_id': 'int',
        'if_name': 'str',
        'rem_prio': 'int',
        'rem_id': 'str',
        'if_op_status': 'str',
        'if_weight': 'int'
    }

    attribute_map = {
        'if_id': 'ifId',
        'if_name': 'ifName',
        'rem_prio': 'remPrio',
        'rem_id': 'remId',
        'if_op_status': 'ifOpStatus',
        'if_weight': 'ifWeight'
    }

    def __init__(self, if_id=None, if_name=None, rem_prio=None, rem_id=None, if_op_status=None, if_weight=None):
        """
        EthTrunkInterfacesDto - a model defined in Swagger
        """

        self._if_id = None
        self._if_name = None
        self._rem_prio = None
        self._rem_id = None
        self._if_op_status = None
        self._if_weight = None

        if if_id is not None:
          self.if_id = if_id
        if if_name is not None:
          self.if_name = if_name
        if rem_prio is not None:
          self.rem_prio = rem_prio
        if rem_id is not None:
          self.rem_id = rem_id
        if if_op_status is not None:
          self.if_op_status = if_op_status
        if if_weight is not None:
          self.if_weight = if_weight

    @property
    def if_id(self):
        """
        Gets the if_id of this EthTrunkInterfacesDto.
        接口ID。

        :return: The if_id of this EthTrunkInterfacesDto.
        :rtype: int
        """
        return self._if_id

    @if_id.setter
    def if_id(self, if_id):
        """
        Sets the if_id of this EthTrunkInterfacesDto.
        接口ID。

        :param if_id: The if_id of this EthTrunkInterfacesDto.
        :type: int
        """

        self._if_id = if_id

    @property
    def if_name(self):
        """
        Gets the if_name of this EthTrunkInterfacesDto.
        接口名称。

        :return: The if_name of this EthTrunkInterfacesDto.
        :rtype: str
        """
        return self._if_name

    @if_name.setter
    def if_name(self, if_name):
        """
        Sets the if_name of this EthTrunkInterfacesDto.
        接口名称。

        :param if_name: The if_name of this EthTrunkInterfacesDto.
        :type: str
        """

        self._if_name = if_name

    @property
    def rem_prio(self):
        """
        Gets the rem_prio of this EthTrunkInterfacesDto.
        远端系统优先级。

        :return: The rem_prio of this EthTrunkInterfacesDto.
        :rtype: int
        """
        return self._rem_prio

    @rem_prio.setter
    def rem_prio(self, rem_prio):
        """
        Sets the rem_prio of this EthTrunkInterfacesDto.
        远端系统优先级。

        :param rem_prio: The rem_prio of this EthTrunkInterfacesDto.
        :type: int
        """

        self._rem_prio = rem_prio

    @property
    def rem_id(self):
        """
        Gets the rem_id of this EthTrunkInterfacesDto.
        远端系统ID。

        :return: The rem_id of this EthTrunkInterfacesDto.
        :rtype: str
        """
        return self._rem_id

    @rem_id.setter
    def rem_id(self, rem_id):
        """
        Sets the rem_id of this EthTrunkInterfacesDto.
        远端系统ID。

        :param rem_id: The rem_id of this EthTrunkInterfacesDto.
        :type: str
        """

        self._rem_id = rem_id

    @property
    def if_op_status(self):
        """
        Gets the if_op_status of this EthTrunkInterfacesDto.
        接口操作状态：up、down。

        :return: The if_op_status of this EthTrunkInterfacesDto.
        :rtype: str
        """
        return self._if_op_status

    @if_op_status.setter
    def if_op_status(self, if_op_status):
        """
        Sets the if_op_status of this EthTrunkInterfacesDto.
        接口操作状态：up、down。

        :param if_op_status: The if_op_status of this EthTrunkInterfacesDto.
        :type: str
        """

        self._if_op_status = if_op_status

    @property
    def if_weight(self):
        """
        Gets the if_weight of this EthTrunkInterfacesDto.
        接口负载的权重。

        :return: The if_weight of this EthTrunkInterfacesDto.
        :rtype: int
        """
        return self._if_weight

    @if_weight.setter
    def if_weight(self, if_weight):
        """
        Sets the if_weight of this EthTrunkInterfacesDto.
        接口负载的权重。

        :param if_weight: The if_weight of this EthTrunkInterfacesDto.
        :type: int
        """

        self._if_weight = if_weight

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
        if not isinstance(other, EthTrunkInterfacesDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
