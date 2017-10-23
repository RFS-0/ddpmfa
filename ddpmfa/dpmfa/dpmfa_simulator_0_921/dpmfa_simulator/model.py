# -*- coding: utf-8 -*-
"""
Created on Wed Mar 05 11:18:47 2014

@author: bni

The Model module contains the class model to define simulation models for
dynamic probabilistic material flow modeling and simulation.

The type model aggregates several elements from the components module to a
complete unit that covers all aspects of the original system that are necessary
to comprehend the material flows that lead to a specific accumulation and the
uncertainty about it.
"""

import dpmfa.dpmfa_simulator_0_921.dpmfa_simulator.components as cp
import numpy.random as nr



class Model(object):
    """The Model represents the original system as a set of Compartment, flows
    as relative dependencies between the copmartments and absolute, periodic
    inflows to the system.
    The compartment list may contain FlowCompartmentartments that represent immediate
    onflow of material entering a compartment, Sinks that account material
    accumulation over time and Stocks that relese accumulated material after
    some time.

    A PMFA model is assabled using and parametrizing types from the components
    module.


    Parameters:
    ---------------------
    name: string
        the model name
    compartments[]: list<components.Compartment>
        list of all model compartments - Flow Compartments, Stocks and Sinks
    inflows[]: list<components.ExternalInflow>
        list of sources of external inflows to the sysetm
    seed: float
        the seed value for all proability distributions
    """


    def __init__(self, name, compartments=[], inflows=[]):
        self.name = name

        if all(isinstance(comp, cp.Compartment) for comp in compartments):
            self.compartments = compartments
        else:
            print('invalid compartment list!')

        if all(isinstance(inflow, cp.ExternalInflow) for inflow in inflows):
            self.inflows = inflows
        else:
            print('invalid inflow list!')

        self.seed = 1
        self.categoriesList = []

    def setCompartments(self, compartmentList):
        """
        Assigns a list of Compartments to the Model

        Parameter:
        ----------------
        compartmentList: list<component.Compartment>
            list of all compartments - Flow Compartments, Sinks and Stocks of \
            the model
        """
        if all(isinstance(comp, cp.Compartment) for comp in compartmentList):
            self.compartments = compartmentList
        else:
            print('invalid compartment list!')

    def addCompartment(self, compartment):
        """
        Adds a single compartment to the model


        Parameters:
        ----------------
        compartment: component.Compartment
        """
        if(isinstance(compartment, cp.Compartment)):
            self.compartments.append(compartment)

    def setInflows(self, inflowList):
        """
        Assigns inflow list to the model

        Parameters:
        ----------------
        inflowList: list<components.ExternalInflow>
            list of sources of external inflows to the sysetm
        """
        if all(isinstance(inflow, cp.ExternalInflow) for inflow in inflowList):
            self.inflows = inflowList
        else:
            print('invalid inflow list!')


    def addInflow(self, inflow):
        """
        Adds an external inflow source to the model

        Parameter:
        ----------------
        inflow: components.ExternalInflow
            an external source
        """

        if(isinstance(inflow, cp.ExternalInflow)):
            self.inflows.append(inflow)
        else:
            print('not an external inflow')

    def updateCompartmentCategories(self):
        '''
        updates the category list of the model to contain all compartments
        categories
        '''

        newCatList = []
        for comp in self.compartments:
            if comp.categories:
                newCatList += comp.categories
        self.categoriesList  = list(set(newCatList))

    def getCategoriesList(self):
        return self.categoriesList


    def setSeed(self, seed):
        """
        sets common seed value for all probability distributions of the Model

        Parameter:
        ----------------
        seed: int
            the seed value
        """
        self.seed = seed
        nr.seed(seed)





    def addTransfer(self, compartmentName, transfer):
        """
        Adds a transfers to one Compartment that is part of the model.
        The compartment is accessed by its name.

        Parameters:
        ----------------
        compartmentName: string
            name of the compartment
        transfer: component.Transfer
            transfer to be added
        """
        if((isinstance(transfer, cp.Transfer))):
            compartment = next((comp for comp in self.compartments if comp.name == compartmentName), None)
            compartment.transfers.append(transfer)
        else:
            print('not a transfer')


    def setReleaseStrategy(self, stockName, releaseStrategy):
        """
        Defines the release strategy for one Stock that is part of the model.
        The stock is accessed by its name.

        Parameters:
        ----------------
        stockName: string
            name of the stock
        releaseStrategy: components.LocalRelease
            the release strategy

        """
        stock = next((comp for comp in self.compartments if comp.name == stockName), None)
        if (stock !=None):
            stock.releaseStrategy = releaseStrategy
        else:
            print('no such stock: '+ str(stockName))

    def checkModelValidity(self):
        """
        Checks the types of the model components; Checks types, if there are
        compartments, if flow compartmetns have transfers and if stocks have
        a release strategy.
        """
        
        valid = True
        
        for comp in self.compartments:
            if isinstance(comp, cp.FlowCompartment):
                transferList = comp.transfers
                if not transferList:
                    print('Err: no transfers assined')
                    valid = False
                for trans in transferList:
                    if not isinstance(trans, cp.Transfer):
                        print('invalid transfer')
                        valid = False

            if isinstance(comp, cp.Stock):
                release = comp.localRelease
                if not isinstance(release, cp.LocalRelease):
                    print('local release from stock not assigned')
                    valid = False

        if not self.inflows:
            print('No model inflow defined!')
        if valid:
            print("Model is valid")
        else:
            print("Model is not valid!")
        return valid