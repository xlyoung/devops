from django.conf.urls import url
from . import views

app_name = 'ansible_module'

urlpatterns = [
    # url(r'select', views.get_ip, name='select'),
    url(r'$', views.ansible_config, name='ansible_config'),
]
