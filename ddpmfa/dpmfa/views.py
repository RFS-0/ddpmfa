from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("You are at the home page. This is site provides information about the WebApp.")

def project_administration(request):
    return HttpResponse("You are at the project administration site. Here you can add and edit projects.")

def project_overview(request, project_name):
    return HttpResponse("You are at the project overview site of project: %s" % project_name)

def model_overview(request, project_name):
    return HttpResponse("You are at the model over view site for project: %s" % project_name)