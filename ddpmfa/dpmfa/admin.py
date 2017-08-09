from django.contrib import admin

from .models import *

admin.site.register(model)
admin.site.register(compartment)
admin.site.register(flow_compartment)
admin.site.register(local_release)
admin.site.register(stock)
admin.site.register(sink)
admin.site.register(fixed_rate_release)
admin.site.register(list_release)
admin.site.register(function_release)
admin.site.register(transfer)
admin.site.register(constant_transfer)
admin.site.register(random_choice_transfer)
admin.site.register(stochastic_transfer)
admin.site.register(aggregated_transfer)
admin.site.register(external_inflow)
admin.site.register(external_list_inflow)
admin.site.register(external_function_inflow)
admin.site.register(single_period_inflow)
admin.site.register(fixed_value_inflow)
admin.site.register(stochastic_function_inflow)
admin.site.register(random_choice_inflow)
admin.site.register(project)
admin.site.register(simulation)
admin.site.register(flow_compartment_outflow_record)
admin.site.register(compartment_inflow_record)
admin.site.register(compartment_inventory_record)
admin.site.register(stock_immediate_flow_record)