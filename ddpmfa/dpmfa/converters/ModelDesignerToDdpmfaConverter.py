#python
import pprint

# django
import dpmfa.models as django_models

# dpmfa
from dpmfa.dpmfa_simulator_0_921.dpmfa_simulator.components import ExternalListInflow

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

#==============================================================================
#  Package functions
#==============================================================================



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
        
        self.externalListInflows = {}
        self.externalFunctionInflows = {}
        
        self.flowCompartments = {}
        self.stocks = {}
        self.sinks = {}
        
        self.constantTransfers = {}
        self.randomChoiceTransfers = {}
        self.aggregatedTransfers = {}
        self.stochasticTransfers = {}
        
        self.inflowTargets = {}
        
        self.compartments_DB = {}
        self.flow_compartments_DB = {}
        self.sinks_DB = {}
        self.stocks_DB = {}
        self.transfers_DB = {}
        self.constant_transfers_DB = {}
        self.stochastic_transfers_DB = {}
        self.random_choice_transfers_DB = {}
        self.aggregated_transfers_DB = {}
        self.local_releases_DB = {}
        self.fixed_rate_releases_DB = {}
        self.list_releases_DB = {}
        self.function_releases_DB = {}
        self.single_period_inflows_DB = {}
        self.stochastic_function_inflows_DB = {}
        self.random_choice_inflows_DB = {}
        self.fixed_value_inflows_DB = {}
        self.external_inflows_DB = {}
        self.external_list_inflows_DB = {}
        self.external_function_inflows_DB = {}
        
    def recreateDBModel(self, model_pk):
        
        old_model = django_models.model.objects.get(pk=model_pk)
        
        pk = old_model.pk
        project = old_model.project
        name = old_model.name
        description = old_model.description
        
        # delete all everything that relates to the old model except model instances, experiments and results
        for compartment in django_models.compartment.objects.filter(model = old_model):
            compartment.delete()
            
        for localRelease in django_models.local_release.objects.filter(model = old_model):
            localRelease.delete()
            
        for transfer in django_models.transfer.objects.filter(model = old_model):
            transfer.delete()
            
        for externalInflow in django_models.external_inflow.objects.filter(model = old_model):
            externalInflow.delete()
            
        for singlePeriodInflow in django_models.single_period_inflow.objects.filter(model = old_model):
            singlePeriodInflow.delete()
        
        old_model.delete()
        
        
        new_model = django_models.model(
            pk = pk,
            project = project,
            name = name,
            description = description)
        
        new_model.save()
        
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
        generatedPrimaryKey = 0
        for node in self.nodes:
            
            type = node['typeName']
            tempId = node['tempId']
            id = node['id']
            
            primaryKey = ""
            if id != None:
                primaryKey += id
            elif tempId != None:
                primaryKey += tempId
            else:
                primaryKey = generatedPrimaryKey
                generatedPrimaryKey += 1
                
            if type == EXTERNAL_LIST_INFLOW:
                self.addExternalListInflow(primaryKey, node)
            elif type == EXTERNAL_FUNCTION_INFLOW:
                self.addExternalFunctionInflow(primaryKey, node)
            elif type == FLOW_COMPARTMENT:
                self.addFlowCompartment(primaryKey, node)
            elif type == STOCK:
                self.addStock(primaryKey, node)
            elif type == SINK:
                self.addSink(primaryKey, node)
                
    def separateConnections(self):
        generatedPrimaryKey = 0
        for connection in self.connections:
            
            type = connection['typeName']
            tempId = connection['tempId']
            id = connection['id']
            
            primaryKey = ""
            if id != None:
                primaryKey += id
            elif tempId != None:
                primaryKey += tempId
            else:
                primaryKey = generatedPrimaryKey
                generatedPrimaryKey += 1
                
            if type == CONSTANT_TRANSFER:
                self.addConstantTransfer(primaryKey, connection)
            elif type == RANDOM_CHOICE_TRANSFER:
                self.addRandomChoiceTransfer(primaryKey, connection)
            elif type == AGGREGATED_TRANSFER:
                self.addAggregatedTransfer(primaryKey, connection)
            elif type == STOCHASTIC_TRANSFER:
                self.addStochasticTransfers(primaryKey, connection)
            elif type == INFLOW_TARGET:
                self.addInflowTarget(primaryKey, connection)
                
    def createDBEntitiesExternalListInflows(self):
        for primaryKey, externalListInflow in self.getExternalListInflows().items():
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
            
            self.addDBEntityExternalListInflow(primaryKey, external_list_inflow)
            self.addDBEntityExternalInflow(primaryKey, external_list_inflow)

    def createDBEntitiesExternalFunctionInflows(self):
        for primaryKey, externalFunctionInflow in self.getExternalFunctionInflows().items():
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
            
            self.addDBEntityExternalFunctionInflow(primaryKey, external_function_inflow)
            self.addDBEntityExternalInflow(primaryKey, external_function_inflow)
            
    def createDBEntitiesSink(self):
        for primaryKey, sink in self.getSinks().items():
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
            
            self.addDBEntitySink(primaryKey, sink_db)
            self.addDBEntityCompartment(primaryKey, sink_db)

    def createDBEntitiesFlowCompartment(self):
        for primaryKey, flowCompartment in self.getFlowCompartments().items():
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
            
            self.addDBEntityFlowCompartment(primaryKey, flow_compartment_db)
            self.addDBEntityCompartment(primaryKey, flow_compartment_db)
            
    def createDBEntitiesStock(self):
        for primaryKey, stock in self.getStocks().items():
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
            
            self.addDBEntityStock(primaryKey, stock_db)
            self.addDBEntityCompartment(primaryKey, stock_db)

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
        for id, inflowTarget in self.getInflowTargets().items():
            
            sourceNode = inflowTarget['sourceNode']
            targetNode = inflowTarget['targetNode']
            
            pkSourceNode = self.getPkOfInflowTarget(sourceNode)
            pkTargetNode = self.getPkOfInflowTarget(targetNode)

            externalInflowDB = self.getDBEntityExternalInflow(pkSourceNode)
            
            externalInflowDB.target = self.getDBEntityCompartment(pkTargetNode)
            
            externalInflowDB.save()
            
    def createDBEntitiesConstantTransfers(self):
        for primaryKey, constantTransfer in self.getConstantTransfers().items():
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
            
            self.addDBEntityConstantTransfer(primaryKey, constant_transfer_db)
            
    def createDBEntitiesRandomChoiceTransfers(self):
        for primaryKey, randomChoiceTransfer in self.getRandomChoiceTransfers().items():
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
            
            self.addDBEntityRandomChoiceTransfer(primaryKey, random_choice_transfer_db)
            
    def createDBEntitiesStochasticTransfers(self):
        for primaryKey, stochasticTransfer in self.getStochasticTransfers().items():
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
            
            self.addDBEntityStochasticTransfer(primaryKey, stochastic_transfer_db)
        
    
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
        pkTargetNode = self.getPkOfInflowTarget(targetNode)
        
        sourceCompartment = self.getDBEntityCompartment(pkSourceNode)
        targetCompartment = self.getDBEntityCompartment(pkTargetNode)
        
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
        
        sourceCompartment = self.getDBEntityCompartment(pkSourceNode)
        targetCompartment = self.getDBEntityCompartment(pkTargetNode)
        
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
                    parameterValues.append(str(dictionary['valueData']))
                
                self.attributes['parameters'] = ",".join(parameterValues)
        
        sourceNode = stochasticTransfer['sourceNode']
        targetNode = stochasticTransfer['targetNode']
        
        pkSourceNode = self.getPkOfInflowTarget(sourceNode)
        pkTargetNode = self.getPkOfInflowTarget(targetNode)
        
        sourceCompartment = self.getDBEntityCompartment(pkSourceNode)
        targetCompartment = self.getDBEntityCompartment(pkTargetNode)
        
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
        
    # JSON
    def addExternalListInflow(self, primaryKey, externalListInflow):
        self.externalListInflows[primaryKey] = externalListInflow
    
    def getExternalListInflow(self, primaryKey):
        return self.externalListInflows.get(primaryKey)
    
    def getExternalListInflows(self):
        return self.externalListInflows
    
    def addExternalFunctionInflow(self, primaryKey, externalFunctionInflow):
        self.externalFunctionInflows[primaryKey] = externalFunctionInflow
    
    def getExternalFunctionInflow(self, primaryKey):
        return self.externalFunctionInflows.get(primaryKey)
    
    def getExternalFunctionInflows(self):
        return self.externalFunctionInflows
    
    def addFlowCompartment(self, primaryKey, flowCompartment):
        self.flowCompartments[primaryKey] = flowCompartment
    
    def getFlowCompartment(self, primaryKey):
        return self.flowCompartments.get(primaryKey)
    
    def getFlowCompartments(self):
        return self.flowCompartments
    
    def addStock(self, primaryKey, stock):
        self.stocks[primaryKey] = stock
    
    def getStock(self, primaryKey):
        return self.stocks.get(primaryKey)
    
    def getStocks(self):
        return self.stocks
    
    def addSink(self, primaryKey, sink):
        self.sinks[primaryKey] = sink
    
    def getSink(self, primaryKey):
        return self.sinks.get(primaryKey)
    
    def getSinks(self):
        return self.sinks
    
    def addConstantTransfer(self, primaryKey, constantTransfer):
        self.constantTransfers[primaryKey] = constantTransfer
    
    def getConstantTransfer(self, primaryKey):
        return self.constantTransfers.get(primaryKey)
    
    def getConstantTransfers(self):
        return self.constantTransfers
    
    def addRandomChoiceTransfer(self, primaryKey, randomChoiceTransfer):
        self.randomChoiceTransfers[primaryKey] = randomChoiceTransfer
    
    def getRandomChoiceTransfer(self, primaryKey):
        return self.randomChoiceTransfers.get(primaryKey)
    
    def getRandomChoiceTransfers(self):
        return self.randomChoiceTransfers
    
    def addAggregatedTransfer(self, primaryKey, aggregatedTransfer):
        self.aggregatedTransfers[primaryKey] = aggregatedTransfer
    
    def getAggregatedTransfer(self, primaryKey):
        return self.aggregatedTransfers.get(primaryKey)
    
    def getAggregatedTransfers(self):
        return self.aggregatedTransfers
    
    def addStochasticTransfers(self, primaryKey, stochasticTransfer):
        self.stochasticTransfers[primaryKey] = stochasticTransfer
    
    def getStochasticTransfer(self, primaryKey):
        return self.stochasticTransfers.get(primaryKey)
    
    def getStochasticTransfers(self):
        return self.stochasticTransfers
    
    def addInflowTarget(self, primaryKey, inflowTarget):
        self.inflowTargets[primaryKey] = inflowTarget
        
    def getInflowTargets(self):
        return self.inflowTargets
    
    def getInflowTarget(self, primaryKey):
        return self.inflowTargets[primaryKey]
    
    # Compartments
    
    def getDBEntityCompartment(self, primaryKey):
        return self.compartments_DB.get(primaryKey)
    
    def addDBEntityCompartment(self, primaryKey, DBEntity):
        self.compartments_DB[primaryKey] = DBEntity
    
    def getDBEntityFlowCompartment(self, primaryKey):
        return self.flow_compartments_DB.get(primaryKey)
    
    def addDBEntityFlowCompartment(self, primaryKey, DBEntity):
        self.flow_compartments_DB[primaryKey] = DBEntity
    
    def getDBEntitySink(self, primaryKey):
        return self.sinks_DB.get(primaryKey)
    
    def addDBEntitySink(self, primaryKey, DBEntity):
        self.sinks_DB[primaryKey] = DBEntity
    
    def getDBEntityStock(self, primaryKey):
        return self.stocks_DB.get(primaryKey)
    
    def addDBEntityStock(self, primaryKey, DBEntity):
        self.stocks_DB[primaryKey] = DBEntity
    
    # Transfers
    
    def getDBEntityTransfer(self, primaryKey):
        return self.transfers_DB.get(primaryKey)
    
    def addDBEntityTransfer(self, primaryKey, DBEntity):
        self.transfers_DB[primaryKey] = DBEntity
        
    def getDBEntityConstantTransfer(self, primaryKey):
        return self.constant_transfers_DB.get(primaryKey)
    
    def addDBEntityConstantTransfer(self, primaryKey, DBEntity):
        self.constant_transfers_DB[primaryKey] = DBEntity
        
    def getDBEntityStochasticTransfer(self, primaryKey):
        return self.stochastic_transfers_DB.get(primaryKey)
    
    def addDBEntityStochasticTransfer(self, primaryKey, DBEntity):
        self.stochastic_transfers_DB[primaryKey] = DBEntity
        
    def getDBEntityRandomChoiceTransfer(self, primaryKey):
        return self.random_choice_transfers_DB.get(primaryKey)
    
    def addDBEntityRandomChoiceTransfer(self, primaryKey, DBEntity):
        self.random_choice_transfers_DB[primaryKey] = DBEntity
        
    def getDBEntityAggregatedTransfer(self, primaryKey):
        return self.aggregated_transfers_DB.get(primaryKey)
    
    def addDBEntityAggregatedTransfer(self, primaryKey, DBEntity):
        self.aggregated_transfers_DB[primaryKey] = DBEntity
    
    # Releases
    
    def getDBEntityLocalRelease(self, primaryKey):
        return self.local_releases_DB.get(primaryKey)
    
    def addDBEntityLocalRelease(self, primaryKey, DBEntity):
        self.local_releases_DB[primaryKey] = DBEntity
    
    def getDBEntityFixedRateRelease(self, primaryKey):
        return self.fixed_rate_releases_DB.get(primaryKey)
    
    def addDBEntityFixedRateRelease(self, primaryKey, DBEntity):
        self.fixed_rate_releases_DB[primaryKey] = DBEntity
    
    def getDBEntityListRelease(self, primaryKey):
        return self.list_releases_DB.get(primaryKey)
    
    def addDBEntityListRelease(self, primaryKey, DBEntity):
        self.list_releases_DB[primaryKey] = DBEntity
    
    def getDBEntityFunctionRelease(self, primaryKey):
        return self.function_releases_DB.get(primaryKey)
    
    def addDBEntityFunctionRelease(self, primaryKey, DBEntity):
        self.function_releases_DB[primaryKey] = DBEntity
    
    # Single Period Inflows
    
    def getDBEntitySinglePeriodInflow(self, primaryKey):
        return self.single_period_inflows_DB.get(primaryKey)
    
    def addDBEntitySinglePeriodInflow(self, primaryKey, DBEntity):
        self.single_period_inflows_DB[primaryKey] = DBEntity
    
    def getDBEntityStochasticFunctionInflow(self, primaryKey):
        return self.stochastic_function_inflows_DB.get(primaryKey)
    
    def addDBEntityStochasticFunctionInflow(self, primaryKey, DBEntity):
        self.stochastic_function_inflows_DB[primaryKey] = DBEntity
    
    def getDBEntityRandomChoiceInflow(self, primaryKey):
        return self.random_choice_inflows_DB.get(primaryKey)
    
    def addDBEntityRandomChoiceInflow(self, primaryKey, DBEntity):
        self.random_choice_inflows_DB[primaryKey] = DBEntity
    
    def getDBEntityFixedValueInflow(self, primaryKey):
        return self.fixed_value_inflows_DB.get(primaryKey)
    
    def addDBEntityFixedValueInflow(self, primaryKey, DBEntity):
        self.fixed_value_inflows_DB[primaryKey] = DBEntity
        
    # External Inflows
        
    def getDBEntityExternalInflow(self, primaryKey):
        return self.external_inflows_DB.get(primaryKey)
    
    def addDBEntityExternalInflow(self, primaryKey, DBEntity):
        self.external_inflows_DB[primaryKey] = DBEntity
        
    def getDBEntityExternalListInflow(self, primaryKey):
        return self.external_list_inflows_DB.get(primaryKey)
    
    def addDBEntityExternalListInflow(self, primaryKey, DBEntity):
        self.external_list_inflows_DB[primaryKey] = DBEntity
        
    def getDBEntityExternalFunctionInflow(self, primaryKey):
        return self.external_function_inflows_DB.get(primaryKey)
    
    def addDBEntityExternalFunctionInflow(self, primaryKey, DBEntity):
        self.external_function_inflows_DB[primaryKey] = DBEntity
        
    def printData(self):
        print("data:")
        pprint.pprint(str(self.jsonModel))
        
    def printEntries(self):
        for entry in self.jsonModel:
            print(entry)
    