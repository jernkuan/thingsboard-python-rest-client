# coding: utf-8

"""
    ThingsBoard REST API

    For instructions how to authorize requests please visit <a href='http://thingsboard.io/docs/reference/rest-api/'>REST API documentation page</a>.  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from tb_rest_client.api_client import ApiClient


class RpcV2ControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_resource_using_delete(self, rpc_id, **kwargs):  # noqa: E501
        """deleteResource  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_resource_using_delete(rpc_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str rpc_id: rpcId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_resource_using_delete_with_http_info(rpc_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_resource_using_delete_with_http_info(rpc_id, **kwargs)  # noqa: E501
            return data

    def delete_resource_using_delete_with_http_info(self, rpc_id, **kwargs):  # noqa: E501
        """deleteResource  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_resource_using_delete_with_http_info(rpc_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str rpc_id: rpcId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['rpc_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_resource_using_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'rpc_id' is set
        if ('rpc_id' not in params or
                params['rpc_id'] is None):
            raise ValueError("Missing the required parameter `rpc_id` when calling `delete_resource_using_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'rpc_id' in params:
            path_params['rpcId'] = params['rpc_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/rpc/persistent/{rpcId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_persisted_rpc_by_device_using_get(self, device_id, page_size, page, rpc_status, **kwargs):  # noqa: E501
        """getPersistedRpcByDevice  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_persisted_rpc_by_device_using_get(device_id, page_size, page, rpc_status, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_id: deviceId (required)
        :param int page_size: pageSize (required)
        :param int page: page (required)
        :param str rpc_status: rpcStatus (required)
        :param str text_search: textSearch
        :param str sort_property: sortProperty
        :param str sort_order: sortOrder
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_persisted_rpc_by_device_using_get_with_http_info(device_id, page_size, page, rpc_status, **kwargs)  # noqa: E501
        else:
            (data) = self.get_persisted_rpc_by_device_using_get_with_http_info(device_id, page_size, page, rpc_status, **kwargs)  # noqa: E501
            return data

    def get_persisted_rpc_by_device_using_get_with_http_info(self, device_id, page_size, page, rpc_status, **kwargs):  # noqa: E501
        """getPersistedRpcByDevice  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_persisted_rpc_by_device_using_get_with_http_info(device_id, page_size, page, rpc_status, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_id: deviceId (required)
        :param int page_size: pageSize (required)
        :param int page: page (required)
        :param str rpc_status: rpcStatus (required)
        :param str text_search: textSearch
        :param str sort_property: sortProperty
        :param str sort_order: sortOrder
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_id', 'page_size', 'page', 'rpc_status', 'text_search', 'sort_property', 'sort_order']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_persisted_rpc_by_device_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params or
                params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `get_persisted_rpc_by_device_using_get`")  # noqa: E501
        # verify the required parameter 'page_size' is set
        if ('page_size' not in params or
                params['page_size'] is None):
            raise ValueError("Missing the required parameter `page_size` when calling `get_persisted_rpc_by_device_using_get`")  # noqa: E501
        # verify the required parameter 'page' is set
        if ('page' not in params or
                params['page'] is None):
            raise ValueError("Missing the required parameter `page` when calling `get_persisted_rpc_by_device_using_get`")  # noqa: E501
        # verify the required parameter 'rpc_status' is set
        if ('rpc_status' not in params or
                params['rpc_status'] is None):
            raise ValueError("Missing the required parameter `rpc_status` when calling `get_persisted_rpc_by_device_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'device_id' in params:
            path_params['deviceId'] = params['device_id']  # noqa: E501

        query_params = []
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'rpc_status' in params:
            query_params.append(('rpcStatus', params['rpc_status']))  # noqa: E501
        if 'text_search' in params:
            query_params.append(('textSearch', params['text_search']))  # noqa: E501
        if 'sort_property' in params:
            query_params.append(('sortProperty', params['sort_property']))  # noqa: E501
        if 'sort_order' in params:
            query_params.append(('sortOrder', params['sort_order']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/rpc/persistent/device/{deviceId}{?pageSize,page,rpcStatus,textSearch,sortProperty,sortOrder}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeferredResultResponseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_persisted_rpc_using_get(self, rpc_id, **kwargs):  # noqa: E501
        """getPersistedRpc  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_persisted_rpc_using_get(rpc_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str rpc_id: rpcId (required)
        :return: Rpc
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_persisted_rpc_using_get_with_http_info(rpc_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_persisted_rpc_using_get_with_http_info(rpc_id, **kwargs)  # noqa: E501
            return data

    def get_persisted_rpc_using_get_with_http_info(self, rpc_id, **kwargs):  # noqa: E501
        """getPersistedRpc  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_persisted_rpc_using_get_with_http_info(rpc_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str rpc_id: rpcId (required)
        :return: Rpc
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['rpc_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_persisted_rpc_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'rpc_id' is set
        if ('rpc_id' not in params or
                params['rpc_id'] is None):
            raise ValueError("Missing the required parameter `rpc_id` when calling `get_persisted_rpc_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'rpc_id' in params:
            path_params['rpcId'] = params['rpc_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/rpc/persistent/{rpcId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Rpc',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def handle_one_way_device_rpc_request_using_post1(self, body, device_id, **kwargs):  # noqa: E501
        """handleOneWayDeviceRPCRequest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.handle_one_way_device_rpc_request_using_post1(body, device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: requestBody (required)
        :param str device_id: deviceId (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.handle_one_way_device_rpc_request_using_post1_with_http_info(body, device_id, **kwargs)  # noqa: E501
        else:
            (data) = self.handle_one_way_device_rpc_request_using_post1_with_http_info(body, device_id, **kwargs)  # noqa: E501
            return data

    def handle_one_way_device_rpc_request_using_post1_with_http_info(self, body, device_id, **kwargs):  # noqa: E501
        """handleOneWayDeviceRPCRequest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.handle_one_way_device_rpc_request_using_post1_with_http_info(body, device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: requestBody (required)
        :param str device_id: deviceId (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'device_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method handle_one_way_device_rpc_request_using_post1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `handle_one_way_device_rpc_request_using_post1`")  # noqa: E501
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params or
                params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `handle_one_way_device_rpc_request_using_post1`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'device_id' in params:
            path_params['deviceId'] = params['device_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/rpc/oneway/{deviceId}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeferredResultResponseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def handle_two_way_device_rpc_request_using_post1(self, body, device_id, **kwargs):  # noqa: E501
        """handleTwoWayDeviceRPCRequest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.handle_two_way_device_rpc_request_using_post1(body, device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: requestBody (required)
        :param str device_id: deviceId (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.handle_two_way_device_rpc_request_using_post1_with_http_info(body, device_id, **kwargs)  # noqa: E501
        else:
            (data) = self.handle_two_way_device_rpc_request_using_post1_with_http_info(body, device_id, **kwargs)  # noqa: E501
            return data

    def handle_two_way_device_rpc_request_using_post1_with_http_info(self, body, device_id, **kwargs):  # noqa: E501
        """handleTwoWayDeviceRPCRequest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.handle_two_way_device_rpc_request_using_post1_with_http_info(body, device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: requestBody (required)
        :param str device_id: deviceId (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'device_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method handle_two_way_device_rpc_request_using_post1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `handle_two_way_device_rpc_request_using_post1`")  # noqa: E501
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params or
                params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `handle_two_way_device_rpc_request_using_post1`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'device_id' in params:
            path_params['deviceId'] = params['device_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/rpc/twoway/{deviceId}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeferredResultResponseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
