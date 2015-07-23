# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locker', '0002_auto_20150529_1531'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LockVault',
        ),
        migrations.CreateModel(
            name='Lockers',
            fields=[
            ],
            options={
                'proxy': True,
                'verbose_name_plural': 'locker',
            },
            bases=('locker.locker',),
        ),
    ]
