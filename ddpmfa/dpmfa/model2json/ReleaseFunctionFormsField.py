from dpmfa.model2json.ExponentialDistributionForm import ExponentialDistributionForm
from dpmfa.model2json.FormsField import FormsField
from dpmfa.model2json.NormalDistributionForm import NormalDistributionForm
from dpmfa.model2json.TriangularDistributionForm import TriangularDistributionForm
from dpmfa.model2json.UniformDistributionForm import UniformDistributionForm


class ReleaseFunctionFormsField(FormsField):

    def __init__(self, owner, prop_name, label):
        super(ReleaseFunctionFormsField, self).__init__(owner, prop_name, label)

        self.set_min_forms(1)
        self.set_max_forms(1)

        self.__add_linear_function_form(self.enter_form_definitions(), 0, 1)
        self.__add_polynomial_function_form(self.enter_form_definitions(), [1])
        self.__add_exponential_function_form(self.enter_form_definitions(), 1, 2, 1, 0)
        self.__add_logarithmic_function_form(self.enter_form_definitions(), 1, 2, 1, 0)
        self.__add_sine_function_form(self.enter_form_definitions(), 1, 1, 0)
        self.__add_cosine_function_form(self.enter_form_definitions(), 1, 1, 0)


    def apply_default_configuration(self):
        self.__add_linear_function_form(self.enter_value_forms(), 0, 1)
        return self

    def configure_for(self, db_entity):
        params = [p.strip() for p in db_entity.function_parameters.split(',')] if (db_entity.function_parameters is not None and db_entity.function_parameters != '') else []
        if db_entity.release_function == 'LI':
            self.__add_linear_function_form(self.enter_value_forms(), *params)
        elif db_entity.release_function == 'PO':
            self.__add_polynomial_function_form(self.enter_value_forms(), *params)
        elif db_entity.release_function == 'EX':
            self.__add_exponential_function_form(self.enter_value_forms(), *params)
        elif db_entity.release_function == 'LG':
            self.__add_logarithmic_function_form(self.enter_value_forms(), *params)
        elif db_entity.release_function == 'SI':
            self.__add_sine_function_form(self.enter_value_forms(), *params)
        elif db_entity.release_function == 'CO':
            self.__add_cosine_function_form(self.enter_value_forms(), *params)
        return self


    def __add_linear_function_form(self, form_list, intercept, slope):
        form_list.enter_new_form('linearFunction', 'Linear Function')\
            .enter_fields()\
                .enter_new_text_field('intercept', 'Intercept')\
                    .set_value(intercept)\
                    .enter_number_config()\
                    .exit()\
                .exit()\
                .enter_new_text_field('slope', 'Slope')\
                    .set_value(slope)\
                    .enter_number_config()\
                    .exit()\
                .exit()\
            .exit()
        return self

    def __add_polynomial_function_form(self, form_list, coefficients):
        coefficients_field = form_list.enter_new_form('polynomialFunction', 'Polynomial Function (coefficient1 * x^(n-1) + ... + coefficientN)')\
            .enter_fields()\
                .enter_new_forms_field('coefficients', 'Coefficients')\
                    .set_min_forms(1)\
                    .enter_form_definitions()\
                        .enter_new_form('coefficient', 'Coefficient')\
                            .enter_title_template()\
                                .append_item(' ').append_item('positionOneBased')\
                            .exit()\
                            .enter_fields()\
                                .enter_new_text_field('value', 'Value')\
                                    .set_value(0)\
                                    .enter_number_config().exit()\
                                .exit()\
                            .exit()\
                        .exit()\
                    .exit()
        for coefficient in coefficients:
            coefficients_field\
                .enter_value_forms()\
                    .enter_new_form('coefficient', 'Coefficient') \
                        .enter_title_template() \
                            .append_item(' ').append_item('positionOneBased') \
                        .exit() \
                        .enter_fields() \
                            .enter_new_text_field('value', 'Value') \
                                .set_value(coefficient) \
                                .enter_number_config().exit()
        return self

    def __add_exponential_function_form(self, form_list, factor, base, exponent_factor, exponent_shift):
        form_list.enter_new_form('exponentialFunction', 'Exponential Function (a * b^(c * x + d))')\
            .enter_fields()\
                .enter_new_text_field('factor', 'a')\
                    .set_value(factor)\
                    .enter_number_config()\
                    .exit()\
                .exit()\
                .enter_new_text_field('base', 'b')\
                    .set_value(base)\
                    .enter_number_config()\
                    .exit()\
                .exit()\
                .enter_new_text_field('exponentFactor', 'c')\
                    .set_value(exponent_factor)\
                    .enter_number_config()\
                    .exit()\
                .exit()\
                .enter_new_text_field('exponentShift', 'd')\
                    .set_value(exponent_shift)\
                    .enter_number_config()\
                    .exit()\
                .exit()\
            .exit()
        return self

    def __add_logarithmic_function_form(self, form_list, factor, base, arg_factor, arg_shift):
       form_list.enter_new_form('logarithmicFunction', 'Logarithmic Function (a * log_b(c * x + d))')\
           .enter_fields()\
               .enter_new_text_field('factor', 'a')\
                   .set_value(factor)\
                   .enter_number_config()\
                   .exit()\
               .exit()\
               .enter_new_text_field('base', 'b')\
                   .set_value(base)\
                   .enter_number_config()\
                   .exit()\
               .exit()\
               .enter_new_text_field('argFactor', 'c')\
                   .set_value(arg_factor)\
                   .enter_number_config()\
                   .exit()\
               .exit()\
               .enter_new_text_field('argShift', 'd')\
                   .set_value(arg_shift)\
                   .enter_number_config()\
                   .exit()\
               .exit()\
           .exit()
       return self

    def __add_sine_function_form(self, form_list, amplitude, frequency, phase):
       form_list.enter_new_form('sineFunction', 'Sine Function')\
           .enter_fields()\
               .enter_new_text_field('amplitude', 'Amplitude')\
                   .set_value(amplitude)\
                   .enter_number_config()\
                   .exit()\
               .exit()\
               .enter_new_text_field('frequency', 'Frequency')\
                   .set_value(frequency)\
                   .enter_number_config()\
                   .exit()\
               .exit()\
               .enter_new_text_field('phase', 'Phase')\
                   .set_value(phase)\
                   .enter_number_config()\
                   .exit()\
               .exit()\
           .exit()
       return self

    def __add_cosine_function_form(self, form_list, amplitude, frequency, phase):
       form_list.enter_new_form('cosineFunction', 'Cosine Function')\
           .enter_fields()\
               .enter_new_text_field('amplitude', 'Amplitude')\
                   .set_value(amplitude)\
                   .enter_number_config()\
                   .exit()\
               .exit()\
               .enter_new_text_field('frequency', 'Frequency')\
                   .set_value(frequency)\
                   .enter_number_config()\
                   .exit()\
               .exit()\
               .enter_new_text_field('phase', 'Phase')\
                   .set_value(phase)\
                   .enter_number_config()\
                   .exit()\
               .exit()\
           .exit()
       return self