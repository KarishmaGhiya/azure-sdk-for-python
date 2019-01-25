# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import uuid
from msrest.pipeline import ClientRawResponse

from .. import models


class ReservationRecommendationsSharedOperations(object):
    """ReservationRecommendationsSharedOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: Version of the API to be used with the client request. The current version is 2018-10-01. Constant value: "2018-10-01".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2018-10-01"

        self.config = config

    def list_by_billing_profile(
            self, billing_account_id, billing_profile_id, custom_headers=None, raw=False, **operation_config):
        """List of recommendations for purchasing reserved instances calculated
        based on past usage for the provided billingAccountId and
        billingProfileId.

        :param billing_account_id: BillingAccount ID
        :type billing_account_id: str
        :param billing_profile_id: BillingProfile ID
        :type billing_profile_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ReservationRecommendationsSharedListResult or
         ClientRawResponse if raw=true
        :rtype:
         ~azure.mgmt.consumption.models.ReservationRecommendationsSharedListResult
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.consumption.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.list_by_billing_profile.metadata['url']
        path_format_arguments = {
            'billingAccountId': self._serialize.url("billing_account_id", billing_account_id, 'str'),
            'billingProfileId': self._serialize.url("billing_profile_id", billing_profile_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
        query_parameters['lookBackPeriod'] = self._serialize.query("self.config.look_back_period", self.config.look_back_period, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ReservationRecommendationsSharedListResult', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_by_billing_profile.metadata = {'url': '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/providers/Microsoft.Consumption/sharedReservationRecommendations'}
