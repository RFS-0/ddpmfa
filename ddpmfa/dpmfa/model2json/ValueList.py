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
