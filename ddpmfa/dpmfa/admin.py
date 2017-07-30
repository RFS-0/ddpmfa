from django.contrib import admin
from dpmfa_simulator.components import FlowCompartment

from .models import *

admin.site.register(Compartment)
admin.site.register(FlowCompartment)
admin.site.register(Stock)
admin.site.register(FixedRateRelease)
admin.site.register(ListRelease)
admin.site.register(FunctionRelease)
admin.site.register(Transfer)
admin.site.register(ConstantTransfer)
admin.site.register(RandomChoiceTransfer)
admin.site.register(StochasticTransfer)
admin.site.register(AggregatedTransfer)
admin.site.register(ExternalInflow)
admin.site.register(ExternalListInflow)
admin.site.register(ExternalFunctionInflow)
admin.site.register(SinglePeriodInflow)
admin.site.register(FixedValueInflow)
admin.site.register(StochasticInflow)
admin.site.register(RandomChoiceInflow)
admin.site.register(Model)

