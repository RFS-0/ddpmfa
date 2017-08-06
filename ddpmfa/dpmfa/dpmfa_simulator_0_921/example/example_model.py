# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 10:43:53 2015

@author: Nikolaus Bornhöft

This Model is designed to demonstrate the functionality of the Dynamic
Probabilistic Mateial Flow Modeling package.

The model includes a material inflow source to flow compartment
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
import dpmfa_simulator.components as cp
import dpmfa_simulator.model as model


# creation of the model
exampleModel = model.Model('Example Model')

# creation of the Flow Compartment
compartment1 = cp.FlowCompartment('Flow Compartment 1', logInflows = True, logOutflows =True)

# creation of the stock
stock1 = cp.Stock('Stock 1', logInflows = True, logOutflows = True)

# Sinks
sink1 = cp.Sink('Sink 1', logInflows = True)
sink2 = cp.Sink('Sink 2', logInflows = True)


# external inflows to the system
inflow = cp.ExternalListInflow(compartment1, [\
    cp.StochasticFunctionInflow(nr.normal, [1000, 250]),
    cp.StochasticFunctionInflow(nr.normal, [1200, 250]),
    cp.StochasticFunctionInflow(nr.normal, [1400, 250]),
    cp.StochasticFunctionInflow(nr.normal, [1600, 250]),
    cp.StochasticFunctionInflow(nr.normal, [1800, 250])])


# material transfer from flow compartment to Sink 1 as triangular distribution
# remaining part transferred to Stock 1
compartment1.transfers= [cp.StochasticTransfer(nr.triangular, [0.5, 0.7, 0.9], sink1, priority = 2),
                         cp.ConstTransfer(1, stock1, priority = 1)]

# release strategy, defining the delay time and the release rates based on material transferred to Stock 1
stock1.localRelease = cp.ListRelease([0.5, 0.5], delay = 2)

# total release from Stock in transferred to
stock1.transfers =[cp.ConstTransfer(1, sink2)]

# add compartments and inflow to the model
exampleModel.setCompartments([compartment1, stock1, sink1, sink2])
exampleModel.setInflows([inflow])
