from django.contrib import messages
from django.http import HttpResponse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

import dpmfa.forms as forms
import dpmfa.models as models


class HomeView(TemplateView):
    template_name = 'dpmfa/home.html'


class ProjectsView(ListView):
    model = models.project
    context_object_name = 'projects'
    template_name = 'dpmfa/projects.html'


class ProjectView(DetailView):
    model = models.project
    context_object_name = 'project'
    template_name = 'dpmfa/project.html'


class ProjectCreateView(CreateView):
    model = models.project
    fields = ['name', 'description']
    template_name = 'dpmfa/new_project.html'
    success_url = reverse_lazy('dpmfa:projects')


class ProjectUpdateView(UpdateView):
    model = models.project
    fields = ['name', 'description']
    template_name = 'dpmfa/update_project.html'
    success_url = reverse_lazy('dpmfa:projects')


class ProjectDeleteView(DeleteView):
    model = models.project
    success_url = reverse_lazy('dpmfa:projects')


class ModelView(DetailView):
    model = models.model
    template_name = 'dpmfa/model.html'


class ModelCreateView(CreateView):
    model = models.model
    template_name = 'dpmfa/new_model.html'
    fields = ['name', 'description']

    # Change!
    # success_url = reverse_lazy('dpmfa:project', model.project_id)

    def get_success_url(self, **kwargs):
        return reverse_lazy('dpmfa:project', kwargs={'pk': self.kwargs['project_pk']})

    def form_valid(self, form):
        model = form.save(commit=False)
        model.project_id = self.kwargs['project_pk']
        return super(ModelCreateView, self).form_valid(form)


def delete_model(request, model_pk):
    return HttpResponse("Delete model " + model_pk)

def designer(request, model_pk):
    return HttpResponse("Designer " + model_pk)

def save_designer(request, model_pk):
    return HttpResponse("Save designer " + model_pk)

def update_designer(request, model_pk):
    return HttpResponse("Update designer " + model_pk)

def parameters(request, model_pk):
    return HttpResponse("Parameters for model " + model_pk)

def flow_compartment(request, flow_compartment_pk):
    return HttpResponse("Flow  " + flow_compartment_pk)

def sink(request, sink_pk):
    return HttpResponse("Sink " + sink_pk)

def stock(request, stock_pk):
    return HttpResponse("Stock " + stock_pk)

def list_inflow(request, inflow_pk):
    return HttpResponse("external_list_inflow: " + inflow_pk)

def function_inflow(request, inflow_pk):
    return HttpResponse("external_function_inflow: " + inflow_pk)

#==============================================================================
#  Transfers
#==============================================================================

# Constant

class ConstantTransferDetailView(generic.DetailView):
    model = models.constant_transfer
    
    fields = [
        'target',
        'belongs_to_aggregated_transfer',
        'name',
        'priority',
        'current_tc',
        'weight',
        'value'
        ]

class ConstantTransferCreateView(generic.CreateView):
    model = models.constant_transfer
    
    fields = [
        'target',
        'belongs_to_aggregated_transfer',
        'name',
        'priority',
        'current_tc',
        'weight',
        'value'
        ]
    
class ConstantTransferUpdateView(generic.UpdateView):
    model = models.constant_transfer
    
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
#  Simulation
#==============================================================================
    
class SimulationDetailView(generic.DetailView):
    model = models.simulation
    
    fields = [
        'model',
        'runs',
        'periods',
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
    
#==============================================================================
#  Results
#==============================================================================

class ResultsDetailView(generic.DetailView):
    model = models.model
    template_name = 'dpmfa/model_results_detail.html'
