# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ceamon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commandmodel',
            name='check',
            field=models.CharField(default=b'N/A', max_length=254, unique=True, null=True, choices=[(b'ck_os_version.py', b'ck_os_version.py'), (b'ck_gettotalsizefs.py', b'ck_gettotalsizefs.py'), (b'ck_osv_version.py', b'ck_osv_version.py'), (b'ck_get_ram.py', b'ck_get_ram.py'), (b'ck_timeout.py', b'ck_timeout.py'), (b'ck_get_num_cpus.py', b'ck_get_num_cpus.py')]),
        ),
        migrations.AlterField(
            model_name='statusmodel',
            name='status_id',
            field=models.CharField(default=b'N/A', max_length=256, choices=[(b'ck_os_version.py', b'ck_os_version.py'), (b'ck_gettotalsizefs.py', b'ck_gettotalsizefs.py'), (b'ck_osv_version.py', b'ck_osv_version.py'), (b'ck_get_ram.py', b'ck_get_ram.py'), (b'ck_timeout.py', b'ck_timeout.py'), (b'ck_get_num_cpus.py', b'ck_get_num_cpus.py')]),
        ),
    ]
