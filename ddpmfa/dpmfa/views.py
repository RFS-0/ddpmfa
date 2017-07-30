from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    return HttpResponse("You are at the home page. This is site provides information about the WebApp.")

def project_administration(request):
    return HttpResponse("You are at the project administration site. Here you can add and edit projects.")

def project_overview(request, project_name):
    return HttpResponse("You are at the project overview site of project: %s" % project_name)

def model_overview(request, project_name):
    latest_model_list = Model.objects.order_by('-evt_created')[:5]
    ','.join([m.name for  m in latest_model_list])
    return HttpResponse("You are at the model over view site for project: %s"
                        "The latest models you created are: %s" % (project_name, latest_model_list))