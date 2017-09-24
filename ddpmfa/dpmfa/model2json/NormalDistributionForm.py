from dpmfa.model2json.Form import Form


class NormalDistributionForm(Form):

    #mean_field = None
    #variance_field = None

    def __init__(self, owner):
        super(NormalDistributionForm, self).__init__(owner, 'normalDistribution', 'Normal Distribution')
        self.mean_field = self.enter_fields().enter_new_text_field('mean', 'Mean')\
            .set_value('0')\
            .enter_number_config().exit()

        self.variance_field = self.enter_fields().enter_new_text_field('variance', 'Variance')\
            .set_value('1')\
            .enter_number_config()\
                .enter_min_bound()\
                    .set_value(0)\
                    .set_inclusive(True)\
                .exit()\
            .exit()

    def set_mean(self, mean):
        self.mean_field.set_value(mean)
        return self

    def enter_mean_field(self):
        return self.mean_field

    def set_variance(self, variance):
        self.variance_field.set_value(variance)
        return self

    def enter_variance_field(self):
        return self.variance_field

    def set_parameters(self, parameters):
        self.set_mean(parameters[0])
        self.set_variance(parameters[1])
        return self
