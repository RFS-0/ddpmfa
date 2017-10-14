from dpmfa.model2json.BinomialDistributionForm import BinomialDistributionForm
from dpmfa.model2json.ExponentialDistributionForm import ExponentialDistributionForm
from dpmfa.model2json.FormsField import FormsField
from dpmfa.model2json.GammaDistributionForm import GammaDistributionForm
from dpmfa.model2json.GeometricDistributionForm import GeometricDistributionForm
from dpmfa.model2json.NormalDistributionForm import NormalDistributionForm
from dpmfa.model2json.ParetoDistributionForm import ParetoDistributionForm
from dpmfa.model2json.TriangularDistributionForm import TriangularDistributionForm
from dpmfa.model2json.UniformDistributionForm import UniformDistributionForm


class DistributionFormsField(FormsField):

    #normal_distribution_definition_form = None
    #uniform_distribution_definition_form = None
    #triangular_distribution_definition_form = None
    #exponential_distribution_definition_form = None
    #geometric_distribution_definition_form = None
    #binomial_distribution_definition_form = None
    #gamma_distribution_definition_form = None
    #pareto_distribution_definition_form = None

    def __init__(self, owner, prop_name, label):
        super(DistributionFormsField, self).__init__(owner, prop_name, label)

        self.set_max_forms(1)

        form_definitions = self.enter_form_definitions()
        self.normal_distribution_definition_form = form_definitions\
            .append_and_enter(NormalDistributionForm(None))
        self.uniform_distribution_definition_form = form_definitions\
            .append_and_enter(UniformDistributionForm(None))
        self.triangular_distribution_definition_form = form_definitions\
            .append_and_enter(TriangularDistributionForm(None))
        self.exponential_distribution_definition_form = form_definitions\
            .append_and_enter(ExponentialDistributionForm(None))
        self.geometric_distribution_definition_form = form_definitions \
            .append_and_enter(GeometricDistributionForm(None))
        self.binomial_distribution_definition_form = form_definitions \
            .append_and_enter(BinomialDistributionForm(None))
        self.gamma_distribution_definition_form = form_definitions \
            .append_and_enter(GammaDistributionForm(None))
        self.pareto_distribution_definition_form = form_definitions \
            .append_and_enter(ParetoDistributionForm(None))

    def apply_default_configuration(self):
        self.enter_new_normal_distribution_value_form()
        return self

    def enter_normal_distribution_definition_form(self):
        return self.normal_distribution_definition_form

    def enter_uniform_distribution_definition_form(self):
        return self.uniform_distribution_definition_form

    def enter_triangular_distribution_definition_form(self):
        return self.triangular_distribution_definition_form

    def enter_exponential_distribution_definition_form(self):
        return self.exponential_distribution_definition_form

    def enter_geometric_distribution_definition_form(self):
        return self.geometric_distribution_definition_form

    def enter_binomial_distribution_definition_form(self):
        return self.binomial_distribution_definition_form

    def enter_gamma_distribution_definition_form(self):
        return self.gamma_distribution_definition_form

    def enter_pareto_distribution_definition_form(self):
        return self.pareto_distribution_definition_form

    def enter_new_normal_distribution_value_form(self):
        return self.enter_value_forms().append_and_enter(NormalDistributionForm(None))

    def enter_new_uniform_distribution_value_form(self):
        return self.enter_value_forms().append_and_enter(UniformDistributionForm(None))

    def enter_new_triangular_distribution_value_form(self):
        return self.enter_value_forms().append_and_enter(TriangularDistributionForm(None))

    def enter_new_exponential_distribution_value_form(self):
        return self.enter_value_forms().append_and_enter(ExponentialDistributionForm(None))

    def enter_new_geometric_distribution_value_form(self):
        return self.enter_value_forms().append_and_enter(GeometricDistributionForm(None))

    def enter_new_binomial_distribution_value_form(self):
        return self.enter_value_forms().append_and_enter(BinomialDistributionForm(None))

    def enter_new_gamma_distribution_value_form(self):
        return self.enter_value_forms().append_and_enter(GammaDistributionForm(None))

    def enter_new_pareto_distribution_value_form(self):
        return self.enter_value_forms().append_and_enter(ParetoDistributionForm(None))

    def enter_new_distribution_value_form(self, distribution_code, parameters):
        if distribution_code == 'UNI':
            return self.enter_new_uniform_distribution().set_parameters(parameters)
        elif distribution_code == 'TRI':
            return self.enter_new_triangular_distribution_value_form().set_parameters(parameters)
        elif distribution_code == 'EXPO':
            return self.enter_new_exponential_distribution_value_form().set_parameters(parameters)
        elif distribution_code == 'GEO':
            return self.enter_new_geometric_distribution_value_form().set_parameters(parameters)
        elif distribution_code == 'BINOM':
            return self.enter_new_binomial_distribution_value_form().set_parameters(parameters)
        elif distribution_code == 'GAMMA':
            return self.enter_new_gamma_distribution_value_form().set_parameters(parameters)
        elif distribution_code == 'PAR':
            return self.enter_new_pareto_distribution_value_form().set_parameters(parameters)
        else:
            return self.enter_new_normal_distribution_value_form().set_parameters(parameters)
