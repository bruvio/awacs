# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Elemental Activations'
prefix = 'elemental-activations'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CompleteFileUpload = Action('CompleteFileUpload')
DownloadSoftware = Action('DownloadSoftware')
GenerateLicenses = Action('GenerateLicenses')
GetActivation = Action('GetActivation')
ListTagsForResource = Action('ListTagsForResource')
StartFileUpload = Action('StartFileUpload')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
