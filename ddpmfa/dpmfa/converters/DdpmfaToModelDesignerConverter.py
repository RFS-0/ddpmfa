# python
import itertools as itertools

# ddpmfa
import dpmfa.models as models

class DdpmfaToModelDesignerConverter(object):

    #model_id = None
    #valid = True
    #cycles_allowed = False
    #parallels_allowed = False
    #nodes = []
    #node_types = []
    #connections = []
    #connection_types = []

    def __init__(self):
        self.model_id = None
        self.valid = True
        self.cycles_allowed = False
        self.parallels_allowed = False
        self.nodes = []
        self.node_types = []
        self.connections = []
        self.connection_types = []

    def configure_for(self, db_entity):
        self.model_id = db_entity.pk

        self.node_types.append(ExternalListInflow(self).apply_default_configuration())
        self.node_types.append(ExternalFunctionInflow(self).apply_default_configuration())
        self.node_types.append(FlowCompartment(self).apply_default_configuration())
        self.node_types.append(Sink(self).apply_default_configuration())
        self.node_types.append(Stock(self).apply_default_configuration())

        self.connection_types.append(InflowTargetConnection(self).apply_default_configuration())
        self.connection_types.append(ConstantTransferConnection(self).apply_default_configuration())
        self.connection_types.append(RandomChoiceTransferConnection(self).apply_default_configuration())
        self.connection_types.append(StochasticTransferConnection(self).apply_default_configuration())

        for db_inflow in models.external_list_inflow.objects.filter(target__model=db_entity):
            self.nodes.append(ExternalListInflow(self).configure_for(db_inflow))
            self.connections.append(InflowTargetConnection(self).set_source_node_id('inflow_' + str(db_inflow.pk)).set_target_node_id('compartment_' + str(db_inflow.target.pk)))

        for db_inflow in models.external_function_inflow.objects.filter(target__model=db_entity):
            self.nodes.append(ExternalFunctionInflow(self).configure_for(db_inflow))
            self.connections.append(InflowTargetConnection(self).set_source_node_id('inflow_' + str(db_inflow.pk)).set_target_node_id('compartment_' + str(db_inflow.target.pk)))

        for db_flow_compartment in models.flow_compartment.objects.filter(model=db_entity):
            db_stocks = models.stock.objects.filter(pk=db_flow_compartment.pk)
            if db_stocks.count() == 0:
                self.nodes.append(FlowCompartment(self).configure_for(db_flow_compartment))
            else:
                self.nodes.append(Stock(self).configure_for(db_stocks[0]))

        for db_sink in models.sink.objects.filter(model=db_entity):
            self.nodes.append(Sink(self).configure_for(db_sink))

        for db_transfer in models.constant_transfer.objects.filter(target__model=db_entity, belongs_to_aggregated_transfer__id__isnull=True):
            self.connections.append(ConstantTransferConnection(self).configure_for(db_transfer))

        for db_transfer in models.random_choice_transfer.objects.filter(target__model=db_entity, belongs_to_aggregated_transfer__id__isnull=True):
            self.connections.append(RandomChoiceTransferConnection(self).configure_for(db_transfer))

        for db_transfer in models.stochastic_transfer.objects.filter(target__model=db_entity, belongs_to_aggregated_transfer__id__isnull=True):
            self.connections.append(StochasticTransferConnection(self).configure_for(db_transfer))

        return self

    def set_model_id(self, model_id):
        self.model_id = model_id
        return self

    def get_model_id(self):
        return self.model_id

    def set_valid(self, valid):
        self.valid = valid
        return self

    def get_valid(self):
        return self.valid

    def set_cycles_allowed(self, cycles_allowed):
        self.cycles_allowed = cycles_allowed
        return self

    def get_cycles_allowed(self):
        return self.cycles_allowed

    def set_parallels_allowed(self, parallels_allowed):
        self.parallels_allowed = parallels_allowed
        return self

    def get_parallels_allowed(self):
        return self.parallels_allowed

    def get_nodes(self):
        return self.nodes

    def get_node_types(self):
        return self.node_types

    def get_connections(self):
        return self.connections

    def get_connection_types(self):
        return self.connection_types

    def as_dictionary(self):
        return {
            'id': self.model_id,
            'valid': self.valid,
            'cyclesAllowed': self.cycles_allowed,
            'parallelsAllowed': self.parallels_allowed,
            'nodes': [node.as_dictionary() for node in self.nodes],
            'nodeTypes': [node_type.as_dictionary() for node_type in self.node_types],
            'connections': [connection.as_dictionary() for connection in self.connections],
            'connectionTypes': [connection_type.as_dictionary() for connection_type in self.connection_types]
        }

# Config

class NumberBound(object):
    owner = None

    #value = 0
    #inclusive = True

    def __init__(self, owner):
        self.value = 0
        self.inclusive = True

        self.owner = owner

    def set_value(self, value):
        self.value = value
        return self

    def get_value(self):
        return self.value

    def set_inclusive(self, inclusive):
        self.inclusive = inclusive
        return self

    def get_inclusive(self):
        return self.inclusive

    def as_dictionary(self):
        return {
            'value': self.value,
            'inclusive': self.inclusive
        }

    def set_owner(self, owner):
        self.owner = owner

    def exit(self):
        return self.owner
    
class NumberConfig(object):
    #owner = None

    #decimals = -1
    #min_bound = None
    #max_bound = None

    def __init__(self, owner):
        self.decimals = -1
        self.min_bound = None
        self.max_bound = None

        self.owner = owner

    def set_decimals(self, decimals):
        self.decimals = decimals
        return self

    def get_decimals(self):
        return self.decimals

    def enter_min_bound(self):
        if self.min_bound is None:
            self.min_bound = NumberBound(self)
        return self.min_bound

    def enter_max_bound(self):
        if self.max_bound is None:
            self.max_bound = NumberBound(self)
        return self.max_bound

    def as_dictionary(self):
        return {
            'decimals': self.decimals,
            'min': self.min_bound.as_dictionary() if self.min_bound is not None else None,
            'max': self.max_bound.as_dictionary() if self.max_bound is not None else None
        }

    def set_owner(self, owner):
        self.owner = owner

    def exit(self):
        return self.owner
    
class Position(object):
    #owner = None

    #x = 5000
    #y = 5000

    def __init__(self, owner):
        self.x = 5000
        self.y = 5000

        self.owner = owner

    def set_x(self, x):
        self.x = x
        return self

    def get_x(self):
        return self.x

    def set_y(self, y):
        self.y = y
        return self

    def get_y(self):
        return self.y

    def as_dictionary(self):
        return {
            'x': self.x,
            'y': self.y
        }

    def set_owner(self, owner):
        self.owner = owner

    def exit(self):
        return self.owner

        
# Fields

class CheckField(object):
    # owner = None

    # prop_name = None
    # label = None

    # checked = False
    # dirty = True

    def __init__(self, owner, prop_name, label):
        self.owner = owner
        self.prop_name = prop_name
        self.label = label
        self.checked = False
        self.dirty = True

    def get_prop_name(self):
        return self.prop_name

    def get_label(self):
        return self.label

    def get_checked(self):
        return self.checked

    def set_checked(self, checked):
        self.checked = checked
        return self

    def get_dirty(self):
        return self.dirty

    def set_dirty(self, dirty):
        self.dirty = dirty
        return self

    def as_dictionary(self):
        return {
            'fieldType': 'CHECK',
            'fieldArgs': {},
            'propName': self.prop_name,
            'label': self.label,
            'valueData': self.checked,
            'dirty': self.dirty
        }

    def exit(self):
        return self
    
class TextField(object):
    #owner = None

    #prop_name = None
    #label = None

    #display_as_text_area = False
    #not_empty = True
    #max_length = 250
    #number_config = None
    #value = ''
    #dirty = True

    def __init__(self, owner, prop_name, label):
        self.display_as_text_area = False
        self.not_empty = True
        self.max_length = 250
        self.number_config = None
        self.value = ''
        self.dirty = True

        self.owner = owner
        self.prop_name = prop_name
        self.label = label

    def get_prop_name(self):
        return self.prop_name

    def get_label(self):
        return self.label

    def set_display_as_text_area(self, display_as_text_area):
        self.display_as_text_area = display_as_text_area
        return self

    def get_display_as_text_area(self):
        return self.display_as_text_area

    def set_not_empty(self, not_empty):
        self.not_empty = not_empty
        return self

    def get_not_empty(self):
        return self.not_empty

    def set_max_length(self, max_length):
        self.max_length = max_length
        return self

    def get_max_length(self):
        return self.max_length

    def enter_number_config(self):
        if self.number_config is None:
            self.number_config = NumberConfig(self)
        return self.number_config

    def set_value(self, value):
        self.value = value
        return self

    def get_value(self):
        return self.value

    def set_dirty(self, dirty):
        self.dirty = dirty
        return self

    def get_dirty(self):
        return self.dirty

    def as_dictionary(self):
        return {
            'fieldType': 'TEXT',
            'fieldArgs': {
                'displayAsTextArea': self.display_as_text_area,
                'notEmpty': self.not_empty,
                'maxLength': self.max_length,
                'numberConfig': self.number_config.as_dictionary() if self.number_config is not None else None
            },
            'propName': self.prop_name,
            'label': self.label,
            'valueData': self.value,
            'dirty': self.dirty
        }

    def set_owner(self, owner):
        self.owner = owner

    def exit(self):
        return self.owner
    
class FieldList(object):
    #owner = None

    #fields = []
    #field_by_prop_name = {}

    def __init__(self, owner):
        self.owner = owner
        self.fields = []
        self.field_by_prop_name = {}

    def count_fields(self):
        return len(self.fields)

    def get_prop_names(self):
        return [prop_name for prop_name in self.field_by_prop_name]

    def enter_field_by_index(self, index):
        return self.fields[index]

    def enter_field(self, prop_name):
        return self.field_by_prop_name[prop_name]

    def append_and_enter(self, field):
        field.set_owner(self)
        self.field_by_prop_name[field.get_prop_name()] = field
        self.fields.append(field)
        return field

    def enter_new_text_field(self, prop_name, label):
        text_field = TextField(self, prop_name, label)
        self.field_by_prop_name[prop_name] = text_field
        self.fields.append(text_field)
        return text_field

    def enter_new_check_field(self, prop_name, label):
        check_field = CheckField(self, prop_name, label)
        self.field_by_prop_name[prop_name] = check_field
        self.fields.append(check_field)
        return check_field

    def enter_new_forms_field(self, prop_name, label):
        forms_field = FormsField(self, prop_name, label)
        self.field_by_prop_name[prop_name] = forms_field
        self.fields.append(forms_field)
        return forms_field

    def clear(self):
        self.fields = []
        self.field_by_prop_name = {}
        return self

    def as_list(self):
        return [field.as_dictionary() for field in self.fields]

    def set_owner(self, owner):
        self.owner = owner

    def exit(self):
        return self.owner
    
class ValueList(object):
    #owner = None

    #items = []

    def __init__(self, owner):
        self.items = []

        self.owner = owner

    def append_item(self, item):
        self.items.append(item)
        return self

    def count_items(self):
        return len(self.items)

    def get_item(self, index):
        return self.items[index]

    def clear(self):
        self.items = []
        return self

    def as_list(self):
        return [item for item in self.items]

    def set_owner(self, owner):
        self.owner = owner

    def exit(self):
        return self.owner

# Forms

class FormList(object):
    #owner = None

    #forms = []
    #forms_by_form_type = {}

    def __init__(self, owner):
        self.owner = owner
        self.forms = []
        self.forms_by_form_type = {}

    def count_forms(self):
        return len(self.forms)

    def get_form_types(self):
        return [form_type for form_type in self.forms_by_form_type]

    def enter_form_by_index(self, index):
        return self.forms[index]

    def enter_form(self, form_type, index):
        return self.forms_by_form_type[form_type][index]

    def append_and_enter(self, form):
        form.set_owner(self)
        if form.get_form_type() not in self.forms_by_form_type:
            self.forms_by_form_type[form.get_form_type()] = []
        self.forms_by_form_type[form.get_form_type()].append(form)
        self.forms.append(form)
        return form

    def enter_new_form(self, form_type, label):
        form = Form(self, form_type, label)
        if form_type not in self.forms_by_form_type:
            self.forms_by_form_type[form_type] = []
        self.forms_by_form_type[form_type].append(form)
        self.forms.append(form)
        return form

    def clear(self):
        self.forms = []
        self.forms_by_form_type = {}
        return self

    def as_list(self):
        return [form.as_dictionary() for form in self.forms]

    def set_owner(self, owner):
        self.owner = owner

    def exit(self):
        return self.owner
    
class FormsField(object):
    #owner = None

    #prop_name = None
    #label = None

    #form_definitions = None
    #value_forms = None

    #min_forms = 0
    #max_forms = -1
    #dirty = True

    def __init__(self, owner, prop_name, label):
        self.min_forms = 0
        self.max_forms = -1
        self.dirty = True

        self.owner = owner
        self.prop_name = prop_name
        self.label = label
        self.form_definitions = FormList(self)
        self.value_forms = FormList(self)

    def get_prop_name(self):
        return self.prop_name

    def get_label(self):
        return self.label

    def set_min_forms(self, min_forms):
        self.min_forms = min_forms
        return self

    def get_min_forms(self):
        return self.min_forms

    def set_max_forms(self, max_forms):
        self.max_forms = max_forms
        return self

    def get_max_forms(self):
        return self.max_forms

    def enter_form_definitions(self):
        return self.form_definitions

    def enter_value_forms(self):
        return self.value_forms

    def set_dirty(self, dirty):
        self.dirty = dirty
        return self

    def get_dirty(self):
        return self.dirty

    def as_dictionary(self):
        return {
            'fieldType': 'FORMS',
            'fieldArgs': {
                'minForms': self.min_forms,
                'maxForms': self.max_forms,
                'forms': self.form_definitions.as_list()
            },
            'propName': self.prop_name,
            'label': self.label,
            'valueData': self.value_forms.as_list(),
            'dirty': self.dirty
        }

    def set_owner(self, owner):
        self.owner = owner

    def exit(self):
        return self.owner
    
class Form(object):
    #owner = None

    #form_type = None
    #label = None

    #title_template = None
    #fields = None

    #form_id = None
    #temp_id = None
    #dirty = True

    def __init__(self, owner, form_type, label):
        self.form_id = None
        self.temp_id = None
        self.dirty = True

        self.owner = owner
        self.form_type = form_type
        self.label = label
        self.title_template = ValueList(self).append_item('').append_item('label')
        self.fields = FieldList(self)

    def get_form_type(self):
        return self.form_type

    def get_label(self):
        return self.label

    def set_form_id(self, form_id):
        self.form_id = form_id
        return self

    def get_form_id(self):
        return self.form_id

    def set_temp_id(self, temp_id):
        self.temp_id = temp_id
        return self

    def get_temp_id(self):
        return self.temp_id

    def enter_title_template(self):
        return self.title_template

    def set_dirty(self, dirty):
        self.dirty = dirty
        return self

    def get_dirty(self):
        return self.dirty

    def enter_fields(self):
        return self.fields

    def as_dictionary(self):
        return {
            'id': self.form_id,
            'tempId': self.temp_id,
            'label': self.label,
            'type': self.form_type,
            'titleTemplate': self.title_template.as_list(),
            'dirty': self.dirty,
            'fields': self.fields.as_list()
        }

    def set_owner(self, owner):
        self.owner = owner

    def exit(self):
        return self.owner
    
class FixedRateReleaseForm(Form):


    #name_field = None
    #delay_field = None
    #release_rate_field = None

    def __init__(self, owner):
        super(FixedRateReleaseForm, self).__init__(owner, 'fixedRateRelease', 'Fixed Rate Release')

        fields = self.enter_fields()
        self.name_field = fields.enter_new_text_field('name', 'Name')
        self.delay_field = fields.enter_new_text_field('delay', 'Delay')\
            .enter_number_config()\
                .set_decimals(0)\
                .enter_min_bound()\
                    .set_value(0)\
                    .set_inclusive(True)\
                .exit()\
            .exit()
        self.release_rate_field = fields.enter_new_text_field('releaseRate', 'Release Rate')\
            .enter_number_config()\
                .enter_min_bound()\
                    .set_value(0)\
                    .set_inclusive(True)\
                .exit()\
                .enter_max_bound()\
                    .set_value(1)\
                    .set_inclusive(1)\
                .exit()\
            .exit()

    def apply_default_configuration(self):
        self.name_field.set_value('New Fixed Rate Release')
        self.delay_field.set_value('0')
        self.release_rate_field.set_value('0.5')
        return self

    def configure_for(self, db_entity):
        self.name_field.set_value(db_entity.name)
        self.delay_field.set_value(db_entity.delay)
        self.release_rate_field.set_value(db_entity.release_rate)
        return self

    def enter_name_field(self):
        return self.name_field

    def set_name(self, name):
        self.name_field.set_value(name)
        return self

    def enter_delay_field(self):
        return self.delay_field

    def set_delay(self, delay):
        self.delay_field.set_value(delay)
        return self

    def enter_release_rate_field(self):
        return self.release_rate_field

    def set_release_rate(self, release_rate):
        self.relase_rate_field.set_value(release_rate)
        return self

class FunctionReleaseForm(Form):

    #name_field = None
    #delay_field = None
    #release_function_field = None

    def __init__(self, owner):
        super(FunctionReleaseForm, self).__init__(owner, 'functionRelease', 'Function Release')

        fields = self.enter_fields()
        self.name_field = fields.enter_new_text_field('name', 'Name')
        self.delay_field = fields.enter_new_text_field('delay', 'Delay')\
            .enter_number_config()\
                .set_decimals(0)\
                .enter_min_bound()\
                    .set_value(0)\
                    .set_inclusive(True)\
                .exit()\
            .exit()
        self.release_function_field = fields.append_and_enter(ReleaseFunctionFormsField(self, 'releaseFunction', 'Release Function'))

    def apply_default_configuration(self):
        self.name_field.set_value('New Function Release')
        self.delay_field.set_value('0')
        self.release_function_field.apply_default_configuration()
        return self

    def configure_for(self, db_entity):
        self.name_field.set_value(db_entity.name)
        self.delay_field.set_value(db_entity.delay)
        self.release_function_field.configure_for(db_entity)
        return self

    def enter_name_field(self):
        return self.name_field

    def set_name(self, name):
        self.name_field.set_value(name)
        return self

    def enter_delay_field(self):
        return self.delay_field

    def set_delay(self, delay):
        self.delay_field.set_value(delay)
        return self

class ListReleaseForm(Form):


    #name_field = None
    #delay_field = None
    #release_rate_list_field = None

    def __init__(self, owner):
        super(ListReleaseForm, self).__init__(owner, 'listRelease', 'List Release')

        fields = self.enter_fields()
        self.name_field = fields.enter_new_text_field('name', 'Name')
        self.delay_field = fields.enter_new_text_field('delay', 'Delay')\
            .enter_number_config()\
                .set_decimals(0)\
                .enter_min_bound()\
                    .set_value(0)\
                    .set_inclusive(True)\
                .exit()\
            .exit()
        self.release_rate_list_field = fields.enter_new_forms_field('releaseList', 'Release List') \
            .set_min_forms(1)
        self.__add_item_form(self.release_rate_list_field.enter_form_definitions(), 0.5)

    def __add_item_form(self, form_list, value):
        return form_list.enter_new_form('item', 'Item')\
            .enter_title_template().clear().append_item('Item ').append_item('positionOneBased').exit()\
            .enter_fields()\
                .enter_new_text_field('value', 'Value').set_value(value).exit()\
            .exit()

    def apply_default_configuration(self):
        self.name_field.set_value('New List Release')
        self.delay_field.set_value('0')
        self.set_release_rate_values(['0.5'])
        return self

    def configure_for(self, db_entity):
        self.name_field.set_value(db_entity.name)
        self.delay_field.set_value(db_entity.delay)
        self.set_release_rate_values([s.strip() for s in db_entity.release_rate_list.split(',')] if db_entity.release_rate_list is not None and db_entity.release_rate_list != '' else [])
        return self

    def enter_name_field(self):
        return self.name_field

    def set_name(self, name):
        self.name_field.set_value(name)
        return self

    def enter_delay_field(self):
        return self.delay_field

    def set_delay(self, delay):
        self.delay_field.set_value(delay)
        return self

    def enter_release_rate_list_field(self):
        return self.release_rate_field

    def set_release_rate_values(self, values):
        value_forms = self.release_rate_list_field.enter_value_forms().clear()
        for value in values:
            self.__add_item_form(value_forms, str(value))
        return self

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

        fixed_rate_releases = models.fixed_rate_release.objects.filter(stock=db_stock)
        if fixed_rate_releases.count() > 0:
            self.enter_value_forms().append_and_enter(FixedRateReleaseForm(None)).configure_for(fixed_rate_releases[0])
            release_processed = True

        if not release_processed:
            list_releases = models.list_release.objects.filter(stock=db_stock)
            if list_releases.count() > 0:
                self.enter_value_forms().append_and_enter(ListReleaseForm(None)).configure_for(list_releases[0])
                release_processed = True

        if not release_processed:
            function_releases = models.function_release.objects.filter(stock=db_stock)
            if function_releases.count() > 0:
                self.enter_value_forms().append_and_enter(FunctionReleaseForm(None)).configure_for(function_releases[0])
                release_processed = True

        return self

    def enter_fixed_rate_release_definition_form(self):
        return self.fixed_rate_release_definition_form
  
class FixedValueInflowForm(Form):

    #value_field = None

    def __init__(self, owner):
        super(FixedValueInflowForm, self).__init__(owner, 'fixedValueInflow', 'Fixed Value Inflow')
        self.value_field = self.enter_fields().enter_new_text_field('value', 'Value')\
            .set_value(0)\
            .enter_number_config()\
                .enter_min_bound().set_value('0').set_inclusive(True).exit()\
            .exit()

    def enter_value_field(self):
        return self.value_field

    def apply_default_configuration(self):
        return self

    def configure_for(self, db_entity):
        self.value_field.set_value(str(db_entity.value))
        return self
    
class RandomChoiceInflowForm(Form):

    #sample_field = None

    def __init__(self, owner):
        super(RandomChoiceInflowForm, self).__init__(owner, 'randomChoiceInflow', 'Random Choice Inflow')
        self.sample_field = self.enter_fields().enter_new_forms_field('sample', 'Sample') \
            .set_min_forms(1)
        self.__add_item_form(self.sample_field.enter_form_definitions(), '0')

    def __add_item_form(self, form_list, value):
        return form_list.enter_new_form('item', 'Item')\
            .enter_title_template().clear().append_item('Item ').append_item('positionOneBased').exit()\
            .enter_fields()\
                .enter_new_text_field('value', 'Value').set_value(value).exit()\
            .exit()

    def set_values(self, values):
        value_forms = self.sample_field.enter_value_forms().clear()
        for value in values:
            self.__add_item_form(value_forms, str(value))
        return self

    def apply_default_configuration(self):
        self.set_values([0])
        return self

    def configure_for(self, db_entity):
        self.set_values(
            [s.strip() for s in db_entity.sample.split(',')] if (db_entity.sample is not None and db_entity.sample != '') else []
        )
        return self
    
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
        self.pdf_field.enter_new_distribution_value_form(
            db_entity.pdf,
            [s.strip() for s in db_entity.parameter_values.split(',')] if (db_entity.parameter_values is not None and db_entity.parameter_values != '') else []
        )
        return self
    
class CategoryFormsField(FormsField):

    def __init__(self, owner, prop_name, label):
        super(CategoryFormsField, self).__init__(owner, prop_name, label)
        self.__add_category_form(self.enter_form_definitions(), '')

    def __add_category_form(self, form_list, name):
        return form_list.enter_new_form('category', 'Category')\
            .enter_fields()\
                .enter_new_text_field('name', 'Name').set_value(name).exit()\
            .exit()

    def apply_default_configuration(self):
        return self

    def set_categories(self, category_names):
        value_forms = self.enter_value_forms().clear()
        for category_name in category_names:
            self.__add_category_form(value_forms, category_name)
        return self
    
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
    
# Distribution forms

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

class ExponentialDistributionForm(Form):

    #scale_field = None

    def __init__(self, owner):
        super(ExponentialDistributionForm, self).__init__(owner, 'exponentialDistribution', 'Exponential Distribution')
        self.scale_field = self.enter_fields().enter_new_text_field('scale', 'Scale (1 / lambda)')\
            .set_value(1)\
            .enter_number_config().enter_min_bound().set_value(0).set_inclusive(False)

    def set_scale(self, scale):
        self.scale_field.set_value(scale)
        return self

    def enter_scale_field(self):
        return self.scale_field

    def set_parameters(self, parameters):
        self.set_scale(parameters[0])
        return self
    
class GammaDistributionForm(Form):

    #shape_field = None
    #scale_field = None

    def __init__(self, owner):
        super(GammaDistributionForm, self).__init__(owner, 'gammaDistribution', 'Gamma Distribution')
        self.shape_field = self.enter_fields().enter_new_text_field('shape', 'Shape')\
            .set_value('0.5')\
            .enter_number_config()\
                .enter_min_bound()\
                    .set_value(0)\
                    .set_inclusive(False)\
                .exit()\
            .exit()
        self.shape_field = self.enter_fields().enter_new_text_field('scale', 'Scale') \
            .set_value('0.5') \
            .enter_number_config() \
               .enter_min_bound() \
                    .set_value(0) \
                    .set_inclusive(False) \
                .exit() \
            .exit()

    def set_shape(self, shape):
        self.shape_field.set_value(shape)
        return self

    def enter_shape_field(self):
        return self.shape_field

    def set_scale(self, scale):
        self.scale_field.set_value(scale)
        return self

    def enter_scale_field(self):
        return self.scale_field

    def set_parameters(self, parameters):
        self.set_shape(parameters[0])
        self.set_scale(parameters[1])
        return self

class GeometricDistributionForm(Form):

    #probability_field = None
    #size_field = None

    def __init__(self, owner):
        super(GeometricDistributionForm, self).__init__(owner, 'geometricDistribution', 'Geometric Distribution')
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

        self.size_field = self.enter_fields().enter_new_text_field('size', 'Size')\
            .set_value('1')\
            .enter_number_config()\
                .set_decimals(0)\
                .enter_min_bound()\
                    .set_value(0)\
                    .set_inclusive(True)\
                .exit()\
            .exit()

    def set_probability(self, probability):
        self.probability_field.set_value(probability)
        return self

    def enter_probability_field(self):
        return self.probability_field

    def set_size(self, size):
        self.size_field.set_value(size)
        return self

    def enter_size_field(self):
        return self.size_field

    def set_parameters(self, parameters):
        self.set_probability(parameters[0])
        self.set_size(parameters[1])
        return self
    
class NormalDistributionForm(Form):

    #mean_field = None
    #variance_field = None

    def __init__(self, owner):
        super(NormalDistributionForm, self).__init__(owner, 'normalDistribution', 'Normal Distribution')
        self.mean_field = self.enter_fields().enter_new_text_field('mean', 'Mean')\
            .set_value('0')\
            .enter_number_config().exit()

        self.variance_field = self.enter_fields().enter_new_text_field('variance', 'Variance')\
            .set_value('1')\
            .enter_number_config()\
                .enter_min_bound()\
                    .set_value(0)\
                    .set_inclusive(True)\
                .exit()\
            .exit()

    def set_mean(self, mean):
        self.mean_field.set_value(mean)
        return self

    def enter_mean_field(self):
        return self.mean_field

    def set_variance(self, variance):
        self.variance_field.set_value(variance)
        return self

    def enter_variance_field(self):
        return self.variance_field

    def set_parameters(self, parameters):
        self.set_mean(parameters[0])
        self.set_variance(parameters[1])
        return self
    
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

class TriangularDistributionForm(Form):

    #left_field = None
    #mode_field = None
    #right_field = None

    def __init__(self, owner):
        super(TriangularDistributionForm, self).__init__(owner, 'triangularDistribution', 'Triangular Distribution')
        self.left_field = self.enter_fields().enter_new_text_field('left', 'Left')\
            .set_value(0)\
            .enter_number_config()
        self.mode_field = self.enter_fields().enter_new_text_field('mode', 'Mode') \
            .set_value(0.5) \
            .enter_number_config()
        self.right_field = self.enter_fields().enter_new_text_field('right', 'Right') \
            .set_value(1) \
            .enter_number_config()

    def set_left(self, left):
        self.left_field.set_value(left)
        return self

    def enter_left_field(self):
        return self.left_field

    def set_mode(self, mode):
        self.mode_field.set_value(mode)
        return self

    def enter_mode_field(self):
        return self.mode_field

    def set_right(self, right):
        self.right_field.set_value(right)
        return self

    def enter_right_field(self):
        return self.right_field

    def set_parameters(self, parameters):
        self.set_left(parameters[0])
        self.set_mode(parameters[1])
        self.set_right(parameters[2])
        return self

class UniformDistributionForm(Form):

    #low_field = None
    #high_field = None

    def __init__(self, owner):
        super(UniformDistributionForm, self).__init__(owner, 'uniformDistribution', 'Uniform Distribution')
        self.low_field = self.enter_fields().enter_new_text_field('low', 'Low')\
            .set_value(0)\
            .enter_number_config()
        self.low_field = self.enter_fields().enter_new_text_field('high', 'High') \
            .set_value(1) \
            .enter_number_config()

    def set_low(self, low):
        self.low_field.set_value(low)
        return self

    def enter_low_field(self):
        return self.low_field

    def set_high(self, high):
        self.high_field.set_value(high)
        return self

    def enter_high_field(self):
        return self.high_field

    def set_parameters(self, parameters):
        self.set_low(parameters[0])
        self.set_high(parameters[1])
        return self
    
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

# Node

class NodeReference(object):

    #node_id
    #temp_id

    def __init__(self, owner):
        self.node_id = None
        self.temp_id = None

    def get_node_id(self):
        return self.node_id

    def set_node_id(self, node_id):
        self.node_id = node_id
        return self

    def get_temp_id(self):
        return self.temp_id

    def set_temp_id(self, temp_id):
        self.temp_id = temp_id
        return self

    def as_dictionary(self):
        return {
            'id': self.node_id,
            'tempId': self.temp_id
        }

    def exit(self):
        return self.owner
    
class Node(object):
    #owner = None

    #type_name = None
    #type_label = None

    #title_label_path = None
    #classes = None
    #out_connection_types = None
    #fields = None

    #title = None
    #node_id = None
    #temp_id = None
    #position = None
    #max_outgoing = -1
    #min_outgoing = 0
    #max_incoming = -1
    #min_incoming = 0
    #dirty = True

    def __init__(self, owner, type_name, type_label):
        self.title = None
        self.node_id = None
        self.temp_id = None
        self.position = None
        self.max_outgoing = -1
        self.min_outgoing = 0
        self.max_incoming = -1
        self.min_incoming = 0
        self.dirty = True

        self.owner = owner
        self.type_name = type_name
        self.type_label = type_label

        self.title_label_path = ValueList(self).append_item('name').append_item('valueData')
        self.classes = ValueList(self)
        self.out_connection_types = ValueList(self)
        self.fields = FieldList(self)

    def get_type_name(self):
        return self.type_name

    def get_type_label(self):
        return self.type_label

    def set_title(self, title):
        self.title = title
        return self

    def get_title(self):
        return self.title

    def enter_title_label_path(self):
        return self.title_label_path

    def set_node_id(self, node_id):
        self.node_id = node_id
        return self

    def get_node_id(self):
        return self.node_id

    def set_temp_id(self, temp_id):
        self.temp_id = temp_id

    def get_temp_id(self):
        return self.temp_id

    def enter_position(self):
        if self.position is None:
            self.position = Position(self)
        return self.position

    def set_position(self, x, y):
        self.position = Position(self).set_x(x).set_y(y)
        return self

    def enter_classes(self):
        return self.classes

    def enter_out_connection_types(self):
        return self.out_connection_types

    def set_max_outgoing(self, max_outgoing):
        self.max_outgoing = max_outgoing
        return self

    def get_max_outgoing(self):
        return self.max_outgoing

    def set_min_outgoing(self, min_outgoing):
        self.min_outgoing = min_outgoing
        return self

    def get_min_outgoing(self):
        return self.min_outgoing

    def set_max_incoming(self, max_incoming):
        self.max_incoming = max_incoming
        return self

    def get_max_incoming(self):
        return self.max_incoming

    def set_min_incoming(self, min_incoming):
        self.min_incoming = min_incoming
        return self

    def get_min_incoming(self):
        return self.min_incoming

    def set_outgoing_bounds(self, min_outgoing, max_outgoing):
        self.min_outgoing = min_outgoing
        self.max_outgoing = max_outgoing
        return self

    def set_incoming_bound(self, min_incoming, max_incoming):
        self.min_incoming = min_incoming
        self.max_incoming = max_incoming
        return self

    def set_dirty(self, dirty):
        self.dirty = dirty

    def get_dirty(self):
        return self.dirty

    def enter_fields(self):
        return self.fields

    def as_dictionary(self):
        return {
            'title': self.title,
            'titleLabelPath': self.title_label_path.as_list(),
            'typeName': self.type_name,
            'typeLabel': self.type_label,
            'id': self.node_id,
            'tempId': self.temp_id,
            'position': self.position.as_dictionary() if self.position is not None else None,
            'classes': self.classes.as_list(),
            'maxOutgoing': self.max_outgoing,
            'minOutgoing': self.min_outgoing,
            'maxIncoming': self.max_incoming,
            'minIncoming': self.min_incoming,
            'outConnectionTypes': self.out_connection_types.as_list(),
            'dirty': self.dirty,
            'fields': self.fields.as_list()
        }

    def set_owner(self, owner):
        self.owner = owner

    def exit(self):
        return self.owner
    
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

        for db_base_inflow in models.fixed_value_inflow.objects.filter(external_function_inflow=db_entity):
            self.basic_inflow_field.enter_value_forms().append_and_enter(FixedValueInflowForm(None).configure_for(db_base_inflow))
        for db_base_inflow in models.random_choice_inflow.objects.filter(external_function_inflow=db_entity):
            self.basic_inflow_field.enter_value_forms().append_and_enter(RandomChoiceInflowForm(None).configure_for(db_base_inflow))
        for db_base_inflow in models.stochastic_function_inflow.objects.filter(external_function_inflow=db_entity):
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

        db_fixed_value_inflows = models.fixed_value_inflow.objects.filter(external_list_inflow=db_entity)
        db_random_choice_inflows = models.random_choice_inflow.objects.filter(external_list_inflow=db_entity)
        db_stochastic_function_inflows = models.stochastic_function_inflow.objects.filter(external_list_inflow=db_entity)

        db_single_period_inflows = list(itertools.chain(db_fixed_value_inflows, db_random_choice_inflows, db_stochastic_function_inflows))
        db_single_period_inflows.sort(key=lambda x : x.period)

        for db_single_period_inflow in db_single_period_inflows:
            if (isinstance(db_single_period_inflow, models.fixed_value_inflow)):
                self.single_period_inflows_field.enter_value_forms().append_and_enter(FixedValueInflowForm(None).configure_for(db_single_period_inflow))
            elif (isinstance(db_single_period_inflow, models.random_choice_inflow)):
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
    
class FlowCompartment(Node):

    #name_field = None
    #description_field = None
    #log_inflows_field = None

    #log_outflows_field = None
    #adjust_outgoing_tcs_field = None

    #categories_field = None

    def __init__(self, owner):
        super(FlowCompartment, self).__init__(owner, 'flowCompartment', 'Flow Compartment')

        self.enter_classes().append_item('compartment').append_item('flow-compartment')
        self.enter_out_connection_types()\
            .append_item('constantTransfer')\
            .append_item('randomChoiceTransfer')\
            .append_item('stochasticTransfer')
        #    .append_item('aggregatedTransfer')

        self.set_min_outgoing(1)
        self.set_min_incoming(1)

        fields = self.enter_fields()
        self.name_field = fields.enter_new_text_field('name', 'Name').set_value('New Flow Compartment')
        self.description_field = fields.enter_new_text_field('description', 'Description')\
            .set_display_as_text_area(True).set_not_empty(False)
        self.log_inflows_field = fields.enter_new_check_field('logInflows', 'Log Inflows')
        self.log_outflows_field = fields.enter_new_check_field('logOutflows', 'Log Outflows')
        self.adjust_outgoing_tcs_field = fields.enter_new_check_field('adjustOutgoingTcs', 'Adjust Outgoing Transfer Coefficients')
        self.categories_field = fields.append_and_enter(CategoryFormsField(None, 'categories', 'Categories'))

    def configure_for(self, db_entity):
        self.set_node_id('compartment_' + str(db_entity.pk))
        self.set_position(db_entity.x, db_entity.y)

        self.name_field.set_value(db_entity.name)
        self.description_field.set_value(db_entity.description)
        self.log_inflows_field.set_checked(db_entity.log_inflows)
        self.log_outflows_field.set_checked(db_entity.log_outflows)
        self.adjust_outgoing_tcs_field.set_checked(db_entity.adjust_outgoing_tcs)
        self.categories_field.set_categories([s.strip() for s in db_entity.categories.split(',')] if (db_entity.categories is not None and db_entity.categories != '') else [])

        return self

    def apply_default_configuration(self):
        self.log_inflows_field.set_checked(True)
        self.log_outflows_field.set_checked(True)
        self.adjust_outgoing_tcs_field.set_checked(True)
        self.categories_field.apply_default_configuration()
        return self

    def enter_name_field(self):
        return self.name_field

    def enter_description_field(self):
        return self.description_field

    def enter_log_inflows_field(self):
        return self.log_inflows_field

    def enter_log_outflows_field(self):
        return self.log_outflows_field

    def enter_adjust_outgoing_tcs_field(self):
        return self.adjust_outgoing_tcs_field

    def enter_categories_field(self):
        return self.categories_field

class Stock(Node):

    #name_field = None
    #description_field = None
    #log_inflows_field = None

    #log_outflows_field = None
    #adjust_outgoing_tcs_field = None

    #categories_field = None

    #local_release_field = None

    def __init__(self, owner):
        super(Stock, self).__init__(owner, 'stock', 'Stock')

        self.enter_classes().append_item('compartment').append_item('stock')
        self.enter_out_connection_types()\
            .append_item('constantTransfer')\
            .append_item('randomChoiceTransfer')\
            .append_item('stochasticTransfer')
        #    .append_item('aggregatedTransfer')

        self.set_min_outgoing(1)
        self.set_min_incoming(1)

        fields = self.enter_fields()
        self.name_field = fields.enter_new_text_field('name', 'Name').set_value('New Stock')
        self.description_field = fields.enter_new_text_field('description', 'Description')\
            .set_display_as_text_area(True).set_not_empty(False)
        self.log_inflows_field = fields.enter_new_check_field('logInflows', 'Log Inflows')
        self.log_outflows_field = fields.enter_new_check_field('logOutflows', 'Log Outflows')
        self.adjust_outgoing_tcs_field = fields.enter_new_check_field('adjustOutgoingTcs', 'Adjust Outgoing Transfer Coefficients')
        self.categories_field = fields.append_and_enter(CategoryFormsField(None, 'categories', 'Categories'))
        self.local_release_field = fields.append_and_enter(LocalReleaseFormsField(None, 'localRelease', 'Local Release'))

    def configure_for(self, db_entity):
        self.set_node_id('compartment_' + str(db_entity.pk))
        self.set_position(db_entity.x, db_entity.y)

        self.name_field.set_value(db_entity.name)
        self.description_field.set_value(db_entity.description)
        self.log_inflows_field.set_checked(db_entity.log_inflows)
        self.log_outflows_field.set_checked(db_entity.log_outflows)
        self.adjust_outgoing_tcs_field.set_checked(db_entity.adjust_outgoing_tcs)
        self.categories_field.set_categories([s.strip() for s in db_entity.categories.split(',')] if (db_entity.categories is not None and db_entity.categories != '') else [])

        self.local_release_field.configure_for_stock(db_entity)

        return self

    def apply_default_configuration(self):
        self.log_inflows_field.set_checked(True)
        self.log_outflows_field.set_checked(True)
        self.adjust_outgoing_tcs_field.set_checked(True)
        self.categories_field.apply_default_configuration()
        self.local_release_field.apply_default_configuration()
        return self

    def enter_name_field(self):
        return self.name_field

    def enter_description_field(self):
        return self.description_field

    def enter_log_inflows_field(self):
        return self.log_inflows_field

    def enter_log_outflows_field(self):
        return self.log_outflows_field

    def enter_adjust_outgoing_tcs_field(self):
        return self.adjust_outgoing_tcs_field

    def enter_categories_field(self):
        return self.categories_field

class Sink(Node):

    # name_field = None
    # description_field = None
    # log_inflows_field = None

    # categories_field = None

    def __init__(self, owner):
        super(Sink, self).__init__(owner, 'sink', 'Sink')

        self.enter_classes().append_item('compartment').append_item('sink')

        self.set_max_outgoing(0)
        self.set_min_outgoing(0)
        self.set_min_incoming(1)

        fields = self.enter_fields()
        self.name_field = fields.enter_new_text_field('name', 'Name').set_value('New Sink')
        self.description_field = fields.enter_new_text_field('description', 'Description') \
            .set_display_as_text_area(True).set_not_empty(False)
        self.log_inflows_field = fields.enter_new_check_field('logInflows', 'Log Inflows')
        self.categories_field = fields.append_and_enter(CategoryFormsField(None, 'categories', 'Categories'))

    def configure_for(self, db_entity):
        self.set_node_id('compartment_' + str(db_entity.pk))
        self.set_position(db_entity.x, db_entity.y)

        self.name_field.set_value(db_entity.name)
        self.description_field.set_value(db_entity.description)
        self.log_inflows_field.set_checked(db_entity.log_inflows)
        self.categories_field.set_categories([s.strip() for s in db_entity.categories.split(',')] if (db_entity.categories is not None and db_entity.categories != '') else [])

        return self

    def apply_default_configuration(self):
        self.log_inflows_field.set_checked(True)
        self.categories_field.apply_default_configuration()
        return self

    def enter_name_field(self):
        return self.name_field

    def enter_description_field(self):
        return self.description_field

    def enter_log_inflows_field(self):
        return self.log_inflows_field

    def enter_categories_field(self):
        return self.categories_field
    
# Connection

class Connection(object):

    def __init__(self, owner, type_name, type_label):
        self.owner = owner

        self.type_name = type_name
        self.type_label = type_label

        self.connection_id = None
        self.temp_id = None

        self.title = ''
        self.title_label_path = None

        self.target_node = None
        self.source_node = None

        self.fields = FieldList(self)

        self.dirty = True

    def apply_default_configuration(self):
        return self

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def enter_title_label_path(self):
        if self.title_label_path is None:
            self.title_label_path = ValueList(self)
        return self.title_label_path

    def set_type_name(self, type_name):
        self.type_name = type_name
        return self

    def enter_source_node(self):
        if self.source_node is None:
            self.source_node = NodeReference(self)
        return self.source_node

    def enter_target_node(self):
        if self.target_node is None:
            self.target_node = NodeReference(self)
        return self.target_node

    def set_source_node_id(self, node_id):
        self.enter_source_node().set_node_id(node_id)
        return self

    def set_target_node_id(self, node_id):
        self.enter_target_node().set_node_id(node_id)
        return self

    def get_type_name(self):
        return self.type_name

    def set_type_label(self, type_label):
        self.type_label = type_label
        return self

    def get_type_label(self):
        return self.type_label

    def set_connection_id(self, connection_id):
        self.connection_id = connection_id
        return self

    def get_connection_id(self):
        return self.connection_id

    def set_temp_id(self, temp_id):
        self.temp_id = temp_id
        return self

    def get_temp_if(self):
        return self.temp_id

    def enter_fields(self):
        return self.fields

    def as_dictionary(self):
        return {
            'title': self.title,
            'titleLabelPath': self.title_label_path.as_list() if self.title_label_path is not None else None,
            'typeName': self.type_name,
            'typeLabel': self.type_label,
            'id': self.connection_id,
            'tempId': self.temp_id,
            'targetNode': self.target_node.as_dictionary() if self.target_node is not None else None,
            'sourceNode': self.source_node.as_dictionary() if self.source_node is not None else None,
            'dirty': self.dirty,
            'fields': self.fields.as_list()
        }

    def exit(self):
        return self.owner
    
class InflowTargetConnection(Connection):

    def __init__(self, owner):
        super(InflowTargetConnection, self).__init__(owner, 'inflowTarget', 'Inflow Target')
        
class TransferConnection(Connection):

    # name_field
    # priority_field

    def __init__(self, owner, type_name, type_label):
        super(TransferConnection, self).__init__(owner, type_name, type_label)
        self.title_label_path = ValueList(self).append_item('name').append_item('valueData')

        fields = self.enter_fields()
        self.name_field = fields.enter_new_text_field('name', 'Name').set_value('New Transfer')
        self.priority_field = fields.enter_new_text_field('priority', 'Priority')\
            .enter_number_config() \
                .enter_min_bound().set_value(0).set_inclusive(True).exit()\
            .exit()

    def set_name(self, value):
        self.name_field.set_value(value)
        return self

    def set_priority(self, priority):
        self.priority_field.set_value(priority)
        return self
    
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
    
class ConstantTransferConnection(TransferConnection):

    # value_field

    def __init__(self, owner):
        super(ConstantTransferConnection, self).__init__(owner, 'constantTransfer', 'Constant Transfer')

        fields = self.enter_fields()
        self.value_field = fields.enter_new_text_field('value', 'Value')\
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

    def apply_default_configuration(self):
        self.set_name('New Constant Transfer')
        self.set_priority(0)
        self.set_value(0.5)
        return self

    def configure_for(self, db_entity):
        self.set_source_node_id('compartment_' + str(db_entity.source_flow_compartment.pk))
        self.set_target_node_id('compartment_' + str(db_entity.target.pk))
        self.set_name(db_entity.name)
        self.set_priority(db_entity.priority)
        self.set_value(db_entity.value)
        return self

    def set_value(self, value):
        self.value_field.set_value(value)
        
class RandomChoiceTransferConnection(TransferConnection):

    # sample_field

    def __init__(self, owner):
        super(RandomChoiceTransferConnection, self).__init__(owner, 'randomChoiceTransfer', 'Random Choice Transfer')

        fields = self.enter_fields()
        self.sample_field = self.fields.enter_new_forms_field('sample', 'Sample').set_min_forms(1)
        self.__add_item_form(self.sample_field.enter_form_definitions(), '0')

    def __add_item_form(self, form_list, value):
        return form_list.enter_new_form('item', 'Item')\
            .enter_title_template().clear().append_item('Item ').append_item('positionOneBased').exit()\
            .enter_fields()\
                .enter_new_text_field('value', 'Value').set_value(value).exit()\
            .exit()

    def set_values(self, values):
        value_forms = self.sample_field.enter_value_forms().clear()
        for value in values:
            self.__add_item_form(value_forms, str(value))
        return self

    def apply_default_configuration(self):
        self.set_name('New Random Choice Transfer')
        self.set_priority(0)
        self.set_values([0.5])
        return self

    def configure_for(self, db_entity):
        self.set_source_node_id('compartment_' + str(db_entity.source_flow_compartment.pk))
        self.set_target_node_id('compartment_' + str(db_entity.target.pk))
        self.set_name(db_entity.name)
        self.set_priority(db_entity.priority)
        self.set_values([s.strip() for s in db_entity.sample.split(',')] if (db_entity.sample is not None and db_entity.sample != '') else [])
        return self
