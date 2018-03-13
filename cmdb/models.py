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
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    hostname = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    ip = models.GenericIPAddressField(protocol="ipv4", null=True, blank=True)
    class Meta:
        db_table = "iplist"
