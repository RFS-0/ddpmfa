from dpmfa.model2json.Form import Form


class RandomChoiceInflowForm(Form):

    #sample_field = None

    def __init__(self, owner):
        super(RandomChoiceInflowForm, self).__init__(owner, 'randomChoiceInflow', 'Random Choice Inflow')
        self.sample_field = self.enter_fields().enter_new_forms_field('sample', 'Sample') \
            .set_min_forms(1)
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
        self.set_values([0])
        return self

    def configure_for(self, db_entity):
        self.set_values(
            [s.strip() for s in db_entity.sample.split(',')] if db_entity != '' else []
        )
        return self
