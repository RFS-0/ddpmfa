from django import template
register = template.Library()



@register.filter(name='prepend')
def prepend(value, prefix):
    return '%s%s' % (prefix, value)