""" This class contains custom validators for the dpmfa app """

from django.core.validators import _lazy_re_compile
from django.core.validators import RegexValidator
import re

def float_list_validator(sep=',', message=None, allow_negative=False, code='invalid'):
    comma_separated_float_list_re = re.compile('^([-+]?\d*\.?\d+[,\s]*)+$')
    
    validate_comma_separated_float_list = RegexValidator(
              comma_separated_float_list_re, _(u'Enter only floats separated by commas.'), 'invalid')
    
    return validate_comma_separated_float_list

def alpha_numeric_list_validator(sep=',', message=None, code='invalid'):
    regexp = _lazy_re_compile(r'^[A-Za-z0-9_]+(?:%(sep)s[A-Za-z0-9_]+)*\Z' % {
        'sep': re.escape(sep),
    })
    print("validate alpha num list")
    return RegexValidator(regexp, message=message, code=code)

# TODO [all]: we will have to implement a float list validator