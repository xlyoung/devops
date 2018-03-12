#coding:utf-8

from django.conf.urls import include, url
from django.contrib import admin



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('users.urls' ,namespace="users")),
    # 将 auth 应用中的 urls 模块包含进来(登陆、注销)
    url(r'^users/', include('django.contrib.auth.urls')),
    url(r'^homepage/', include('homepage.urls' ,namespace="homepage")),
    url(r'^inspection/', include('inspection.urls' , namespace="inspection")),
    url(r'^cmdb/', include('cmdb.urls' , namespace="cmdb")),
    ]
