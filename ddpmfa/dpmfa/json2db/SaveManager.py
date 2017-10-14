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
    
    def __init__(self, jsonModel):
        self.jsonModel = jsonModel
        self.MODEL_DB = self.getDBModel(jsonModel) 
        
        self.nodes = self.jsonModel['nodes']
        self.connections = self.jsonModel['connections']

        self.separateNodes()
        self.separateConnections()
        
        
        
        self.createDBEntitiesExternalListInflows()
        self.createDBEntitiesExternalFunctionInflows()
        self.createDBEntitiesSink()
        self.createDBEntitiesFlowCompartment()
        self.createDBEntitiesStock()
        
    def getDBModel(self, jsonModel):
        primaryKey = jsonModel['id']
        return django_models.model.objects.get(pk=primaryKey)
           
    def separateNodes(self):
        for node in self.nodes:
            type = node['typeName']
            tempId = node['tempId']
            id = node['id']
            
            primaryKey = ""
            if tempId:
                primaryKey += tempId
            if id:
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
            type = node['typeName']
            tempId = node['tempId']
            id = node['id']
            
            primaryKey = ""
            if tempId:
                primaryKey += tempId
            if id:
                primaryKey += id
                
            if type == CONSTANT_TRANSFER:
                addConstantTransfer(primaryKey, connection)
            elif type == RANDOM_CHOICE_TRANSFER:
                addRandomChoiceTransfer(primaryKey, connection)
            elif type == AGGREGATED_TRANSFER:
                addAggregatedTransfer(primaryKey, connection)
            elif type == STOCHASTIC_TRANSFER:
                addStochasticTransfers(primaryKey, connection)
                
    def createDBEntitiesExternalListInflows(self):
        for primaryKey, externalListInflow in getExternalListInflows().items():
            self.attributes = {}
            
            self.extractAttributesExternalListInflow(externalListInflow)
            external_list_inflow = django_models.external_list_inflow(
                target=self.getAttributeOrNone('target'),
                name=self.getAttributeOrNone('name'),
                start_delay=self.getAttributeOrNone('start_delay'),
                derivation_distribution=self.getAttributeOrNone('derivation_distribution'),
                derivation_parameters=self.getAttributeOrNone('derivation_parameters'),
                derivation_factor=self.getAttributeOrNone('derivation_factor'),
                x=self.getAttributeOrNone('x'),
                y=self.getAttributeOrNone('y')
                )
            external_list_inflow.save()
            addDBEntityExternalListInflow(primaryKey, external_list_inflow)

    def createDBEntitiesExternalFunctionInflows(self):
        for primaryKey, externalFunctionInflow in getExternalFunctionInflows().items():
            self.attributes = {}
            
            external_function_inflow = django_models.external_function_inflow()
            external_function_inflow.save()
            
            self.extractAttributesExternalFunctionInflow(externalFunctionInflow, external_function_inflow)
            
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
            
    def createDBEntitiesSink(self):
        for primaryKey, sink in getSinks().items():
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

    def createDBEntitiesFlowCompartment(self):
        for primaryKey, flowCompartment in getFlowCompartments().items():
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
            
    def createDBEntitiesStock(self):
        for primaryKey, stock in getStocks().items():
            self.attributes = {}
            
            stock_db = django_models.stock()
            stock_db.save()
            
            self.extractAttributesStock(stock)

    def extractAttributesExternalListInflow(self, externalListInflow):
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
                    self.attributes['basic_inflow'] = self.createFixedValueInflow(data, external_function_inflow)
                elif type == 'stochasticFunctionInflow':
                    self.attributes['basic_inflow'] = self.createStochasticInflow(data, external_function_inflow)
                elif type == 'randomChoiceInflow':
                    self.attributes['basic_inflow'] = self.createRandomChoiceInflow(data, external_function_inflow)
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
        pprint.pprint(stock)

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
        pprint.pprint(fixedRateRelease)
        fixed_rate_release = django_models.fixed_rate_release(
            name = fixedRateRelease['fields'][0]['valueData'],
            delay = fixedRateRelease['fields'][1]['valueData'],
            release_rate = fixedRateRelease['fields'][2]['valueData']
            )
        fixed_rate_release.save()
        return fixed_rate_release
    
    def createListRelease(self, listRelease):
        pprint.pprint(listRelease)
        items = listRelease['fields'][2]['valueData']
        for dictionary in items:
            items.append(dictionary['fields'][0]['valueData'])
        list_release = django_models.list_release(
            name = listRelease['fields'][0]['valueData'],
            delay = listRelease['fields'][1]['valueData'],
            release_rate_list = ",".join(items)
            )
        list_release.save()
        return list_release
    
    def createFunctionRelease(self, functionRelease):
        pprint.pprint(functionRelease)
        
        type = functionRelease['fields'][2]['type']
        
        parameters = data[3]['fields']
        parameterValues = []
        for dictionary in parameters:
            parameterValues.append(dictionary['valueData'])
        
        function_release = django_models.function_release(
            name = functionRelease['fields'][0]['valueData'],
            delay = functionRelease['fields'][1]['valueData'],
            release_function = getFunction(type),
            function_parameters = ",".join(parameterValues)
            )
        
    def createFixedValueInflow(self, fixedValueInflow, external_function_inflow):
        fixed_value_inflow = django_models.fixed_value_inflow(
            external_list_inflow = external_function_inflow,
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
            external_list_inflow = external_function_inflow,
            current_value = 0,
            period = 0,
            sample = ",".join(samples)
            )
        
        random_choice_inflow.save()
        
        return random_choice_inflow
        
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
        if type == 'linear':
            return 'LI'
        elif type == 'polynomial':
            return 'PO'
        elif type == 'exponential':
            return 'EX'
        elif type == 'logarithmic':
            return 'LG'
        elif type == 'sine':
            return 'SI'
        elif type == 'cosine':
            return 'CO'
        
            
    def printData(self):
        print("data:")
        pprint.ppritn(str(self.jsonModel))
        
    def printEntries(self):
        for entry in self.jsonModel:
            print(entry)
    