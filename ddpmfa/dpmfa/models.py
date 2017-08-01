from django.db import models
from django.db.models.fields import CharField
from django.core.validators import int_list_validator
from django.utils import timezone
from .validators.validator import alpha_numeric_list_validator

class model(models.Model):
    project = models.ForeignKey(to='project', related_name='models', verbose_name='project', null=True)
    
    name = models.CharField(verbose_name='Name', primary_key=True, max_length=250)
    description = models.TextField(verbose_name='Description')
    seed = models.FloatField(verbose_name='Seed')
    evt_created = models.DateTimeField('Date created', auto_now_add=True)
    evt_changed = models.DateTimeField(verbose_name='Time of last change', auto_now=True)
    
    def __str__(self):
        return self.name + ' (' + self.pk + ')'

class compartment(models.Model):
    model = models.ForeignKey(to='model', related_name='compartments', null=True, on_delete=models.CASCADE)
    
    name = models.CharField(verbose_name='Compartment', max_length=250)
    description = models.TextField(verbose_name='description of this model')
    evt_created = models.DateTimeField(verbose_name='Time of creation', auto_now_add=True)
    evt_changed = models.DateTimeField(verbose_name='Time of last change', auto_now=True)
    log_inflows = models.BooleanField(verbose_name='Log inflows', default=True)
    categories = models.CharField(verbose_name='Categories', validators=[alpha_numeric_list_validator], max_length=250)
    
    def __str__(self):
        return self.name + ' (' + self.pk + ')'
    
class flow_compartment(compartment):
    adjust_outgoing_tcs = models.BooleanField(verbose_name='Adjust outgoing TCs', default=True)
    log_outflows = models.BooleanField(verbose_name='Log outflows', default=True)
    
    
class local_release(models.Model):
    name = CharField(verbose_name='Local release', default='local release', max_length=250)
    delay = models.SmallIntegerField(verbose_name='Delay', null=True)
       
    def __str__(self):
        return self.name + ' (' + self.pk + ')'

class stock(flow_compartment):
    local_release = models.OneToOneField(local_release, related_name='stock')
    
class fixed_rate_release(local_release):
    release_rate = models.FloatField(verbose_name='Release rate', null=True)
      
class list_release(local_release):
    # TODO [all]: we will have to implement a float list validator
    release_rate_list = models.CharField(verbose_name='Release rate list', validators=[int_list_validator()], max_length=250)
    
class function_release(local_release):
    release_function = models.CharField(verbose_name='Release function', max_length=250)
    
    
class transfer(models.Model):
    target=models.ForeignKey(to='compartment', on_delete=models.CASCADE, related_name='transfers')
    belongs_to_aggregated_transfer = models.ForeignKey(to='aggregated_transfer', related_name='transfers', verbose_name='Aggregated transfer', on_delete=models.CASCADE, max_length=250)  
    
    name = models.CharField(verbose_name='Name', max_length=250)
    priority = models.SmallIntegerField(verbose_name='Priority')
    current_tc = models.FloatField(verbose_name='Current transfer coefficient')
    weight = models.FloatField(verbose_name='Weight')   
    
    def __str__(self):
        return self.name + ' (' + self.pk + ')'
    
class constant_transfer(transfer):
    value = models.FloatField(verbose_name='Value')
    
    def __str__(self):
        return self.name + ' (' + self.pk + ')'
    
class random_choice_transfer(transfer):
    # TODO [all]: we will have to implement a float list validator 
    sample = models.CharField(verbose_name='Sample', validators=[int_list_validator()], max_length=250)
    
    def __str__(self):
        return self.name + ' (' + self.pk + ')'
    
class stochastic_transfer(transfer):
    parameters = models.CharField(verbose_name='Parameters', validators=[int_list_validator()], max_length=250)
    # TODO [all]: we will have to implement a function field to store functions
    function = models.CharField(verbose_name='Function', max_length=250)
    
    def __str__(self):
        return self.name + ' (' + self.pk + ')'
    
class aggregated_transfer(transfer):
        
    def __str__(self):
        return self.name + ' (' + self.pk + ')'
    
class external_inflow(models.Model):
    target = models.ForeignKey(to='compartment', related_name='external_inflows', on_delete=models.CASCADE)
    
    name = models.CharField(verbose_name='Name', max_length=250)
    start_delay = models.SmallIntegerField(verbose_name='Start delay')
    # TODO [all]: we will have to implement a function field to store functions
    derivation_distribution = models.CharField(verbose_name='Probability density function', max_length=250)
    derivation_parameters = models.CharField(verbose_name='Parameter list of the probability distribution function', validators=[int_list_validator()], max_length=250)
    derivation_factor = models.FloatField(verbose_name='Derivation factor')
    
    def __str__(self):
        return self.name + ' (' + self.pk + ')'
        
class external_list_inflow(external_inflow):
    
    def __str__(self):
        return self.name + ' (' + self.pk + ')'
    
class external_function_inflow(external_inflow):
    # TODO [all]: we will have to implement a function field to store functions
    inflow_function = models.CharField(verbose_name='Inflow function', max_length=250)
    basic_inflow = models.ForeignKey(to='single_period_inflow', verbose_name='name of the single period inflow')
    
    def __str__(self):
        return self.name + ' (' + self.pk + ')'
    

class single_period_inflow(models.Model):
    current_value = models.BigIntegerField(verbose_name='current inflow value')
    
    period = models.IntegerField(verbose_name='Period')
    external_list_inflow = models.ForeignKey(to='external_list_inflow', related_name='single_period_inflows', verbose_name='External list inflow', null=True) 
    
class fixed_value_inflow(single_period_inflow):
    value = models.FloatField(verbose_name='the inflow value')
    
class stochastic_inflow(single_period_inflow):
    # TODO [all]: we will have to implement a function field to store functions
    pdf = models.CharField(verbose_name='Pdf', max_length=250)
    parameter_values = models.CharField(verbose_name='Pdf parameter values', max_length=250) 
    
    def __str__(self):
        return self.name + ' (' + self.pk + ')'
    
class random_choice_inflow(single_period_inflow):
    # TODO [all]: we will have to implement a float list validator
    sample = models.CharField(verbose_name='Sample', max_length=250)
                
    def __str__(self):
        return self.name + ' (' + self.pk + ')'


class project(models.Model):
    name = models.CharField(verbose_name='Name', max_length=250)
    description = models.TextField(verbose_name='Description')

class simulation(models.Model):
    model = models.ForeignKey(to='model', related_name='simulation', verbose_name='model')
    
    runs = models.IntegerField(verbose_name='Runs')
    periods = models.IntegerField(verbose_name='Periods')
    evt_created = models.DateTimeField('Date created', auto_now_add=True)
    evt_changed = models.DateTimeField(verbose_name='Time of last change', auto_now=True)

class flow_compartment_outflow_record(models.Model):
    flow_compartment = models.ForeignKey(to='flow_compartment', related_name='flow_compartment_outflow_records', verbose_name='Flow compartment', null=True)
    
    run = models.IntegerField(verbose_name="Run", null=True)
    period = models.IntegerField(verbose_name="Period", null=True)
    amount = models.FloatField(verbose_name="Amount", null=True)

class compartment_inflow_record(models.Model):
    compartment = models.ForeignKey(to='compartment', related_name='compartment_inflow_records', verbose_name='Compartment', null=True)
    
    run = models.IntegerField(verbose_name="Run", null=True)
    period = models.IntegerField(verbose_name="Period", null=True)
    amount = models.FloatField(verbose_name="Amount", null=True)
    
    
class compartment_inventory_record(models.Model):
    compartment = models.ForeignKey(to='compartment', related_name='compartment_inventory_records', verbose_name='Compartment', null=True)
    
    run = models.IntegerField(verbose_name="Run", null=True)
    period = models.IntegerField(verbose_name="Period", null=True)
    amount = models.FloatField(verbose_name="Amount", null=True)


class stock_immediate_flow_record(models.Model):
    stock = models.ForeignKey(to='stock', related_name='stock_immediate_flow_records', verbose_name='Stock', null=True)
    
    run = models.IntegerField(verbose_name="Run", null=True)
    period = models.IntegerField(verbose_name="Period", null=True)
    amount = models.FloatField(verbose_name="Amount", null=True)
