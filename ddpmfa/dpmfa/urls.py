from django.conf.urls import url
from . import views

app_name = 'dpmfa'
urlpatterns = [
    
#==============================================================================
#  Home
#==============================================================================

    # ex: /home/
    url(r'(?:^$)|(?:^home$)', views.HomeTemplateView.as_view(), name='home'),
    
#==============================================================================
#  Project
#==============================================================================

    # ex: /projects/list
    url(r'^projects/list$', views.ProjectsListView.as_view(), name='projects'),
    
    # ex: /project/123/detail
    url(r'^project/(?P<pk>[0-9]+)/detail$', views.ProjectDetailView.as_view(), name='project-detail'),
    
    # ex: /project/create
    url(r'^project/create$', views.ProjectCreateView.as_view(), name='project-create'),
    
    # ex: /project/update
    url(r'^project/(?P<pk>[0-9]+)/update$', views.ProjectUpdateView.as_view(), name='project-update'),
    
    # ex: /project/123/delete
    url(r'^project/(?P<pk>[0-9]+)/delete$', views.ProjectDeleteView.as_view(), name='project-delete'),

#==============================================================================
#  Model
#==============================================================================

    # ex: /models/list
    url(r'^model/list$', views.ModelListView.as_view(), name='model'),
    
    # ex: /model/123/detail
    url(r'^model/(?P<pk>[0-9]+)/detail$', views.ModelCreateView.as_view(), name='model'),
    
    # ex: /model/create
    url(r'^model/create$', views.ModelDetailView.as_view(), name='model'),
    
    # ex: /model/update
    url(r'^model/(?P<model_pk>[0-9]+)/update', views.ModelUpdateView.as_view(), name='model'),
    
    # ex: /model/123/delete
    url(r'^model/(?P<model_pk>[0-9]+)/delete$', views.ModelDeleteView.as_view(), name='delete_model'),
    
#==============================================================================
#  Model Designer
#==============================================================================

    # ex: /designer/123/detail
    url(r'^designer/(?P<pk>[0-9]+)/detail$', views.ModelDesingerDetailView.as_view(), name='designer-detail'),
    
    # ex: /designer/create
    url(r'^designer/create$', views.ModelDesingerCreateView.as_view(), name='designer-create'),
    
    # ex: /designer/123/update
    url(r'^designer/(?P<pk>[0-9]+)/update$', views.ModelDesingerUpdateView.as_view(), name='designer-update'),

    # ex: /designer/123/delete
    url(r'^designer/(?P<pk>[0-9]+)/delete$', views.ModelDesingerDeleteView.as_view(), name='designer-update'),
    
#==============================================================================
#  Parameters
#==============================================================================

    # ex: /model/123/parameters
    url(r'^model/(?P<model_pk>[0-9]+)/parameters/$', views.ParametersDetailView.as_view(), name='parameters'),

#==============================================================================
#  Flow Compartment
#==============================================================================

    # ex: /flow_compartment/123
    url(r'^flow_compartment/(?P<flow_compartment_pk>[0-9]+)/$', views.FlowCompartmentDetailView.as_view(), name='flow_compartment'),
 
#==============================================================================
#  Sink
#==============================================================================

    # ex: /sink/123
    url(r'^sink/(?P<sink_pk>[0-9]+)/$', views.SinkDetailView.as_view(), name='sink'),
    
#==============================================================================
#  Stock
#==============================================================================

    # ex: /stock/123
    url(r'^stock/(?P<stock_pk>[0-9]+)/$', views.StockDetailView.as_view(), name='stock'),

#==============================================================================
#  External Inflows
#==============================================================================

# External Inflow

    # ex: /external_inflow/123/detail
    url(r'^external_inflow/(?P<pk>[0-9]+)/detail$', views.ExternalInflowDetailView.as_view(), name='constant-transfer-detail'),
    
    # ex: /external_inflow/123/create
    url(r'^external_inflow/(?P<pk>[0-9]+)/create$', views.ExternalInflowCreateView.as_view(), name='constant-transfer-detail'),
    
    # ex: /external_inflow/123/update
    url(r'^external_inflow/(?P<pk>[0-9]+)/update$', views.ExternalInflowUpdateView.as_view(), name='constant-transfer-detail'),
    
    # ex: /external_inflow/123/delete
    url(r'^external_inflow/(?P<pk>[0-9]+)/delete$', views.ExternalInflowDeleteView.as_view(), name='constant-transfer-detail'),
    
# External List Inflow

    # ex: /external_list_inflow/123/detail
    url(r'^external_list_inflow/(?P<pk>[0-9]+)/detail$', views.ExternalListInflowDetailView.as_view(), name='constant-transfer-detail'),
    
    # ex: /external_list_inflow/123/create
    url(r'^external_list_inflow/(?P<pk>[0-9]+)/create$', views.ExternalListInflowCreateView.as_view(), name='constant-transfer-detail'),
    
    # ex: /external_list_inflow/123/update
    url(r'^external_list_inflow/(?P<pk>[0-9]+)/update$', views.ExternalListInflowUpdateView.as_view(), name='constant-transfer-detail'),
    
    # ex: /external_list_inflow/123/delete
    url(r'^external_list_inflow/(?P<pk>[0-9]+)/delete$', views.ExternalListInflowDeleteView.as_view(), name='constant-transfer-detail'),

# External Function Inflow

    # ex: /external_function_inflow/123/detail
    url(r'^external_list_inflow/(?P<pk>[0-9]+)/detail$', views.ExternalFunctionInflowDetailView.as_view(), name='constant-transfer-detail'),
    
    # ex: /external_function_inflow/123/create
    url(r'^external_list_inflow/(?P<pk>[0-9]+)/create$', views.ExternalFunctionInflowCreateView.as_view(), name='constant-transfer-detail'),
    
    # ex: /external_function_inflow/123/update
    url(r'^external_list_inflow/(?P<pk>[0-9]+)/update$', views.ExternalFunctionInflowUpdateView.as_view(), name='constant-transfer-detail'),
    
    # ex: /external_function_inflow/123/delete
    url(r'^external_list_inflow/(?P<pk>[0-9]+)/delete$', views.ExternalFunctionInflowDeleteView.as_view(), name='constant-transfer-detail'),


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