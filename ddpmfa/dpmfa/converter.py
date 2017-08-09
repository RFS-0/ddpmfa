import dpmfa.models as django_models
from dpmfa.dpmfa_simulator_0_921.dpmfa_simulator import components as package_components
from dpmfa.dpmfa_simulator_0_921.dpmfa_simulator import model as package_model
from dpmfa.dpmfa_simulator_0_921.dpmfa_simulator import simulator as package_simulator

#==============================================================================
#  DPMFA Components Converters
#==============================================================================

class CompartmentConverter(object):
    
    def __init__(self, db_compartment=django_models.compartment):
        self.db_entity = db_compartment
        self.compNumber = db_compartment.pk
        self.name = db_compartment.name
        self.logInflows = db_compartment.log_inflows
        self.categories = db_compartment.categories
            
        try: 
            self.compartment_dpmfa = package_components.Compartment(
                self.name, 
                self.logInflows, 
                self.categories
                )
                
        except:
            print("Could not convert from DB to dpmfa compartment")
            
    def getCompartment(self):
        return self.compartment_dpmfa
    
class FlowCompartmentConverter(CompartmentConverter):
    
    def __init__(self, db_flow_compartment=django_models.flow_compartment):
        super(FlowCompartmentConverter, self).__init__(db_flow_compartment)
        
        # TODO: Transfers be queried and instantiated here      
        self.transfers = []        
        self.adjustOutTCs = db_flow_compartment.adjust_outgoing_tcs
        self.logOutflows = db_flow_compartment.log_outflows
        self.immediateReleaseRate = 1
            
        try:
            self.flow_compartment_dpmfa = package_components.FlowCompartment(
                self.name, 
                self.transfers, 
                self.logInflows, 
                self.logOutflows, 
                self.adjustOutTCs, 
                self.categories
                )
        
        except:
            print("Could not convert from DB to dpmfa flow compartment")
     
        
    def getFlowCompartment(self):
        return self.flow_compartment_dpmfa
    
class SinkConverter(CompartmentConverter):
    
    def __init__(self, db_sink=django_models.sink):
        super(SinkConverter, self).__init__(db_sink)
        
        try:
            self.sink_dpmfa = package_components.Sink(
            name = self.name, 
            logInflows = self.logInflows, 
            categories = self.categories
            )

        except:
            print("Could not convert from DB to dpmfa sink")
            
    def getSink(self):
        return self.sink_dpmfa
            
class StockConverter(FlowCompartmentConverter):
    
    def __init__(self, db_stock=django_models.stock):
        super(FlowCompartmentConverter, self).__init__(db_stock)
        
    # TODO: convert local release here 
    """
        self.db_local_release = db_stock.local_release
        
        self.stock_dpmfa = package_components.Stock(
            name=,
            transfers=[], 
            localRelease = 0, 
            logInflows = False, 
            logOutflows = False, 
            logImmediateFlows = False, 
            categories = []
            )
        
        
        def getStock(self):
            return self.stock_dpmfa
        """

class LocalReleaseConverter(object):
    
    def __init__(self, db_local_release=django_models.local_release):
        self.db_entity = db_local_release
            
        self.stock_of_local_release = db_local_release.stock_of_local_release
        self.name = db_local_release.name
        self.delay = db_local_release.delay
            
        try:
            self.local_release_dpmfa = package_components.LocalRelease()
        
        except:
             print("Could not convert from DB to dpmfa local release")
        
    def getLocalRelease(self):
        return self.local_release_dpmfa
    
class FixedRateReleaseConverter(LocalReleaseConverter):
    
    def __init__(self, db_fixed_rate_release=django_models.fixed_rate_release):
        super(FixedRateRelease, self).__init__(db_fixed_rate_release)
        
        self.releaseRate = db_fixed_rate_release.release_rate
        
        try:  
            self.fixed_rate_release_dpmfa = package_components.FixedRateRelease(
                releaseRate = self.releaseRate,
                delay = self.delay
                )
            
        except:
             print("Could not convert from DB to dpmfa fixed rate release")
             
class ListReleaseConverter(LocalReleaseConverter):
    
    def __init__(self, db_list_release=django_models.list_release):
        super(ListReleaseConverter, self).__init__(db_list_release)
        
        self.releaseRatesList = db_list_release.release_rate_list
            
        try:
            self.list_release_dpmfa = package_components.ListRelease(
                releaseRatesList = self.releaseRatesList,
                delay = self.delay
                )
        
        except:
             print("Could not convert from DB to dpmfa list release")
             
class FunctionReleaseConverter(LocalReleaseConverter):
    
     def __init__(self, db_function_release=django_models.function_release):
        super(ListReleaseConverter, self).__init__(db_function_release)
        
        self.releaseFunction = db_list_release.release_function
        
        try:
            self.function_release_dpmfa = package_components.FunctionRelease(
                releaseFunction = self.releaseFunction,
                delay = self.delay
                )
        
        except:
             print("Could not convert from DB to dpmfa FunctionRelease")
             
class TransferConverter(object):
    
    def __init__(self, db_transfer=django_models.transfer):
        self.db_entity = db_transfer
        self.belongs_to_aggregated_transfer = db_transfer.belongs_to_aggregated_transfer
        
        self.target = db_transfer.target
        self.priority = db_transfer
        self.currentTC = db_transfer
        
        try:
            self.transfer_dpmfa = Transfer(
                target = self.target,
                priority = self.priority
                )
        
        except:
            print("Could not convert from DB to dpmfa Transfer")
            
    def getTransfer(self):
        return self.transfer_dpmfa
    
            
class ConstTransferConverter(TransferConverter):
    
    def __init__(self, db_const_transfer=django_models.constant_transfer):
        super(ConstTransferConverter, self).__init__(db_const_transfer)
        
        self.value = db_const_transfer.value
        
        try:
            self.const_transfer_dpmfa = package_components.ConstTransfer(
                value = self.value,
                target = self.target,
                priority = self.priority
                )
            
        except:
            print("Could not convert from DB to dpmfa ConstTransfer")

    
    def getConstTransferConverter(self):
        return self.const_transfer_dpmfa

class StochasticTransferConverter(TransferConverter):
    
    def __init__(self, db_stochastic_transfer=django_models.stochastic_transfer):
        super(StochasticTransferConverter, self).__init__(stochastic_transfer)
        
        self.function = db_stochastic_transfer.function
        self.parameters = db_stochastic_transfer.parameters
        
        try:
            self.stochastic_transfer_dpmfa = package_components.StochasticTransfer(
                function = self.function,
                parameters = self.parameters,
                target = self.target,
                priority = self.priority
                )
            
        except:
            print("Could not convert from to DB dpmfa StochasticTransfer")
            
class RandomChoiceTransferConverter(TransferConverter):
    
    def __init__(self, db_random_choice_transfer=django_models.random_choice_transfer):
        super(RandomChoiceTransferConverter, self).__init__(db_random_choice_transfer)
        
        self.sample = db_random_choice_transfer.sample
        
        try:
            self.random_choice_transfer = package_components.RandomChoiceTransfer(
                sample = self.sample, 
                target = self.target, 
                priority = self.priority
                )
            
        except:
            print("Could not convert from to DB dpmfa RandomChoiceTransfer")
    
    def getRandomChoiceTransferConverter(self):
        return self.random_choice_transfer
    
class AggregatedTransferConverter(TransferConverter):
    
    def __init__(self, db_aggregated_transfer=django_models.aggregated_transfer):
        super(AggregatedTransferConverter, self).__init__(db_transfer)
        
        # TODO: figure out how to get all relevant aggregate transfers and put them into a list of transfers
        
        self.weights = db_aggregated_transfer.weights
        
        try:
            self.aggregate_transfer_dpmfa = django_models.AggregatedTransfer(
                target = self.target ,
                singleTransfers = self.singleTransfers, 
                weights = self.weights, 
                priority = self.priority
                )
        
        except:
            print("Could not convert from to DB dpmfa AggregatedTransfer")

class SinglePeriodInflowConverter(object):
    
    def __init__(self, db_single_period_inflow=django_models.single_period_inflow):
        self.db_entity = db_single_period_inflow
        
        self.external_list_inflow = db_single_period_inflow.external_list_inflow
        
        self.currentValue = db_single_period_inflow.current_value
        self.period = db_single_period_inflow.period
        
        try:
            self.single_period_inflow_dpmfa = package_components.SinglePeriodInflow()
        
        except:
            print("Could not convert from to DB dpmfa SinglePeriodInflow")
        
    def getSinglePeriodInflowConverter(self):
        return self.single_period_inflow_dpmfa
    
class StochasticFunctionInflowConverter(SinglePeriodInflowConverter):
    
    def __init__(self, db_stochastic_function_inflow=django_models.stochastic_function_inflow):
        super(StochasticFunctionInflowConverter, self).__init__(db_stochastic_function_inflow)
        
        self.probabilityDistribution = db_stochastic_function_inflow.pdf
        self.parameters = db_stochastic_function_inflow.parameter_values
        
        try:
            self.stochastic_function_inflow_dpmfa = package_components.StochasticFunctionInflow(
                probabilityDistribution = self.probabilityDistribution, 
                parameters = self.parameters
                )
        
        except:
            print("Could not convert from DB to dpmfa StochasticFunctionInflow")
            
    def getStochasticFunctionInflowConverter(self):
        return self.stochastic_function_inflow_dpmfa
            
class RandomChoiceInflowConverter(SinglePeriodInflowConverter):
    
    def __init__(self, db_random_choice_inflow=django_models.random_choice_inflow):
        super(StochasticFunctionInflowConverter, self).__init__(db_random_choice_inflow)
        
        self.sample = db_random_choice_inflow.sample
        
        try:
            self.random_choice_inflow_dpmfa = package_components.RandomChoiceInflow(
                sample = self.sample
                )
            
        except:
            print("Could not convert from DB to dpmfa RandomChoiceInflow")
            
    def getRandomChoiceInflowConverter(self):
        return self.random_choice_inflow_dpmfa
            
class FixedValueInflowConverter(SinglePeriodInflowConverter):
    
    def __init__(self, db_fixed_value_inflow=django_models.fixed_value_inflow):
        super(FixedValueInflowConverter, self).__init__(db_fixed_value_inflow)
        
        self.currentValue = db_fixed_value_inflow.value
        
        try:
            self.fixed_value_inflow_dpmfa = package_components.FixedValueInflow(
                value = self.currentValue
                )
            
        except:
            print("Could not convert from DB to dpmfa FixedValueInflow")
            
    def getFixedValueInflowConverter(self):
        return self.fixed_value_inflow_dpmfa

class ExternalInflowConverter(object):
    
    def __init__(self, db_external_inflow=django_models.external_inflow):
        self.db_entity = db_external_inflow
        self.name = db_external_inflow.name
        # Convert the the target to actual dpmfa target
        self.target = db_external_inflow.target
        self.startDelay = db_external_inflow.start_delay
        self.derivationDistribution = db_external_inflow.derivation_distribution
        self.derivationParameters = db_external_inflow.derivation_parameters
        self.derivationFactor = db_external_inflow.derivation_factor
        
        try:
            self.external_inflow_dpmfa = package_components.ExternalInflow(
            target = self.target,
            startDelay = self.startDelay,
            derivationDistribution = self.derivationDistribution,
            derivationParameters = self.derivationParameters,
            derivationFactor = self.derivationFactor
            )
        
        except:
            print("Could not convert from DB to dpmfa ExternalInflow")
            
    def getExternalInflowConverter(self):
        return self.external_inflow_dpmfa
            
class ExternalListInflowConverter(ExternalInflowConverter):
    
    def __init__(self, db_external_list_inflow=django_models.external_list_inflow):
        super(ExternalListInflowConverter, self).__init__(db_external_list_inflow)
        
        try:
            self.external_list_inflow_dpmfa = package_components.ExternalListInflow(
                target = self.target,
                inflowList = self.inflowList,
                derivationDistribution = self.derivationDistribution, 
                derivationParameters = self.derivationParameters,
                startDelay = self.startDelay
                )
            
        except:
            print("Could not convert from DB to dpmfa ExternalListInflow")
            
    def getExternalListInflowConverter(self):
        return self.external_inflow_dpmfa
            
class ExternalFunctionInflowConverter(ExternalInflowConverter):
    
    def __init__(self, db_external_function_inflow=django_models.external_function_inflow):
        super(ExternalFunctionInflowConverter, self).__init__(db_external_function_inflow)
        
        self.inflowFunction = db_external_function_inflow.inflow_function
        self.basicInflow = db_external_function_inflow.basic_inflow
    
        
        try:
            self.external_function_inflow_dpmfa = package_components.ExternalFunctionInflow(
                target = self.target,
                basicInflow = self.basicInflow,
                inflowFunction = self.inflowFunction,
                defaultInflowFunction = 0, 
                derivationDistribution = self.derivationDistribution,
                derivationParameters = self.derivationParameters
                )
        
        except:
            print("Could not convert from DB to dpmfa ExternalFunctionInflow")
            
    def getExternalFunctionInflowConverter(self):
        return self.external_function_inflow_dpmfa

#==============================================================================
#  DPMFA Model Converters
#==============================================================================

# Instantiate the model of the ModelConverter in such a way that it is directly runnable
        
#==============================================================================
#  DPMFA Simulator Converters
#==============================================================================

# Instantiate the simulator of the SimulatorConverter in such a way that it is directly runnable

            
        
        
            
            
        
        
        
        
        
        
 
        
            
        
            
            
        
    
    
    
    
        
        
        
        
        
        
        

            

        
    
        