from pprint import pformat

from six import iteritems


class TokenDtoWrapper(object):
    """
    This class is body for token.
    Create by author.
    """

    def __init__(self, errmsg=None, errcode=None, data=None, status=None, HTTPHeaderDict=None):
        """
        TokenDtoWrapper - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'errmsg': 'str',
            'errcode': 'str',
            'data': 'TokenDto',
            # 'status':'status',
            # 'HTTPHeaderDict': 'HTTPHeaderDictDto'
        }

        self.attribute_map = {
            'errmsg': 'errmsg',
            'errcode': 'errcode',
            'data': 'data',
            # 'status':'status',
            # 'HTTPHeaderDict': 'HTTPHeaderDict'
        }

        self._errmsg = errmsg
        self._errcode = errcode
        self._data = data
        # self._status = status
        # self._HTTPHeaderDict = HTTPHeaderDict

    @property
    def errmsg(self):
        """
        :return: The errmsg of this TokenDtoWrapper.
        :rtype: str
        """
        return self._errmsg

    @errmsg.setter
    def errmsg(self, errmsg):
        """
        :return: The errmsg of this TokenDtoWrapper.
        :rtype: str
        """
        if errmsg is None:
            raise ValueError("Invalid value for 'errmsg', must not be `None`")

        self._errmsg = errmsg

    @property
    def errcode(self):
        """
        :return: The errmsg of this TokenDtoWrapper.
        :rtype: str
        """
        return self._errcode

    @errcode.setter
    def errcode(self, errcode):
        """
        :return: The errcode of this TokenDtoWrapper.
        :rtype: str
        """
        if errcode is None:
            raise ValueError("Invalid value for 'errcode', must not be `None`")

        self._errcode = errcode

    # @property
    # def status(self):
    #     """
    #     :return: The data of this TokenDtoWrapper.
    #     :rtype: str
    #     """
    #     return self._status
    #
    # @status.setter
    # def status(self, status):
    #     """
    #     :return: The errcode of this TokenDtoWrapper.
    #     :rtype: str
    #     """
    #     # if data is None:
    #     #     raise ValueError("Invalid value for 'data', must not be `None`")
    #
    #     self._status = status
    #
    # @property
    # def HTTPHeaderDict(self):
    #     """
    #     :return: The data of this TokenDtoWrapper.
    #     :rtype: str
    #     """
    #     return self._HTTPHeaderDict
    #
    # @HTTPHeaderDict.setter
    # def HTTPHeaderDict(self, HTTPHeaderDict):
    #     """
    #     :return: The errcode of this TokenDtoWrapper.
    #     :rtype: str
    #     """
    #     # if HTTPHeaderDict is None:
    #     #     raise ValueError("Invalid value for 'data', must not be `None`")
    #
    #     self._HTTPHeaderDict = HTTPHeaderDict

    @property
    def data(self):
        """
        :return: The data of this TokenDtoWrapper.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        :return: The errcode of this TokenDtoWrapper.
        :rtype: str
        """
        if data is None:
            raise ValueError("Invalid value for 'data', must not be `None`")

        self._data = data

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
        if not isinstance(other, TokenDtoWrapper):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

        # def __getitem__(self):
        #      return self.data
