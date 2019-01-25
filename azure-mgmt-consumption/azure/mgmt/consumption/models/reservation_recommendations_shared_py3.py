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

from .resource_py3 import Resource


class ReservationRecommendationsShared(Resource):
    """Reservation Recommendation for shared scope.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar look_back_period: The number of days of usage to look back for
     recommendation.
    :vartype look_back_period: str
    :ivar meter_id: The meter id (GUID)
    :vartype meter_id: str
    :ivar sku_name: Sku name of the reserved instance resource.
    :vartype sku_name: str
    :ivar region: Region of the reserved instance resource.
    :vartype region: str
    :ivar term: RI recommendations in one or three year terms.
    :vartype term: str
    :ivar cost_with_no_ri: The total amount of cost without reserved
     instances.
    :vartype cost_with_no_ri: decimal.Decimal
    :ivar recommended_quantity: Recommended quality for reserved instances.
    :vartype recommended_quantity: decimal.Decimal
    :ivar total_cost_with_ri: The total amount of cost with reserved
     instances.
    :vartype total_cost_with_ri: decimal.Decimal
    :ivar net_savings: Total estimated savings with reserved instances.
    :vartype net_savings: decimal.Decimal
    :ivar first_usage_date: The usage date for looking back.
    :vartype first_usage_date: datetime
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'tags': {'readonly': True},
        'look_back_period': {'readonly': True},
        'meter_id': {'readonly': True},
        'sku_name': {'readonly': True},
        'region': {'readonly': True},
        'term': {'readonly': True},
        'cost_with_no_ri': {'readonly': True},
        'recommended_quantity': {'readonly': True},
        'total_cost_with_ri': {'readonly': True},
        'net_savings': {'readonly': True},
        'first_usage_date': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'look_back_period': {'key': 'properties.lookBackPeriod', 'type': 'str'},
        'meter_id': {'key': 'properties.meterId', 'type': 'str'},
        'sku_name': {'key': 'properties.skuName', 'type': 'str'},
        'region': {'key': 'properties.region', 'type': 'str'},
        'term': {'key': 'properties.term', 'type': 'str'},
        'cost_with_no_ri': {'key': 'properties.costWithNoRI', 'type': 'decimal'},
        'recommended_quantity': {'key': 'properties.recommendedQuantity', 'type': 'decimal'},
        'total_cost_with_ri': {'key': 'properties.totalCostWithRI', 'type': 'decimal'},
        'net_savings': {'key': 'properties.netSavings', 'type': 'decimal'},
        'first_usage_date': {'key': 'properties.firstUsageDate', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs) -> None:
        super(ReservationRecommendationsShared, self).__init__(**kwargs)
        self.look_back_period = None
        self.meter_id = None
        self.sku_name = None
        self.region = None
        self.term = None
        self.cost_with_no_ri = None
        self.recommended_quantity = None
        self.total_cost_with_ri = None
        self.net_savings = None
        self.first_usage_date = None
