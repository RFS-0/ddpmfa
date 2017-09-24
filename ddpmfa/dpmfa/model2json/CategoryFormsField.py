from dpmfa.model2json.FormsField import FormsField


class CategoryFormsField(FormsField):

    def __init__(self, owner, prop_name, label):
        super(CategoryFormsField, self).__init__(owner, prop_name, label)
        self.__add_category_form(self.enter_form_definitions(), '')

    def __add_category_form(self, form_list, name):
        return form_list.enter_new_form('category', 'Category')\
            .enter_fields()\
                .enter_new_text_field('name', 'Name').set_value(name).exit()\
            .exit()

    def apply_default_configuration(self):
        return self

    def set_categories(self, category_names):
        value_forms = self.enter_value_forms().clear()
        for category_name in category_names:
            self.__add_category_form(value_forms, category_name)
        return self
