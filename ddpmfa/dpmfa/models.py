from django.db import models

from django.core.validators import int_list_validator
from django.utils import timezone
from .validators.validator import *
# install this with: pip install jsonfield
from jsonfield import JSONField

from django.urls import reverse
from django.db.models.fields.related import OneToOneField

#==============================================================================
#  Project
#==============================================================================

class project(models.Model):
    
    name = models.CharField(
        verbose_name='Name', 
        max_length=250, 
        null=True)
    
    description = models.TextField(
        verbose_name='Description', 
        null=True)
    
    def __str__(self):
        return self.name + ' (' + str(self.pk) + ')'
    
#==============================================================================
#  Model
#==============================================================================

class model(models.Model):

    project = models.ForeignKey(
        to='project', 
        related_name='models', 
        verbose_name='project', 
        on_delete=models.CASCADE)
    
    
    name = models.CharField(
        verbose_name='Name',
        max_length=250, 
        null=True)
    
    description = models.TextField(
        verbose_name='Description', 
        null=True)
    
    seed = models.FloatField(
        verbose_name='Seed', 
        null=True)
    
    evt_created = models.DateTimeField(
        'Date created', 
        auto_now_add=True)
    
    evt_changed = models.DateTimeField(
        verbose_name='Time of last change',
         auto_now=True)
    
    def __str__(self):
        return self.name + ' (' + str(self.pk) + ')'

class model_instance(model):

    prototype_model = models.ForeignKey(
        to= 'model',
        related_name='model_instances',
        verbose_name='prototype',
        null=True,
        on_delete=models.CASCADE)
    
#==============================================================================
#  Model Designer
#==============================================================================
    
class model_designer(models.Model):
    
    model = models.OneToOneField(
        to=model, 
        related_name='model_desinger', 
        on_delete=models.CASCADE,
        null=True)
    
    
    designer_configuration = JSONField()
    
    evt_created = models.DateTimeField(
        'Date created', 
        auto_now_add=True)
    
    evt_changed = models.DateTimeField(
        verbose_name='Time of last change',
         auto_now=True)
    
    def __str__(self):
        return self.name + ' (' + self.pk + ')'
    
    def get_absolute_url(self):
        return reverse('dpmfa:designer-update', args=[self.id])
    
#==============================================================================
#  Model Parameters
#==============================================================================

class model_parameters(models.Model):
    
    NOT_DEFINED =  'ND'
    NEW = 'NW'
    TO_BE_CONFIGURED = 'TC'
    VALID = 'VA'
    
    STATUS_VARIABLES = (
        (NOT_DEFINED, 'Not defined yet'),
        (NEW, 'New'),
        (TO_BE_CONFIGURED, 'To be configured'),
        (VALID, 'Valid'),
    )
    
    model = models.OneToOneField(
        to=model, 
        related_name='model_parameters', 
        on_delete=models.CASCADE,
        null=True)
    
    
    status = models.CharField(
        max_length=2,
        choices=STATUS_VARIABLES,
        default=NOT_DEFINED,
        null=True
        )
    
    evt_created = models.DateTimeField(
        'Date created', 
        auto_now_add=True)
    
    evt_changed = models.DateTimeField(
        verbose_name='Time of last change',
         auto_now=True)
    
    def __str__(self):
        return self.name + ' (' + self.pk + ')'
    
#==============================================================================
#  Compartment
#==============================================================================

class compartment(models.Model):
    
    model = models.ForeignKey(
        to='model', 
        related_name='compartments', 
        null=True, 
        on_delete=models.CASCADE)
    
    
    name = models.CharField(
        verbose_name='Compartment', 
        max_length=250, 
        null=True)
    
    description = models.TextField(
        verbose_name='description of this model',
        null=True)
    
    evt_created = models.DateTimeField(
        verbose_name='Time of creation', 
        auto_now_add=True)
    
    evt_changed = models.DateTimeField(
        verbose_name='Time of last change', 
        auto_now=True)
    
    log_inflows = models.BooleanField(
        verbose_name='Log inflows', 
        default=True)
    
    categories = models.CharField(
        verbose_name='Categories', 
        validators=[alpha_numeric_list_validator], 
        max_length=250, 
        null=True)
    
    def __str__(self):
        return self.name + ' (' + str(self.pk) + ')'
    
#==============================================================================
#  Flow Compartment
#==============================================================================
    
class flow_compartment(compartment):
    
    adjust_outgoing_tcs = models.BooleanField(
        verbose_name='Adjust outgoing TCs', 
        default=True)
    
    log_outflows = models.BooleanField(
        verbose_name='Log outflows', 
        default=True)
    
    def get_absolute_url(self):
        return reverse('dpmfa:flow-compartment-update', args=[self.id])
    
#==============================================================================
#  Stock
#==============================================================================

class stock(flow_compartment):
    
    local_release = models.OneToOneField(
        to='local_release', 
        related_name='stock', 
        on_delete=models.CASCADE,
        null=True)
    
    def get_absolute_url(self):
        return reverse('dpmfa:stock--update', args=[self.id])
    
#==============================================================================
#  Sink
#==============================================================================
    
class sink(compartment):
    
    def __str__(self):
        return self.name + ' (' + str(self.pk) + ')'
    
    def get_absolute_url(self):
        return reverse('dpmfa:sink-update', args=[self.id])
    
#==============================================================================
#  Releases
#==============================================================================

class local_release(models.Model):
    
    name = models.CharField(
        verbose_name='Local release', 
        default='local release', 
        null=True,
        max_length=250)
    
    delay = models.SmallIntegerField(
        verbose_name='Delay', 
        null=True)
       
    def __str__(self):
        return self.name + ' (' + str(self.pk) + ')'
    
class fixed_rate_release(local_release):
    
    release_rate = models.FloatField(
        verbose_name='Release rate', 
        null=True)
      
class list_release(local_release):
    
    release_rate_list = models.CharField(
        verbose_name='Release rate list', 
        validators=[int_list_validator()], 
        max_length=250, 
        null=True)
    
class function_release(local_release):
    
    LINEAR = 'LI'
    POLYNOMIAL = 'PO'
    EXPONENTIAL = 'EX'
    LOGARITHMIC = 'LG'
    SINE = 'SI'
    COSINE = 'CO'

    FUNCTION_TYPES = (
    (LINEAR, 'Linear function'),
    (POLYNOMIAL, 'Polynomial function'),
    (EXPONENTIAL, 'Exponential function'),
    (LOGARITHMIC, 'Logarithmic function'),
    (SINE, 'Sine'),
    (COSINE, 'Cosine')
    )

    release_function = models.CharField(
        verbose_name='Release function type', 
        choices = FUNCTION_TYPES,
        max_length=250, 
        null=True)

    function_parameters = models.CharField(
        verbose_name='Release function parameters',
        max_length = 250,
        null = True)

#==============================================================================
#  Transfers
#==============================================================================
    
    
class transfer(models.Model):
    
    target=models.ForeignKey(
        to='compartment', 
        on_delete=models.CASCADE, 
        related_name='transfers', 
        null=True)
    
    source_flow_compartment = models.ForeignKey(
        to=flow_compartment, 
        related_name='outgoing_transfers', 
        on_delete=models.CASCADE,
        null=True)
    
    belongs_to_aggregated_transfer = models.ForeignKey(
        to='aggregated_transfer', 
        related_name='transfers', 
        verbose_name='Aggregated transfer', 
        on_delete=models.CASCADE, 
        max_length=250, 
        null=True)  
    
    
    name = models.CharField(
        verbose_name='Name', 
        max_length=250, 
        null=True)
    
    priority = models.SmallIntegerField(
        verbose_name='Priority', 
        null=True)
    
    current_tc = models.FloatField(
        verbose_name='Current transfer coefficient', 
        null=True)
    
    weight = models.FloatField(
        verbose_name='Weight', 
        null=True)   
    
    def __str__(self):
        return self.name + ' (' + str(self.pk) + ')'
    
class constant_transfer(transfer):
    
    value = models.FloatField(
        verbose_name='Value', 
        null=True)
    
    def __str__(self):
        return self.name + ' (' + str(self.pk) + ')'
    
    def get_absolute_url(self):
        return reverse('dpmfa:constant-transfer-update', args=[self.id])
    
class random_choice_transfer(transfer):
    
    sample = models.CharField(
        verbose_name='Sample', 
        validators=[int_list_validator()], 
        max_length=250, 
        null=True)
    
    def __str__(self):
        return self.name + ' (' + str(self.pk) + ')'
    
    def get_absolute_url(self):
        return reverse('dpmfa:random-choice-transfer-update', args=[self.id])
    
class stochastic_transfer(transfer):
    
    NORMAL = 'NORM'
    GEOMETRIC = 'GEO'
    BINOMIAL = 'BINOM'
    EXPONENTIAL = 'EXPO'
    TRIANGULAR = 'TRI'
    UNIFORM = 'UNI'
    GAMMA = 'GAM'
    PARETO = 'PAR'
    POISSON = 'POI'
    CHISQUARE = 'CHI'

    DISTRIBUTION_TYPES = (
    (NORMAL, 'Normal distribution'),
    (GEOMETRIC, 'Geometric distribution'),
    (BINOMIAL, 'Binomial distribution'),
    (EXPONENTIAL, 'Exponential distribution'),
    (TRIANGULAR, 'Triangular distribution'),
    (UNIFORM, 'Uniform distribution'),
    (GAMMA, 'Gamma distribution'),
    (PARETO, 'Pareto distribution'),
    (POISSON, 'Poisson distribution'),
    (CHISQUARE, 'Chisquare distribution'),    
    )
    
    parameters = models.CharField(
        verbose_name='Parameters', 
        validators=[int_list_validator()], 
        max_length=250, 
        null=True)
    
    function = models.CharField(
        choices = DISTRIBUTION_TYPES,
        verbose_name='Function', 
        max_length=250,
        null=True)
    
    def __str__(self):
        return self.name + ' (' + str(self.pk) + ')'
    
    def get_absolute_url(self):
        return reverse('dpmfa:stochastic-transfer-update', args=[self.id])
    
class aggregated_transfer(transfer):
    
    weights = models.CharField(
        verbose_name='Weights', 
        validators=[int_list_validator()], 
        max_length=250, null=True)
    
    priorities = models.CharField(
        verbose_name='Priorities', 
        validators=[int_list_validator()], 
        max_length=250, null=True)
        
    def __str__(self):
        return self.name + ' (' + str(self.pk) + ')'
    
    def get_absolute_url(self):
        return reverse('dpmfa:aggregated-transfer-update', args=[self.id])
    

#==============================================================================
#  External Inflow
#==============================================================================
    
class external_inflow(models.Model):
    
    NORMAL = 'NORM'
    GEOMETRIC = 'GEO'
    BINOMIAL = 'BINOM'
    EXPONENTIAL = 'EXPO'
    TRIANGULAR = 'TRI'
    UNIFORM = 'UNI'
    GAMMA = 'GAM'
    PARETO = 'PAR'
    POISSON = 'POI'
    CHISQUARE = 'CHI'

    DISTRIBUTION_TYPES = (
    (NORMAL, 'Normal distribution'),
    (GEOMETRIC, 'Geometric distribution'),
    (BINOMIAL, 'Binomial distribution'),
    (EXPONENTIAL, 'Exponential distribution'),
    (TRIANGULAR, 'Triangular distribution'),
    (UNIFORM, 'Uniform distribution'),
    (GAMMA, 'Gamma distribution'),
    (PARETO, 'Pareto distribution'),
    (POISSON, 'Poisson distribution'),
    (CHISQUARE, 'Chisquare distribution'),    
    )
    
    target = models.ForeignKey(
        to='compartment', 
        related_name='external_inflows', 
        on_delete=models.CASCADE, 
        null=True)
    
    name = models.CharField(
        verbose_name='Name', 
        max_length=250, 
        null=True)
    
    start_delay = models.SmallIntegerField(
        verbose_name='Start delay', 
        null=True)
    
    derivation_distribution = models.CharField(
        choices = DISTRIBUTION_TYPES,
        verbose_name='Probability density function', 
        max_length=250, 
        null=True)
    
    derivation_parameters = models.CharField(
        verbose_name='Parameter list of the probability distribution function', 
        validators=[int_list_validator()], 
        max_length=250, 
        null=True)
    
    derivation_factor = models.FloatField(
        verbose_name='Derivation factor',
        null=True)
    
    def __str__(self):
        return self.name + ' (' + str(self.pk) + ')'
        
class external_list_inflow(external_inflow):
    
    def __str__(self):
        return self.name + ' (' + str(self.pk) + ')'
    
class external_function_inflow(external_inflow):
    
    NORMAL = 'NORM'
    GEOMETRIC = 'GEO'
    BINOMIAL = 'BINOM'
    EXPONENTIAL = 'EXPO'
    TRIANGULAR = 'TRI'
    UNIFORM = 'UNI'
    GAMMA = 'GAM'
    PARETO = 'PAR'
    POISSON = 'POI'
    CHISQUARE = 'CHI'

    DISTRIBUTION_TYPES = (
    (NORMAL, 'Normal distribution'),
    (GEOMETRIC, 'Geometric distribution'),
    (BINOMIAL, 'Binomial distribution'),
    (EXPONENTIAL, 'Exponential distribution'),
    (TRIANGULAR, 'Triangular distribution'),
    (UNIFORM, 'Uniform distribution'),
    (GAMMA, 'Gamma distribution'),
    (PARETO, 'Pareto distribution'),
    (POISSON, 'Poisson distribution'),
    (CHISQUARE, 'Chisquare distribution'),    
    )
    
    inflow_function = models.CharField(
        verbose_name='Inflow function', 
        choices = DISTRIBUTION_TYPES,
        max_length=250, 
        null=True)

    function_parameters = models.CharField(
        verbose_name='Inflow function parameters',
        max_length = 250,
        null = True)
      
    basic_inflow = models.OneToOneField(
        to='single_period_inflow', 
        verbose_name='name of the single period inflow',
        related_name='external_function_inflow',
        on_delete=models.CASCADE, 
        null=True)
    
    def __str__(self):
        return self.name + ' (' + str(self.pk) + ')'
    
#==============================================================================
#  Single Period Inflow
#==============================================================================  

class single_period_inflow(models.Model):
    
    external_list_inflow = models.ForeignKey(
        to='external_list_inflow', 
        related_name='single_period_inflows', 
        verbose_name='External list inflow', 
        null=True) 
    
    current_value = models.BigIntegerField(
        verbose_name='current inflow value', 
        null=True)
    
    period = models.IntegerField(
        verbose_name='Period', 
        null=True)
    
    def __str__(self):
        return str(self.pk)
    
class fixed_value_inflow(single_period_inflow):
    
    value = models.FloatField(
        verbose_name='the inflow value', 
        null=True)
    
    def get_absolute_url(self):
        return reverse('dpmfa:fixed-value-inflow-update', args=[self.id])
    
class stochastic_function_inflow(single_period_inflow):
    
    NORMAL = 'NORM'
    GEOMETRIC = 'GEO'
    BINOMIAL = 'BINOM'
    EXPONENTIAL = 'EXPO'
    TRIANGULAR = 'TRI'
    UNIFORM = 'UNI'
    GAMMA = 'GAM'
    PARETO = 'PAR'
    POISSON = 'POI'
    CHISQUARE = 'CHI'

    DISTRIBUTION_TYPES = (
    (NORMAL, 'Normal distribution'),
    (GEOMETRIC, 'Geometric distribution'),
    (BINOMIAL, 'Binomial distribution'),
    (EXPONENTIAL, 'Exponential distribution'),
    (TRIANGULAR, 'Triangular distribution'),
    (UNIFORM, 'Uniform distribution'),
    (GAMMA, 'Gamma distribution'),
    (PARETO, 'Pareto distribution'),
    (POISSON, 'Poisson distribution'),
    (CHISQUARE, 'Chisquare distribution'),    
    )
    
    pdf = models.CharField(
        choices = DISTRIBUTION_TYPES,
        verbose_name='Pdf', 
        max_length=250, 
        null=True)
    
    parameter_values = models.CharField(
        verbose_name='Pdf parameter values', 
        max_length=250, 
        null=True)
    
    def get_absolute_url(self):
        return reverse('dpmfa:stochastic-function-inflow-update', args=[self.id]) 
    
class random_choice_inflow(single_period_inflow):
    
    sample = models.CharField(
        verbose_name='Sample', 
        max_length=250, 
        null=True)
    
    def get_absolute_url(self):
        return reverse('dpmfa:random-choice-inflow-update', args=[self.id])


# ==============================================================================
#  Experiments
# ==============================================================================

class experiment(models.Model):
    
    prototype_model = models.ForeignKey(
        to='model',
        related_name='experiments',
        on_delete=models.CASCADE,
        null=True)
    
    model_instance = models.OneToOneField(
        to='model_instance',
        related_name='experiment',
        on_delete=models.CASCADE,
        null=True)

    name = models.CharField(
        verbose_name='Name',
        max_length=250,
        null=True)

    runs = models.IntegerField(
        verbose_name='Runs',
        null=True)

    periods = models.IntegerField(
        verbose_name='Periods',
        null=True)

    evt_created = models.DateTimeField(
        'Date created',
        auto_now_add=True,
        null=True)

    evt_changed = models.DateTimeField(
        verbose_name='Time of last change',
        auto_now=True,
        null=True)

    def __str__(self):
        return str(self.pk)

#==============================================================================
#  Simulation
#==============================================================================

class simulation(models.Model):
    
    model = models.ForeignKey(
        to='model', 
        related_name='simulation', 
        verbose_name='model', 
        null=True)
    
    runs = models.IntegerField(
        verbose_name='Runs', 
        null=True)
    
    periods = models.IntegerField(
        verbose_name='Periods', 
        null=True)
    
    evt_created = models.DateTimeField(
        'Date created', 
        auto_now_add=True, 
        null=True)
    
    results = OneToOneField(
        to='result', 
        related_name='r', 
        verbose_name='model', 
        null=True)
    
    evt_changed = models.DateTimeField(
        verbose_name='Time of last change', 
        auto_now=True, 
        null=True)
    
    def __str__(self):
        return str(self.pk)
    
#==============================================================================
#  Flow Compartment Records
#==============================================================================

class flow_compartment_outflow_record(models.Model):
    
    flow_compartment = models.ForeignKey(
        to='flow_compartment', 
        related_name='flow_compartment_outflow_records', 
        verbose_name='Flow compartment', 
        on_delete=models.CASCADE,
        null=True)
    
    
    run = models.IntegerField(
        verbose_name="Run", 
        null=True)
    
    period = models.IntegerField(
        verbose_name="Period", 
        null=True)
    
    amount = models.FloatField(
        verbose_name="Amount", 
        null=True)
    
    def __str__(self):
        return 'primary key: ' + ' (' + str(self.pk) + ')'

class compartment_inflow_record(models.Model):
    
    compartment = models.ForeignKey(
        to='compartment', 
        related_name='compartment_inflow_records', 
        verbose_name='Compartment',
        on_delete=models.CASCADE, 
        null=True)
    
    
    run = models.IntegerField(
        verbose_name="Run", 
        null=True)
    
    period = models.IntegerField(
        verbose_name="Period", 
        null=True)
    
    amount = models.FloatField(
        verbose_name="Amount", 
        null=True)
    
    def __str__(self):
        return 'primary key: ' + ' (' + str(self.pk) + ')'
    
    
class compartment_inventory_record(models.Model):
    
    compartment = models.ForeignKey(
        to='compartment', 
        related_name='compartment_inventory_records', 
        verbose_name='Compartment',
        on_delete=models.CASCADE, 
        null=True)
    
    
    run = models.IntegerField(
        verbose_name="Run", 
        null=True)
    
    period = models.IntegerField(
        verbose_name="Period", 
        null=True)
    
    amount = models.FloatField(
        verbose_name="Amount", 
        null=True)
    
    def __str__(self):
        return 'primary key: ' + ' (' + str(self.pk) + ')'
    
#==============================================================================
#  Stock Records
#==============================================================================

class stock_immediate_flow_record(models.Model):
    
    stock = models.ForeignKey(
        to='stock', 
        related_name='stock_immediate_flow_records', 
        verbose_name='Stock',
        on_delete=models.CASCADE, 
        null=True)
    
    
    run = models.IntegerField(
        verbose_name="Run", 
        null=True)
    
    period = models.IntegerField(
        verbose_name="Period", 
        null=True)
    
    amount = models.FloatField(
        verbose_name="Amount", 
        null=True)
    
    def __str__(self):
        return 'primary key: ' + ' (' + str(self.pk) + ')'
    
#==============================================================================
# Result
#==============================================================================

class result(models.Model):
    
    model_instance = models.ForeignKey(
        to = 'model_instance',
        related_name = 'results',
        verbose_name = 'Results',
        on_delete = models.CASCADE,
        null = True
        )
    
    experiment = models.OneToOneField(
        to = 'experiment',
        related_name = 'result',
        null = True
        )
    
    FLOW_COMPARTEMENT = 'FLOW_COMPARTMENT'
    SINK = 'SINK'
    STOCK = 'STOCK'

    ENTITY_TYPES = (
    (FLOW_COMPARTEMENT, 'Flow Compartment'),
    (SINK, 'Sink'),
    (STOCK, 'Stock'),
    )
    
    entity_type_of_result = models.CharField(
        choices = ENTITY_TYPES,
        verbose_name = 'Entity type',
        max_length = 250,
        null = True
        )
    
    name_of_entity = models.CharField(
        verbose_name = 'Name',
        max_length = 250,
        null = True
        )
    
    primary_key_of_entity = models.IntegerField(
        verbose_name = 'Primary Key of Entity',
        null = True
        )
    
    file = models.FileField(
        verbose_name = 'File',
        upload_to = 'experiments/%Y/%m/%d/',
        null = True
        )
    
    evt_created = models.DateTimeField(
        verbose_name = 'Date created', 
        auto_now_add = True, 
        null = True)
    
    result = models.CharField(
        verbose_name = 'Result', 
        max_length = 250, 
        null = True)