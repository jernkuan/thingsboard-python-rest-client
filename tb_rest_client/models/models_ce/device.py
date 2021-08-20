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

class Device(object):
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
        'additional_info': 'str',
        'created_time': 'int',
        'customer_id': 'CustomerId',
        'device_data': 'DeviceData',
        'device_profile_id': 'DeviceProfileId',
        'firmware_id': 'OtaPackageId',
        'id': 'DeviceId',
        'label': 'str',
        'name': 'str',
        'software_id': 'OtaPackageId',
        'tenant_id': 'TenantId',
        'type': 'str'
    }

    attribute_map = {
        'additional_info': 'additionalInfo',
        'created_time': 'createdTime',
        'customer_id': 'customerId',
        'device_data': 'deviceData',
        'device_profile_id': 'deviceProfileId',
        'firmware_id': 'firmwareId',
        'id': 'id',
        'label': 'label',
        'name': 'name',
        'software_id': 'softwareId',
        'tenant_id': 'tenantId',
        'type': 'type'
    }

    def __init__(self, additional_info=None, created_time=None, customer_id=None, device_data=None, device_profile_id=None, firmware_id=None, id=None, label=None, name=None, software_id=None, tenant_id=None, type=None):  # noqa: E501
        """Device - a model defined in Swagger"""  # noqa: E501
        self._additional_info = None
        self._created_time = None
        self._customer_id = None
        self._device_data = None
        self._device_profile_id = None
        self._firmware_id = None
        self._id = None
        self._label = None
        self._name = None
        self._software_id = None
        self._tenant_id = None
        self._type = None
        self.discriminator = None
        if additional_info is not None:
            self.additional_info = additional_info
        if created_time is not None:
            self.created_time = created_time
        if customer_id is not None:
            self.customer_id = customer_id
        if device_data is not None:
            self.device_data = device_data
        if device_profile_id is not None:
            self.device_profile_id = device_profile_id
        if firmware_id is not None:
            self.firmware_id = firmware_id
        if id is not None:
            self.id = id
        if label is not None:
            self.label = label
        if name is not None:
            self.name = name
        if software_id is not None:
            self.software_id = software_id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if type is not None:
            self.type = type

    @property
    def additional_info(self):
        """Gets the additional_info of this Device.  # noqa: E501


        :return: The additional_info of this Device.  # noqa: E501
        :rtype: str
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this Device.


        :param additional_info: The additional_info of this Device.  # noqa: E501
        :type: str
        """

        self._additional_info = additional_info

    @property
    def created_time(self):
        """Gets the created_time of this Device.  # noqa: E501


        :return: The created_time of this Device.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this Device.


        :param created_time: The created_time of this Device.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def customer_id(self):
        """Gets the customer_id of this Device.  # noqa: E501


        :return: The customer_id of this Device.  # noqa: E501
        :rtype: CustomerId
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this Device.


        :param customer_id: The customer_id of this Device.  # noqa: E501
        :type: CustomerId
        """

        self._customer_id = customer_id

    @property
    def device_data(self):
        """Gets the device_data of this Device.  # noqa: E501


        :return: The device_data of this Device.  # noqa: E501
        :rtype: DeviceData
        """
        return self._device_data

    @device_data.setter
    def device_data(self, device_data):
        """Sets the device_data of this Device.


        :param device_data: The device_data of this Device.  # noqa: E501
        :type: DeviceData
        """

        self._device_data = device_data

    @property
    def device_profile_id(self):
        """Gets the device_profile_id of this Device.  # noqa: E501


        :return: The device_profile_id of this Device.  # noqa: E501
        :rtype: DeviceProfileId
        """
        return self._device_profile_id

    @device_profile_id.setter
    def device_profile_id(self, device_profile_id):
        """Sets the device_profile_id of this Device.


        :param device_profile_id: The device_profile_id of this Device.  # noqa: E501
        :type: DeviceProfileId
        """

        self._device_profile_id = device_profile_id

    @property
    def firmware_id(self):
        """Gets the firmware_id of this Device.  # noqa: E501


        :return: The firmware_id of this Device.  # noqa: E501
        :rtype: OtaPackageId
        """
        return self._firmware_id

    @firmware_id.setter
    def firmware_id(self, firmware_id):
        """Sets the firmware_id of this Device.


        :param firmware_id: The firmware_id of this Device.  # noqa: E501
        :type: OtaPackageId
        """

        self._firmware_id = firmware_id

    @property
    def id(self):
        """Gets the id of this Device.  # noqa: E501


        :return: The id of this Device.  # noqa: E501
        :rtype: DeviceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Device.


        :param id: The id of this Device.  # noqa: E501
        :type: DeviceId
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this Device.  # noqa: E501


        :return: The label of this Device.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Device.


        :param label: The label of this Device.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def name(self):
        """Gets the name of this Device.  # noqa: E501


        :return: The name of this Device.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Device.


        :param name: The name of this Device.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def software_id(self):
        """Gets the software_id of this Device.  # noqa: E501


        :return: The software_id of this Device.  # noqa: E501
        :rtype: OtaPackageId
        """
        return self._software_id

    @software_id.setter
    def software_id(self, software_id):
        """Sets the software_id of this Device.


        :param software_id: The software_id of this Device.  # noqa: E501
        :type: OtaPackageId
        """

        self._software_id = software_id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this Device.  # noqa: E501


        :return: The tenant_id of this Device.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this Device.


        :param tenant_id: The tenant_id of this Device.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def type(self):
        """Gets the type of this Device.  # noqa: E501


        :return: The type of this Device.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Device.


        :param type: The type of this Device.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(Device, dict):
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
        if not isinstance(other, Device):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
