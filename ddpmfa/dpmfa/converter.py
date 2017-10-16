import dpmfa.models as django_models
import dpmfa.functions as fs
import numpy.random as nr
from dpmfa.dpmfa_simulator_0_921.dpmfa_simulator import components as package_components
from dpmfa.dpmfa_simulator_0_921.dpmfa_simulator import model as package_model
from dpmfa.dpmfa_simulator_0_921.dpmfa_simulator import simulator as package_simulator
import django
from django.db.models.sql.constants import SINGLE

# Make sure to always convert the compartments before the transfers

#==============================================================================
#  Package variables
#==============================================================================

compartments_dpmfa = {}
flow_compartments_dpmfa = {}
sinks_dpmfa = {}
stocks_dpmfa = {}
transfers_dpmfa = {}
constant_transfers_dpmfa = {}
stochastic_transfers_dpmfa = {}
random_choice_transfers_dpmfa = {}
aggregated_transfers_dpmfa = {}
local_releases_dpmfa = {}
fixed_rate_releases_dpmfa = {}
list_releases_dpmfa = {}
function_releases_dpmfa = {}
single_period_inflows_dpmfa = {}
stochastic_function_inflows_dpmfa = {}
random_choice_inflows_dpmfa = {}
fixed_value_inflows_dpmfa = {}
external_inflows_dpmfa = {}
external_list_inflows_dpmfa = {}
external_function_inflows_dpmfa = {}

#==============================================================================
#  Package functions
#==============================================================================

# Compartments

def getDpmfaEntityOfCompartment(primaryKey):
    return compartments_dpmfa.get(primaryKey)

def setDpmfaEntityOfCompartment(primaryKey, dpmfaEntity):
    compartments_dpmfa[primaryKey] = dpmfaEntity

def getDpmfaEntityOfFlowCompartment(primaryKey):
    return flow_compartments_dpmfa.get(primaryKey)

def setDpmfaEntityOfFlowCompartment(primaryKey, dpmfaEntity):
    flow_compartments_dpmfa[primaryKey] = dpmfaEntity

def getDpmfaEntityOfSink(primaryKey):
    return sinks_dpmfa.get(primaryKey)

def setDpmfaEntityOfSink(primaryKey, dpmfaEntity):
    sinks_dpmfa[primaryKey] = dpmfaEntity

def getDpmfaEntityOfStock(primaryKey):
    return stocks_dpmfa.get(primaryKey)

def setDpmfaEntityOfStock(primaryKey, dpmfaEntity):
    stocks_dpmfa[primaryKey] = dpmfaEntity

# Transfers

def getDpmfaEntityOfTransfer(primaryKey):
    return transfers_dpmfa.get(primaryKey)

def setDpmfaEntityOfTransfer(primaryKey, dpmfaEntity):
    transfers_dpmfa[primaryKey] = dpmfaEntity
    
def getDpmfaEntityOfConstantTransfer(primaryKey):
    return constant_transfers_dpmfa.get(primaryKey)

def setDpmfaEntityOfConstantTransfer(primaryKey, dpmfaEntity):
    constant_transfers_dpmfa[primaryKey] = dpmfaEntity
    
def getDpmfaEntityOfStochasticTransfer(primaryKey):
    return stochastic_transfers_dpmfa.get(primaryKey)

def setDpmfaEntityOfStochasticTransfer(primaryKey, dpmfaEntity):
    stochastic_transfers_dpmfa[primaryKey] = dpmfaEntity
    
def getDpmfaEntityOfRandomChoiceTransfer(primaryKey):
    return random_choice_transfers_dpmfa.get(primaryKey)

def setDpmfaEntityOfRandomChoiceTransfer(primaryKey, dpmfaEntity):
    random_choice_transfers_dpmfa[primaryKey] = dpmfaEntity
    
def getDpmfaEntityOfAggregatedTransfer(primaryKey):
    return aggregated_transfers_dpmfa.get(primaryKey)

def setDpmfaEntityOfAggregatedTransfer(primaryKey, dpmfaEntity):
    aggregated_transfers_dpmfa[primaryKey] = dpmfaEntity

# Releases

def getDpmfaEntityOfLocalRelease(primaryKey):
    return local_releases_dpmfa.get(primaryKey)

def setDpmfaEntityOfLocalRelease(primaryKey, dpmfaEntity):
    local_releases_dpmfa[primaryKey] = dpmfaEntity

def getDpmfaEntityOfFixedRateRelease(primaryKey):
    return fixed_rate_releases_dpmfa.get(primaryKey)

def setDpmfaEntityOfFixedRateRelease(primaryKey, dpmfaEntity):
    fixed_rate_releases_dpmfa[primaryKey] = dpmfaEntity

def getDpmfaEntityOfListRelease(primaryKey):
    return list_releases_dpmfa.get(primaryKey)

def setDpmfaEntityOfListRelease(primaryKey, dpmfaEntity):
    list_releases_dpmfa[primaryKey] = dpmfaEntity

def getDpmfaEntityOfFunctionRelease(primaryKey):
    return function_releases_dpmfa.get(primaryKey)

def setDpmfaEntityOfFunctionRelease(primaryKey, dpmfaEntity):
    function_releases_dpmfa[primaryKey] = dpmfaEntity

# Single Period Inflows

def getDpmfaEntityOfSinglePeriodInflow(primaryKey):
    return single_period_inflows_dpmfa.get(primaryKey)

def setDpmfaEntityOfSinglePeriodInflow(primaryKey, dpmfaEntity):
    single_period_inflows_dpmfa[primaryKey] = dpmfaEntity

def getDpmfaEntityOfStochasticFunctionInflow(primaryKey):
    return stochastic_function_inflows_dpmfa.get(primaryKey)

def setDpmfaEntityOfStochasticFunctionInflow(primaryKey, dpmfaEntity):
    stochastic_function_inflows_dpmfa[primaryKey] = dpmfaEntity

def getDpmfaEntityOfRandomChoiceInflow(primaryKey):
    return random_choice_inflows_dpmfa.get(primaryKey)

def setDpmfaEntityOfRandomChoiceInflow(primaryKey, dpmfaEntity):
    random_choice_inflows_dpmfa[primaryKey] = dpmfaEntity

def getDpmfaEntityOfFixedValueInflow(primaryKey):
    return fixed_value_inflows_dpmfa.get(primaryKey)

def setDpmfaEntityOfFixedValueInflow(primaryKey, dpmfaEntity):
    fixed_value_inflows_dpmfa[primaryKey] = dpmfaEntity
    
# External Inflows
    
def getDpmfaEntityOfExternalInflow(primaryKey):
    return external_inflows_dpmfa.get(primaryKey)

def setDpmfaEntityOfExternalInflow(primaryKey, dpmfaEntity):
    external_inflows_dpmfa[primaryKey] = dpmfaEntity
    
def getDpmfaEntityOfExternalListInflow(primaryKey):
    return external_list_inflows_dpmfa.get(primaryKey)

def setDpmfaEntityOfExternalListInflow(primaryKey, dpmfaEntity):
    external_list_inflows_dpmfa[primaryKey] = dpmfaEntity
    
def getDpmfaEntityOfExternalFunctionInflow(primaryKey):
    return external_function_inflows_dpmfa.get(primaryKey)

def setDpmfaEntityOfExternalFunctionInflow(primaryKey, dpmfaEntity):
    external_function_inflows_dpmfa[primaryKey] = dpmfaEntity

# Distributions
    
def getDistributionFunction(distribution_type):
    if distribution_type == 'NORM':
        return nr.normal
    elif distribution_type == 'GEO':
        return nr.geometric
    elif distribution_type == 'BINOM':
        return nr.binomial
    elif distribution_type == 'EXPO':
        return nr.exponential
    elif distribution_type == 'TRI':
        return nr.triangular
    elif distribution_type == 'UNI':
        return nr.uniform
    elif distribution_type == 'GAM':
        return nr.gamma
    elif distribution_type == 'PAR':
        return nr.pareto
    elif distribution_type == 'POI':
        return nr.poisson
    elif distribution_type == 'CHI':
        return nr.chisquare
    else:
        return None

#==============================================================================
#  DPMFA Components Converters
#==============================================================================

class CompartmentConverter(object):
    
    def __init__(self, db_compartment=django_models.compartment):
        self.db_entity = db_compartment
        self.compNumber = db_compartment.pk
        self.name = db_compartment.name
        self.logInflows = db_compartment.log_inflows
        
        if db_compartment.categories:
            self.categories = [str(x.strip()) for x in db_compartment.categories.split(',')]
        else:
            # no warning for categories
            self.categories = []
            
        self.compartment_dpmfa = package_components.Compartment(
            name = self.name, 
            logInflows = self.logInflows, 
            categories = self.categories
            )
        
        setDpmfaEntityOfCompartment(db_compartment.pk, self.getCompartmentAsDpmfaEntity())
        
    def getCompartmentAsDpmfaEntity(self):
        return self.compartment_dpmfa
    
class FlowCompartmentConverter(CompartmentConverter):
    
    def __init__(self, db_flow_compartment=django_models.flow_compartment):
        super(FlowCompartmentConverter, self).__init__(db_flow_compartment)
        
        self.transfers = [] 
        self.adjustOutgoingTCs = db_flow_compartment.adjust_outgoing_tcs
        self.logOutflows = db_flow_compartment.log_outflows
            
        self.flow_compartment_dpmfa = package_components.FlowCompartment(
            name = self.name, 
            transfers = self.transfers, 
            logInflows = self.logInflows, 
            logOutflows = self.logOutflows, 
            adjustOutgoingTCs = self.adjustOutgoingTCs,
            categories = self.categories 
            )
        
        setDpmfaEntityOfFlowCompartment(db_flow_compartment.pk, self.getFlowCompartmentAsDpmfaEntity())
        
    def setTransfersOfFlowCompartment(self):
        for transfer in self.db_entity.outgoing_transfers.all():
            if getDpmfaEntityOfConstantTransfer(transfer.pk):
                self.transfers.append(getDpmfaEntityOfConstantTransfer(transfer.pk))
            elif getDpmfaEntityOfRandomChoiceTransfer(transfer.pk):
                self.transfers.append(getDpmfaEntityOfRandomChoiceTransfer(transfer.pk))
            elif getDpmfaEntityOfStochasticTransfer(transfer.pk):
                self.transfers.append(getDpmfaEntityOfStochasticTransfer(transfer.pk))
            elif getDpmfaEntityOfAggregatedTransfer(transfer.pk):
                self.transfers.append(getDpmfaEntityOfAggregatedTransfer(transfer.pk))
            else:
                print("Could not set transfer with name %s to flow compartment with name %s" %(transfer.name, self.db_entity.name))
                print("PK of transfer: " + str(transfer.pk))
            
        self.getFlowCompartmentAsDpmfaEntity().transfers = self.transfers
        
    def getFlowCompartmentAsDpmfaEntity(self):
        return self.flow_compartment_dpmfa
    
class SinkConverter(CompartmentConverter):
    
    def __init__(self, db_sink=django_models.sink):
        super(SinkConverter, self).__init__(db_sink)
        
        self.sink_dpmfa = package_components.Sink(
        name = self.name, 
        logInflows = self.logInflows, 
        categories = self.categories
        )
        
        setDpmfaEntityOfSink(db_sink.pk, self.getSinkAsDpmfaEntity())
            
    def getSinkAsDpmfaEntity(self):
        return self.sink_dpmfa
            
class StockConverter(FlowCompartmentConverter):
    
    def __init__(self, db_stock=django_models.stock):
        super(StockConverter, self).__init__(db_stock)
    
        self.localRelease = None

        self.stock_dpmfa = package_components.Stock(
            name = self.name,
            transfers = self.transfers, 
            localRelease = self.localRelease, 
            logInflows = self.logInflows, 
            logOutflows = self.logOutflows,
            logImmediateFlows = True,
            categories = self.categories
            )
        
        setDpmfaEntityOfStock(db_stock.pk, self.getStockAsDpmfaEntity())
    
    def setTransfersOfStock(self):
        for transfer in self.db_entity.outgoing_transfers.all():
            if getDpmfaEntityOfConstantTransfer(transfer.pk):
                self.transfers.append(getDpmfaEntityOfConstantTransfer(transfer.pk))
            elif getDpmfaEntityOfRandomChoiceTransfer(transfer.pk):
                self.transfers.append(getDpmfaEntityOfRandomChoiceTransfer(transfer.pk))
            elif getDpmfaEntityOfStochasticTransfer(transfer.pk):
                self.transfers.append(getDpmfaEntityOfStochasticTransfer(transfer.pk))
            elif getDpmfaEntityOfAggregatedTransfer(transfer.pk):
                self.transfers.append(getDpmfaEntityOfAggregatedTransfer(transfer.pk))
            else:
                print("Could not set transfer with pk %i for stock %s" %(transfer.pk, self.db_entity.name))
        
        self.getStockAsDpmfaEntity().transfers = self.transfers 
        
    def setLocalReleaseOfStock(self):
        if getDpmfaEntityOfFixedRateRelease(self.db_entity.local_release.pk):
            self.localRelease = getDpmfaEntityOfFixedRateRelease(self.db_entity.local_release.pk)
        elif getDpmfaEntityOfListRelease(self.db_entity.local_release.pk):
            self.localRelease = getDpmfaEntityOfListRelease(self.db_entity.local_release.pk)
        elif getDpmfaEntityOfFunctionRelease(self.db_entity.local_release.pk):
            self.localRelease = getDpmfaEntityOfFunctionRelease(self.db_entity.local_release.pk)
        else:
            print("Could not set local release with pk %i for stock %s" %(self.db_entity.local_release.pk, self.db_entity.name))
        
        self.getStockAsDpmfaEntity().localRelease = self.localRelease
        
    def getStockAsDpmfaEntity(self):
        return self.stock_dpmfa

#==============================================================================
#  Releases
#==============================================================================

# Local Release

class LocalReleaseConverter(object):
    
    def __init__(self, db_local_release=django_models.local_release):
        self.db_entity = db_local_release
            
        self.name = db_local_release.name
        self.delay = db_local_release.delay

        self.local_release_dpmfa = package_components.LocalRelease()
        
        setDpmfaEntityOfLocalRelease(db_local_release.pk, self.getLocalReleaseAsDpmfaEntity())
        
    def getLocalReleaseAsDpmfaEntity(self):
        return self.local_release_dpmfa
    
# Fixed Rate Release

class FixedRateReleaseConverter(LocalReleaseConverter):
    
    def __init__(self, db_fixed_rate_release=django_models.fixed_rate_release):
        super(FixedRateReleaseConverter, self).__init__(db_fixed_rate_release)
        
        self.releaseRate = db_fixed_rate_release.release_rate
        
        self.fixed_rate_release_dpmfa = package_components.FixedRateRelease(
            releaseRate = self.releaseRate,
            delay = self.delay
            )
        
        setDpmfaEntityOfFixedRateRelease(db_fixed_rate_release.pk, self.getFixedRateReleaseAsDpmfaEntity())
    
    def getFixedRateReleaseAsDpmfaEntity(self):
        return self.fixed_rate_release_dpmfa
            
class ListReleaseConverter(LocalReleaseConverter):
    
    def __init__(self, db_list_release=django_models.list_release):
        super(ListReleaseConverter, self).__init__(db_list_release)
        
        self.releaseRatesList = []
        if db_list_release.release_rate_list:
            self.releaseRatesList = [float(x.strip()) for x in db_list_release.release_rate_list.split(',')]
        else:
            print("entity: List Release; Attribute: releaseRateList; Problem: Could not set release rates list; argument: %s" %str(db_list_release.release_rate_list))
            
        self.list_release_dpmfa = package_components.ListRelease(
            releaseRatesList = self.releaseRatesList,
            delay = self.delay
            )
        
        setDpmfaEntityOfListRelease(db_list_release.pk, self.getListReleaseAsDpmfaEntity())
        
    def getListReleaseAsDpmfaEntity(self):
        return self.list_release_dpmfa

class FunctionReleaseConverter(LocalReleaseConverter):
     
     def __init__(self, db_function_release=django_models.function_release):
        super(FunctionReleaseConverter, self).__init__(db_function_release)

        release_function_name = db_function_release.release_function
        
        self.functionParameters = []
        if self.db_entity.function_parameters:
            params = self.db_entity.function_parameters
            self.functionParameters = [float(x.strip()) for x in params.split(',')]
        else:
            print("entity: Function Release; Attribute: functionParameters; Problem: Could not set function parameters; argument: %s" %str(self.db_entity.function_parameters))
        
        self.releaseFunction = fs.function_by_name(release_function_name, self.functionParameters)

        self.function_release_dpmfa = package_components.FunctionRelease(
            delay = self.delay,
            releaseFunction = self.releaseFunction
            )
        
        setDpmfaEntityOfFunctionRelease(db_function_release.pk, self.getFunctionReleaseAsDpmfaEntity())
             
     def getFunctionReleaseAsDpmfaEntity(self):
        return self.function_release_dpmfa
    
#==============================================================================
#  Transfers
#==============================================================================

class TransferConverter(object):
    
    def __init__(self, db_transfer=django_models.transfer):
        self.db_entity = db_transfer
        self.belongs_to_aggregated_transfer = db_transfer.belongs_to_aggregated_transfer
        
        self.target = None
        self.priority = db_transfer.priority
        
        self.transfer_dpmfa = package_components.Transfer(
            target = self.target,
            priority = self.priority
            )
        
        setDpmfaEntityOfTransfer(db_transfer.pk, self.getTransferAsDpmfaEntity())
        
    def getTransferAsDpmfaEntity(self):
        return self.transfer_dpmfa
            
class ConstTransferConverter(TransferConverter):
    
    def __init__(self, db_const_transfer=django_models.constant_transfer):
        super(ConstTransferConverter, self).__init__(db_const_transfer)
        
        self.value = db_const_transfer.value
        
        self.const_transfer_dpmfa = package_components.ConstTransfer(
            target = self.target,
            value = self.value,
            priority = self.priority
            )
        
        setDpmfaEntityOfConstantTransfer(db_const_transfer.pk, self.getConstantTransferAsDpmfaEntity())
        
    def setTargetOfConstantTransfer(self):
        if getDpmfaEntityOfSink(self.db_entity.target.pk):
            self.target = getDpmfaEntityOfSink(self.db_entity.target.pk)
        elif getDpmfaEntityOfStock(self.db_entity.target.pk):
            self.target = getDpmfaEntityOfStock(self.db_entity.target.pk)
        elif getDpmfaEntityOfFlowCompartment(self.db_entity.target.pk):
            self.target = getDpmfaEntityOfFlowCompartment(self.db_entity.target.pk)
        else:
            print("Could not set target with name %s for transfer with pk %i" %(self.db_entity.target.name, self.db_entity.pk))
        
        self.getConstantTransferAsDpmfaEntity().target = self.target
                    
    def getConstantTransferAsDpmfaEntity(self):
        return self.const_transfer_dpmfa

class StochasticTransferConverter(TransferConverter):
    
    def __init__(self, db_stochastic_transfer=django_models.stochastic_transfer):
        super(StochasticTransferConverter, self).__init__(db_stochastic_transfer)
        
        self.function = None
        if db_stochastic_transfer.function and getDistributionFunction(db_stochastic_transfer.function) != None:
            self.function = getDistributionFunction(db_stochastic_transfer.function)
        else:
            print("entity: Stochastic Transfer Converter; Attribute: function; Problem: Could not set function; argument: %s" %str(db_stochastic_transfer.function))
        self.parameters = []
        if db_stochastic_transfer.parameters:
            self.parameters = [float(x.strip()) for x in db_stochastic_transfer.parameters.split(',')]
        else:
            print("entity: Stochastic Transfer Converter; Attribute: parameters; Problem: Could not set parameters; argument: %s" %str(db_stochastic_transfer.parameters))
        
        
        self.stochastic_transfer_dpmfa = package_components.StochasticTransfer(
            target = self.target,
            function = self.function,
            parameters = self.parameters,
            priority = self.priority
            )
        
        setDpmfaEntityOfStochasticTransfer(db_stochastic_transfer.pk, self.getStochasticTransferAsDpmfaEntity())
            
    def setTargetOfStochasticTransfer(self):
        if getDpmfaEntityOfSink(self.db_entity.target.pk):
            self.target = getDpmfaEntityOfSink(self.db_entity.target.pk)
        elif getDpmfaEntityOfStock(self.db_entity.target.pk):
            self.target = getDpmfaEntityOfStock(self.db_entity.target.pk)
        elif getDpmfaEntityOfFlowCompartment(self.db_entity.target.pk):
            self.target = getDpmfaEntityOfFlowCompartment(self.db_entity.target.pk)
        else:
            print("Could not set target with name %s for transfer with pk %i" %(self.db_entity.target.name, self.db_entity.pk))
        
        self.getStochasticTransferAsDpmfaEntity().target = self.target
    
    def getStochasticTransferAsDpmfaEntity(self):
        return self.stochastic_transfer_dpmfa
            
class RandomChoiceTransferConverter(TransferConverter):
    
    def __init__(self, db_random_choice_transfer=django_models.random_choice_transfer):
        super(RandomChoiceTransferConverter, self).__init__(db_random_choice_transfer)
        
        self.sample = []
        if db_random_choice_transfer.sample:
            self.sample = [float(x.strip()) for x in db_random_choice_transfer.sample.split(',')]
        else:
            print("Could not set sample for random choice transfer; argument: %s" %str(db_random_choice_transfer.sample))
    
        self.random_choice_transfer_dpmfa = package_components.RandomChoiceTransfer(
            target = self.target, 
            sample = self.sample, 
            )
        
        setDpmfaEntityOfRandomChoiceTransfer(db_random_choice_transfer.pk, self.getRandomChoiceTransferAsDpmfaEntity())
    
    def setTargetOfRandomChoiceTransfer(self):
        if getDpmfaEntityOfSink(self.db_entity.target.pk):
            self.target = getDpmfaEntityOfSink(self.db_entity.target.pk)
        elif getDpmfaEntityOfStock(self.db_entity.target.pk):
            self.target = getDpmfaEntityOfStock(self.db_entity.target.pk)
        elif getDpmfaEntityOfFlowCompartment(self.db_entity.target.pk):
            self.target = getDpmfaEntityOfFlowCompartment(self.db_entity.target.pk)
        else:
            print("Could not set target with name %s for transfer with pk %i" %(self.db_entity.target.name, self.db_entity.pk))
        
        self.getRandomChoiceTransferAsDpmfaEntity().target = self.target
    
    def getRandomChoiceTransferAsDpmfaEntity(self):
        return self.random_choice_transfer_dpmfa
    
class AggregatedTransferConverter(TransferConverter):
    
    def __init__(self, db_aggregated_transfer=django_models.aggregated_transfer):
        super(AggregatedTransferConverter, self).__init__(db_aggregated_transfer)
        
        self.singleTransfers = None 
        
        self.weights = None
        if db_aggregated_transfer.weights:
            self.weights = [float(x.strip()) for x in db_aggregated_transfer.weights.split(',')]
        else:
            print("entity: Aggregated Transfer Converter; Attribute: weights; Problem: Could not set weights; argument: %s" %str(db_aggregated_transfer.weights))
        
        self.aggregated_transfer_dpmfa = package_components.AggregatedTransfer(
            target = self.target,
            singleTransfers = self.singleTransfers, 
            weights = self.weights, 
            priority = self.priority
            )
        
        setDpmfaEntityOfAggregatedTransfer(db_aggregated_transfer.pk, self.getAggregatedTransferAsDpmfaEntity())
        
    def setSingleTransfersOfAggregatedTransfer(self):
        self.singleTransfers = []
        for singleTransfer in self.db_aggregated_transfer.transfers:
            if getDpmfaEntityOfSink(singleTransfer.pk):
                self.singleTransfers.append(getDpmfaEntityOfSink(singleTransfer.pk))
            elif getDpmfaEntityOfStock(singleTransfer.pk):
                self.singleTransfers.append(getDpmfaEntityOfStock(singleTransfer.pk))
            elif getDpmfaEntityOfFlowCompartment(singleTransfer.pk):
                self.singleTransfers.append(getDpmfaEntityOfFlowCompartment(singleTransfer.pk))
            else:
                print("Could not set target with name %s for transfer with pk %i" %(self.db_entity.target.name, singleTransfer.pk))
            
        self.getAggregatedTransferAsDpmfaEntity().singleTransfers = self.singleTransfers
        
    def getAggregatedTransferAsDpmfaEntity(self):
        return self.aggregated_transfer_dpmfa
    
#==============================================================================
#  Single Period Inflow
#==============================================================================

class SinglePeriodInflowConverter(object):
    
    def __init__(self, db_single_period_inflow=django_models.single_period_inflow):
        self.db_entity = db_single_period_inflow
        
        self.external_list_inflow = None
        self.currentValue = db_single_period_inflow.current_value
        self.period = db_single_period_inflow.period
        
        self.single_period_inflow_dpmfa = package_components.SinglePeriodInflow()
        
        setDpmfaEntityOfSinglePeriodInflow(db_single_period_inflow, self.getSinglePeriodInflowAsDpmfaEntity())
        
    def getSinglePeriodInflowAsDpmfaEntity(self):
        return self.single_period_inflow_dpmfa
    
class StochasticFunctionInflowConverter(SinglePeriodInflowConverter):
    
    def __init__(self, db_stochastic_function_inflow=django_models.stochastic_function_inflow):
        super(StochasticFunctionInflowConverter, self).__init__(db_stochastic_function_inflow)
        
        
        self.probabilityDistribution = None
        if db_stochastic_function_inflow.pdf and getDistributionFunction(db_stochastic_function_inflow.pdf) != None:
            self.probabilityDistribution = getDistributionFunction(db_stochastic_function_inflow.pdf)
        else:
            print("entity: Stochastic Function Inflow; Attribute: probabilityDensityFunction; Problem: Could not set probability density function; argument: %s" %str(db_stochastic_function_inflow.pdf))
        if db_stochastic_function_inflow.parameter_values:
            self.parameters = [float(x.strip()) for x in db_stochastic_function_inflow.parameter_values.split(',')]
        else:
            print("entity: Stochastic Function Inflow; Attribute: parameter values; Problem: Could not set parameter values; argument: %s" %str(db_stochastic_function_inflow.parameter_values))
        
        
        self.stochastic_function_inflow_dpmfa = package_components.StochasticFunctionInflow(
            probabilityDistribution = self.probabilityDistribution, 
            parameters = self.parameters
            )
        
        setDpmfaEntityOfStochasticFunctionInflow(db_stochastic_function_inflow.pk, self.getStochasticFunctionInflowAsDpmfaEntity())

    def getStochasticFunctionInflowAsDpmfaEntity(self):
        return self.stochastic_function_inflow_dpmfa
            
class RandomChoiceInflowConverter(SinglePeriodInflowConverter):
    
    def __init__(self, db_random_choice_inflow=django_models.random_choice_inflow):
        super(RandomChoiceInflowConverter, self).__init__(db_random_choice_inflow)
        
        if db_random_choice_inflow.sample:
            self.sample = [float(x.strip()) for x in db_random_choice_inflow.sample.split(',')]
        else:
            print("entity: Random Choice Inflow; Attribute: sample; Problem: Could not set sample; argument: %s" %str(db_random_choice_inflow.sample))
        
        
        self.random_choice_inflow_dpmfa = package_components.RandomChoiceInflow(
            sample = self.sample
            )
        
        setDpmfaEntityOfRandomChoiceInflow(db_random_choice_inflow.pk, self.getRandomChoiceInflowAsDpmfaEntity())
            
    def getRandomChoiceInflowAsDpmfaEntity(self):
        return self.random_choice_inflow_dpmfa
            
class FixedValueInflowConverter(SinglePeriodInflowConverter):
    
    def __init__(self, db_fixed_value_inflow=django_models.fixed_value_inflow):
        super(FixedValueInflowConverter, self).__init__(db_fixed_value_inflow)
        
        self.currentValue = db_fixed_value_inflow.value
        
        self.fixed_value_inflow_dpmfa = package_components.FixedValueInflow(
            value = self.currentValue
            )
        
        setDpmfaEntityOfFixedValueInflow(db_fixed_value_inflow.pk, self.getFixedValueInflowAsDpmfaEntity())
            
    def getFixedValueInflowAsDpmfaEntity(self):
        return self.fixed_value_inflow_dpmfa
    
#==============================================================================
#  External Inflow
#==============================================================================

class ExternalInflowConverter(object):
    
    def __init__(self, db_external_inflow=django_models.external_inflow):
        self.db_entity = db_external_inflow
        
        self.target = None
        
        self.name = db_external_inflow.name
        self.startDelay = db_external_inflow.start_delay
        if db_external_inflow.derivation_distribution and getDistributionFunction(db_external_inflow.derivation_distribution) != None:
            self.derivationDistribution = getDistributionFunction(db_external_inflow.derivation_distribution)
        else:
            print("entity: External Inflow; Attribute: derivationDistribution; Problem: Could not set derivation distribution; argument: %s" %str(db_external_inflow.derivation_distribution))
        self.derivationParameters = []
        if db_external_inflow.derivation_parameters:
            self.derivationParameters = [float(x.strip()) for x in db_external_inflow.derivation_parameters.split(',')]
        else:
            print("entity: External Inflow; Attribute: derivationParameters; Problem: Could not set derivation parameters; argument: %s" %str(db_external_inflow.derivation_parameters))
        self.derivationFactor = db_external_inflow.derivation_factor
        
        self.external_inflow_dpmfa = package_components.ExternalInflow(
            target = self.target,
            startDelay = self.startDelay,
            derivationDistribution = self.derivationDistribution,
            derivationParameters = self.derivationParameters
            )
        
        setDpmfaEntityOfExternalInflow(db_external_inflow.pk, self.getExternalInflowAsDpmfaEntity())
        
    def getExternalInflowAsDpmfaEntity(self):
        return self.external_inflow_dpmfa

class ExternalListInflowConverter(ExternalInflowConverter):
    
    def __init__(self, db_external_list_inflow=django_models.external_list_inflow):
        super(ExternalListInflowConverter, self).__init__(db_external_list_inflow)
        
        self.inflowList = None        
        
        self.external_list_inflow_dpmfa = package_components.ExternalListInflow(
            target = self.target,
            inflowList = self.inflowList,
            derivationDistribution = self.derivationDistribution, 
            derivationParameters = self.derivationParameters,
            startDelay = self.startDelay
            )
        
        setDpmfaEntityOfExternalListInflow(db_external_list_inflow.pk, self.getExternalListInflowAsDpmfaEntity())
        
    def setTargetOfExternalListInflow(self):
        if getDpmfaEntityOfSink(self.db_entity.target.pk):
            self.target = getDpmfaEntityOfSink(self.db_entity.target.pk)
        elif getDpmfaEntityOfStock(self.db_entity.target.pk):
            self.target = getDpmfaEntityOfStock(self.db_entity.target.pk)
        elif getDpmfaEntityOfFlowCompartment(self.db_entity.target.pk):
            self.target = getDpmfaEntityOfFlowCompartment(self.db_entity.target.pk)
        else:
            print("Could not set target with name %s for external list inflow with pk %i" %(self.db_entity.target.name, self.db_entity.pk))
        
        self.getExternalListInflowAsDpmfaEntity().target = self.target
    
    def setInflowListOfExternalListInflow(self):
        self.inflowList = []
        for singlePeriodInflow in self.db_entity.single_period_inflows.all():
            if getDpmfaEntityOfFixedValueInflow(singlePeriodInflow.pk):
                self.inflowList.append(getDpmfaEntityOfFixedValueInflow(singlePeriodInflow.pk))
            elif getDpmfaEntityOfStochasticFunctionInflow(singlePeriodInflow.pk):
                self.inflowList.append(getDpmfaEntityOfStochasticFunctionInflow(singlePeriodInflow.pk))
            elif getDpmfaEntityOfRandomChoiceInflow(singlePeriodInflow.pk):
                self.inflowList.append(getDpmfaEntityOfRandomChoiceInflow(singlePeriodInflow.pk))
            else:
                print("Could not set single period inflow with pk %i for external list inflow with name %s" %(singlePeriodInflow.pk, self.db_entity.name))
            
        self.getExternalListInflowAsDpmfaEntity().setInflowList(self.inflowList)
            
    def getExternalListInflowAsDpmfaEntity(self):
        return self.external_list_inflow_dpmfa
            
class ExternalFunctionInflowConverter(ExternalInflowConverter):
    
    def __init__(self, db_external_function_inflow=django_models.external_function_inflow):
        super(ExternalFunctionInflowConverter, self).__init__(db_external_function_inflow)
        
        self.basicInflow = db_external_function_inflow.basic_inflow
        self.inflowFunction = getDistributionFunction(db_external_function_inflow.inflow_function)
        
        self.external_function_inflow_dpmfa = package_components.ExternalFunctionInflow(
            target = self.target,
            basicInflow = self.basicInflow,
            inflowFunction = self.inflowFunction,
            defaultInflowFunction = 0, 
            derivationDistribution = self.derivationDistribution,
            derivationParameters = self.derivationParameters
            )
        
        setDpmfaEntityOfExternalFunctionInflow(db_external_function_inflow.pk, self.getExternalFunctionInflowAsDpmfaEntity())
            
    def setTargetOfExternalFunctionInflow(self):
        if getDpmfaEntityOfSink(self.db_entity.target.pk):
            self.target = getDpmfaEntityOfSink(self.db_entity.target.pk)
        elif getDpmfaEntityOfStock(self.db_entity.target.pk):
            self.target = getDpmfaEntityOfStock(self.db_entity.target.pk)
        elif getDpmfaEntityOfFlowCompartment(self.db_entity.target.pk):
            self.target = getDpmfaEntityOfFlowCompartment(self.db_entity.target.pk)
        else:
            print("Could not set target with name %s for external list inflow with pk %i" %(self.db_entity.target.name, self.db_entity.pk))
        
        self.getExternalFunctionInflowAsDpmfaEntity().target = self.target
    
    def setBasicInflowOfExternalFunctionInflow(self):
        pk = self.basicInflow.pk
        if getDpmfaEntityOfFixedValueInflow(pk):
            self.basicInflow = getDpmfaEntityOfFixedValueInflow(pk)
        elif getDpmfaEntityOfStochasticFunctionInflow(pk):
            self.basicInflow = getDpmfaEntityOfStochasticFunctionInflow(pk)
        elif getDpmfaEntityOfRandomChoiceInflow(pk):
            self.basicInflow = getDpmfaEntityOfRandomChoiceInflow(pk)
        else:
            print("Set basic inflow")
            print("Could not set single period inflow with pk %i for external list inflow with name %s" %(pk, self.db_entity.name))
        
        self.getExternalFunctionInflowAsDpmfaEntity().basicInflow = self.basicInflow
    
    def getExternalFunctionInflowAsDpmfaEntity(self):
        return self.external_function_inflow_dpmfa

#==============================================================================
#  DPMFA Model
#==============================================================================

class ModelInstanceConverter(object):
    
    def __init__(self, db_model_instance=django_models.model_instance):
        self.db_entity = db_model_instance
        self.name = db_model_instance.name
        self.project = db_model_instance.project
        self.description = db_model_instance.description
        
        self.flowCompartments = []
        self.stocks = []
        self.sinks = []
        self.externalListInflows = []
        self.externalFunctionInflows = []
        self.singlePeriodInflows = []
        self.transfers = []
        self.constantTransfers = []
        self.randomChoiceTransfers = []
        self.stochasticTransfers = []
        self.aggregatedTransfers = []
        self.localReleases = []
        
        self.compartments = []
        self.inflows = []
        
        #==============================================================================
        # create instances
        #==============================================================================
        
        # model instance
        self.model_instance_dpmfa = package_model.Model(
            name = self.name,
            )
        
        # flow compartments
        self.mapDpmfaFlowCompartmentToConverter = {}
        flow_compartments_qs = django_models.flow_compartment.objects.filter(model=db_model_instance.pk)
        for flowCompartment in flow_compartments_qs:
            fcc = FlowCompartmentConverter(flowCompartment)
            self.flowCompartments.append(fcc)
            self.compartments.append(fcc.getFlowCompartmentAsDpmfaEntity())
            self.mapDpmfaFlowCompartmentToConverter[fcc.getFlowCompartmentAsDpmfaEntity()] = fcc            
        
        # stocks
        self.mapDpmfaStockToConverter = {}
        stocks_qs = django_models.stock.objects.filter(model=db_model_instance.pk)
        for stock in stocks_qs:
            s = StockConverter(stock)
            self.stocks.append(s)
            self.compartments.append(s.getStockAsDpmfaEntity())
            self.mapDpmfaStockToConverter[s.getStockAsDpmfaEntity()] = s
            
            # local release
            if len(django_models.fixed_rate_release.objects.filter(pk=stock.local_release.pk)) > 0:
                db_fixed_rate_release = django_models.fixed_rate_release.objects.get(pk=stock.local_release.pk)
                frr = FixedRateReleaseConverter(db_fixed_rate_release).getFixedRateReleaseAsDpmfaEntity()
                self.localReleases.append(frr)
            elif len(django_models.list_release.objects.filter(pk=stock.local_release.pk)) > 0:
                db_list_release =django_models.list_release.objects.get(pk=stock.local_release.pk)
                lr = ListReleaseConverter(db_list_release).getListReleaseAsDpmfaEntity()
                self.localReleases.append(lr)
            elif len(django_models.function_release.objects.filter(pk=stock.local_release.pk)) > 0:
                db_function_release = django_models.function_release.objects.get(pk=stock.local_release.pk)
                fr = FunctionReleaseConverter(db_function_release).getFunctionReleaseAsDpmfaEntity()
                self.localReleases.append(fr)
            else:
                print("Could not convert local release with pk " + str(localRelease.pk) + "for stock %s" %stock.name)        
        
        # sinks
        self.mapDpmfaSinkToConverter = {}
        sinks_qs = django_models.sink.objects.filter(model=db_model_instance.pk)
        for sink in sinks_qs:
            s = SinkConverter(sink)
            self.sinks.append(s)
            self.compartments.append(s.getSinkAsDpmfaEntity())
            self.mapDpmfaSinkToConverter[s.getSinkAsDpmfaEntity()] = s
            
        # external list inflows
        external_list_inflows_qs = django_models.external_list_inflow.objects.filter(target__model=db_model_instance.pk)
        for externalListInflow in external_list_inflows_qs:
            eli = ExternalListInflowConverter(externalListInflow)
            self.externalListInflows.append(eli)
            self.inflows.append(eli.getExternalListInflowAsDpmfaEntity())
            
            # single period inflows
            qs = externalListInflow.single_period_inflows.get_queryset()
            for singlePeriodInflow in qs:
                if len(django_models.fixed_value_inflow.objects.filter(pk=singlePeriodInflow.pk)) > 0:
                    db_fixed_value_inflow = django_models.fixed_value_inflow.objects.get(pk=singlePeriodInflow.pk)
                    fvi = FixedValueInflowConverter(db_fixed_value_inflow).getFixedValueInflowAsDpmfaEntity()
                    self.singlePeriodInflows.append(fvi)
                elif len(django_models.stochastic_function_inflow.objects.filter(pk=singlePeriodInflow.pk)) > 0:
                    db_stochastic_function_inflow = django_models.stochastic_function_inflow.objects.get(pk=singlePeriodInflow.pk)
                    sfi = StochasticFunctionInflowConverter(db_stochastic_function_inflow).getStochasticFunctionInflowAsDpmfaEntity()
                    self.singlePeriodInflows.append(sfi)
                elif len(django_models.random_choice_inflow.objects.filter(pk=singlePeriodInflow.pk)) > 0:
                    db_random_choice_inflow = django_models.random_choice_inflow.objects.get(pk=singlePeriodInflow.pk)
                    rci = RandomChoiceInflowConverter(db_random_choice_inflow).getRandomChoiceInflowAsDpmfaEntity()
                    self.singlePeriodInflows.append(rci)
                else:
                    print("Could not construct single period inflow for external list inflow %s" %externalListInflow.name)
            
        # external function inflows
        external_function_inflow_qs = django_models.external_function_inflow.objects.filter(target__model=db_model_instance.pk)
        for externalFunctionInflow in external_function_inflow_qs:
            efi = ExternalFunctionInflowConverter(externalFunctionInflow)
            
            self.externalFunctionInflows.append(efi)
            self.inflows.append(efi.getExternalFunctionInflowAsDpmfaEntity())
            
            # single period inflow
            basicInfow = externalFunctionInflow.basic_inflow
            if len(django_models.fixed_value_inflow.objects.filter(pk=basicInfow.pk)) > 0:
                db_fixed_value_inflow = django_models.fixed_value_inflow.objects.get(pk=basicInfow.pk)
                fvi = FixedValueInflowConverter(db_fixed_value_inflow).getFixedValueInflowAsDpmfaEntity()
                self.singlePeriodInflows.append(fvi)
            elif len(django_models.stochastic_function_inflow.objects.filter(pk=basicInfow.pk)) > 0:
                db_stochastic_function_inflow = django_models.stochastic_function_inflow.objects.get(pk=basicInfow.pk)
                sfi = StochasticFunctionInflowConverter(db_stochastic_function_inflow).getStochasticFunctionInflowAsDpmfaEntity()
                self.singlePeriodInflows.append(sfi)
            elif len(django_models.random_choice_inflow.objects.filter(pk=basicInfow.pk)) > 0:
                db_random_choice_inflow = django_models.random_choice_inflow.objects.get(pk=basicInfow.pk)
                rci = RandomChoiceInflowConverter(db_random_choice_inflow).getRandomChoiceInflowAsDpmfaEntity()
                self.singlePeriodInflows.append(rci)
            else:
                print("Could not construct single period inflow for external list inflow %s" %externalListInflow.name)
           
        # transfers
        
        # constant transfers
        for constantTransfer in django_models.constant_transfer.objects.filter(target__model=db_model_instance.pk):
            ct = ConstTransferConverter(constantTransfer)
            self.constantTransfers.append(ct)
            self.transfers.append(ct.getConstantTransferAsDpmfaEntity())
        
        # random choice transfers
        for randomChoiceTransfer in django_models.random_choice_transfer.objects.filter(target__model=db_model_instance.pk):
            rct = RandomChoiceTransferConverter(randomChoiceTransfer)
            self.randomChoiceTransfers.append(rct)
            self.transfers.append(rct.getRandomChoiceTransferAsDpmfaEntity())
        
        # stochastic transfers
        for stochasticTransfer in django_models.stochastic_transfer.objects.filter(target__model=db_model_instance.pk):
            st = StochasticTransferConverter(stochasticTransfer)
            self.stochasticTransfers.append(st)
            self.transfers.append(st.getStochasticTransferAsDpmfaEntity())
            
        # aggregated transfers
#         for aggregatedTransfer in django_models.aggregated_transfer.objects.filter(target__model=db_model_instance.pk):
#             at = AggregatedTransferConverter(aggregatedTransfer)
#             self.aggregatedTransfers.append(at)
#             self.transfers.append(at.getAggregatedTransferAsDpmfaEntity())
        
        #==============================================================================  
        # set up all the relationships and references
        #==============================================================================
        
        # flow compartments
        for flowCompartment in self.flowCompartments:
            flowCompartment.setTransfersOfFlowCompartment()
            
        
        # stocks
        for stock in self.stocks:
            stock.setTransfersOfStock()
            stock.setLocalReleaseOfStock()
            
        # sinks
        # no relations needed
        
        # external list inflows
        for externalListInflow in self.externalListInflows:
            externalListInflow.setTargetOfExternalListInflow()
            externalListInflow.setInflowListOfExternalListInflow()
        
        # external function inflows
        for externalFunctionInflow in self.externalFunctionInflows:
            externalFunctionInflow.setTargetOfExternalFunctionInflow()
            externalFunctionInflow.setBasicInflowOfExternalFunctionInflow()
            
        # transfers
        
        # constant transfers
        for constTransfer in self.constantTransfers:
            constTransfer.setTargetOfConstantTransfer()
        
        # random choice transfers
        for randomChoiceTransfer in self.randomChoiceTransfers:
            randomChoiceTransfer.setTargetOfRandomChoiceTransfer()
        
        # stochastic transfer
        for stochasticTransfer in self.stochasticTransfers:
            stochasticTransfer.setTargetOfStochasticTransfer()
        
        # aggregated transfers
        for aggregateTransfer in self.aggregatedTransfers:
            print(str(aggregatedTransfer))
            aggregatedTransfer.setSingleTransfersOfAggregatedTransfer()
            
        #==============================================================================  
        # set up model
        #==============================================================================
               
        self.getModelInstanceAsDpmfaEntity().setCompartments(self.compartments)
        self.getModelInstanceAsDpmfaEntity().setInflows(self.inflows)
        
    def getModelInstanceAsDpmfaEntity(self):
        return self.model_instance_dpmfa
    
    def getAllCompartmentConvertersOfModel(self):
        return self.allCompartmentConvertersOfModel
    
    def getFlowCompartmentMap(self):
        return self.mapDpmfaFlowCompartmentToConverter
    
    def getStockMap(self):
        return self.mapDpmfaStockToConverter
    
    def getSinkMap(self):
        return self.mapDpmfaSinkToConverter
        

#==============================================================================
#  DPMFA Simulator
#==============================================================================

class ExperimentConverter(object):
    
    def __init__(self, db_experiment=django_models.experiment):
        self.db_entity = db_experiment
        self.name = db_experiment.name
        self.project = db_experiment.model_instance.project
        self.description = db_experiment.model_instance.description
        self.model_instance = db_experiment.model_instance
        self.runs = db_experiment.runs
        self.periods = db_experiment.periods

        self.model_instance_converter = ModelInstanceConverter(self.model_instance)
        
        self.simulator_dpmfa = package_simulator.Simulator(
            runs = self.runs,
            periods = self.periods,
            )

        self.getSimulatorAsDpmfaEntity().setModel(self.getModelInstanceConverter().getModelInstanceAsDpmfaEntity())
            
    def getSimulatorAsDpmfaEntity(self):
        return self.simulator_dpmfa
    
    def getModelInstanceConverter(self):
        return self.model_instance_converter
