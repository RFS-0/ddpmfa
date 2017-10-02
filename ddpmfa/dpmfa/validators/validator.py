""" This class contains custom validators for the dpmfa app """

from django.core.validators import _lazy_re_compile
from django.core.validators import RegexValidator
import re

def float_list_validator(sep=',', message=None, allow_negative=False, code='invalid'):
    comma_separated_float_list_re = re.compile('^([-+]?\d*\.?\d+[,\s]*)+$')
    
    validate_comma_separated_float_list = RegexValidator(
              comma_separated_float_list_re, (u'Enter only floats separated by commas.'), 'invalid')
    
    return validate_comma_separated_float_list

# TODO [all]: we will have to implement a float list validator