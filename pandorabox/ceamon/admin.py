import django.contrib.admin.widgets
from django.contrib import admin, messages
from ceamon import models as m
from ceamon.models import sapnode, CommandModel, ProjectsModel
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django import forms
from django.db import models
from ceamon import forms
import copy
# Register your models here.
# Visualizacion admin

# Proxy's de clases

class VerboseName(str):
    def __init__(self, func):
        self.func = func

    def decode(self, encoding, erros):
        return self.func().decode(encoding, erros)


class server(sapnode):
    class Meta:
        verbose_name_plural = VerboseName(lambda: "Servers (%d)" % sapnode.objects.count())
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
    list_display = ['sid', 'hostname', 'client_role', 'product', 'product_def',]
    list_filter = ('active_moni', 'client_role', 'project', )
    filter_horizontal = ('command', 'project')
    resource_class = sapnodeResource
    fieldsets = [
        (None, {'fields': ['active_moni', 'remote_mon_active', 'project', 'product', 'client_role', 'product_def', 'sid', 'hostname', 'command']}),
        ('product_v', {'fields': ['product_v'], 'classes': ['collapse']}),
        ('database', {'fields': ['database'], 'classes': ['collapse']}),
        ('database_v', {'fields': ['database_v'], 'classes': ['collapse']}),
        ('os', {'fields': ['os'], 'classes': ['collapse']}),
        ('os_v', {'fields': ['os_v'], 'classes': ['collapse']}),
        ('ip', {'fields': ['ip'], 'classes': ['collapse']}),
        ('cpu', {'fields': ['cpu'], 'classes': ['collapse']}),
        ('asi_disk', {'fields': ['asi_disk'], 'classes': ['collapse']}),
        ('asi_ram', {'fields': ['asi_ram'], 'classes': ['collapse']}),
        ('url', {'fields': ['url'], 'classes': ['collapse']}),
        ('sap_kernel', {'fields': ['sap_kernel'], 'classes': ['collapse']}),
        ('sap_clnt', {'fields': ['sap_clnt'], 'classes': ['collapse']}),
        ('sap_sysn', {'fields': ['sap_sysn'], 'classes': ['collapse']}),
        ('status', {'fields': ['status'], 'classes': ['collapse']}),
    ]


##### Import Export #####
#### COMMANDS
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
#Ej. verbose_name_plural = VerboseName(lambda: "Used Coupons (%d)" % UsedCoupons.objects.count())
#### PROJECTS
class Project(ProjectsModel):
    class Meta:
        verbose_name_plural = VerboseName(lambda: "Projects")
        proxy=True


# Servers:
class ProjectModelResource(resources.ModelResource):
    class Meta:
        model = ProjectsModel


class ProjectModelAdmin(ImportExportModelAdmin):
    #list_display = ['status',]
    resource_class = ProjectModelResource
    fieldsets = (
        (None, {
            'fields': ('projects',),
            'description': "Here you can define the projects to add in servers."
        }),
    )
    pass

####


#Registros activos:
#admin.site.register(server_mod, sapnodeadmin)
#admin.site.register(status_mod, status_admin )
#admin.site.register(imp_exp_Admin_mod)
admin.site.register(server, sapnodeAdmin)
admin.site.register(Command, CommandModelAdmin)
admin.site.register(Project, ProjectModelAdmin)
#admin.site.register(ProjectsModel)
#admin.site.register(status_mod, statusAdmin)
