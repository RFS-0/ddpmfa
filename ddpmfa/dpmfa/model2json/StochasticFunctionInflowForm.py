from dpmfa.model2json.DistributionFormsField import DistributionFormsField
from dpmfa.model2json.Form import Form


class StochasticFunctionInflowForm(Form):

    #pdf_field = None

    def __init__(self, owner):
        super(StochasticFunctionInflowForm, self).__init__(owner, 'stochasticFunctionInflow', 'Stochastic Function Inflow')
        self.pdf_field = self.enter_fields().append_and_enter(DistributionFormsField(None, 'pdf', 'Probability Distribution Function'))\
            .set_min_forms(1)

    def enter_pdf_field(self):
        return self.pdf_field

    def apply_default_configuration(self):
        self.pdf_field.apply_default_configuration()
        return self

    def configure_for(self, db_entity):
        self.pdf_field.enter_new_distribution_value_form(db_entity.pdf, db_entity.parameter_values)
        return self
