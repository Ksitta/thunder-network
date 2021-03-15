from pprint import pformat

from six import iteritems


class TokenDto(object):
    """
    This class is body data for token.
    Create by author.
    """

    def __init__(self, expiredDate=None, token_id=None):
        """
        TokenDto - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'expiredDate': 'str',
            'token_id': 'str'
        }

        self.attribute_map = {
            'expiredDate': 'expiredDate',
            'token_id': 'token_id'
        }

        self._expiredDate = expiredDate
        self._token_id = token_id

    def tokedto(self):
        return self._token_id

    @property
    def expiredDate(self):
        """
        :return: The errmsg of this TokenDto.
        :rtype: str
        """
        return self._expiredDate

    @expiredDate.setter
    def expiredDate(self, expiredDate):
        """
        :return: The errmsg of this TokenDto.
        :rtype: str
        """
        if expiredDate is None:
            raise ValueError("Invalid value for 'expiredDate', must not be `None`")

        self._expiredDate = expiredDate

    @property
    def token_id(self):
        """
        :return: The errmsg of this TokenDto.
        :rtype: str
        """
        return self._token_id

    @token_id.setter
    def token_id(self, token_id):
        """
        :return: The errmsg of this TokenDto.
        :rtype: str
        """
        if token_id is None:
            raise ValueError("Invalid value for 'token_id', must not be `None`")

        self._token_id = token_id

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
        if not isinstance(other, TokenDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

        # def __getitem__(self):
        #      return self.token_id
