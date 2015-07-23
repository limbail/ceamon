# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locker', '0003_auto_20150713_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locker',
            name='url',
            field=models.URLField(default=b'http://temporal.corp', max_length=500, verbose_name=b'Site URL', blank=True),
        ),
        migrations.AlterField(
            model_name='locker',
            name='username',
            field=models.CharField(unique=True, max_length=200, blank=True),
        ),
    ]
