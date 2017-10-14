from dpmfa import models as dbm

from dpmfa.model2json.DistributionFormsField import DistributionFormsField
from dpmfa.model2json.FixedValueInflowForm import FixedValueInflowForm
from dpmfa.model2json.Node import Node
from dpmfa.model2json.RandomChoiceInflowForm import RandomChoiceInflowForm
from dpmfa.model2json.SinglePeriodInflowFormsField import SinglePeriodInflowFormsField
from dpmfa.model2json.StochasticFunctionInflowForm import StochasticFunctionInflowForm

from itertools import chain


class ExternalListInflow(Node):

    #name_field = None
    #start_delay_field = None
    #derivation_distribution_field = None
    #derivation_factor_field = None
    #single_period_inflows_field = None

    def __init__(self, owner):
        super(ExternalListInflow, self).__init__(owner, 'externalListInflow', 'External List Inflow')

        self.enter_classes().append_item('inflow').append_item('external-list-inflow')
        self.enter_out_connection_types().append_item('inflowTarget')

        self.set_max_outgoing(1)
        self.set_min_outgoing(1)
        self.set_max_incoming(0)

        fields = self.enter_fields()
        self.name_field = fields.enter_new_text_field('name', 'Name').set_value('New External List Inflow')
        self.start_delay_field = fields.enter_new_text_field('startDelay', 'Start Delay')\
                .set_value('0')\
                .enter_number_config()\
                    .set_decimals(0)\
                    .enter_min_bound().set_value(0).set_inclusive(True).exit()\
                .exit()
        self.derivation_distribution_field = fields.append_and_enter(DistributionFormsField(None, 'derivationDistribution', 'Derivation Distribution'))
        self.derivation_factor_field = fields.enter_new_text_field('derivationFactor', 'Derivation Factor')\
                .set_value('1')\
                .enter_number_config().exit()
        self.single_period_inflows_field = fields.append_and_enter(SinglePeriodInflowFormsField(None, 'singlePeriodInflows', 'Single Period Inflows'))

    def apply_default_configuration(self):
        self.derivation_distribution_field.apply_default_configuration()
        self.single_period_inflows_field.apply_default_configuration()
        return self

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

        db_fixed_value_inflows = dbm.fixed_value_inflow.objects.filter(external_list_inflow=db_entity)
        db_random_choice_inflows = dbm.random_choice_inflow.objects.filter(external_list_inflow=db_entity)
        db_stochastic_function_inflows = dbm.stochastic_function_inflow.objects.filter(external_list_inflow=db_entity)

        db_single_period_inflows = list(chain(db_fixed_value_inflows, db_random_choice_inflows, db_stochastic_function_inflows))
        db_single_period_inflows.sort(key=lambda x : x.period)

        for db_single_period_inflow in db_single_period_inflows:
            if (isinstance(db_single_period_inflow, dbm.fixed_value_inflow)):
                self.single_period_inflows_field.enter_value_forms().append_and_enter(FixedValueInflowForm(None).configure_for(db_single_period_inflow))
            elif (isinstance(db_single_period_inflow, dbm.random_choice_inflow)):
                self.single_period_inflows_field.enter_value_forms().append_and_enter(RandomChoiceInflowForm(None).configure_for(db_single_period_inflow))
            else:
                self.single_period_inflows_field.enter_value_forms().append_and_enter(StochasticFunctionInflowForm(None).configure_for(db_single_period_inflow))

        return self

    def enter_name_field(self):
        return self.name_field

    def enter_start_delay_field(self):
        return self.start_delay_field

    def enter_derivation_distribution_field(self):
        return self.derivation_distribution_field

    def enter_derivation_factor_field(self):
        return self.derivation_factor_field

    def enter_single_period_inflows_field(self):
        return self.single_period_inflows_field
