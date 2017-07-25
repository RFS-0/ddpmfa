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

import numpy as np
import numpy.random as nr
import components as cp
import model as model
import simulator as sim

# creation of the model
IotModel = model.Model("IoT Model")

# creation of the external inflows to the system


# These Inflows can be used in ExternalListInflow

FixedValueInflows1 = [
    cp.FixedValueInflow(10),
    cp.FixedValueInflow(20),
    cp.FixedValueInflow(10),
    cp.FixedValueInflow(20),
    cp.FixedValueInflow(10),
    cp.FixedValueInflow(10),
    cp.RandomChoiceInflow([0, 10, 100, 1000, 1000])
]

StochasticInflows1 = [
    cp.StochasticFunctionInflow(nr.normal, [1000, 250]),
    cp.StochasticFunctionInflow(nr.normal, [1200, 250]),
    cp.StochasticFunctionInflow(nr.normal, [1400, 250]),
    cp.StochasticFunctionInflow(nr.normal, [1600, 250]),
    cp.StochasticFunctionInflow(nr.normal, [1800, 250]),
    cp.StochasticFunctionInflow(nr.normal, [1800, 250]),
    cp.StochasticFunctionInflow(nr.normal, [1800, 250])
]

def expInflowFunction(base, period):
    return base ** period

def squareInflowfunction(base, period):
    return base * period ** 2

#RandomChoiceInflows1 = [
#    cp.RandomChoiceInflow([10, 100, 1000, 4, 7]),
#    cp.RandomChoiceInflow([10, 100, 1000, 4, 7]),
#    cp.RandomChoiceInflow([10, 100, 1000, 4, 7]),
#    cp.RandomChoiceInflow([10, 100, 1000, 4, 7]),
#    cp.RandomChoiceInflow([10, 100, 1000, 4, 7]),
#    cp.RandomChoiceInflow([10, 100, 1000, 4, 7]),
#    cp.RandomChoiceInflow([10, 100, 1000, 4, 7])
#]

# creation of the flow compartments
EconomyFirstStageUseCompartment = cp.Stock(name="First Stage Use (Economy)", logInflows = True, logOutflows = True)
EconomyFirstStageRecyclingCompartment = cp.Stock(name="First Stage Recycling (Economy)", logInflows = True, logOutflows = True)
EconomyFirstStageDisposalCompartment = cp.Sink(name="First Stage Disposal (Economy)", logInflows = True)

EconomyFirstStageFlowCompartment = cp.FlowCompartment(name="First Stage Flow Compartment (Economy)", logInflows = True, logOutflows = True)

EconomySecondStageUseCompartment = cp.Stock(name="Second Stage Use (Economy)", logInflows = True, logOutflows = True)
EconomySecondStageRecyclingCompartment = cp.Stock(name="Second Stage Recycling (Economy)", logInflows = True, logOutflows = True)
EconomySecondStageDisposalCompartment = cp.Sink(name="Second Stage Disposal (Economy)", logInflows = True)

EconomySecondStageFlowCompartment = cp.FlowCompartment(name="Second Stage Flow Compartment (Economy)", logInflows = True, logOutflows = True)

EconomyThirdStageUseCompartment = cp.Stock(name="Third Stage Use (Economy)", logInflows = True)
EconomyThirdStageDisposalCompartment = cp.Sink(name="Third Stage Use (Economy)", logInflows = True)
EconomyThirdStageExportCompartment = cp.Sink(name="Third Stage Use (Economy)", logInflows = True)



EconomyImportOfAdInflow = cp.ExternalListInflow(target=EconomyFirstStageUseCompartment, inflowList=FixedValueInflows1)
EconomyImportOfSendInflow = cp.ExternalListInflow(target=EconomyFirstStageUseCompartment, inflowList=StochasticInflows1)
EconomyImportOfStdInflow = cp.ExternalFunctionInflow(
    target=EconomyFirstStageUseCompartment, 
    basicInflow=cp.FixedValueInflow(10),
    inflowFunction=expInflowFunction,
    derivationDistribution=nr.normal,
    derivationParameters=[1000, 250],
    startDelay=3
)

# add compartments and inflow to the model
IotModel.setCompartments([EconomyFirstStageUseCompartment])
IotModel.setInflows([EconomyImportOfAdInflow, 
                         EconomyImportOfSendInflow, 
                         EconomyImportOfStdInflow])

# check validity of the model
IotModel.checkModelValidity()

# investigated number of periods (e.g. Years in the origninal system)
PERIODS = 7
# For each element of the sample the model is calculated once using a set of
# random values for the model parameters from the underlying probability distributions.
SAMPLESIZE = 100

# create the simulator
simulator = sim.Simulator(
    runs=SAMPLESIZE, 
    periods=PERIODS, 
    seed=1, 
    useGlobalTCSettings=True, 
    normalizeTCs=True)

# connect the model
simulator.setModel(IotModel)

# The Monte-Carlo simultion process is perfomed.
simulator.runSimulation()

#==============================================================================
#  Evalutation of the simulation results.
#
#  Display the material amount in sinks and stocks over time:
#   - by printing the inventory matrix
#   - plotting the simulation output as serieses of annual values for each sample (grey lines)
#   - calculating the annual mean values (red line)
#==============================================================================


stock = simulator.getStocks()

# plotting \\ evaluation
allFigures = []
figureNumber = 0
xRange = np.arange(PERIODS)
for sink in sinks:
    print ''
    print stock + ':'
    print sink.inventory
    fig = plt.figure(figureNumber)
    figureNumber +=1
    plt.title(sink.name)
    plt.xlabel('Period')
    plt.ylabel('Amount in tons')

    sinkInv = sink.inventory

    for row in sinkInv:
        plt.plot(xRange, row, color = '0.5', lw = 1)
        #plt.show()

    sinkMeans = []
    for row in sink.inventory.transpose():
        sinkMeans.append(np.mean(row))
    plt.plot(xRange, sinkMeans, color = 'red', linewidth=2)
    #plt.show()