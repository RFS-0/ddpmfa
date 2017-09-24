from dpmfa.model2json.Form import Form


class FixedValueInflowForm(Form):

    #value_field = None

    def __init__(self, owner):
        super(FixedValueInflowForm, self).__init__(owner, 'fixedValueInflow', 'Fixed Value Inflow')
        self.value_field = self.enter_fields().enter_new_text_field('value', 'Value')\
            .set_value(0)\
            .enter_number_config()\
                .enter_min_bound().set_value('0').set_inclusive(True).exit()\
            .exit()

    def enter_value_field(self):
        return self.value_field

    def apply_default_configuration(self):
        return self

    def configure_for(self, db_entity):
        self.value_field.set_value(str(db_entity.value))
        return self
