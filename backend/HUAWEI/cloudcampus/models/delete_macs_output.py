# coding: utf-8

"""
    mac帐号管理

    mac帐号管理

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DeleteMacsOutput(object):
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
        'error_code': 'str',
        'error_message': 'str',
        'delete_name_list': 'list[str]'
    }

    attribute_map = {
        'error_code': 'errorCode',
        'error_message': 'errorMessage',
        'delete_name_list': 'deleteNameList'
    }

    def __init__(self, error_code=None, error_message=None, delete_name_list=None):
        """
        DeleteMacsOutput - a model defined in Swagger
        """

        self._error_code = None
        self._error_message = None
        self._delete_name_list = None

        if error_code is not None:
          self.error_code = error_code
        if error_message is not None:
          self.error_message = error_message
        if delete_name_list is not None:
          self.delete_name_list = delete_name_list

    @property
    def error_code(self):
        """
        Gets the error_code of this DeleteMacsOutput.
        错误码。

        :return: The error_code of this DeleteMacsOutput.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """
        Sets the error_code of this DeleteMacsOutput.
        错误码。

        :param error_code: The error_code of this DeleteMacsOutput.
        :type: str
        """

        self._error_code = error_code

    @property
    def error_message(self):
        """
        Gets the error_message of this DeleteMacsOutput.
        错误信息。

        :return: The error_message of this DeleteMacsOutput.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this DeleteMacsOutput.
        错误信息。

        :param error_message: The error_message of this DeleteMacsOutput.
        :type: str
        """

        self._error_message = error_message

    @property
    def delete_name_list(self):
        """
        Gets the delete_name_list of this DeleteMacsOutput.
        成功删除mac账号名称列表。

        :return: The delete_name_list of this DeleteMacsOutput.
        :rtype: list[str]
        """
        return self._delete_name_list

    @delete_name_list.setter
    def delete_name_list(self, delete_name_list):
        """
        Sets the delete_name_list of this DeleteMacsOutput.
        成功删除mac账号名称列表。

        :param delete_name_list: The delete_name_list of this DeleteMacsOutput.
        :type: list[str]
        """

        self._delete_name_list = delete_name_list

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
        if not isinstance(other, DeleteMacsOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
