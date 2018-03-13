from django.conf.urls import url
from . import views

app_name = 'cmdb'
urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^select', views.select, name='select'),
    url(r'^config_update', views.config_update, name='config'),
]