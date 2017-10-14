from dpmfa.model2json.CategoryFormsField import CategoryFormsField
from dpmfa.model2json.Node import Node


class Sink(Node):

    # name_field = None
    # description_field = None
    # log_inflows_field = None

    # categories_field = None

    def __init__(self, owner):
        super(Sink, self).__init__(owner, 'sink', 'Sink')

        self.enter_classes().append_item('compartment').append_item('sink')

        self.set_max_outgoing(0)
        self.set_min_outgoing(0)
        self.set_min_incoming(1)

        fields = self.enter_fields()
        self.name_field = fields.enter_new_text_field('name', 'Name').set_value('New Sink')
        self.description_field = fields.enter_new_text_field('description', 'Description') \
            .set_display_as_text_area(True).set_not_empty(False)
        self.log_inflows_field = fields.enter_new_check_field('logInflows', 'Log Inflows')
        self.categories_field = fields.append_and_enter(CategoryFormsField(None, 'categories', 'Categories'))

    def configure_for(self, db_entity):
        self.set_node_id('compartment_' + str(db_entity.pk))
        self.set_position(db_entity.x, db_entity.y)

        self.name_field.set_value(db_entity.name)
        self.description_field.set_value(db_entity.description)
        self.log_inflows_field.set_checked(db_entity.log_inflows)
        self.categories_field.set_categories([s.strip() for s in db_entity.categories.split(',')] if (db_entity.categories is not None and db_entity.categories != '') else [])

        return self

    def apply_default_configuration(self):
        self.log_inflows_field.set_checked(True)
        self.categories_field.apply_default_configuration()
        return self

    def enter_name_field(self):
        return self.name_field

    def enter_description_field(self):
        return self.description_field

    def enter_log_inflows_field(self):
        return self.log_inflows_field

    def enter_categories_field(self):
        return self.categories_field
