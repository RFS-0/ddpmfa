from dpmfa.model2json.Form import Form


class GammaDistributionForm(Form):

    #shape_field = None
    #scale_field = None

    def __init__(self, owner):
        super(GammaDistributionForm, self).__init__(owner, 'gammaDistribution', 'Gamma Distribution')
        self.shape_field = self.enter_fields().enter_new_text_field('shape', 'Shape')\
            .set_value('0.5')\
            .enter_number_config()\
                .enter_min_bound()\
                    .set_value(0)\
                    .set_inclusive(False)\
                .exit()\
            .exit()
        self.shape_field = self.enter_fields().enter_new_text_field('scale', 'Scale') \
            .set_value('0.5') \
            .enter_number_config() \
               .enter_min_bound() \
                    .set_value(0) \
                    .set_inclusive(False) \
                .exit() \
            .exit()

    def set_shape(self, shape):
        self.shape_field.set_value(shape)
        return self

    def enter_shape_field(self):
        return self.shape_field

    def set_scale(self, scale):
        self.scale_field.set_value(scale)
        return self

    def enter_scale_field(self):
        return self.scale_field

    def set_parameters(self, parameters):
        self.set_shape(parameters[0])
        self.set_scale(parameters[1])
        return self
