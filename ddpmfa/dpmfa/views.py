from django.contrib import messages
from django.http import HttpResponse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic

import dpmfa.forms as forms
import dpmfa.models as models


class HomeView(generic.TemplateView):
    template_name = 'dpmfa/home.html'


class ProjectsView(generic.ListView):
    model = models.project
    context_object_name = 'projects'
    template_name = 'dpmfa/projects.html'


class ProjectView(generic.DetailView):
    model = models.project
    context_object_name = 'project'
    template_name = 'dpmfa/project.html'


#def projects(request):
#    context = {}
#    context['projects'] = models.project.objects.all()
#    return render(request, 'dpmfa/projects.html', context)

#def project(request, project_pk):
#    context = {}
#    context['project'] = get_object_or_404(models.project, pk=project_pk)
#    #context['message'] = models.project.objects.all().count()
#    return render(request, 'dpmfa/project.html', context)

def new_project(request):
    context = {}

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.project_form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            project = models.project(name=form.cleaned_data['name'], description=form.cleaned_data['description'])
            project.save()

            messages.success(request, 'New project "%s" was created.' % project.name)
#            messages.error(request, 'This would be an error message')
#            messages.debug(request, 'This would be a debug message')
#            messages.info(request, 'This would be an info message')
#            messages.warning(request, 'This would be a warning message')

            return HttpResponseRedirect('/dpmfa/projects/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = forms.project_form()

    context['form'] = form

    return render(request, 'dpmfa/new_project.html', context)

def delete_project(request, project_pk):
    project = get_object_or_404(models.project, pk=project_pk)
    project_name = project.name
    project.delete()
    messages.success(request, 'New project "%s" was deleted.' % project_name)
    return HttpResponseRedirect('/dpmfa/projects/')

def new_model(request, project_pk):
    context = {}

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.model_form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            model = models.model(name=form.cleaned_data['name'], description=form.cleaned_data['description'])
            model.save()

            messages.success(request, 'New model "%s" was created.' % model.name)
#            messages.error(request, 'This would be an error message')
#            messages.debug(request, 'This would be a debug message')
#            messages.info(request, 'This would be an info message')
#            messages.warning(request, 'This would be a warning message')

            return HttpResponseRedirect('/dpmfa/project/'+project_pk)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = forms.model_form()

    context['form'] = form

    return render(request, 'dpmfa/new_model.html', context)

class ModelUpdateView(generic.UpdateView):
    model = models.model
    
    fields = ['project', 
              'name',
              'description',
              'seed'
             ]

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
