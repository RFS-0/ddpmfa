from django.conf.urls import url
from . import views

app_name = 'dpmfa'
urlpatterns = [
    
# ==============================================================================
# Home
# ==============================================================================

    # ex: /dpmfa
    # ex: dpmfa/home/
    url(r'^$', views.HomeTemplateView.as_view(), name='default'),
    url(r'^home/$', views.HomeTemplateView.as_view(), name='home'),
    
    # ex: dpmfa/example
    url(r'^example/$', views.ExampleTemplateView.as_view(), name='example'),
    
    # ex: dpmfa/quick_reference
    url(r'^quick_reference/$', views.QuickReferenceTemplateView.as_view(), name='quick-reference'),
    
    # ex: dpmfa/documentation
    url(r'^documentation/$', views.DocumentationTemplateView.as_view(), name='documentation'),
    

# ==============================================================================
# Project
# ==============================================================================

    # ex: /projects/list
    url(r'^project/list$', views.ProjectListView.as_view(), name='project-list'),
    
    # ex: /project/123/detail
    url(r'^project/(?P<pk>[0-9]+)/detail$', views.ProjectDetailView.as_view(), name='project-detail'),
    
    # ex: /project/create
    url(r'^project/create$', views.ProjectCreateView.as_view(), name='project-create'),
    
    # ex: /project/update
    url(r'^project/(?P<pk>[0-9]+)/update$', views.ProjectUpdateView.as_view(), name='project-update'),
    
    # ex: /project/123/delete
    url(r'^project/(?P<pk>[0-9]+)/delete$', views.ProjectDeleteView.as_view(), name='project-delete'),

# ==============================================================================
# Model
# ==============================================================================

    # # ex: /models/list
    # url(r'^model/list$', views.ModelListView.as_view(), name='model'),
    
    # ex: /model/123/detail
    url(r'^model/(?P<pk>[0-9]+)/detail$', views.ModelDetailView.as_view(), name='model-detail'),
    
    
    # ex: /model/create
    url(r'^model/create/(?P<project_pk>[0-9]+)$', views.ModelCreateView.as_view(), name='model-create'),
    
    # ex: /model/update
    url(r'^model/(?P<pk>[0-9]+)/update', views.ModelUpdateView.as_view(), name='model-update'),
    
    # ex: /model/123/delete
    url(r'^model/(?P<pk>[0-9]+)/delete$', views.ModelDeleteView.as_view(), name='model-delete'),
    
#==============================================================================
#  Model Designer
#==============================================================================

    # ex: /designer/123/detail
    #url(r'^designer/(?P<pk>[0-9]+)/detail$', views.ModelDesingerDetailView.as_view(), name='designer-detail'),
    
    # ex: /designer/create
    url(r'^designer/create/(?P<model_pk>[0-9]+)$', views.ModelDesingerCreateView.as_view(), name='designer-create'),
    
    # ex: /designer/123/update
    url(r'^designer/(?P<pk>[0-9]+)/update$', views.ModelDesingerUpdateView.as_view(), name='designer-update'),

    # ex: /designer/123/delete
    url(r'^designer/(?P<pk>[0-9]+)/delete$', views.ModelDesingerDeleteView.as_view(), name='designer-delete'),
    
    # only for redirection
    url(r'designer/(?P<model_pk>[0-9]+)/redirect$', views.ModelDesignerRedirectView.as_view(), name='designer-redirect'),
    
#==============================================================================
#  Model Parameters
#==============================================================================

    # ex: /model/123/parameters
    url(r'^model/(?P<model_pk>[0-9]+)/parameters/$', views.ParametersDetailView.as_view(), name='parameters'),

#==============================================================================
#  Compartment
#==============================================================================

    # only for redirection
    url(r'compartment/(?P<compartment_pk>[0-9]+)/redirect$', views.CompartmentRedirectView.as_view(), name='compartment-redirect'),

    # # ex: /compartment/12/detail
    # url(r'^compartment/(?P<model_pk>[0-9]+)/detail$', views.CompartmentDetailView.as_view(), name='compartment-detail'),

    # # ex: /compartment/create
    # url(r'^compartment/create$', views.CompartmentCreateView.as_view(), name='compartment-detail'),

    # # ex: /compartment/12/update
    # url(r'^compartment/(?P<model_pk>[0-9]+)/update', views.CompartmentUpdateView.as_view(), name='compartment-detail'),

    # # ex: /compartment/12/delete
    # url(r'^compartment/(?P<model_pk>[0-9]+)/delete', views.CompartmentDeleteView.as_view(), name='compartment-detail'),


#==============================================================================
#  Flow Compartment
#==============================================================================

    # ex: /flow_compartment/123/detail
    url(r'^flow_compartment/(?P<pk>[0-9]+)/detail$', views.FlowCompartmentDetailView.as_view(), name='flow-compartment-detail'),
 
    # ex: /flow_compartment/create
    #url(r'^flow_compartment/create$', views.FlowCompartmentCreateView.as_view(), name='flow-compartment-create'),
 
    # ex: /flow_compartment/123/update
    url(r'^flow_compartment/(?P<pk>[0-9]+)/update$', views.FlowCompartmentUpdateView.as_view(), name='flow-compartment-update'),
 
    # ex: /flow_compartment/123/delete
    url(r'^flow_compartment/(?P<pk>[0-9]+)/delete$', views.FlowCompartmentDeleteView.as_view(), name='flow-compartment-delete'),
    
#==============================================================================
#  Stock
#==============================================================================

    # ex: /stock/123/detail
    url(r'^stock/(?P<pk>[0-9]+)/detail$', views.StockDetailView.as_view(), name='stock-detail'),
 
    # ex: /stock/create
    #url(r'^stock/create$', views.StockCreateView.as_view(), name='stock-create'),
    
    # ex: /stock/123/update
    url(r'^stock/(?P<pk>[0-9]+)/update', views.StockUpdateView.as_view(), name='stock-update'),
 
    # ex: /stock/123/delete
    url(r'^stock/(?P<pk>[0-9]+)/delete', views.StockDeleteView.as_view(), name='stock-delete'),
 
#==============================================================================
#  Sink
#==============================================================================

    # ex: /sink/123/detail
    url(r'^sink/(?P<pk>[0-9]+)/detail$', views.SinkDetailView.as_view(), name='sink-detail'),

    # ex: /sink/create
    #url(r'^sink/create$', views.SinkCreateView.as_view(), name='sink-create'),
    
    # ex: /sink/123/update
    url(r'^sink/(?P<pk>[0-9]+)/update$', views.SinkUpdateView.as_view(), name='sink-update'),

    # ex: /sink/123
    url(r'^sink/(?P<pk>[0-9]+)/delete$', views.SinkDeleteView.as_view(), name='sink-delete'),

#==============================================================================
#  Releases
#==============================================================================

    # ex: /local_release/123/detail
    url(r'^local_release/(?P<pk>[0-9]+)/detail$', views.LocalReleaseDetailView.as_view(), name='local-release-detail'),

    # ex: /local_release/123/update
    url(r'^local_release/(?P<pk>[0-9]+)/update$', views.LocalReleaseUpdateView.as_view(), name='local-release-update'),
    
    # ex: /fixed_rate_release/123/detail
    url(r'^fixed_rate_release/(?P<pk>[0-9]+)/detail$', views.FixedRateReleaseDetailView.as_view(), name='fixed-release-detail'),
    
    # ex: /fixed_rate_release/123/update
    url(r'^fixed_rate_release/(?P<pk>[0-9]+)/update$', views.FixedRateReleaseUpdateView.as_view(), name='fixed-release-update'),

    # ex: /function_release/123/detail
    url(r'^function_release/(?P<pk>[0-9]+)/detail$', views.FunctionReleaseDetailView.as_view(), name='function-release-detail'),

    # ex: /function_release/123/detail
    url(r'^function_release/(?P<pk>[0-9]+)/update$', views.FunctionReleaseUpdateView.as_view(), name='function-release-detail'),
    
#==============================================================================
#  Transfers
#==============================================================================

    # only for redirection
    url(r'transfer/(?P<transfer_pk>[0-9]+)/redirect$', views.TransferRedirectView.as_view(), name='transfer-redirect'),

    # Constant

    # ex: /constant_transfer/123/detail
    url(r'^constant_transfer/(?P<pk>[0-9]+)/detail$', views.ConstantTransferDetailView.as_view(), name='constant-transfer-detail'),
    
    # ex: /constant_transfer/123/create
    #url(r'^constant_transfer/(?P<pk>[0-9]+)/create$', views.ConstantTransferCreateView.as_view(), name='constant-transfer-create'),
    
    # ex: /constant_transfer/123/update
    url(r'^constant_transfer/(?P<pk>[0-9]+)/update$', views.ConstantTransferUpdateView.as_view(), name='constant-transfer-update'),
    
    # ex: /constant_transfer/123/delete
    url(r'^constant_transfer/(?P<pk>[0-9]+)/delete$', views.ConstantTransferDeleteView.as_view(), name='constant-transfer-delete'),
    
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
    url(r'^stochastic_transfer/(?P<pk>[0-9]+)/detail$', views.StochasticTransferDetailView.as_view(), name='stochastic-transfer-detail'),
    
    # ex: /stochastic_transfer/123/create
    url(r'^stochastic_transfer/(?P<pk>[0-9]+)/create$', views.StochasticTransferCreateView.as_view(), name='stochastic-transfer-create'),
    
    # ex: /stochastic_transfer/123/update
    url(r'^stochastic_transfer/(?P<pk>[0-9]+)/update$', views.StochasticTransferUpdateView.as_view(), name='stochastic-transfer-update'),
    
    # ex: /stochastic_transfer/123/delete
    url(r'^stochastic_transfer/(?P<pk>[0-9]+)/delete$', views.StochasticTransferDeleteView.as_view(), name='stochastic-transfer-delete'),

#==============================================================================
#  External Inflows
#==============================================================================

    # External Inflow

    # # ex: /external_inflow/123/detail
    # url(r'^external_inflow/(?P<pk>[0-9]+)/detail$', views.ExternalInflowDetailView.as_view(), name='constant-transfer-detail'),

    # # ex: /external_inflow/123/create
    # url(r'^external_inflow/(?P<pk>[0-9]+)/create$', views.ExternalInflowCreateView.as_view(), name='constant-transfer-detail'),

    # # ex: /external_inflow/123/update
    # url(r'^external_inflow/(?P<pk>[0-9]+)/update$', views.ExternalInflowUpdateView.as_view(), name='constant-transfer-detail'),

    # # ex: /external_inflow/123/delete
    # url(r'^external_inflow/(?P<pk>[0-9]+)/delete$', views.ExternalInflowDeleteView.as_view(), name='constant-transfer-detail'),
    
    # External List Inflow

    # ex: /external_list_inflow/123/detail
    url(r'^external_list_inflow/(?P<pk>[0-9]+)/detail$', views.ExternalListInflowDetailView.as_view(), name='external-list-inflow-detail'),
    
    # ex: /external_list_inflow/123/create
    url(r'^external_list_inflow/create$', views.ExternalListInflowCreateView.as_view(), name='external-list-inflow-create'),
    
    # ex: /external_list_inflow/123/update
    url(r'^external_list_inflow/(?P<pk>[0-9]+)/update$', views.ExternalListInflowUpdateView.as_view(), name='external-list-inflow-update'),
    
    # ex: /external_list_inflow/123/delete
    url(r'^external_list_inflow/(?P<pk>[0-9]+)/delete$', views.ExternalListInflowDeleteView.as_view(), name='external-list-inflow-delete'),

    # External Function Inflow

    # ex: /external_function_inflow/123/detail
    url(r'^external_function_inflow/(?P<pk>[0-9]+)/detail$', views.ExternalFunctionInflowDetailView.as_view(), name='external-function-inflow-detail'),
    
    # ex: /external_function_inflow/123/create
    url(r'^external_function_inflow/create$', views.ExternalFunctionInflowCreateView.as_view(), name='external-function-inflow-create'),
    
    # ex: /external_function_inflow/123/update
    url(r'^external_function_inflow/(?P<pk>[0-9]+)/update$', views.ExternalFunctionInflowUpdateView.as_view(), name='external-function-inflow-update'),
    
    # ex: /external_function_inflow/123/delete
    url(r'^external_function_inflow/(?P<pk>[0-9]+)/delete$', views.ExternalFunctionInflowDeleteView.as_view(), name='external-function-inflow-delete'),

#==============================================================================
#  Single Period Inflow
#==============================================================================

    # only for redirection
    url(r'single_period_inflow/(?P<single_period_inflow_pk>[0-9]+)/redirect$', views.SinglePeriodInflowRedirectView.as_view(), name='single-period-inflow-redirect'),

#==============================================================================
#  Fixed Value Inflow
#==============================================================================

    url(r'^fixed_value_inflow/(?P<pk>[0-9]+)/detail$', views.FixedValueInflowDetailView.as_view(), name='fixed-value-inflow-detail'),

    url(r'^fixed_value_inflow/(?P<pk>[0-9]+)/update', views.FixedValueInflowUpdateView.as_view(), name='fixed-value-inflow-update'),

    url(r'^fixed_value_inflow/(?P<pk>[0-9]+)/delete', views.FixedValueInflowDeleteView.as_view(), name='fixed-value-inflow-delete'),

    url(r'^fixed_value_inflow/(?P<pk>[0-9]+)/(?P<previous_period>[0-9]+)/create$', views.FixedValueInflowCreateView.as_view(), name='fixed-value-inflow-create'),

#==============================================================================
#  Random Choice Inflow
#==============================================================================

    url(r'^random_choice_inflow/(?P<pk>[0-9]+)/detail$', views.RandomChoiceInflowDetailView.as_view(), name='random-choice-inflow-detail'),

    url(r'^random_choice_inflow/(?P<pk>[0-9]+)/update', views.RandomChoiceInflowUpdateView.as_view(), name='random-choice-inflow-update'),

    url(r'^random_choice_inflow/(?P<pk>[0-9]+)/delete', views.RandomChoiceInflowDeleteView.as_view(), name='random-choice-inflow-delete'),

    url(r'^random_choice_inflow/(?P<external_list_inflow_pk>[0-9]+)/(?P<previous_period>[0-9]+)/create$', views.RandomChoiceInflowCreateView.as_view(), name='random-choice-inflow-create'),

#==============================================================================
#  Stochastic Function Inflow
#==============================================================================

#     url(r'^stochastic_function_inflow/(?P<pk>[0-9]+)/detail$', views.StochasticFunctionInflowDetailView.as_view(), name='stochastic-function-inflow-detail'),

    url(r'^stochastic_function_inflow/(?P<pk>[0-9]+)/update', views.StochasticFunctionInflowUpdateView.as_view(), name='stochastic-function-inflow-update'),

    url(r'^stochastic_function_inflow/(?P<pk>[0-9]+)/delete', views.StochasticFunctionInflowDeleteView.as_view(), name='stochastic-function-inflow-delete'),

    url(r'^stochastic_function_inflow/(?P<external_list_inflow_pk>[0-9]+)/(?P<previous_period>[0-9]+)/create$', views.StochasticFunctionInflowCreateView.as_view(), name='stochastic-function-inflow-create'),

#==============================================================================
#  Simulation
#==============================================================================

    # ex: /simulation/12/detail
    url(r'^simulation/(?P<pk>[0-9]+)/detail', views.SimulationDetailView.as_view(), name='simulation-detail'),
    
    # ex: /simulation/create
    url(r'^simulation/create/(?P<model_pk>[0-9]+)$', views.SimulationCreateView.as_view(), name='simulation-create'),
    
    # ex: /simulation/12/update
    url(r'^simulation/(?P<pk>[0-9]+)/update', views.SimulationUpdateView.as_view(), name='simulation-update'),
    
    # ex: /simulation/12/delete
    url(r'^simulation/(?P<pk>[0-9]+)/delete$', views.SimulationDeleteView.as_view(), name='simulation-delete'),
    
    # ex: /simulation/12/run
    url(r'^simulation/(?P<model_pk>[0-9]+)/run$', views.SimulationRunView.as_view(), name='simulation-run'),

#==============================================================================
#  Results
#==============================================================================

    # ex: /result/123
    url(r'^result/(?P<pk>[0-9]+)/$', views.ResultsDetailView.as_view(), name='result-detail'),

    # ex: /result/123/delete
    url(r'^result/(?P<pk>[0-9]+)/delete$', views.ResultsDeleteView.as_view(), name='result-delete'),
]