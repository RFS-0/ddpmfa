#from dpmfa.model2json.Form import Form
import dpmfa


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
        form = dpmfa.model2json.Form.Form(self, form_type, label)
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
