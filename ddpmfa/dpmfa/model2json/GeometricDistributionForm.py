from dpmfa.model2json.Form import Form


class GeometricDistributionForm(Form):

    #probability_field = None
    #size_field = None

    def __init__(self, owner):
        super(GeometricDistributionForm, self).__init__(owner, 'geometricDistribution', 'Geometric Distribution')
        self.probability_field = self.enter_fields().enter_new_text_field('probability', 'Probability')\
            .set_value('0.5')\
            .enter_number_config()\
                .enter_min_bound()\
                    .set_value(0)\
                    .set_inclusive(True)\
                .exit()\
                .enter_max_bound()\
                    .set_value(1)\
                    .set_inclusive(True)\
                .exit()\
            .exit()

        self.size_field = self.enter_fields().enter_new_text_field('size', 'Size')\
            .set_value('1')\
            .enter_number_config()\
                .set_decimals(0)\
                .enter_min_bound()\
                    .set_value(0)\
                    .set_inclusive(True)\
                .exit()\
            .exit()

    def set_probability(self, probability):
        self.probability_field.set_value(probability)
        return self

    def enter_probability_field(self):
        return self.probability_field

    def set_size(self, size):
        self.size_field.set_value(size)
        return self

    def enter_size_field(self):
        return self.size_field

    def set_parameters(self, parameters):
        self.set_probability(parameters[0])
        self.set_size(parameters[1])
        return self
