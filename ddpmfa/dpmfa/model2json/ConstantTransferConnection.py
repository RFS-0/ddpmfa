from dpmfa.model2json.TransferConnection import TransferConnection
from dpmfa.model2json.ValueList import ValueList


class ConstantTransferConnection(TransferConnection):

    # value_field

    def __init__(self, owner):
        super(ConstantTransferConnection, self).__init__(owner, 'constantTransfer', 'Constant Transfer')

        fields = self.enter_fields()
        self.value_field = fields.enter_new_text_field('value', 'Value')\
            .enter_number_config()\
                .enter_min_bound()\
                    .set_value(0)\
                    .set_inclusive(True)\
                .exit()\
                .enter_max_bound()\
                    .set_value(1)\
                    .set_inclusive(True)\
                .exit()\
            .exit()

    def apply_default_configuration(self):
        self.set_name('New Constant Transfer')
        self.set_priority(0)
        self.set_value(0.5)
        return self

    def configure_for(self, db_entity):
        self.set_source_node_id('compartment_' + str(db_entity.source_flow_compartment.pk))
        self.set_target_node_id('compartment_' + str(db_entity.target.pk))
        self.set_name(db_entity.name)
        self.set_priority(db_entity.priority)
        self.set_value(db_entity.value)
        return self

    def set_value(self, value):
        self.value_field.set_value(value)
