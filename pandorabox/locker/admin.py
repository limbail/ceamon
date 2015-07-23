from django.contrib import admin
from locker import models as m
from locker.models import locker
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
# Visualizacion admin
'''
class lockeradmin(admin.ModelAdmin):
    model = locker
    list_display = ['title', 'password', 'url', 'notes', 'created_at', 'updated_at',]

class LockVault(locker):
    class Meta:
        verbose_name_plural = "LockVault"
        proxy=True
'''
##### Import Export #####
class Lockers(locker):
    class Meta:
        verbose_name_plural = "locker"
        proxy=True

# Servers:
class LockerModelResource(resources.ModelResource):
    class Meta:
        model = locker

class LockerModelAdmin(ImportExportModelAdmin):
    list_display = ['title', 'username']
    resource_class = LockerModelResource
    pass

####

#admin.site.register(LockVault, lockeradmin)
admin.site.register(Lockers, LockerModelAdmin)

