import os
import django.contrib.admin.widgets
from django.db import models as m
from django.utils import timezone

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dir = (BASE_DIR + "/ceamon/management/commands/scripts/")

ck_scripts = os.listdir(dir)
ck_scripts = [x for x in ck_scripts if x.startswith('ck') and x.endswith('py')]
for x in ck_scripts:
    check = dict([ (x, x) for x in ck_scripts ])
check = [(v, k) for k, v in check.iteritems()]

status = (
    ('N/A', 'N/A'),
    ('SUCCESS', 'SUCCESS'),
    ('WARNING', 'WARNING'),
    ('DANGER', 'DANGER'),
    ('INFO', 'INFO'),
)


class ProjectsModel(m.Model):
    projects = m.CharField(max_length=254,
        verbose_name='Projects',
        null=True,
        help_text="You can add projects to ceamon",
        default='N/A')

    def __unicode__(self):
        return self.projects

class CommandModel(m.Model):
    check = m.CharField(max_length=254,
            choices=check,
            unique=True,
            null=True,
            default='N/A')
 
    def __unicode__(self):
        return u'%s' % (self.check)


class sapnode(m.Model):
    class Meta:
        verbose_name_plural = "sapnode"

    active_moni_YES_OR_NO = (
        ('Yes', 'yes'),
        ('No', 'no'),
    )

    remote_mon_active_YES_OR_NO = (
        ('No', 'no'),
        ('Yes', 'yes'),
    )
    
    # Boolean no funciona correctamente, se cambia a charfield, el admin no reflejaba correctamente los valores
    active_moni = m.CharField( 
        max_length=10,
        verbose_name='Moni active?',
        choices=active_moni_YES_OR_NO,
        default='Yes',
    )

    remote_mon_active = m.CharField(
        max_length=10,
        verbose_name='Scout active?',
        help_text="If yes, the remote client (scout) will be installed into remote server",
        choices=remote_mon_active_YES_OR_NO,
        default='No',
    )

    product = (
        ('ABAP', 'Abap'),
        ('PORTAL', 'Portal'),
        ('JAVA_ENGINE', 'Java_engine'),
        ('WEBDISPATCHER', 'Webdispatcher'),
        ('APACHE', 'Apache'),
        ('OPENTEXT', 'Opentext'),
        ('CONTENT_SERVER', 'Content_server'),
        ('TREX', 'Trex'),
    )

    client_role = (
        ('DESARROLLO', 'Desarrollo'),
        ('INTEGRACION', 'Integracion'),
        ('PRODUCCION', 'Produccion'),
        ('CERTIFICACION', 'Certificacion'),
        ('GOLD', 'Gold'),
        ('TEMPORAL', 'Temporal'),
    )

    product_def = (
        ('APP', 'APP'),
        ('CI', 'CI'),
    )

    project = m.ManyToManyField(ProjectsModel)
    product = m.CharField(max_length=256,
            choices=product,
            help_text="Product related to this server",
            default='Abap')

    client_role = m.CharField(max_length=256,
            choices=client_role,
            help_text="Client role for this server on project",
            default='Desarrollo')

    status = m.CharField(max_length=256,
            choices=status,
            default='N/A')

    product_def = m.CharField(max_length=256,
            choices=product_def,
            default='APP')

    product_v = m.CharField(max_length=256, blank=True, default='N/A')
    database = m.CharField(max_length=256, blank=True, default='N/A')
    database_v = m.CharField(max_length=256, blank=True, default='N/A')
    os = m.CharField(max_length=256, blank=True, default='N/A')
    os_v = m.CharField(max_length=256, blank=True, default='N/A')
    ip = m.CharField(max_length=256, blank=True, default='N/A')
    cpu = m.CharField(max_length=256, blank=True, default='N/A' )
    asi_disk = m.CharField(max_length=256, blank=True, default='N/A')
    asi_ram = m.CharField(max_length=256, blank=True, default='N/A')
    sid = m.CharField(max_length=10, blank=True, default='N/A', help_text="Short ID for this server",)
    hostname = m.CharField(max_length=100, unique=True, blank=True, default='N/A', help_text="Hostname must be unique",)
    url = m.CharField(max_length=256, blank=True, default='N/A')
    sap_kernel = m.CharField(max_length=256, blank=True, default='N/A')
    sap_clnt = m.CharField(max_length=256, blank=True, default='100')
    sap_sysn = m.CharField(max_length=256, blank=True, default='00')
    command = m.ManyToManyField(CommandModel)

    #created_at = m.DateTimeField(null=True, 'Datetime created')

    def __unicode__(self):
        return u'%s' % (self.hostname)

class StatusModel(m.Model):
    system = m.ForeignKey(sapnode)
    status_id = m.CharField(max_length=256,
            choices=check,
            default='N/A')
    status = m.CharField(max_length=256,
            choices=status,
            default='N/A')
    comment = m.CharField(max_length=256, blank=True, default='N/A')
    created = m.DateTimeField(auto_now_add=True)
    modified = m.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s -- %s -- %s -- %s' % (self.system,  self.status_id, self.status, self.comment)
