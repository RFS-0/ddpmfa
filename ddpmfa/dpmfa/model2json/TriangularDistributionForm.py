from dpmfa.model2json.Form import Form


class TriangularDistributionForm(Form):

    #left_field = None
    #mode_field = None
    #right_field = None

    def __init__(self, owner):
        super(TriangularDistributionForm, self).__init__(owner, 'triangularDistribution', 'Triangular Distribution')
        self.left_field = self.enter_fields().enter_new_text_field('left', 'Left')\
            .set_value(0)\
            .enter_number_config()
        self.mode_field = self.enter_fields().enter_new_text_field('mode', 'Mode') \
            .set_value(0.5) \
            .enter_number_config()
        self.right_field = self.enter_fields().enter_new_text_field('right', 'Right') \
            .set_value(1) \
            .enter_number_config()

    def set_left(self, left):
        self.left_field.set_value(left)
        return self

    def enter_left_field(self):
        return self.left_field

    def set_mode(self, mode):
        self.mode_field.set_value(mode)
        return self

    def enter_mode_field(self):
        return self.mode_field

    def set_right(self, right):
        self.right_field.set_value(right)
        return self

    def enter_right_field(self):
        return self.right_field

    def set_parameters(self, parameters):
        self.set_left(parameters[0])
        self.set_mode(parameters[1])
        self.set_right(parameters[2])
        return self
