# -*- coding: utf-8 -*-
"""
Created in July 20178

@author: Remo Schenker

This Model is designed to demonstrate the functionality of the Dynamic
Probabilistic Mateial Flow Modeling package. It has been created to demonstrate
most of the functionality of th DPMFA package. The model threfore does not describe a 
scientifically justified model. It has been created only for demonstration purposes.

The system boundary of the model is Switzerland. The model differentiates between
two distinct areas, the economy and the private households.

Each of those arease includes three material inflow sources (Import of different Devices). The inflow go
directly to the flow compartment "Frist Stage Use of Economy" resp. "First Stage Use 
of Households". Thsese inflows were used to illustrate all the different types of 
inflows provided by the DPFMA package:

- External List Inflow -> fixed, random or stochastic
- External Function Inflow -> fixed, randmom or stochastic

After the first flow compartment (i. e. First Stage Use (of either Economy or Households)) 
the flow is split into a part that is transfered to the sink "Frist Stage Disposal", the flow
compartment "Frist Stage Recycling" or the flow compartment "Second Stage Use".

The material in the Flow Compartment "Frist Stage Recycling" flows after a delay also 
to the flow compartment "Second Stage Use".

After the "Second Stage Use" the material is being transfered either to the sink "Second Stage
Disposal", to the flow compartment "Second Stage Recycling" or to the flow compartment "Third
Stage Use".

Finally, from the flow compartment "Third Stage Use" the material is being transfered to either
the sink "Third Stage Disposal", the sink "Disposal outside Switzerland" or the sink "Export".

[TODO: rse]: determine how the flows should be described

The model includes six material inflow sources to flow compartment
"Flow Compartment 1" where the flow is split into a part that is transferred
to the sink compartment "Sink 1" and the stock compartment "Stock 1".
After a delay, the inflow to "Stock 1" is further transported to "Sink 2"

The model parameters for the absolute input to the system and the relative
transfer coefficients in the split of the flow in "Compartment 1" are assumed
to be not precisely known.

The model inflow is represented by an indepenendent normal distribution for
each period. In the first period a mean value of 1000t is assumed, increased
by 200t in every subsequent period. For each distribution the standard
deviation is 250t.

The split in "Compartment 1" is represented by a triangular distribution for
the transfer coefficient for the flow proportion to "Sink 1" with a mode value
of 0.7 and a min value of 0.5 and a max value of 0.9. The remainder is trans-
ferred to "Stock 1"

The inflow to "Stock 1" is kept there for 2 periods completely. In the
following 2 periods 50% of the material is further transported to the model
sink "Sink 2" in each of those 2 periods.

The Sinks 1 and 2 mark the endpoints of the material streams.

"""

import numpy.random as nr
import components as cp
import model as model

# creation of the model
IotModel = model.Model("IoT Model")

# creation of the external inflows to the system

EconomyImportOfAdInflow = cp.ExternalListInflow('Import of Actuator Devices (Economy)')
EconomyImportOfSendInflow = cp.ExternalListInflow('Import of Sensor Devices (Economy)')
EconomyImportOfStdInflow = cp.ExternalListInflow('Import of Streaming Devices (Economy)')

HouseholdsImportOfAdInflow = cp.ExternalFunctionInflow('Import of Actuator Devices (Households)')
HouseholdsImportOfSendInflow = cp.ExternalFunctionInflow('Import of Sensor Devices (Households)')
HouseholdsImportOfStdInflow = cp.ExternalFunctionInflow('Import of Streaming Devices (Households)')

# creation of the flow compartments
EconomyFirstStageUseCompartment = cp.FlowCompartment("First Stage Use (Economy)")
EconomyFirstStageRecyclingCompartment = cp.FlowCompartment("First Stage Use (Economy)")
EconomyFirstStageDisposalCompartment = cp.FlowCompartment("First Stage Use (Economy)")

EconomySecondStageUseCompartment = cp.FlowCompartment("Second Stage Use (Economy)")
EconomySecondStageRecyclingCompartment = cp.FlowCompartment("Second Stage Use (Economy)")
EconomySecondStageDisposalCompartment = cp.FlowCompartment("Second Stage Use (Economy)")

EconomyThirdStageUseCompartment = cp.FlowCompartment("Third Stage Use (Economy)")
EconomyThirdStageRecyclingCompartment = cp.FlowCompartment("Third Stage Use (Economy)")
EconomyThirdStageDisposalCompartment = cp.FlowCompartment("Third Stage Use (Economy)")
