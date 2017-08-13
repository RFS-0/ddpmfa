from django import template
register = template.Library()



@register.filter(name='underline_to_ws')
def underline_to_ws(value):
    return value.replace('_', ' ')