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


class RoleControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_role_using_delete(self, role_id, **kwargs):  # noqa: E501
        """deleteRole  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_role_using_delete(role_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role_id: roleId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_role_using_delete_with_http_info(role_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_role_using_delete_with_http_info(role_id, **kwargs)  # noqa: E501
            return data

    def delete_role_using_delete_with_http_info(self, role_id, **kwargs):  # noqa: E501
        """deleteRole  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_role_using_delete_with_http_info(role_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role_id: roleId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['role_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_role_using_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'role_id' is set
        if ('role_id' not in params or
                params['role_id'] is None):
            raise ValueError("Missing the required parameter `role_id` when calling `delete_role_using_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'role_id' in params:
            path_params['roleId'] = params['role_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/role/{roleId}', 'DELETE',
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

    def get_role_by_id_using_get(self, role_id, **kwargs):  # noqa: E501
        """getRoleById  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_role_by_id_using_get(role_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role_id: roleId (required)
        :return: Role
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_role_by_id_using_get_with_http_info(role_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_role_by_id_using_get_with_http_info(role_id, **kwargs)  # noqa: E501
            return data

    def get_role_by_id_using_get_with_http_info(self, role_id, **kwargs):  # noqa: E501
        """getRoleById  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_role_by_id_using_get_with_http_info(role_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role_id: roleId (required)
        :return: Role
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['role_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_role_by_id_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'role_id' is set
        if ('role_id' not in params or
                params['role_id'] is None):
            raise ValueError("Missing the required parameter `role_id` when calling `get_role_by_id_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'role_id' in params:
            path_params['roleId'] = params['role_id']  # noqa: E501

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
            '/api/role/{roleId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Role',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_roles_by_ids_using_get(self, role_ids, **kwargs):  # noqa: E501
        """getRolesByIds  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_roles_by_ids_using_get(role_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role_ids: roleIds (required)
        :return: list[Role]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_roles_by_ids_using_get_with_http_info(role_ids, **kwargs)  # noqa: E501
        else:
            (data) = self.get_roles_by_ids_using_get_with_http_info(role_ids, **kwargs)  # noqa: E501
            return data

    def get_roles_by_ids_using_get_with_http_info(self, role_ids, **kwargs):  # noqa: E501
        """getRolesByIds  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_roles_by_ids_using_get_with_http_info(role_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role_ids: roleIds (required)
        :return: list[Role]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['role_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_roles_by_ids_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'role_ids' is set
        if ('role_ids' not in params or
                params['role_ids'] is None):
            raise ValueError("Missing the required parameter `role_ids` when calling `get_roles_by_ids_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'role_ids' in params:
            query_params.append(('roleIds', params['role_ids']))  # noqa: E501

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
            '/api/roles{?roleIds}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Role]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_roles_using_get(self, page_size, page, **kwargs):  # noqa: E501
        """getRoles  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_roles_using_get(page_size, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str page_size: pageSize (required)
        :param str page: page (required)
        :param str type: type
        :param str text_search: textSearch
        :param str sort_property: sortProperty
        :param str sort_order: sortOrder
        :return: PageDataRole
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_roles_using_get_with_http_info(page_size, page, **kwargs)  # noqa: E501
        else:
            (data) = self.get_roles_using_get_with_http_info(page_size, page, **kwargs)  # noqa: E501
            return data

    def get_roles_using_get_with_http_info(self, page_size, page, **kwargs):  # noqa: E501
        """getRoles  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_roles_using_get_with_http_info(page_size, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str page_size: pageSize (required)
        :param str page: page (required)
        :param str type: type
        :param str text_search: textSearch
        :param str sort_property: sortProperty
        :param str sort_order: sortOrder
        :return: PageDataRole
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'page', 'type', 'text_search', 'sort_property', 'sort_order']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_roles_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'page_size' is set
        if ('page_size' not in params or
                params['page_size'] is None):
            raise ValueError("Missing the required parameter `page_size` when calling `get_roles_using_get`")  # noqa: E501
        # verify the required parameter 'page' is set
        if ('page' not in params or
                params['page'] is None):
            raise ValueError("Missing the required parameter `page` when calling `get_roles_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501
        if 'text_search' in params:
            query_params.append(('textSearch', params['text_search']))  # noqa: E501
        if 'sort_property' in params:
            query_params.append(('sortProperty', params['sort_property']))  # noqa: E501
        if 'sort_order' in params:
            query_params.append(('sortOrder', params['sort_order']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

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
            '/api/roles{?type,textSearch,sortProperty,sortOrder,pageSize,page}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageDataRole',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def save_role_using_post(self, body, **kwargs):  # noqa: E501
        """saveRole  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_role_using_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Role body: role (required)
        :return: Role
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.save_role_using_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.save_role_using_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def save_role_using_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """saveRole  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_role_using_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Role body: role (required)
        :return: Role
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method save_role_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `save_role_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

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
            '/api/role', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Role',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
