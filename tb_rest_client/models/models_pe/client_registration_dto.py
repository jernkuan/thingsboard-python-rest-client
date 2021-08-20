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

class ClientRegistrationDto(object):
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
        'access_token_uri': 'str',
        'additional_info': 'str',
        'authorization_uri': 'str',
        'client_authentication_method': 'str',
        'client_id': 'str',
        'client_secret': 'str',
        'jwk_set_uri': 'str',
        'login_button_icon': 'str',
        'login_button_label': 'str',
        'mapper_config': 'OAuth2MapperConfig',
        'scope': 'list[str]',
        'user_info_uri': 'str',
        'user_name_attribute_name': 'str'
    }

    attribute_map = {
        'access_token_uri': 'accessTokenUri',
        'additional_info': 'additionalInfo',
        'authorization_uri': 'authorizationUri',
        'client_authentication_method': 'clientAuthenticationMethod',
        'client_id': 'clientId',
        'client_secret': 'clientSecret',
        'jwk_set_uri': 'jwkSetUri',
        'login_button_icon': 'loginButtonIcon',
        'login_button_label': 'loginButtonLabel',
        'mapper_config': 'mapperConfig',
        'scope': 'scope',
        'user_info_uri': 'userInfoUri',
        'user_name_attribute_name': 'userNameAttributeName'
    }

    def __init__(self, access_token_uri=None, additional_info=None, authorization_uri=None, client_authentication_method=None, client_id=None, client_secret=None, jwk_set_uri=None, login_button_icon=None, login_button_label=None, mapper_config=None, scope=None, user_info_uri=None, user_name_attribute_name=None):  # noqa: E501
        """ClientRegistrationDto - a model defined in Swagger"""  # noqa: E501
        self._access_token_uri = None
        self._additional_info = None
        self._authorization_uri = None
        self._client_authentication_method = None
        self._client_id = None
        self._client_secret = None
        self._jwk_set_uri = None
        self._login_button_icon = None
        self._login_button_label = None
        self._mapper_config = None
        self._scope = None
        self._user_info_uri = None
        self._user_name_attribute_name = None
        self.discriminator = None
        if access_token_uri is not None:
            self.access_token_uri = access_token_uri
        if additional_info is not None:
            self.additional_info = additional_info
        if authorization_uri is not None:
            self.authorization_uri = authorization_uri
        if client_authentication_method is not None:
            self.client_authentication_method = client_authentication_method
        if client_id is not None:
            self.client_id = client_id
        if client_secret is not None:
            self.client_secret = client_secret
        if jwk_set_uri is not None:
            self.jwk_set_uri = jwk_set_uri
        if login_button_icon is not None:
            self.login_button_icon = login_button_icon
        if login_button_label is not None:
            self.login_button_label = login_button_label
        if mapper_config is not None:
            self.mapper_config = mapper_config
        if scope is not None:
            self.scope = scope
        if user_info_uri is not None:
            self.user_info_uri = user_info_uri
        if user_name_attribute_name is not None:
            self.user_name_attribute_name = user_name_attribute_name

    @property
    def access_token_uri(self):
        """Gets the access_token_uri of this ClientRegistrationDto.  # noqa: E501


        :return: The access_token_uri of this ClientRegistrationDto.  # noqa: E501
        :rtype: str
        """
        return self._access_token_uri

    @access_token_uri.setter
    def access_token_uri(self, access_token_uri):
        """Sets the access_token_uri of this ClientRegistrationDto.


        :param access_token_uri: The access_token_uri of this ClientRegistrationDto.  # noqa: E501
        :type: str
        """

        self._access_token_uri = access_token_uri

    @property
    def additional_info(self):
        """Gets the additional_info of this ClientRegistrationDto.  # noqa: E501


        :return: The additional_info of this ClientRegistrationDto.  # noqa: E501
        :rtype: str
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this ClientRegistrationDto.


        :param additional_info: The additional_info of this ClientRegistrationDto.  # noqa: E501
        :type: str
        """

        self._additional_info = additional_info

    @property
    def authorization_uri(self):
        """Gets the authorization_uri of this ClientRegistrationDto.  # noqa: E501


        :return: The authorization_uri of this ClientRegistrationDto.  # noqa: E501
        :rtype: str
        """
        return self._authorization_uri

    @authorization_uri.setter
    def authorization_uri(self, authorization_uri):
        """Sets the authorization_uri of this ClientRegistrationDto.


        :param authorization_uri: The authorization_uri of this ClientRegistrationDto.  # noqa: E501
        :type: str
        """

        self._authorization_uri = authorization_uri

    @property
    def client_authentication_method(self):
        """Gets the client_authentication_method of this ClientRegistrationDto.  # noqa: E501


        :return: The client_authentication_method of this ClientRegistrationDto.  # noqa: E501
        :rtype: str
        """
        return self._client_authentication_method

    @client_authentication_method.setter
    def client_authentication_method(self, client_authentication_method):
        """Sets the client_authentication_method of this ClientRegistrationDto.


        :param client_authentication_method: The client_authentication_method of this ClientRegistrationDto.  # noqa: E501
        :type: str
        """

        self._client_authentication_method = client_authentication_method

    @property
    def client_id(self):
        """Gets the client_id of this ClientRegistrationDto.  # noqa: E501


        :return: The client_id of this ClientRegistrationDto.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this ClientRegistrationDto.


        :param client_id: The client_id of this ClientRegistrationDto.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def client_secret(self):
        """Gets the client_secret of this ClientRegistrationDto.  # noqa: E501


        :return: The client_secret of this ClientRegistrationDto.  # noqa: E501
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """Sets the client_secret of this ClientRegistrationDto.


        :param client_secret: The client_secret of this ClientRegistrationDto.  # noqa: E501
        :type: str
        """

        self._client_secret = client_secret

    @property
    def jwk_set_uri(self):
        """Gets the jwk_set_uri of this ClientRegistrationDto.  # noqa: E501


        :return: The jwk_set_uri of this ClientRegistrationDto.  # noqa: E501
        :rtype: str
        """
        return self._jwk_set_uri

    @jwk_set_uri.setter
    def jwk_set_uri(self, jwk_set_uri):
        """Sets the jwk_set_uri of this ClientRegistrationDto.


        :param jwk_set_uri: The jwk_set_uri of this ClientRegistrationDto.  # noqa: E501
        :type: str
        """

        self._jwk_set_uri = jwk_set_uri

    @property
    def login_button_icon(self):
        """Gets the login_button_icon of this ClientRegistrationDto.  # noqa: E501


        :return: The login_button_icon of this ClientRegistrationDto.  # noqa: E501
        :rtype: str
        """
        return self._login_button_icon

    @login_button_icon.setter
    def login_button_icon(self, login_button_icon):
        """Sets the login_button_icon of this ClientRegistrationDto.


        :param login_button_icon: The login_button_icon of this ClientRegistrationDto.  # noqa: E501
        :type: str
        """

        self._login_button_icon = login_button_icon

    @property
    def login_button_label(self):
        """Gets the login_button_label of this ClientRegistrationDto.  # noqa: E501


        :return: The login_button_label of this ClientRegistrationDto.  # noqa: E501
        :rtype: str
        """
        return self._login_button_label

    @login_button_label.setter
    def login_button_label(self, login_button_label):
        """Sets the login_button_label of this ClientRegistrationDto.


        :param login_button_label: The login_button_label of this ClientRegistrationDto.  # noqa: E501
        :type: str
        """

        self._login_button_label = login_button_label

    @property
    def mapper_config(self):
        """Gets the mapper_config of this ClientRegistrationDto.  # noqa: E501


        :return: The mapper_config of this ClientRegistrationDto.  # noqa: E501
        :rtype: OAuth2MapperConfig
        """
        return self._mapper_config

    @mapper_config.setter
    def mapper_config(self, mapper_config):
        """Sets the mapper_config of this ClientRegistrationDto.


        :param mapper_config: The mapper_config of this ClientRegistrationDto.  # noqa: E501
        :type: OAuth2MapperConfig
        """

        self._mapper_config = mapper_config

    @property
    def scope(self):
        """Gets the scope of this ClientRegistrationDto.  # noqa: E501


        :return: The scope of this ClientRegistrationDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this ClientRegistrationDto.


        :param scope: The scope of this ClientRegistrationDto.  # noqa: E501
        :type: list[str]
        """

        self._scope = scope

    @property
    def user_info_uri(self):
        """Gets the user_info_uri of this ClientRegistrationDto.  # noqa: E501


        :return: The user_info_uri of this ClientRegistrationDto.  # noqa: E501
        :rtype: str
        """
        return self._user_info_uri

    @user_info_uri.setter
    def user_info_uri(self, user_info_uri):
        """Sets the user_info_uri of this ClientRegistrationDto.


        :param user_info_uri: The user_info_uri of this ClientRegistrationDto.  # noqa: E501
        :type: str
        """

        self._user_info_uri = user_info_uri

    @property
    def user_name_attribute_name(self):
        """Gets the user_name_attribute_name of this ClientRegistrationDto.  # noqa: E501


        :return: The user_name_attribute_name of this ClientRegistrationDto.  # noqa: E501
        :rtype: str
        """
        return self._user_name_attribute_name

    @user_name_attribute_name.setter
    def user_name_attribute_name(self, user_name_attribute_name):
        """Sets the user_name_attribute_name of this ClientRegistrationDto.


        :param user_name_attribute_name: The user_name_attribute_name of this ClientRegistrationDto.  # noqa: E501
        :type: str
        """

        self._user_name_attribute_name = user_name_attribute_name

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
        if issubclass(ClientRegistrationDto, dict):
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
        if not isinstance(other, ClientRegistrationDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
