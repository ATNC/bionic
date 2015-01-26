# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0002_twit_twit_from'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twit',
            name='twit_from',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
    ]
