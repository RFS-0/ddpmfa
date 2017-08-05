from django.contrib import messages
from django.http import HttpResponse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
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
        model = form.save(commit = False)
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

def constant_transfer(request, transfer_pk):
    return HttpResponse("constant_transfer: " + transfer_pk)

def random_choice_transfer(request, transfer_pk):
    return HttpResponse("random_choice_transfer: " + transfer_pk)

def aggregated_transfer(request, transfer_pk):
    return HttpResponse("aggregated_transfer: " + transfer_pk)

def stochastic_transfer(request, transfer_pk):
    return HttpResponse("stochastic_transfer: " + transfer_pk)

def simulation(request, model_pk):
    return HttpResponse("Simulation for model " + model_pk)

def run_simulation(request, model_pk):
    return HttpResponse("Run simulation for model " + model_pk)

def results(request, model_pk):
    return HttpResponse("Results for model " + model_pk)

"""
def project_administration(request):
    return HttpResponse("You are at the project administration site. Here you can add and edit projects.")

def project_overview(request, project_name):
    return HttpResponse("You are at the project overview site of project: %s" % project_name)

def model_overview(request, model_name):
    primary_key = model_name
    model = get_object_or_404(Model, pk=primary_key)
    model_attributes = {} 
    model_attributes['Name of the model: '] = model.name
    model_attributes['Description of the model: '] = model.description
    context = {
    'primary_key': primary_key,
    'model_attributes': model_attributes,
    }
    
    return render(request, 'dpmfa/model_overview.html', context)
"""

"""def model_configuratio(request, model_name):
    try:
<<<<<<< HEAD
        model = model.objects.get(pk=project_name)
        latest_model_list = model.objects.order_by('-evt_created')[:5]
=======
        model = Model.objects.get(pk=model_name)
>>>>>>> refs/heads/master
        context = {
<<<<<<< HEAD
        'latest_model_list': latest_model_list,
        }
    
    except model.DoesNotExist:
        raise Http404("Model does not exist")
=======
        'model_attributes': model_attributes,
            }
          
    except Model.DoesNotExist:
        raise Http404("This model does not exist.")
>>>>>>> refs/heads/master
    
    return render(request, )"""