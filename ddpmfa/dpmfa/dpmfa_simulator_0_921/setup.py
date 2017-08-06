# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 11:48:16 2015

@author: bni
"""

from setuptools import setup

setup(name='dpmfa-simulator',
      version='0.921',
      description='A framework for dynamic probabilistic material flow analysis',
#      url='http://github.com/NikolausBornhoeft/dpmfa',
      author='Nikolaus Bornhoeft',
      author_email='Nikolaus.Bornhoeft@empa.ch',
      license='Apache License Version 2.0',
      packages=['dpmfa_simulator', 'example'],
      keywords = ['Bayesian modeling, material flow modeling, environmental modeling, exposure assessment modeling'],
      zip_safe=False)