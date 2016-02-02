# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20160202_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sshinfo',
            name='host_name',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
