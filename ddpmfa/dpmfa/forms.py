from django import forms

import dpmfa.models as django_models


# ==============================================================================
#  Project
# ==============================================================================

class ProjectForm(forms.ModelForm):
    class Meta:
        model = django_models.project
        fields = ('name', 
                  'description')
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
        fields = ('name', 
                  'description')
        
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

# ==============================================================================
#  Compartments
# ==============================================================================

# Flow Compartment

class FlowCompartmentForm(forms.ModelForm):
    class Meta:
        model = django_models.flow_compartment
        fields = ('name',
                  'description',
                  'categories',
                  'log_inflows',
                  'log_outflows',
                  'adjust_outgoing_tcs')
        
        widgets = {
            'name': forms.widgets.TextInput(attrs={'type': 'text',
                                                   'class': 'form-control',
                                                   'id': 'flowCompartmentName',
                                                   'placeholder' : 'Enter a flow compartment name'}),
            'description': forms.widgets.Textarea(attrs={'type': 'text',
                                                         'class': 'form-control',
                                                         'id':'flowCompartmentDescription',
                                                         'placeholder' : 'Enter a flow compartment description'}),
            'categories': forms.widgets.TextInput(attrs={'type': 'text',
                                                         'class': 'form-control',
                                                         'id': 'flowCompartmentCategories',
                                                         'placeholder' : 'Enter categories'}),
            'log_inflows': forms.widgets.CheckboxInput(attrs={'type':'checkbox',
                                                              'class': 'checkbox',
                                                              'id': 'flowCompartmentLogInflows'}),
            'log_outflows': forms.widgets.CheckboxInput(attrs={'type':'checkbox',
                                                              'class': 'checkbox',
                                                              'id': 'flowCompartmentLogInflows'}),
            'adjust_outgoing_tcs': forms.widgets.CheckboxInput(attrs={'type':'checkbox',
                                                              'class': 'checkbox',
                                                              'id': 'flowCompartmentLogInflows'})
            }
        
# Stock

class StockForm(forms.ModelForm):
    class Meta:
        model = django_models.stock
        fields = ('name',
                  'description',
                  'local_release',
                  'categories',
                  'log_inflows',
                  'log_outflows',
                  'adjust_outgoing_tcs')
        
        widgets = {
            'name': forms.widgets.TextInput(attrs={'class': 'form-control',
                                                   'id': 'stockName',
                                                   'placeholder' : 'Enter a flow compartment name'}),
            'description': forms.widgets.Textarea(attrs={'class': 'form-control',
                                                         'id':'stockDescription',
                                                         'placeholder' : 'Enter a flow compartment description'}),
            'local_release':forms.widgets.Select(attrs={'class':'form-control',
                                                 'id':'stockLocalRelease'}),
            'categories': forms.widgets.TextInput(attrs={'class': 'form-control',
                                                         'id': 'stockCategories',
                                                         'placeholder' : 'Enter categories'}),
            'log_inflows': forms.widgets.CheckboxInput(attrs={'class': 'checkbox',
                                                              'id': 'stockLogInflows'}),
            'log_outflows': forms.widgets.CheckboxInput(attrs={'class': 'checkbox',
                                                              'id': 'stockLogInflows'}),
            'adjust_outgoing_tcs': forms.widgets.CheckboxInput(attrs={'type':'checkbox',
                                                              'class': 'checkbox',
                                                              'id': 'stockLogInflows'})
            }


# ==============================================================================
#  Compartments
# ==============================================================================

# Local Release

class LocalReleaseForm(forms.ModelForm):
    class Meta:
        model = django_models.local_release
        fields = ('name',
                  'delay')
        
        widgets = {
            'name': forms.widgets.TextInput(attrs={'class': 'form-control',
                                                   'id': 'stockName',
                                                   'placeholder' : 'Enter a flow compartment name'}),
            'delay': forms.widgets.NumberInput(attrs={'type': 'text',
                                                   'class': 'form-control',
                                                   'id': 'stockName',
                                                   'placeholder' : 'Enter a flow compartment name'})
            }

# Fixed Rate Release

class FixedRateReleaseForm(forms.ModelForm):
    class Meta:
        model = django_models.fixed_rate_release
        fields = ('name',
                  'delay',
                  'release_rate')
        
        widgets = {
            'name': forms.widgets.TextInput(attrs={'class': 'form-control',
                                                   'id': 'stockName',
                                                   'placeholder' : 'Enter a flow compartment name'}),
            'delay': forms.widgets.NumberInput(attrs={'type': 'text',
                                                   'class': 'form-control',
                                                   'id': 'stockName',
                                                   'placeholder' : 'Enter a flow compartment name'}),
            'release_rate': forms.widgets.NumberInput(attrs={'type': 'text',
                                                   'class': 'form-control',
                                                   'id': 'stockName',
                                                   'placeholder' : 'Enter a flow compartment name'})
            }
        
class FunctionReleaseForm(forms.ModelForm):
    class Meta:
        model = django_models.function_release
        fields = ('name',
                  'delay',
                  'release_function',
                  'function_parameters')
        
        widgets = {
            'name': forms.widgets.TextInput(attrs={'class': 'form-control',
                                                   'id': 'stockName',
                                                   'placeholder' : 'Enter a flow compartment name'}),
            'delay': forms.widgets.NumberInput(attrs={'type': 'text',
                                                   'class': 'form-control',
                                                   'id': 'stockName',
                                                   'placeholder' : 'Enter a flow compartment name'}),
            'release_rate': forms.widgets.NumberInput(attrs={'type': 'text',
                                                   'class': 'form-control',
                                                   'id': 'stockName',
                                                   'placeholder' : 'Enter a flow compartment name'})
            }

