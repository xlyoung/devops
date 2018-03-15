#coding:utf-8

from django.forms import Form
from django.forms import fields
from cmdb import models

class IpList(Form,):
    # id = fields.UUIDField(required=True)
    hostname = fields.CharField(required=True)
    ip = fields.GenericIPAddressField(required=True)
    product = fields.ChoiceField(choices=[(1,'服务器'),(2,'交换机'),(3,'路由器')])
    group = fields.CharField(required=True)
    system = fields.ChoiceField(choices=[(1,'linux'),(2,'windows')])


# class QueryIp(IpList):
#     q_id  = models.ip_list.id()
#     q_hostname = models.ip_list.hostname()
#     q_ip = models.ip_list.ip()
#     q_product = models.ip_list.product()
#     q_group = models.ip_list.groupname()
#     q_system = models.ip_list.system()
