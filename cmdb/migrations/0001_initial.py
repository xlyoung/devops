# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ip_list',
            fields=[
                ('uuid', models.CharField(max_length=100, editable=False)),
                ('id', models.AutoField(serialize=False, verbose_name=b'ID', primary_key=True)),
                ('hostname', models.CharField(max_length=100)),
                ('groupname', models.CharField(max_length=100)),
                ('ip', models.GenericIPAddressField(null=True, protocol=b'ipv4', blank=True)),
                ('system', models.CharField(max_length=100)),
                ('product', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100)),
                ('passwd', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'iplist',
            },
        ),
    ]
