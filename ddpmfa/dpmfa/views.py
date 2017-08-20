from django.contrib import messages
from django.http import HttpResponse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.urls import reverse_lazy, reverse

from itertools import chain

import dpmfa.forms as forms
import dpmfa.models as models


# ==============================================================================
#  Home
# ==============================================================================


class HomeTemplateView(generic.TemplateView):
    template_name = 'dpmfa/home/home.html'
    context_object_name = 'home'
    
class ExampleTemplateView(generic.TemplateView):
    template_name = 'dpmfa/home/example.html'
    context_object_name = 'example'

class QuickReferenceTemplateView(generic.TemplateView):
    template_name = 'dpmfa/home/quick_reference.html'
    context_object_name = 'quick-reference'
    
class DocumentationTemplateView(generic.TemplateView):
    template_name = 'dpmfa/home/documentation.html'
    context_object_name = 'documentation'
    

# ==============================================================================
#  Project
# ==============================================================================


class ProjectListView(generic.ListView):
    model = models.project
    context_object_name = 'projects'
    template_name = 'dpmfa/project/project_list.html'


class ProjectDetailView(generic.DetailView):
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

    def find_external_list_inflows_by_model(self, model_pk):
        return models.external_list_inflow.objects.filter(target__model=model_pk)

    def find_external_function_inflows_by_model(self, model_pk):
        return models.external_function_inflow.objects.filter(target__model=model_pk)

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

    def find_flow_compartments_by_model(self, model_pk):
        return models.flow_compartment.objects.filter(model=model_pk)

    def find_stocks_by_model(self, model_pk):
        return models.stock.objects.filter(model=model_pk)

    def find_sinks_by_model(self, model_pk):
        return models.sink.objects.filter(model=model_pk)
    
    def find_simulation_by_model(self, model_pk):
        return models.simulation.objects.get(model=model_pk)
    
    def find_result_by_model(self, model_pk):
        return models.result.objects.filter(model=model_pk)

    def get_context_data(self, **kwargs):
        context = super(ModelDetailView, self).get_context_data(**kwargs)

        context['external_list_inflows'] = self.find_external_list_inflows_by_model(self.object.pk)
        context['external_function_inflows'] = self.find_external_function_inflows_by_model(self.object.pk)

        context['constant_transfers'] = self.find_constant_transfers_by_model(self.object.pk, False)
        context['random_choice_transfers'] = self.find_random_choice_transfers_by_model(self.object.pk, False)
        context['stochastic_transfers'] = self.find_stochastic_transfers_by_model(self.object.pk, False)
        context['aggregated_transfers'] = self.find_aggregated_transfers_by_model(self.object.pk, False)

        context['flow_compartments'] = self.find_flow_compartments_by_model(self.object.pk)
        context['stocks'] = self.find_stocks_by_model(self.object.pk)
        context['sinks'] = self.find_sinks_by_model(self.object.pk)
        context['simulation'] = self.find_simulation_by_model(self.object.pk)
        context['results'] = self.find_result_by_model(self.object.pk)

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
#  Model Designer
# ==============================================================================

# class ModelDesingerDetailView(generic.DetailView):
#     model = models.model_designer

class ModelDesingerCreateView(generic.CreateView):
    model = models.model_designer
    template_name = 'dpmfa/model_designer/model_designer_form.html'
    
    fields = [
        'designer_configuration',
        ]

    def get_success_url(self, **kwargs):
        return reverse_lazy('dpmfa:model-detail', kwargs={'pk': self.object.model_designer.model})

    def form_valid(self, form):
        model = form.save(commit=False)
        model.model_id = self.kwargs['model_pk']
        return super(ModelDesingerCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ModelDesingerCreateView, self).get_context_data(**kwargs)
        context['model'] = models.model.objects.get(pk=self.kwargs['model_pk'])
        return context
    
class ModelDesingerUpdateView(generic.UpdateView):
    model = models.model_designer
    template_name = 'dpmfa/model_designer/model_designer_form.html'
    
    fields = [
        'designer_configuration',
        ]

    def get_context_data(self, **kwargs):
        context = super(ModelDesingerUpdateView, self).get_context_data(**kwargs)
        context['model'] = models.model_designer.objects.get(pk=self.kwargs['pk']).model
        return context

class ModelDesingerDeleteView(generic.UpdateView):
    model = models.model
    
class ModelDesignerRedirectView(generic.RedirectView):
    permanent = False
    query_string = False
    
    def get_redirect_url(self, *args, **kwargs):
        try:
            print("trying to get designer")
            designer = models.model_designer.objects.get(model_id=self.kwargs['model_pk'])
            print("got designer")
            print("not yet redirected")
            return designer.get_absolute_url()
            print("redirected")
        except:
            return reverse_lazy('dpmfa:designer-create', kwargs={'model_pk': self.kwargs['model_pk']})

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
    
class FlowCompartmentUpdateView(generic.UpdateView):
    model = models.flow_compartment
    template_name = 'dpmfa/compartments/flow_compartment_form.html'
    
    fields = [
        'name',
        'description',
        'categories',
        'adjust_outgoing_tcs',
        'log_inflows',
        'log_outflows',
        ]

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
    
    fields = [
        'name',
        'description',
        'categories',
        'adjust_outgoing_tcs',
        'log_inflows',
        'log_outflows',
        ]

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
    
    fields = [
        'name',
        'description',
        'log_inflows',
        'categories',
        ]

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
    
    fields = [
        'stock_of_local_release',
        'name',
        'delay'
        ]
    
# Fixed Rate Release

class FixedRateReleaseDetailView(generic.DetailView):
    model = models.fixed_rate_release
    
    fields = [
        'stock_of_local_release',
        'name',
        'delay',
        'fixed_rate_release'
        ]
    
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
    
#==============================================================================
#  Transfers
#==============================================================================

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
    
    fields = [
        'target',
        'belongs_to_aggregated_transfer',
        'name',
        'priority',
        'current_tc',
        'weight',
        'value'
        ]
    
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
    
    fields = [
        'target',
        'belongs_to_aggregated_transfer',
        'name',
        'priority',
        'current_tc',
        'weight',
        'sample'
        ]

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
    
    fields = [
        'target',
        'belongs_to_aggregated_transfer',
        'name',
        'priority',
        'current_tc',
        'weight',
        'sample'
        ]

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
    
    fields = [
        'target',
        'belongs_to_aggregated_transfer',
        'name',
        'priority',
        'current_tc',
        'weight'
        ]
    
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
    
    fields = [
        'target',
        'belongs_to_aggregated_transfer',
        'name',
        'priority',
        'current_tc',
        'weight'
        ]
    
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

# External Inflow

# class ExternalInflowDetailView(generic.DetailView):
#    model = models.external_inflow
#
#    fields = [
#        'target',
#        'name',
#        'start_delay',
#        'derivation_distribution',
#        'derivation_parameters',
#        'derivation_factor'
#        ]

#class ExternalInflowCreateView(generic.CreateView):
#    model = models.external_inflow
#
#    fields = [
#        'target',
#        'name',
#        'start_delay',
#        'derivation_distribution',
#        'derivation_parameters',
#        'derivation_factor'
#        ]

#class ExternalInflowUpdateView(generic.UpdateView):
#    model = models.external_inflow
#
#    fields = [
#        'target',
#        'name',
#        'start_delay',
#        'derivation_distribution',
#        'derivation_parameters',
#        'derivation_factor'
#        ]
    
#class ExternalInflowDeleteView(generic.DeleteView):
#    model = models.external_inflow
#
#    fields = [
#        'target',
#        'name',
#        'start_delay',
#        'derivation_distribution',
#        'derivation_parameters',
#        'derivation_factor'
#        ]
    
# External List Inflow

class ExternalListInflowDetailView(generic.DetailView):
    model = models.external_list_inflow
    template_name = 'dpmfa/external_inflow/external_list_inflow_detail.html'
    
    def find_fixed_value_inflows_by_external_list_inflow(self, ext_list_pk):
        return models.fixed_value_inflow.objects.filter(external_list_inflow__pk=ext_list_pk).order_by('period')

    def find_stochastic_function_inflows_by_external_list_inflow(self, ext_list_pk):
        return models.stochastic_function_inflow.objects.filter(external_list_inflow=ext_list_pk).order_by('period')

    def find_random_choice_inflows_by_external_list_inflow(self, ext_list_pk):
        return models.random_choice_inflow.objects.filter(external_list_inflow=ext_list_pk).order_by('period')

    def get_context_data(self, **kwargs):
        context = super(ExternalListInflowDetailView, self).get_context_data(**kwargs)

        fixed_value_inflows = self.find_fixed_value_inflows_by_external_list_inflow(self.object.pk)
        stochastic_function_inflows = self.find_stochastic_function_inflows_by_external_list_inflow(self.object.pk)
        random_choice_inflows = self.find_random_choice_inflows_by_external_list_inflow(self.object.pk)

        single_period_inflows = list(chain(fixed_value_inflows, stochastic_function_inflows, random_choice_inflows))
        single_period_inflows.sort(key=lambda x: x.period)

        if len(single_period_inflows) == 0:
            context['last_period'] = 0
        else:
            context['last_period'] = single_period_inflows[-1].period

        context['single_period_inflows'] = single_period_inflows

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
    
    fields = [
        'target',
        'name',
        'start_delay',
        'derivation_distribution',
        'derivation_parameters',
        'derivation_factor'
        ]
    
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
#  Fixed Value Inflow
#==============================================================================

class FixedValueInflowDetailView(generic.DetailView):
    model = models.fixed_value_inflow

    def get_context_data(self, **kwargs):
        context = super(FixedValueInflowDetailView, self).get_context_data(**kwargs)

        external_list_inflow_pk = self.object.external_list_inflow.pk
        context['external_list_inflow'] = models.external_list_inflow.objects.get(pk=external_list_inflow_pk)

        return context

class FixedValueInflowUpdateView(generic.UpdateView):
    model = models.fixed_value_inflow

    fields = ['value']

    def get_context_data(self, **kwargs):
        context = super(FixedValueInflowUpdateView, self).get_context_data(**kwargs)

        external_list_inflow_pk = self.object.external_list_inflow.pk
        context['external_list_inflow'] = models.external_list_inflow.objects.get(pk=external_list_inflow_pk)

        return context

    def get_success_url(self, **kwargs):
        external_list_inflow_pk = self.object.external_list_inflow.pk
        return reverse_lazy('dpmfa:external-list-inflow-detail', kwargs={'pk': external_list_inflow_pk})

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

# ==============================================================================
#  Random Choice Inflow
# ==============================================================================

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

    fields = ['sample']

    def get_context_data(self, **kwargs):
        context = super(RandomChoiceInflowUpdateView, self).get_context_data(**kwargs)

        external_list_inflow_pk = self.object.external_list_inflow.pk
        context['external_list_inflow'] = models.external_list_inflow.objects.get(pk=external_list_inflow_pk)

        return context

    def get_success_url(self, **kwargs):
        external_list_inflow_pk = self.object.external_list_inflow.pk
        return reverse_lazy('dpmfa:external-list-inflow-detail', kwargs={'pk': external_list_inflow_pk})


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


# ==============================================================================
#  Stochastic Function Inflow
# ==============================================================================

class StochasticFunctionInflowDetailView(generic.DetailView):
    model = models.stochastic_function_inflow

    def get_context_data(self, **kwargs):
        context = super(StochasticFunctionInflowDetailView, self).get_context_data(**kwargs)

        external_list_inflow_pk = self.object.external_list_inflow.pk
        context['external_list_inflow'] = models.external_list_inflow.objects.get(pk=external_list_inflow_pk)

        return context

class StochasticFunctionInflowUpdateView(generic.UpdateView):
    model = models.stochastic_function_inflow

    fields = ['pdf', 'parameter_values']

    def get_context_data(self, **kwargs):
        context = super(StochasticFunctionInflowUpdateView, self).get_context_data(**kwargs)

        external_list_inflow_pk = self.object.external_list_inflow.pk
        context['external_list_inflow'] = models.external_list_inflow.objects.get(pk=external_list_inflow_pk)

        return context

    def get_success_url(self, **kwargs):
        external_list_inflow_pk = self.object.external_list_inflow.pk
        return reverse_lazy('dpmfa:external-list-inflow-detail', kwargs={'pk': external_list_inflow_pk })


class StochasticFunctionInflowDeleteView(generic.DeleteView):
    model = models.stochastic_function_inflow

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

class ResultsDetailView(generic.DetailView):
    model = models.result

class ResultsDeleteView(generic.DeleteView):
    model = models.result
