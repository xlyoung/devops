# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ip_list',
            name='id',
            field=models.CharField(max_length=100, serialize=False, editable=False, primary_key=True),
        ),
    ]
