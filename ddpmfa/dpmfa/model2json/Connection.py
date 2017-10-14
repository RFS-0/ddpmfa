from dpmfa.model2json.FieldList import FieldList
from dpmfa.model2json.Position import Position
from dpmfa.model2json.ValueList import ValueList


class Node(object):
    #owner = None

    #type_name = None
    #type_label = None

    #connection_id = None
    #temp_id = None

    def __init__(self, owner, type_name, type_label):
        self.owner = owner

        self.type_name = type_name
        self.type_label = type_label

        self.connection_id = None
        self.temp_id = None

    def set_type_name(self, type_name):
        self.type_name = type_name
        return self

    def get_type_name(self):
        return self.type_name

    def set_type_label(self, type_label):
        self.tyle_label = type_label
        return self

    def get_type_label(self):
        return self.type_label

    def set_connection_id(self, connection_id):
        self.connection_id = connection_id
        return self

    def get_connection_id(self):
        return self.connection_id

    def set_temp_id(self, temp_id):
        self.temp_id = temp_id
        return self

    def get_temp_if(self):
        return self.temp_id

    def exit(self):
        return self.owner
