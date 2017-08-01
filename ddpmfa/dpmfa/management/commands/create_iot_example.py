from django.core.management.base import BaseCommand, CommandError
from dpmfa.models import *

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        iot_project = project.objects.filter(name='IoT project')
        
        if len(iot_project) >= 1:
            self.stdout.write("The IoT project already exists\n", ending='')
            self.stdout.write("Exiting without any changes to db\n", ending='')
            self.stdout.write("Bye", ending='')
            return
        
        # creation of the project
        iot_project = project(
            name = 'IoT project',
            description = 'This is the description of the IoT project. It is great. Very great.')
        
        # creation of the model
        iot_model = model(
            name = 'IoT Model',
            description = 'This is a very detailed description of the IoT example model. It describes everything. It is awesome.',
            seed = 1,
            project = iot_project)
        
        # creation of the flow compartments
        first_stage_flow_compartment = flow_compartment(
            model=iot_model, 
            name="First Stage Flow Compartment", 
            log_inflows = True, 
            log_outflows = True)
        
        second_stage_flow_compartment = flow_compartment(
            model=iot_model, 
            name="Second Stage Flow Compartment", 
            log_inflows = True, 
            log_outflows = True)
        
        third_stage_flow_compartment = flow_compartment(
            model=iot_model, 
            name="Third Stage Flow Compartment", 
            log_inflows = True, 
            log_outflows = True)
        
        # release strategy, defining the delay time and the release rates based on material transferred to first stage use compartment
        list_release_for_first_stage_use_compartment = list_release(
            name='List release for first stage use compartment', 
            delay=0, 
            release_rate_list='[0.5, 0.5]')
        

        
        # release strategy, defining the delay time and the release rates based on material transferred to second stage use compartment
        function_release_for_first_stage_recycling_compartment = function_release(
            name='Fucntion release for first stage use compartment', 
            delay=0, 
            release_function='Some function')
        
        # release strategy, defining the delay time and the release rates based on material transferred to second stage use compartment
        function_release_for_second_stage_use_compartment = fixed_rate_release(
            name='Fixed rate release for first stage use compartment', 
            delay=0, 
            release_rate=0.2)
        
        
        
        # release strategy, defining the delay time and the release rates based on material transferred to second stage flow compartment
        function_release_for_third_stage_use_compartment = function_release(
            name='Function release for second state flow compartment', 
            delay = 0,
            release_function='Some function')
        
        
        
        # creation of the stock
        first_stage_use_compartment = stock(
            model=iot_model, 
            name="First Stage Use",
            log_inflows = True, 
            log_outflows = True,
            local_release = list_release_for_first_stage_use_compartment)
        
        first_stage_recycling_compartment = stock(
            model=iot_model, 
            name="First Stage Recycling", 
            log_inflows = True, 
            log_outflows = True,
            local_release = function_release_for_first_stage_recycling_compartment)
        
        second_stage_use_compartment = stock(
            model=iot_model, 
            name="Second Stage Use", 
            log_inflows = True, 
            log_outflows = True,
            local_release = function_release_for_second_stage_use_compartment)
        
        third_stage_use_compartment = stock(
            model=iot_model, 
            name="Third Stage Use", 
            log_inflows = True,
            local_release = function_release_for_third_stage_use_compartment)
        
        # creation of the sinks
        first_stage_disposal_compartment = sink(
            model=iot_model,
            name="First Stage Disposal", 
            log_inflows = True)
        
        second_stage_disposal_compartment = sink(
            model=iot_model,
            name="Second Stage Disposal", 
            log_inflows = True)
        
        third_stage_disposal_compartment = sink(
            model=iot_model,
            name="Third Stage Use", 
            log_inflows = True)
        
        third_stage_export_compartment = sink(
            model=iot_model,
            name="Third Stage Use", 
            log_inflows = True)
        
        # definition of the fucntions used in  the model
        
        def expInflowFunction(base, period):
            return base ** period

        def squareInflowfunction(base, period):
            return base * period ** 2

        def  linearReleaseFunction(period):
            return period * 1/5
        
        # creation of the external list inflow for AD into fist stage use compartment
        import_of_ad_inflow = external_list_inflow(
            target = first_stage_use_compartment, 
            name = 'External list inflow of AD to first stage use compartment', 
            start_delay = 0, 
            derivation_distribution = 'Some Pdf', 
            derivation_factor = 1.0)
        
        # fixed value inflows and random choice inflow representing the inflows of ad (devices) into the first stage use compartment
        fvif_1 = fixed_value_inflow(
            external_list_inflow = import_of_ad_inflow,
            current_value = 0,
            period = 1,
            value = 100)
        
        fvif_2 = fixed_value_inflow(
            external_list_inflow = import_of_ad_inflow,
            current_value = 0,
            period = 2,
            value = 100)
        
        fvif_3 = fixed_value_inflow(
            external_list_inflow = import_of_ad_inflow,
            current_value = 0,
            period = 3,
            value = 100)
        
        fvif_4 = fixed_value_inflow(
            external_list_inflow = import_of_ad_inflow,
            current_value = 0,
            period = 4,
            value = 100)
        
        fvif_5 = fixed_value_inflow(
            external_list_inflow = import_of_ad_inflow,
            current_value = 0,
            period = 5,
            value = 100)
        
        fvif_6 = fixed_value_inflow(
            external_list_inflow = import_of_ad_inflow,
            current_value = 0,
            period = 6,
            value = 100)
        
        rcif_7 = random_choice_inflow(
            external_list_inflow = import_of_ad_inflow,
            current_value = 0,
            period = 7,
            sample = '[0, 10, 100, 1000, 1000]')
        
        # creation of the external list inflow for SenD into fist stage use compartment
        import_of_send_inflow = external_list_inflow(
            target = first_stage_use_compartment, 
            name = 'External list inflow of SenD to first stage use compartment', 
            start_delay = 0, 
            derivation_distribution = 'Some Pdf', 
            derivation_factor = 1.0)
        
        
        # fixed stochastic inflows representing the inflows of StD (devices) into the first stage use compartment
        si_1 = stochastic_inflow(
            external_list_inflow = import_of_send_inflow,
            current_value = 0,
            period = 1,
            pdf = 'Some Pdf',
            parameter_values = '[1000, 250]')
        
        si_2 = stochastic_inflow(
            external_list_inflow = import_of_send_inflow,
            current_value = 0,
            period = 2,
            pdf = 'Some Pdf',
            parameter_values = '[1000, 250]')
        
        si_3 = stochastic_inflow(
            external_list_inflow = import_of_send_inflow,
            current_value = 0,
            period = 3,
            pdf = 'Some Pdf',
            parameter_values = '[1000, 250]')
        
        si_4 = stochastic_inflow(
            external_list_inflow = import_of_send_inflow,
            current_value = 0,
            period = 4,
            pdf = 'Some Pdf',
            parameter_values = '[1000, 250]')
        si_5 = stochastic_inflow(
            external_list_inflow = import_of_send_inflow,
            current_value = 0,
            period = 5,
            pdf = 'Some Pdf',
            parameter_values = '[1000, 250]')
        
        si_6 = stochastic_inflow(
            external_list_inflow = import_of_send_inflow,
            current_value = 0,
            period = 6,
            pdf = 'Some Pdf',
            parameter_values = '[1000, 250]')
        
        si_7 = stochastic_inflow(
            external_list_inflow = import_of_send_inflow,
            current_value = 0,
            period = 7,
            pdf = 'Some Pdf',
            parameter_values = '[1000, 250]')
        
        
        # fixed value inflow
        fvif_for_efi = fixed_value_inflow(
            external_list_inflow = import_of_ad_inflow,
            current_value = 0,
            period = 1,
            value = 100)
        
        
        # creation of the external function inflow of StD (devices) into the first stage use compartment
        import_of_std_inflow = external_function_inflow(
            target=first_stage_use_compartment, 
            name='External list inflow of SenD to first stage use compartment', 
            start_delay=0, derivation_distribution='Some Pdf', 
            derivation_factor=1.0, 
            inflow_function='Some inflow function', 
            basic_inflow=fvif_for_efi, 
            derivation_parameters='[1000, 250]')

        # material transfer from first stage flow compartment to frist stage disposal, first stage recycling and second stage use
        stochastic_transfer_for_first_stage_flow_compartment = stochastic_transfer(
            target=second_stage_use_compartment, 
            name='Stochastic transfer from first stage flow compartment to second stage use compartment', 
            priority=3, 
            current_tc=0, 
            weight=0, 
            parameters='[0.5, 0.7, 0.9]')
        
        random_choice_transfer_for_first_stage_flow_compartment = random_choice_transfer(
            target=first_stage_recycling_compartment, 
            name='Random choice transfer from first stage flow compartment to first stage recycling compartment',
            priority=2, 
            current_tc=0, 
            weight=0, 
            sample='[0.3, 0.4, 0.5]')
        
        
        
        const_transfer_for_first_stage_flow_compartment = constant_transfer(
            target=second_stage_use_compartment, 
            name='Stochastic transfer from first stage flow compartment to first stage disposal compartment', 
            priority=1, 
            current_tc=0, 
            weight=0, 
            value=1)
        
        # material transfer from second stage flow compartment to second stage disposal and third stage use
        stochastic_transfer_for_second_stage_flow_compartment = stochastic_transfer(
            target=third_stage_use_compartment, 
            name='Stochastic transfer from second stage flow compartment to third stage use compartment', 
            priority=2, 
            current_tc=0, 
            weight=0, 
            parameters='[0.5, 0.7, 0.9]')
        
        const_transfer_for_second_stage_flow_compartment = constant_transfer(
            target=second_stage_disposal_compartment, 
            name='Stochastic transfer from first stage flow compartment to first stage disposal compartment', 
            priority=1, 
            current_tc=0, 
            weight=0, 
            value=1)
        
        
        
        # material transfer from third stage flow compartment to third stage disposal and export
        stochastic_transfer_for_third_stage_flow_compartment = stochastic_transfer(
            target=third_stage_export_compartment, 
            name='Stochastic transfer from third stage flow compartment to third export compartment', 
            priority=2, 
            current_tc=0, 
            weight=0, 
            parameters='[0.5, 0.7, 0.9]')
        
        const_transfer_for_third_stage_flow_compartment = constant_transfer(
            target=third_stage_disposal_compartment, 
            name='Stochastic transfer from third stage flow compartment to third stage disposal compartment', 
            priority=1, 
            current_tc=0, 
            weight=0, 
            value=1)
        
        # total release from First Stage Use Compartment in transferred to First Stage Flow Compartment
        transfer_for_first_stage_use_compartment = constant_transfer(
            target=first_stage_flow_compartment, 
            name='Stochastic transfer from first stage flow compartment to first stage disposal compartment', 
            priority=1, 
            current_tc=0, 
            weight=0, 
            value=1)
        
        # total release from First Recycling Use Compartment in transferred to First Stage Flow Compartment
        transfer_for_first_stage_use_recycling = constant_transfer(
            target=second_stage_flow_compartment, 
            name='Stochastic transfer from first stage flow compartment to first stage disposal compartment', 
            priority=1, 
            current_tc=0, 
            weight=0, 
            value=1)
        
        # total release from Second Stage Use Compartment in transferred to Second Stage Flow Compartment
        transfer_for_second_stage_use_compartment = constant_transfer(
            target=second_stage_flow_compartment, 
            name='Stochastic transfer from first stage flow compartment to first stage disposal compartment', 
            priority=1, 
            current_tc=0, 
            weight=0, 
            value=1)
        
        # total release from Second Stage Use Compartment in transferred to Second Stage Flow Compartment
        transfer_for_first_third_use_compartment = constant_transfer(
            target=third_stage_flow_compartment, 
            name='Stochastic transfer from first stage flow compartment to first stage disposal compartment', 
            priority=1, 
            current_tc=0, 
            weight=0, 
            value=1)
        
        
        
        # save all the entities
        iot_project.save()
        iot_model.save()
        first_stage_flow_compartment.save()
        second_stage_flow_compartment.save()
        third_stage_flow_compartment.save()
        list_release_for_first_stage_use_compartment.save()
        function_release_for_first_stage_recycling_compartment.save()
        function_release_for_second_stage_use_compartment.save()
        function_release_for_third_stage_use_compartment.save()
        first_stage_use_compartment.save()
        first_stage_recycling_compartment.save()
        second_stage_use_compartment.save()
        third_stage_use_compartment.save()
        first_stage_disposal_compartment.save()
        second_stage_disposal_compartment.save()
        third_stage_disposal_compartment.save()
        third_stage_export_compartment.save()
        import_of_ad_inflow.save()
        import_of_send_inflow.save()
        fvif_for_efi.save()
        import_of_std_inflow.save()
        fvif_1.save()
        fvif_2.save()
        fvif_3.save()
        fvif_4.save()
        fvif_5.save()
        fvif_6.save()
        rcif_7.save()
        si_1.save()
        si_2.save()
        si_3.save()
        si_4.save()
        si_5.save()
        si_6.save()
        si_7.save()
        stochastic_transfer_for_first_stage_flow_compartment.save()
        random_choice_transfer_for_first_stage_flow_compartment.save()
        const_transfer_for_first_stage_flow_compartment.save()
        stochastic_transfer_for_second_stage_flow_compartment.save()
        const_transfer_for_second_stage_flow_compartment.save()
        stochastic_transfer_for_third_stage_flow_compartment.save()
        const_transfer_for_third_stage_flow_compartment.save()
        transfer_for_first_stage_use_compartment.save()
        transfer_for_first_stage_use_recycling.save()
        transfer_for_second_stage_use_compartment.save()
        transfer_for_first_third_use_compartment.save()