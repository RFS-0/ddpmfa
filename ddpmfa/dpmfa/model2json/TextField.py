from dpmfa.model2json.NumberConfig import NumberConfig


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
