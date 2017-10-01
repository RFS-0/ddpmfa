from dpmfa import models as dbm
from dpmfa.model2json.FixedRateReleaseForm import FixedRateReleaseForm
from dpmfa.model2json.FormsField import FormsField
from dpmfa.model2json.FunctionReleaseForm import FunctionReleaseForm
from dpmfa.model2json.ListReleaseForm import ListReleaseForm


class LocalReleaseFormsField(FormsField):

    #fixed_rate_release_definition_form = None
    #list_release_definition_form = None
    #function_release_definition_form = None

    def __init__(self, owner, prop_name, label):
        super(LocalReleaseFormsField, self).__init__(owner, prop_name, label)

        self.set_min_forms(1)
        self.set_max_forms(1)

        form_definitions = self.enter_form_definitions()
        self.fixed_rate_release_definition_form = form_definitions\
            .append_and_enter(FixedRateReleaseForm(None)).apply_default_configuration()
        self.list_release_definition_form = form_definitions\
            .append_and_enter(ListReleaseForm(None)).apply_default_configuration()
        self.function_release_definition_form = form_definitions\
            .append_and_enter(FunctionReleaseForm(None)).apply_default_configuration()

    def apply_default_configuration(self):
        self.enter_value_forms()\
            .append_and_enter(FixedRateReleaseForm(None)).apply_default_configuration()
        return self

    def configure_for_stock(self, db_stock):
        release_processed = False

        fixed_rate_releases = dbm.fixed_rate_release.objects.filter(stock=db_stock)
        if fixed_rate_releases.count() > 0:
            self.enter_value_forms().append_and_enter(FixedRateReleaseForm(None)).configure_for(fixed_rate_releases[0])
            release_processed = True

        if not release_processed:
            list_releases = dbm.list_release.objects.filter(stock=db_stock)
            if list_releases.count() > 0:
                self.enter_value_forms().append_and_enter(ListReleaseForm(None)).configure_for(list_releases[0])
                release_processed = True

        if not release_processed:
            function_releases = dbm.function_release.objects.filter(stock=db_stock)
            if function_releases.count() > 0:
                self.enter_value_forms().append_and_enter(FunctionReleaseForm(None)).configure_for(function_releases[0])
                release_processed = True

        return self

    def enter_fixed_rate_release_definition_form(self):
        return self.fixed_rate_release_definition_form
