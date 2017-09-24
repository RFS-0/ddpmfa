from dpmfa.model2json.FormList import FormList


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
