from dpmfa.model2json.Form import Form


class UniformDistributionForm(Form):

    #low_field = None
    #high_field = None

    def __init__(self, owner):
        super(UniformDistributionForm, self).__init__(owner, 'uniformDistribution', 'Uniform Distribution')
        self.low_field = self.enter_fields().enter_new_text_field('low', 'Low')\
            .set_value(0)\
            .enter_number_config()
        self.low_field = self.enter_fields().enter_new_text_field('high', 'High') \
            .set_value(1) \
            .enter_number_config()

    def set_low(self, low):
        self.low_field.set_value(low)
        return self

    def enter_low_field(self):
        return self.low_field

    def set_high(self, high):
        self.high_field.set_value(high)
        return self

    def enter_high_field(self):
        return self.high_field

    def set_parameters(self, parameters):
        self.set_low(parameters[0])
        self.set_high(parameters[1])
        return self
