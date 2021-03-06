from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from dpmfa.models import *
from dpmfa.copiers.ModelCopier import ModelCopier

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        iot_user = User.objects.filter(username='admin')
        
        if len(iot_user) < 1:
            admin = User(username='admin')
            admin.set_password('masterproject')
            admin.is_superuser = True
            admin.is_staff = True
            
            admin.save()
            
#==============================================================================
#  Project
#==============================================================================
        
        # creation of the project
        iot_project = project(
            name = 'IoT project',
            description = 'This is the description of the IoT project. It is great. Very great.')
            
        iot_project.save()
        
#==============================================================================
#  Model
#==============================================================================
        
        # creation of the model
        iot_model = model(
            name = 'IoT Model',
            description = 'This is a very detailed description of the IoT example model. It describes everything. It is awesome.',
            project = iot_project)
        
        iot_model.save()
        
#==============================================================================
#  Flow Compartments
#==============================================================================
        
        # creation of the flow compartments
        first_stage_flow_compartment = flow_compartment(
            model=iot_model, 
            name="First Stage", 
            log_inflows = True, 
            log_outflows = True,
            categories='Category 1,Category 2',
            x=5260,
            y=5120)
        
        first_stage_flow_compartment.save()
        
        second_stage_flow_compartment = flow_compartment(
            model=iot_model, 
            name="Second Stage", 
            log_inflows = True, 
            log_outflows = True,
            x=5260,
            y=5220)
        
        second_stage_flow_compartment.save()
        
        third_stage_flow_compartment = flow_compartment(
            model=iot_model, 
            name="Third Stage", 
            log_inflows = True, 
            log_outflows = True,
            x=5260,
            y=5320)
        
        third_stage_flow_compartment.save()
        
#==============================================================================
#  Releases
#==============================================================================
        
        # release strategy, defining the delay time and the release rates based on material transferred to first stage use compartment
        list_release_for_first_stage_use_compartment = list_release(
            model=iot_model,
            name='LR -> FSUC', 
            delay=0, 
            release_rate_list='0.5, 0.5')
        
        list_release_for_first_stage_use_compartment.save()
        
        # release strategy, defining the delay time and the release rates based on material transferred to second stage use compartment
        function_release_for_first_stage_recycling_compartment = function_release(
            model=iot_model,
            name='FFR -> FSRC', 
            delay=0, 
            release_function='LI',
            function_parameters='-3.7543, 0.67')
        
        function_release_for_first_stage_recycling_compartment.save()

        # release strategy, defining the delay time and the release rates based on material transferred to second stage use compartment
        fixed_rate_release_for_second_stage_use_compartment = fixed_rate_release(
            model=iot_model,
            name='FR -> SSUC', 
            delay=0, 
            release_rate=0.2)
        
        fixed_rate_release_for_second_stage_use_compartment.save()
        
        
        # release strategy, defining the delay time and the release rates based on material transferred to second stage flow compartment
        function_release_for_third_stage_use_compartment = function_release(
            model=iot_model,
            name='FFR -> TSUC', 
            delay = 0,
            release_function='EX',
            function_parameters='4, 4, 4, 4')
        
        function_release_for_third_stage_use_compartment.save()
        
#==============================================================================
#  Stock
#==============================================================================
        
        # creation of the stock
        first_stage_use_compartment = stock(
            model=iot_model, 
            name="First Stage Use",
            log_inflows = True, 
            log_outflows = True,
            local_release = list_release_for_first_stage_use_compartment,
            x=5480,
            y=5040)
        
        first_stage_use_compartment.save()
        
        
        first_stage_recycling_compartment = stock(
            model=iot_model, 
            name="First Stage Recycling", 
            log_inflows = True, 
            log_outflows = True,
            local_release = function_release_for_first_stage_recycling_compartment,
            x=5480,
            y=5140)
        
        first_stage_recycling_compartment.save()
        
        second_stage_use_compartment = stock(
            model=iot_model, 
            name="Second Stage Use", 
            log_inflows = True, 
            log_outflows = True,
            local_release = fixed_rate_release_for_second_stage_use_compartment,
            x=5480,
            y=5240)
        
        second_stage_use_compartment.save()
        
        third_stage_use_compartment = stock(
            model=iot_model, 
            name="Third Stage Use", 
            log_inflows = True,
            log_outflows = True,
            local_release = function_release_for_third_stage_use_compartment,
            x=5480,
            y=5340)
        
        third_stage_use_compartment.save()
        
#==============================================================================
#  Sink
#==============================================================================
        
        # creation of the sinks
        first_stage_disposal_compartment = sink(
            model=iot_model,
            name="First Stage Disposal", 
            log_inflows = True,
            x=5720,
            y=5120)
        
        first_stage_disposal_compartment.save()
        
        second_stage_disposal_compartment = sink(
            model=iot_model,
            name="Second Stage Disposal", 
            log_inflows = True,
            x=5720,
            y=5220)
        
        second_stage_disposal_compartment.save()
        
        third_stage_disposal_compartment = sink(
            model=iot_model,
            name="Third Stage Use", 
            log_inflows = True,
            x=5720,
            y=5320)
        
        third_stage_disposal_compartment.save()
        
        third_stage_export_compartment = sink(
            model=iot_model,
            name="Third Stage Export", 
            log_inflows = True,
            x=5720,
            y=5420)
        
        third_stage_export_compartment.save()
        
        # definition of the functions used in  the model
        
        def expInflowFunction(base, period):
            return base ** period

        def squareInflowfunction(base, period):
            return base * period ** 2

        def  linearReleaseFunction(period):
            return period * 1/5
        
#==============================================================================
#  External Inflows
#==============================================================================
        
        # creation of the external list inflow for AD into fist stage use compartment
        import_of_ad_inflow = external_list_inflow(
            model=iot_model,
            target = first_stage_use_compartment, 
            name = 'Inflow of AD', 
            start_delay = 0, 
            derivation_distribution = 'NORM',
            derivation_parameters = '1000, 250',
            derivation_factor = 1.0,
            x=5040,
            y=5040)
        
        import_of_ad_inflow.save()
        
        # fixed value inflows and random choice inflow representing the inflows of ad (devices) into the first stage use compartment
        fvif_1 = fixed_value_inflow(
            model=iot_model,
            external_list_inflow = import_of_ad_inflow,
            period = 1,
            value = 100)
        
        fvif_1.save()
        
        fvif_2 = fixed_value_inflow(
            model=iot_model,
            external_list_inflow = import_of_ad_inflow,
            period = 2,
            value = 100)
        
        fvif_2.save()
        
        fvif_3 = fixed_value_inflow(
            model=iot_model,
            external_list_inflow = import_of_ad_inflow,
            period = 3,
            value = 100)
        
        fvif_3.save()
        
        fvif_4 = fixed_value_inflow(
            model=iot_model,
            external_list_inflow = import_of_ad_inflow,
            period = 4,
            value = 100)
        
        fvif_4.save()
        
        fvif_5 = fixed_value_inflow(
            model=iot_model,
            external_list_inflow = import_of_ad_inflow,
            period = 5,
            value = 100)
        
        fvif_5.save()
        
        fvif_6 = fixed_value_inflow(
            model=iot_model,
            external_list_inflow = import_of_ad_inflow,
            period = 6,
            value = 100)
        
        fvif_6.save()
        
        rcif_7 = random_choice_inflow(
            model=iot_model,
            external_list_inflow = import_of_ad_inflow,
            period = 7,
            sample = '0, 10, 100, 1000, 1000')
        
        rcif_7.save()
        
        # creation of the external list inflow for SenD into fist stage use compartment
        import_of_send_inflow = external_list_inflow(
            model=iot_model,
            target = first_stage_use_compartment, 
            name = 'Inflow of SenD', 
            start_delay = 0, 
            derivation_distribution = 'NORM',
            derivation_parameters = '1000, 250',
            derivation_factor = 1.0,
            x=5040,
            y=5140)
        
        import_of_send_inflow.save()
        
        # fixed stochastic inflows representing the inflows of StD (devices) into the first stage use compartment
        si_1 = stochastic_function_inflow(
            model=iot_model,
            external_list_inflow = import_of_send_inflow,
            period = 1,
            pdf = 'NORM',
            parameter_values = '1000, 250')
        
        si_1.save()
        
        si_2 = stochastic_function_inflow(
            model=iot_model,
            external_list_inflow = import_of_send_inflow,
            period = 2,
            pdf = 'NORM',
            parameter_values = '1000, 250')
        
        si_2.save()
        
        si_3 = stochastic_function_inflow(
            model=iot_model,
            external_list_inflow = import_of_send_inflow,
            period = 3,
            pdf = 'NORM',
            parameter_values = '1000, 250')
        
        si_3.save()
        
        si_4 = stochastic_function_inflow(
            model=iot_model,
            external_list_inflow = import_of_send_inflow,
            period = 4,
            pdf = 'NORM',
            parameter_values = '1000, 250')
        
        si_4.save()
        
        si_5 = stochastic_function_inflow(
            model=iot_model,
            external_list_inflow = import_of_send_inflow,
            period = 5,
            pdf = 'NORM',
            parameter_values = '1000, 250')
        
        si_5.save()
        
        si_6 = stochastic_function_inflow(
            model=iot_model,
            external_list_inflow = import_of_send_inflow,
            period = 6,
            pdf = 'NORM',
            parameter_values = '1000, 250')
        
        si_6.save()
        
        si_7 = stochastic_function_inflow(
            model=iot_model,
            external_list_inflow = import_of_send_inflow,
            period = 7,
            pdf = 'NORM',
            parameter_values = '1000, 250')
        
        si_7.save()
        
        
        # fixed value inflow
        fvif_for_efi = fixed_value_inflow(
            model=iot_model,
            external_list_inflow = None,
            period = 1,
            value = 100)
        
        fvif_for_efi.save()
        
        
        # creation of the external function inflow of StD (devices) into the first stage use compartment
        import_of_std_inflow = external_function_inflow(
            model=iot_model,
            target=first_stage_use_compartment, 
            name='Inflow of SenD', 
            start_delay=0, 
            derivation_distribution='NORM', 
            derivation_factor=1.0, 
            inflow_function='LI',
            basic_inflow=fvif_for_efi, 
            derivation_parameters='1000, 250',
            function_parameters = '100,200,300',
            x=5040,
            y=5240)
        
        import_of_std_inflow.save()
        
#==============================================================================
#  Transfers
#==============================================================================

        # material transfer from first stage flow compartment to frist stage disposal, first stage recycling and second stage use
        stochastic_transfer_for_first_stage_flow_compartment = stochastic_transfer(
            model=iot_model,
            target = second_stage_use_compartment,
            source_flow_compartment = first_stage_flow_compartment,
            name = 'ST: FSFC -> SSUC', 
            priority = 3, 
            parameters = '1000, 250',
            function='NORM')
        
        stochastic_transfer_for_first_stage_flow_compartment.save()
        
        random_choice_transfer_for_first_stage_flow_compartment = random_choice_transfer(
            model=iot_model,
            target=first_stage_recycling_compartment, 
            source_flow_compartment = first_stage_flow_compartment,
            name='RCT: FSFC -> FSRC',
            priority=2, 
            sample='0.3, 0.4, 0.5')
        
        random_choice_transfer_for_first_stage_flow_compartment.save()
        
        const_transfer_for_first_stage_flow_compartment = constant_transfer(
            model=iot_model,
            target=first_stage_disposal_compartment, 
            source_flow_compartment = first_stage_flow_compartment,
            name='CT: FSFC -> FSDC', 
            priority=1, 
            value=1)
        
        const_transfer_for_first_stage_flow_compartment.save()
        
        # material transfer from second stage flow compartment to second stage disposal and third stage use
        stochastic_transfer_for_second_stage_flow_compartment = stochastic_transfer(
            model=iot_model,
            target=third_stage_use_compartment,
            source_flow_compartment = second_stage_flow_compartment,
            name='ST: SSFC -> TSUC', 
            priority=2, 
            parameters = '1000, 250',
            function='NORM')
        
        stochastic_transfer_for_second_stage_flow_compartment.save()
        
        const_transfer_for_second_stage_flow_compartment = constant_transfer(
            model=iot_model,
            target=second_stage_disposal_compartment,
            source_flow_compartment = second_stage_flow_compartment,
            name='CT: SSFC -> SSDC', 
            priority=1, 
            value=1)
        
        const_transfer_for_second_stage_flow_compartment.save()
        
        # material transfer from third stage flow compartment to third stage disposal and export
        stochastic_transfer_for_third_stage_flow_compartment = stochastic_transfer(
            model=iot_model,
            target=third_stage_export_compartment, 
            source_flow_compartment = third_stage_flow_compartment,
            name='ST: TSFC -> TSEC', 
            priority=2, 
            parameters = '1000, 250',
            function='NORM')
        
        stochastic_transfer_for_third_stage_flow_compartment.save()
        
        const_transfer_for_third_stage_flow_compartment = constant_transfer(
            model=iot_model,
            target=third_stage_disposal_compartment, 
            source_flow_compartment = third_stage_flow_compartment,
            name='CT: TSFC -> TSDC', 
            priority=1, 
            value=1)
        
        const_transfer_for_third_stage_flow_compartment.save()
        
        # total release from First Stage Use Compartment in transferred to First Stage Flow Compartment
        transfer_for_first_stage_use_compartment = constant_transfer(
            model=iot_model,
            target=first_stage_flow_compartment,
            source_flow_compartment = first_stage_use_compartment, 
            name='CT: FSUC -> FSFC', 
            priority=1, 
            value=1)
        
        transfer_for_first_stage_use_compartment.save()
        
        # total release from First Recycling Use Compartment in transferred to First Stage Flow Compartment
        transfer_for_first_stage_use_recycling = constant_transfer(
            model=iot_model,
            target=second_stage_flow_compartment, 
            source_flow_compartment = first_stage_recycling_compartment, 
            name='CT: FSRC -> SSFC', 
            priority=1, 
            value=1)
        
        transfer_for_first_stage_use_recycling.save()
        
        # total release from Second Stage Use Compartment in transferred to Second Stage Flow Compartment
        transfer_for_second_stage_use_compartment = constant_transfer(
            model=iot_model,
            target=second_stage_flow_compartment, 
            source_flow_compartment = second_stage_use_compartment,
            name='CT: SSUC -> SSFC', 
            priority=1, 
            value=1)
        
        transfer_for_second_stage_use_compartment.save()
        
        # total release from Second Stage Use Compartment in transferred to Second Stage Flow Compartment
        transfer_for_third_stage_use_compartment = constant_transfer(
            model=iot_model,
            target=third_stage_flow_compartment, 
            source_flow_compartment = third_stage_use_compartment,
            name='CT: TSUC -> TSFC', 
            priority=1, 
            value=1)
        
        transfer_for_third_stage_use_compartment.save()
        
#==============================================================================
#  Model Instance
#==============================================================================

        iot_model_instance = ModelCopier.copy_model(iot_model)

        iot_model_instance.save()
        
#==============================================================================
#  Experiment
#==============================================================================
        
        iot_experiment = experiment(
            prototype_model=iot_model,
            model_instance = iot_model_instance,
            name='IoT Experiment',
            runs=100,
            periods=50 
            )
        
        iot_experiment.save()
        
#==============================================================================
#  Entities only for test purposes
#==============================================================================  

# Aggregated Transfer

        aggregated_transfer_for_conversion = aggregated_transfer(
            target=None, # because otherwise it will be considered by model converter
            name='Aggregated Transfer for Conversion Test',
            priority=1,
            weights='0.3, 0.4, 0.3'
            )
         
        aggregated_transfer_for_conversion.save()
         
        transfer_for_aggregated_transfer = constant_transfer(
            target=None, # because otherwise it will be considered by model converter
            belongs_to_aggregated_transfer=aggregated_transfer_for_conversion,  
            name='CT', 
            priority=1, 
            value=1)
         
        transfer_for_aggregated_transfer.save()
        
        iot_result = result(
            model_instance=iot_model_instance,
            experiment=iot_experiment,
            )
        
        iot_result.save()
        



        
        

        