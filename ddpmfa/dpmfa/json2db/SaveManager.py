



#==============================================================================
#  Package variables
#==============================================================================

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

# Compartments

def getDBEntityOfCompartment(primaryKey):
    return compartments_DB.get(primaryKey)

def setDBEntityOfCompartment(primaryKey, DBEntity):
    compartments_DB[primaryKey] = DBEntity

def getDBEntityOfFlowCompartment(primaryKey):
    return flow_compartments_DB.get(primaryKey)

def setDBEntityOfFlowCompartment(primaryKey, DBEntity):
    flow_compartments_DB[primaryKey] = DBEntity

def getDBEntityOfSink(primaryKey):
    return sinks_DB.get(primaryKey)

def setDBEntityOfSink(primaryKey, DBEntity):
    sinks_DB[primaryKey] = DBEntity

def getDBEntityOfStock(primaryKey):
    return stocks_DB.get(primaryKey)

def setDBEntityOfStock(primaryKey, DBEntity):
    stocks_DB[primaryKey] = DBEntity

# Transfers

def getDBEntityOfTransfer(primaryKey):
    return transfers_DB.get(primaryKey)

def setDBEntityOfTransfer(primaryKey, DBEntity):
    transfers_DB[primaryKey] = DBEntity
    
def getDBEntityOfConstantTransfer(primaryKey):
    return constant_transfers_DB.get(primaryKey)

def setDBEntityOfConstantTransfer(primaryKey, DBEntity):
    constant_transfers_DB[primaryKey] = DBEntity
    
def getDBEntityOfStochasticTransfer(primaryKey):
    return stochastic_transfers_DB.get(primaryKey)

def setDBEntityOfStochasticTransfer(primaryKey, DBEntity):
    stochastic_transfers_DB[primaryKey] = DBEntity
    
def getDBEntityOfRandomChoiceTransfer(primaryKey):
    return random_choice_transfers_DB.get(primaryKey)

def setDBEntityOfRandomChoiceTransfer(primaryKey, DBEntity):
    random_choice_transfers_DB[primaryKey] = DBEntity
    
def getDBEntityOfAggregatedTransfer(primaryKey):
    return aggregated_transfers_DB.get(primaryKey)

def setDBEntityOfAggregatedTransfer(primaryKey, DBEntity):
    aggregated_transfers_DB[primaryKey] = DBEntity

# Releases

def getDBEntityOfLocalRelease(primaryKey):
    return local_releases_DB.get(primaryKey)

def setDBEntityOfLocalRelease(primaryKey, DBEntity):
    local_releases_DB[primaryKey] = DBEntity

def getDBEntityOfFixedRateRelease(primaryKey):
    return fixed_rate_releases_DB.get(primaryKey)

def setDBEntityOfFixedRateRelease(primaryKey, DBEntity):
    fixed_rate_releases_DB[primaryKey] = DBEntity

def getDBEntityOfListRelease(primaryKey):
    return list_releases_DB.get(primaryKey)

def setDBEntityOfListRelease(primaryKey, DBEntity):
    list_releases_DB[primaryKey] = DBEntity

def getDBEntityOfFunctionRelease(primaryKey):
    return function_releases_DB.get(primaryKey)

def setDBEntityOfFunctionRelease(primaryKey, DBEntity):
    function_releases_DB[primaryKey] = DBEntity

# Single Period Inflows

def getDBEntityOfSinglePeriodInflow(primaryKey):
    return single_period_inflows_DB.get(primaryKey)

def setDBEntityOfSinglePeriodInflow(primaryKey, DBEntity):
    single_period_inflows_DB[primaryKey] = DBEntity

def getDBEntityOfStochasticFunctionInflow(primaryKey):
    return stochastic_function_inflows_DB.get(primaryKey)

def setDBEntityOfStochasticFunctionInflow(primaryKey, DBEntity):
    stochastic_function_inflows_DB[primaryKey] = DBEntity

def getDBEntityOfRandomChoiceInflow(primaryKey):
    return random_choice_inflows_DB.get(primaryKey)

def setDBEntityOfRandomChoiceInflow(primaryKey, DBEntity):
    random_choice_inflows_DB[primaryKey] = DBEntity

def getDBEntityOfFixedValueInflow(primaryKey):
    return fixed_value_inflows_DB.get(primaryKey)

def setDBEntityOfFixedValueInflow(primaryKey, DBEntity):
    fixed_value_inflows_DB[primaryKey] = DBEntity
    
# External Inflows
    
def getDBEntityOfExternalInflow(primaryKey):
    return external_inflows_DB.get(primaryKey)

def setDBEntityOfExternalInflow(primaryKey, DBEntity):
    external_inflows_DB[primaryKey] = DBEntity
    
def getDBEntityOfExternalListInflow(primaryKey):
    return external_list_inflows_DB.get(primaryKey)

def setDBEntityOfExternalListInflow(primaryKey, DBEntity):
    external_list_inflows_DB[primaryKey] = DBEntity
    
def getDBEntityOfExternalFunctionInflow(primaryKey):
    return external_function_inflows_DB.get(primaryKey)

def setDBEntityOfExternalFunctionInflow(primaryKey, DBEntity):
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
        print("type: " + str(type(jsonModel)))
        print("data")
        print(str(jsonModel))
        
    
class CompartmentConver(object):
    
    def __init__(self, jsonCompartment):
        self.json_entity = jsonCompartment
        self.compNumber = db_compartment.pk
        self.name = db_compartment.name
        self.logInflows = db_compartment.log_inflows
        
    def parseCompartmentNumber(self):
        pass
    