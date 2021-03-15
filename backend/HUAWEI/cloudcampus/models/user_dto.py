# coding: utf-8

"""
    用户管理

    用户管理第三方北向接口。 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UserDto(object):
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
        'user_group_id': 'str',
        'user_name': 'str',
        'password': 'str',
        'user_type': 'int',
        'modify_date': 'str',
        'vaild_period': 'str',
        'email': 'str',
        'telephone': 'str',
        'path': 'str',
        'time_flag': 'str',
        'next_update_userpass': 'bool',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'user_group_id': 'userGroupId',
        'user_name': 'userName',
        'password': 'password',
        'user_type': 'userType',
        'modify_date': 'modifyDate',
        'vaild_period': 'vaildPeriod',
        'email': 'email',
        'telephone': 'telephone',
        'path': 'path',
        'time_flag': 'timeFlag',
        'next_update_userpass': 'nextUpdateUserpass',
        'description': 'description'
    }

    def __init__(self, id=None, user_group_id=None, user_name=None, password=None, user_type=None, modify_date=None, vaild_period=None, email=None, telephone=None, path=None, time_flag=None, next_update_userpass=None, description=None):
        """
        UserDto - a model defined in Swagger
        """

        self._id = None
        self._user_group_id = None
        self._user_name = None
        self._password = None
        self._user_type = None
        self._modify_date = None
        self._vaild_period = None
        self._email = None
        self._telephone = None
        self._path = None
        self._time_flag = None
        self._next_update_userpass = None
        self._description = None

        if id is not None:
          self.id = id
        if user_group_id is not None:
          self.user_group_id = user_group_id
        if user_name is not None:
          self.user_name = user_name
        if password is not None:
          self.password = password
        if user_type is not None:
          self.user_type = user_type
        if modify_date is not None:
          self.modify_date = modify_date
        if vaild_period is not None:
          self.vaild_period = vaild_period
        if email is not None:
          self.email = email
        if telephone is not None:
          self.telephone = telephone
        if path is not None:
          self.path = path
        if time_flag is not None:
          self.time_flag = time_flag
        if next_update_userpass is not None:
          self.next_update_userpass = next_update_userpass
        if description is not None:
          self.description = description

    @property
    def id(self):
        """
        Gets the id of this UserDto.
        用户ID。

        :return: The id of this UserDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UserDto.
        用户ID。

        :param id: The id of this UserDto.
        :type: str
        """

        self._id = id

    @property
    def user_group_id(self):
        """
        Gets the user_group_id of this UserDto.
        用户组ID。

        :return: The user_group_id of this UserDto.
        :rtype: str
        """
        return self._user_group_id

    @user_group_id.setter
    def user_group_id(self, user_group_id):
        """
        Sets the user_group_id of this UserDto.
        用户组ID。

        :param user_group_id: The user_group_id of this UserDto.
        :type: str
        """

        self._user_group_id = user_group_id

    @property
    def user_name(self):
        """
        Gets the user_name of this UserDto.
        用户名。

        :return: The user_name of this UserDto.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this UserDto.
        用户名。

        :param user_name: The user_name of this UserDto.
        :type: str
        """

        self._user_name = user_name

    @property
    def password(self):
        """
        Gets the password of this UserDto.
        密码密文。

        :return: The password of this UserDto.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this UserDto.
        密码密文。

        :param password: The password of this UserDto.
        :type: str
        """

        self._password = password

    @property
    def user_type(self):
        """
        Gets the user_type of this UserDto.
        用户类型。

        :return: The user_type of this UserDto.
        :rtype: int
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        """
        Sets the user_type of this UserDto.
        用户类型。

        :param user_type: The user_type of this UserDto.
        :type: int
        """
        if user_type is not None and user_type > 64:
            raise ValueError("Invalid value for `user_type`, must be a value less than or equal to `64`")
        if user_type is not None and user_type < 0:
            raise ValueError("Invalid value for `user_type`, must be a value greater than or equal to `0`")

        self._user_type = user_type

    @property
    def modify_date(self):
        """
        Gets the modify_date of this UserDto.
        账号创建时间。

        :return: The modify_date of this UserDto.
        :rtype: str
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """
        Sets the modify_date of this UserDto.
        账号创建时间。

        :param modify_date: The modify_date of this UserDto.
        :type: str
        """

        self._modify_date = modify_date

    @property
    def vaild_period(self):
        """
        Gets the vaild_period of this UserDto.
        过期时间。

        :return: The vaild_period of this UserDto.
        :rtype: str
        """
        return self._vaild_period

    @vaild_period.setter
    def vaild_period(self, vaild_period):
        """
        Sets the vaild_period of this UserDto.
        过期时间。

        :param vaild_period: The vaild_period of this UserDto.
        :type: str
        """

        self._vaild_period = vaild_period

    @property
    def email(self):
        """
        Gets the email of this UserDto.
        邮箱。

        :return: The email of this UserDto.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this UserDto.
        邮箱。

        :param email: The email of this UserDto.
        :type: str
        """

        self._email = email

    @property
    def telephone(self):
        """
        Gets the telephone of this UserDto.
        联系电话。

        :return: The telephone of this UserDto.
        :rtype: str
        """
        return self._telephone

    @telephone.setter
    def telephone(self, telephone):
        """
        Sets the telephone of this UserDto.
        联系电话。

        :param telephone: The telephone of this UserDto.
        :type: str
        """

        self._telephone = telephone

    @property
    def path(self):
        """
        Gets the path of this UserDto.
        用户组全路径。

        :return: The path of this UserDto.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this UserDto.
        用户组全路径。

        :param path: The path of this UserDto.
        :type: str
        """

        self._path = path

    @property
    def time_flag(self):
        """
        Gets the time_flag of this UserDto.
        用户过期判断。

        :return: The time_flag of this UserDto.
        :rtype: str
        """
        return self._time_flag

    @time_flag.setter
    def time_flag(self, time_flag):
        """
        Sets the time_flag of this UserDto.
        用户过期判断。

        :param time_flag: The time_flag of this UserDto.
        :type: str
        """

        self._time_flag = time_flag

    @property
    def next_update_userpass(self):
        """
        Gets the next_update_userpass of this UserDto.
        下次登录修改密码。

        :return: The next_update_userpass of this UserDto.
        :rtype: bool
        """
        return self._next_update_userpass

    @next_update_userpass.setter
    def next_update_userpass(self, next_update_userpass):
        """
        Sets the next_update_userpass of this UserDto.
        下次登录修改密码。

        :param next_update_userpass: The next_update_userpass of this UserDto.
        :type: bool
        """

        self._next_update_userpass = next_update_userpass

    @property
    def description(self):
        """
        Gets the description of this UserDto.
        描述。

        :return: The description of this UserDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UserDto.
        描述。

        :param description: The description of this UserDto.
        :type: str
        """

        self._description = description

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
        if not isinstance(other, UserDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
