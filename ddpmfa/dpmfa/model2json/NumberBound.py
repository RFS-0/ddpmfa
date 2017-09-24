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
