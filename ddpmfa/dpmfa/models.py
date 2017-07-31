from django.db import models
from django.db.models.fields import CharField
from django.core.validators import int_list_validator
from django.utils import timezone

class compartment(models.Model):
    name = models.CharField(verbose_name='compartment: ', default='compartment', max_length=250)
    evt_created = models.DateTimeField(verbose_name='time of creation of the compartment', auto_now_add=True)
    compNumber = models.BigIntegerField(verbose_name='number of the compartment')
    logInflows = models.BooleanField(verbose_name='log inflows to this compartment', default=True)
    category = models.CharField(verbose_name='category of the compartment', max_length=250)
    
    def __str__(self):
        return self.name + " " + str(self.pk)
    
class flow_compartment(compartment):
    name_of_flow_compartment = models.CharField('flow compartment', default='flow compartment', max_length=250)
    adjustOutgoingTCs = models.BooleanField(verbose_name='adjust outgoing TCs of this compartment', default=True)
    logOutflows = models.BooleanField(verbose_name='log outflows from this compartment', default=True)
    immediateReleaseRate = models.FloatField(verbose_name='the immediate release rate of this compartment', default=0.0)
    
    def __str__(self):
        return self.name + " " + str(self.pk)
    
class stock(flow_compartment):
    name_of_stock = models.CharField(verbose_name='stock', default='stock', max_length=250)
    
    def __str__(self):
        return self.name_of_stock.verbose_name + self.pk
    
class local_release(models.Model):
    # TODO [rse]: should be FK field
    name = CharField(verbose_name='local release: ', default='local release', max_length=250)
    releaseList = CharField(verbose_name='a list of with a release for each period', validators=[int_list_validator()], max_length=250)
    
    class Meta:
        abstract = True
        
    def __str__(self):
        return self.name.verbose_name + self.pk
    
class fixed_rate_release(local_release):
    delay = models.SmallIntegerField(verbose_name='delay time in periods before release starts')
    releaseRate = models.FloatField(verbose_name='periodic release rate')
    
    
class list_release(local_release):
    delay = models.SmallIntegerField(verbose_name='delay time in periods before release starts')
    # TODO [all]: we will have to implement a float list validator
    releaseRateList = models.CharField(verbose_name='list of release rates of a stored material in future periods', validators=[int_list_validator()], max_length=250)
    
class function_release(local_release):
    delay = models.SmallIntegerField(verbose_name='delay time in periods before release starts')
    # TODO [all]: we will have to implement a function field to store functions
    releaseFunction = models.CharField(verbose_name='probability density function probability distribution function (e.g. from scipy.stats) to sample random values for the transfer coefficient', max_length=250)
    
    
class transfer(models.Model):
    target=models.ForeignKey(to=compartment, on_delete=models.CASCADE)
    
    name = models.CharField(verbose_name='transfer: ', default='transfer', max_length=250)
    priority = models.SmallIntegerField(verbose_name='priority of the transfer')
    currentTC = models.FloatField(verbose_name='current transfer coefficient')   
    
    def __str__(self):
        return self.name.verbose_name + self.pk
    
class constant_transfer(transfer):
    name_of_constant_transfer = models.CharField(verbose_name='constant transfer: ', default='constant transfer', max_length=250)
    value = models.FloatField(verbose_name='deterministic value for the transfer coefficient')
    
    def __str__(self):
        return self.name_of_constant_transfer.verbose_name + self.pk
    
class random_choice_transfer(transfer):
    name_of_random_choice_transfer = models.CharField(verbose_name='random choice transfer: ', default='random choice transfer', max_length=250)
    # TODO [all]: we will have to implement a float list validator 
    sample = models.CharField(verbose_name='a given sample of values from which is randomly drawn', validators=[int_list_validator()], max_length=250)
    
    def __str__(self):
        return self.name_of_random_choice_transfer.verbose_name + self.pk
    
class stochastic_transfer(transfer):
    name_of_stochastic_transfer = models.CharField(verbose_name='stochastic transfer: ', default='stochastic transfer', max_length=250)
    parameters = models.CharField(verbose_name='parameter list of the probability distribution function', validators=[int_list_validator()], max_length=250)
    # TODO [all]: we will have to implement a function field to store functions
    fucntion = models.CharField(verbose_name='probability density function probability distribution function (e.g. from scipy.stats) to sample random values for the transfer coefficient', max_length=250)
    
    def __str__(self):
        return self.name_of_stochastic_transfer.verbose_name + self.pk
    
class aggregated_transfer(transfer):
    singleTransfers = models.ForeignKey(to=transfer, related_name='transfer', verbose_name='a list of SochasticTransfers and/or RandomChoiceTransfers to be considered in the combined distribution', on_delete=models.CASCADE, max_length=250)  
    
    name_of_aggregated_transfer = models.CharField(verbose_name='aggregated transfer: ', default='aggregated transfer', max_length=250)
    # TODO [all]: we will have to implement a float list validator
    weights = models.CharField(verbose_name='a given sample of values from which is randomly drawn', validators=[int_list_validator()], max_length=250)
    
    def __str__(self):
        return self.name_of_aggregated_transfer.verbose_name + self.pk
    
class external_inflow(models.Model):
    target=models.ForeignKey(to=compartment, on_delete=models.CASCADE)
    
    name = models.CharField(verbose_name=' external inflow: ', default='External Inflow', max_length=250)
    startDelay = models.SmallIntegerField(verbose_name='delay time in periods before release starts')
    # TODO [all]: we will have to implement a function field to store functions
    derivationDistribution = models.CharField(verbose_name='probability density function probability distribution function (e.g. from scipy.stats) to sample random values for the transfer coefficient', max_length=250)
    derivationParameters = models.CharField(verbose_name='parameter list of the probability distribution function', validators=[int_list_validator()], max_length=250)
    derivationFactor = models.FloatField(verbose_name='deterministic value for the transfer coefficient')
    
    def __str__(self):
        return self.name.verbose_name + self.pk
        
class external_list_inflow(external_inflow):
    valueList = models.ForeignKey(to='single_period_inflow', verbose_name='name of the single period inflow') 
    
    name_of_external_list_inflow = models.CharField(verbose_name='name of the external list inflow', default='external list inflow', max_length=250)
    
    def __str__(self):
        return self.name_of_external_list_inflow.verbose_name + self.pk
    
class external_function_inflow(external_inflow):
    name_of_external_function_inflow = models.CharField(verbose_name='name of external function inflow', default='external function inflow', max_length=250)
    # TODO [all]: we will have to implement a function field to store functions
    inflowFunction = models.CharField(verbose_name='probability density function probability distribution function (e.g. from scipy.stats) to sample random values for the transfer coefficient', max_length=250)
    basicInflow = models.ForeignKey(to='single_period_inflow', verbose_name='name of the single period inflow')
    
    def __str__(self):
        return self.name_of_external_function_inflow.verbose_name + self.pk
    

class single_period_inflow(external_list_inflow):
    currentValue = models.BigIntegerField(verbose_name='current inflow value')
    
class fixed_value_inflow(single_period_inflow):
    value = models.FloatField(verbose_name='the inflow value')
    
class stochastic_inflow(single_period_inflow):
    name_of_stochastic_inflow = models.CharField(verbose_name='stochastic inflow', default='stochastic inflow', max_length=250)
    
    def __str__(self):
        return self.name.verbose_name + self.pk
    
class random_choice_inflow(single_period_inflow):
    name_of_random_choice_inflow = models.CharField(verbose_name='random choice inflow', default='random choice inflow', max_length=250)
    # TODO [all]: we will have to implement a float list validator
    sample = models.CharField(verbose_name='a given sample of values from which is randomly drawn', validators=[int_list_validator()], max_length=250)
                
    def __str__(self):
        return self.name_of_random_choice_inflow.verbose_name + self.pk
                
class model(models.Model):
    compartment = models.ForeignKey(to=compartment, on_delete=models.CASCADE)
    inflow = models.ForeignKey(to=external_inflow, on_delete=models.CASCADE)
    
    name = models.CharField(verbose_name='name of the model', primary_key=True, max_length=250)
    description = models.TextField(verbose_name='description of this model')
    evt_created = models.DateTimeField('Date created', auto_now_add=True)
    
    def __str__(self):
        return self.name + " " + str(self.evt_created)    