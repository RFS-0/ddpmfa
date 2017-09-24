from dpmfa.model2json.CheckField import CheckField
from dpmfa.model2json.FormsField import FormsField
from dpmfa.model2json.TextField import TextField


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
