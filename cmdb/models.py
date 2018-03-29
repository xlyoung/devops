from django.db import models

# Create your models here.

import uuid


class UUIDTools(object):
    """uuid function tools"""

    @staticmethod
    def uuid1_hex():
        """
        return uuid1 hex string
        eg: 23f87b528d0f11e696a7f45c89a84eed
        """
        return uuid.uuid1().hex



class ip_list(models.Model):
    uuid = models.CharField(editable=False,max_length=100)
    id = models.AutoField('ID', primary_key=True,default=1)
    hostname = models.CharField(max_length=100)
    groupname = models.CharField(max_length=100)
    ip = models.GenericIPAddressField(protocol="ipv4", null=True, blank=True)
    system = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    passwd = models.CharField(max_length=100)
    class Meta:
        db_table = "iplist"
