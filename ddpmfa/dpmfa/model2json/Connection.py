from dpmfa.model2json.NodeReference import NodeReference
from dpmfa.model2json.FieldList import FieldList
from dpmfa.model2json.ValueList import ValueList

class Connection(object):

    def __init__(self, owner, type_name, type_label):
        self.owner = owner

        self.type_name = type_name
        self.type_label = type_label

        self.connection_id = None
        self.temp_id = None

        self.title = ''
        self.title_label_path = None

        self.target_node = None
        self.source_node = None

        self.fields = FieldList(self)

        self.dirty = True

    def apply_default_configuration(self):
        return self

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def enter_title_label_path(self):
        if self.title_label_path is None:
            self.title_label_path = ValueList(self)
        return self.title_label_path

    def set_type_name(self, type_name):
        self.type_name = type_name
        return self

    def enter_source_node(self):
        if self.source_node is None:
            self.source_node = NodeReference(self)
        return self.source_node

    def enter_target_node(self):
        if self.target_node is None:
            self.target_node = NodeReference(self)
        return self.target_node

    def set_source_node_id(self, node_id):
        self.enter_source_node().set_node_id(node_id)
        return self

    def set_target_node_id(self, node_id):
        self.enter_target_node().set_node_id(node_id)
        return self

    def get_type_name(self):
        return self.type_name

    def set_type_label(self, type_label):
        self.type_label = type_label
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

    def enter_fields(self):
        return self.fields

    def as_dictionary(self):
        return {
            'title': self.title,
            'titleLabelPath': self.title_label_path.as_list() if self.title_label_path is not None else None,
            'typeName': self.type_name,
            'typeLabel': self.type_label,
            'id': self.connection_id,
            'tempId': self.temp_id,
            'targetNode': self.target_node.as_dictionary() if self.target_node is not None else None,
            'sourceNode': self.source_node.as_dictionary() if self.source_node is not None else None,
            'dirty': self.dirty,
            'fields': self.fields.as_list()
        }

    def exit(self):
        return self.owner
