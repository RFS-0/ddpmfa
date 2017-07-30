from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Model

def home(request):
    return HttpResponse("You are at the home page. This is site provides information about the WebApp.")

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

"""def model_configuratio(request, model_name):
    try:
        model = Model.objects.get(pk=model_name)
        context = {
        'model_attributes': model_attributes,
            }
          
    except Model.DoesNotExist:
        raise Http404("This model does not exist.")
    
    return render(request, )"""