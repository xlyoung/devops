from django.conf.urls import url
from . import views

app_name = 'inspection'

urlpatterns = [
    url(r'select', views.get_ip, name='select'),
    url(r'$', views.inspection, name='inspection'),
]
