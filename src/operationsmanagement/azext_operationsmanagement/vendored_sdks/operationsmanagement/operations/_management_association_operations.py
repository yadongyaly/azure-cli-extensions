# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class ManagementAssociationOperations(object):
    """ManagementAssociationOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.operationsmanagement.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list_by_subscription(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ManagementAssociationPropertiesList"
        """Retrieves the ManagementAssociations list.

        Retrieves the ManagementAssociations list for the subscription.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ManagementAssociationPropertiesList or the result of cls(response)
        :rtype: ~azure.mgmt.operationsmanagement.models.ManagementAssociationPropertiesList
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ManagementAssociationPropertiesList"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2015-11-01-preview"

        # Construct URL
        url = self.list_by_subscription.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.CodeMessageError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ManagementAssociationPropertiesList', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    list_by_subscription.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.OperationsManagement/ManagementAssociations'}

    def create_or_update(
        self,
        resource_group_name,  # type: str
        provider_name,  # type: str
        resource_type,  # type: str
        resource_name,  # type: str
        management_association_name,  # type: str
        location=None,  # type: Optional[str]
        properties=None,  # type: Optional["models.ManagementAssociationProperties"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ManagementAssociation"
        """Creates or updates the ManagementAssociation.

        Create/Update ManagementAssociation.

        :param resource_group_name: The name of the resource group to get. The name is case
         insensitive.
        :type resource_group_name: str
        :param provider_name: Provider name for the parent resource.
        :type provider_name: str
        :param resource_type: Resource type for the parent resource.
        :type resource_type: str
        :param resource_name: Parent resource name.
        :type resource_name: str
        :param management_association_name: User ManagementAssociation Name.
        :type management_association_name: str
        :param location: Resource location.
        :type location: str
        :param properties: Properties for ManagementAssociation object supported by the
         OperationsManagement resource provider.
        :type properties: ~azure.mgmt.operationsmanagement.models.ManagementAssociationProperties
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ManagementAssociation or the result of cls(response)
        :rtype: ~azure.mgmt.operationsmanagement.models.ManagementAssociation
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ManagementAssociation"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})

        _parameters = models.ManagementAssociation(location=location, properties=properties)
        api_version = "2015-11-01-preview"

        # Construct URL
        url = self.create_or_update.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'providerName': self._serialize.url("provider_name", provider_name, 'str'),
            'resourceType': self._serialize.url("resource_type", resource_type, 'str'),
            'resourceName': self._serialize.url("resource_name", resource_name, 'str'),
            'managementAssociationName': self._serialize.url("management_association_name", management_association_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = kwargs.pop('content_type', 'application/json')

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_parameters, 'ManagementAssociation')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.CodeMessageError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ManagementAssociation', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{providerName}/{resourceType}/{resourceName}/providers/Microsoft.OperationsManagement/ManagementAssociations/{managementAssociationName}'}

    def delete(
        self,
        resource_group_name,  # type: str
        provider_name,  # type: str
        resource_type,  # type: str
        resource_name,  # type: str
        management_association_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Deletes the ManagementAssociation in the subscription.

        Deletes the ManagementAssociation.

        :param resource_group_name: The name of the resource group to get. The name is case
         insensitive.
        :type resource_group_name: str
        :param provider_name: Provider name for the parent resource.
        :type provider_name: str
        :param resource_type: Resource type for the parent resource.
        :type resource_type: str
        :param resource_name: Parent resource name.
        :type resource_name: str
        :param management_association_name: User ManagementAssociation Name.
        :type management_association_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2015-11-01-preview"

        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'providerName': self._serialize.url("provider_name", provider_name, 'str'),
            'resourceType': self._serialize.url("resource_type", resource_type, 'str'),
            'resourceName': self._serialize.url("resource_name", resource_name, 'str'),
            'managementAssociationName': self._serialize.url("management_association_name", management_association_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.CodeMessageError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
          return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{providerName}/{resourceType}/{resourceName}/providers/Microsoft.OperationsManagement/ManagementAssociations/{managementAssociationName}'}

    def get(
        self,
        resource_group_name,  # type: str
        provider_name,  # type: str
        resource_type,  # type: str
        resource_name,  # type: str
        management_association_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ManagementAssociation"
        """Retrieves the user ManagementAssociation.

        Retrieve ManagementAssociation.

        :param resource_group_name: The name of the resource group to get. The name is case
         insensitive.
        :type resource_group_name: str
        :param provider_name: Provider name for the parent resource.
        :type provider_name: str
        :param resource_type: Resource type for the parent resource.
        :type resource_type: str
        :param resource_name: Parent resource name.
        :type resource_name: str
        :param management_association_name: User ManagementAssociation Name.
        :type management_association_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ManagementAssociation or the result of cls(response)
        :rtype: ~azure.mgmt.operationsmanagement.models.ManagementAssociation
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ManagementAssociation"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2015-11-01-preview"

        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'providerName': self._serialize.url("provider_name", provider_name, 'str'),
            'resourceType': self._serialize.url("resource_type", resource_type, 'str'),
            'resourceName': self._serialize.url("resource_name", resource_name, 'str'),
            'managementAssociationName': self._serialize.url("management_association_name", management_association_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.CodeMessageError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ManagementAssociation', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{providerName}/{resourceType}/{resourceName}/providers/Microsoft.OperationsManagement/ManagementAssociations/{managementAssociationName}'}
