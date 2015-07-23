from django.db import models as m

class CommandModel(m.Model):
    status = (
        ('N/A', 'N/A'),
        ('ck_abap.py', 'ck_abap.py'),
        ('ck_java.py', 'ck_java.py'),
        ('ck_webdispatcher.py', 'ck_webdispatcher.py'),
        ('ck_db_version.py', 'ck_db_version.py'),
        ('ck_os_version.py', 'ck_os_version.py'),
        ('ck_gettotalsizefs.py', 'ck_gettotalsizefs.py'),
        ('ck_get_num_cpus.py', 'ck_get_num_cpus.py'),
        ('ck_osv_version.py', 'ck_osv_version.py'),
        ('ck_dbv_version.py', 'ck_dbv_version.py'),
        ('ck_get_ram.py', 'ck_get_ram.py'),
        ('ck_sap_kernel_version.py', 'ck_sap_kernel_version.py'),
    )

    status = m.CharField(max_length=254,
            choices=status,
            unique=True,
            null=True,
            default='N/A')

    def __unicode__(self):
        return u'%s' % (self.status)

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

    project = (
        ('PROJECT1', 'Project1'),
        ('PROJECT2', 'Project2'),
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

    status = (
        ('N/A', 'N/A'),
        ('SUCCESS', 'SUCCESS'),
        ('WARNING', 'WARNING'),
        ('DANGER', 'DANGER'),
        ('INFO', 'INFO'),
    )

    product_def = (
        ('APP', 'APP'),
        ('CI', 'CI'),
    )

    project = m.CharField(max_length=256,
            choices=project,
            help_text="Project related to this server",
            default='Project1')

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
    #product_def = m.CharField(max_length=256, blank=True, default='N/A', help_text="This server is APP or CI?",)
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
        return u'%s ---- %s' % (self.sid, self.hostname)


