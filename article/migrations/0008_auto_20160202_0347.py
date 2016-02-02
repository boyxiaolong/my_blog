# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20160202_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sshinfo',
            name='port',
            field=models.IntegerField(default=22),
        ),
    ]
