from dpmfa.model2json.Form import Form


class ExponentialDistributionForm(Form):

    #scale_field = None

    def __init__(self, owner):
        super(ExponentialDistributionForm, self).__init__(owner, 'exponentialDistribution', 'Exponential Distribution')
        self.scale_field = self.enter_fields().enter_new_text_field('scale', 'Scale (1 / lambda)')\
            .set_value(1)\
            .enter_number_config().enter_min_bound().set_value(0).set_inclusive(False)

    def set_scale(self, scale):
        self.scale_field.set_value(scale)
        return self

    def enter_scale_field(self):
        return self.scale_field

    def set_parameters(self, parameters):
        self.set_scale(parameters[0])
        return self
