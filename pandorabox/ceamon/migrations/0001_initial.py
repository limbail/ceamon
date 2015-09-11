# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommandModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('check', models.CharField(default=b'N/A', max_length=254, unique=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectsModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('projects', models.CharField(default=b'N/A', max_length=254, null=True, verbose_name=b'Projects', help_text=b'You can add projects to ceamon')),
            ],
        ),
        migrations.CreateModel(
            name='sapnode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active_moni', models.CharField(default=b'Yes', max_length=10, verbose_name=b'Moni active?', choices=[(b'Yes', b'yes'), (b'No', b'no')])),
                ('remote_mon_active', models.CharField(default=b'No', help_text=b'If yes, the remote client (scout) will be installed into remote server', max_length=10, verbose_name=b'Scout active?', choices=[(b'No', b'no'), (b'Yes', b'yes')])),
                ('product', models.CharField(default=b'Abap', help_text=b'Product related to this server', max_length=256, choices=[(b'ABAP', b'Abap'), (b'PORTAL', b'Portal'), (b'JAVA_ENGINE', b'Java_engine'), (b'WEBDISPATCHER', b'Webdispatcher'), (b'APACHE', b'Apache'), (b'OPENTEXT', b'Opentext'), (b'CONTENT_SERVER', b'Content_server'), (b'TREX', b'Trex')])),
                ('client_role', models.CharField(default=b'Desarrollo', help_text=b'Client role for this server on project', max_length=256, choices=[(b'DESARROLLO', b'Desarrollo'), (b'INTEGRACION', b'Integracion'), (b'PRODUCCION', b'Produccion'), (b'CERTIFICACION', b'Certificacion'), (b'GOLD', b'Gold'), (b'TEMPORAL', b'Temporal')])),
                ('status', models.CharField(default=b'N/A', max_length=256, choices=[(b'N/A', b'N/A'), (b'SUCCESS', b'SUCCESS'), (b'WARNING', b'WARNING'), (b'DANGER', b'DANGER'), (b'INFO', b'INFO')])),
                ('product_def', models.CharField(default=b'APP', max_length=256, choices=[(b'APP', b'APP'), (b'CI', b'CI')])),
                ('product_v', models.CharField(default=b'N/A', max_length=256, blank=True)),
                ('database', models.CharField(default=b'N/A', max_length=256, blank=True)),
                ('database_v', models.CharField(default=b'N/A', max_length=256, blank=True)),
                ('os', models.CharField(default=b'N/A', max_length=256, blank=True)),
                ('os_v', models.CharField(default=b'N/A', max_length=256, blank=True)),
                ('ip', models.CharField(default=b'N/A', max_length=256, blank=True)),
                ('cpu', models.CharField(default=b'N/A', max_length=256, blank=True)),
                ('asi_disk', models.CharField(default=b'N/A', max_length=256, blank=True)),
                ('asi_ram', models.CharField(default=b'N/A', max_length=256, blank=True)),
                ('sid', models.CharField(default=b'N/A', help_text=b'Short ID for this server', max_length=10, blank=True)),
                ('hostname', models.CharField(default=b'N/A', help_text=b'Hostname must be unique', unique=True, max_length=100, blank=True)),
                ('url', models.CharField(default=b'N/A', max_length=256, blank=True)),
                ('sap_kernel', models.CharField(default=b'N/A', max_length=256, blank=True)),
                ('sap_clnt', models.CharField(default=b'100', max_length=256, blank=True)),
                ('sap_sysn', models.CharField(default=b'00', max_length=256, blank=True)),
                ('command', models.ManyToManyField(to='ceamon.CommandModel')),
                ('project', models.ManyToManyField(to='ceamon.ProjectsModel')),
            ],
            options={
                'verbose_name_plural': 'sapnode',
            },
        ),
        migrations.CreateModel(
            name='StatusModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status_id', models.CharField(default=b'N/A', max_length=256)),
                ('status', models.CharField(default=b'N/A', max_length=256, choices=[(b'N/A', b'N/A'), (b'SUCCESS', b'SUCCESS'), (b'WARNING', b'WARNING'), (b'DANGER', b'DANGER'), (b'INFO', b'INFO')])),
                ('comment', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('system', models.ForeignKey(to='ceamon.sapnode')),
            ],
        ),
        migrations.CreateModel(
            name='Command',
            fields=[
            ],
            options={
                'proxy': True,
                'verbose_name_plural': 'Commands',
            },
            bases=('ceamon.commandmodel',),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
            ],
            options={
                'proxy': True,
                'verbose_name_plural': 'Projects',
            },
            bases=('ceamon.projectsmodel',),
        ),
        migrations.CreateModel(
            name='server',
            fields=[
            ],
            options={
                'proxy': True,
                'verbose_name_plural': 'Servers (1)',
            },
            bases=('ceamon.sapnode',),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
            ],
            options={
                'proxy': True,
                'verbose_name_plural': 'Status',
            },
            bases=('ceamon.statusmodel',),
        ),
    ]
