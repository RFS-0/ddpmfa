from dpmfa.model2json.CategoryFormsField import CategoryFormsField
from dpmfa.model2json.LocalReleaseFormsField import LocalReleaseFormsField
from dpmfa.model2json.Node import Node


class Stock(Node):

    #name_field = None
    #description_field = None
    #log_inflows_field = None

    #log_outflows_field = None
    #adjust_outgoing_tcs_field = None

    #categories_field = None

    #local_release_field = None

    def __init__(self, owner):
        super(Stock, self).__init__(owner, 'stock', 'Stock')

        self.enter_classes().append_item('compartment').append_item('stock')
        #self.enter_out_connection_types()\
        #    .append_item('constantTransfer')\
        #    .append_item('randomChoiceTransfer')\
        #    .append_item('stochasticTransfer')\
        #    .append_item('aggregatedTransfer')

        self.set_min_outgoing(1)
        self.set_min_incoming(1)

        fields = self.enter_fields()
        self.name_field = fields.enter_new_text_field('name', 'Name').set_value('New Stock')
        self.description_field = fields.enter_new_text_field('description', 'Description')\
            .set_display_as_text_area(True).set_not_empty(False)
        self.log_inflows_field = fields.enter_new_check_field('logInflows', 'Log Inflows')
        self.log_outflows_field = fields.enter_new_check_field('logOutflows', 'Log Outflows')
        self.adjust_outgoing_tcs_field = fields.enter_new_check_field('adjustOutgoingTcs', 'Adjust Outgoing Transfer Coefficients')
        self.categories_field = fields.append_and_enter(CategoryFormsField(None, 'categories', 'Categories'))
        self.local_release_field = fields.append_and_enter(LocalReleaseFormsField(None, 'localRelease', 'Local Release'))

    def configure_for(self, db_entity):
        self.set_node_id(db_entity.pk)
        self.set_position(db_entity.x, db_entity.y)

        self.name_field.set_value(db_entity.name)
        self.description_field.set_value(db_entity.description)
        self.log_inflows_field.set_checked(db_entity.log_inflows)
        self.log_outflows_field.set_checked(db_entity.log_outflows)
        self.adjust_outgoing_tcs_field.set_checked(db_entity.adjust_outgoing_tcs)
        self.categories_field.set_categories([s.strip() for s in db_entity.categories.split(',')] if (db_entity.categories is not None and db_entity.categories != '') else [])

        self.local_release_field.configure_for_stock(db_entity)

        return self

    def apply_default_configuration(self):
        self.log_inflows_field.set_checked(True)
        self.log_outflows_field.set_checked(True)
        self.adjust_outgoing_tcs_field.set_checked(True)
        self.categories_field.apply_default_configuration()
        self.local_release_field.apply_default_configuration()
        return self

    def enter_name_field(self):
        return self.name_field

    def enter_description_field(self):
        return self.description_field

    def enter_log_inflows_field(self):
        return self.log_inflows_field

    def enter_log_outflows_field(self):
        return self.log_outflows_field

    def enter_adjust_outgoing_tcs_field(self):
        return self.adjust_outgoing_tcs_field

    def enter_categories_field(self):
        return self.categories_field
