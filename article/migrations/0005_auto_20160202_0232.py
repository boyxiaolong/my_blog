# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_sshinfo_host_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sshinfo',
            name='state',
            field=models.IntegerField(default=0),
        ),
    ]
