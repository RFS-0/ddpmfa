from dpmfa import models as dbm
from dpmfa.model2json.ExternalFunctionInflow import ExternalFunctionInflow
from dpmfa.model2json.ExternalListInflow import ExternalListInflow
from dpmfa.model2json.FlowCompartment import FlowCompartment

class Model(object):

    #model_id = None
    #valid = True
    #cycles_allowed = False
    #parallels_allowed = False
    #nodes = []
    #node_types = []
    #connections = []
    #connection_types = []

    def __init__(self):
        self.model_id = None
        self.valid = True
        self.cycles_allowed = False
        self.parallels_allowed = False
        self.nodes = []
        self.node_types = []
        self.connections = []
        self.connection_types = []

    def configure_for(self, db_entity):
        self.model_id = db_entity.pk

        self.node_types.append(ExternalListInflow(self).apply_default_configuration())
        self.node_types.append(FlowCompartment(self).apply_default_configuration())

        for db_inflow in dbm.external_list_inflow.objects.filter(target__model=db_entity):
            self.nodes.append(ExternalListInflow(self).configure_for(db_inflow))

        for db_inflow in dbm.external_function_inflow.objects.filter(target__model=db_entity):
            self.nodes.append(ExternalFunctionInflow(self).configure_for(db_inflow))

        for db_flow_compartment in dbm.flow_compartment.objects.filter(model=db_entity):
            db_stocks = dbm.stock.objects.filter(pk=db_flow_compartment.pk)
            if db_stocks.count() == 0:
                self.nodes.append(FlowCompartment(self).configure_for(db_flow_compartment))
            else:
                #TODO: stocks
                print('TODO')


        return self

    def set_model_id(self, model_id):
        self.model_id = model_id
        return self

    def get_model_id(self):
        return self.model_id

    def set_valid(self, valid):
        self.valid = valid
        return self

    def get_valid(self):
        return self.valid

    def set_cycles_allowed(self, cycles_allowed):
        self.cycles_allowed = cycles_allowed
        return self

    def get_cycles_allowed(self):
        return self.cycles_allowed

    def set_parallels_allowed(self, parallels_allowed):
        self.parallels_allowed = parallels_allowed
        return self

    def get_parallels_allowed(self):
        return self.parallels_allowed

    def get_nodes(self):
        return self.nodes

    def get_node_types(self):
        return self.node_types

    def get_connections(self):
        return self.connections

    def get_connection_types(self):
        return self.connection_types

    def as_dictionary(self):
        return {
            'id': self.model_id,
            'valid': self.valid,
            'cyclesAllowed': self.cycles_allowed,
            'parallelsAllowed': self.parallels_allowed,
            'nodes': [node.as_dictionary() for node in self.nodes],
            'nodeTypes': [node_type.as_dictionary() for node_type in self.node_types],
            'connections': [connection.as_dictionary() for connection in self.connections],
            'connectionTypes': [connection_type.as_dictionary() for connection_type in self.connection_types]
        }
