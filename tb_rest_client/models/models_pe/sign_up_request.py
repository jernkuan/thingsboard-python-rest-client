# coding: utf-8

"""
    ThingsBoard REST API

    For instructions how to authorize requests please visit <a href='http://thingsboard.io/docs/reference/rest-api/'>REST API documentation page</a>.  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SignUpRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'app_secret': 'str',
        'email': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'password': 'str',
        'pkg_name': 'str',
        'recaptcha_response': 'str'
    }

    attribute_map = {
        'app_secret': 'appSecret',
        'email': 'email',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'password': 'password',
        'pkg_name': 'pkgName',
        'recaptcha_response': 'recaptchaResponse'
    }

    def __init__(self, app_secret=None, email=None, first_name=None, last_name=None, password=None, pkg_name=None, recaptcha_response=None):  # noqa: E501
        """SignUpRequest - a model defined in Swagger"""  # noqa: E501
        self._app_secret = None
        self._email = None
        self._first_name = None
        self._last_name = None
        self._password = None
        self._pkg_name = None
        self._recaptcha_response = None
        self.discriminator = None
        if app_secret is not None:
            self.app_secret = app_secret
        if email is not None:
            self.email = email
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if password is not None:
            self.password = password
        if pkg_name is not None:
            self.pkg_name = pkg_name
        if recaptcha_response is not None:
            self.recaptcha_response = recaptcha_response

    @property
    def app_secret(self):
        """Gets the app_secret of this SignUpRequest.  # noqa: E501


        :return: The app_secret of this SignUpRequest.  # noqa: E501
        :rtype: str
        """
        return self._app_secret

    @app_secret.setter
    def app_secret(self, app_secret):
        """Sets the app_secret of this SignUpRequest.


        :param app_secret: The app_secret of this SignUpRequest.  # noqa: E501
        :type: str
        """

        self._app_secret = app_secret

    @property
    def email(self):
        """Gets the email of this SignUpRequest.  # noqa: E501


        :return: The email of this SignUpRequest.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this SignUpRequest.


        :param email: The email of this SignUpRequest.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this SignUpRequest.  # noqa: E501


        :return: The first_name of this SignUpRequest.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this SignUpRequest.


        :param first_name: The first_name of this SignUpRequest.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this SignUpRequest.  # noqa: E501


        :return: The last_name of this SignUpRequest.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this SignUpRequest.


        :param last_name: The last_name of this SignUpRequest.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def password(self):
        """Gets the password of this SignUpRequest.  # noqa: E501


        :return: The password of this SignUpRequest.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this SignUpRequest.


        :param password: The password of this SignUpRequest.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def pkg_name(self):
        """Gets the pkg_name of this SignUpRequest.  # noqa: E501


        :return: The pkg_name of this SignUpRequest.  # noqa: E501
        :rtype: str
        """
        return self._pkg_name

    @pkg_name.setter
    def pkg_name(self, pkg_name):
        """Sets the pkg_name of this SignUpRequest.


        :param pkg_name: The pkg_name of this SignUpRequest.  # noqa: E501
        :type: str
        """

        self._pkg_name = pkg_name

    @property
    def recaptcha_response(self):
        """Gets the recaptcha_response of this SignUpRequest.  # noqa: E501


        :return: The recaptcha_response of this SignUpRequest.  # noqa: E501
        :rtype: str
        """
        return self._recaptcha_response

    @recaptcha_response.setter
    def recaptcha_response(self, recaptcha_response):
        """Sets the recaptcha_response of this SignUpRequest.


        :param recaptcha_response: The recaptcha_response of this SignUpRequest.  # noqa: E501
        :type: str
        """

        self._recaptcha_response = recaptcha_response

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(SignUpRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SignUpRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
