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
