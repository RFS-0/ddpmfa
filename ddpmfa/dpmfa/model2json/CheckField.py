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
