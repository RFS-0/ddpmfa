from dpmfa.model2json.TransferConnection import TransferConnection
from dpmfa.model2json.ValueList import ValueList


class RandomChoiceTransferConnection(TransferConnection):

    # sample_field

    def __init__(self, owner):
        super(RandomChoiceTransferConnection, self).__init__(owner, 'randomChoiceTransfer', 'Random Choice Transfer')

        fields = self.enter_fields()
        self.sample_field = self.fields.enter_new_forms_field('sample', 'Sample').set_min_forms(1)
        self.__add_item_form(self.sample_field.enter_form_definitions(), '0')

    def __add_item_form(self, form_list, value):
        return form_list.enter_new_form('item', 'Item')\
            .enter_title_template().clear().append_item('Item ').append_item('positionOneBased').exit()\
            .enter_fields()\
                .enter_new_text_field('value', 'Value').set_value(value).exit()\
            .exit()

    def set_values(self, values):
        value_forms = self.sample_field.enter_value_forms().clear()
        for value in values:
            self.__add_item_form(value_forms, str(value))
        return self

    def apply_default_configuration(self):
        self.set_name('New Random Choice Transfer')
        self.set_priority(0)
        self.set_values([0.5])
        return self

    def configure_for(self, db_entity):
        self.set_source_node_id('compartment_' + str(db_entity.source_flow_compartment.pk))
        self.set_target_node_id('compartment_' + str(db_entity.target.pk))
        self.set_name(db_entity.name)
        self.set_priority(db_entity.priority)
        self.set_values([s.strip() for s in db_entity.sample.split(',')] if (db_entity.sample is not None and db_entity.sample != '') else [])
        return self
