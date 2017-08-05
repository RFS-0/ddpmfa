from django.conf.urls import url
from . import views

app_name = 'dpmfa'
urlpatterns = [
    # ex: /home/
    url(r'(?:^$)|(?:^home/$)', views.HomeView.as_view(), name='home'),
    # ex: /project/
    url(r'^projects/$', views.ProjectsView.as_view(), name='project_list'),
    # ex: /project/123
    url(r'^project/(?P<pk>[0-9]+)/$', views.ProjectView.as_view(), name='project'),
    # ex: /project/new
    url(r'^project/new/$', views.new_project, name='new_project'),
    # ex: /project/123/delete
    url(r'^project/(?P<project_pk>[0-9]+)/delete/$', views.delete_project, name='delete_project'),
    # ex: /project/123/model/new
    url(r'^project/(?P<project_pk>[0-9]+)/model/new/$', views.new_model, name='new_model'),

    # ex: /model/123
    url(r'^model/(?P<model_pk>[0-9]+)/$', views.model, name='model'),
    # ex: /model/123/delete
    url(r'^model/(?P<model_pk>[0-9]+)/delete/$', views.delete_model, name='delete_model'),
    # ex: /model/123/designer
    url(r'^model/(?P<model_pk>[0-9]+)/designer/$', views.designer, name='designer'),
    # ex: /model/123/designer/save
    url(r'^model/(?P<model_pk>[0-9]+)/designer/save/$', views.save_designer, name='save_designer'),
    # ex: /model/123/designer/update
    url(r'^model/(?P<model_pk>[0-9]+)/designer/update/$', views.update_designer, name='update_designer'),

    # ex: /model/123/parameters
    url(r'^model/(?P<model_pk>[0-9]+)/parameters/$', views.parameters, name='parameters'),

    # ex: /flow_compartment/123
    url(r'^flow_compartment/(?P<flow_compartment_pk>[0-9]+)/$', views.flow_compartment, name='flow_compartment'),
    # ex: /sink/123
    url(r'^sink/(?P<sink_pk>[0-9]+)/$', views.sink, name='sink'),
    # ex: /stock/123
    url(r'^stock/(?P<stock_pk>[0-9]+)/$', views.stock, name='stock'),

    # ex: /list_inflow/123
    url(r'^list_inflow/(?P<inflow_pk>[0-9]+)/$', views.list_inflow, name='list_inflow'),
    # ex: /function_inflow/123
    url(r'^function_inflow/(?P<inflow_pk>[0-9]+)/$', views.function_inflow, name='function_inflow'),

    # ex: /constant_transfer/123
    url(r'^constant_transfer/(?P<transfer_pk>[0-9]+)/$', views.constant_transfer, name='constant_transfer'),
    # ex: /random_choice_transfer/123
    url(r'^random_choice_transfer/(?P<transfer_pk>[0-9]+)/$', views.random_choice_transfer, name='random_choice_transfer'),
    # ex: /aggregated_transfer/123
    url(r'^aggregated_transfer/(?P<transfer_pk>[0-9]+)/$', views.aggregated_transfer, name='aggregated_transfer'),
    # ex: /stochastic_transfer/123
    url(r'^stochastic_transfer/(?P<transfer_pk>[0-9]+)/$', views.stochastic_transfer, name='stochastic_transfer'),

    # ex: /model/123/simulation
    url(r'^model/(?P<model_pk>[0-9]+)/simulation/$', views.simulation, name='simulation'),
    # ex: /model/123/simulation/run
    url(r'^model/(?P<model_pk>[0-9]+)/simulation/run/$', views.run_simulation, name='run_simulation'),

    # ex: /model/123/results
    url(r'^model/(?P<model_pk>[0-9]+)/results/$', views.results, name='results'),

]