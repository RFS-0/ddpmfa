from dpmfa.model2json.DistributionFormsField import DistributionFormsField
from dpmfa.model2json.TransferConnection import TransferConnection
from dpmfa.model2json.ValueList import ValueList


class StochasticTransferConnection(TransferConnection):

    def __init__(self, owner):
        super(StochasticTransferConnection, self).__init__(owner, 'stochasticTransfer', 'Stochastic Transfer')

        fields = self.enter_fields()
        self.function_field = self.enter_fields().append_and_enter(DistributionFormsField(None, 'distributionFunction', 'Distribution Function')) \
            .set_min_forms(1)

    def apply_default_configuration(self):
        self.set_name('New Stochastic Transfer')
        self.set_priority(0)
        self.function_field.apply_default_configuration()
        return self

    def configure_for(self, db_entity):
        self.set_source_node_id('compartment_' + str(db_entity.source_flow_compartment.pk))
        self.set_target_node_id('compartment_' + str(db_entity.target.pk))
        self.set_name(db_entity.name)
        self.set_priority(db_entity.priority)
        self.function_field.enter_new_distribution_value_form(
            db_entity.function,
            [s.strip() for s in db_entity.parameters.split(',')] if (db_entity.parameters is not None and db_entity.parameters != '') else []
        )
        return self
