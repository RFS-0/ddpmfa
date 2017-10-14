from dpmfa import models as dbm

from dpmfa.model2json.DistributionFormsField import DistributionFormsField
from dpmfa.model2json.FixedValueInflowForm import FixedValueInflowForm
from dpmfa.model2json.Node import Node
from dpmfa.model2json.RandomChoiceInflowForm import RandomChoiceInflowForm
from dpmfa.model2json.SinglePeriodInflowFormsField import SinglePeriodInflowFormsField
from dpmfa.model2json.StochasticFunctionInflowForm import StochasticFunctionInflowForm


class ExternalFunctionInflow(Node):

    # name_field = None
    # start_delay_field = None
    # derivation_distribution_field = None
    # derivation_factor_field = None
    # inflow_function_field = None
    # basic_inflow_field = None
    # external_function_field = None

    def __init__(self, owner):
        super(ExternalFunctionInflow, self).__init__(owner, 'externalFunctionInflow', 'External Function Inflow')

        self.enter_classes().append_item('inflow').append_item('external-function-inflow')
        self.enter_out_connection_types().append_item('inflowTarget')

        self.set_max_outgoing(1)
        self.set_min_outgoing(1)
        self.set_max_incoming(0)

        fields = self.enter_fields()
        self.name_field = fields.enter_new_text_field('name', 'Name').set_value('New External Function Inflow')
        self.start_delay_field = fields.enter_new_text_field('startDelay', 'Start Delay') \
            .set_value('0') \
            .enter_number_config() \
            .set_decimals(0) \
            .enter_min_bound().set_value(0).set_inclusive(True).exit() \
            .exit()
        self.derivation_distribution_field = fields.append_and_enter(
            DistributionFormsField(None, 'derivationDistribution', 'Derivation Distribution'))
        self.derivation_factor_field = fields.enter_new_text_field('derivationFactor', 'Derivation Factor') \
            .set_value('1') \
            .enter_number_config().exit()

        self.basic_inflow_field = fields.append_and_enter(SinglePeriodInflowFormsField(None, 'basicInflow', 'Basic Inflow'))\
            .set_max_forms(1)

        self.inflow_function_field = fields.enter_new_forms_field('inflowFunction', 'Inflow Function')\
            .set_min_forms(1)\
            .set_max_forms(1)
        self.__add_linear_function(self.inflow_function_field.enter_form_definitions(), 0, 1, 0)


    def __add_linear_function(self, form_definitions, a, b, c):
        form_definitions \
            .enter_new_form('linearFunction', 'Linear Function (a * basicInflow + b * period + c)') \
                .enter_fields() \
                    .enter_new_text_field('a', 'a') \
                        .set_value(a)\
                        .enter_number_config().exit()\
                    .exit() \
                    .enter_new_text_field('b', 'b') \
                        .set_value(b)\
                        .enter_number_config().exit()\
                    .exit() \
                    .enter_new_text_field('c', 'c') \
                        .set_value(c)\
                        .enter_number_config().exit()\
                    .exit() \
                .exit() \
            .exit() \

    def configure_for(self, db_entity):
        self.set_node_id('inflow_' + str(db_entity.pk))
        self.set_position(db_entity.x, db_entity.y)

        self.name_field.set_value(db_entity.name)
        self.start_delay_field.set_value(db_entity.start_delay)
        self.derivation_distribution_field.enter_new_distribution_value_form(
            db_entity.derivation_distribution,
            [s.strip() for s in db_entity.derivation_parameters.split(',')] if (db_entity.derivation_parameters is not None and db_entity.derivation_parameters != '') else [],
        )
        self.derivation_factor_field.set_value(db_entity.derivation_factor)

        for db_base_inflow in dbm.fixed_value_inflow.objects.filter(external_function_inflow=db_entity):
            self.basic_inflow_field.enter_value_forms().append_and_enter(FixedValueInflowForm(None).configure_for(db_base_inflow))
        for db_base_inflow in dbm.random_choice_inflow.objects.filter(external_function_inflow=db_entity):
            self.basic_inflow_field.enter_value_forms().append_and_enter(RandomChoiceInflowForm(None).configure_for(db_base_inflow))
        for db_base_inflow in dbm.stochastic_function_inflow.objects.filter(external_function_inflow=db_entity):
            self.basic_inflow_field.enter_value_forms().append_and_enter(StochasticFunctionInflowForm(None).configure_for(db_base_inflow))

        params = [p.strip() for p in db_entity.function_parameters.split(',')] if (db_entity.function_parameters is not None and db_entity.function_parameters != '') else []
        a = params[0] if len(params) > 0 else 0
        b = params[1] if len(params) > 1 else 0
        c = params[2] if len(params) > 2 else 0
        self.__add_linear_function(self.inflow_function_field.enter_value_forms(), a, b, c)
        return self

    def apply_default_configuration(self):
        self.derivation_distribution_field.apply_default_configuration()
        self.basic_inflow_field.apply_default_configuration()
        self.__add_linear_function(self.inflow_function_field.enter_value_forms(), 0, 1, 0)
        return self

    def enter_name_field(self):
        return self.name_field

    def enter_start_delay_field(self):
        return self.start_delay_field

    def enter_derivation_distribution_field(self):
        return self.derivation_distribution_field

    def enter_derivation_factor_field(self):
        return self.derivation_factor_field

    def enter_inflow_function_field(self):
        return self.inflow_function_field

    def enter_basic_inflow_field(self):
        return self.basic_inflow_field
