import dpmfa.models as django_models
import dpmfa.functions as fs
import numpy.random as nr
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
                name = self.name, 
                logInflows = self.logInflows, 
                categories = self.categories
                )
                
        except:
            print("Could not convert from DB to dpmfa compartment")
            
    def getDpmfaEntity(self):
        return self.compartment_dpmfa
    
class FlowCompartmentConverter(CompartmentConverter):
    
    def __init__(self, db_flow_compartment=django_models.flow_compartment):
        super(FlowCompartmentConverter, self).__init__(db_flow_compartment)
        
        # set the transfers
        self.transfers = [] 
        for transfer in self.db_entity.outgoing_transfers.all():
            if len(django_models.constant_transfer.objects.filter(pk=self.db_entity.id)) > 0:
                qs_constant_transfer = django_models.constant_transfer.objects.filter(pk=self.db_entity.id)
                db_constant_transfer = qs_constant_transfer[0]
                self.transfers.append(ConstTransferConverter(db_constant_transfer).getDpmfaEntity())
            elif len(django_models.random_choice_transfer.objects.filter(pk=self.db_entity.id)) > 0:
                qs_random_choice_transfer = django_models.random_choice_transfer.objects.filter(pk=self.db_entity.id)
                db_random_choice_transfer = qs_random_choice_transfer[0]
                self.transfers.append(RandomChoiceTransferConverter(db_random_choice_transfer).getDpmfaEntity())
            elif len(django_models.stochastic_transfer.objects.filter(pk=self.db_entity.id)) > 0:
                qs_stochastic_transfer = django_models.stochastic_transfer.objects.filter(pk=self.db_entity.id)
                db_stochastic_transfer = qs_stochastic_transfer[0]
                self.transfers.append(StochasticTransferConverter(db_stochastic_transfer).getDpmfaEntity())
            elif len(django_models.aggregated_transfer.objects.filter(pk=self.db_entity.id)) > 0:
                qs_aggregated_transfer = django_models.aggregated_transfer.objects.filter(pk=self.db_entity.id)
                db_aggregated_transfer = qs_aggregated_transfer[0]
                self.transfers.append(AggregatedTransferConverter(db_aggregated_transfer).getDpmfaEntity())
            else:
                print("Could not retrieve a transfer for flow compartment: %s (%i)" %(db_entity.name, db_entity.id))
 
        self.adjustOutgoingTCs = db_flow_compartment.adjust_outgoing_tcs
        self.logOutflows = db_flow_compartment.log_outflows
        self.immediateReleaseRate = 1
            
        self.flow_compartment_dpmfa = package_components.FlowCompartment(
            name = self.name, 
            transfers = self.transfers, 
            logInflows = self.logInflows, 
            logOutflows = self.logOutflows, 
            adjustOutgoingTCs = self.adjustOutgoingTCs,
            categories = self.categories 
            )
        
    def getDpmfaEntity(self):
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
            
    def getDpmfaEntity(self):
        return self.sink_dpmfa
            
class StockConverter(FlowCompartmentConverter):
    
    def __init__(self, db_stock=django_models.stock):
        super(StockConverter, self).__init__(db_stock)
    
        self.db_local_release = db_stock.local_release
        
        # set the localRelease
        if len(django_models.fixed_rate_release.objects.filter(pk=self.db_local_release.id)) > 0:
            self.qs_fixed_rate_release = django_models.fixed_rate_release.objects.filter(pk=self.db_local_release.id)
            db_fixed_rate_release = self.qs_fixed_rate_release[0]
            self.localRelease = FixedRateReleaseConverter(db_fixed_rate_release).getDpmfaEntity()
        elif len(django_models.list_release.objects.filter(pk=self.db_local_release.id)) > 0:
            self.qs_list_release = django_models.list_release.objects.filter(pk=self.db_local_release.id)
            db_list_release = self.qs_list_release[0]
            self.localRelease = ListReleaseConverter(db_list_release).getDpmfaEntity()
        elif len(django_models.function_release.objects.filter(pk=self.db_local_release.id)) > 0:
            self.qs_function_release = django_models.function_release.objects.filter(pk=self.db_local_release.id)
            db_function_release = self.qs_function_release[0]
            self.localRelease = FunctionReleaseConverter(db_function_release).getDpmfaEntity()
        else:
            print("Could not retrieve a local release for stock: %s (%i)" %(db_stock.name, db_stock.id))
            
        # set the transfers
        self.transfers = [] 
        for transfer in self.db_entity.outgoing_transfers.all():
            if len(django_models.constant_transfer.objects.filter(pk=self.db_entity.id)) > 0:
                qs_constant_transfer = django_models.constant_transfer.objects.filter(pk=self.db_entity.id)
                db_constant_transfer = qs_constant_transfer[0]
                self.transfers.append(ConstTransferConverter(db_constant_transfer).getDpmfaEntity())
            elif len(django_models.random_choice_transfer.objects.filter(pk=self.db_entity.id)) > 0:
                qs_random_choice_transfer = django_models.random_choice_transfer.objects.filter(pk=self.db_entity.id)
                db_random_choice_transfer = qs_random_choice_transfer[0]
                self.transfers.append(RandomChoiceTransferConverter(db_random_choice_transfer).getDpmfaEntity())
            elif len(django_models.stochastic_transfer.objects.filter(pk=self.db_entity.id)) > 0:
                qs_stochastic_transfer = django_models.stochastic_transfer.objects.filter(pk=self.db_entity.id)
                db_stochastic_transfer = qs_stochastic_transfer[0]
                self.transfers.append(StochasticTransferConverter(db_stochastic_transfer).getDpmfaEntity())
            elif len(django_models.aggregated_transfer.objects.filter(pk=self.db_entity.id)) > 0:
                qs_aggregated_transfer = django_models.aggregated_transfer.objects.filter(pk=self.db_entity.id)
                db_aggregated_transfer = qs_aggregated_transfer[0]
                self.transfers.append(AggregatedTransferConverter(db_aggregated_transfer).getDpmfaEntity())
            else:
                print("Could not retrieve a transfer for flow compartment: %s (%i)" %(db_entity.name, db_entity.id))
        
        self.stock_dpmfa = package_components.Stock(
            name = self.name,
            transfers = self.transfers, 
            localRelease = self.localRelease, 
            logInflows = self.logInflows, 
            logOutflows = self.logOutflows,
            logImmediateFlows = True,
            categories = self.categories
            )
        
        
    def getDpmfaEntity(self):
        return self.stock_dpmfa

#==============================================================================
#  Releases
#==============================================================================

# Local Release

class LocalReleaseConverter(object):
    
    def __init__(self, db_local_release=django_models.local_release):
        self.db_entity = db_local_release
            
        # self.stock_of_local_release = db_local_release.stock_of_local_release
        self.name = db_local_release.name
        self.delay = db_local_release.delay
            
        try:
            self.local_release_dpmfa = package_components.LocalRelease()
        
        except:
             print("Could not convert from DB to dpmfa local release")
        
    def getDpmfaEntity(self):
        return self.local_release_dpmfa
    
# Fixed Rate Release

class FixedRateReleaseConverter(LocalReleaseConverter):
    
    def __init__(self, db_fixed_rate_release=django_models.fixed_rate_release):
        super(FixedRateReleaseConverter, self).__init__(db_fixed_rate_release)
        
        self.releaseRate = db_fixed_rate_release.release_rate
        
        try:  
            self.fixed_rate_release_dpmfa = package_components.FixedRateRelease(
                releaseRate = self.releaseRate,
                delay = self.delay
                )
            
        except:
             print("Could not convert from DB to dpmfa fixed rate release")
    
    def getDpmfaEntity(self):
        return self.fixed_rate_release_dpmfa
            
class ListReleaseConverter(LocalReleaseConverter):
    
    def __init__(self, db_list_release=django_models.list_release):
        super(ListReleaseConverter, self).__init__(db_list_release)
        
        self.releaseRatesList = db_list_release.release_rate_list
            
        try:
            self.list_release_dpmfa = package_components.ListRelease(
                releaseRatesList = [],
                delay = self.delay
                )
        
        except:
             print("Could not convert from DB to dpmfa list release")
     
    def getDpmfaEntity(self):
        return self.list_release_dpmfa

class FunctionReleaseConverter(LocalReleaseConverter):
     
     def __init__(self, db_function_release=django_models.function_release):
        super(FunctionReleaseConverter, self).__init__(db_function_release)

        release_function_name = db_function_release.release_function
        function_parameters = [float(x.strip()) for x in db_function_release.function_parameters.split(',')]

        self.releaseFunction = fs.function_by_name(release_function_name, function_parameters)

        try:
            function_parameters = [float(x.strip()) for x in db_function_release.function_parameters.split(',')]
            
            self.function_release_dpmfa = package_components.FunctionRelease(
            releaseFunction = self.releaseFunction,
            delay = self.delay
            )
        
        except:
            print("Could not convert from DB to dpmfa FunctionRelease")
             
             
     def getDpmfaEntity(self):
        return self.function_release_dpmfa

class TransferConverter(object):
    
    def __init__(self, db_transfer=django_models.transfer):
        self.db_entity = db_transfer
        self.belongs_to_aggregated_transfer = db_transfer.belongs_to_aggregated_transfer
        
        self.target = db_transfer.target
        self.priority = db_transfer
        self.currentTC = db_transfer
        
        try:
            self.transfer_dpmfa = package_components.Transfer(
                target = self.target,
                priority = self.priority
                )
            
        except:
            print("Could not convert from DB to dpmfa Transfer")
            
    def getDpmfaEntity(self):
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

    
    def getDpmfaEntity(self):
        return self.const_transfer_dpmfa

class StochasticTransferConverter(TransferConverter):
    
    def __init__(self, db_stochastic_transfer=django_models.stochastic_transfer):
        super(StochasticTransferConverter, self).__init__(db_stochastic_transfer)
        
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
            
    def getDpmfaEntity(self):
        return self.stochastic_transfer_dpmfa
            
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
    
    def getDpmfaEntity(self):
        return self.random_choice_transfer
    
class AggregatedTransferConverter(TransferConverter):
    
    def __init__(self, db_aggregated_transfer=django_models.aggregated_transfer):
        super(AggregatedTransferConverter, self).__init__(db_aggregated_transfer)
        
        # TODO: figure out how to get all relevant aggregate transfers and put them into a list of transfers
        
        self.weights = db_aggregated_transfer.weights
        # TODO[rse]: fix this
        self.singleTransfers = []   
        
        try:
            self.aggregate_transfer_dpmfa = package_components.AggregatedTransfer(
                target = self.target ,
                singleTransfers = self.singleTransfers, 
                weights = self.weights, 
                priority = self.priority
                )
        
        except:
            print("Could not convert from to DB dpmfa AggregatedTransfer")
        
    def getDpmfaEntity(self):
        return self.aggregate_transfer_dpmfa

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
        
    def getDpmfaEntity(self):
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
            
    def getDpmfaEntity(self):
        return self.stochastic_function_inflow_dpmfa
            
class RandomChoiceInflowConverter(SinglePeriodInflowConverter):
    
    def __init__(self, db_random_choice_inflow=django_models.random_choice_inflow):
        super(RandomChoiceInflowConverter, self).__init__(db_random_choice_inflow)
        
        self.sample = db_random_choice_inflow.sample
        
        try:
            self.random_choice_inflow_dpmfa = package_components.RandomChoiceInflow(
                sample = self.sample
                )
            
        except:
            print("Could not convert from DB to dpmfa RandomChoiceInflow")
            
    def getDpmfaEntity(self):
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
            
    def getDpmfaEntity(self):
        return self.fixed_value_inflow_dpmfa

class ExternalInflowConverter(object):
    
    def __init__(self, db_external_inflow=django_models.external_inflow):
        self.db_entity = db_external_inflow
        self.name = db_external_inflow.name
        # Convert the the target to actual dpmfa target
        self.target = []
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
            )
        
        except:
            print("Could not convert from DB to dpmfa ExternalInflow")
            
    def getDpmfaEntity(self):
        return self.external_inflow_dpmfa
            
class ExternalListInflowConverter(ExternalInflowConverter):
    
    def __init__(self, db_external_list_inflow=django_models.external_list_inflow):
        super(ExternalListInflowConverter, self).__init__(db_external_list_inflow)
        
        self.inflowList = []
        for inflow in self.db_entity.single_period_inflows.all():
            if len(django_models.fixed_value_inflow.objects.filter(pk=self.db_entity.id)) > 0:
                qs_fixed_value_inflow = django_models.fixed_value_inflow.objects.filter(pk=self.db_entity.id)
                db_fixed_value_inflow = qs_fixed_value_inflow[0]
                self.inflowList.append(FixedValueInflowConverter(db_fixed_value_inflow))
            elif len(django_models.stochastic_function_inflow.objects.filter(pk=self.db_entity.id)) > 0:
                qs_stochastic_function_inflow = django_models.stochastic_function_inflow.objects.filter(pk=self.db_entity.id)
                db_stochastic_function_inflow = qs_stochastic_function_inflow[0]
                self.inflowList.append(StochasticFunctionInflowConverter(db_stochastic_function_inflow))
            elif len(django_models.random_choice_inflow.objects.filter(pk=self.db_entity.id)) > 0:
                qs_random_choice_inflow = django_models.random_choice_inflow.objects.filter(pk=self.db_entity.id)
                db_random_choice_inflow = qs_stochastic_function_inflow[0]
                self.inflowList.append(RandomChoiceInflowConverter(db_random_choice_inflow))
            else:
                print("Could not retrieve a inflow for single period inflow: %s (%i)" %(db_entity.name, db_entity.id))
        
        
        self.external_list_inflow_dpmfa = package_components.ExternalListInflow(
            target = self.target,
            inflowList = self.inflowList,
            derivationDistribution = self.derivationDistribution, 
            derivationParameters = self.derivationParameters,
            startDelay = self.startDelay
            )
            
    def getDpmfaEntity(self):
        return self.external_inflow_dpmfa
            
class ExternalFunctionInflowConverter(ExternalInflowConverter):
    
    def __init__(self, db_external_function_inflow=django_models.external_function_inflow):
        super(ExternalFunctionInflowConverter, self).__init__(db_external_function_inflow)
    
        self.basicInflow = db_external_function_inflow.basic_inflow
    
        self.derivationParameters = [float(x.strip()) for x in db_external_function_inflow.function_parameters.split(',')]
        
        self.inflow_function = db_external_function_inflow.inflow_function
        
        if self.inflow_function == 'NORM':
            self.inflowFunction = nr.normal
        elif self.inflow_function == 'GEO':
            self.inflowFunction = nr.geometric
        elif self.inflow_function == 'BINOM':
            self.inflowFunction = nr.binomial
        elif self.inflow_function == 'EXPO':
            self.inflowFunction = nr.exponential
        elif self.inflow_function == 'TRI':
            self.inflowFunction = nr.triangular
        elif self.inflow_function == 'UNI':
            self.inflowFunction = nr.uniform
        elif self.inflow_function == 'GAM':
            self.inflowFunction = nr.gamma
        elif self.inflow_function == 'PAR':
            self.inflowFunction = nr.pareto
        elif self.inflow_function == 'POI':
            self.inflowFunction = nr.poisson
        elif self.inflow_function == 'CHI':
            self.inflowFunction = nr.chisquare  
        
        #try:
        self.external_function_inflow_dpmfa = package_components.ExternalFunctionInflow(
            target = self.target,
            basicInflow = self.basicInflow,
            inflowFunction = self.inflowFunction,
            defaultInflowFunction = 0, 
            derivationDistribution = self.derivationDistribution,
            derivationParameters = self.derivationParameters
            )
    
        #except:
        #    print("Could not convert from DB to dpmfa ExternalFunctionInflow")
            
    def getDpmfaEntity(self):
        return self.external_function_inflow_dpmfa

#==============================================================================
#  DPMFA Model Converters
#==============================================================================

class ModelInstanceConverter(object):
    
    def __init__(self, db_model_instance=django_models.model_instance):
        self.db_entity = db_model_instance
        self.name = db_model_instance.name
        self.project = db_model_instance.project
        self.description = db_model_instance.description
        self.seed = db_model_instance.seed
        
        # 1. creation of the model
        self.model_dpmfa = package_model.Model(
            name = self.name,
            )
        
        compartmentsDpmfa = []
        inflowsDpmfa = []
        
        # 2. creation of the flow compartments
        flow_compartments_qs = django_models.flow_compartment.objects.filter(model=db_model_instance.pk)
        for fc in flow_compartments_qs:
            compartmentsDpmfa.append(FlowCompartmentConverter(fc).getDpmfaEntity())
            
        
        # 3. creation of the stocks
        stocksDpmfa = []
        stocks_qs = django_models.stock.objects.filter(model=db_model_instance.pk)
        for stock in stocks_qs:
            compartmentsDpmfa.append(StockConverter(stock).getDpmfaEntity())
            
        # 4. creation of the sinks
        sinksDpmfa = []
        sinks_qs = django_models.sink.objects.filter(model=db_model_instance.pk)
        for sink in sinks_qs:
            sinksDpmfa.append(SinkConverter(sink).getDpmfaEntity())
            
        # 5. creation of the external list inflows
        external_list_inflows_qs = django_models.external_list_inflow.objects.filter(target__model=db_model_instance.pk)
        for external_list_inflow in external_list_inflows_qs:
            inflowsDpmfa.append(ExternalListInflowConverter(external_list_inflow).getDpmfaEntity())
            
        # 6. creation of the external function inflows
        external_function_inflow_qs = django_models.external_function_inflow.objects.filter(target__model=db_model_instance.pk)
        for external_function_inflow in external_function_inflow_qs:
            inflowsDpmfa.append(ExternalFunctionInflowConverter(external_function_inflow).getDpmfaEntity())
            
        self.model_dpmfa.setCompartments(compartmentsDpmfa)
        self.model_dpmfa.setInflows(inflowsDpmfa)
        
        self.model_dpmfa.checkModelValidity()
            
    def getDpmfaEntity(self):
        return self.model_dpmfa

#==============================================================================
#  DPMFA Simulator Converters
#==============================================================================

class SimulatorConverter(object):
    
    def __init__(self, db_experiment=django_models.model_instance):
        self.db_entity = db_experiment
        self.name = db_experiment.name
        self.project = db_experiment.model_instance.project
        self.description = db_experiment.model_instance.description
        self.model_instance = db_experiment.model_instance
        self.runs = db_experiment.runs
        self.periods = db_experiment.periods

        # 1. create the model
        self.model = ModelInstanceConverter(self.model_instance).getDpmfaEntity()
        
        # 2. create the simulator
        self.simulator_dpmfa = package_simulator.Simulator(
            runs = self.runs,
            periods = self.periods,
            )

        # 3. set up the model
        self.simulator_dpmfa.setModel(self.model)
            
    def getDpmfaEntity(self):
        return self.simulator_dpmfa
            
        
        
            
            
        
        
        
        
        
        
 
        
            
        
            
            
        
    
    
    
    
        
        
        
        
        
        
        

            

        
    
        