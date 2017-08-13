import math

# Functions available as input for dpmfa classes

def function_by_name(name, args):
    if name == 'LI':
        return LinearFunction(*args)
    elif name == 'PO':
        return PolynomialFunction(args)
    elif name == 'EX':
        return ExponentialFunction(*args)
    elif name == 'LG':
        return LogarithmFunction(*args)
    elif name == 'SI':
        return SineFunction(*args)
    elif name == 'CO':
        return CosineFunction(*args)
    else:
        return None

class LinearFunction(object):

    def __init__(self, intercept, slope):
        self.intercept = intercept
        self.slope = slope

    def __call__(self, x):
        return self.intercept + x * self.slope

class PolynomialFunction(object):

    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __call__(self, x):
        result = 0
        for coefficient in self.coefficients:
            result = result * x + coefficient
        return result

class ExponentialFunction(object):

    def __init__(self, factor, base, exponent_factor, exponent_shift):
        self.factor = factor
        self.base = base
        self.exponent_factor = exponent_factor
        self.exponent_shift = exponent_shift

    def __call__(self, x):
        return self.factor * self.base ** (self.exponent_factor * x + self.exponent_shift)

class LogarithmFunction(object):

    def __init__(self, factor, base, arg_factor, arg_shift):
        self.factor = factor
        self.base = base
        self.arg_factor = arg_factor
        self.arg_shift = arg_shift

    def __call__(self, x):
        return self.factor * math.log(self.arg_factor * x + self.arg_shift, self.base)

class SineFunction(object):

    def __init__(self, amplitude, frequency, phase):
        self.amplitude = amplitude
        self.frequency = frequency
        self.phase = phase

    def __call__(self, x):
        return self.amplitude * math.sin(2 * math.pi * self.frequency * x + self.phase)

class CosineFunction(object):

    def __init__(self, amplitude, frequency, phase):
        self.amplitude = amplitude
        self.frequency = frequency
        self.phase = phase

    def __call__(self, x):
        return self.amplitude * math.cos(2 * math.pi * self.frequency * x + self.phase)
