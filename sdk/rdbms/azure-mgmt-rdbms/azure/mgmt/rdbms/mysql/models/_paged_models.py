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

from msrest.paging import Paged


class ServerPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Server <azure.mgmt.rdbms.mysql.models.Server>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Server]'}
    }

    def __init__(self, *args, **kwargs):

        super(ServerPaged, self).__init__(*args, **kwargs)
class FirewallRulePaged(Paged):
    """
    A paging container for iterating over a list of :class:`FirewallRule <azure.mgmt.rdbms.mysql.models.FirewallRule>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[FirewallRule]'}
    }

    def __init__(self, *args, **kwargs):

        super(FirewallRulePaged, self).__init__(*args, **kwargs)
class VirtualNetworkRulePaged(Paged):
    """
    A paging container for iterating over a list of :class:`VirtualNetworkRule <azure.mgmt.rdbms.mysql.models.VirtualNetworkRule>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[VirtualNetworkRule]'}
    }

    def __init__(self, *args, **kwargs):

        super(VirtualNetworkRulePaged, self).__init__(*args, **kwargs)
class DatabasePaged(Paged):
    """
    A paging container for iterating over a list of :class:`Database <azure.mgmt.rdbms.mysql.models.Database>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Database]'}
    }

    def __init__(self, *args, **kwargs):

        super(DatabasePaged, self).__init__(*args, **kwargs)
class ConfigurationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Configuration <azure.mgmt.rdbms.mysql.models.Configuration>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Configuration]'}
    }

    def __init__(self, *args, **kwargs):

        super(ConfigurationPaged, self).__init__(*args, **kwargs)
class LogFilePaged(Paged):
    """
    A paging container for iterating over a list of :class:`LogFile <azure.mgmt.rdbms.mysql.models.LogFile>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[LogFile]'}
    }

    def __init__(self, *args, **kwargs):

        super(LogFilePaged, self).__init__(*args, **kwargs)
class ServerAdministratorResourcePaged(Paged):
    """
    A paging container for iterating over a list of :class:`ServerAdministratorResource <azure.mgmt.rdbms.mysql.models.ServerAdministratorResource>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ServerAdministratorResource]'}
    }

    def __init__(self, *args, **kwargs):

        super(ServerAdministratorResourcePaged, self).__init__(*args, **kwargs)
class PerformanceTierPropertiesPaged(Paged):
    """
    A paging container for iterating over a list of :class:`PerformanceTierProperties <azure.mgmt.rdbms.mysql.models.PerformanceTierProperties>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PerformanceTierProperties]'}
    }

    def __init__(self, *args, **kwargs):

        super(PerformanceTierPropertiesPaged, self).__init__(*args, **kwargs)
class QueryTextPaged(Paged):
    """
    A paging container for iterating over a list of :class:`QueryText <azure.mgmt.rdbms.mysql.models.QueryText>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[QueryText]'}
    }

    def __init__(self, *args, **kwargs):

        super(QueryTextPaged, self).__init__(*args, **kwargs)
class QueryStatisticPaged(Paged):
    """
    A paging container for iterating over a list of :class:`QueryStatistic <azure.mgmt.rdbms.mysql.models.QueryStatistic>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[QueryStatistic]'}
    }

    def __init__(self, *args, **kwargs):

        super(QueryStatisticPaged, self).__init__(*args, **kwargs)
class WaitStatisticPaged(Paged):
    """
    A paging container for iterating over a list of :class:`WaitStatistic <azure.mgmt.rdbms.mysql.models.WaitStatistic>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[WaitStatistic]'}
    }

    def __init__(self, *args, **kwargs):

        super(WaitStatisticPaged, self).__init__(*args, **kwargs)
class AdvisorPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Advisor <azure.mgmt.rdbms.mysql.models.Advisor>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Advisor]'}
    }

    def __init__(self, *args, **kwargs):

        super(AdvisorPaged, self).__init__(*args, **kwargs)
class RecommendationActionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`RecommendationAction <azure.mgmt.rdbms.mysql.models.RecommendationAction>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[RecommendationAction]'}
    }

    def __init__(self, *args, **kwargs):

        super(RecommendationActionPaged, self).__init__(*args, **kwargs)
class PrivateEndpointConnectionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`PrivateEndpointConnection <azure.mgmt.rdbms.mysql.models.PrivateEndpointConnection>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PrivateEndpointConnection]'}
    }

    def __init__(self, *args, **kwargs):

        super(PrivateEndpointConnectionPaged, self).__init__(*args, **kwargs)
class PrivateLinkResourcePaged(Paged):
    """
    A paging container for iterating over a list of :class:`PrivateLinkResource <azure.mgmt.rdbms.mysql.models.PrivateLinkResource>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PrivateLinkResource]'}
    }

    def __init__(self, *args, **kwargs):

        super(PrivateLinkResourcePaged, self).__init__(*args, **kwargs)
class ServerKeyPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ServerKey <azure.mgmt.rdbms.mysql.models.ServerKey>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ServerKey]'}
    }

    def __init__(self, *args, **kwargs):

        super(ServerKeyPaged, self).__init__(*args, **kwargs)
