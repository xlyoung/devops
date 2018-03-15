# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ip_list',
            fields=[
                ('id', models.UUIDField(auto_created=True, primary_key=True, default=uuid.uuid4, serialize=False, editable=False)),
                ('hostname', models.CharField(max_length=100)),
                ('group', models.CharField(max_length=100)),
                ('ip', models.GenericIPAddressField(null=True, protocol=b'ipv4', blank=True)),
                ('system', models.CharField(max_length=100)),
                ('product', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'iplist',
            },
        ),
    ]
