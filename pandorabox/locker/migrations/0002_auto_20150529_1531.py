# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locker', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='locker_mod',
        ),
        migrations.CreateModel(
            name='LockVault',
            fields=[
            ],
            options={
                'proxy': True,
                'verbose_name_plural': 'LockVault',
            },
            bases=('locker.locker',),
        ),
    ]
