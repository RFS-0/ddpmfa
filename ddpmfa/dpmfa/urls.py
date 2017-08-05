from django.conf.urls import url
from . import views

app_name = 'dpmfa'
urlpatterns = [
    # ex: /home/
    url(r'(?:^$)|(?:^home/$)', views.HomeView.as_view(), name='home'),
    # ex: /project/
    url(r'^projects/$', views.ProjectsView.as_view(), name='projects'),
    # ex: /project/123
    url(r'^project/(?P<pk>[0-9]+)/$', views.ProjectView.as_view(), name='project'),
    # ex: /project/new
    url(r'^project/new/$', views.ProjectCreateView.as_view(), name='new_project'),
    # ex: /project/update
    url(r'^project/(?P<pk>[0-9]+)/edit/$', views.ProjectUpdateView.as_view(), name='update_project'),
    # ex: /project/123/delete
    url(r'^project/(?P<pk>[0-9]+)/delete/$', views.ProjectDeleteView.as_view(), name='delete_project'),
    # ex: /project/123/model/new
    url(r'^project/(?P<project_pk>[0-9]+)/model/new/$', views.ModelCreateView.as_view(), name='new_model'),

    # ex: /model/123
    url(r'^model/(?P<pk>[0-9]+)/$', views.ModelView.as_view(), name='model'),
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

#==============================================================================
#  Transfers
#==============================================================================

# Constant 

    # ex: /constant_transfer/123/detail
    url(r'^constant_transfer/(?P<pk>[0-9]+)/detail$', views.ConstantTransferDetailView.as_view(), name='constant-transfer-detail'),
    
    # ex: /constant_transfer/123/create
    url(r'^constant_transfer/(?P<pk>[0-9]+)/create$', views.ConstantTransferCreateView.as_view(), name='constant-transfer-detail'),
    
    # ex: /constant_transfer/123/update
    url(r'^constant_transfer/(?P<pk>[0-9]+)/update$', views.ConstantTransferUpdateView.as_view(), name='constant-transfer-detail'),
    
    # ex: /constant_transfer/123/delete
    url(r'^constant_transfer/(?P<pk>[0-9]+)/delete$', views.ConstantTransferDeleteView.as_view(), name='constant-transfer-detail'),
    
    
    
# Random Choice
   
    # ex: /random_choice_transfer/123/detail
    url(r'^random_choice_transfer/(?P<pk>[0-9]+)/detail$', views.RandomChoiceTransferDetailView.as_view(), name='random-choice-transfer-detail'),
    
    # ex: /random_choice_transfer/123/create
    url(r'^random_choice_transfer/(?P<pk>[0-9]+)/create$', views.RandomChoiceTransferCreateView.as_view(), name='random-choice-transfer-create'),
    
    # ex: /random_choice_transfer/123/update
    url(r'^random_choice_transfer/(?P<pk>[0-9]+)/update$', views.RandomChoiceTransferUpdateView.as_view(), name='random-choice-transfer-update'),
    
    # ex: /random_choice_transfer/123/delete
    url(r'^random_choice_transfer/(?P<pk>[0-9]+)/delete$', views.RandomChoiceTransferDeleteView.as_view(), name='random-choice-transfer-delete'),
    
# Aggregated
    
    # ex: /aggregated_transfer/123/detail
    url(r'^aggregated_transfer/(?P<pk>[0-9]+)/detail$', views.AggregatedTransferDetailView.as_view(), name='aggregated-transfer-detail'),
   
    # ex: /aggregated_transfer/123/create
    url(r'^aggregated_transfer/(?P<pk>[0-9]+)/create$', views.AggregatedTransferCreateView.as_view(), name='aggregated-transfer-create'),
   
    # ex: /aggregated_transfer/123/update
    url(r'^aggregated_transfer/(?P<pk>[0-9]+)/update$', views.AggregatedTransferUpdateView.as_view(), name='aggregated-transfer-update'),
   
    # ex: /aggregated_transfer/123/delete
    url(r'^aggregated_transfer/(?P<pk>[0-9]+)/delete$', views.AggregatedTransferDeleteView.as_view(), name='aggregated-transfer-delete'),
   
# Stochastic 
    
    # ex: /stochastic_transfer/123/detail
    url(r'^stochastic_transfer/(?P<pk>[0-9]+)/detail$', views.StochasticTransferDetailView.as_view(), name='stochastic-transfer'),
    
    # ex: /stochastic_transfer/123/create
    url(r'^stochastic_transfer/(?P<pk>[0-9]+)/create$', views.StochasticTransferCreateView.as_view(), name='stochastic-transfer'),
    
    # ex: /stochastic_transfer/123/update
    url(r'^stochastic_transfer/(?P<pk>[0-9]+)/update$', views.StochasticTransferUpdateView.as_view(), name='stochastic-transfer'),
    
    # ex: /stochastic_transfer/123/delete
    url(r'^stochastic_transfer/(?P<pk>[0-9]+)/delete$', views.StochasticTransferDeleteView.as_view(), name='stochastic-transfer'),

#==============================================================================
#  Simulation
#==============================================================================

    # ex: /simulation/12/detail
    url(r'^simulation/(?P<pk>[0-9]+)/detail', views.SimulationDetailView.as_view(), name='simulation'),
    
    # ex: /simulation/12/create
    url(r'^simulation/(?P<pk>[0-9]+)/create$', views.SimulationCreateView.as_view(), name='simulation'),
    
    # ex: /simulation/12/update
    url(r'^simulation/(?P<pk>[0-9]+)/update', views.SimulationUpdateView.as_view(), name='simulation'),
    
    # ex: /simulation/12/delete
    url(r'^simulation/(?P<pk>[0-9]+)/update$', views.SimulationDeleteView.as_view(), name='simulation'),

#==============================================================================
#  Results
#==============================================================================

    # ex: /model/123/results
    url(r'^model/(?P<pk>[0-9]+)/results/$', views.ResultsDetailView.as_view(), name='results'),

]