import pprint

import dpmfa.models as django_models
from dpmfa_simulator.components import ExternalListInflow

#==============================================================================
#  Package variables
#==============================================================================

# Types

EXTERNAL_LIST_INFLOW = 'externalListInflow'
EXTERNAL_FUNCTION_INFLOW = 'externalFunctionInflow'

FLOW_COMPARTMENT = 'flowCompartment'
STOCK = 'stock'
SINK = 'sink'

CONSTANT_TRANSFER = 'constantTransfer'
RANDOM_CHOICE_TRANSFER = 'randomChoiceTransfer'
AGGREGATED_TRANSFER = 'aggregatedTransfer'
STOCHASTIC_TRANSFER = 'stochasticTransfer'

INFLOW_TARGET = 'inflowTarget'


# JSON

externalListInflows = {}
externalFunctionInflows = {}

flowCompartments = {}
stocks = {}
sinks = {}

constantTransfers = {}
randomChoiceTransfers = {}
aggregatedTransfers = {}
stochasticTransfers = {}

inflowTargets = {}

# DB

compartments_DB = {}
flow_compartments_DB = {}
sinks_DB = {}
stocks_DB = {}
transfers_DB = {}
constant_transfers_DB = {}
stochastic_transfers_DB = {}
random_choice_transfers_DB = {}
aggregated_transfers_DB = {}
local_releases_DB = {}
fixed_rate_releases_DB = {}
list_releases_DB = {}
function_releases_DB = {}
single_period_inflows_DB = {}
stochastic_function_inflows_DB = {}
random_choice_inflows_DB = {}
fixed_value_inflows_DB = {}
external_inflows_DB = {}
external_list_inflows_DB = {}
external_function_inflows_DB = {}

#==============================================================================
#  Package functions
#==============================================================================

# JSON

def addExternalListInflow(primaryKey, externalListInflow):
    externalListInflows[primaryKey] = externalListInflow

def getExternalListInflow(primaryKey):
    return externalListInflows.get(primaryKey)

def getExternalListInflows():
    return externalListInflows

def addExternalFunctionInflow(primaryKey, externalFunctionInflow):
    externalFunctionInflows[primaryKey] = externalFunctionInflow

def getExternalFunctionInflow(primaryKey):
    return externalFunctionInflows.get(primaryKey)

def getExternalFunctionInflows():
    return externalFunctionInflows

def addFlowCompartment(primaryKey, flowCompartment):
    flowCompartments[primaryKey] = flowCompartment

def getFlowCompartment(primaryKey):
    return flowCompartments.get(primaryKey)

def getFlowCompartments():
    return flowCompartments

def addStock(primaryKey, stock):
    stocks[primaryKey] = stock

def getStock(primaryKey):
    return stocks.get(primaryKey)

def getStocks():
    return stocks

def addSink(primaryKey, sink):
    sinks[primaryKey] = sink

def getSink(primaryKey):
    return sinks.get(primaryKey)

def getSinks():
    return sinks

def addConstantTransfer(primaryKey, constantTransfer):
    constantTransfers[primaryKey] = constantTransfer

def getConstantTransfer(primaryKey):
    return constantTransfers.get(primaryKey)

def getConstantTransfers():
    return constantTransfers

def addRandomChoiceTransfer(primaryKey, randomChoiceTransfer):
    randomChoiceTransfers[primaryKey] = randomChoiceTransfer

def getRandomChoiceTransfer(primaryKey):
    return randomChoiceTransfers.get(primaryKey)

def getRandomChoiceTransfers():
    return randomChoiceTransfers

def addAggregatedTransfer(primaryKey, aggregatedTransfer):
    aggregatedTransfers[primaryKey] = aggregatedTransfer

def getAggregatedTransfer(primaryKey):
    return aggregatedTransfers.get(primaryKey)

def getAggregatedTransfers():
    return aggregatedTransfers

def addStochasticTransfers(primaryKey, stochasticTransfer):
    stochasticTransfers[primaryKey] = stochasticTransfer

def getStochasticTransfer(primaryKey):
    return stochasticTransfers.get(primaryKey)

def getStochasticTransfers():
    return stochasticTransfers

def addInflowTarget(primaryKey, inflowTarget):
    inflowTargets[primaryKey] = inflowTarget
    
def getInflowTargets():
    return inflowTargets

def getInflowTarget(primaryKey):
    return inflowTargets[primaryKey]

# Compartments

def getDBEntityCompartment(primaryKey):
    return compartments_DB.get(primaryKey)

def addDBEntityCompartment(primaryKey, DBEntity):
    compartments_DB[primaryKey] = DBEntity

def getDBEntityFlowCompartment(primaryKey):
    return flow_compartments_DB.get(primaryKey)

def addDBEntityFlowCompartment(primaryKey, DBEntity):
    flow_compartments_DB[primaryKey] = DBEntity

def getDBEntitySink(primaryKey):
    return sinks_DB.get(primaryKey)

def addDBEntitySink(primaryKey, DBEntity):
    sinks_DB[primaryKey] = DBEntity

def getDBEntityStock(primaryKey):
    return stocks_DB.get(primaryKey)

def addDBEntityStock(primaryKey, DBEntity):
    stocks_DB[primaryKey] = DBEntity

# Transfers

def getDBEntityTransfer(primaryKey):
    return transfers_DB.get(primaryKey)

def addDBEntityTransfer(primaryKey, DBEntity):
    transfers_DB[primaryKey] = DBEntity
    
def getDBEntityConstantTransfer(primaryKey):
    return constant_transfers_DB.get(primaryKey)

def addDBEntityConstantTransfer(primaryKey, DBEntity):
    constant_transfers_DB[primaryKey] = DBEntity
    
def getDBEntityStochasticTransfer(primaryKey):
    return stochastic_transfers_DB.get(primaryKey)

def addDBEntityStochasticTransfer(primaryKey, DBEntity):
    stochastic_transfers_DB[primaryKey] = DBEntity
    
def getDBEntityRandomChoiceTransfer(primaryKey):
    return random_choice_transfers_DB.get(primaryKey)

def addDBEntityRandomChoiceTransfer(primaryKey, DBEntity):
    random_choice_transfers_DB[primaryKey] = DBEntity
    
def getDBEntityAggregatedTransfer(primaryKey):
    return aggregated_transfers_DB.get(primaryKey)

def addDBEntityAggregatedTransfer(primaryKey, DBEntity):
    aggregated_transfers_DB[primaryKey] = DBEntity

# Releases

def getDBEntityLocalRelease(primaryKey):
    return local_releases_DB.get(primaryKey)

def addDBEntityLocalRelease(primaryKey, DBEntity):
    local_releases_DB[primaryKey] = DBEntity

def getDBEntityFixedRateRelease(primaryKey):
    return fixed_rate_releases_DB.get(primaryKey)

def addDBEntityFixedRateRelease(primaryKey, DBEntity):
    fixed_rate_releases_DB[primaryKey] = DBEntity

def getDBEntityListRelease(primaryKey):
    return list_releases_DB.get(primaryKey)

def addDBEntityListRelease(primaryKey, DBEntity):
    list_releases_DB[primaryKey] = DBEntity

def getDBEntityFunctionRelease(primaryKey):
    return function_releases_DB.get(primaryKey)

def addDBEntityFunctionRelease(primaryKey, DBEntity):
    function_releases_DB[primaryKey] = DBEntity

# Single Period Inflows

def getDBEntitySinglePeriodInflow(primaryKey):
    return single_period_inflows_DB.get(primaryKey)

def addDBEntitySinglePeriodInflow(primaryKey, DBEntity):
    single_period_inflows_DB[primaryKey] = DBEntity

def getDBEntityStochasticFunctionInflow(primaryKey):
    return stochastic_function_inflows_DB.get(primaryKey)

def addDBEntityStochasticFunctionInflow(primaryKey, DBEntity):
    stochastic_function_inflows_DB[primaryKey] = DBEntity

def getDBEntityRandomChoiceInflow(primaryKey):
    return random_choice_inflows_DB.get(primaryKey)

def addDBEntityRandomChoiceInflow(primaryKey, DBEntity):
    random_choice_inflows_DB[primaryKey] = DBEntity

def getDBEntityFixedValueInflow(primaryKey):
    return fixed_value_inflows_DB.get(primaryKey)

def addDBEntityFixedValueInflow(primaryKey, DBEntity):
    fixed_value_inflows_DB[primaryKey] = DBEntity
    
# External Inflows
    
def getDBEntityExternalInflow(primaryKey):
    return external_inflows_DB.get(primaryKey)

def addDBEntityExternalInflow(primaryKey, DBEntity):
    external_inflows_DB[primaryKey] = DBEntity
    
def getDBEntityExternalListInflow(primaryKey):
    return external_list_inflows_DB.get(primaryKey)

def addDBEntityExternalListInflow(primaryKey, DBEntity):
    external_list_inflows_DB[primaryKey] = DBEntity
    
def getDBEntityExternalFunctionInflow(primaryKey):
    return external_function_inflows_DB.get(primaryKey)

def addDBEntityExternalFunctionInflow(primaryKey, DBEntity):
    external_function_inflows_DB[primaryKey] = DBEntity

# Distributions
    
def getDistributionFunction(distribution_type):
    if distribution_type == 'NORM':
        return nr.normal
    elif distribution_type == 'GEO':
        return nr.geometric
    elif distribution_type == 'BINOM':
        return nr.binomial
    elif distribution_type == 'EXPO':
        return nr.exponential
    elif distribution_type == 'TRI':
        return nr.triangular
    elif distribution_type == 'UNI':
        return nr.uniform
    elif distribution_type == 'GAM':
        return nr.gamma
    elif distribution_type == 'PAR':
        return nr.pareto
    elif distribution_type == 'POI':
        return nr.poisson
    elif distribution_type == 'CHI':
        return nr.chisquare
    else:
        return None
    
class SaveManager(object):
    
    def __init__(self, jsonModel, model_pk):
        self.jsonModel = jsonModel
        self.MODEL_DB = self.recreateDBModel(model_pk) 
        
        self.nodes = self.jsonModel['nodes']
        self.connections = self.jsonModel['connections']
        
    def recreateDBModel(self, model_pk):
        
        print("Recreating db model...")
        
        old_model = django_models.model.objects.get(pk=model_pk)
        
        pk = old_model.pk
        project = old_model.project
        name = old_model.name
        description = old_model.description
        
        print("PK of old model: " + str(pk))
        
        
        
        # delete all everything that relates to the old model except model instances, experiments and results
        print("Deleting entities of model...")
        for compartment in django_models.compartment.objects.filter(model = old_model):
            print("Deleting compartment: " + str(compartment))
            compartment.delete()
            
        for localRelease in django_models.local_release.objects.filter(model = old_model):
            print("Deleting local release: " + str(localRelease))
            localRelease.delete()
            
        for transfer in django_models.transfer.objects.filter(model = old_model):
            print("Deleting transfer: " + str(transfer))
            transfer.delete()
            
        for externalInflow in django_models.external_inflow.objects.filter(model = old_model):
            print("Deleting external inflow: " + str(externalInflow))
            externalInflow.delete()
            
        for singlePeriodInflow in django_models.single_period_inflow.objects.filter(model = old_model):
            print("Deleting single period inflow: " + str(singlePeriodInflow))
            singlePeriodInflow.delete()
        
        print("Deleting old model...")
        old_model.delete()
        
        print("Creating new model...")
        
        new_model = django_models.model(
            pk = pk,
            project = project,
            name = name,
            description = description)
        
        new_model.save()
        
        print("Saved new model...")
        
        return new_model
    
    def separateEntities(self):
        self.separateNodes()
        self.separateConnections()
        
    def createNodes(self):
        self.createDBEntitiesExternalListInflows()
        self.createDBEntitiesExternalFunctionInflows()
        self.createDBEntitiesSink()
        self.createDBEntitiesFlowCompartment()
        self.createDBEntitiesStock()
    
    def createConnections(self):
        self.setupInflowTargets()
        self.createDBEntitiesConstantTransfers()
        self.createDBEntitiesRandomChoiceTransfers()
        self.createDBEntitiesStochasticTransfers()
        
        
        
           
    def separateNodes(self):
        for node in self.nodes:
            
            type = node['typeName']
            tempId = node['tempId']
            id = node['id']
            
            primaryKey = ""
            if tempId != None:
                primaryKey += tempId
            if id != None:
                primaryKey += id
                
            if type == EXTERNAL_LIST_INFLOW:
                addExternalListInflow(primaryKey, node)
            elif type == EXTERNAL_FUNCTION_INFLOW:
                addExternalFunctionInflow(primaryKey, node)
            elif type == FLOW_COMPARTMENT:
                addFlowCompartment(primaryKey, node)
            elif type == STOCK:
                addStock(primaryKey, node)
            elif type == SINK:
                addSink(primaryKey, node)
                
    def separateConnections(self):
        for connection in self.connections:
            
            type = connection['typeName']
            tempId = connection['tempId']
            id = connection['id']
            
            primaryKey = ""
            if tempId != None:
                primaryKey += tempId
            if id != None:
                primaryKey += id
                
            if type == CONSTANT_TRANSFER:
                addConstantTransfer(primaryKey, connection)
            elif type == RANDOM_CHOICE_TRANSFER:
                addRandomChoiceTransfer(primaryKey, connection)
            elif type == AGGREGATED_TRANSFER:
                addAggregatedTransfer(primaryKey, connection)
            elif type == STOCHASTIC_TRANSFER:
                addStochasticTransfers(primaryKey, connection)
            elif type == INFLOW_TARGET:
                addInflowTarget(primaryKey, connection)
                
    def createDBEntitiesExternalListInflows(self):
        for primaryKey, externalListInflow in getExternalListInflows().items():
            print("PK/ELI: " + str(primaryKey))
            self.attributes = {}
            
            external_list_inflow = django_models.external_list_inflow()
            external_list_inflow.save()
            
            self.extractAttributesExternalListInflow(externalListInflow, external_list_inflow)
            
            external_list_inflow.model = self.MODEL_DB
            external_list_inflow.target = self.getAttributeOrNone('target')
            external_list_inflow.name = self.getAttributeOrNone('name')
            external_list_inflow.start_delay = self.getAttributeOrNone('start_delay')
            external_list_inflow.derivation_distribution = self.getAttributeOrNone('derivation_distribution')
            external_list_inflow.derivation_parameters = self.getAttributeOrNone('derivation_parameters')
            external_list_inflow.derivation_factor = self.getAttributeOrNone('derivation_factor')
            external_list_inflow.x = self.getAttributeOrNone('x')
            external_list_inflow.y = self.getAttributeOrNone('y')
                
            external_list_inflow.save()
            
            addDBEntityExternalListInflow(primaryKey, external_list_inflow)
            addDBEntityExternalInflow(primaryKey, external_list_inflow)

    def createDBEntitiesExternalFunctionInflows(self):
        for primaryKey, externalFunctionInflow in getExternalFunctionInflows().items():
            print("PK/EFI: " + str(primaryKey))
            self.attributes = {}
            
            external_function_inflow = django_models.external_function_inflow()
            external_function_inflow.save()
            
            self.extractAttributesExternalFunctionInflow(externalFunctionInflow, external_function_inflow)
            
            external_function_inflow.model = self.MODEL_DB
            external_function_inflow.target = self.getAttributeOrNone('target')
            external_function_inflow.name = self.getAttributeOrNone('name')
            external_function_inflow.start_delay = self.getAttributeOrNone('start_delay')
            external_function_inflow.derivation_distribution = self.getAttributeOrNone('derivation_distribution')
            external_function_inflow.derivation_parameters = self.getAttributeOrNone('derivation_parameters')
            external_function_inflow.derivation_factor = self.getAttributeOrNone('derivation_factor')
            external_function_inflow.x = self.getAttributeOrNone('x')
            external_function_inflow.y = self.getAttributeOrNone('y')
            # to be implemented
            external_function_inflow.inflow_function=None
            # to be implemented
            external_function_inflow.function_parameters=None
            external_function_inflow.basic_inflow = self.getAttributeOrNone('basic_inflow')
            
            external_function_inflow.save()
            
            addDBEntityExternalFunctionInflow(primaryKey, external_function_inflow)
            addDBEntityExternalInflow(primaryKey, external_function_inflow)
            
    def createDBEntitiesSink(self):
        for primaryKey, sink in getSinks().items():
            print("PK/SINK: " + str(primaryKey))
            self.attributes = {}
            
            sink_db = django_models.sink()
            sink_db.save()
            
            self.extractAttributesSink(sink)
            
            sink_db.model = self.MODEL_DB
            sink_db.name = self.getAttributeOrNone('name')
            sink_db.description = self.getAttributeOrNone('description')
            sink_db.log_inflows = self.getAttributeOrNone('log_inflows')
            sink_db.categories = self.getAttributeOrNone('categories')
            sink_db.x = self.getAttributeOrNone('x')
            sink_db.y = self.getAttributeOrNone('y')
            
            sink_db.save()
            
            addDBEntitySink(primaryKey, sink_db)
            addDBEntityCompartment(primaryKey, sink_db)

    def createDBEntitiesFlowCompartment(self):
        for primaryKey, flowCompartment in getFlowCompartments().items():
            print("PK/FC: " + str(primaryKey))
            self.attributes = {}
            
            flow_compartment_db = django_models.flow_compartment()
            flow_compartment_db.save()
            
            self.extractAttributesFlowCompartment(flowCompartment)
            
            flow_compartment_db.model = self.MODEL_DB
            flow_compartment_db.name = self.getAttributeOrNone('name')
            flow_compartment_db.description = self.getAttributeOrNone('description')
            flow_compartment_db.log_inflows = self.getAttributeOrNone('log_inflows')
            flow_compartment_db.categories = self.getAttributeOrNone('categories')
            flow_compartment_db.x = self.getAttributeOrNone('x')
            flow_compartment_db.y = self.getAttributeOrNone('y')
            flow_compartment_db.adjust_outgoing_tcs = self.getAttributeOrNone('adjust_outgoing_tcs')
            flow_compartment_db.log_outflows = self.getAttributeOrNone('log_outflows')
            
            flow_compartment_db.save()
            
            addDBEntityFlowCompartment(primaryKey, flow_compartment_db)
            addDBEntityCompartment(primaryKey, flow_compartment_db)
            
    def createDBEntitiesStock(self):
        for primaryKey, stock in getStocks().items():
            print("PK/STOCKS: " + str(primaryKey))
            self.attributes = {}
            
            stock_db = django_models.stock()
            stock_db.save()
            
            self.extractAttributesStock(stock)
            
            stock_db.model = self.MODEL_DB
            stock_db.name = self.getAttributeOrNone('name')
            stock_db.description = self.getAttributeOrNone('description')
            stock_db.log_inflows = self.getAttributeOrNone('log_inflows')
            stock_db.categories = self.getAttributeOrNone('categories')
            stock_db.x = self.getAttributeOrNone('x')
            stock_db.y = self.getAttributeOrNone('y')
            stock_db.local_release = self.getAttributeOrNone('local_release')
            
            stock_db.save()
            
            addDBEntityStock(primaryKey, stock_db)
            addDBEntityCompartment(primaryKey, stock_db)

    def extractAttributesExternalListInflow(self, externalListInflow, external_list_inflow):
        for field in externalListInflow['fields']:
            if field['propName'] == 'target':
                self.attributes['target'] = field['valueData']
            elif field['propName'] == 'name':
                self.attributes['name'] = field['valueData']            
            elif field['propName'] == 'startDelay':
                self.attributes['start_delay'] = field['valueData']
            elif field['propName'] == 'derivationDistribution':
                data = field['valueData'][0]
                self.attributes['derivation_distribution'] = self.getDerivationDistribution(data['type'])
                fields = data['fields']
                params = []
                for dictionary in fields:
                    params.append(dictionary['valueData'])
                self.attributes['derivation_parameters'] = ",".join(params)
            elif field['propName'] == 'derivationFactor':
                self.attributes['derivation_factor'] = field['valueData']
            elif field['propName'] == 'singlePeriodInflows':
                singlePeriodInflows = field['valueData']
                index = 0
                for singlePeriodInflow in singlePeriodInflows:
                    data = field['valueData'][index]
                    type = data['type'] 
                    if type == 'fixedValueInflow':
                        self.createFixedValueInflow(data, external_list_inflow)
                    elif type == 'stochasticFunctionInflow':
                        self.createStochasticInflow(data, external_list_inflow)
                    elif type == 'randomChoiceInflow':
                        self.createRandomChoiceInflow(data, external_list_inflow)
                    else:
                        print("Could not set basic inflow of external function inflow")
                    index += 1
        
        for key, value in externalListInflow['position'].items():
            if key == 'x':
                self.attributes['x'] = value
            elif key == 'y':
                self.attributes['y'] = value
        
    def extractAttributesExternalFunctionInflow(self, externalFunctionInflow, external_function_inflow):
        for field in externalFunctionInflow['fields']:
            if field['propName'] == 'target':
                self.attributes['target'] = field['valueData']
            elif field['propName'] == 'name':
                self.attributes['name'] = field['valueData']            
            elif field['propName'] == 'startDelay':
                self.attributes['start_delay'] = field['valueData']
            elif field['propName'] == 'derivationDistribution':
                data = field['valueData'][0]
                self.attributes['derivation_distribution'] = self.getDerivationDistribution(data['type'])
                fields = data['fields']
                params = []
                for dictionary in fields:
                    params.append(dictionary['valueData'])
                self.attributes['derivation_parameters'] = ",".join(params)
            elif field['propName'] == 'derivationFactor':
                self.attributes['derivation_factor'] = field['valueData']
            elif field['propName'] == 'basicInflow':
                # create single period inflow here
                data = field['valueData'][0]
                type = data['type'] 
                if type == 'fixedValueInflow':
                    self.attributes['basic_inflow'] = self.createFixedValueInflow(data, None)
                elif type == 'stochasticFunctionInflow':
                    self.attributes['basic_inflow'] = self.createStochasticInflow(data, None)
                elif type == 'randomChoiceInflow':
                    self.attributes['basic_inflow'] = self.createRandomChoiceInflow(data, None)
                else:
                    print("Could not set basic inflow of external function inflow")
                
        
        for key, value in externalFunctionInflow['position'].items():
            if key == 'x':
                self.attributes['x'] = value
            elif key == 'y':
                self.attributes['y'] = value
                
    def extractAttributesSink(self, sink):
        for field in sink['fields']:
            if field['propName'] == 'name':
                self.attributes['name'] = field['valueData']
            elif field['propName'] == 'description':
                self.attributes['description'] = field['valueData']
            elif field['propName'] == 'logInflows':
                self.attributes['log_inflows'] = field['valueData']
            elif field['propName'] == 'categories':
                dictionaries = field['valueData']
                categories = []
                for dictionary in dictionaries:
                    categories.append(dictionary['fields'][0]['valueData'])
                self.attributes['categories'] = ",".join(categories)
        
        for key, value in sink['position'].items():
            if key == 'x':
                self.attributes['x'] = value
            elif key == 'y':
                self.attributes['y'] = value

    def extractAttributesFlowCompartment(self, flowCompartment):
        for field in flowCompartment['fields']:
            if field['propName'] == 'name':
                self.attributes['name'] = field['valueData']
            elif field['propName'] == 'description':
                self.attributes['description'] = field['valueData']
            elif field['propName'] == 'logInflows':
                self.attributes['log_inflows'] = field['valueData']
            elif field['propName'] == 'categories':
                dictionaries = field['valueData']
                categories = []
                for dictionary in dictionaries:
                    categories.append(dictionary['fields'][0]['valueData'])
                self.attributes['categories'] = ",".join(categories)
            elif field['propName'] == 'adjustOutgoingTcs':
                self.attributes['adjust_outgoing_tcs'] = field['valueData']
            elif field['propName'] == 'logOutflows':
                self.attributes['log_outflows'] = field['valueData']
        
        for key, value in flowCompartment['position'].items():
            if key == 'x':
                self.attributes['x'] = value
            elif key == 'y':
                self.attributes['y'] = value
    
    def extractAttributesStock(self, stock):
        for field in stock['fields']:
            if field['propName'] == 'name':
                self.attributes['name'] = field['valueData']
            elif field['propName'] == 'description':
                self.attributes['description'] = field['valueData']
            elif field['propName'] == 'logInflows':
                self.attributes['log_inflows'] = field['valueData']
            elif field['propName'] == 'categories':
                dictionaries = field['valueData']
                categories = []
                for dictionary in dictionaries:
                    categories.append(dictionary['fields'][0]['valueData'])
                print(str(categories))
                self.attributes['categories'] = ",".join(categories)
            elif field['propName'] == 'adjustOutgoingTcs':
                self.attributes['adjust_outgoing_tcs'] = field['valueData']
            elif field['propName'] == 'logOutflows':
                self.attributes['log_outflows'] = field['valueData']
            elif field['propName'] == 'localRelease':
                # create local release here
                data = field['valueData'][0]
                type = data['type'] 
                if type == 'fixedRateRelease':
                    self.attributes['local_release'] = self.createFixedRateRelease(data)
                elif type == 'listRelease':
                    self.attributes['local_release'] = self.createListRelease(data)
                elif type == 'functionRelease':
                    self.attributes['local_release'] = self.createFunctionRelease(data)
                else:
                    print("Could not set basic inflow of external function inflow")
        
        for key, value in stock['position'].items():
            if key == 'x':
                self.attributes['x'] = value
            elif key == 'y':
                self.attributes['y'] = value
    
    def createFixedRateRelease(self, fixedRateRelease):
        fixed_rate_release = django_models.fixed_rate_release(
            model = self.MODEL_DB,
            name = fixedRateRelease['fields'][0]['valueData'],
            delay = fixedRateRelease['fields'][1]['valueData'],
            release_rate = fixedRateRelease['fields'][2]['valueData']
            )
        
        fixed_rate_release.save()
        
        return fixed_rate_release
    
    def createListRelease(self, listRelease):
        items = listRelease['fields'][2]['valueData']
        tempItems = []
        for dictionary in items:
            tempItems.append(dictionary['fields'][0]['valueData'])
        
        list_release = django_models.list_release(
            model = self.MODEL_DB,
            name = listRelease['fields'][0]['valueData'],
            delay = listRelease['fields'][1]['valueData'],
            release_rate_list = ",".join(tempItems)
            )
        
        list_release.save()
        
        return list_release
    
    def createFunctionRelease(self, functionRelease):
        function = functionRelease['fields'][2]['valueData'][0]
        type = function['type']
        
        parameters = function['fields']
        parameterValues = []
        for dictionary in parameters:
            parameterValues.append(dictionary['valueData'])
        
        function_release = django_models.function_release(
            model = self.MODEL_DB,
            name = functionRelease['fields'][0]['valueData'],
            delay = functionRelease['fields'][1]['valueData'],
            release_function = self.getFunction(type),
            function_parameters = ",".join(parameterValues)
            )
        
        function_release.save()
        
        return function_release
        
    def createFixedValueInflow(self, fixedValueInflow, external_list_inflow):
        fixed_value_inflow = django_models.fixed_value_inflow(
            model = self.MODEL_DB,
            external_list_inflow = external_list_inflow,
            current_value = 0,
            period = 0,
            value = fixedValueInflow['fields'][0]['valueData']
            )
        
        fixed_value_inflow.save()
        
        return fixed_value_inflow
        
    def createStochasticInflow(self, stochasticInflow, external_function_inflow):
        data = stochasticInflow['fields'][0]['valueData']
        type = data[0]['type']
        fields = data[0]['fields']
        
        parameterValues = []
        for dictionary in fields:
            parameterValues.append(dictionary['valueData'])
        
        pdf = self.getDerivationDistribution(type)
        
        stochastic_function_inflow = django_models.stochastic_function_inflow(
            model = self.MODEL_DB,
            external_list_inflow = external_function_inflow,
            current_value = 0,
            period = 0,
            pdf = pdf,
            parameter_values = ",".join(parameterValues),
            )
                 
        stochastic_function_inflow.save()
        
        return stochastic_function_inflow
        
    def createRandomChoiceInflow(self, randomChoiceInflow, external_function_inflow):
        fields = randomChoiceInflow['fields'][0]
        data = fields['valueData']
        samples = []
        for dictonary in data:
            innerFields = dictonary['fields']
            for innerField in innerFields:
                samples.append(innerField['valueData'])
        random_choice_inflow = django_models.random_choice_inflow(
            model = self.MODEL_DB,
            external_list_inflow = external_function_inflow,
            current_value = 0,
            period = 0,
            sample = ",".join(samples)
            )
        
        random_choice_inflow.save()
        
        return random_choice_inflow
    
    def setupInflowTargets(self):
        for id, inflowTarget in getInflowTargets().items():
            
            sourceNode = inflowTarget['sourceNode']
            targetNode = inflowTarget['targetNode']
            
            pkSourceNode = self.getPkOfInflowTarget(sourceNode)
            pkTargetNode = self.   getPkOfInflowTarget(targetNode)

            externalInflowDB = getDBEntityExternalInflow(pkSourceNode)
            
            externalInflowDB.target = getDBEntityCompartment(pkTargetNode)
            
            externalInflowDB.save()
            
    def createDBEntitiesConstantTransfers(self):
        for primaryKey, constantTransfer in getConstantTransfers().items():
            self.attributes = {}
            
            self.extractAttributesConstantTransfer(constantTransfer)
            
            constant_transfer_db = django_models.constant_transfer(
                model = self.MODEL_DB,
                target = self.getAttributeOrNone('target'),
                source_flow_compartment = self.getAttributeOrNone('source_flow_compartment'),
                belongs_to_aggregated_transfer = None,
                name = self.getAttributeOrNone('name'),
                priority = self.getAttributeOrNone('priority'),
                value = self.getAttributeOrNone('value')
                )
            
            constant_transfer_db.save()
            
            addDBEntityConstantTransfer(primaryKey, constant_transfer_db)
            
    def createDBEntitiesRandomChoiceTransfers(self):
        for primaryKey, randomChoiceTransfer in getRandomChoiceTransfers().items():
            self. attributes = {}
            
            self.extractAttributesRandomChoiceTranfers(randomChoiceTransfer)
            
            random_choice_transfer_db = django_models.random_choice_transfer(
                model = self.MODEL_DB,
                target = self.getAttributeOrNone('target'),
                source_flow_compartment = self.getAttributeOrNone('source_flow_compartment'),
                belongs_to_aggregated_transfer = None,
                name = self.getAttributeOrNone('name'),
                priority = self.getAttributeOrNone('priority'),
                sample = self.getAttributeOrNone('sample')
                )
            
            random_choice_transfer_db.save()
            
            addDBEntityRandomChoiceTransfer(primaryKey, random_choice_transfer_db)
            
    def createDBEntitiesStochasticTransfers(self):
        for primaryKey, stochasticTransfer in getStochasticTransfers().items():
            self.attributes = {}
            
            self.extractAttributesStochasticTransfers(stochasticTransfer)
            
            stochastic_transfer_db = django_models.stochastic_transfer(
                model = self.MODEL_DB,
                target = self.getAttributeOrNone('target'),
                source_flow_compartment = self.getAttributeOrNone('source_flow_compartment'),
                belongs_to_aggregated_transfer = None,
                name = self.getAttributeOrNone('name'),
                priority = self.getAttributeOrNone('priority'),
                parameters = self.getAttributeOrNone('parameters'),
                function = self.getAttributeOrNone('function')
                )
            
            stochastic_transfer_db.save()
            
            addDBEntityStochasticTransfer(primaryKey, stochastic_transfer_db)
        
    
    def extractAttributesConstantTransfer(self, constantTransfer):
        for field in constantTransfer['fields']:
            if field['propName'] == 'name':
                self.attributes['name'] = field['valueData']
            elif field['propName'] == 'priority':
                self.attributes['priority'] = field['valueData']
            elif field['propName'] == 'value':
                self.attributes['value'] = field['valueData']
        
        sourceNode = constantTransfer['sourceNode']
        targetNode = constantTransfer['targetNode']
        
        pkSourceNode = self.getPkOfInflowTarget(sourceNode)
        pkTargetNode = self.   getPkOfInflowTarget(targetNode)
        
        sourceCompartment = getDBEntityCompartment(pkSourceNode)
        targetCompartment = getDBEntityCompartment(pkTargetNode)
        
        self.attributes['source_flow_compartment'] = sourceCompartment
        self.attributes['target'] = targetCompartment
        
    def extractAttributesRandomChoiceTranfers(self, randomChoiceTransfer):
        for field in randomChoiceTransfer['fields']:
            if field['propName'] == 'name':
                self.attributes['name'] = field['valueData']
            elif field['propName'] == 'priority':
                self.attributes['priority'] = field['valueData']
            elif field['propName'] == 'sample':
                
                data = field['valueData']
                
                samples = []
                for dictionary in data:
                    samples.append(dictionary['fields'][0]['valueData'])

                self.attributes['sample'] = ",".join(samples)
                
        sourceNode = randomChoiceTransfer['sourceNode']
        targetNode = randomChoiceTransfer['targetNode']
        
        pkSourceNode = self.getPkOfInflowTarget(sourceNode)
        pkTargetNode = self.getPkOfInflowTarget(targetNode)
        
        sourceCompartment = getDBEntityCompartment(pkSourceNode)
        targetCompartment = getDBEntityCompartment(pkTargetNode)
        
        self.attributes['source_flow_compartment'] = sourceCompartment
        self.attributes['target'] = targetCompartment
        
    def extractAttributesStochasticTransfers(self, stochasticTransfer):
        for field in stochasticTransfer['fields']:
            if field['propName'] == 'name':
                self.attributes['name'] = field['valueData']
            elif field['propName'] == 'priority':
                self.attributes['priority'] = field['valueData']
            elif field['propName'] == 'distributionFunction':
                distribution = field['valueData'][0]

                innerFields = distribution['fields']
                
                type = distribution['type']
                self.attributes['function'] = self.getDerivationDistribution(type)
                
                parameterValues = []
                for dictionary in innerFields:
                    parameterValues.append(dictionary['valueData'])
                
                self.attributes['parameters'] = ",".join(parameterValues)
        
        sourceNode = stochasticTransfer['sourceNode']
        targetNode = stochasticTransfer['targetNode']
        
        pkSourceNode = self.getPkOfInflowTarget(sourceNode)
        pkTargetNode = self.getPkOfInflowTarget(targetNode)
        
        sourceCompartment = getDBEntityCompartment(pkSourceNode)
        targetCompartment = getDBEntityCompartment(pkTargetNode)
        
        self.attributes['source_flow_compartment'] = sourceCompartment
        self.attributes['target'] = targetCompartment
            
    def getPkOfInflowTarget(self, node):
        pk = ""
        tempId = node['tempId']
        id = node['id']
        if tempId != None:
            pk += tempId
        if id != None:
            pk += id
        
        return pk
            
    
    def getAttributeOrNone(self, key):
        try:
            attribute = self.attributes[key]
            return attribute
        except:
            return None
        
    def getDerivationDistribution(self, type):
        if type == 'normalDistribution':
            return 'NORM'
        elif type == 'uniformDistribution':
            return 'UNI'
        elif type == 'triangularDistribution':
            return 'TRI'
        elif type == 'exponentialDistribution':
            return 'EXPO'
        print("Could not retrieve derivation distribution for external list inflow")
        
    def getFunction(self, type):
        if type == 'linearFunction':
            return 'LI'
        elif type == 'polynomialFunction':
            return 'PO'
        elif type == 'exponentialFunction':
            return 'EX'
        elif type == 'logarithmicFunction':
            return 'LG'
        elif type == 'sineFunction':
            return 'SI'
        elif type == 'cosineFunction':
            return 'CO'
        
            
    def printData(self):
        print("data:")
        pprint.ppritn(str(self.jsonModel))
        
    def printEntries(self):
        for entry in self.jsonModel:
            print(entry)
    