from django.contrib import admin, messages
from ceamon import models as m
from ceamon.models import sapnode, CommandModel
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django import forms
from django.db import models
import copy
# Register your models here.
# Visualizacion admin

"""
class sapnodeadmin(admin.ModelAdmin):
    model = sapnode
    list_display = ['sid', 'hostname','url', 'project', 'client_role', 'product', 'created_at', 'database', 'os', 'ip',]

    def get_name(self, obj):
        return obj.hostname.name
    get_name.admin_order_field  = 'sid'  #Allows column order sorting
    get_name.short_description = 'SID'  #Renames column head

class status_admin(admin.ModelAdmin):
    model = status
    list_display = ['sapnode_id', 'check_java', 'check_abap', 'check_webdispatcher', ]
 
    def __unicode__(self):
        return self.status

class status_mod(status):
    class Meta:
        proxy=True

class statusResource(resources.ModelResource):
    class Meta:
        model = status

class statusAdmin(ImportExportModelAdmin):
    resource_class = statusResource
    pass

"""

# Proxy's de clases
class server(sapnode):
    class Meta:
        verbose_name_plural = "Servers"
        proxy=True

# Servers:
class sapnodeResource(resources.ModelResource):
    class Meta:
        model = sapnode

def copy_server(modeladmin, request, queryset):
    try:
        for sd in queryset:
            sd_copy = copy.copy(sd)
            sd_copy.id = None
            #defaults=({sd.hostname:'asdasd'})
            sd_copy.hostname = "hostname"
            sd_copy.save()

            for req in sd.command.all(): # tambien copiamos el m2m command
                sd_copy.command.add(req)

            for attr_name in [ 'hostname' ]:
                sd_copy.__dict__.update({attr_name : "N/A"})
            sd_copy.save()

        copy_server.short_description = "copy_server"
        messages.success(request,'Object has been copied')
    except:
        messages.error(request,'Now exist a object with same hostname')

class sapnodeAdmin(ImportExportModelAdmin):
    actions = [copy_server]
    save_on_top = True    
    list_display = ['sid', 'hostname', 'project', 'client_role', 'product', 'product_def',]
    filter_horizontal = ('command',)
    resource_class = sapnodeResource
    pass


##### Import Export #####
####
class Command(CommandModel):
    class Meta:
        verbose_name_plural = "Commands"
        proxy=True

# Servers:
class CommandModelResource(resources.ModelResource):
    class Meta:
        model = CommandModel

class CommandModelAdmin(ImportExportModelAdmin):
    list_display = ['status',]
    resource_class = CommandModelResource
    pass

####

#Registros activos:
#admin.site.register(server_mod, sapnodeadmin)
#admin.site.register(status_mod, status_admin )
#admin.site.register(imp_exp_Admin_mod)
admin.site.register(server, sapnodeAdmin)
admin.site.register(Command, CommandModelAdmin)
#admin.site.register(status_mod, statusAdmin)
