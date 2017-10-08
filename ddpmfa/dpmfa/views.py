import dpmfa.converter as converter
import dpmfa.forms as forms
import dpmfa.models as models
import csv
import json
import os


from dpmfa.modelcopier import ModelCopier
from dpmfa.model2json.Model import Model as JsonModel

from django.contrib import messages
from django.http import HttpResponse
from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy, reverse
from itertools import chain
from dpmfa.dpmfa_simulator_0_921.dpmfa_simulator import components as package_components
from django.conf import settings

# ==============================================================================
#  Home
# ==============================================================================


class HomeTemplateView(generic.TemplateView):
    template_name = 'dpmfa/home/home.html'
    
class ExampleTemplateView(generic.TemplateView):
    template_name = 'dpmfa/home/example.html'

class QuickReferenceTemplateView(generic.TemplateView):
    template_name = 'dpmfa/home/quick_reference.html'
    
class DocumentationTemplateView(generic.TemplateView):
    template_name = 'dpmfa/home/documentation.html'
    

# ==============================================================================
#  Project
# ==============================================================================


class ProjectListView(generic.ListView):
    model = models.project
    context_object_name = 'projects'
    template_name = 'dpmfa/project/project_list.html'


class ProjectDetailView(generic.DetailView):
    
    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['prototype_models'] = models.model.objects.filter(model_instance=None)
        return context

    model = models.project
    form_class = forms.ProjectForm
    context_object_name = 'project'
    template_name = 'dpmfa/project/project_detail.html'


class ProjectCreateView(generic.CreateView):
    model = models.project
    form_class = forms.ProjectForm
    template_name = 'dpmfa/project/project_form.html'
    success_url = reverse_lazy('dpmfa:project-list')


class ProjectUpdateView(generic.UpdateView):
    model = models.project
    form_class = forms.ProjectForm
    template_name = 'dpmfa/project/project_form.html'
    success_url = reverse_lazy('dpmfa:project-list')
    
class ProjectDeleteView(generic.DeleteView):
    model = models.project
    form_class = forms.ProjectForm
    template_name = 'dpmfa/project/project_confirm_delete.html'
    success_url = reverse_lazy('dpmfa:project-list')


# ==============================================================================
#  Model
# ==============================================================================


# class ModelListView(generic.ListView):
#     model = models.model
#     template_name = 'dpmfa/model_list.html'


class ModelDetailView(generic.DetailView):
    model = models.model
    template_name = 'dpmfa/model/model_detail.html'

    def find_flow_compartments_by_model(self, model_pk):
        return models.flow_compartment.objects.filter(model=model_pk)
    
    def find_stocks_by_model(self, model_pk):
        return models.stock.objects.filter(model=model_pk)
    
    def find_sinks_by_model(self, model_pk):
        return models.sink.objects.filter(model=model_pk)
    
    def find_external_list_inflows_by_model(self, model_pk):
        return models.external_list_inflow.objects.filter(target__model=model_pk)
    
    def find_external_function_inflows_by_model(self, model_pk):
        return models.external_function_inflow.objects.filter(target__model=model_pk)
    
    def find_single_period_inflows_by_external_list_inflow(self, model_pk):
        external_list_inflows = models.external_list_inflow.objects.filter(target__model=model_pk)
        single_period_inflows_of_external_list_inflow = {}
        for external_list_inflow in external_list_inflows:
            qs = external_list_inflow.single_period_inflows.get_queryset()
            single_period_inflows = []
            for single_period_inflow in qs:
                if len(models.fixed_value_inflow.objects.filter(pk=single_period_inflow.pk)) > 0:
                    single_period_inflows.append(models.fixed_value_inflow.objects.get(pk=single_period_inflow.pk))
                elif len(models.stochastic_function_inflow.objects.filter(pk=single_period_inflow.pk)) > 0:
                    single_period_inflows.append(models.stochastic_function_inflow.objects.get(pk=single_period_inflow.pk))
                elif len(models.random_choice_inflow.objects.filter(pk=single_period_inflow.pk)) > 0:
                    single_period_inflows.append(models.random_choice_inflow.objects.get(pk=single_period_inflow.pk))
                else:
                    print("Could not retrieve a compartment for inflow")
            single_period_inflows.sort(key=lambda x: x.period)
            single_period_inflows_of_external_list_inflow[external_list_inflow.pk] = single_period_inflows
        return single_period_inflows_of_external_list_inflow

    def find_constant_transfers_by_model(self, model_pk, not_in_aggregated):
        if not_in_aggregated:
            return models.constant_transfer.objects.filter(target__model=model_pk, belongs_to_aggregated_transfer__id__isnull=False)
        else:
            return models.constant_transfer.objects.filter(target__model=model_pk)

    def find_random_choice_transfers_by_model(self, model_pk, not_in_aggregated):
        if not_in_aggregated:
            return models.random_choice_transfer.objects.filter(target__model=model_pk, belongs_to_aggregated_transfer__id__isnull=False)
        else:
            return models.random_choice_transfer.objects.filter(target__model=model_pk)

    def find_stochastic_transfers_by_model(self, model_pk, not_in_aggregated):
        if not_in_aggregated:
            return models.stochastic_transfer.objects.filter(target__model=model_pk, belongs_to_aggregated_transfer__id__isnull=False)
        else:
            return models.stochastic_transfer.objects.filter(target__model=model_pk)

    def find_aggregated_transfers_by_model(self, model_pk, not_in_aggregated):
        if not_in_aggregated:
            return models.aggregated_transfer.objects.filter(target__model=model_pk, belongs_to_aggregated_transfer__id__isnull=False)
        else:
            return models.aggregated_transfer.objects.filter(target__model=model_pk)
    
    def find_transfers_by_flow_compartment(self, model_pk):
        flow_compartments = models.flow_compartment.objects.filter(model=model_pk)
        transfers_of_flow_compartment = {}
        for flow_compartment in flow_compartments:
            qs = flow_compartment.transfers.get_queryset()
            transfers = []
            for transfer in qs:
                transfers.append(transfer)
            transfers.sort(key=lambda t: t.priority)
            transfers_of_flow_compartment[flow_compartment.pk] = transfers
        return transfers_of_flow_compartment
    
    def find_transfers_by_stock(self, model_pk):
        stocks = models.stock.objects.filter(model=model_pk)
        stock_transfers = {}
        for stock in stocks:
            qs = stock.transfers.get_queryset()
            stock_transfers[stock.pk] = qs
        return stock_transfers
    
    def find_transfers_by_sink(self, model_pk):
        sinks = models.sink.objects.filter(model=model_pk)
        sink_transfers = {}
        for sink in sinks:
            qs = sink.transfers.get_queryset()
            sink_transfers[sink.pk] = qs
        return sink_transfers
    
    def find_simulation_by_model(self, model_pk):
        try:
            simulation = models.simulation.objects.get(model=model_pk)
            return simulation
        except:
            return None

    def find_result_by_model(self, model_pk):
        return models.result.objects.filter(model=model_pk)
    
    def find_experiments_by_model(self, model_pk):
        return models.experiment.objects.filter(prototype_model=model_pk)

    def get_context_data(self, **kwargs):
        context = super(ModelDetailView, self).get_context_data(**kwargs)

        context['flow_compartments'] = self.find_flow_compartments_by_model(self.object.pk)
        context['transfers_of_flow_compartment'] = self.find_transfers_by_flow_compartment(self.object.pk)
        context['stocks'] = self.find_stocks_by_model(self.object.pk)
        context['transfers_of_stock'] = self.find_transfers_by_stock(self.object.pk)
        context['sinks'] = self.find_sinks_by_model(self.object.pk)
        context['transfers_of_sink'] = self.find_transfers_by_sink(self.object.pk)
        
        context['constant_transfers'] = self.find_constant_transfers_by_model(self.object.pk, False)
        context['random_choice_transfers'] = self.find_random_choice_transfers_by_model(self.object.pk, False)
        context['stochastic_transfers'] = self.find_stochastic_transfers_by_model(self.object.pk, False)
        context['aggregated_transfers'] = self.find_aggregated_transfers_by_model(self.object.pk, False)
        
        context['external_list_inflows'] = self.find_external_list_inflows_by_model(self.object.pk)
        context['single_period_inflows'] = self.find_single_period_inflows_by_external_list_inflow(self.object.pk)
        context['external_function_inflows'] = self.find_external_function_inflows_by_model(self.object.pk)
        
        context['experiments'] = self.find_experiments_by_model(self.object.pk)
        context['check_models'] = models.model.objects.all()
        
        return context
    
class ModelInstanceReadOnlyView(generic.DetailView):
    
    model = models.model_instance
    template_name = 'dpmfa/model_instance/model_instance_detail.html'

    def find_external_list_inflows_by_model_instance(self, model_instance_pk):
        return models.external_list_inflow.objects.filter(target__model=model_instance_pk)
    
    def find_single_period_inflows_by_external_list_inflow(self, model_instance_pk):
        external_list_inflows = models.external_list_inflow.objects.filter(target__model=model_instance_pk)
        single_period_inflows_of_external_list_inflow = {}
        for external_list_inflow in external_list_inflows:
            qs = external_list_inflow.single_period_inflows.get_queryset()
            single_period_inflows = []
            for single_period_inflow in qs:
                single_period_inflows.append(single_period_inflow)
            single_period_inflows.sort(key=lambda x: x.period)
            single_period_inflows_of_external_list_inflow[external_list_inflow.pk] = single_period_inflows
        return single_period_inflows_of_external_list_inflow

    def find_external_function_inflows_by_model(self, model_instance_pk):
        return models.external_function_inflow.objects.filter(target__model=model_instance_pk)

    def find_constant_transfers_by_model(self, model_instance_pk, not_in_aggregated):
        if not_in_aggregated:
            return models.constant_transfer.objects.filter(target__model=model_instance_pk, belongs_to_aggregated_transfer__id__isnull=False)
        else:
            return models.constant_transfer.objects.filter(target__model=model_instance_pk)

    def find_random_choice_transfers_by_model(self, model_instance_pk, not_in_aggregated):
        if not_in_aggregated:
            return models.random_choice_transfer.objects.filter(target__model=model_instance_pk, belongs_to_aggregated_transfer__id__isnull=False)
        else:
            return models.random_choice_transfer.objects.filter(target__model=model_instance_pk)

    def find_stochastic_transfers_by_model(self, model_instance_pk, not_in_aggregated):
        if not_in_aggregated:
            return models.stochastic_transfer.objects.filter(target__model=model_instance_pk, belongs_to_aggregated_transfer__id__isnull=False)
        else:
            return models.stochastic_transfer.objects.filter(target__model=model_instance_pk)

    def find_aggregated_transfers_by_model(self, model_instance_pk, not_in_aggregated):
        if not_in_aggregated:
            return models.aggregated_transfer.objects.filter(target__model=model_instance_pk, belongs_to_aggregated_transfer__id__isnull=False)
        else:
            return models.aggregated_transfer.objects.filter(target__model=model_instance_pk)

    def find_flow_compartments_by_model(self, model_instance_pk):
        return models.flow_compartment.objects.filter(model=model_instance_pk)
    
    def find_transfers_by_flow_compartment(self, model_instance_pk):
        flow_compartments = models.flow_compartment.objects.filter(model=model_instance_pk)
        transfers_of_flow_compartment = {}
        for flow_compartment in flow_compartments:
            qs = flow_compartment.transfers.get_queryset()
            transfers = []
            for transfer in qs:
                transfers.append(transfer)
            transfers.sort(key=lambda t: t.priority)
            transfers_of_flow_compartment[flow_compartment.pk] = transfers
        return transfers_of_flow_compartment

    def find_stocks_by_model(self, model_instance_pk):
        return models.stock.objects.filter(model=model_instance_pk)
    
    def find_transfers_by_stock(self, model_instance_pk):
        stocks = models.stock.objects.filter(model=model_instance_pk)
        stock_transfers = {}
        for stock in stocks:
            qs = stock.transfers.get_queryset()
            stock_transfers[stock.pk] = qs
        return stock_transfers

    def find_sinks_by_model(self, model_instance_pk):
        return models.sink.objects.filter(model=model_instance_pk)
    
    def find_transfers_by_sink(self, model_instance_pk):
        sinks = models.sink.objects.filter(model=model_instance_pk)
        sink_transfers = {}
        for sink in sinks:
            qs = sink.transfers.get_queryset()
            sink_transfers[sink.pk] = qs
        return sink_transfers
    
    
    def find_simulation_by_model(self, model_instance_pk):
        try:
            simulation = models.simulation.objects.get(model=model_instance_pk)
            return simulation
        except:
            return None

    def find_result_by_model(self, model_instance_pk):
        return models.result.objects.filter(model=model_instance_pk)
    
    def get_context_data(self, **kwargs):
        context = super(ModelInstanceReadOnlyView, self).get_context_data(**kwargs)

        context['flow_compartments'] = self.find_flow_compartments_by_model(self.object.pk)
        context['transfers_of_flow_compartment'] = self.find_transfers_by_flow_compartment(self.object.pk)
        context['stocks'] = self.find_stocks_by_model(self.object.pk)
        context['transfers_of_stock'] = self.find_transfers_by_stock(self.object.pk)
        context['sinks'] = self.find_sinks_by_model(self.object.pk)
        context['transfers_of_sink'] = self.find_transfers_by_sink(self.object.pk)
        
        context['constant_transfers'] = self.find_constant_transfers_by_model(self.object.pk, False)
        context['random_choice_transfers'] = self.find_random_choice_transfers_by_model(self.object.pk, False)
        context['stochastic_transfers'] = self.find_stochastic_transfers_by_model(self.object.pk, False)
        context['aggregated_transfers'] = self.find_aggregated_transfers_by_model(self.object.pk, False)
        
        context['external_list_inflows'] = self.find_external_list_inflows_by_model_instance(self.object.pk)
        context['single_period_inflows'] = self.find_single_period_inflows_by_external_list_inflow(self.object.pk)
        context['external_function_inflows'] = self.find_external_function_inflows_by_model(self.object.pk)
        
        return context


class ModelCreateView(generic.CreateView):
    model = models.model
    form_class = forms.ModelForm
    template_name = 'dpmfa/model/model_form.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('dpmfa:project-detail', kwargs={'pk': self.kwargs['project_pk']})

    def form_valid(self, form):
        model = form.save(commit=False)
        model.project_id = self.kwargs['project_pk']
        return super(ModelCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ModelCreateView, self).get_context_data(**kwargs)
        context['project'] = models.project.objects.get(pk=self.kwargs['project_pk'])
        return context


class ModelUpdateView(generic.UpdateView):
    model = models.model
    form_class = forms.ModelForm
    template_name = 'dpmfa/model/model_form.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('dpmfa:project-detail', kwargs={'pk': self.object.project.pk })

    def get_context_data(self, **kwargs):
        context = super(ModelUpdateView, self).get_context_data(**kwargs)
        context['project'] = self.object.project
        return context


class ModelDeleteView(generic.DeleteView):
    model = models.model
    template_name = 'dpmfa/model/model_confirm_delete.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('dpmfa:project-detail', kwargs={'pk': self.object.project.pk})


# ==============================================================================
#  Experiment
# ==============================================================================

class ExperimentCreateView(generic.CreateView):
    model = models.experiment
    form_class = forms.ExperimentForm
    template_name = 'dpmfa/experiment/experiment_form.html'

    def get_context_data(self, **kwargs):
        context = super(ExperimentCreateView, self).get_context_data(**kwargs)
        context['prototype_model'] = models.model.objects.get(pk=self.kwargs['prototype_pk'])
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('dpmfa:results-template', kwargs={'experiment_pk': self.experiment.pk})
    
    def setupExperiment(self): 
        self.prototype_model = models.model.objects.get(pk=self.kwargs['prototype_pk'])
        self.model_instance = ModelCopier.copy_model(self.prototype_model)
        self.experiment.prototype_model = self.prototype_model
        self.experiment.model_instance = self.model_instance
        self.experiment.save()
                
    def runSimulation(self):
        self.experimentConverter = converter.ExperimentConverter(self.experiment)
        self.simulationDpmfa = self.experimentConverter.getSimulatorAsDpmfaEntity()
        self.modelInstanceConverter = self.experimentConverter.getModelInstanceConverter()
        self.flowCompartmentMap = self.modelInstanceConverter.getFlowCompartmentMap()
        self.stockMap = self.modelInstanceConverter.getStockMap()
        self.sinkMap = self.modelInstanceConverter.getSinkMap()
        print("Running simulation...")
        self.simulationDpmfa.runSimulation()
        
    def storeResults(self):
        self.storeResultsOfSinks()
        self.storeResultsOfFlowCompartmets()
        self.storeResultsOfStocks()
        
    # sinks only have inflows
    def storeResultsOfSinks(self):
        index = 0
        for sink in self.simulationDpmfa.getSinks():
            
            # remove anything that is not actually a sink
            if type(sink) is not package_components.Sink:
                continue
            
            # default values
            nameOfInflowResult = 'Entity_' + str(index) + '_Inflow'
            primaryKey = None
            index += 1
            
            # get the converter for this sink
            converter = self.sinkMap[sink]
            
            if converter.db_entity.pk:
                primaryKey = converter.db_entity.pk
            if converter.name:
                nameOfInflowResult = converter.name + " " + str(primaryKey)
                
            print(str(sink.getInflowRecords()))
            
            self.storeArray(sink.getInflowRecords(), sink, nameOfInflowResult, primaryKey)
    
    # flow compartments have inflows and outflows
    def storeResultsOfFlowCompartmets(self):
        index = 0
        for flowCompartment in self.simulationDpmfa.getFlowCompartmentartments():
            
            # remove anything that is not actually a flow compartment
            if type(flowCompartment) is package_components.Sink  or type(flowCompartment) is package_components.Stock:
                continue
            
            # default values
            nameOfInflowResult = 'Entity_' + str(index) + '_Inflow'
            nameOfOutflowResult = 'Entity_' + str(index) + '_Outflow'
            primaryKey = None
            index += 1
            
            converter = self.flowCompartmentMap[flowCompartment]
            
            if converter.db_entity.pk:
                primaryKey = converter.db_entity.pk
            if converter.name:
                nameOfInflowResult = converter.name + " " + str(primaryKey) + '_Inflow'
                nameOfOutflowResult = converter.name + " " + str(primaryKey) + '_Outflow'
                
            # path to result folder
            names = []
            names.append(nameOfInflowResult)
            names.append(nameOfOutflowResult)
            
            for name in names:
                
                if name == nameOfInflowResult:
                    print(str(flowCompartment.getInflowRecords()))
                    self.storeArray(flowCompartment.getInflowRecords(), flowCompartment, name, primaryKey)
                else:
                    print(str(flowCompartment.getOutflowRecords()))
                    self.storeOutflowDict(flowCompartment.getOutflowRecords(), flowCompartment, name, primaryKey)
                    
    # stocks have inflows and outflows
    def storeResultsOfStocks(self):
        index = 0
        for stock in self.simulationDpmfa.getStocks():
            
            # remove anything that is not actually a flow compartment
            if type(stock) is not package_components.Stock:
                continue
            
            # default values
            nameOfInflowResult = 'Entity_' + str(index) + '_Inflow'
            nameOfOutflowResult = 'Entity_' + str(index) + '_Outflow'
            primaryKey = None
            index += 1
            
            converter = self.stockMap[stock]
            
            if converter.db_entity.pk:
                primaryKey = converter.db_entity.pk
            if converter.name:
                nameOfInflowResult = converter.name + " " + str(primaryKey) + '_Inflow'
                nameOfOutflowResult = converter.name + " " + str(primaryKey) + '_Outflow'
                
            # path to result folder
            names = []
            names.append(nameOfInflowResult)
            names.append(nameOfOutflowResult)
            
            for name in names:   
                # store the results
                if name == nameOfInflowResult:
                    print(str(stock.getInflowRecords()))
                    self.storeArray(stock.getInflowRecords(), stock, name, primaryKey)
                else:
                    print(str(stock.getOutflowRecords()))
                    self.storeOutflowDict(stock.getOutflowRecords(), stock, name, primaryKey)

    def form_valid(self, form):
        self.experiment = form.save(commit=False)
        self.setupExperiment()
        self.runSimulation()
        self.storeResults()
        return super(ExperimentCreateView, self).form_valid(form)
                
    def storeOutflowDict(self, outFlowDict, entity, name, primaryKey):
        resultAsString = ""
        for target, array in outFlowDict.items():
            resultAsString += str(target) + '\n'
            for row in array:
                for amount in row:
                    amountAsString = str(amount).strip() + ","
                    resultAsString += amountAsString
            
                resultAsString += "\n"
        
        # create the result entity
        r = models.result(
            model_instance = self.model_instance,
            experiment = self.experiment,
            entity_type = self.getEntityConstant(entity),
            name_of_entity = name,
            pk_of_entity = primaryKey,
            result = resultAsString,
            )
        print(r)
        r.save()
    
    def storeArray(self, array, entity, name, primaryKey):
        resultAsString = ""
        for row in array:
            for amount in row:
                amountAsString = str(amount).strip() + ","
                resultAsString += amountAsString
        
            resultAsString += "\n"
            
        # create the result entity
        r = models.result(
            model_instance = self.model_instance,
            experiment = self.experiment,
            entity_type = self.getEntityConstant(entity),
            name_of_entity = name,
            pk_of_entity = primaryKey,
            result = resultAsString,
            )
        print(r)
        r.save()
    
    def getEntityConstant(self, entity):
        if type(entity) is package_components.Stock:
            return models.result.STOCK
        elif type(entity) is package_components.Sink:
            return models.result.SINK
        elif type(entity) is package_components.FlowCompartment:
            return models.result.FLOW_COMPARTEMENT
        
    
class ExperimentDetailView(generic.DetailView):
    model = models.experiment
    template_name = 'dpmfa/experiment/experiment_detail.html'

class ExperimentDeleteView(generic.DeleteView):
    model = models.experiment
    template_name = 'dpmfa/experiment/experiment_confirm_delete.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('dpmfa:model-detail', kwargs={'pk': self.object.prototype_model.pk })

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.model_instance.delete()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())

# ==============================================================================
#  Model Designer
# ==============================================================================


class ModelDesignerTemplateView(generic.TemplateView):
    template_name = 'dpmfa/model_designer/model_designer.html'

    def get_context_data(self, **kwargs):
        context = super(ModelDesignerTemplateView, self).get_context_data(**kwargs)

        model = models.model.objects.get(pk=self.kwargs['model_pk'])

        model_dict = (JsonModel()).configure_for(model).as_dictionary()

        context['model'] = model
        context['model_data_json'] = json.dumps(model_dict)
        return context

class ModelDesignerSaveView(generic.View):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(ModelDesignerSaveView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(request.body);
        # TODO: save the changes and return real id map
        return JsonResponse({
            'tempId123': 'persistentId456',
            'tempId678': 'persistentId999'
        })
        


#==============================================================================
#  Model Parameters
#==============================================================================

class ParametersDetailView(generic.DetailView):
    model = models.model_parameters
    
    fields = [
        'model',
        'status'
        ]

class ParameterRedirectView(generic.RedirectView):
    model = models.model_parameters
    
    fields = [
        'model',
        'status'
        ]
    
#==============================================================================
#  Compartment
#==============================================================================

class CompartmentRedirectView(generic.RedirectView):
    permanent = False
    query_string = False
    
    def get_redirect_url(self, *args, **kwargs):
        try: 
            compartment_pk = self.kwargs['compartment_pk']
            if len(models.flow_compartment.objects.filter(pk=compartment_pk)) > 0:
                return models.flow_compartment.objects.get(pk=compartment_pk).get_absolute_url()
            elif len(models.sink.objects.filter(pk=compartment_pk)) > 0:
                return models.sink.objects.get(pk=compartment_pk).get_absolute_url()
            elif len(models.stock.objects.filter(pk=compartment_pk)) > 0:
                return models.stock.objects.get(pk=compartment_pk).get_absolute_url()
            else:
                print("Could not retrieve a compartment for inflow")
        except:
            return

# class CompartmentDetailView(generic.DetailView):
#    model = models.compartment
#
#    fields = [
#        'model',
#        'name',
#        'description',
#        'log_inflows',
#        'categories'
#        ]
    
# class CompartmentCreateView(generic.CreateView):
#    model = models.compartment
#
#    fields = [
#        'model',
#        'name',
#        'description',
#        'log_inflows',
#        'categories'
#        ]
    
#class CompartmentUpdateView(generic.UpdateView):
#    model = models.compartment
#
#    fields = [
#        'model',
#        'name',
#        'description',
#        'log_inflows',
#        'categories'
#        ]
    
#class CompartmentDeleteView(generic.DeleteView):
#    model = models.compartment
#
#    fields = [
#        'model',
#        'name',
#        'description',
#        'log_inflows',
#        'categories'
#        ]
    
#==============================================================================
#  Flow Compartment
#==============================================================================

class FlowCompartmentDetailView(generic.DetailView):
    model = models.flow_compartment
    template_name = 'dpmfa/compartments/flow_compartment_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(FlowCompartmentDetailView, self).get_context_data(**kwargs)
        model_instances = models.model_instance.objects.filter(pk = self.object.model.pk)
        if len(model_instances) != 0:
            context['model'] = model_instances[0]
        else:
            context['model'] = self.object.model
        return context
    
class FlowCompartmentUpdateView(generic.UpdateView):
    model = models.flow_compartment
    template_name = 'dpmfa/compartments/flow_compartment_form.html'
    form_class = forms.FlowCompartmentForm
    context_object_name = 'flow_compartment'

    def get_success_url(self, **kwargs):
        return reverse_lazy('dpmfa:flow-compartment-detail', kwargs={'pk': self.object.pk})

class FlowCompartmentDeleteView(generic.DeleteView):
    model = models.flow_compartment
    template_name = 'dpmfa/compartments/flow_compartment_confirm_delete.html'
    
    fields = [
        'model',
        'name',
        'description',
        'evt_created',
        'evt_changed',
        'log_inflows',
        'categories',
        'adjust_outgoing_tcs',
        'log_outflows',
        ]

    def get_success_url(self, **kwargs):
        return reverse_lazy('dpmfa:model-detail', kwargs={'pk': self.object.model.pk})
    
#==============================================================================
#  Stock
#==============================================================================

class StockDetailView(generic.DetailView):
    model = models.stock
    template_name = 'dpmfa/compartments/stock_detail.html'
    
    fields = [
        'model',
        'name',
        'description',
        'evt_created',
        'evt_changed',
        'log_inflows',
        'categories',
        'local_release',
        'adjust_outgoing_tcs',
        'log_outflows',
        ]
    def get_context_data(self, **kwargs):
        context = super(StockDetailView, self).get_context_data(**kwargs)
        model_instances = models.model_instance.objects.filter(pk = self.object.model.pk)
        if len(model_instances) != 0:
            context['model'] = model_instances[0]
        else:
            context['model'] = self.object.model
        return context

# class StockCreateView(generic.CreateView):
#     model = models.stock
#     
#     fields = [
#         'model',
#         'name',
#         'description',
#         'evt_created',
#         'evt_changed',
#         'log_inflows',
#         'categories',
#         'local_release',
#         'adjust_outgoing_tcs',
#         'log_outflows',
#         ]

class StockUpdateView(generic.UpdateView):
    model = models.stock
    template_name = 'dpmfa/compartments/stock_form.html'
    form_class = forms.StockForm
    context_object_name = 'stock'

    def get_success_url(self, **kwargs):
        return reverse_lazy('dpmfa:stock-detail', kwargs={'pk': self.object.pk})
    
class StockDeleteView(generic.DeleteView):
    model = models.stock
    template_name = 'dpmfa/compartments/stock_confirm_delete.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('dpmfa:model-detail', kwargs={'pk': self.object.model.pk})

#==============================================================================
#  Sink
#==============================================================================

class SinkDetailView(generic.DetailView):
    model = models.sink
    template_name = 'dpmfa/compartments/sink_detail.html'
    
    fields = [
        'model',
        'name',
        'description',
        'evt_created',
        'evt_changed',
        'log_inflows',
        'categories',
        'adjust_outgoing_tcs',
        'log_outflows',
        ]
    def get_context_data(self, **kwargs):
        context = super(SinkDetailView, self).get_context_data(**kwargs)
        model_instances = models.model_instance.objects.filter(pk = self.object.model.pk)
        if len(model_instances) != 0:
            context['model'] = model_instances[0]
        else:
            context['model'] = self.object.model
        return context

# class SinkCreateView(generic.CreateView):
#     model = models.sink
#     
#     fields = [
#         'model',
#         'name',
#         'description',
#         'evt_created',
#         'evt_changed',
#         'log_inflows',
#         'categories',
#         'adjust_outgoing_tcs',
#         'log_outflows',
#         ]
    
class SinkUpdateView(generic.UpdateView):
    model = models.sink
    template_name = 'dpmfa/compartments/sink_form.html'
    form_class = forms.SinkForm
    context_object_name = 'sink'

    def get_success_url(self, **kwargs):
        return reverse_lazy('dpmfa:sink-detail', kwargs={'pk': self.object.pk})

class SinkDeleteView(generic.DeleteView):
    model = models.sink
    template_name = 'dpmfa/compartments/sink_confirm_delete.html'
    
    fields = [
        'model',
        'name',
        'description',
        'evt_created',
        'evt_changed',
        'log_inflows',
        'categories',
        'adjust_outgoing_tcs',
        'log_outflows',
        ]

    def get_success_url(self, **kwargs):
        return reverse_lazy('dpmfa:model-detail', kwargs={'pk': self.object.model.pk})
    
#==============================================================================
#  Releases
#==============================================================================

# Local Release

class LocalReleaseDetailView(generic.DetailView):
    model = models.local_release
    template_name = 'dpmfa/release/local_release_detail.html'
    
    fields = [
        'stock_of_local_release',
        'name',
        'delay'
        ]
    def get_context_data(self, **kwargs):
        context = super(LocalReleaseDetailView, self).get_context_data(**kwargs)
        model_instances = models.model_instance.objects.filter(pk = self.object.stock.model.pk)
        if len(model_instances) != 0:
            context['model'] = model_instances[0]
        else:
            context['model'] = self.object.stock.model
        return context
    
class LocalReleaseUpdateView(generic.UpdateView):
    model = models.local_release
    template_name = 'dpmfa/release/local_release_form.html'
    form_class = forms.LocalReleaseForm
    context_object_name = 'local_release'

    def get_success_url(self, **kwargs):
        return reverse_lazy('dpmfa:local-release-detail', kwargs={'pk': self.object.pk})
    
# Fixed Rate Release

class FixedRateReleaseDetailView(generic.DetailView):
    model = models.fixed_rate_release
    
    fields = [
        'stock_of_local_release',
        'name',
        'delay',
        'fixed_rate_release'
        ]
    def get_context_data(self, **kwargs):
        context = super(FixedRateReleaseDetailView, self).get_context_data(**kwargs)
        model_instances = models.model_instance.objects.filter(pk = self.object.stock.model.pk)
        if len(model_instances) != 0:
            context['model'] = model_instances[0]
        else:
            context['model'] = self.object.stock.model
        return context
    
class FixedRateReleaseUpdateView(generic.UpdateView):
    model = models.fixed_rate_release
    template_name = 'dpmfa/release/fixed_rate_form.html'
    form_class = forms.FixedRateReleaseForm
    context_object_name = 'fixed_rate_release'

    def get_success_url(self, **kwargs):
        return reverse_lazy('dpmfa:fixed-rate-release-detail', kwargs={'pk': self.object.pk})
    
# List Release

class FixedRateReleaseDetailView(generic.DetailView):
    model = models.fixed_rate_release
    
    fields = [
        'stock_of_local_release',
        'name',
        'delay',
        'fixed_rate_release'
        ]
    
# Function Release

class FunctionReleaseDetailView(generic.DetailView):
    model = models.function_release
    
    fields = [
        'stock_of_local_release',
        'name',
        'delay',
        'fixed_rate_release',
        'function_release'
        ]
    def get_context_data(self, **kwargs):
        context = super(FunctionReleaseDetailView, self).get_context_data(**kwargs)
        model_instances = models.model_instance.objects.filter(pk = self.object.stock.model.pk)
        if len(model_instances) != 0:
            context['model'] = model_instances[0]
        else:
            context['model'] = self.object.stock.model
        return context
    
class FunctionReleaseUpdateView(generic.UpdateView):
    model = models.function_release
    template_name = 'dpmfa/release/function_release_form.html'
    form_class = forms.FunctionReleaseForm
    context_object_name = 'fixed_rate_release'

    def get_success_url(self, **kwargs):
        return reverse_lazy('dpmfa:fixed-rate-release-detail', kwargs={'pk': self.object.pk})
    
#==============================================================================
#  Transfers
#==============================================================================

class TransferRedirectView(generic.RedirectView):
    permanent = False
    query_string = False
    
    def get_redirect_url(self, *args, **kwargs):
        try: 
            transfer_pk = self.kwargs['transfer_pk']
            if len(models.constant_transfer.objects.filter(pk=transfer_pk)) > 0:
                return models.constant_transfer.objects.get(pk=transfer_pk).get_absolute_url()
            elif len(models.random_choice_transfer.objects.filter(pk=transfer_pk)) > 0:
                return models.random_choice_transfer.objects.get(pk=transfer_pk).get_absolute_url()
            elif len(models.stochastic_transfer.objects.filter(pk=transfer_pk)) > 0:
                return models.stochastic_transfer.objects.get(pk=transfer_pk).get_absolute_url()
            elif len(models.aggregated_transfer.objects.filter(pk=transfer_pk)) > 0:
                return models.aggregated_transfer.objects.get(pk=transfer_pk).get_absolute_url()
            else:
                print("Could not retrieve a transfer for sink")
        except:
            return

# Constant

class ConstantTransferDetailView(generic.DetailView):
    model = models.constant_transfer
    template_name = 'dpmfa/transfers/constant_transfer_detail.html'
    
    fields = [
        'target',
        'belongs_to_aggregated_transfer',
        'name',
        'priority',
        'current_tc',
        'weight',
        'value'
        ]
    
    def get_context_data(self, **kwargs):
        context = super(ConstantTransferDetailView, self).get_context_data(**kwargs)
        model_instances = models.model_instance.objects.filter(pk = self.object.target.model.pk)
        if len(model_instances) != 0:
            context['model'] = model_instances[0]
        else:
            context['model'] = self.object.target.model
        return context

# class ConstantTransferCreateView(generic.CreateView):
#     model = models.constant_transfer
#     
#     fields = [
#         'target',
#         'belongs_to_aggregated_transfer',
#         'name',
#         'priority',
#         'current_tc',
#         'weight',
#         'value'
#         ]
    
class ConstantTransferUpdateView(generic.UpdateView):
    model = models.constant_transfer
    template_name = 'dpmfa/transfers/constant_transfer_form.html'
    form_class = forms.ConstantTransferForm
    context_object_name = 'constant_transfer'
    
    def get_context_data(self, **kwargs):
        context = super(ConstantTransferUpdateView, self).get_context_data(**kwargs)
        context['model'] = self.object.target.model 
        return context
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('dpmfa:model-detail', kwargs={'pk': self.object.target.model.pk })
   
        
class ConstantTransferDeleteView(generic.DeleteView):
    model = models.constant_transfer
    template_name = 'dpmfa/transfers/constant_transfer_confirm_delete.html'
    
    fields = [
        'target',
        'belongs_to_aggregated_transfer',
        'name',
        'priority',
        'current_tc',
        'weight',
        'value'
        ]
    
# Random Choice

class RandomChoiceTransferDetailView(generic.DetailView):
    model = models.random_choice_transfer
    template_name = 'dpmfa/transfers/random_choice_transfer_detail.html'
    
    fields = [
        'target',
        'belongs_to_aggregated_transfer',
        'name',
        'priority',
        'current_tc',
        'weight',
        'sample'
        ]
    def get_context_data(self, **kwargs):
        context = super(RandomChoiceTransferDetailView, self).get_context_data(**kwargs)
        model_instances = models.model_instance.objects.filter(pk = self.object.target.model.pk)
        if len(model_instances) != 0:
            context['model'] = model_instances[0]
        else:
            context['model'] = self.object.target.model
        return context

class RandomChoiceTransferCreateView(generic.CreateView):
    model = models.random_choice_transfer
    
    fields = [
        'target',
        'belongs_to_aggregated_transfer',
        'name',
        'priority',
        'current_tc',
        'weight',
        'sample'
        ]

class RandomChoiceTransferUpdateView(generic.UpdateView):
    model = models.random_choice_transfer
    template_name = 'dpmfa/transfers/random_choice_transfer_form.html'
    form_class = forms.RandomChoiceTransferForm
    context_object_name = 'random_choice_transfer'
    
    def get_context_data(self, **kwargs):
        context = super(RandomChoiceTransferUpdateView, self).get_context_data(**kwargs)
        context['model'] = self.object.target.model 
        return context
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('dpmfa:random-choice-transfer-detail', kwargs={'pk': self.object.pk })


class RandomChoiceTransferDeleteView(generic.UpdateView):
    model = models.random_choice_transfer
    
    fields = [
        'target',
        'belongs_to_aggregated_transfer',
        'name',
        'priority',
        'current_tc',
        'weight',
        'sample'
        ]

# Aggregated

class AggregatedTransferDetailView(generic.DetailView):
    model = models.aggregated_transfer
    template_name = 'dpmfa/transfers/aggregated_transfer_detail.html'
    
    fields = [
        'target',
        'belongs_to_aggregated_transfer',
        'name',
        'priority',
        'current_tc',
        'weight'
        ]
    def get_context_data(self, **kwargs):
        context = super(AggregatedTransferDetailView, self).get_context_data(**kwargs)
        model_instances = models.model_instance.objects.filter(pk = self.object.target.model.pk)
        if len(model_instances) != 0:
            context['model'] = model_instances[0]
        else:
            context['model'] = self.object.target.model
        return context
    
class AggregatedTransferCreateView(generic.CreateView):
    model = models.aggregated_transfer
    
    fields = [
        'target',
        'belongs_to_aggregated_transfer',
        'name',
        'priority',
        'current_tc',
        'weight'
        ]

class AggregatedTransferUpdateView(generic.UpdateView):
    model = models.aggregated_transfer
    template_name = 'dpmfa/transfers/aggregated_transfer_form.html'
    form_class = forms.AggregatedTransferForm
    context_object_name = 'aggregated_transfer'
    
    def get_context_data(self, **kwargs):
        context = super(AggregatedTransferUpdateView, self).get_context_data(**kwargs)
        context['model'] = self.object.target.model 
        return context
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('dpmfa:aggregated-transfer-detail', kwargs={'pk': self.object.pk })
   
    
    
class AggregatedTransferDeleteView(generic.DeleteView):
    model = models.aggregated_transfer
    
    fields = [
        'target',
        'belongs_to_aggregated_transfer',
        'name',
        'priority',
        'current_tc',
        'weight'
        ]

# Stochastic

class StochasticTransferDetailView(generic.DetailView):
    model = models.stochastic_transfer
    template_name = 'dpmfa/transfers/stochastic_transfer_detail.html'
    
    fields = [
        'target',
        'belongs_to_aggregated_transfer',
        'name',
        'priority',
        'current_tc',
        'weight',
        'parameters',
        'function'
        ]
    def get_context_data(self, **kwargs):
        context = super(StochasticTransferDetailView, self).get_context_data(**kwargs)
        model_instances = models.model_instance.objects.filter(pk = self.object.target.model.pk)
        if len(model_instances) != 0:
            context['model'] = model_instances[0]
        else:
            context['model'] = self.object.target.model
        return context

class StochasticTransferCreateView(generic.CreateView):
    model = models.stochastic_transfer
    
    fields = [
        'target',
        'belongs_to_aggregated_transfer',
        'name',
        'priority',
        'current_tc',
        'weight',
        'parameters',
        'function'
        ]    
    
class StochasticTransferUpdateView(generic.UpdateView):
    model = models.stochastic_transfer
    template_name = 'dpmfa/transfers/stochastic_transfer_form.html'
    form_class = forms.StochasticTransferForm
    context_object_name = 'stochastic_transfer'
    
    def get_context_data(self, **kwargs):
        context = super(StochasticTransferUpdateView, self).get_context_data(**kwargs)
        context['model'] = self.object.target.model 
        return context
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('dpmfa:stochastic-transfer-detail', kwargs={'pk': self.object.pk })

    
class StochasticTransferDeleteView(generic.DeleteView):
    model = models.stochastic_transfer
    
    fields = [
        'target',
        'belongs_to_aggregated_transfer',
        'name',
        'priority',
        'current_tc',
        'weight',
        'parameters',
        'function'
        ]    
    
#==============================================================================
#  External Inflows
#==============================================================================
    
# External List Inflow

class ExternalListInflowDetailView(generic.DetailView):
    model = models.external_list_inflow
    template_name = 'dpmfa/external_inflow/external_list_inflow_detail.html'
    
    def find_fixed_value_inflows_by_external_function_inflow(self, ext_list_pk):
        return models.fixed_value_inflow.objects.filter(external_list_inflow__pk=ext_list_pk).order_by('period')

    def find_stochastic_function_inflows_by_external_function_inflow(self, ext_list_pk):
        return models.stochastic_function_inflow.objects.filter(external_list_inflow=ext_list_pk).order_by('period')

    def find_random_choice_inflows_by_external_function_inflow(self, ext_list_pk):
        return models.random_choice_inflow.objects.filter(external_list_inflow=ext_list_pk).order_by('period')

    def get_context_data(self, **kwargs):
        context = super(ExternalListInflowDetailView, self).get_context_data(**kwargs)

        fixed_value_inflows = self.find_fixed_value_inflows_by_external_function_inflow(self.object.pk)
        stochastic_function_inflows = self.find_stochastic_function_inflows_by_external_function_inflow(self.object.pk)
        random_choice_inflows = self.find_random_choice_inflows_by_external_function_inflow(self.object.pk)

        single_period_inflows = list(chain(fixed_value_inflows, stochastic_function_inflows, random_choice_inflows))
        single_period_inflows.sort(key=lambda x: x.period)

        context['single_period_inflows'] = single_period_inflows

        return context
    
    def get_context_data(self, **kwargs):
        context = super(ExternalListInflowDetailView, self).get_context_data(**kwargs)
        model_instances = models.model_instance.objects.filter(pk = self.object.target.model.pk)
        if len(model_instances) != 0:
            context['model'] = model_instances[0]
        else:
            context['model'] = self.object.target.model
        return context


class ExternalListInflowCreateView(generic.CreateView):
    model = models.external_list_inflow

    fields = [
        'target',
        'name',
        'start_delay',
        'derivation_distribution',
        'derivation_parameters',
        'derivation_factor'
        ]
    
class ExternalListInflowUpdateView(generic.UpdateView):
    model = models.external_list_inflow
    template_name = 'dpmfa/external_inflow/external_list_inflow_form.html'
    form_class = forms.ExternalListInflowForm
    context_object_name = 'external_list_inflow'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('dpmfa:model-detail', kwargs={'pk': self.object.target.model.pk })
    
class ExternalListInflowDeleteView(generic.DeleteView):
    model = models.external_list_inflow
    template_name = 'dpmfa/external_inflow/external_list_inflow_confirm_delete.html'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('dpmfa:model-detail', kwargs={'pk': self.object.target.model.pk })
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        
        check_for_last_inflow = models.external_inflow.objects.filter(target__model = self.object.target.model).count()
        if check_for_last_inflow > 2:
            self.object.delete()
        return HttpResponseRedirect(self.get_success_url())

# External Function Inflow

class ExternalFunctionInflowDetailView(generic.DetailView):
    model = models.external_function_inflow
    template_name = 'dpmfa/external_inflow/external_function_inflow_detail.html'
    
    def find_fixed_value_inflows_by_external_function_inflow(self, external_function_inflow_pk):
        return models.fixed_value_inflow.objects.filter(external_list_inflow__pk=external_function_inflow_pk).order_by('period')

    def find_stochastic_function_inflows_by_external_function_inflow(self, external_function_inflow_pk):
        return models.stochastic_function_inflow.objects.filter(external_list_inflow=external_function_inflow_pk).order_by('period')

    def find_random_choice_inflows_by_external_function_inflow(self, external_function_inflow_pk):
        return models.random_choice_inflow.objects.filter(external_list_inflow=external_function_inflow_pk).order_by('period')

    def get_context_data(self, **kwargs):
        context = super(ExternalFunctionInflowDetailView, self).get_context_data(**kwargs)

        fixed_value_inflows = self.find_fixed_value_inflows_by_external_function_inflow(self.object.pk)
        stochastic_function_inflows = self.find_stochastic_function_inflows_by_external_function_inflow(self.object.pk)
        random_choice_inflows = self.find_random_choice_inflows_by_external_function_inflow(self.object.pk)

        single_period_inflows = list(chain(fixed_value_inflows, stochastic_function_inflows, random_choice_inflows))
        single_period_inflows.sort(key=lambda x: x.period)

        context['project'] = self.object.target.model.project
        context['model'] = self.object.target.model
        context['single_period_inflow'] = single_period_inflows

        return context
    
    def get_context_data(self, **kwargs):
        context = super(ExternalFunctionInflowDetailView, self).get_context_data(**kwargs)
        model_instances = models.model_instance.objects.filter(pk = self.object.target.model.pk)
        if len(model_instances) != 0:
            context['model'] = model_instances[0]
        else:
            context['model'] = self.object.target.model
        return context

class ExternalFunctionInflowCreateView(generic.CreateView):
    model = models.external_list_inflow
    
    fields = [
        'target',
        'name',
        'start_delay',
        'derivation_distribution',
        'derivation_parameters',
        'derivation_factor',
        'inflow_function',
        'basic_inflow'
        ]
    
class ExternalFunctionInflowUpdateView(generic.UpdateView):
    model = models.external_list_inflow
    
    fields = [
        'name',
        'start_delay',
        'derivation_distribution',
        'derivation_parameters',
        'derivation_factor'
        ]

class ExternalFunctionInflowDeleteView(generic.DeleteView):
    model = models.external_list_inflow
    template_name = 'dpmfa/external_inflow/external_function_inflow_confirm_delete.html'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('dpmfa:model-detail', kwargs={'pk': self.object.target.model.pk })
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        
        check_for_last_inflow = models.external_inflow.objects.filter(target__model = self.object.target.model).count()
        if check_for_last_inflow > 1:
            self.object.delete()
        return HttpResponseRedirect(self.get_success_url())
    
#==============================================================================
#  Single Period Inflow
#==============================================================================

class SinglePeriodInflowRedirectView(generic.RedirectView):
    permanent = False
    query_string = False
    
    def get_redirect_url(self, *args, **kwargs):
        #try: 
            single_period_inflow_pk = self.kwargs['single_period_inflow_pk']
            if len(models.fixed_value_inflow.objects.filter(pk=single_period_inflow_pk)) > 0:
                print("trying to get fixed value inflow")
                print("single period inflow pk:" + single_period_inflow_pk)
                return models.fixed_value_inflow.objects.get(pk=single_period_inflow_pk).get_absolute_url()
            elif len(models.stochastic_function_inflow.objects.filter(pk=single_period_inflow_pk)) > 0:
                print("trying to get stochastic function inflow")
                return models.stochastic_function_inflow.objects.get(pk=single_period_inflow_pk).get_absolute_url()
            elif len(models.random_choice_inflow.objects.filter(pk=single_period_inflow_pk)) > 0:
                print("trying to get random choice inflow")
                return models.random_choice_inflow.objects.get(pk=single_period_inflow_pk).get_absolute_url()
            else:
                print("Could not retrieve a compartment for inflow")
        #except:
            print("Redirection of single period inflow failed")

# Fixed Value Inflow

class FixedValueInflowUpdateView(generic.UpdateView):
    model = models.fixed_value_inflow
    template_name = 'dpmfa/external_inflow/fixed_value_inflow_form.html'
    form_class = forms.FixedValueInflowForm
    context_object_name = 'fixed_value_inflow'
    
    def get_context_data(self, **kwargs):
        context = super(FixedValueInflowUpdateView, self).get_context_data(**kwargs)
        
        context['external_list_inflow'] = self.object.external_list_inflow
        context['compartment'] = self.object.external_list_inflow.target
        context['model'] = self.object.external_list_inflow.target.model
        context['project'] = self.object.external_list_inflow.target.model.project
        
        return context
    
    def form_valid(self, form):
        model_instance = form.save(commit=False)
        
        single_period_inflow_objects = models.single_period_inflow.objects.filter(external_list_inflow=self.object.external_list_inflow.pk)
        
        single_period_inflows = []
        for spi in single_period_inflow_objects:
            single_period_inflows.append(spi)
            
        single_period_inflows.sort(key=lambda x: x.period)
        
        period = 0
        for single_period_inflow in single_period_inflows:
            print(single_period_inflow.period)
            period += 1
            single_period_inflow.period = period
            print(single_period_inflow.period)
            single_period_inflow.save()
            
        return super(FixedValueInflowUpdateView, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('dpmfa:model-detail', kwargs={'pk': self.object.external_list_inflow.target.model.pk})

class FixedValueInflowDetailView(generic.DetailView):
    model = models.fixed_value_inflow
    template_name = 'dpmfa/external_inflow/fixed_value_inflow_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(FixedValueInflowDetailView, self).get_context_data(**kwargs)
        
        context['external_list_inflow'] = self.object.external_list_inflow
        context['compartment'] = self.object.external_list_inflow.target
        context['model'] = self.object.external_list_inflow.target.model
        context['project'] = self.object.external_list_inflow.target.model.project
        
        return context
  

class FixedValueInflowDeleteView(generic.DeleteView):
    model = models.fixed_value_inflow

    def get_context_data(self, **kwargs):
        context = super(FixedValueInflowDeleteView, self).get_context_data(**kwargs)

        context['external_list_inflow'] = self.object.external_list_inflow

        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('dpmfa:external-list-inflow-detail', kwargs={'pk': self.object.external_list_inflow.pk})

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()

        following_single_period_inflows = models.single_period_inflow.objects.filter(external_list_inflow=self.object.external_list_inflow,period__gt=self.object.period)
        for following_single_period_inflow in following_single_period_inflows:
            following_single_period_inflow.period = following_single_period_inflow.period - 1
            following_single_period_inflow.save()

        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())

class FixedValueInflowCreateView(generic.CreateView):
    model = models.fixed_value_inflow
    
    fields = ['value']

    def get_context_data(self, **kwargs):
        context = super(FixedValueInflowCreateView, self).get_context_data(**kwargs)

        context['external_list_inflow'] = models.external_list_inflow.objects.get(pk=self.kwargs['external_list_inflow_pk'])

        return context

    def form_valid(self, form):
        model = form.save(commit=False)

        external_list_inflow_pk = self.kwargs['external_list_inflow_pk']
        period = int(self.kwargs['previous_period']) + 1

        model.external_list_inflow_id = external_list_inflow_pk
        model.period = period

        following_single_period_inflows = models.single_period_inflow.objects.filter(external_list_inflow_id=external_list_inflow_pk, period__gte=period)
        for following_single_period_inflow in following_single_period_inflows:
            following_single_period_inflow.period = following_single_period_inflow.period + 1
            following_single_period_inflow.save()

        return super(FixedValueInflowCreateView, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('dpmfa:external-list-inflow-detail', kwargs={'pk': self.kwargs['external_list_inflow_pk']})


#  Random Choice Inflow


class RandomChoiceInflowDetailView(generic.DetailView):
    model = models.random_choice_inflow

    fields = ['sample']

    def get_context_data(self, **kwargs):
        context = super(RandomChoiceInflowDetailView, self).get_context_data(**kwargs)

        external_list_inflow_pk = self.object.external_list_inflow.pk
        context['external_list_inflow'] = models.external_list_inflow.objects.get(pk=external_list_inflow_pk)

        return context


class RandomChoiceInflowUpdateView(generic.UpdateView):
    model = models.random_choice_inflow
    template_name = 'dpmfa/external_inflow/random_choice_inflow_form.html'
    form_class = forms.RandomChoiceInflowForm
    context_object_name = 'random_choice_inflow'
    
    def get_context_data(self, **kwargs):
        context = super(RandomChoiceInflowUpdateView, self).get_context_data(**kwargs)
        
        context['external_list_inflow'] = self.object.external_list_inflow
        context['compartment'] = self.object.external_list_inflow.target
        context['model'] = self.object.external_list_inflow.target.model
        context['project'] = self.object.external_list_inflow.target.model.project
        
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('dpmfa:model-detail', kwargs={'pk': self.object.external_list_inflow.target.model.pk})
    
    def get_absolute_url(self):
        return reverse('dpmfa:random-choice-inflow-update', args=[self.id])


class RandomChoiceInflowDeleteView(generic.DeleteView):
    model = models.random_choice_inflow

    def get_context_data(self, **kwargs):
        context = super(RandomChoiceInflowDeleteView, self).get_context_data(**kwargs)

        context['external_list_inflow'] = self.object.external_list_inflow

        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('dpmfa:external-list-inflow-detail', kwargs={'pk': self.object.external_list_inflow.pk})

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()

        following_single_period_inflows = models.single_period_inflow.objects.filter(external_list_inflow=self.object.external_list_inflow,period__gt=self.object.period)
        for following_single_period_inflow in following_single_period_inflows:
            following_single_period_inflow.period = following_single_period_inflow.period - 1
            following_single_period_inflow.save()

        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())


class RandomChoiceInflowCreateView(generic.CreateView):
    model = models.random_choice_inflow

    fields = ['sample']

    def get_context_data(self, **kwargs):
        context = super(RandomChoiceInflowCreateView, self).get_context_data(**kwargs)

        context['external_list_inflow'] = models.external_list_inflow.objects.get(pk=self.kwargs['external_list_inflow_pk'])

        return context

    def form_valid(self, form):
        model = form.save(commit=False)

        external_list_inflow_pk = self.kwargs['external_list_inflow_pk']
        period = int(self.kwargs['previous_period']) + 1

        model.external_list_inflow_id = external_list_inflow_pk
        model.period = period

        following_single_period_inflows = models.single_period_inflow.objects.filter(
            external_list_inflow_id=external_list_inflow_pk, period__gte=period)
        for following_single_period_inflow in following_single_period_inflows:
            following_single_period_inflow.period = following_single_period_inflow.period + 1
            following_single_period_inflow.save()

        return super(RandomChoiceInflowCreateView, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('dpmfa:external-list-inflow-detail', kwargs={'pk': self.kwargs['external_list_inflow_pk']})



#  Stochastic Function Inflow


class StochasticFunctionInflowDetailView(generic.DetailView):
    model = models.stochastic_function_inflow
    template_name = 'dpmfa/external_inflow/stochastic_function_inflow_detail.html'

    def get_context_data(self, **kwargs):
        context = super(StochasticFunctionInflowDetailView, self).get_context_data(**kwargs)

        external_list_inflow_pk = self.object.external_list_inflow.pk
        context['external_list_inflow'] = models.external_list_inflow.objects.get(pk=external_list_inflow_pk)

        return context

class StochasticFunctionInflowUpdateView(generic.UpdateView):
    model = models.stochastic_function_inflow
    template_name = 'dpmfa/external_inflow/stochastic_function_inflow_form.html'
    form_class = forms.StochasticFunctionInflowForm
    context_object_name = 'stochastic_function_inflow'

    def get_success_url(self, **kwargs):
        stochastic_function_inflow = self.object.stochastic_function_inflow.get_queryset()[0]
        return reverse_lazy('dpmfa:model-detail', kwargs={'pk': stochastic_function_inflow.pk})
    
    def get_absolute_url(self):
        return reverse('dpmfa:stochastic-function-inflow-update', args=[self.id])


class StochasticFunctionInflowDeleteView(generic.DeleteView):
    model = models.stochastic_function_inflow
    template_name = 'dpmfa/external_inflow/stochastic_function_inflow_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super(StochasticFunctionInflowDeleteView, self).get_context_data(**kwargs)

        context['external_list_inflow'] = self.object.external_list_inflow

        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('dpmfa:external-list-inflow-detail', kwargs={'pk': self.object.external_list_inflow.pk})

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()

        following_single_period_inflows = models.single_period_inflow.objects.filter(external_list_inflow=self.object.external_list_inflow,period__gt=self.object.period)
        for following_single_period_inflow in following_single_period_inflows:
            following_single_period_inflow.period = following_single_period_inflow.period - 1
            following_single_period_inflow.save()

        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())

class StochasticFunctionInflowCreateView(generic.CreateView):
    model = models.stochastic_function_inflow
    template_name = 'dpmfa/external_inflow/stochastic_function_inflow_form.html'

    fields = ['pdf', 'parameter_values']

    def get_context_data(self, **kwargs):
        context = super(StochasticFunctionInflowCreateView, self).get_context_data(**kwargs)

        context['external_list_inflow'] = models.external_list_inflow.objects.get(pk=self.kwargs['external_list_inflow_pk'])

        return context


    def form_valid(self, form):
        model = form.save(commit=False)

        external_list_inflow_pk = self.kwargs['external_list_inflow_pk']
        period = int(self.kwargs['previous_period']) + 1

        model.external_list_inflow_id = external_list_inflow_pk
        model.period = period

        following_single_period_inflows = models.single_period_inflow.objects.filter(
            external_list_inflow_id=external_list_inflow_pk, period__gte=period)
        for following_single_period_inflow in following_single_period_inflows:
            following_single_period_inflow.period = following_single_period_inflow.period + 1
            following_single_period_inflow.save()

        return super(StochasticFunctionInflowCreateView, self).form_valid(form)


    def get_success_url(self, **kwargs):
        return reverse_lazy('dpmfa:external-list-inflow-detail', kwargs={'pk': self.kwargs['external_list_inflow_pk']})


#==============================================================================
#  Simulation
#==============================================================================
    
class SimulationDetailView(generic.DetailView):
    model = models.simulation
    
    fields = [
        'model',
        'runs',
        'periods',
        'evt_created',
        'evt_changed'
        ]
    
class SimulationCreateView(generic.CreateView):
    model = models.simulation
    
    fields = [
        'model',
        'runs',
        'periods',
        ]
    
class SimulationUpdateView(generic.UpdateView):
    model = models.simulation
    
    fields = [
        'model',
        'runs',
        'periods',
        ]
    
class SimulationDeleteView(generic.DeleteView):
    model = models.simulation
    
    fields = [
        'model',
        'runs',
        'periods',
        ]
    
class SimulationRunView(generic.DetailView):
    model = models.simulation
    
    fields = [
        'model',
        'runs',
        'periods',
        'evt_created',
        'evt_changed',
        ]
    
#==============================================================================
#  Flow Compartment Records
#==============================================================================

# Implement when needed

#==============================================================================
#  Stock Records
#==============================================================================

# Implement when needed
    
#==============================================================================
#  Results
#==============================================================================

class ResultsTemplateView(generic.TemplateView):
    template_name = 'dpmfa/results/results.html'
    
    def get_context_data(self, **kwargs):
        context = super(ResultsTemplateView, self).get_context_data(**kwargs)

        context['model_instance'] = self.getModelInstance(self.kwargs['experiment_pk'])
        context['experiment'] = self.getExperiment(self.kwargs['experiment_pk'])
        context['flow_compartment_results'] = self.getFlowCompartmentResults(self.kwargs['experiment_pk'])
        context['stock_results'] = self.getStockResults(self.kwargs['experiment_pk'])
        context['sink_results'] = self.getSinkResults(self.kwargs['experiment_pk'])
        
        return context
    
    def getModelInstance(self, experiment_pk):
        experiment = models.experiment.objects.get(pk=experiment_pk)
        return models.model_instance.objects.get(pk=experiment.model_instance)
    
    def getExperiment(self, experiment_pk):
        return models.experiment.objects.get(pk=experiment_pk)
    
    def getFlowCompartmentResults(self, experiment_pk):
        return models.result.objects.filter(experiment=experiment_pk, entity_type=models.result.FLOW_COMPARTEMENT)
    
    def getStockResults(self, experiment_pk):
        return models.result.objects.filter(experiment=experiment_pk, entity_type=models.result.STOCK)
    
    def getSinkResults(self, experiment_pk):
        return models.result.objects.filter(experiment=experiment_pk, entity_type=models.result.SINK)

class ResultDetailView(generic.DetailView):
    model = models.result
    