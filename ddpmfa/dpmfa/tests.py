from django.test import TestCase

from dpmfa import models as dpmfa_models
from dpmfa import converter as converters
from dpmfa.management.commands import create_iot_example as example
from dpmfa.dpmfa_simulator_0_921.dpmfa_simulator import components
from dpmfa.dpmfa_simulator_0_921.dpmfa_simulator import model
from dpmfa.dpmfa_simulator_0_921.dpmfa_simulator import simulator



#==============================================================================
#  Compartment
#==============================================================================

class CompartmentConverterTest(TestCase):
        
    def test_compartment_converter(self):
        # entity specific stuff
        db_model = dpmfa_models.compartment
        converter = converters.CompartmentConverter
        dpmfa_class = components.Compartment
        
        # set up db
        command = example.Command()
        command.handle()
        
        # set entities of test
        db_entity = db_model.objects.all()[0]
        converter_class = converter(db_entity)
        dpmfa_instance = converter_class.getDpmfaEntity()
        
        # assertion 
        self.assertIsInstance(dpmfa_instance, dpmfa_class)
        
#==============================================================================
#  Flow Compartment
#==============================================================================
        
class FlowCompartmentConverterTest(TestCase):
    
    def test_flow_compartment_converter(self):
        # entity specific stuff
        db_model = dpmfa_models.flow_compartment
        converter = converters.FlowCompartmentConverter
        dpmfa_class = components.FlowCompartment
        
        # set up db
        command = example.Command()
        command.handle()
        
        # set entities of test
        db_entity = db_model.objects.all()[0]
        converter_class = converter(db_entity)
        dpmfa_instance = converter_class.getDpmfaEntity()
        
        # assertion 
        self.assertIsInstance(dpmfa_instance, dpmfa_class)

#==============================================================================
#  Sink
#==============================================================================
 
class SinkConverterConverterTest(TestCase):
    
    def test_sink_converter(self):
        # entity specific stuff
        db_model = dpmfa_models.sink
        converter = converters.SinkConverter
        dpmfa_class = components.Sink
        
        # set up db
        command = example.Command()
        command.handle()
        
        # set entities of test
        db_entity = db_model.objects.all()[0]
        converter_class = converter(db_entity)
        dpmfa_instance = converter_class.getDpmfaEntity()
        
        # assertion 
        self.assertIsInstance(dpmfa_instance, dpmfa_class)

#==============================================================================
#  Stock
#==============================================================================
 
class StockConverterTest(TestCase):
    
    def test_stock_converter(self):
        # entity specific stuff
        db_model = dpmfa_models.stock
        converter = converters.StockConverter
        dpmfa_class = components.Stock
        
        # set up db
        command = example.Command()
        command.handle()
        
        # set entities of test
        db_entity = db_model.objects.all()[0]
        converter_class = converter(db_entity)
        dpmfa_instance = converter_class.getDpmfaEntity()
        
        # assertion 
        self.assertIsInstance(dpmfa_instance, dpmfa_class)
         
#==============================================================================
#  Releases
#==============================================================================

# Local Release

class LocalReleaseConverterTest(TestCase):
    
    def test_local_release_converter(self):
        # entity specific stuff
        db_model = dpmfa_models.local_release
        converter = converters.LocalReleaseConverter
        dpmfa_class = components.LocalRelease
        
        # set up db
        command = example.Command()
        command.handle()
        
        # set entities of test
        db_entity = db_model.objects.all()[0]
        converter_class = converter(db_entity)
        dpmfa_instance = converter_class.getDpmfaEntity()
        
        # assertion 
        self.assertIsInstance(dpmfa_instance, dpmfa_class)

# Fixed Rate Release

class FixedRateReleaseConverterTest(TestCase):
    
    def test_fixed_release_converter(self):
        # entity specific stuff
        db_model = dpmfa_models.fixed_rate_release
        converter = converters.FixedRateReleaseConverter
        dpmfa_class = components.FixedRateRelease
        
        # set up db
        command = example.Command()
        command.handle()
        
        # set entities of test
        db_entity = db_model.objects.all()[0]
        converter_class = converter(db_entity)
        dpmfa_instance = converter_class.getDpmfaEntity()
        
        # assertion 
        self.assertIsInstance(dpmfa_instance, dpmfa_class)
  
# List Release

class ListReleaseConverterTest(TestCase):
    
    def test_list_release_converter(self):
        # entity specific stuff
        db_model = dpmfa_models.list_release
        converter = converters.ListReleaseConverter
        dpmfa_class = components.ListRelease
        
        # set up db
        command = example.Command()
        command.handle()
        
        # set entities of test
        db_entity = db_model.objects.all()[0]
        converter_class = converter(db_entity)
        dpmfa_instance = converter_class.getDpmfaEntity()
        
        # assertion 
        self.assertIsInstance(dpmfa_instance, dpmfa_class)

# Function Release

class FunctionReleaseConverterTest(TestCase):
    
    def test_function_release_converter(self):
        # entity specific stuff
        db_model = dpmfa_models.function_release
        converter = converters.FunctionReleaseConverter
        dpmfa_class = components.FunctionRelease
        
        # set up db
        command = example.Command()
        command.handle()
        
        # set entities of test
        db_entity = db_model.objects.all()[0]
        converter_class = converter(db_entity)
        dpmfa_instance = converter_class.getDpmfaEntity()
        
        # assertion 
        self.assertIsInstance(dpmfa_instance, dpmfa_class)

#==============================================================================
#  Transfers
#==============================================================================

# Transfer

class TransferConverterTest(TestCase):
    
    def test_transfer_converter(self):
        # entity specific stuff
        db_model = dpmfa_models.transfer
        converter = converters.TransferConverter
        dpmfa_class = components.Transfer
        
        # set up db
        command = example.Command()
        command.handle()
        
        # set entities of test
        db_entity = db_model.objects.all()[0]
        converter_class = converter(db_entity)
        dpmfa_instance = converter_class.getDpmfaEntity()
        
        # assertion 
        self.assertIsInstance(dpmfa_instance, dpmfa_class)

# Constant Transfer

class ConstTransferConverterTest(TestCase):
    
    def test_constant_transfer_converter(self):
        # entity specific stuff
        db_model = dpmfa_models.constant_transfer
        converter = converters.ConstTransferConverter
        dpmfa_class = components.ConstTransfer
        
        # set up db
        command = example.Command()
        command.handle()
        
        # set entities of test
        db_entity = db_model.objects.all()[0]
        converter_class = converter(db_entity)
        dpmfa_instance = converter_class.getDpmfaEntity()
        
        # assertion 
        self.assertIsInstance(dpmfa_instance, dpmfa_class)
        
# Stochastic Transfer

class StochasticTransferConverterTest(TestCase):
    
    def test_stochastic_transfer_converter(self):
        # entity specific stuff
        db_model = dpmfa_models.stochastic_transfer
        converter = converters.StochasticTransferConverter
        dpmfa_class = components.StochasticTransfer
        
        # set up db
        command = example.Command()
        command.handle()
        
        # set entities of test
        db_entity = db_model.objects.all()[0]
        converter_class = converter(db_entity)
        dpmfa_instance = converter_class.getDpmfaEntity()
        
        # assertion 
        self.assertIsInstance(dpmfa_instance, dpmfa_class)
        
# Random Choice Transfer

class RandomChoiceTransferConverterTest(TestCase):
    
    def test_random_choice_transfer_converter(self):
        # entity specific stuff
        db_model = dpmfa_models.random_choice_transfer
        converter = converters.RandomChoiceTransferConverter
        dpmfa_class = components.RandomChoiceTransfer
        
        # set up db
        command = example.Command()
        command.handle()
        
        # set entities of test
        db_entity = db_model.objects.all()[0]
        converter_class = converter(db_entity)
        dpmfa_instance = converter_class.getDpmfaEntity()
        
        # assertion 
        self.assertIsInstance(dpmfa_instance, dpmfa_class)
        
# Aggregated Transfer

class AggregatedTransferConverterTest(TestCase):
    
    def test_aggregated_transfer_converter(self):
        # entity specific stuff
        db_model = dpmfa_models.aggregated_transfer
        converter = converters.AggregatedTransferConverter
        dpmfa_class = components.AggregatedTransfer
        
        # set up db
        command = example.Command()
        command.handle()
        
        # set entities of test
        db_entity = db_model.objects.all()[0]
        converter_class = converter(db_entity)
        dpmfa_instance = converter_class.getDpmfaEntity()
        
        # assertion 
        self.assertIsInstance(dpmfa_instance, dpmfa_class)

#==============================================================================
#  Single Period Inflow                                                                    
#==============================================================================  

# Single Period Inflow

class SinglePeriodInflowConverterTest(TestCase):
    
    def test_single_period_inflow_converter(self):
        # entity specific stuff
        db_model = dpmfa_models.single_period_inflow
        converter = converters.SinglePeriodInflowConverter
        dpmfa_class = components.SinglePeriodInflow
        
        # set up db
        command = example.Command()
        command.handle()
        
        # set entities of test
        db_entity = db_model.objects.all()[0]
        converter_class = converter(db_entity)
        dpmfa_instance = converter_class.getDpmfaEntity()
        
        # assertion 
        self.assertIsInstance(dpmfa_instance, dpmfa_class)
        
# Stochastic Function Inflow

class StochasticFunctionInflowConverterTest(TestCase):
    
    def test_stochastic_function_inflow_converter(self):
        # entity specific stuff
        db_model = dpmfa_models.stochastic_function_inflow
        converter = converters.StochasticFunctionInflowConverter
        dpmfa_class = components.StochasticFunctionInflow
        
        # set up db
        command = example.Command()
        command.handle()
        
        # set entities of test
        db_entity = db_model.objects.all()[0]
        converter_class = converter(db_entity)
        dpmfa_instance = converter_class.getDpmfaEntity()
        
        # assertion 
        self.assertIsInstance(dpmfa_instance, dpmfa_class)
        
# Random Choice Inflow

class RandomChoiceInflowConverterTest(TestCase):
    
    def test_random_choice_inflow_converter(self):
        # entity specific stuff
        db_model = dpmfa_models.random_choice_inflow
        converter = converters.RandomChoiceInflowConverter
        dpmfa_class = components.RandomChoiceInflow
        
        # set up db
        command = example.Command()
        command.handle()
        
        # set entities of test
        db_entity = db_model.objects.all()[0]
        converter_class = converter(db_entity)
        dpmfa_instance = converter_class.getDpmfaEntity()
        
        # assertion 
        self.assertIsInstance(dpmfa_instance, dpmfa_class)
        
# Fixed Value Inflow

class FixedValueInflowConverterTest(TestCase):
    
    def test_fixed_value_inflow_converter(self):
        # entity specific stuff
        db_model = dpmfa_models.fixed_value_inflow
        converter = converters.FixedValueInflowConverter
        dpmfa_class = components.FixedValueInflow
        
        # set up db
        command = example.Command()
        command.handle()
        
        # set entities of test
        db_entity = db_model.objects.all()[0]
        converter_class = converter(db_entity)
        dpmfa_instance = converter_class.getDpmfaEntity()
        
        # assertion 
        self.assertIsInstance(dpmfa_instance, dpmfa_class)

#==============================================================================
#  External Inflow
#==============================================================================

# External Inflow

class ExternalInflowConverterTest(TestCase):
    
    def test_external_inflow_converter(self):
        # entity specific stuff
        db_model = dpmfa_models.external_inflow
        converter = converters.ExternalInflowConverter
        dpmfa_class = components.ExternalInflow
        
        # set up db
        command = example.Command()
        command.handle()
        
        # set entities of test
        db_entity = db_model.objects.all()[0]
        converter_class = converter(db_entity)
        dpmfa_instance = converter_class.getDpmfaEntity()
        
        # assertion 
        self.assertIsInstance(dpmfa_instance, dpmfa_class)
        
# External List Inflow

class ExternalListInflowConverterTest(TestCase):
    
    def test_external_list_inflow_converter(self):
        # entity specific stuff
        db_model = dpmfa_models.external_inflow
        converter = converters.ExternalInflowConverter
        dpmfa_class = components.ExternalInflow
        
        # set up db
        command = example.Command()
        command.handle()
        
        # set entities of test
        db_entity = db_model.objects.all()[0]
        converter_class = converter(db_entity)
        dpmfa_instance = converter_class.getDpmfaEntity()
        
        # assertion 
        self.assertIsInstance(dpmfa_instance, dpmfa_class)
        
# External Function Inflow

class ExternalFunctionInflowConverterTest(TestCase):
    
    def test_external_function_inflow_converter(self):
        # entity specific stuff
        db_model = dpmfa_models.external_function_inflow
        converter = converters.ExternalFunctionInflowConverter
        dpmfa_class = components.ExternalFunctionInflow
        
        # set up db
        command = example.Command()
        command.handle()
        
        # set entities of test
        db_entity = db_model.objects.all()[0]
        converter_class = converter(db_entity)
        dpmfa_instance = converter_class.getDpmfaEntity()
        
        # assertion 
        self.assertIsInstance(dpmfa_instance, dpmfa_class)
        
#==============================================================================
#  Model
#==============================================================================

class ModelConverterTest(TestCase):
    
    def test_model_converter(self):
        # entity specific stuff
        db_model = dpmfa_models.model
        converter = converters.ModelInstanceConverter
        dpmfa_class = model.Model
        
        # set up db
        command = example.Command()
        command.handle()
        
        # set entities of test
        db_entity = db_model.objects.all()[0]
        converter_class = converter(db_entity)
        dpmfa_instance = converter_class.getDpmfaEntity()
        
        # assertion 
        self.assertIsInstance(dpmfa_instance, dpmfa_class)

#==============================================================================
# Experiment
#==============================================================================

class ExperimentConverterTest(TestCase):
    
    def test_experiment_converter(self): 
        # entity specific stuff
        db_model = dpmfa_models.experiment
        converter = converters.ExperimentConverter
        dpmfa_class = simulator.Simulator
        
        # set up db
        command = example.Command()
        command.handle()
        
        # set entities of test
        db_entity = db_model.objects.all()[0]
        converter_class = converter(db_entity)
        dpmfa_instance = converter_class.getDpmfaEntity()
        
        # assertion 
        self.assertIsInstance(dpmfa_instance, dpmfa_class)       