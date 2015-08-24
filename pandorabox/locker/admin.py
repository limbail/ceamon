from django.contrib import admin, messages
from locker import models as m
from locker.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from os import urandom
from base64 import b64encode, b64decode
from django.db import models
from Crypto.Cipher import ARC4

def get_value(name):
    def f(self):
        return locker.decrypt(getattr(self, 'e_%s'%name))
    return f

def set_value(name):
    def f(self, value):
        setattr(self, 'e_%s'%name, locker.encrypt(value))
    return f

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
    list_display = ['title', 'e_username', 'e_password', 'e_url',]
    resource_class = LockerModelResource

    def save_model(self, request, obj, form, change):
        try:
            username = request.GET.get('', str(obj.e_username))
            password = request.GET.get('', str(obj.e_password))
            url = request.GET.get('', str(obj.e_url))
            notes = request.GET.get('', str(obj.e_notes))
            obj.username = username
            obj.password = password
            obj.url = url
            obj.notes = notes
            obj.save()
            messages.success(request,'Locker has been added')
        except:
            messages.error(request,'You cant modify objects with encrypted data, delete the encrypted data or create a new object')

####

#admin.site.register(LockVault, lockeradmin)
admin.site.register(Lockers, LockerModelAdmin)

