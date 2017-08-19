from django import forms

from .models import *

class ProjectForm(forms.ModelForm):
    class Meta:
        model = project
        fields = ('name', 'description')
        widgets = {
            'name': forms.widgets.TextInput(attrs={'type': 'text',
                                                   'class': 'form-control',
                                                   'id': 'projectName',
                                                   'placeholder' : 'Enter a project name'}),
            'description': forms.widgets.Textarea(attrs={'type': 'text',
                                                   'class': 'form-control',
                                                   'id':'projectDescription',
                                                   'placeholder' : 'Enter a project description'}),
            }

