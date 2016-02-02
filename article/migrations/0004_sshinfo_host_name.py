# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_sshinfo_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='sshinfo',
            name='host_name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
