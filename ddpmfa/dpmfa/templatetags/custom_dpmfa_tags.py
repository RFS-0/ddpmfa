from django import template
register = template.Library()

@register.filter(name='get_class')
def get_class(value):
    return value.__class__.__name__

@register.filter(name='lookup')
def getValue(dictionary, key):
    return dictionary[key]

@register.filter(name='prepend')
def prepend(value, prefix):
    return '%s%s' % (prefix, value)

@register.filter(name='underline_to_minus')
def underline_to_minus(value):
    return value.replace('_', '-')

@register.filter(name='underline_to_ws')
def underline_to_ws(value):
    return value.replace('_', ' ')