from django import forms

import dpmfa.models as django_models


# ==============================================================================
#  Project
# ==============================================================================

class ProjectForm(forms.ModelForm):
    class Meta:
        model = django_models.project
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

# ==============================================================================
#  Model
# ==============================================================================

class ModelForm(forms.ModelForm):
    class Meta:
        model = django_models.model
        fields = ('name', 'description')
        
        widgets = {
            'name': forms.widgets.TextInput(attrs={'type': 'text',
                                                   'class': 'form-control',
                                                   'id': 'modelName',
                                                   'placeholder' : 'Enter a model name'}),
            'description': forms.widgets.Textarea(attrs={'type': 'text',
                                                   'class': 'form-control',
                                                   'id':'modelDescription',
                                                   'placeholder' : 'Enter a model description'}),
            }
