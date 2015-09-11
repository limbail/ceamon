"""pandorabox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
#### Imports
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers, serializers, viewsets
import overview.views
import systemlist.views
import main.views as vi_main
import locker.views
import ceamon.views
from ceamon.models import sapnode
from django.views.generic import TemplateView
from ceamon.views import sapnode_list 
from todo.views import w_problem_View

from django.conf.urls import url, include
from rest_framework import routers
from ceamon import views

router = routers.DefaultRouter()
router.register(r'users', ceamon.views.UserViewSet)
router.register(r'groups', ceamon.views.GroupViewSet)

admin.autodiscover()
##### 
admin.site.site_header = 'CEAMON - Administration'

"""
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^overview/', views.overview, name='overview'),
    (r'^login/$', 'auth.views.login_user'),
]

    url(r'^overview/', vi_overview.overview, name='overview'),

"""
# ex: url(r'^admin/', include("someUrlpattern", namespace="admin"))
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$', vi_main.main, name='main'),
    (r'^login/$', 'auth.views.login_user'),
    url(r'^overview/$', 'overview.views.overview', name='overview'),
    url(r'^logout/$', 'auth.views.logout_user', name='logout'),
    url(r'^systemlist/$', systemlist.views.systemlist, name='systemlist'),
    url(r'^locker/$', locker.views.LockerView, name='locker'),
### TESTS:
    url(r'^todo/$', w_problem_View, name='todo'),
    url(r'^sapnode/$', ceamon.views.sapnode_list, name='sapnodelist'),
    url(r'^sapnode/(?P<pk>[0-9]+)/$', ceamon.views.sapnode_detail, name='sapnodedetail'),
    url(r'^status/$', ceamon.views.StatusViewSet, name='status'),
    url(r'^status/(?P<pk>[0-9]+)/$', ceamon.views.status_detail, name='statusdetail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^sapnode/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
