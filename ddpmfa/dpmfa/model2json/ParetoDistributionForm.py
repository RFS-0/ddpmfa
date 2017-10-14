from dpmfa.model2json.Form import Form


class ParetoDistributionForm(Form):

    #a_field

    def __init__(self, owner):
        super(ParetoDistributionForm, self).__init__(owner, 'peretoDistribution', 'Pareto Distribution')
        self.a_field = self.enter_fields().enter_new_text_field('a', 'A')\
            .set_value('0.5')\
            .enter_number_config()\
                .enter_min_bound()\
                    .set_value(0)\
                    .set_inclusive(False)\
                .exit()\
            .exit()

    def set_a(self, a):
        self.a_field.set_value(a)
        return self

    def enter_a_field(self):
        return self.a_field

    def set_parameters(self, parameters):
        self.set_a(parameters[0])
        return self
