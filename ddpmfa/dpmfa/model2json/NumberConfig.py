from dpmfa.model2json.NumberBound import NumberBound


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
