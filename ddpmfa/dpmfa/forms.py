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
            'name': forms.widgets.TextInput(attrs={'class': 'form-control',
                                                   'id': 'projectName',
                                                   'placeholder' : 'Enter a project name'}),
            'description': forms.widgets.Textarea(attrs={'class': 'form-control',
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
            'name': forms.widgets.TextInput(attrs={'class': 'form-control',
                                                   'id': 'modelName',
                                                   'placeholder' : 'Enter a model name'}),
            'description': forms.widgets.Textarea(attrs={'class': 'form-control',
                                                   'id':'modelDescription',
                                                   'placeholder' : 'Enter a model description'}),
            }

# ==============================================================================
#  Experiment
# ==============================================================================

class ExperimentForm(forms.ModelForm):
    class Meta:
        model = django_models.experiment
        fields = ('name', 'runs', 'periods')

        widgets = {
            'name': forms.widgets.TextInput(attrs={'class': 'form-control',
                                                   'id': 'experimentName',
                                                   'placeholder': 'Enter an experiment name'}),
            'runs': forms.widgets.NumberInput(attrs={'class': 'form-control',
                                                       'id': 'experimentRuns',
                                                       'placeholder': 'Enter the number of runs for the simulation'}),
            'periods': forms.widgets.NumberInput(attrs={'class': 'form-control',
                                                       'id': 'experimentPeriods',
                                                       'placeholder': 'Enter the number of periods for the simulation'}),
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
            'name': forms.widgets.TextInput(attrs={'class': 'form-control',
                                                   'id': 'flowCompartmentName',
                                                   'placeholder' : 'Enter a name'}),
            'description': forms.widgets.Textarea(attrs={'class': 'form-control',
                                                         'id':'flowCompartmentDescription',
                                                         'placeholder' : 'Enter a description'}),
            'categories': forms.widgets.TextInput(attrs={'class': 'form-control',
                                                         'id': 'flowCompartmentCategories',
                                                         'placeholder' : 'Enter categories'}),
            'log_inflows': forms.widgets.CheckboxInput(attrs={'class': 'checkbox',
                                                              'id': 'flowCompartmentLogInflows'}),
            'log_outflows': forms.widgets.CheckboxInput(attrs={'class': 'checkbox',
                                                              'id': 'flowCompartmentLogOutflows'}),
            'adjust_outgoing_tcs': forms.widgets.CheckboxInput(attrs={'class': 'checkbox',
                                                              'id': 'flowCompartmentAdjustTCs'})
            }
        
# Stock

class StockForm(forms.ModelForm):
    class Meta:
        model = django_models.stock
        fields = ('name',
                  'description',
                  'categories',
                  'log_inflows',
                  'log_outflows',
                  'adjust_outgoing_tcs')
        
        widgets = {
            'name': forms.widgets.TextInput(attrs={'class': 'form-control',
                                                   'id': 'stockName',
                                                   'placeholder' : 'Enter a name'}),
            'description': forms.widgets.Textarea(attrs={'class': 'form-control',
                                                         'id':'stockDescription',
                                                         'placeholder' : 'Enter a description'}),
            'categories': forms.widgets.TextInput(attrs={'class': 'form-control',
                                                         'id': 'stockCategories',
                                                         'placeholder' : 'Enter categories'}),
            'log_inflows': forms.widgets.CheckboxInput(attrs={'class': 'checkbox',
                                                              'id': 'stockLogInflows'}),
            'log_outflows': forms.widgets.CheckboxInput(attrs={'class': 'checkbox',
                                                              'id': 'stockLogOutflows'}),
            'adjust_outgoing_tcs': forms.widgets.CheckboxInput(attrs={'type':'checkbox',
                                                              'class': 'checkbox',
                                                              'id': 'stockAdjustOutgoingTCs'})
            }

# ==============================================================================
#  Sinks
# ==============================================================================

class SinkForm(forms.ModelForm):
    class Meta:
        model = django_models.sink
        fields = ('name',
                  'description',
                  'categories',
                  'log_inflows')
        
        widgets = {
            'name': forms.widgets.TextInput(attrs={'class': 'form-control',
                                                   'id': 'sinkName',
                                                   'placeholder' : 'Enter a name'}),
            'description': forms.widgets.Textarea(attrs={'class': 'form-control',
                                                         'id':'sinkDescription',
                                                         'placeholder' : 'Enter a description'}),
            'categories': forms.widgets.TextInput(attrs={'class': 'form-control',
                                                         'id': 'sinkCategories',
                                                         'placeholder' : 'Enter categories'}),
            'log_inflows': forms.widgets.CheckboxInput(attrs={'class': 'checkbox',
                                                              'id': 'sinkkLogInflows'}),
            }


# ==============================================================================
#  Releases
# ==============================================================================

# Local Release

class LocalReleaseForm(forms.ModelForm):
    class Meta:
        model = django_models.local_release
        fields = ('name',
                  'delay')
        
        widgets = {
            'name': forms.widgets.TextInput(attrs={'class': 'form-control',
                                                   'id': 'localReleasekName',
                                                   'placeholder' : 'Enter a name'}),
            'delay': forms.widgets.NumberInput(attrs={'type': 'text',
                                                   'class': 'form-control',
                                                   'id': 'localReleaseName',
                                                   'placeholder' : 'Enter a delay'})
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
                                                   'id': 'fixedRateReleasekName',
                                                   'placeholder' : 'Enter a name'}),
            'delay': forms.widgets.NumberInput(attrs={'type': 'text',
                                                   'class': 'form-control',
                                                   'id': 'fixedRateReleaseName',
                                                   'placeholder' : 'Enter a delay'}),
            'release_rate': forms.widgets.NumberInput(attrs={'class': 'form-control',
                                                   'id': 'fixedRateReleaseReleaseRate',
                                                   'placeholder' : 'Enter a release rate'})
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
                                                   'id': 'functionReleaseName',
                                                   'placeholder' : 'Enter a name'}),
            'delay': forms.widgets.NumberInput(attrs={'class': 'form-control',
                                                   'id': 'functionReleaseDelay',
                                                   'placeholder' : 'Enter a delay'}),
            'release_rate': forms.widgets.NumberInput(attrs={'type': 'text',
                                                   'class': 'form-control',
                                                   'id': 'functionReleaseRate',
                                                   'placeholder' : 'Enter a release rate'}),
            'release_function': forms.widgets.Select(attrs={'class':'form-control',
                                                           'id':'functionReleaseFunction'}),
            'function_parameters': forms.widgets.NumberInput(attrs={'class':'form-control',
                                                           'id':'functionReleaseFunctionParameters'}),       
            }

# ==============================================================================
#  Transfers
# ==============================================================================

# Constant Transfer

class ConstantTransferForm(forms.ModelForm):
    class Meta:
        model = django_models.constant_transfer
        fields = ('name',
                  'priority',
                  'value')
        
        widgets = {
            'name': forms.widgets.TextInput(attrs={'class': 'form-control',
                                                   'id': 'constantTransferName',
                                                   'placeholder' : 'Enter a name'}),
            'priority': forms.widgets.NumberInput(attrs={'class': 'form-control',
                                                   'id': 'constantTransferPriority',
                                                   'placeholder' : 'Enter a priority'}),
            'value': forms.widgets.NumberInput(attrs={'class': 'form-control',
                                                   'id': 'constantTransferWeight',
                                                   'placeholder' : 'Enter a value'})
            }
        
# Random Choice Transfer
        
class RandomChoiceTransferForm(forms.ModelForm):
    class Meta:
        model = django_models.random_choice_transfer
        fields = ('name',
                  'priority',
                  'sample')
        
        widgets = {
            'name': forms.widgets.TextInput(attrs={'class': 'form-control',
                                                   'id': 'randomChoiceTransferrName',
                                                   'placeholder' : 'Enter a name'}),
            'priority': forms.widgets.NumberInput(attrs={'class': 'form-control',
                                                   'id': 'randomChoiceTransferrPriority',
                                                   'placeholder' : 'Enter a priority'}),
            'sample': forms.widgets.TextInput(attrs={'class': 'form-control',
                                                   'id': 'randomChoiceTransferSample',
                                                   'placeholder' : 'Enter a sample'})
            }
        
# Aggregated Transfer    
        
class AggregatedTransferForm(forms.ModelForm):
    class Meta:
        model = django_models.aggregated_transfer
        fields = ('name',
                  'priority',
                  'weights')
        
        widgets = {
            'name': forms.widgets.TextInput(attrs={'class': 'form-control',
                                                   'id': 'aggregatedTransferrName',
                                                   'placeholder' : 'Enter a name'}),
            'priority': forms.widgets.NumberInput(attrs={'class': 'form-control',
                                                   'id': 'aggregatedTransferrPriority',
                                                   'placeholder' : 'Enter a priority'}),
            'weight': forms.widgets.NumberInput(attrs={'class': 'form-control',
                                                   'id': 'aggregatedTransferrWeight',
                                                   'placeholder' : 'Enter a weight'}),
            'weights': forms.widgets.TextInput(attrs={'class': 'form-control',
                                                   'id': 'aggregatedTransferrWeights',
                                                   'placeholder' : 'Enter weights'})
            }

# Stochastic Transfer 
        
class StochasticTransferForm(forms.ModelForm):
    class Meta:
        model = django_models.stochastic_transfer
        fields = ('name',
                  'priority',
                  'function',
                  'parameters')
        
        widgets = {
            'name': forms.widgets.TextInput(attrs={'class': 'form-control',
                                                   'id': 'stochasticTransferrName',
                                                   'placeholder' : 'Enter a name'}),
            'priority': forms.widgets.NumberInput(attrs={'class': 'form-control',
                                                   'id': 'stochasticTransferPriority',
                                                   'placeholder' : 'Enter a priority'}),
            'function': forms.widgets.Select(attrs={'class':'form-control',
                                                                  'id':'stochasticTransferrFunction'}),
            'parameters': forms.widgets.TextInput(attrs={'class': 'form-control',
                                                   'id': 'stochasticTransferParameters',
                                                   'placeholder' : 'Enter parameters'})
            }
# ==============================================================================
#  External Inflows
# ==============================================================================

# External List Inflow

class ExternalListInflowForm(forms.ModelForm):
    class Meta:
        model = django_models.external_list_inflow
        fields = ('name',
                  'start_delay',
                  'derivation_distribution',
                  'derivation_parameters',
                  'derivation_factor')
        
        widgets = {
            'name': forms.widgets.TextInput(attrs={'class': 'form-control',
                                                   'id': 'externalListInflowName',
                                                    'placeholder' : 'Enter a name'}),
            'start_delay': forms.widgets.NumberInput(attrs={'class': 'form-control',
                                                            'id': 'externalListInflowStartDelay',
                                                            'placeholder' : 'Enter delay'}),
            'derivation_distribution':forms.widgets.Select(attrs={'class':'form-control',
                                                                  'id':'externalListInflowDerivationDistribution'}),
            'derivation_parameters': forms.widgets.TextInput(attrs={'class': 'form-control',
                                                                    'id': 'externalListInflowDerivationParameters',
                                                                    'placeholder' : 'Enter the derivation parameters'}),
            'derivation_factor': forms.widgets.NumberInput(attrs={'class': 'form-control',
                                                    'id': 'externalListInflowDerivationFactor',
                                                    'placeholder' : 'Enter derivation factor'})
            }

class ExternalFunctionInflowForm(forms.ModelForm):
    class Meta:
        model = django_models.external_function_inflow
        fields = ('name',
                  'start_delay',
                  'derivation_distribution',
                  'derivation_parameters',
                  'derivation_factor',
                  'inflow_function',
                  'function_parameters')
        
        widgets = {
            'name': forms.widgets.TextInput(attrs={'class': 'form-control',
                                                   'id': 'externalFunctionInflowName',
                                                    'placeholder' : 'Enter a name'}),
            'start_delay': forms.widgets.NumberInput(attrs={'class': 'form-control',
                                                            'id': 'externalFunctionInflowStartDelay',
                                                            'placeholder' : 'Enter delay'}),
            'derivation_distribution':forms.widgets.Select(attrs={'class':'form-control',
                                                                  'id':'externalFunctionInflowDerivationDistribution'}),
            'derivation_parameters': forms.widgets.TextInput(attrs={'class': 'form-control',
                                                                    'id': 'externalFunctionInflowDerivationParameters',
                                                                    'placeholder' : 'Enter the derivation parameters'}),
            'inflow_function': forms.widgets.Select(attrs={'class':'form-control',
                                                                  'id':'externalFunctionInflowInflowFunction'}),
            'function_parameters': forms.widgets.TextInput(attrs={'class': 'form-control',
                                                                    'id': 'externalFunctionInflowFunctionParameters',
                                                                    'placeholder' : 'Enter the derivation parameters'}),
            'derivation_factor': forms.widgets.NumberInput(attrs={'class': 'form-control',
                                    'id': 'externalListInflowDerivationFactor',
                                    'placeholder' : 'Enter derivation factor'})
            }
        
# ==============================================================================
#  Single Period Inflows
# ==============================================================================

# Fixed Value Inflow

class FixedValueInflowForm(forms.ModelForm):
    class Meta:
        model = django_models.fixed_value_inflow
        fields = ('period',
                  'value')
        
        widgets = {
            'period': forms.widgets.NumberInput(attrs={'class': 'form-control',
                                                                'id': 'fixedValueInflowPeriod',
                                                                'placeholder' : 'Enter a period'}),
            'value': forms.widgets.NumberInput(attrs={'class': 'form-control',
                                                                'id': 'fixedValueInflowValue',
                                                                'placeholder' : 'Enter a value'}),
            }
        
class StochasticFunctionInflowForm(forms.ModelForm):
    class Meta:
        model = django_models.stochastic_function_inflow
        fields = ('period',
                  'pdf',
                  'parameter_values')
        
        widgets = {
            'period': forms.widgets.NumberInput(attrs={'class': 'form-control',
                                                                'id': 'stochasticFunctionInflowPeriod',
                                                                'placeholder' : 'Enter a period'}),
            'value': forms.widgets.NumberInput(attrs={'class': 'form-control',
                                                                'id': 'stochasticFunctionInflowValue',
                                                                'placeholder' : 'Enter a value'}),
            'parameter_values': forms.widgets.TextInput(attrs={'class': 'form-control',
                                                   'id': 'stochasticFunctionInflowwParameterValues',
                                                   'placeholder' : 'Enter parameter values'}),
            }

class RandomChoiceInflowForm(forms.ModelForm):
    class Meta:
        model = django_models.random_choice_inflow
        fields = ('period',
                  'sample')
        
        widgets = {
            'period': forms.widgets.NumberInput(attrs={'class': 'form-control',
                                                                'id': 'randomChoiceInflowPeriod',
                                                                'placeholder' : 'Enter a period'}),
            'sample': forms.widgets.TextInput(attrs={'class': 'form-control',
                                                   'id': 'randomChoiceInflowwParameterValues',
                                                   'placeholder' : 'Enter a sample'}),
            }