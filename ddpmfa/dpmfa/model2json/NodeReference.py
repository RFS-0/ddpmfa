class NodeReference(object):

    #node_id
    #temp_id

    def __init__(self, owner):
        self.node_id = None
        self.temp_id = None

    def get_node_id(self):
        return self.node_id

    def set_node_id(self, node_id):
        self.node_id = node_id
        return self

    def get_temp_id(self):
        return self.temp_id

    def set_temp_id(self, temp_id):
        self.temp_id = temp_id
        return self

    def as_dictionary(self):
        return {
            'id': self.node_id,
            'tempId': self.temp_id
        }

    def exit(self):
        return self.owner
