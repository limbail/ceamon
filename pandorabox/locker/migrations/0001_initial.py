# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='locker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200, blank=True)),
                ('password', models.CharField(max_length=200)),
                ('url', models.URLField(max_length=500, verbose_name=b'Site URL', blank=True)),
                ('notes', models.TextField(help_text=b'Any extra notes', max_length=500, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='locker_mod',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('locker.locker',),
        ),
    ]
