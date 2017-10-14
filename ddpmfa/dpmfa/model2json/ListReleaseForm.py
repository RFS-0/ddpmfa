from dpmfa.model2json.Form import Form


class ListReleaseForm(Form):


    #name_field = None
    #delay_field = None
    #release_rate_list_field = None

    def __init__(self, owner):
        super(ListReleaseForm, self).__init__(owner, 'listRelease', 'List Release')

        fields = self.enter_fields()
        self.name_field = fields.enter_new_text_field('name', 'Name')
        self.delay_field = fields.enter_new_text_field('delay', 'Delay')\
            .enter_number_config()\
                .set_decimals(0)\
                .enter_min_bound()\
                    .set_value(0)\
                    .set_inclusive(True)\
                .exit()\
            .exit()
        self.release_rate_list_field = fields.enter_new_forms_field('releaseList', 'Release List') \
            .set_min_forms(1)
        self.__add_item_form(self.release_rate_list_field.enter_form_definitions(), 0.5)

    def __add_item_form(self, form_list, value):
        return form_list.enter_new_form('item', 'Item')\
            .enter_title_template().clear().append_item('Item ').append_item('positionOneBased').exit()\
            .enter_fields()\
                .enter_new_text_field('value', 'Value').set_value(value).exit()\
            .exit()

    def apply_default_configuration(self):
        self.name_field.set_value('New List Release')
        self.delay_field.set_value('0')
        self.set_release_rate_values(['0.5'])
        return self

    def configure_for(self, db_entity):
        self.name_field.set_value(db_entity.name)
        self.delay_field.set_value(db_entity.delay)
        self.set_release_rate_values([s.strip() for s in db_entity.release_rate_list.split(',')] if db_entity.release_rate_list is not None and db_entity.release_rate_list != '' else [])
        return self

    def enter_name_field(self):
        return self.name_field

    def set_name(self, name):
        self.name_field.set_value(name)
        return self

    def enter_delay_field(self):
        return self.delay_field

    def set_delay(self, delay):
        self.delay_field.set_value(delay)
        return self

    def enter_release_rate_list_field(self):
        return self.release_rate_field

    def set_release_rate_values(self, values):
        value_forms = self.release_rate_list_field.enter_value_forms().clear()
        for value in values:
            self.__add_item_form(value_forms, str(value))
        return self
