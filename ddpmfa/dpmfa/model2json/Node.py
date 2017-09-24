from dpmfa.model2json.FieldList import FieldList
from dpmfa.model2json.Position import Position
from dpmfa.model2json.ValueList import ValueList


class Node(object):
    #owner = None

    #type_name = None
    #type_label = None

    #title_label_path = None
    #classes = None
    #out_connection_types = None
    #fields = None

    #title = None
    #node_id = None
    #temp_id = None
    #position = None
    #max_outgoing = -1
    #min_outgoing = 0
    #max_incoming = -1
    #min_incoming = 0
    #dirty = True

    def __init__(self, owner, type_name, type_label):
        self.title = None
        self.node_id = None
        self.temp_id = None
        self.position = None
        self.max_outgoing = -1
        self.min_outgoing = 0
        self.max_incoming = -1
        self.min_incoming = 0
        self.dirty = True

        self.owner = owner
        self.type_name = type_name
        self.type_label = type_label

        self.title_label_path = ValueList(self).append_item('name').append_item('valueData')
        self.classes = ValueList(self)
        self.out_connection_types = ValueList(self)
        self.fields = FieldList(self)

    def get_type_name(self):
        return self.type_name

    def get_type_label(self):
        return self.type_label

    def set_title(self, title):
        self.title = title
        return self

    def get_title(self):
        return self.title

    def enter_title_label_path(self):
        return self.title_label_path

    def set_node_id(self, node_id):
        self.node_id = node_id
        return self

    def get_node_id(self):
        return self.node_id

    def set_temp_id(self, temp_id):
        self.temp_id = temp_id

    def get_temp_id(self):
        return self.temp_id

    def enter_position(self):
        if self.position is None:
            self.position = Position(self)
        return self.position

    def set_position(self, x, y):
        self.position = Position(self).set_x(x).set_y(y)
        return self

    def enter_classes(self):
        return self.classes

    def enter_out_connection_types(self):
        return self.out_connection_types

    def set_max_outgoing(self, max_outgoing):
        self.max_outgoing = max_outgoing
        return self

    def get_max_outgoing(self):
        return self.max_outgoing

    def set_min_outgoing(self, min_outgoing):
        self.min_outgoing = min_outgoing
        return self

    def get_min_outgoing(self):
        return self.min_outgoing

    def set_max_incoming(self, max_incoming):
        self.max_incoming = max_incoming
        return self

    def get_max_incoming(self):
        return self.max_incoming

    def set_min_incoming(self, min_incoming):
        self.min_incoming = min_incoming
        return self

    def get_min_incoming(self):
        return self.min_incoming

    def set_outgoing_bounds(self, min_outgoing, max_outgoing):
        self.min_outgoing = min_outgoing
        self.max_outgoing = max_outgoing
        return self

    def set_incoming_bound(self, min_incoming, max_incoming):
        self.min_incoming = min_incoming
        self.max_incoming = max_incoming
        return self

    def set_dirty(self, dirty):
        self.dirty = dirty

    def get_dirty(self):
        return self.dirty

    def enter_fields(self):
        return self.fields

    def as_dictionary(self):
        return {
            'title': self.title,
            'titleLabelPath': self.title_label_path.as_list(),
            'typeName': self.type_name,
            'typeLabel': self.type_label,
            'id': self.node_id,
            'tempId': self.temp_id,
            'position': self.position.as_dictionary() if self.position is not None else None,
            'classes': self.classes.as_list(),
            'maxOutgoing': self.max_outgoing,
            'minOutgoing': self.min_outgoing,
            'maxIncoming': self.max_incoming,
            'minIncoming': self.min_incoming,
            'outConnectionTypes': self.out_connection_types.as_list(),
            'dirty': self.dirty,
            'fields': self.fields.as_list()
        }

    def set_owner(self, owner):
        self.owner = owner

    def exit(self):
        return self.owner
