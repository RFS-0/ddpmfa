from dpmfa.model2json.FixedValueInflowForm import FixedValueInflowForm
from dpmfa.model2json.FormsField import FormsField
from dpmfa.model2json.RandomChoiceInflowForm import RandomChoiceInflowForm
from dpmfa.model2json.StochasticFunctionInflowForm import StochasticFunctionInflowForm


class SinglePeriodInflowFormsField(FormsField):

    #fixed_value_inflow_definition_form = None
    #random_choice_inflow_definition_form = None
    #stochastic_function_inflow_definition_form = None

    def __init__(self, owner, prop_name, label):
        super(SinglePeriodInflowFormsField, self).__init__(owner, prop_name, label)

        self.set_min_forms(1)

        form_definitions = self.enter_form_definitions()
        self.fixed_value_inflow_definition_form = form_definitions\
            .append_and_enter(FixedValueInflowForm(None)).apply_default_configuration().exit()
        self.fixed_value_inflow_definition_form = form_definitions\
            .append_and_enter(RandomChoiceInflowForm(None)).apply_default_configuration().exit()
        self.fixed_value_inflow_definition_form = form_definitions\
            .append_and_enter(StochasticFunctionInflowForm(None)).apply_default_configuration().exit()

    def apply_default_configuration(self):
        self.enter_value_forms().append_and_enter(FixedValueInflowForm(None)).apply_default_configuration()
        return self

