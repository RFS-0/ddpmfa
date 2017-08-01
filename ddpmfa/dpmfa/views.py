from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import *

def home(request):
    context = {}
    return render(request, 'dpmfa/home.html', context)

def projects(request):
    return HttpResponse("Projects")

def project(request, project_pk):
    return HttpResponse("Project " + project_pk)

def new_project(request):
    return HttpResponse("New project")

def delete_project(request, project_pk):
    return HttpResponse("Delete project " + project_pk)

def new_model(request, project_pk):
    return HttpResponse("New model for project " + project_pk)

def model(request, model_pk):
    return HttpResponse("Model (overview) " + model_pk)

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