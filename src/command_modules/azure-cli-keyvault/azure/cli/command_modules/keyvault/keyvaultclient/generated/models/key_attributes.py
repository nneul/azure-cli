# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
#pylint: skip-file
from .attributes import Attributes


class KeyAttributes(Attributes):
    """The attributes of a key managed by the KeyVault service.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param enabled: Determines whether the object is enabled
    :type enabled: bool
    :param not_before: Not before date in UTC
    :type not_before: datetime
    :param expires: Expiry date in UTC
    :type expires: datetime
    :ivar created: Creation time in UTC
    :vartype created: datetime
    :ivar updated: Last updated time in UTC
    :vartype updated: datetime
    """ 

    _validation = {
        'created': {'readonly': True},
        'updated': {'readonly': True},
    }

    def __init__(self, enabled=None, not_before=None, expires=None):
        super(KeyAttributes, self).__init__(enabled=enabled, not_before=not_before, expires=expires)
