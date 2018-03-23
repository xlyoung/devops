#coding:utf-8

from django.forms import Form
from django.forms import fields
from django.forms import widgets
from cmdb import models

class IpList(Form,):
    # id = fields.UUIDField(required=True)
    hostname = fields.CharField(required=True)
    ip = fields.GenericIPAddressField(required=True)
    product = fields.ChoiceField(choices=[('service','服务器'),('switch','交换机'),('router','路由器')],widget=widgets.Select)
    group = fields.CharField(required=True)
    system = fields.ChoiceField(choices=[('linux','linux'),('windows','windows')],widget=widgets.Select)

# class QueryIp(IpList):
#     q_id  = models.ip_list.id()
#     q_hostname = models.ip_list.hostname()
#     q_ip = models.ip_list.ip()
#     q_product = models.ip_list.product()
#     q_group = models.ip_list.groupname()
#     q_system = models.ip_list.system()
