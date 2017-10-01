from dpmfa.model2json.Form import Form


class FunctionReleaseForm(Form):


    #name_field = None
    #delay_field = None

    def __init__(self, owner):
        super(FunctionReleaseForm, self).__init__(owner, 'functionRelease', 'Function Release')

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

    def apply_default_configuration(self):
        self.name_field.set_value('New Function Release')
        self.delay_field.set_value('0')
        return self

    def configure_for(self, db_entity):
        self.name_field.set_value(db_entity.name)
        self.delay_field.set_value(db_entity.delay)
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
