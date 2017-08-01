from django.conf.urls import url
from . import views

app_name = 'dpmfa'
urlpatterns = [
    # ex: /home/
    url(r'(?:^$)|(?:^home/$)', views.home, name='home'),
    # ex: /administration/
    url(r'^administration/$', views.project_administration, name='project_administration'),
    # ex: /some_project_name/
    url(r'^(?P<project_name>[a-zA-Z0-9_]+)/$', views.project_overview, name='project_overview'),
    # ex: /some_project_name/model_overview
    url(r'^(?P<model_name>[a-zA-Z0-9_]+)/model_overview$', views.model_overview, name='model_overview'),
    # ex: /some_project_name/configuration
    url(r'^(?P<model_name>[a-zA-Z0-9_]+)/configuration', views.model_overview, name='model_configuration'),

    ]