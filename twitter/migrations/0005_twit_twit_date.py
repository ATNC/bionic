# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0004_twit_twit_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='twit',
            name='twit_date',
            field=models.DateField(default=datetime.datetime(2015, 1, 28, 8, 13, 24, 684204, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
