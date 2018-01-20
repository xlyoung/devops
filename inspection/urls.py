from django.conf.urls import url
from . import views

app_name = 'inspection'


urlpatterns = [
    url(r'^inspection/', views.inspection, name='inspection'),
]