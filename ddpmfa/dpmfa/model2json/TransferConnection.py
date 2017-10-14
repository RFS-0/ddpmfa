from dpmfa.model2json.Connection import Connection
from dpmfa.model2json.ValueList import ValueList


class TransferConnection(Connection):

    # name_field
    # priority_field

    def __init__(self, owner, type_name, type_label):
        super(TransferConnection, self).__init__(owner, type_name, type_label)
        self.title_label_path = ValueList(self).append_item('name').append_item('valueData')

        fields = self.enter_fields()
        self.name_field = fields.enter_new_text_field('name', 'Name').set_value('New Transfer')
        self.priority_field = fields.enter_new_text_field('priority', 'Priority')\
            .enter_number_config() \
                .enter_min_bound().set_value(0).set_inclusive(True).exit()\
            .exit()

    def set_name(self, value):
        self.name_field.set_value(value)
        return self

    def set_priority(self, priority):
        self.priority_field.set_value(priority)
        return self
