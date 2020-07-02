# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum

class AccessRights(str, Enum):
    """Access rights of the entity
    """

    manage = "Manage"
    send = "Send"
    listen = "Listen"

class EntityAvailabilityStatus(str, Enum):
    """Availability status of the entity
    """

    available = "Available"
    limited = "Limited"
    renaming = "Renaming"
    restoring = "Restoring"
    unknown = "Unknown"

class EntityStatus(str, Enum):
    """Status of a Service Bus resource
    """

    active = "Active"
    creating = "Creating"
    deleting = "Deleting"
    disabled = "Disabled"
    receive_disabled = "ReceiveDisabled"
    renaming = "Renaming"
    restoring = "Restoring"
    send_disabled = "SendDisabled"
    unknown = "Unknown"

class MessagingSku(str, Enum):
    """The SKU for the messaging entity.
    """

    basic = "Basic"
    standard = "Standard"
    premium = "Premium"

class NamespaceType(str, Enum):
    """The type of entities the namespace can contain.
    """

    messaging = "Messaging"
    notification_hub = "NotificationHub"
    mixed = "Mixed"
    event_hub = "EventHub"
    relay = "Relay"
