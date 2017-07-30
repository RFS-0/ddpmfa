from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /home/
    url(r'^$', views.home, name='home'),
    # ex: /administration/
    url(r'^administration/$', views.project_administration, name='project_administration'),
    # ex: /some_project_name/
    url(r'^(?P<project_name>[a-z0-9_]+)/$', views.project_overview, name='project_overview'),
    # ex: /some_project_name/model_overview
    url(r'^(?P<project_name>[a-z0-9_]+)/model_overview$', views.model_overview, name='model_overview'),
    ]