from django.conf.urls import url
from . import views

app_name = 'cmdb'
urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^select', views.select, name='select'),
    url(r'^config', views.add_config, name='config'),
    # url(r'^config_update', views.config_update, name='config'),
    url(r'^add_host', views.add_host, name='add_host'),
    url(r'^query_resource', views.query_resource, name='query_resource'),
]