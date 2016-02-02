# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20160201_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='sshinfo',
            name='state',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
