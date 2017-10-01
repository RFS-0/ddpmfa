from dpmfa.model2json.Form import Form


class FixedRateReleaseForm(Form):


    #name_field = None
    #delay_field = None
    #release_rate_field = None

    def __init__(self, owner):
        super(FixedRateReleaseForm, self).__init__(owner, 'fixedRateRelease', 'Fixed Rate Release')

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
        self.release_rate_field = fields.enter_new_text_field('releaseRate', 'Release Rate')\
            .enter_number_config()\
                .enter_min_bound()\
                    .set_value(0)\
                    .set_inclusive(True)\
                .exit()\
                .enter_max_bound()\
                    .set_value(1)\
                    .set_inclusive(1)\
                .exit()\
            .exit()

    def apply_default_configuration(self):
        self.name_field.set_value('New Fixed Rate Release')
        self.delay_field.set_value('0')
        self.release_rate_field.set_value('0.5')
        return self

    def configure_for(self, db_entity):
        self.name_field.set_value(db_entity.name)
        self.delay_field.set_value(db_entity.delay)
        self.release_rate_field.set_value(db_entity.release_rate)
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

    def enter_release_rate_field(self):
        return self.release_rate_field

    def set_release_rate(self, release_rate):
        self.relase_rate_field.set_value(release_rate)
        return self
