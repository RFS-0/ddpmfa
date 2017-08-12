from django import template
register = template.Library()



@register.filter(name='underline_to_minus')
def underline_to_minus(value):
    return value.replace('_', '-')