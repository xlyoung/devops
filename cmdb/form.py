#coding:utf-8

from django.forms import Form
from django.forms import fields


class IpList(Form):
    id = fields.UUIDField(required=True)
    hostname = fields.CharField(required=True)
    ip = fields.GenericIPAddressField(required=True)
    product = fields.ChoiceField(choices=[(1,'服务器'),(2,'交换机'),(3,'路由器')])
    group = fields.CharField(required=True)
    system = fields.ChoiceField(choices=[(1,'linux'),(2,'windows')])