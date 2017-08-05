from django.contrib import messages
from django.http import HttpResponse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

import dpmfa.forms as forms
import dpmfa.models as models

def home(request):
    context = {}
    return render(request, 'dpmfa/home.html', context)

def projects(request):
    context = {}
    context['projects'] = models.project.objects.all()
    return render(request, 'dpmfa/projects.html', context)

def project(request, project_pk):
    context = {}
    context['project'] = get_object_or_404(models.project, pk=project_pk)
    #context['message'] = models.project.objects.all().count()
    return render(request, 'dpmfa/project.html', context)

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