""" This class contains custom validators for the dpmfa app """

from django.core.validators import _lazy_re_compile
from django.core.validators import RegexValidator

def alpha_numeric_list_validator(sep=',', message=None, code='invalid'):
    regexp = _lazy_re_compile(r'^[A-Za-z0-9_]+(?:%(sep)s[A-Za-z0-9_]+)*\Z' % {
        'sep': re.escape(sep),
    })
    print("validate alpha num list")
    return RegexValidator(regexp, message=message, code=code)

# TODO [all]: we will have to implement a float list validator