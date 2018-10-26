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


class MigrateSchemaSqlServerSqlDbDatabaseInput(Model):
    """Database input for migrate schema Sql Server to Azure SQL Server scenario.

    :param target_database_name: Name of target database
    :type target_database_name: str
    :param schema_setting: Database schema migration settings
    :type schema_setting:
     ~azure.mgmt.datamigration.models.SchemaMigrationSetting
    """

    _attribute_map = {
        'target_database_name': {'key': 'targetDatabaseName', 'type': 'str'},
        'schema_setting': {'key': 'schemaSetting', 'type': 'SchemaMigrationSetting'},
    }

    def __init__(self, **kwargs):
        super(MigrateSchemaSqlServerSqlDbDatabaseInput, self).__init__(**kwargs)
        self.target_database_name = kwargs.get('target_database_name', None)
        self.schema_setting = kwargs.get('schema_setting', None)
