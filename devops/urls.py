#coding:utf-8

from django.conf.urls import include, url
from django.contrib import admin
from users import views as uviews
from inspection import views as iviews
from homepage import views as hviews


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('users.urls')),
    # 将 auth 应用中的 urls 模块包含进来(登陆、注销)
    url(r'^users/', include('django.contrib.auth.urls')),
    url(r'^index', hviews.index, name='index'),
    url(r'^inspection', iviews.inspection, name='index'),
    url(r'^$', hviews.index, name='index'),

    ]
