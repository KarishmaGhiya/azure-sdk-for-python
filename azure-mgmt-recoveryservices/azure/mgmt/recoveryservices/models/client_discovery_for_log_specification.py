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

from msrest.serialization import Model


class ClientDiscoveryForLogSpecification(Model):
    """Class to represent shoebox log specification in json client discovery.

    :param name: Name of the log.
    :type name: str
    :param display_name: Localized display name
    :type display_name: str
    :param blob_duration: Blobs created in customer storage account per hour
    :type blob_duration: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'blob_duration': {'key': 'blobDuration', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ClientDiscoveryForLogSpecification, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display_name = kwargs.get('display_name', None)
        self.blob_duration = kwargs.get('blob_duration', None)
