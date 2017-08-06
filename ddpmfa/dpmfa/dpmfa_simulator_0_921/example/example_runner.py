# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 11:41:50 2015

@author: bni


The example_runner module serves to illustrate the functionality of the Dynamic
Probabilisti Material Flow Assesssment package.

In this script a simulator object is created. The example model defined in the
package is imported and connected to the simulator.

Then the simulator is used to perform a Monte-Carlo experiment on the model
that propagates the assumptions about the model parameters (e.g. input volumes,
transfer coefficients and delay times) to the dependent variables such as
material in stock over time.

The simulation results, for the variables under examination such as stocks and
flow volumes are provided as matrix of values over time and sample size. Based
on these matrices further evaluations and visualizations can be performed.
"""


import dpmfa_simulator.simulator as sc
import numpy as np
import matplotlib.pyplot as plt
import example.example_model


# the example model
model = example.example_model.exampleModel
model.checkModelValidity()

# investigated number of periods (e.g. Years in the origninal system)
PERIODS = 5
# For each element of the sample the model is calculated once using a set of
# random values for the model parameters from the underlying probability distributions.
SAMPLESIZE = 20

# create the simulator
simulator = sc.Simulator(SAMPLESIZE, PERIODS, 1, True, True)

# connect the model
simulator.setModel(model)

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


sinks = simulator.getSinks()

# plotting / evaluation
allFigures = []
figureNumber = 0
xRange = np.arange(PERIODS)
for sink in sinks:
    print ''
    print sink.name + ':'
    print sink.inventory
    fig = plt.figure(figureNumber)
    figureNumber +=1
    plt.title(sink.name)
    plt.xlabel('Period')
    plt.ylabel('Amount in tons')

    sinkInv = sink.inventory

    for row in sinkInv:
        plt.plot(xRange, row, color = '0.5', lw = 1)

    sinkMeans = []
    for row in sink.inventory.transpose():
        sinkMeans.append(np.mean(row))
    plt.plot(xRange, sinkMeans, color = 'red', linewidth=2)
