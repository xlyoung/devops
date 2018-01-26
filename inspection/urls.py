from django.conf.urls import url
from . import views

app_name = 'inspection'

urlpatterns = [
    url(r'select', views.index, name='select'),
    url(r'$', views.inspection, name='inspection'),

]
