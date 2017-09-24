from dpmfa.model2json.FieldList import FieldList
from dpmfa.model2json.ValueList import ValueList


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
