# -*- coding: utf-8 -*-
"""
Created on Tue Mar 04 17:22:50 2014

@author: bni


The Simulator class provides a framework to perform simulation experiments on a
Dynamic Probabilistic Material Flow Model.
"""

import numpy as np
import numpy.linalg as la
import dpmfa.dpmfa_simulator_0_921.dpmfa_simulator.components as cp
import math
import pdb


class Simulator(object):
    """ The simulator provides a framework to perform simulaton experiments on
    pmfa models.

    Parameters:
    -------------
    runs: integer
        the number of simulation runs (the sample size) over which the model \
        is evaluated.
    periods: integer
        the number of periods (e.g. years) over which the system is investigated
    seed: integer
        The seed value for all probability distributions.
    useGlobalTCSettings: boolean
        defines, if the settings for the normalization of the outgoing TCs \
        from Compartments or Stocks are used that are made in the model \
        definition (False) or the global settings defined in the simulator (True)
    normalizeTCs: boolean
        defines, if outgoing TCs from Model Compartments and Stocks are adjusted to sum\
        up to one. This Parameter is only considered, if the global parameter\
        for normalization is used.


    """
    def __init__(self, runs, periods, seed = None, useGlobalTCSettings = True,
    normalizeTCs = True):
        self.numRuns = runs
        self.numPeriods = periods
        self.useGlobalTCSettings = useGlobalTCSettings
        self.normalizeTCs = normalizeTCs
        if seed is None:
            self.seed = np.random.randint(1, 10000)
        else:
            self.seed = seed
        self.flowCompartments = []
        self.sinks = []
        self.stocks = []
        self.checkInflows  =None

    def setModel(self, model):
        self.model = model
        self.compartments = model.compartments
        self.inflows = model.inflows
        self.model.setSeed(self.seed)
        self.model.updateCompartmentCategories()

        for i in range(len(self.compartments)):
            self.compartments[i].compNumber = i

        for comp in self.compartments:
            comp.initFlowLog(self.numRuns, self.numPeriods)
            if isinstance(comp, cp.FlowCompartment):
                self.flowCompartments.append(comp)
            if isinstance(comp, cp.Sink):
                self.sinks.append(comp)
                comp.initInventory(self.numRuns, self.numPeriods)
            if type(comp) is cp.Stock:
                self.stocks.append(comp)
                comp.updateImmediateReleaseRate()


    def runSimulation(self):
        """ performs the simulation on the model with regard to the given
        parameters
        """
        currentStep = 1

        stepSize =  math.ceil(self.numRuns/100)
        currentStepRun = math.ceil(stepSize)

        for run in range(self.numRuns):
            
            for comp in self.flowCompartments:
                comp.determineTCs(self.useGlobalTCSettings, self.normalizeTCs)
            for infl in self.inflows:
                infl.sampleValues()
            for stock in self.stocks:
                stock.determineTCs(self.useGlobalTCSettings, self.normalizeTCs)
#                stock.localRelease.sampleDelay()

            allInflows = np.zeros((len(self.compartments), self.numPeriods))

            for period in range (self.numPeriods):
                
                for sink in self.sinks:
                    sink.updateInventory(run, period)

                for inflow in self.inflows:
                    allInflows[self.compartments.index(inflow.target), period] += inflow.getCurrentInflow(period)

                for stock in self.stocks:
                    localReleases = stock.releaseMaterial(run, period)
                    for locRel in localReleases.keys():
                        allInflows [locRel.compNumber, period] += localReleases[locRel]

                inflowVector = allInflows[:,period]
                flowMatrix = np.zeros(shape=(len(self.compartments), len(self.compartments)))
                np.fill_diagonal(flowMatrix,1)

                for compartment in self.flowCompartments:
                    for trans in compartment.transfers:
                        flowMatrix[trans.target.compNumber, compartment.compNumber]= -trans.getCurrentTC()*compartment.immediateReleaseRate
                solutionVector = la.solve(flowMatrix, inflowVector)

                for i in self.compartments:
                    i.logFlow(run, period, solutionVector[i.compNumber])

                for i in self.sinks:
                    i.storeMaterial(run, period, solutionVector[i.compNumber])

            if run == currentStepRun:
                currentStepRun += stepSize
                currentStep +=1

    def getAllStockedMaterial(self):
        '''
        returns a dictionary of all sinks and stocks and the matrices of the
        logged stored material
        '''
        inventories = {}
        for sink in self.sinks:
            inventories[sink.name]= sink.inventory
        return inventories


    def getLoggedInflows(self):
        '''
        returns a dictionary of all compartments and logged inflow matrices
        '''
        inflows = {}
        for comp in self.compartments:
            if comp.logInflows:
                inflows[comp.name]= comp.inflowRecord
        return inflows


    def getLoggedTotalOutflows(self):
        '''
        gives absolulte outflows from each compartments (if logged)
        '''
        outflows = {}
        for comp in self.flowCompartments:
            if comp.logOutflows:
                outflowSum = []
                for outflow in comp.outflowRecord:
                    outflowSum.append(comp.outflowRecord[outflow])
                outflows[comp.name]=sum(outflowSum)
        return outflows


    def getLoggedFlows(self):
        '''
        returns matrices for all flows in between compartments (dictionary of dictionaries)
        '''
        allFlows = {}
        for comp in self.flowCompartments:
            if comp.logOutflows:
                allFlows[comp.name]= comp.outflowRecord

        return allFlows

    def getImmediateFlowsFromAllStocks(self):
        '''
        returns all immediate flows from stocks
        '''
        immediateStocks = [stock for stock in self.stocks if stock.logImmediateFlows]

        allFlows = {}
        for stock in immediateStocks:
            allFlows[stock]=stock.immediateFlowRecord
        return allFlows


    def getLoggedCategoryStock(self, category):
        '''
        return the summed up inventory for all sinks and stocks of a category
        '''
        catStocks = [c for c in self.sinks if category in c.categories]
        combinedInventory = []

        for stock in catStocks:
            combinedInventory.append(stock.inventory)
        return sum(combinedInventory)


    def getLoggedCategoryInflows(self, category):
        '''
        returns the summed up inflow to the compartments of a category
        '''
        catCompartments = [comp for comp in self.compartments if category in comp.categories and comp.logInflows]
        loggedInflows = []
        for catComp in catCompartments:
            loggedInflows.append(catComp.inflowRecord)
        return sum(loggedInflows)


    def getLoggedCategoryOutflowSum(self, category):
        '''
        returns a matrix of the sums of the outflows from all the compartments of the category to all
        subsequet compartments
        '''
        catFlows = [c for c in self.flowCompartments if category in c.categories and c.logOutflows]
        allOutflows = []
        for catFlow in catFlows:
            for name in catFlow.outflowRecord:
                allOutflows.append(catFlow.outflowRecord[name])
        return sum(allOutflows)


    def getLoggedCategoryOutflows(self, category):
        '''
        returns the outflows of all comparmtents of a category to all subsequent compartments
        '''
        catFlows = [c for c in self.flowCompartments if category in c.categories and c.logOutflows]
        allFlows = {}
        for flow in catFlows:
            for name in flow.outflowRecord:
                if allFlows.has_key(name):
                    allFlows[name] = allFlows[name]+flow.outflowRecord[name]
                else:
                    allFlows[name]= flow.outflowRecord[name]
        return allFlows


    def getCategoryImmediateFlowFromStockSum(self, category):
        '''
        returns a matrix of the sum of all immediate outflows from stocks of a category
        '''
        immediateStocks = [stock for stock in self.stocks if stock.logImmediateFlows and category in stock.categories]
        totalImmediateFlow = []
        for stock in immediateStocks:
            for rec in stock.immediateFlowRecord:
                totalImmediateFlow.append(stock.immediateFlowRecord[rec])

        return sum(totalImmediateFlow)



    def getCompartmentsOfCategory(self, category):
        '''
        returns all compartments of one category
        '''
        return [c for c in self.compartments if category in c.categories]



    def getCombinedOutflows(compartmentList):
        """
        returns a combined dictonary of the outflows of a list of compartments
        """

        combinedOutflow= {}
        for comp in compartmentList:
            for name in comp.outflowRecord:
                if combinedOutflow.has_key(name):
                    combinedOutflow[name] = combinedOutflow[name]+comp.outflowRecord[name]
                else:
                    combinedOutflow[name]= comp.outflowRecord[name]

        return combinedOutflow

    def getSinks(self):
        """
        returns all Sinks of the model.
        """
        return self.sinks

    def getStocks(self):
        """
        returns all Stocks of the model
        """
        return self.stocks

    def getCompartments(self):
        """
        returns a list of all compartments, flow compartments, sinks and stocks
        """
        return self.compartments

    def getFlowCompartmentartments(self):
        """
        returns a list of all flow compartments
        """
        return self.flowCompartments


    def getLoggedOutflows(self):
        """
        returns a list of all flowCompartments that log outflows
        """

        loggedOutflows = [comp for comp in self.flowCompartments if comp.logOutflows]
        return loggedOutflows



    def getCategories(self):
        '''
        category list of the model
        '''
        return self.model.categoriesList