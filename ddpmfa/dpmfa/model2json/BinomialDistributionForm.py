from dpmfa.model2json.Form import Form


class BinomialDistributionForm(Form):

    # probability_field = None
    # trial_count_field = None

    def __init__(self, owner):
        super(BinomialDistributionForm, self).__init__(owner, 'binomialDistribution', 'Binomial Distribution')
        self.trial_count_field = self.enter_fields().enter_new_text_field('trialCount', 'Number of Trials')\
            .set_value('1')\
            .enter_number_config()\
                .set_decimals(0)\
                .enter_min_bound()\
                    .set_value(0)\
                    .set_inclusive(True)\
                .exit()\
            .exit()

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

    def set_trial_count(self, trial_count):
        self.trial_count_field.set_value(trial_count)
        return self

    def enter_trial_count_field(self):
        return self.trial_count_field

    def set_probability(self, probability):
        self.probability_field.set_value(probability)
        return self

    def enter_probability_field(self):
        return self.probability_field

    def set_parameters(self, parameters):
        self.set_trial_count(parameters[0])
        self.set_probability(parameters[1])
        return self
