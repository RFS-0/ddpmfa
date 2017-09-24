import dpmfa.models as dmb

class NormalDistributionScaffold(object):
    mean = 0
    variance = 1

    def set_mean(self, mean):
        self.mean = mean
        return self

    def set_variance(self, variance):
        self.variance = variance
        return self

class ModelJson(object):



    @staticmethod
    def model_to_dict(model):
        # Step 1: Assemble dictionaries for all entities that are displayed as node

        node_dicts = []

        for external_list_inflow in dmb.external_list_inflow.objects.filter(target__model=model):
            print(external_list_inflow)

        print(node_dicts)


    @staticmethod
    def get_model_scaffold():
        data = {
            'id': None,
            'valid': True,
            'cyclesAllowed': False,
            'parallelsAllowed': False,

            'nodes': [],

            'connections': [],

            'nodeTypes': [
                ModelJson.get_external_list_inflow_scaffold(True, True),
                {  # start: externalFunctionInflow
                    'title': None,
                    'titleLabelPath': ['name', 'valueData'],
                    'typeName': 'externalFunctionInflow',
                    'typeLabel': 'External Function Inflow',
                    'id': None,
                    'tempId': None,
                    'position': None,
                    'classes': ['inflow', 'external-function-inflow'],
                    'maxOutgoing': 1,
                    'minOutgoing': 1,
                    'maxIncoming': 0,
                    'minIncoming': 0,
                    'outConnectionTypes': ['inflowTarget'],
                    'dirty': True,
                    'fields': [  # start: externalFunctionInflow/fields
                        {  # start: externalFunctionInflow/fields/name
                            'fieldType': 'TEXT',
                            'fieldArgs': {
                                'displayAsTextArea': False,
                                'notEmpty': True,
                                'maxLength': 250,
                                'numberConfig': None
                            },
                            'propName': 'name',
                            'label': 'Name',
                            'valueData': 'New External List Inflow',
                            'dirty': True
                        },  # end: externalFunctionInflow/fields/name
                        {  # start: externalFunctionInflow/fields/startDelay
                            'fieldType': 'TEXT',
                            'fieldArgs': {
                                'displayAsTextArea': False,
                                'notEmpty': True,
                                'maxLength': 250,
                                'numberConfig': {
                                    'decimals': 0,
                                    'min': {
                                        'value': 0,
                                        'inclusive': True
                                    },
                                    'max': None
                                }
                            },
                            'propName': 'startDelay',
                            'label': 'Start Delay',
                            'valueData': '0',
                            'dirty': True
                        },  # end: externalFunctionInflow/fields/startDelay
                        {  # start: externalFunctionInflow/fields/derivationDistribution
                            'fieldType': 'FORMS',
                            'fieldArgs': {
                                'minForms': 0,
                                'maxForms': 1,
                                'forms': [  # start: externalFunctionInflow/fields/derivationDistribution/fieldArgs/forms
                                    { # start: externalFunctionInflow/fields/derivationDistribution/fieldArgs/forms/normalDistribution
                                        'id': None,
                                        'tempId': None,
                                        'label': 'Normal Distribution',
                                        'type': 'normalDistribution',
                                        'titleTemplate': ['', 'label'],
                                        'dirty': True,
                                        'fields': [ # start: externalFunctionInflow/fields/derivationDistribution/fieldArgs/forms/normalDistribution/fields
                                            { # start: externalFunctionInflow/fields/derivationDistribution/fieldArgs/forms/normalDistribution/fields/mean
                                                'fieldType': 'TEXT',
                                                'fieldArgs': {
                                                    'displayAsTextArea': False,
                                                    'notEmpty': True,
                                                    'maxLength': 250,
                                                    'numberConfig': {
                                                        'decimals': -1,
                                                        'min': None,
                                                        'max': None
                                                    }
                                                },
                                                'propName': 'mean',
                                                'label': 'Mean',
                                                'valueData': '0',
                                                'dirty': True
                                            }, # end: externalFunctionInflow/fields/derivationDistribution/fieldArgs/forms/normalDistribution/fields/mean
                                            { # start: externalFunctionInflow/fields/derivationDistribution/fieldArgs/forms/normalDistribution/fields/variance
                                                'fieldType': 'TEXT',
                                                'fieldArgs': {
                                                    'displayAsTextArea': False,
                                                    'notEmpty': True,
                                                    'maxLength': 250,
                                                    'numberConfig': {
                                                        'decimals': -1,
                                                        'min': {
                                                            'value': 0,
                                                            'inclusive': True
                                                        },
                                                        'max': None
                                                    }
                                                },
                                                'propName': 'variance',
                                                'label': 'Variance',
                                                'valueData': '1',
                                                'dirty': True
                                            } # end: externalFunctionInflow/fields/derivationDistribution/fieldArgs/forms/normalDistribution/fields/variance
                                        ] # end: externalFunctionInflow/fields/derivationDistribution/fieldArgs/forms/normalDistribution/fields
                                    }, # end: externalFunctionInflow/fields/derivationDistribution/fieldArgs/forms/normalDistribution
                                    { # start: externalFunctionInflow/fields/derivationDistribution/fieldArgs/forms/triangularDistribution
                                        'id': None,
                                        'tempId': None,
                                        'label': 'Triangular Distribution',
                                        'type': 'triangularDistribution',
                                        'titleTemplate': ['', 'label'],
                                        'dirty': True,
                                        'fields': [ # start: externalFunctionInflow/fields/derivationDistribution/fieldArgs/forms/triangularDistribution/fields
                                            { # start: externalFunctionInflow/fields/derivationDistribution/fieldArgs/forms/triangularDistribution/fields/left
                                                'fieldType': 'TEXT',
                                                'fieldArgs': {
                                                    'displayAsTextArea': False,
                                                    'notEmpty': True,
                                                    'maxLength': 250,
                                                    'numberConfig': {
                                                        'decimals': -1,
                                                        'min': None,
                                                        'max': None
                                                    }
                                                },
                                                'propName': 'left',
                                                'label': 'Left',
                                                'valueData': '0',
                                                'dirty': True
                                            }, # end: externalFunctionInflow/fields/derivationDistribution/fieldArgs/forms/triangularDistribution/fields/left
                                            { # start: externalFunctionInflow/fields/derivationDistribution/fieldArgs/forms/triangularDistribution/fields/mode
                                                'fieldType': 'TEXT',
                                                'fieldArgs': {
                                                    'displayAsTextArea': False,
                                                    'notEmpty': True,
                                                    'maxLength': 250,
                                                    'numberConfig': {
                                                        'decimals': -1,
                                                        'min': None,
                                                        'max': None
                                                    }
                                                },
                                                'propName': 'mode',
                                                'label': 'Mode',
                                                'valueData': '0.5',
                                                'dirty': True
                                            }, # end: externalFunctionInflow/fields/derivationDistribution/fieldArgs/forms/triangularDistribution/fields/mode
                                            { # start: externalFunctionInflow/fields/derivationDistribution/fieldArgs/forms/triangularDistribution/fields/right
                                                'fieldType': 'TEXT',
                                                'fieldArgs': {
                                                    'displayAsTextArea': False,
                                                    'notEmpty': True,
                                                    'maxLength': 250,
                                                    'numberConfig': {
                                                        'decimals': -1,
                                                        'min': None,
                                                        'max': None
                                                    }
                                                },
                                                'propName': 'right',
                                                'label': 'Right',
                                                'valueData': '1',
                                                'dirty': True
                                            } # end: externalFunctionInflow/fields/derivationDistribution/fieldArgs/forms/triangularDistribution/fields/right
                                        ] # end: externalFunctionInflow/fields/derivationDistribution/fieldArgs/forms/triangularDistribution/fields
                                    }, # start: externalFunctionInflow/fields/derivationDistribution/fieldArgs/forms/triangularDistribution
                                    { # start: externalFunctionInflow/fields/derivationDistribution/fieldArgs/forms/uniformDistribution
                                        'id': None,
                                        'tempId': None,
                                        'label': 'Uniform Distribution',
                                        'type': 'uniformDistribution',
                                        'titleTemplate': ['', 'label'],
                                        'dirty': True,
                                        'fields': [ # start: externalFunctionInflow/fields/derivationDistribution/fieldArgs/forms/uniformDistribution/fields
                                            { # start: externalFunctionInflow/fields/derivationDistribution/fieldArgs/forms/uniformDistribution/fields/low
                                                'fieldType': 'TEXT',
                                                'fieldArgs': {
                                                    'displayAsTextArea': False,
                                                    'notEmpty': True,
                                                    'maxLength': 250,
                                                    'numberConfig': {
                                                        'decimals': -1,
                                                        'min': None,
                                                        'max': None
                                                    }
                                                },
                                                'propName': 'low',
                                                'label': 'Low',
                                                'valueData': '0',
                                                'dirty': True
                                            }, # end: externalFunctionInflow/fields/derivationDistribution/fieldArgs/forms/uniformDistribution/fields/low
                                            { # start: externalFunctionInflow/fields/derivationDistribution/fieldArgs/forms/uniformDistribution/fields/high
                                                'fieldType': 'TEXT',
                                                'fieldArgs': {
                                                    'displayAsTextArea': False,
                                                    'notEmpty': True,
                                                    'maxLength': 250,
                                                    'numberConfig': {
                                                        'decimals': -1,
                                                        'min': None,
                                                        'max': None
                                                    }
                                                },
                                                'propName': 'high',
                                                'label': 'High',
                                                'valueData': '1',
                                                'dirty': True
                                            } # end: externalFunctionInflow/fields/derivationDistribution/fieldArgs/forms/uniformDistribution/fields/high
                                        ] # end: externalFunctionInflow/fields/derivationDistribution/fieldArgs/forms/uniformDistribution/fields
                                    }, # start: externalFunctionInflow/fields/derivationDistribution/fieldArgs/forms/uniformDistribution
                                    { # start: externalFunctionInflow/fields/derivationDistribution/fieldArgs/forms/exponentialDistribution
                                        'id': None,
                                        'tempId': None,
                                        'label': 'Exponential Distribution',
                                        'type': 'exponentialDistribution',
                                        'titleTemplate': ['', 'label'],
                                        'dirty': True,
                                        'fields': [ # start: externalFunctionInflow/fields/derivationDistribution/fieldArgs/forms/exponentialDistribution/fields
                                            { # start: externalFunctionInflow/fields/derivationDistribution/fieldArgs/forms/exponentialDistribution/fields/scale
                                                'fieldType': 'TEXT',
                                                'fieldArgs': {
                                                    'displayAsTextArea': False,
                                                    'notEmpty': True,
                                                    'maxLength': 250,
                                                    'numberConfig': {
                                                        'decimals': -1,
                                                        'min': {
                                                            'value': 0,
                                                            'inclusive': False
                                                        },
                                                        'max': None
                                                    }
                                                },
                                                'propName': 'scale',
                                                'label': 'Scale (1 / lambda)',
                                                'valueData': '1',
                                                'dirty': True
                                            }, # end: externalFunctionInflow/fields/derivationDistribution/fieldArgs/forms/exponentialDistribution/fields/scale
                                        ] # end: externalFunctionInflow/fields/derivationDistribution/fieldArgs/forms/exponentialDistribution/fields
                                    } # end: externalFunctionInflow/fields/derivationDistribution/fieldArgs/forms/exponentialDistribution

                                    # TODO: more distributions
                                ]  # end: externalFunctionInflow/fields/derivationDistribution/fieldArgs/forms
                            },  # end: externalFunctionInflow/fields/derivationDistribution/fieldArgs
                            'propName': 'derivationDistribution',
                            'label': 'Derivation Distribution',
                            'valueData': [],
                            'dirty': True
                        },  # end: externalFunctionInflow/fields/derivationDistribution
                        {  # start: externalFunctionInflow/fields/derivationFactor
                            'fieldType': 'TEXT',
                            'fieldArgs': {
                                'displayAsTextArea': False,
                                'notEmpty': True,
                                'maxLength': 250,
                                'numberConfig': {
                                    'decimals': -1,
                                    'min': None,
                                    'max': None
                                    # TODO: limits for derivationFactor
                                }
                            },
                            'propName': 'derivationFactor',
                            'label': 'Derivation Factor',
                            'valueData': '1',
                            'dirty': True
                        },  # end: externalFunctionInflow/fields/derivationFactor
                        # TODO: real inflow function field (function field and parameter field)
                        { # start: externalFunctionInflow/fields/inflowFunction
                            'fieldType': 'TEXT',
                            'fieldArgs': {
                                'displayAsTextArea': False,
                                'notEmpty': True,
                                'maxLength': 250,
                                'numberConfig': None
                            },
                            'propName': 'inflowFunction',
                            'label': 'Inflow Function',
                            'valueData': 'baseValue + period * 100',
                            'dirty': True
                        },  # end: externalFunctionInflow/fields/inflowFunction
                        {  # start: externalFunctionInflow/fields/basicInflow
                            'fieldType': 'FORMS',
                            'fieldArgs': {  # start: externalFunctionInflow/fields/basicInflow/fieldArgs
                                'minForms': 1,
                                'maxForms': 1,
                                'forms': [  # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms
                                    { # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/fixedValueInflow
                                        'id': None,
                                        'tempId': None,
                                        'label': 'Fixed Value Inflow',
                                        'type': 'fixedValueInflow',
                                        'titleTemplate': ['Period ', 'positionOneBased', ': ', 'label'],
                                        'dirty': True,
                                        'fields': [ # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/fixedValueInflow/fields
                                            { # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/fixedValueInflow/fields/value
                                                'fieldType': 'TEXT',
                                                'fieldArgs': {
                                                    'displayAsTextArea': False,
                                                    'notEmpty': True,
                                                    'maxLength': 250,
                                                    'numberConfig': {
                                                        'decimals': -1,
                                                        'min': {
                                                            'value': 0,
                                                            'inclusive': True
                                                        },
                                                        'max': None
                                                    }
                                                },
                                                'propName': 'value',
                                                'label': 'Value',
                                                'valueData': '1',
                                                'dirty': True
                                            } # end: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/fixedValueInflow/fields/value
                                        ] # end: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/fixedValueInflow/fields
                                    }, # end: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/fixedValueInflow
                                    { # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/randomChoiceInflow
                                        'id': None,
                                        'tempId': None,
                                        'label': 'Random Choice Inflow',
                                        'type': 'randomChoiceInflow',
                                        'titleTemplate': ['Period ', 'positionOneBased', ': ', 'label'],
                                        'dirty': True,
                                        'fields': [ # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/randomChoiceInflow/fields
                                            { # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/randomChoiceInflow/fields/samples
                                                'fieldType': 'FORMS',
                                                'fieldArgs': { # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/randomChoiceInflow/fields/samples/fieldArgs
                                                    'minForms': 1,
                                                    'maxForms': -1,
                                                    'forms': [ # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/randomChoiceInflow/fields/samples/fieldArgs/forms
                                                        { # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/randomChoiceInflow/fields/samples/fieldArgs/forms/sample
                                                            'id': None,
                                                            'tempId': None,
                                                            'label': 'Sample',
                                                            'type': 'sample',
                                                            'titleTemplate': ['Sample ', 'positionOneBased'],
                                                            'dirty': True,
                                                            'fields': [ # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/randomChoiceInflow/fields/samples/fieldArgs/forms/sample/fields
                                                                { # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/randomChoiceInflow/fields/samples/fieldArgs/forms/sample/fields/value
                                                                    'fieldType': 'TEXT',
                                                                    'fieldArgs': {
                                                                        'displayAsTextArea': False,
                                                                        'notEmpty': True,
                                                                        'maxLength': 250,
                                                                        'numberConfig': {
                                                                            'decimals': -1,
                                                                            'min': {
                                                                                'value': 0,
                                                                                'inclusive': True
                                                                            },
                                                                            'max': None
                                                                        }
                                                                    },
                                                                    'propName': 'value',
                                                                    'label': 'Value',
                                                                    'valueData': '0',
                                                                    'dirty': True
                                                                } # end: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/randomChoiceInflow/fields/samples/fieldArgs/forms/sample/fields/value
                                                            ] # end: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/randomChoiceInflow/fields/samples/fieldArgs/forms/sample/fields
                                                        } # end: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/randomChoiceInflow/fields/samples/fieldArgs/forms/sample
                                                    ] # end: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/randomChoiceInflow/fields/samples/fieldArgs/forms
                                                }, # end: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/randomChoiceInflow/fields/samples/fieldArgs
                                                'propName': 'samples',
                                                'label': 'Samples',
                                                'valueData': [ # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/randomChoiceInflow/fields/samples/valueData
                                                    { # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/randomChoiceInflow/fields/samples/valueData/sample
                                                        'id': None,
                                                        'tempId': None,
                                                        'label': 'Sample',
                                                        'type': 'sample',
                                                        'titleTemplate': ['Sample ', 'positionOneBased'],
                                                        'dirty': True,
                                                        'fields': [ # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/randomChoiceInflow/fields/samples/valueData/sample/fields
                                                            { # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/randomChoiceInflow/fields/samples/valueData/sample/fields/value
                                                                'fieldType': 'TEXT',
                                                                'fieldArgs': {
                                                                    'displayAsTextArea': False,
                                                                    'notEmpty': True,
                                                                    'maxLength': 250,
                                                                    'numberConfig': {
                                                                        'decimals': -1,
                                                                        'min': {
                                                                            'value': 0,
                                                                            'inclusive': True
                                                                        },
                                                                        'max': None
                                                                    }
                                                                },
                                                                'propName': 'value',
                                                                'label': 'Value',
                                                                'valueData': '0',
                                                                'dirty': True
                                                            } # end: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/randomChoiceInflow/fields/samples/valueData/sample/fields/value

                                                        ] # end: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/randomChoiceInflow/fields/samples/valueData/sample/fields
                                                    } # end: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/randomChoiceInflow/fields/samples/valueData/sample
                                                ], # end: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/randomChoiceInflow/fields/samples/valueData
                                                'dirty': True
                                            } # end: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/randomChoiceInflow/fields/samples
                                        ] # end: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/randomChoice/fields
                                    }, # end: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/randomChoiceInflow
                                    { # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow

                                        'id': None,
                                        'tempId': None,
                                        'label': 'Stochastic Function Inflow',
                                        'type': 'stochasticFunctionInflow',
                                        'titleTemplate': ['Period ', 'positionOneBased', ': ', 'label'],
                                        'dirty': True,
                                        'fields': [ # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields
                                            { # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf
                                                'fieldType': 'FORMS',
                                                'fieldArgs': { # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs
                                                    'minForms': 1,
                                                    'maxForms': 1,
                                                    'forms': [ # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms
                                                        { # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/normalDistribution
                                                            'id': None,
                                                            'tempId': None,
                                                            'label': 'Normal Distribution',
                                                            'type': 'normalDistribution',
                                                            'titleTemplate': ['', 'label'],
                                                            'dirty': True,
                                                            'fields': [ # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/normalDistribution/fields
                                                                { # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/normalDistribution/fields/mean
                                                                    'fieldType': 'TEXT',
                                                                    'fieldArgs': {
                                                                        'displayAsTextArea': False,
                                                                        'notEmpty': True,
                                                                        'maxLength': 250,
                                                                        'numberConfig': {
                                                                            'decimals': -1,
                                                                            'min': None,
                                                                            'max': None
                                                                        }
                                                                    },
                                                                    'propName': 'mean',
                                                                    'label': 'Mean',
                                                                    'valueData': '100',
                                                                    'dirty': True
                                                                }, # end: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/normalDistribution/fields/mean
                                                                { # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/normalDistribution/fields/variance
                                                                    'fieldType': 'TEXT',
                                                                    'fieldArgs': {
                                                                        'displayAsTextArea': False,
                                                                        'notEmpty': True,
                                                                        'maxLength': 250,
                                                                        'numberConfig': {
                                                                            'decimals': -1,
                                                                            'min': {
                                                                                'value': 0,
                                                                                'inclusive': True
                                                                            },
                                                                            'max': None
                                                                        }
                                                                    },
                                                                    'propName': 'variance',
                                                                    'label': 'Variance',
                                                                    'valueData': '10',
                                                                    'dirty': True
                                                                } # end: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/normalDistribution/fields/variance
                                                            ] # end: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/normalDistribution/fields
                                                        }, # end: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/normalDistribution
                                                        { # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/triangularDistribution
                                                            'id': None,
                                                            'tempId': None,
                                                            'label': 'Triangular Distribution',
                                                            'type': 'triangularDistribution',
                                                            'titleTemplate': ['', 'label'],
                                                            'dirty': True,
                                                            'fields': [ # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/triangularDistribution/fields
                                                                { # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/triangularDistribution/fields/left
                                                                    'fieldType': 'TEXT',
                                                                    'fieldArgs': {
                                                                        'displayAsTextArea': False,
                                                                        'notEmpty': True,
                                                                        'maxLength': 250,
                                                                        'numberConfig': {
                                                                            'decimals': -1,
                                                                            'min': None,
                                                                            'max': None
                                                                        }
                                                                    },
                                                                    'propName': 'left',
                                                                    'label': 'Left',
                                                                    'valueData': '0',
                                                                    'dirty': True
                                                                }, # end: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/triangularDistribution/fields/left
                                                                { # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/triangularDistribution/fields/mode
                                                                    'fieldType': 'TEXT',
                                                                    'fieldArgs': {
                                                                        'displayAsTextArea': False,
                                                                        'notEmpty': True,
                                                                        'maxLength': 250,
                                                                        'numberConfig': {
                                                                            'decimals': -1,
                                                                            'min': None,
                                                                            'max': None
                                                                        }
                                                                    },
                                                                    'propName': 'mode',
                                                                    'label': 'Mode',
                                                                    'valueData': '0.5',
                                                                    'dirty': True
                                                                }, # end: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/triangularDistribution/fields/mode
                                                                { # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/triangularDistribution/fields/right
                                                                    'fieldType': 'TEXT',
                                                                    'fieldArgs': {
                                                                        'displayAsTextArea': False,
                                                                        'notEmpty': True,
                                                                        'maxLength': 250,
                                                                        'numberConfig': {
                                                                            'decimals': -1,
                                                                            'min': None,
                                                                            'max': None
                                                                        }
                                                                    },
                                                                    'propName': 'right',
                                                                    'label': 'Right',
                                                                    'valueData': '1',
                                                                    'dirty': True
                                                                } # end: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/triangularDistribution/fields/right
                                                            ] # end: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/triangularDistribution/fields
                                                        }, # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/triangularDistribution
                                                        { # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/uniformDistribution
                                                            'id': None,
                                                            'tempId': None,
                                                            'label': 'Uniform Distribution',
                                                            'type': 'uniformDistribution',
                                                            'titleTemplate': ['', 'label'],
                                                            'dirty': True,
                                                            'fields': [ # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/uniformDistribution/fields
                                                                { # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/uniformDistribution/fields/low
                                                                    'fieldType': 'TEXT',
                                                                    'fieldArgs': {
                                                                        'displayAsTextArea': False,
                                                                        'notEmpty': True,
                                                                        'maxLength': 250,
                                                                        'numberConfig': {
                                                                            'decimals': -1,
                                                                            'min': None,
                                                                            'max': None
                                                                        }
                                                                    },
                                                                    'propName': 'low',
                                                                    'label': 'Low',
                                                                    'valueData': '0',
                                                                    'dirty': True
                                                                }, # end: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/uniformDistribution/fields/low
                                                                { # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/uniformDistribution/fields/high
                                                                    'fieldType': 'TEXT',
                                                                    'fieldArgs': {
                                                                        'displayAsTextArea': False,
                                                                        'notEmpty': True,
                                                                        'maxLength': 250,
                                                                        'numberConfig': {
                                                                            'decimals': -1,
                                                                            'min': None,
                                                                            'max': None
                                                                        }
                                                                    },
                                                                    'propName': 'high',
                                                                    'label': 'High',
                                                                    'valueData': '1',
                                                                    'dirty': True
                                                                } # end: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/uniformDistribution/fields/high
                                                            ] # end: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/uniformDistribution/fields
                                                        }, # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/uniformDistribution
                                                        { # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/exponentialDistribution
                                                            'id': None,
                                                            'tempId': None,
                                                            'label': 'Exponential Distribution',
                                                            'type': 'exponentialDistribution',
                                                            'titleTemplate': ['', 'label'],
                                                            'dirty': True,
                                                            'fields': [ # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/exponentialDistribution/fields
                                                                { # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/exponentialDistribution/fields/scale
                                                                    'fieldType': 'TEXT',
                                                                    'fieldArgs': {
                                                                        'displayAsTextArea': False,
                                                                        'notEmpty': True,
                                                                        'maxLength': 250,
                                                                        'numberConfig': {
                                                                            'decimals': -1,
                                                                            'min': {
                                                                                'value': 0,
                                                                                'inclusive': False
                                                                            },
                                                                            'max': None
                                                                        }
                                                                    },
                                                                    'propName': 'scale',
                                                                    'label': 'Scale (1 / lambda)',
                                                                    'valueData': '1',
                                                                    'dirty': True
                                                                }, # end: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/exponentialDistribution/fields/scale
                                                            ] # end: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/exponentialDistribution/fields
                                                        } # end: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/exponentialDistribution
                                                        # TODO: more distributions
                                                    ]
                                                },
                                                'propName': 'pdf',
                                                'label': 'Probability Density Function',
                                                'valueData': [ # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/valueData
                                                    { # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/valueData/normalDistribution
                                                        'id': None,
                                                        'tempId': None,
                                                        'label': 'Normal Distribution',
                                                        'type': 'normalDistribution',
                                                        'titleTemplate': ['', 'label'],
                                                        'dirty': True,
                                                        'fields': [ # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/valueData/normalDistribution/fields
                                                            { # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/valueData/normalDistribution/fields/mean
                                                                'fieldType': 'TEXT',
                                                                'fieldArgs': {
                                                                    'displayAsTextArea': False,
                                                                    'notEmpty': True,
                                                                    'maxLength': 250,
                                                                    'numberConfig': {
                                                                        'decimals': -1,
                                                                        'min': None,
                                                                        'max': None
                                                                    }
                                                                },
                                                                'propName': 'mean',
                                                                'label': 'Mean',
                                                                'valueData': '100',
                                                                'dirty': True
                                                            }, # end: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/valueData/normalDistribution/fields/mean
                                                            { # start: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/valueData/normalDistribution/fields/variance
                                                                'fieldType': 'TEXT',
                                                                'fieldArgs': {
                                                                    'displayAsTextArea': False,
                                                                    'notEmpty': True,
                                                                    'maxLength': 250,
                                                                    'numberConfig': {
                                                                        'decimals': -1,
                                                                        'min': {
                                                                            'value': 0,
                                                                            'inclusive': True
                                                                        },
                                                                        'max': None
                                                                    }
                                                                },
                                                                'propName': 'variance',
                                                                'label': 'Variance',
                                                                'valueData': '10',
                                                                'dirty': True
                                                            } # end: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/valueData/normalDistribution/fields/variance
                                                        ] # end: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/valueData/normalDistribution/fields
                                                    } # end: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/valueData/normalDistribution
                                                ], # end: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/valueData
                                                'dirty': True
                                            } # end: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields/pdf
                                        ] # end: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow/fields
                                    } # end: externalFunctionInflow/fields/basicInflow/fieldArgs/forms/stochasticFunctionInflow
                                ]  # end: externalFunctionInflow/fields/basicInflow/fieldArgs/forms
                            },  # end: externalFunctionInflow/fields/basicInflow/fieldArgs
                            'propName': 'basicInflow',
                            'label': 'Basic Inflow',
                            'valueData': [  # start: externalFunctionInflow/fields/basicInflow/valueData
                                {  # start: externalFunctionInflow/fields/basicInflow/valueData/fixedValueInflow
                                    'id': None,
                                    'tempId': None,
                                    'label': 'Fixed Value Inflow',
                                    'type': 'fixedValueInflow',
                                    'titleTemplate': ['Period ', 'positionOneBased', ': ', 'label'],
                                    'dirty': True,
                                    'fields': [ # start: externalFunctionInflow/fields/basicInflow/valueData/fixedValueInflow/fields
                                        { # start: externalFunctionInflow/fields/basicInflow/valueData/fixedValueInflow/fields/value
                                            'fieldType': 'TEXT',
                                            'fieldArgs': {
                                                'displayAsTextArea': False,
                                                'notEmpty': True,
                                                'maxLength': 250,
                                                'numberConfig': {
                                                    'decimals': -1,
                                                    'min': {
                                                        'value': 0,
                                                        'inclusive': True
                                                    },
                                                    'max': None
                                                }
                                            },
                                            'propName': 'value',
                                            'label': 'Value',
                                            'valueData': '1',
                                            'dirty': True
                                        } # end: externalFunctionInflow/fields/basicInflow/valueData/fixedValueInflow/fields/value
                                    ] # end: externalFunctionInflow/fields/basicInflow/valueData/fixedValueInflow/fields
                                }  # end: externalFunctionInflow/fields/basicInflow/valueData/fixedValueInflow
                            ],  # end: externalFunctionInflow/fields/basicInflow/valueData
                            'dirty': True
                        }  # end: externalFunctionInflow/fields/basicInflow
                    ]  # end: externalFunctionInflow/fields
                },  # end: externalFunctionInflow
                {  # start: flowCompartment
                    'title': None,
                    'titleLabelPath': ['name', 'valueData'],
                    'typeName': 'flowCompartment',
                    'typeLabel': 'Flow Compartment',
                    'id': None,
                    'tempId': None,
                    'position': None,
                    'classes': ['compartment', 'flow-compartment'],
                    'maxOutgoing': -1,
                    'minOutgoing': 1,
                    'maxIncoming': -1,
                    'minIncoming': 1,
                    'outConnectionTypes': ['constantTransfer', 'randomChoiceTransfer', 'stochasticTransfer', 'aggregatedTransfer'],
                    'dirty': True,
                    'fields': [ # start: flowCompartment/fields
                        { # start: flowCompartment/fields/name
                            'fieldType': 'TEXT',
                            'fieldArgs': {
                                'displayAsTextArea': False,
                                'notEmpty': True,
                                'maxLength': 250,
                                'numberConfig': None
                            },
                            'propName': 'name',
                            'label': 'Name',
                            'valueData': 'New Flow Compartment',
                            'dirty': True
                        }, # end: flowCompartment/fields/name
                        {  # start: flowCompartment/fields/description
                            'fieldType': 'TEXT',
                            'fieldArgs': {
                                'displayAsTextArea': True,
                                'notEmpty': False,
                                'maxLength': -1,
                                'numberConfig': None
                            },
                            'propName': 'description',
                            'label': 'Description',
                            'valueData': '',
                            'dirty': True
                        },  # end: flowCompartment/fields/description
                        {  # start: flowCompartment/fields/logInflows
                            'fieldType': 'CHECK',
                            'fieldArgs': {},
                            'propName': 'logInflows',
                            'label': 'Log Inflows',
                            'valueData': True,
                            'dirty': True
                        },  # end: flowCompartment/fields/logInflows
                        {  # start: flowCompartment/fields/logOutflows
                            'fieldType': 'CHECK',
                            'fieldArgs': {},
                            'propName': 'logOutflows',
                            'label': 'Log Outflows',
                            'valueData': True,
                            'dirty': True
                        },  # end: flowCompartment/fields/logOutflows
                        {  # start: flowCompartment/fields/adjustOutgoingTcs
                            'fieldType': 'CHECK',
                            'fieldArgs': {},
                            'propName': 'adjustOutgoingTcs',
                            'label': 'Adjust Outgoing Transfer Coefficients',
                            'valueData': True,
                            'dirty': True
                        },  # end: flowCompartment/fields/adjustOutgoingTcs
                        {  # start: flowCompartment/fields/categories
                            'fieldType': 'FORMS',
                            'fieldArgs': { # start: flowCompartment/fields/categories/fieldArgs
                                'minForms': 0,
                                'maxForms': -1,
                                'forms': [ # start: flowCompartment/fields/categories/fieldArgs/forms
                                    { # start: flowCompartment/fields/categories/fieldArgs/forms/category
                                        'id': None,
                                        'tempId': None,
                                        'label': 'Category',
                                        'type': 'category',
                                        'titleTemplate': ['Category ', 'positionOneBased'],
                                        'dirty': True,
                                        'fields': [ # start: flowCompartment/fields/categories/fieldArgs/forms/category/fields
                                            { # start: flowCompartment/fields/categories/fieldArgs/forms/category/fields/name
                                                'fieldType': 'TEXT',
                                                'fieldArgs': {
                                                    'displayAsTextArea': False,
                                                    'notEmpty': True,
                                                    'maxLength': 250,
                                                    'numberConfig': None
                                                },
                                                'propName': 'description',
                                                'label': 'Description',
                                                'valueData': 'Example',
                                                'dirty': True
                                            } # end: flowCompartment/fields/categories/fieldArgs/forms/category/fields/name
                                        ] # end: flowCompartment/fields/categories/fieldArgs/forms/category/fields
                                    } # end: flowCompartment/fields/categories/fieldArgs/forms/category
                                ] # end: flowCompartment/fields/categories/fieldArgs/forms
                            }, # end: flowCompartment/fields/categories/fieldArgs
                            'propName': 'categories',
                            'label': 'Categories',
                            'valueData': [],
                            'dirty': True
                        }  # end: flowCompartment/fields/categories
                    ] # end: flowCompartment/fields
                }, # end: flowCompartment
                {  # start: stock
                    'title': None,
                    'titleLabelPath': ['name', 'valueData'],
                    'typeName': 'stock',
                    'typeLabel': 'Stock',
                    'id': None,
                    'tempId': None,
                    'position': None,
                    'classes': ['compartment', 'stock'],
                    'maxOutgoing': -1,
                    'minOutgoing': 1,
                    'maxIncoming': -1,
                    'minIncoming': 1,
                    'outConnectionTypes': ['constantTransfer', 'randomChoiceTransfer', 'stochasticTransfer', 'aggregatedTransfer'],
                    'dirty': True,
                    'fields': [ # start: stock/fields
                        { # start: stock/fields/name
                            'fieldType': 'TEXT',
                            'fieldArgs': {
                                'displayAsTextArea': False,
                                'notEmpty': True,
                                'maxLength': 250,
                                'numberConfig': None
                            },
                            'propName': 'name',
                            'label': 'Name',
                            'valueData': 'New Flow Compartment',
                            'dirty': True
                        }, # end: stock/fields/name
                        {  # start: stock/fields/description
                            'fieldType': 'TEXT',
                            'fieldArgs': {
                                'displayAsTextArea': True,
                                'notEmpty': False,
                                'maxLength': -1,
                                'numberConfig': None
                            },
                            'propName': 'description',
                            'label': 'Description',
                            'valueData': '',
                            'dirty': True
                        },  # end: stock/fields/description
                        {  # start: stock/fields/logInflows
                            'fieldType': 'CHECK',
                            'fieldArgs': {},
                            'propName': 'logInflows',
                            'label': 'Log Inflows',
                            'valueData': True,
                            'dirty': True
                        },  # end: stock/fields/logInflows
                        {  # start: stock/fields/logOutflows
                            'fieldType': 'CHECK',
                            'fieldArgs': {},
                            'propName': 'logOutflows',
                            'label': 'Log Outflows',
                            'valueData': True,
                            'dirty': True
                        },  # end: stock/fields/logOutflows
                        {  # start: stock/fields/adjustOutgoingTcs
                            'fieldType': 'CHECK',
                            'fieldArgs': {},
                            'propName': 'adjustOutgoingTcs',
                            'label': 'Adjust Outgoing Transfer Coefficients',
                            'valueData': True,
                            'dirty': True
                        },  # end: stock/fields/adjustOutgoingTcs
                        {  # start: stock/fields/categories
                            'fieldType': 'FORMS',
                            'fieldArgs': { # start: stock/fields/categories/fieldArgs
                                'minForms': 0,
                                'maxForms': -1,
                                'forms': [ # start: stock/fields/categories/fieldArgs/forms
                                    { # start: stock/fields/categories/fieldArgs/forms/category
                                        'id': None,
                                        'tempId': None,
                                        'label': 'Category',
                                        'type': 'category',
                                        'titleTemplate': ['Category ', 'positionOneBased'],
                                        'dirty': True,
                                        'fields': [ # start: stock/fields/categories/fieldArgs/forms/category/fields
                                            { # start: stock/fields/categories/fieldArgs/forms/category/fields/name
                                                'fieldType': 'TEXT',
                                                'fieldArgs': {
                                                    'displayAsTextArea': False,
                                                    'notEmpty': True,
                                                    'maxLength': 250,
                                                    'numberConfig': None
                                                },
                                                'propName': 'description',
                                                'label': 'Description',
                                                'valueData': 'Example',
                                                'dirty': True
                                            } # end: stock/fields/categories/fieldArgs/forms/category/fields/name
                                        ] # end: stock/fields/categories/fieldArgs/forms/category/fields
                                    } # end: stock/fields/categories/fieldArgs/forms/category
                                ] # end: stock/fields/categories/fieldArgs/forms
                            }, # end: stock/fields/categories/fieldArgs
                            'propName': 'categories',
                            'label': 'Categories',
                            'valueData': [],
                            'dirty': True
                        }, # end: stock/fields/categories
                        {  # start: stock/fields/localRelease
                            'fieldType': 'FORMS',
                            'fieldArgs': {  # start: stock/fields/localRelease/fieldArgs
                                'minForms': 1,
                                'maxForms': 1,
                                'forms': [ # start: stock/fields/localRelease/fieldArgs/forms
                                    { # start: stock/fields/localRelease/fieldArgs/forms/fixedRateRelease
                                        'id': None,
                                        'tempId': None,
                                        'label': 'Fixed Rate Release',
                                        'type': 'fixedRateRelease',
                                        'titleTemplate': ['', 'label'],
                                        'dirty': True,
                                        'fields': [  # start: stock/fields/localRelease/fieldArgs/forms/fixedRateRelease/fields
                                            { # start: stock/fields/localRelease/fieldArgs/forms/fixedRateRelease/fields/releaseRate
                                                'fieldType': 'TEXT',
                                                'fieldArgs': {
                                                    'displayAsTextArea': False,
                                                    'notEmpty': True,
                                                    'maxLength': 250,
                                                    'numberConfig': {
                                                        'decimals': -1,
                                                        # TODO: release rate between 0 and 1?
                                                        'min': {
                                                            'value': 0,
                                                            'inclusive': True
                                                        },
                                                        'max': {
                                                            'value': 1,
                                                            'inclusive': True
                                                        }
                                                    }
                                                },
                                                'propName': 'releaseRate',
                                                'label': 'Release Rate',
                                                'valueData': '0.5',
                                                'dirty': True
                                            } # end: stock/fields/localRelease/fieldArgs/forms/fixedRateRelease/fields/releaseRate
                                        ] # end: stock/fields/localRelease/fieldArgs/forms/fixedRateRelease/fields
                                    }, # end: stock/fields/localRelease/fieldArgs/forms/fixedRateRelease
                                    { # start: stock/fields/localRelease/fieldArgs/forms/listRelease
                                        'id': None,
                                        'tempId': None,
                                        'label': 'List Release',
                                        'type': 'listRelease',
                                        'titleTemplate': ['', 'label'],
                                        'dirty': True,
                                        'fields': [  # start: stock/fields/localRelease/fieldArgs/forms/listRelease/fields
                                            { # start: stock/fields/localRelease/fieldArgs/forms/listRelease/fields/items
                                                'fieldType': 'FORMS',
                                                'fieldArgs': { # start: stock/fields/localRelease/fieldArgs/forms/listRelease/fields/items/fieldArgs
                                                    'minForms': 1,
                                                    'maxForms': -1,
                                                    'forms': [ # start: stock/fields/localRelease/fieldArgs/forms/listRelease/fields/items/fieldArgs/forms
                                                        { # start: stock/fields/localRelease/fieldArgs/forms/listRelease/fields/items/fieldArgs/forms/item
                                                            'id': None,
                                                            'tempId': None,
                                                            'label': 'Item',
                                                            'type': 'item',
                                                            'titleTemplate': ['Item Period ', 'positionOneBased'],
                                                            'dirty': True,
                                                            'fields': [ # start: stock/fields/localRelease/fieldArgs/forms/listRelease/fields/items/fieldArgs/forms/item/fields
                                                                { # start: stock/fields/localRelease/fieldArgs/forms/listRelease/fields/items/fieldArgs/forms/item/fields/value
                                                                    'fieldType': 'TEXT',
                                                                    'fieldArgs': {
                                                                        'displayAsTextArea': False,
                                                                        'notEmpty': True,
                                                                        'maxLength': 250,
                                                                        'numberConfig': {
                                                                            'decimals': -1,
                                                                            # TODO: release rate between 0 and 1?
                                                                            'min': {
                                                                                'value': 0,
                                                                                'inclusive': True
                                                                            },
                                                                            'max': {
                                                                                'value': 1,
                                                                                'inclusive': True
                                                                            }
                                                                        }
                                                                    },
                                                                    'propName': 'releaseRate',
                                                                    'label': 'Release Rate',
                                                                    'valueData': '0.5',
                                                                    'dirty': True
                                                                } # end: stock/fields/localRelease/fieldArgs/forms/listRelease/fields/items/fieldArgs/forms/item/fields/value
                                                            ] # end: stock/fields/localRelease/fieldArgs/forms/listRelease/fields/items/fieldArgs/forms/item/fields
                                                        } # end: stock/fields/localRelease/fieldArgs/forms/listRelease/fields/items/fieldArgs/forms/item
                                                    ] # end: stock/fields/localRelease/fieldArgs/forms/listRelease/fields/items/fieldArgs/forms
                                                }, # end: stock/fields/localRelease/fieldArgs/forms/listRelease/fields/items/fieldArgs
                                                'propName': 'items',
                                                'label': 'Items',
                                                'valueData': [ # start: stock/fields/localRelease/fieldArgs/forms/listRelease/fields/items/valueData
                                                    { # start: stock/fields/localRelease/fieldArgs/forms/listRelease/fields/items/valueData/item
                                                        'id': None,
                                                        'tempId': None,
                                                        'label': 'Item',
                                                        'type': 'item',
                                                        'titleTemplate': ['Item Period ', 'positionOneBased'],
                                                        'dirty': True,
                                                        'fields': [ # start: stock/fields/localRelease/fieldArgs/forms/listRelease/fields/items/valueData/item/fields
                                                            { # start: stock/fields/localRelease/fieldArgs/forms/listRelease/fields/items/valueData/item/fields/value
                                                                'fieldType': 'TEXT',
                                                                'fieldArgs': {
                                                                    'displayAsTextArea': False,
                                                                    'notEmpty': True,
                                                                    'maxLength': 250,
                                                                    'numberConfig': {
                                                                        'decimals': -1,
                                                                        # TODO: release rate between 0 and 1?
                                                                        'min': {
                                                                            'value': 0,
                                                                            'inclusive': True
                                                                        },
                                                                        'max': {
                                                                            'value': 1,
                                                                            'inclusive': True
                                                                        }
                                                                    }
                                                                },
                                                                'propName': 'releaseRate',
                                                                'label': 'Release Rate',
                                                                'valueData': '0.5',
                                                                'dirty': True
                                                            } # end: stock/fields/localRelease/fieldArgs/forms/listRelease/fields/items/valueData/item/fields/value
                                                        ] # end: stock/fields/localRelease/fieldArgs/forms/listRelease/fields/items/valueData/item/fields
                                                    }
                                                ], # end: stock/fields/localRelease/fieldArgs/forms/listRelease/fields/items/valueData
                                                'dirty': True
                                            } # end: stock/fields/localRelease/fieldArgs/forms/listRelease/fields/items
                                        ] # end: stock/fields/localRelease/fieldArgs/forms/listRelease/fields
                                    }, # end: stock/fields/localRelease/fieldArgs/forms/listRelease
                                    { # start: stock/fields/localRelease/fieldArgs/forms/functionRelease
                                        'id': None,
                                        'tempId': None,
                                        'label': 'Function Release',
                                        'type': 'functionRelease',
                                        'titleTemplate': ['', 'label'],
                                        'dirty': True,
                                        'fields': [  # start: stock/fields/localRelease/fieldArgs/forms/functionRelease/fields
                                            # TODO: real release function field(s)
                                            { # start: stock/fields/localRelease/fieldArgs/forms/functionRelease/fields/releaseFunction
                                                'fieldType': 'TEXT',
                                                'fieldArgs': {
                                                    'displayAsTextArea': False,
                                                    'notEmpty': True,
                                                    'maxLength': 250,
                                                    'numberConfig': None
                                                },
                                                'propName': 'releaseFunction',
                                                'label': 'Release Function',
                                                'valueData': '15 * currentPeriod + 7',
                                                'dirty': True
                                            } # end: stock/fields/localRelease/fieldArgs/forms/functionRelease/fields/releaseFunction
                                        ] # end: stock/fields/localRelease/fieldArgs/forms/functionRelease/fields
                                    }, # end: stock/fields/localRelease/fieldArgs/forms/functionRelease
                                ] # end: stock/fields/localRelease/fieldArgs/forms
                            }, # end: stock/fields/localRelease/fieldArgs
                            'propName': 'localRelease',
                            'label': 'Local Release',
                            'valueData': [ # start: stock/fields/localRelease/valueData
                                { # start: stock/fields/localRelease/valueData/fixedRateRelease
                                    'id': None,
                                    'tempId': None,
                                    'label': 'Fixed Rate Release',
                                    'type': 'fixedRateRelease',
                                    'titleTemplate': ['', 'label'],
                                    'dirty': True,
                                    'fields': [  # start: stock/fields/localRelease/valueData/fixedRateRelease/fields
                                        { # start: stock/fields/localRelease/valueData/fixedRateRelease/fields/releaseRate
                                            'fieldType': 'TEXT',
                                            'fieldArgs': {
                                                'displayAsTextArea': False,
                                                'notEmpty': True,
                                                'maxLength': 250,
                                                'numberConfig': {
                                                    'decimals': -1,
                                                    # TODO: release rate between 0 and 1?
                                                    'min': {
                                                        'value': 0,
                                                        'inclusive': True
                                                    },
                                                    'max': {
                                                        'value': 1,
                                                        'inclusive': True
                                                    }
                                                }
                                            },
                                            'propName': 'releaseRate',
                                            'label': 'Release Rate',
                                            'valueData': '0.5',
                                            'dirty': True
                                        } # end: stock/fields/localRelease/valueData/fixedRateRelease/fields/releaseRate
                                    ] # end: stock/fields/localRelease/valueData/fixedRateRelease/fields
                                } # end: stock/fields/localRelease/valueData/fixedRateRelease
                            ], # end: stock/fields/localRelease/valueData
                            'dirty': True
                        } # end: stock/fields/localRelease
                    ] # end: stock/fields
                }, # end: stock
                {  # start: sink
                    'title': None,
                    'titleLabelPath': ['name', 'valueData'],
                    'typeName': 'sink',
                    'typeLabel': 'Sink',
                    'id': None,
                    'tempId': None,
                    'position': None,
                    'classes': ['compartment', 'sink'],
                    'maxOutgoing': 0,
                    'minOutgoing': 0,
                    'maxIncoming': -1,
                    'minIncoming': 1,
                    'outConnectionTypes': [],
                    'dirty': True,
                    'fields': [ # start: sink/fields
                        { # start: sink/fields/name
                            'fieldType': 'TEXT',
                            'fieldArgs': {
                                'displayAsTextArea': False,
                                'notEmpty': True,
                                'maxLength': 250,
                                'numberConfig': None
                            },
                            'propName': 'name',
                            'label': 'Name',
                            'valueData': 'New Flow Compartment',
                            'dirty': True
                        }, # end: sink/fields/name
                        {  # start: sink/fields/description
                            'fieldType': 'TEXT',
                            'fieldArgs': {
                                'displayAsTextArea': True,
                                'notEmpty': False,
                                'maxLength': -1,
                                'numberConfig': None
                            },
                            'propName': 'description',
                            'label': 'Description',
                            'valueData': '',
                            'dirty': True
                        },  # end: sink/fields/description
                        {  # start: sink/fields/logInflows
                            'fieldType': 'CHECK',
                            'fieldArgs': {},
                            'propName': 'logInflows',
                            'label': 'Log Inflows',
                            'valueData': True,
                            'dirty': True
                        },  # end: sink/fields/logInflows
                        {  # start: sink/fields/categories
                            'fieldType': 'FORMS',
                            'fieldArgs': { # start: sink/fields/categories/fieldArgs
                                'minForms': 0,
                                'maxForms': -1,
                                'forms': [ # start: sink/fields/categories/fieldArgs/forms
                                    { # start: sink/fields/categories/fieldArgs/forms/category
                                        'id': None,
                                        'tempId': None,
                                        'label': 'Category',
                                        'type': 'category',
                                        'titleTemplate': ['Category ', 'positionOneBased'],
                                        'dirty': True,
                                        'fields': [ # start: sink/fields/categories/fieldArgs/forms/category/fields
                                            { # start: sink/fields/categories/fieldArgs/forms/category/fields/name
                                                'fieldType': 'TEXT',
                                                'fieldArgs': {
                                                    'displayAsTextArea': False,
                                                    'notEmpty': True,
                                                    'maxLength': 250,
                                                    'numberConfig': None
                                                },
                                                'propName': 'description',
                                                'label': 'Description',
                                                'valueData': 'Example',
                                                'dirty': True
                                            } # end: sink/fields/categories/fieldArgs/forms/category/fields/name
                                        ] # end: sink/fields/categories/fieldArgs/forms/category/fields
                                    } # end: sink/fields/categories/fieldArgs/forms/category
                                ] # end: sink/fields/categories/fieldArgs/forms
                            }, # end: sink/fields/categories/fieldArgs
                            'propName': 'categories',
                            'label': 'Categories',
                            'valueData': [],
                            'dirty': True
                        }  # end: sink/fields/categories
                    ] # end: sink/fields
                }, # end: sink
            ], # end of nodeTypes

            'connectionTypes': [
                { # start: inflowTarget
                    'id': None,
                    'tempId': None,
                    'typeName': 'inflowTarget',
                    'typeLabel': 'Inflow Target Connection',
                    'sourceNode': None,
                    'targetNode': None,
                    'title': 'Into',
                    'titleLabelPath': None,
                    'dirty': True,
                    'fields': []
                }, # end: inflowTarget
                { # start: constantTransfer
                    'id': None,
                    'tempId': None,
                    'typeName': 'constantTransfer',
                    'typeLabel': 'Constant Transfer',
                    'title': None,
                    'titleLabelPath': ['name', 'valueData'],
                    'sourceNode': None,
                    'targetNode': None,
                    'dirty': True,
                    'fields': [ # start: constantTransfer/fields
                        { # start: constantTransfer/fields/name
                            'fieldType': 'TEXT',
                            'fieldArgs': {
                                'displayAsTextArea': False,
                                'notEmpty': True,
                                'maxLength': 250,
                                'numberConfig': None
                            },
                            'propName': 'name',
                            'label': 'Name',
                            'valueData': 'Constant Transfer',
                            'dirty': True
                        }, # end: constantTransfer/fields/name
                        {  # start: constantTransfer/fields/priority
                            'fieldType': 'TEXT',
                            'fieldArgs': {
                                'displayAsTextArea': False,
                                'notEmpty': True,
                                'maxLength': 250,
                                'numberConfig': {
                                    'decimals': -1,
                                    'min': {
                                        'value': 0,
                                        'inclusive': True
                                    },
                                    'max': None
                                }
                            },
                            'propName': 'priority',
                            'label': 'Priority',
                            'valueData': '0',
                            'dirty': True
                        },  # end: constantTransfer/fields/priority
                        {  # start: constantTransfer/fields/value
                            'fieldType': 'TEXT',
                            'fieldArgs': {
                                'displayAsTextArea': False,
                                'notEmpty': True,
                                'maxLength': 250,
                                'numberConfig': {
                                    'decimals': -1,
                                    # TODO: transfer coefficients between 0 and 1?
                                    'min': {
                                        'value': 0,
                                        'inclusive': True
                                    },
                                    'max': {
                                        'value': 1,
                                        'inclusive': True
                                    }
                                }
                            },
                            'propName': 'value',
                            'label': 'Value',
                            'valueData': '0.5',
                            'dirty': True
                        }  # end: constantTransfer/fields/value
                    ] # end: constantTransfer/fields
                }, # end: constantTransfer
                {  # start: randomChoiceTransfer
                    'id': None,
                    'tempId': None,
                    'typeName': 'randomChoiceTransfer',
                    'typeLabel': 'Random Choice Transfer',
                    'title': None,
                    'titleLabelPath': ['name', 'valueData'],
                    'sourceNode': None,
                    'targetNode': None,
                    'dirty': True,
                    'fields': [  # start: randomChoiceTransfer/fields
                        {  # start: randomChoiceTransfer/fields/name
                            'fieldType': 'TEXT',
                            'fieldArgs': {
                                'displayAsTextArea': False,
                                'notEmpty': True,
                                'maxLength': 250,
                                'numberConfig': None
                            },
                            'propName': 'name',
                            'label': 'Name',
                            'valueData': 'Random Choice Transfer',
                            'dirty': True
                        },  # end: randomChoiceTransfer/fields/name
                        {  # start: randomChoiceTransfer/fields/priority
                            'fieldType': 'TEXT',
                            'fieldArgs': {
                                'displayAsTextArea': False,
                                'notEmpty': True,
                                'maxLength': 250,
                                'numberConfig': {
                                    'decimals': -1,
                                    'min': {
                                        'value': 0,
                                        'inclusive': True
                                    },
                                    'max': None
                                }
                            },
                            'propName': 'priority',
                            'label': 'Priority',
                            'valueData': '0',
                            'dirty': True
                        },  # end: randomChoiceTransfer/fields/priority
                        {  # start: randomChoiceTransfer/fields/sample
                            'fieldType': 'FORMS',
                            'fieldArgs': { # start: randomChoiceTransfer/fields/samples/fieldArgs
                                'minForms': 1,
                                'maxForms': -1,
                                'forms': [ # start: randomChoiceTransfer/fields/samples/fieldArgs/forms
                                    { # start: randomChoiceTransfer/fields/samples/fieldArgs/forms/sample
                                        'id': None,
                                        'tempId': None,
                                        'label': 'Sample',
                                        'type': 'sample',
                                        'titleTemplate': ['Sample ', 'positionOneBased'],
                                        'dirty': True,
                                        'fields': [ # start: randomChoiceTransfer/fields/samples/fieldArgs/forms/sample/fields
                                            { # start: randomChoiceTransfer/fields/samples/fieldArgs/forms/sample/fields/value
                                                'fieldType': 'TEXT',
                                                'fieldArgs': {
                                                    'displayAsTextArea': False,
                                                    'notEmpty': True,
                                                    'maxLength': 250,
                                                    'numberConfig': {
                                                        'decimals': -1,
                                                        # TODO: transfer coefficients between 0 and 1?
                                                        'min': {
                                                            'value': 0,
                                                            'inclusive': True
                                                        },
                                                        'max': {
                                                            'value': 1,
                                                            'inclusive': True
                                                        }
                                                    }
                                                },
                                                'propName': 'value',
                                                'label': 'Value',
                                                'valueData': '0.5',
                                                'dirty': True
                                            } # end: randomChoiceTransfer/fields/samples/fieldArgs/forms/sample/fields/value
                                        ] # end: randomChoiceTransfer/fields/samples/fieldArgs/forms/sample/fields
                                    }
                                ] # end: randomChoiceTransfer/fields/samples/fieldArgs/forms
                            },
                            'propName': 'samples',
                            'label': 'Samples',
                            'valueData': [ # start: randomChoiceTransfer/fields/samples/valueData
                                { # start: randomChoiceTransfer/fields/samples/valueData/sample
                                    'id': None,
                                    'tempId': None,
                                    'label': 'Sample',
                                    'type': 'sample',
                                    'titleTemplate': ['Sample ', 'positionOneBased'],
                                    'dirty': True,
                                    'fields': [ # start: randomChoiceTransfer/fields/samples/valueData/sample/fields
                                        { # start: randomChoiceTransfer/fields/samples/valueData/sample/fields/value
                                            'fieldType': 'TEXT',
                                            'fieldArgs': {
                                                'displayAsTextArea': False,
                                                'notEmpty': True,
                                                'maxLength': 250,
                                                'numberConfig': {
                                                    'decimals': -1,
                                                    # TODO: transfer coefficients between 0 and 1?
                                                    'min': {
                                                        'value': 0,
                                                        'inclusive': True
                                                    },
                                                    'max': {
                                                        'value': 1,
                                                        'inclusive': True
                                                    }
                                                }
                                            },
                                            'propName': 'value',
                                            'label': 'Value',
                                            'valueData': '0.5',
                                            'dirty': True
                                        } # end: randomChoiceTransfer/fields/samples/valueData/sample/fields/value
                                    ] # end: randomChoiceTransfer/fields/samples/valueData/sample/fields
                                } # end: randomChoiceTransfer/fields/samples/valueData/sample
                            ], # end: randomChoiceTransfer/fields/samples/value/valueData
                            'dirty': True
                        }  # end: randomChoiceTransfer/fields/sample
                    ]  # end: randomChoiceTransfer/fields
                },  # end: randomChoiceTransfer
                {  # start: stochasticTransfer
                    'id': None,
                    'tempId': None,
                    'typeName': 'stochasticTransfer',
                    'typeLabel': 'Stochastic Transfer',
                    'title': None,
                    'titleLabelPath': ['name', 'valueData'],
                    'sourceNode': None,
                    'targetNode': None,
                    'dirty': True,
                    'fields': [  # start: stochasticTransfer/fields
                        {  # start: stochasticTransfer/fields/name
                            'fieldType': 'TEXT',
                            'fieldArgs': {
                                'displayAsTextArea': False,
                                'notEmpty': True,
                                'maxLength': 250,
                                'numberConfig': None
                            },
                            'propName': 'name',
                            'label': 'Name',
                            'valueData': 'Stochastic Transfer',
                            'dirty': True
                        },  # end: stochasticTransfer/fields/name
                        {  # start: stochasticTransfer/fields/priority
                            'fieldType': 'TEXT',
                            'fieldArgs': {
                                'displayAsTextArea': False,
                                'notEmpty': True,
                                'maxLength': 250,
                                'numberConfig': {
                                    'decimals': -1,
                                    'min': {
                                        'value': 0,
                                        'inclusive': True
                                    },
                                    'max': None
                                }
                            },
                            'propName': 'priority',
                            'label': 'Priority',
                            'valueData': '0',
                            'dirty': True
                        },  # end: stochasticTransfer/fields/priority
                        { # start: stochasticTransfer/fields/function
                            'fieldType': 'FORMS',
                            'fieldArgs': { # start: stochasticTransfer/fields/function/fieldArgs
                                'minForms': 1,
                                'maxForms': 1,
                                'forms': [ # start: stochasticTransfer/fields/function/fieldArgs/forms
                                    {
                                    # start: stochasticTransfer/fields/function/fieldArgs/forms/normalDistribution
                                        'id': None,
                                        'tempId': None,
                                        'label': 'Normal Distribution',
                                        'type': 'normalDistribution',
                                        'titleTemplate': ['', 'label'],
                                        'dirty': True,
                                        'fields': [
                                            # start: stochasticTransfer/fields/function/fieldArgs/forms/normalDistribution/fields
                                            {
                                            # start: stochasticTransfer/fields/function/fieldArgs/forms/normalDistribution/fields/mean
                                                'fieldType': 'TEXT',
                                                'fieldArgs': {
                                                    'displayAsTextArea': False,
                                                    'notEmpty': True,
                                                    'maxLength': 250,
                                                    'numberConfig': {
                                                        'decimals': -1,
                                                        'min': None,
                                                        'max': None
                                                    }
                                                },
                                                'propName': 'mean',
                                                'label': 'Mean',
                                                'valueData': '0.5',
                                                'dirty': True
                                            },
                                            # end: stochasticTransfer/fields/function/fieldArgs/forms/normalDistribution/fields/mean
                                            {
                                            # start: stochasticTransfer/fields/function/fieldArgs/forms/normalDistribution/fields/variance
                                                'fieldType': 'TEXT',
                                                'fieldArgs': {
                                                    'displayAsTextArea': False,
                                                    'notEmpty': True,
                                                    'maxLength': 250,
                                                    'numberConfig': {
                                                        'decimals': -1,
                                                        'min': {
                                                            'value': 0,
                                                            'inclusive': True
                                                        },
                                                        'max': None
                                                    }
                                                },
                                                'propName': 'variance',
                                                'label': 'Variance',
                                                'valueData': '0.1',
                                                'dirty': True
                                            }
                                            # end: stochasticTransfer/fields/function/fieldArgs/forms/normalDistribution/fields/variance
                                        ]
                                    # end: stochasticTransfer/fields/function/fieldArgs/forms/normalDistribution/fields
                                    },
                                    # end: stochasticTransfer/fields/function/fieldArgs/forms/normalDistribution
                                    {
                                    # start: stochasticTransfer/fields/function/fieldArgs/forms/triangularDistribution
                                        'id': None,
                                        'tempId': None,
                                        'label': 'Triangular Distribution',
                                        'type': 'triangularDistribution',
                                        'titleTemplate': ['', 'label'],
                                        'dirty': True,
                                        'fields': [
                                            # start: stochasticTransfer/fields/function/fieldArgs/forms/triangularDistribution/fields
                                            {
                                            # start: stochasticTransfer/fields/function/fieldArgs/forms/triangularDistribution/fields/left
                                                'fieldType': 'TEXT',
                                                'fieldArgs': {
                                                    'displayAsTextArea': False,
                                                    'notEmpty': True,
                                                    'maxLength': 250,
                                                    'numberConfig': {
                                                        'decimals': -1,
                                                        'min': None,
                                                        'max': None
                                                    }
                                                },
                                                'propName': 'left',
                                                'label': 'Left',
                                                'valueData': '0',
                                                'dirty': True
                                            },
                                            # end: stochasticTransfer/fields/function/fieldArgs/forms/triangularDistribution/fields/left
                                            {
                                            # start: stochasticTransfer/fields/function/fieldArgs/forms/triangularDistribution/fields/mode
                                                'fieldType': 'TEXT',
                                                'fieldArgs': {
                                                    'displayAsTextArea': False,
                                                    'notEmpty': True,
                                                    'maxLength': 250,
                                                    'numberConfig': {
                                                        'decimals': -1,
                                                        'min': None,
                                                        'max': None
                                                    }
                                                },
                                                'propName': 'mode',
                                                'label': 'Mode',
                                                'valueData': '0.5',
                                                'dirty': True
                                            },
                                            # end: stochasticTransfer/fields/function/fieldArgs/forms/triangularDistribution/fields/mode
                                            {
                                            # start: stochasticTransfer/fields/function/fieldArgs/forms/triangularDistribution/fields/right
                                                'fieldType': 'TEXT',
                                                'fieldArgs': {
                                                    'displayAsTextArea': False,
                                                    'notEmpty': True,
                                                    'maxLength': 250,
                                                    'numberConfig': {
                                                        'decimals': -1,
                                                        'min': None,
                                                        'max': None
                                                    }
                                                },
                                                'propName': 'right',
                                                'label': 'Right',
                                                'valueData': '1',
                                                'dirty': True
                                            }
                                            # end: stochasticTransfer/fields/function/fieldArgs/forms/triangularDistribution/fields/right
                                        ]
                                    # end: stochasticTransfer/fields/function/fieldArgs/forms/triangularDistribution/fields
                                    },
                                    # start: stochasticTransfer/fields/function/fieldArgs/forms/triangularDistribution
                                    {
                                    # start: stochasticTransfer/fields/function/fieldArgs/forms/uniformDistribution
                                        'id': None,
                                        'tempId': None,
                                        'label': 'Uniform Distribution',
                                        'type': 'uniformDistribution',
                                        'titleTemplate': ['', 'label'],
                                        'dirty': True,
                                        'fields': [
                                            # start: stochasticTransfer/fields/function/fieldArgs/forms/uniformDistribution/fields
                                            {
                                            # start: stochasticTransfer/fields/function/fieldArgs/forms/uniformDistribution/fields/low
                                                'fieldType': 'TEXT',
                                                'fieldArgs': {
                                                    'displayAsTextArea': False,
                                                    'notEmpty': True,
                                                    'maxLength': 250,
                                                    'numberConfig': {
                                                        'decimals': -1,
                                                        'min': None,
                                                        'max': None
                                                    }
                                                },
                                                'propName': 'low',
                                                'label': 'Low',
                                                'valueData': '0',
                                                'dirty': True
                                            },
                                            # end: stochasticTransfer/fields/function/fieldArgs/forms/uniformDistribution/fields/low
                                            {
                                            # start: stochasticTransfer/fields/function/fieldArgs/forms/uniformDistribution/fields/high
                                                'fieldType': 'TEXT',
                                                'fieldArgs': {
                                                    'displayAsTextArea': False,
                                                    'notEmpty': True,
                                                    'maxLength': 250,
                                                    'numberConfig': {
                                                        'decimals': -1,
                                                        'min': None,
                                                        'max': None
                                                    }
                                                },
                                                'propName': 'high',
                                                'label': 'High',
                                                'valueData': '1',
                                                'dirty': True
                                            }
                                            # start: stochasticTransfer/fields/function/fieldArgs/forms/uniformDistribution/fields/high
                                        ]
                                    # end: stochasticTransfer/fields/function/fieldArgs/forms/uniformDistribution/fields
                                    },
                                    # start: stochasticTransfer/fields/function/fieldArgs/forms/uniformDistribution
                                    {
                                    # start: stochasticTransfer/fields/function/fieldArgs/forms/exponentialDistribution
                                        'id': None,
                                        'tempId': None,
                                        'label': 'Exponential Distribution',
                                        'type': 'exponentialDistribution',
                                        'titleTemplate': ['', 'label'],
                                        'dirty': True,
                                        'fields': [
                                            # start: stochasticTransfer/fields/function/fieldArgs/forms/exponentialDistribution/fields
                                            {
                                            # start: stochasticTransfer/fields/function/fieldArgs/forms/exponentialDistribution/fields/scale
                                                'fieldType': 'TEXT',
                                                'fieldArgs': {
                                                    'displayAsTextArea': False,
                                                    'notEmpty': True,
                                                    'maxLength': 250,
                                                    'numberConfig': {
                                                        'decimals': -1,
                                                        'min': {
                                                            'value': 0,
                                                            'inclusive': False
                                                        },
                                                        'max': None
                                                    }
                                                },
                                                'propName': 'scale',
                                                'label': 'Scale (1 / lambda)',
                                                'valueData': '1',
                                                'dirty': True
                                            },
                                            # end: stochasticTransfer/fields/function/fieldArgs/forms/exponentialDistribution/fields/scale
                                        ]
                                    # end: stochasticTransfer/fields/function/fieldArgs/forms/exponentialDistribution/fields
                                    }
                                    # start: stochasticTransfer/fields/function/fieldArgs/forms/exponentialDistribution
                                    # TODO: more distributions
                                ]
                            },
                            'propName': 'function',
                            'label': 'Probability Density Function',
                            'valueData': [ # start: stochasticTransfer/fields/function/valueData
                                {
                                    # start: stochasticTransfer/fields/function/valueData/normalDistribution
                                    'id': None,
                                    'tempId': None,
                                    'label': 'Normal Distribution',
                                    'type': 'normalDistribution',
                                    'titleTemplate': ['', 'label'],
                                    'dirty': True,
                                    'fields': [
                                        # start: stochasticTransfer/fields/function/valueData/normalDistribution/fields
                                        {
                                            # start: stochasticTransfer/fields/function/valueData/normalDistribution/fields/mean
                                            'fieldType': 'TEXT',
                                            'fieldArgs': {
                                                'displayAsTextArea': False,
                                                'notEmpty': True,
                                                'maxLength': 250,
                                                'numberConfig': {
                                                    'decimals': -1,
                                                    'min': None,
                                                    'max': None
                                                }
                                            },
                                            'propName': 'mean',
                                            'label': 'Mean',
                                            'valueData': '0.5',
                                            'dirty': True
                                        },
                                        # end: stochasticTransfer/fields/function/valueData/normalDistribution/fields/mean
                                        {
                                            # start: stochasticTransfer/fields/function/valueData/normalDistribution/fields/variance
                                            'fieldType': 'TEXT',
                                            'fieldArgs': {
                                                'displayAsTextArea': False,
                                                'notEmpty': True,
                                                'maxLength': 250,
                                                'numberConfig': {
                                                    'decimals': -1,
                                                    'min': {
                                                        'value': 0,
                                                        'inclusive': True
                                                    },
                                                    'max': None
                                                }
                                            },
                                            'propName': 'variance',
                                            'label': 'Variance',
                                            'valueData': '0.1',
                                            'dirty': True
                                        }
                                        # end: stochasticTransfer/fields/function/valueData/normalDistribution/fields/variance
                                    ]
                                    # end: stochasticTransfer/fields/function/valueData/normalDistribution/fields
                                } # end: stochasticTransfer/fields/function/valueData/normalDistribution
                            ], # end: stochasticTransfer/fields/function/valueData
                            'dirty': True
                        } # end: stochasticTransfer/fields/function
                    ]  # end: stochasticTransfer/fields
                },  # end: stochasticTransfer
                {  # start: aggregatedTransfer
                    'id': None,
                    'tempId': None,
                    'typeName': 'aggregatedTransfer',
                    'typeLabel': 'Aggregated Transfer',
                    'title': None,
                    'titleLabelPath': ['name', 'valueData'],
                    'sourceNode': None,
                    'targetNode': None,
                    'dirty': True,
                    'fields': [  # start: aggregatedTransfer/fields
                        {  # start: aggregatedTransfer/fields/name
                            'fieldType': 'TEXT',
                            'fieldArgs': {
                                'displayAsTextArea': False,
                                'notEmpty': True,
                                'maxLength': 250,
                                'numberConfig': None
                            },
                            'propName': 'name',
                            'label': 'Name',
                            'valueData': 'Aggregated Transfer',
                            'dirty': True
                        }, # end: aggregatedTransfer/fields/name
                        {  # start: aggregatedTransfer/fields/priority
                            'fieldType': 'TEXT',
                            'fieldArgs': {
                                'displayAsTextArea': False,
                                'notEmpty': True,
                                'maxLength': 250,
                                'numberConfig': {
                                    'decimals': -1,
                                    'min': {
                                        'value': 0,
                                        'inclusive': True
                                    },
                                    'max': None
                                }
                            },
                            'propName': 'priority',
                            'label': 'Priority',
                            'valueData': '0',
                            'dirty': True
                        },  # end: aggregatedTransfer/fields/priority
                        {  # start: aggregatedTransfer/fields/singleTransfers
                            'fieldType': 'FORMS',
                            'fieldArgs': { # start: aggregatedTransfer/fields/singleTransfers/fieldArgs
                                'maxForms': -1,
                                'minForms': 1,
                                'forms': [ # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms
                                    {  # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/randomChoiceTransfer
                                        'id': None,
                                        'tempId': None,
                                        'label': 'Random Choice Transfer',
                                        'type': 'randomChoiceTransfer',
                                        'titleTemplate': ['', 'label'],
                                        'dirty': True,
                                        'fields': [  # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/randomChoiceTransfer/fields
                                            {  # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/randomChoiceTransfer/fields/name
                                                'fieldType': 'TEXT',
                                                'fieldArgs': {
                                                    'displayAsTextArea': False,
                                                    'notEmpty': True,
                                                    'maxLength': 250,
                                                    'numberConfig': None
                                                },
                                                'propName': 'name',
                                                'label': 'Name',
                                                'valueData': 'Random Choice Transfer',
                                                'dirty': True
                                            },  # end: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/randomChoiceTransfer/fields/name
                                            # # TODO: Do these need priority (parts of aggregated transfer)?
                                            # {  # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/randomChoiceTransfer/fields/priority
                                            #     'fieldType': 'TEXT',
                                            #     'fieldArgs': {
                                            #         'displayAsTextArea': False,
                                            #         'notEmpty': True,
                                            #         'maxLength': 250,
                                            #         'numberConfig': {
                                            #             'decimals': -1,
                                            #             'min': {
                                            #                 'value': 0,
                                            #                 'inclusive': True
                                            #             },
                                            #             'max': None
                                            #         }
                                            #     },
                                            #     'propName': 'priority',
                                            #     'label': 'Priority',
                                            #     'valueData': '0',
                                            #     'dirty': True
                                            # },  # end: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/randomChoiceTransfer/fields/priority
                                            { # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/randomChoiceTransfer/fields/weight
                                                'fieldType': 'TEXT',
                                                'fieldArgs': {
                                                    'displayAsTextArea': False,
                                                    'notEmpty': True,
                                                    'maxLength': 250,
                                                    'numberConfig': {
                                                        'decimals': -1,
                                                        'min': {
                                                            'value': 0,
                                                            'inclusive': True
                                                        },
                                                        'max': None
                                                    }
                                                },
                                                'propName': 'weight',
                                                'label': 'Weight in Aggregated Transfer',
                                                'valueData': '0.5',
                                                'dirty': True
                                            }, # end: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/randomChoiceTransfer/fields/weight
                                            {  # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/randomChoiceTransfer/fields/sample
                                                'fieldType': 'FORMS',
                                                'fieldArgs': { # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/randomChoiceTransfer/fields/samples/fieldArgs
                                                    'minForms': 1,
                                                    'maxForms': -1,
                                                    'forms': [ # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/randomChoiceTransfer/fields/samples/fieldArgs/forms
                                                        { # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/randomChoiceTransfer/fields/samples/fieldArgs/forms/sample
                                                            'id': None,
                                                            'tempId': None,
                                                            'label': 'Sample',
                                                            'type': 'sample',
                                                            'titleTemplate': ['Sample ', 'positionOneBased'],
                                                            'dirty': True,
                                                            'fields': [ # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/randomChoiceTransfer/fields/samples/fieldArgs/forms/sample/fields
                                                                { # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/randomChoiceTransfer/fields/samples/fieldArgs/forms/sample/fields/value
                                                                    'fieldType': 'TEXT',
                                                                    'fieldArgs': {
                                                                        'displayAsTextArea': False,
                                                                        'notEmpty': True,
                                                                        'maxLength': 250,
                                                                        'numberConfig': {
                                                                            'decimals': -1,
                                                                            # TODO: transfer coefficients between 0 and 1?
                                                                            'min': {
                                                                                'value': 0,
                                                                                'inclusive': True
                                                                            },
                                                                            'max': {
                                                                                'value': 1,
                                                                                'inclusive': True
                                                                            }
                                                                        }
                                                                    },
                                                                    'propName': 'value',
                                                                    'label': 'Value',
                                                                    'valueData': '0.5',
                                                                    'dirty': True
                                                                } # end: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/randomChoiceTransfer/fields/samples/fieldArgs/forms/sample/fields/value
                                                            ] # end: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/randomChoiceTransfer/fields/samples/fieldArgs/forms/sample/fields
                                                        }
                                                    ] # end: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/randomChoiceTransfer/fields/samples/fieldArgs/forms
                                                },
                                                'propName': 'samples',
                                                'label': 'Samples',
                                                'valueData': [ # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/randomChoiceTransfer/fields/samples/valueData
                                                    { # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/randomChoiceTransfer/fields/samples/valueData/sample
                                                        'id': None,
                                                        'tempId': None,
                                                        'label': 'Sample',
                                                        'type': 'sample',
                                                        'titleTemplate': ['Sample ', 'positionOneBased'],
                                                        'dirty': True,
                                                        'fields': [ # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/randomChoiceTransfer/fields/samples/valueData/sample/fields
                                                            { # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/randomChoiceTransfer/fields/samples/valueData/sample/fields/value
                                                                'fieldType': 'TEXT',
                                                                'fieldArgs': {
                                                                    'displayAsTextArea': False,
                                                                    'notEmpty': True,
                                                                    'maxLength': 250,
                                                                    'numberConfig': {
                                                                        'decimals': -1,
                                                                        # TODO: transfer coefficients between 0 and 1?
                                                                        'min': {
                                                                            'value': 0,
                                                                            'inclusive': True
                                                                        },
                                                                        'max': {
                                                                            'value': 1,
                                                                            'inclusive': True
                                                                        }
                                                                    }
                                                                },
                                                                'propName': 'value',
                                                                'label': 'Value',
                                                                'valueData': '0.5',
                                                                'dirty': True
                                                            } # end: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/randomChoiceTransfer/fields/samples/valueData/sample/fields/value
                                                        ] # end: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/randomChoiceTransfer/fields/samples/valueData/sample/fields
                                                    } # end: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/randomChoiceTransfer/fields/samples/valueData/sample
                                                ], # end: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/randomChoiceTransfer/fields/samples/value/valueData
                                                'dirty': True
                                            }  # end: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/randomChoiceTransfer/fields/sample
                                        ]  # end: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/randomChoiceTransfer/fields
                                    },  # end: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/randomChoiceTransfer
                                    {  # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer
                                        'id': None,
                                        'tempId': None,
                                        'label': 'Stochastic Transfer',
                                        'type': 'stochasticTransfer',
                                        'titleTemplate': ['', 'label'],
                                        'dirty': True,
                                        'fields': [  # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields
                                            {  # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/name
                                                'fieldType': 'TEXT',
                                                'fieldArgs': {
                                                    'displayAsTextArea': False,
                                                    'notEmpty': True,
                                                    'maxLength': 250,
                                                    'numberConfig': None
                                                },
                                                'propName': 'name',
                                                'label': 'Name',
                                                'valueData': 'Stochastic Transfer',
                                                'dirty': True
                                            },  # end: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/name
                                            # # TODO: Do these need priority (parts of aggregated transfer)?
                                            # {  # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/priority
                                            #     'fieldType': 'TEXT',
                                            #     'fieldArgs': {
                                            #         'displayAsTextArea': False,
                                            #         'notEmpty': True,
                                            #         'maxLength': 250,
                                            #         'numberConfig': {
                                            #             'decimals': -1,
                                            #             'min': {
                                            #                 'value': 0,
                                            #                 'inclusive': True
                                            #             },
                                            #             'max': None
                                            #         }
                                            #     },
                                            #     'propName': 'priority',
                                            #     'label': 'Priority',
                                            #     'valueData': '0',
                                            #     'dirty': True
                                            # },  # end: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/priority
                                            {
                                            # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/weight
                                                'fieldType': 'TEXT',
                                                'fieldArgs': {
                                                    'displayAsTextArea': False,
                                                    'notEmpty': True,
                                                    'maxLength': 250,
                                                    'numberConfig': {
                                                        'decimals': -1,
                                                        'min': {
                                                            'value': 0,
                                                            'inclusive': True
                                                        },
                                                        'max': None
                                                    }
                                                },
                                                'propName': 'weight',
                                                'label': 'Weight in Aggregated Transfer',
                                                'valueData': '0.5',
                                                'dirty': True
                                            }, # end: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/weight
                                            { # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function
                                                'fieldType': 'FORMS',
                                                'fieldArgs': { # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/fieldArgs
                                                    'minForms': 1,
                                                    'maxForms': 1,
                                                    'forms': [ # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/fieldArgs/forms
                                                        {
                                                        # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/fieldArgs/forms/normalDistribution
                                                            'id': None,
                                                            'tempId': None,
                                                            'label': 'Normal Distribution',
                                                            'type': 'normalDistribution',
                                                            'titleTemplate': ['', 'label'],
                                                            'dirty': True,
                                                            'fields': [
                                                                # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/fieldArgs/forms/normalDistribution/fields
                                                                {
                                                                # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/fieldArgs/forms/normalDistribution/fields/mean
                                                                    'fieldType': 'TEXT',
                                                                    'fieldArgs': {
                                                                        'displayAsTextArea': False,
                                                                        'notEmpty': True,
                                                                        'maxLength': 250,
                                                                        'numberConfig': {
                                                                            'decimals': -1,
                                                                            'min': None,
                                                                            'max': None
                                                                        }
                                                                    },
                                                                    'propName': 'mean',
                                                                    'label': 'Mean',
                                                                    'valueData': '0.5',
                                                                    'dirty': True
                                                                },
                                                                # end: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/fieldArgs/forms/normalDistribution/fields/mean
                                                                {
                                                                # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/fieldArgs/forms/normalDistribution/fields/variance
                                                                    'fieldType': 'TEXT',
                                                                    'fieldArgs': {
                                                                        'displayAsTextArea': False,
                                                                        'notEmpty': True,
                                                                        'maxLength': 250,
                                                                        'numberConfig': {
                                                                            'decimals': -1,
                                                                            'min': {
                                                                                'value': 0,
                                                                                'inclusive': True
                                                                            },
                                                                            'max': None
                                                                        }
                                                                    },
                                                                    'propName': 'variance',
                                                                    'label': 'Variance',
                                                                    'valueData': '0.1',
                                                                    'dirty': True
                                                                }
                                                                # end: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/fieldArgs/forms/normalDistribution/fields/variance
                                                            ]
                                                        # end: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/fieldArgs/forms/normalDistribution/fields
                                                        },
                                                        # end: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/fieldArgs/forms/normalDistribution
                                                        {
                                                        # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/fieldArgs/forms/triangularDistribution
                                                            'id': None,
                                                            'tempId': None,
                                                            'label': 'Triangular Distribution',
                                                            'type': 'triangularDistribution',
                                                            'titleTemplate': ['', 'label'],
                                                            'dirty': True,
                                                            'fields': [
                                                                # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/fieldArgs/forms/triangularDistribution/fields
                                                                {
                                                                # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/fieldArgs/forms/triangularDistribution/fields/left
                                                                    'fieldType': 'TEXT',
                                                                    'fieldArgs': {
                                                                        'displayAsTextArea': False,
                                                                        'notEmpty': True,
                                                                        'maxLength': 250,
                                                                        'numberConfig': {
                                                                            'decimals': -1,
                                                                            'min': None,
                                                                            'max': None
                                                                        }
                                                                    },
                                                                    'propName': 'left',
                                                                    'label': 'Left',
                                                                    'valueData': '0',
                                                                    'dirty': True
                                                                },
                                                                # end: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/fieldArgs/forms/triangularDistribution/fields/left
                                                                {
                                                                # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/fieldArgs/forms/triangularDistribution/fields/mode
                                                                    'fieldType': 'TEXT',
                                                                    'fieldArgs': {
                                                                        'displayAsTextArea': False,
                                                                        'notEmpty': True,
                                                                        'maxLength': 250,
                                                                        'numberConfig': {
                                                                            'decimals': -1,
                                                                            'min': None,
                                                                            'max': None
                                                                        }
                                                                    },
                                                                    'propName': 'mode',
                                                                    'label': 'Mode',
                                                                    'valueData': '0.5',
                                                                    'dirty': True
                                                                },
                                                                # end: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/fieldArgs/forms/triangularDistribution/fields/mode
                                                                {
                                                                # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/fieldArgs/forms/triangularDistribution/fields/right
                                                                    'fieldType': 'TEXT',
                                                                    'fieldArgs': {
                                                                        'displayAsTextArea': False,
                                                                        'notEmpty': True,
                                                                        'maxLength': 250,
                                                                        'numberConfig': {
                                                                            'decimals': -1,
                                                                            'min': None,
                                                                            'max': None
                                                                        }
                                                                    },
                                                                    'propName': 'right',
                                                                    'label': 'Right',
                                                                    'valueData': '1',
                                                                    'dirty': True
                                                                }
                                                                # end: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/fieldArgs/forms/triangularDistribution/fields/right
                                                            ]
                                                        # end: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/fieldArgs/forms/triangularDistribution/fields
                                                        },
                                                        # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/fieldArgs/forms/triangularDistribution
                                                        {
                                                        # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/fieldArgs/forms/uniformDistribution
                                                            'id': None,
                                                            'tempId': None,
                                                            'label': 'Uniform Distribution',
                                                            'type': 'uniformDistribution',
                                                            'titleTemplate': ['', 'label'],
                                                            'dirty': True,
                                                            'fields': [
                                                                # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/fieldArgs/forms/uniformDistribution/fields
                                                                {
                                                                # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/fieldArgs/forms/uniformDistribution/fields/low
                                                                    'fieldType': 'TEXT',
                                                                    'fieldArgs': {
                                                                        'displayAsTextArea': False,
                                                                        'notEmpty': True,
                                                                        'maxLength': 250,
                                                                        'numberConfig': {
                                                                            'decimals': -1,
                                                                            'min': None,
                                                                            'max': None
                                                                        }
                                                                    },
                                                                    'propName': 'low',
                                                                    'label': 'Low',
                                                                    'valueData': '0',
                                                                    'dirty': True
                                                                },
                                                                # end: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/fieldArgs/forms/uniformDistribution/fields/low
                                                                {
                                                                # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/fieldArgs/forms/uniformDistribution/fields/high
                                                                    'fieldType': 'TEXT',
                                                                    'fieldArgs': {
                                                                        'displayAsTextArea': False,
                                                                        'notEmpty': True,
                                                                        'maxLength': 250,
                                                                        'numberConfig': {
                                                                            'decimals': -1,
                                                                            'min': None,
                                                                            'max': None
                                                                        }
                                                                    },
                                                                    'propName': 'high',
                                                                    'label': 'High',
                                                                    'valueData': '1',
                                                                    'dirty': True
                                                                }
                                                                # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/fieldArgs/forms/uniformDistribution/fields/high
                                                            ]
                                                        # end: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/fieldArgs/forms/uniformDistribution/fields
                                                        },
                                                        # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/fieldArgs/forms/uniformDistribution
                                                        {
                                                        # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/fieldArgs/forms/exponentialDistribution
                                                            'id': None,
                                                            'tempId': None,
                                                            'label': 'Exponential Distribution',
                                                            'type': 'exponentialDistribution',
                                                            'titleTemplate': ['', 'label'],
                                                            'dirty': True,
                                                            'fields': [
                                                                # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/fieldArgs/forms/exponentialDistribution/fields
                                                                {
                                                                # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/fieldArgs/forms/exponentialDistribution/fields/scale
                                                                    'fieldType': 'TEXT',
                                                                    'fieldArgs': {
                                                                        'displayAsTextArea': False,
                                                                        'notEmpty': True,
                                                                        'maxLength': 250,
                                                                        'numberConfig': {
                                                                            'decimals': -1,
                                                                            'min': {
                                                                                'value': 0,
                                                                                'inclusive': False
                                                                            },
                                                                            'max': None
                                                                        }
                                                                    },
                                                                    'propName': 'scale',
                                                                    'label': 'Scale (1 / lambda)',
                                                                    'valueData': '1',
                                                                    'dirty': True
                                                                },
                                                                # end: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/fieldArgs/forms/exponentialDistribution/fields/scale
                                                            ]
                                                        # end: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/fieldArgs/forms/exponentialDistribution/fields
                                                        }
                                                        # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/fieldArgs/forms/exponentialDistribution
                                                        # TODO: more distributions
                                                    ]
                                                },
                                                'propName': 'function',
                                                'label': 'Probability Density Function',
                                                'valueData': [ # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/valueData
                                                    {
                                                        # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/valueData/normalDistribution
                                                        'id': None,
                                                        'tempId': None,
                                                        'label': 'Normal Distribution',
                                                        'type': 'normalDistribution',
                                                        'titleTemplate': ['', 'label'],
                                                        'dirty': True,
                                                        'fields': [
                                                            # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/valueData/normalDistribution/fields
                                                            {
                                                                # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/valueData/normalDistribution/fields/mean
                                                                'fieldType': 'TEXT',
                                                                'fieldArgs': {
                                                                    'displayAsTextArea': False,
                                                                    'notEmpty': True,
                                                                    'maxLength': 250,
                                                                    'numberConfig': {
                                                                        'decimals': -1,
                                                                        'min': None,
                                                                        'max': None
                                                                    }
                                                                },
                                                                'propName': 'mean',
                                                                'label': 'Mean',
                                                                'valueData': '0.5',
                                                                'dirty': True
                                                            },
                                                            # end: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/valueData/normalDistribution/fields/mean
                                                            {
                                                                # start: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/valueData/normalDistribution/fields/variance
                                                                'fieldType': 'TEXT',
                                                                'fieldArgs': {
                                                                    'displayAsTextArea': False,
                                                                    'notEmpty': True,
                                                                    'maxLength': 250,
                                                                    'numberConfig': {
                                                                        'decimals': -1,
                                                                        'min': {
                                                                            'value': 0,
                                                                            'inclusive': True
                                                                        },
                                                                        'max': None
                                                                    }
                                                                },
                                                                'propName': 'variance',
                                                                'label': 'Variance',
                                                                'valueData': '0.1',
                                                                'dirty': True
                                                            }
                                                            # end: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/valueData/normalDistribution/fields/variance
                                                        ]
                                                        # end: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/valueData/normalDistribution/fields
                                                    } # end: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/valueData/normalDistribution
                                                ], # end: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function/valueData
                                                'dirty': True
                                            } # end: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields/function
                                        ]  # end: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer/fields
                                    }  # end: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms/stochasticTransfer
                                ] # end: aggregatedTransfer/fields/singleTransfers/fieldArgs/forms
                            }, # end: aggregatedTransfer/fields/singleTransfers/fieldArgs
                            'propName': 'singleTransfers',
                            'label': 'Single Transfers',
                            'valueData': [ # start: aggregatedTransfer/fields/singleTransfers/valueData
                                {
                                # start: aggregatedTransfer/fields/singleTransfers/valueData/randomChoiceTransfer
                                    'id': None,
                                    'tempId': None,
                                    'label': 'Random Choice Transfer',
                                    'type': 'randomChoiceTransfer',
                                    'titleTemplate': ['', 'label'],
                                    'dirty': True,
                                    'fields': [
                                        # start: aggregatedTransfer/fields/singleTransfers/valueData/randomChoiceTransfer/fields
                                        {
                                        # start: aggregatedTransfer/fields/singleTransfers/valueData/randomChoiceTransfer/fields/name
                                            'fieldType': 'TEXT',
                                            'fieldArgs': {
                                                'displayAsTextArea': False,
                                                'notEmpty': True,
                                                'maxLength': 250,
                                                'numberConfig': None
                                            },
                                            'propName': 'name',
                                            'label': 'Name',
                                            'valueData': 'Random Choice Transfer',
                                            'dirty': True
                                        },
                                        # end: aggregatedTransfer/fields/singleTransfers/valueData/randomChoiceTransfer/fields/name
                                        # # TODO: Do these need priority (parts of aggregated transfer)?
                                        # {
                                        # # start: aggregatedTransfer/fields/singleTransfers/valueData/randomChoiceTransfer/fields/priority
                                        #     'fieldType': 'TEXT',
                                        #     'fieldArgs': {
                                        #         'displayAsTextArea': False,
                                        #         'notEmpty': True,
                                        #         'maxLength': 250,
                                        #         'numberConfig': {
                                        #             'decimals': -1,
                                        #             'min': {
                                        #                 'value': 0,
                                        #                 'inclusive': True
                                        #             },
                                        #             'max': None
                                        #         }
                                        #     },
                                        #     'propName': 'priority',
                                        #     'label': 'Priority',
                                        #     'valueData': '0',
                                        #     'dirty': True
                                        # },
                                        # # end: aggregatedTransfer/fields/singleTransfers/valueData/randomChoiceTransfer/fields/priority
                                        {
                                        # start: aggregatedTransfer/fields/singleTransfers/valueData/randomChoiceTransfer/fields/weight
                                            'fieldType': 'TEXT',
                                            'fieldArgs': {
                                                'displayAsTextArea': False,
                                                'notEmpty': True,
                                                'maxLength': 250,
                                                'numberConfig': {
                                                    'decimals': -1,
                                                    'min': {
                                                        'value': 0,
                                                        'inclusive': True
                                                    },
                                                    'max': None
                                                }
                                            },
                                            'propName': 'weight',
                                            'label': 'Weight in Aggregated Transfer',
                                            'valueData': '0.5',
                                            'dirty': True
                                        },
                                        # end: aggregatedTransfer/fields/singleTransfers/valueData/randomChoiceTransfer/fields/weight
                                        {
                                        # start: aggregatedTransfer/fields/singleTransfers/valueData/randomChoiceTransfer/fields/sample
                                            'fieldType': 'FORMS',
                                            'fieldArgs': {
                                            # start: aggregatedTransfer/fields/singleTransfers/valueData/randomChoiceTransfer/fields/samples/fieldArgs
                                                'minForms': 1,
                                                'maxForms': -1,
                                                'forms': [
                                                    # start: aggregatedTransfer/fields/singleTransfers/valueData/randomChoiceTransfer/fields/samples/fieldArgs/forms
                                                    {
                                                    # start: aggregatedTransfer/fields/singleTransfers/valueData/randomChoiceTransfer/fields/samples/fieldArgs/forms/sample
                                                        'id': None,
                                                        'tempId': None,
                                                        'label': 'Sample',
                                                        'type': 'sample',
                                                        'titleTemplate': ['Sample ', 'positionOneBased'],
                                                        'dirty': True,
                                                        'fields': [
                                                            # start: aggregatedTransfer/fields/singleTransfers/valueData/randomChoiceTransfer/fields/samples/fieldArgs/forms/sample/fields
                                                            {
                                                            # start: aggregatedTransfer/fields/singleTransfers/valueData/randomChoiceTransfer/fields/samples/fieldArgs/forms/sample/fields/value
                                                                'fieldType': 'TEXT',
                                                                'fieldArgs': {
                                                                    'displayAsTextArea': False,
                                                                    'notEmpty': True,
                                                                    'maxLength': 250,
                                                                    'numberConfig': {
                                                                        'decimals': -1,
                                                                        # TODO: transfer coefficients between 0 and 1?
                                                                        'min': {
                                                                            'value': 0,
                                                                            'inclusive': True
                                                                        },
                                                                        'max': {
                                                                            'value': 1,
                                                                            'inclusive': True
                                                                        }
                                                                    }
                                                                },
                                                                'propName': 'value',
                                                                'label': 'Value',
                                                                'valueData': '0.5',
                                                                'dirty': True
                                                            }
                                                            # end: aggregatedTransfer/fields/singleTransfers/valueData/randomChoiceTransfer/fields/samples/fieldArgs/forms/sample/fields/value
                                                        ]
                                                    # end: aggregatedTransfer/fields/singleTransfers/valueData/randomChoiceTransfer/fields/samples/fieldArgs/forms/sample/fields
                                                    }
                                                ]
                                            # end: aggregatedTransfer/fields/singleTransfers/valueData/randomChoiceTransfer/fields/samples/fieldArgs/forms
                                            },
                                            'propName': 'samples',
                                            'label': 'Samples',
                                            'valueData': [
                                                # start: aggregatedTransfer/fields/singleTransfers/valueData/randomChoiceTransfer/fields/samples/valueData
                                                {
                                                # start: aggregatedTransfer/fields/singleTransfers/valueData/randomChoiceTransfer/fields/samples/valueData/sample
                                                    'id': None,
                                                    'tempId': None,
                                                    'label': 'Sample',
                                                    'type': 'sample',
                                                    'titleTemplate': ['Sample ', 'positionOneBased'],
                                                    'dirty': True,
                                                    'fields': [
                                                        # start: aggregatedTransfer/fields/singleTransfers/valueData/randomChoiceTransfer/fields/samples/valueData/sample/fields
                                                        {
                                                        # start: aggregatedTransfer/fields/singleTransfers/valueData/randomChoiceTransfer/fields/samples/valueData/sample/fields/value
                                                            'fieldType': 'TEXT',
                                                            'fieldArgs': {
                                                                'displayAsTextArea': False,
                                                                'notEmpty': True,
                                                                'maxLength': 250,
                                                                'numberConfig': {
                                                                    'decimals': -1,
                                                                    # TODO: transfer coefficients between 0 and 1?
                                                                    'min': {
                                                                        'value': 0,
                                                                        'inclusive': True
                                                                    },
                                                                    'max': {
                                                                        'value': 1,
                                                                        'inclusive': True
                                                                    }
                                                                }
                                                            },
                                                            'propName': 'value',
                                                            'label': 'Value',
                                                            'valueData': '0.5',
                                                            'dirty': True
                                                        }
                                                        # end: aggregatedTransfer/fields/singleTransfers/valueData/randomChoiceTransfer/fields/samples/valueData/sample/fields/value
                                                    ]
                                                # end: aggregatedTransfer/fields/singleTransfers/valueData/randomChoiceTransfer/fields/samples/valueData/sample/fields
                                                }
                                                # end: aggregatedTransfer/fields/singleTransfers/valueData/randomChoiceTransfer/fields/samples/valueData/sample
                                            ],
                                        # end: aggregatedTransfer/fields/singleTransfers/valueData/randomChoiceTransfer/fields/samples/value/valueData
                                            'dirty': True
                                        }
                                        # end: aggregatedTransfer/fields/singleTransfers/valueData/randomChoiceTransfer/fields/sample
                                    ]
                                # end: aggregatedTransfer/fields/singleTransfers/valueData/randomChoiceTransfer/fields
                                },
                                # end: aggregatedTransfer/fields/singleTransfers/valueData/randomChoiceTransfer
                            ], # end: aggregatedTransfer/fields/singleTransfers/valueData
                            'dirty': True
                        }  # end: aggregatedTransfer/fields/singleTransfers
                    ] # end: aggregatedTransfer/fields
                } # end: aggregatedTransfer
            ] # end of connectionTypes
        } # end of data
        return data

    @staticmethod
    def get_external_list_inflow_scaffold(add_defaults_to_forms_fields, dirty):
        return {  # start: externalListInflow
            'title': None,
            'titleLabelPath': ['name', 'valueData'],
            'typeName': 'externalListInflow',
            'typeLabel': 'External List Inflow',
            'id': None,
            'tempId': None,
            'position': None,
            'classes': ['inflow', 'external-list-inflow'],
            'maxOutgoing': 1,
            'minOutgoing': 1,
            'maxIncoming': 0,
            'minIncoming': 0,
            'outConnectionTypes': ['inflowTarget'],
            'dirty': dirty,
            'fields': [  # start: externalListInflow/fields
                {  # start: externalListInflow/fields/name
                    'fieldType': 'TEXT',
                    'fieldArgs': {
                        'displayAsTextArea': False,
                        'notEmpty': True,
                        'maxLength': 250,
                        'numberConfig': None
                    },
                    'propName': 'name',
                    'label': 'Name',
                    'valueData': 'New External List Inflow',
                    'dirty': dirty
                },  # end: externalListInflow/fields/name
                {  # start: externalListInflow/fields/startDelay
                    'fieldType': 'TEXT',
                    'fieldArgs': {
                        'displayAsTextArea': False,
                        'notEmpty': True,
                        'maxLength': 250,
                        'numberConfig': {
                            'decimals': 0,
                            'min': {
                                'value': 0,
                                'inclusive': True
                            },
                            'max': None
                        }
                    },
                    'propName': 'startDelay',
                    'label': 'Start Delay',
                    'valueData': '0',
                    'dirty': dirty
                },  # end: externalListInflow/fields/startDelay
                ModelJson.get_distribution_field_scaffold(0, 1, 'derivationDistribution', 'Derivation Distribution', True, True),
                {  # start: externalListInflow/fields/derivationFactor
                    'fieldType': 'TEXT',
                    'fieldArgs': {
                        'displayAsTextArea': False,
                        'notEmpty': True,
                        'maxLength': 250,
                        'numberConfig': {
                            'decimals': -1,
                            'min': None,
                            'max': None
                            # TODO: limits for derivationFactor
                        }
                    },
                    'propName': 'derivationFactor',
                    'label': 'Derivation Factor',
                    'valueData': '1',
                    'dirty': dirty
                },  # end: externalListInflow/fields/derivationFactor
                {  # start: externalListInflow/fields/singlePeriodInflows
                    'fieldType': 'FORMS',
                    'fieldArgs': {  # start: externalListInflow/fields/singlePeriodInflows/fieldArgs
                        'minForms': 1,
                        'maxForms': -1,
                        'forms': [  # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms
                            {  # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/fixedValueInflow
                                'id': None,
                                'tempId': None,
                                'label': 'Fixed Value Inflow',
                                'type': 'fixedValueInflow',
                                'titleTemplate': ['Period ', 'positionOneBased', ': ', 'label'],
                                'dirty': True,
                                'fields': [
                                    # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/fixedValueInflow/fields
                                    {
                                    # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/fixedValueInflow/fields/value
                                        'fieldType': 'TEXT',
                                        'fieldArgs': {
                                            'displayAsTextArea': False,
                                            'notEmpty': True,
                                            'maxLength': 250,
                                            'numberConfig': {
                                                'decimals': -1,
                                                'min': {
                                                    'value': 0,
                                                    'inclusive': True
                                                },
                                                'max': None
                                            }
                                        },
                                        'propName': 'value',
                                        'label': 'Value',
                                        'valueData': '1',
                                        'dirty': True
                                    }
                                    # end: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/fixedValueInflow/fields/value
                                ]
                            # end: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/fixedValueInflow/fields
                            },  # end: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/fixedValueInflow
                            {  # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/randomChoiceInflow
                                'id': None,
                                'tempId': None,
                                'label': 'Random Choice Inflow',
                                'type': 'randomChoiceInflow',
                                'titleTemplate': ['Period ', 'positionOneBased', ': ', 'label'],
                                'dirty': True,
                                'fields': [
                                    # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/randomChoiceInflow/fields
                                    {
                                    # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/randomChoiceInflow/fields/samples
                                        'fieldType': 'FORMS',
                                        'fieldArgs': {
                                        # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/randomChoiceInflow/fields/samples/fieldArgs
                                            'minForms': 1,
                                            'maxForms': -1,
                                            'forms': [
                                                # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/randomChoiceInflow/fields/samples/fieldArgs/forms
                                                {
                                                # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/randomChoiceInflow/fields/samples/fieldArgs/forms/sample
                                                    'id': None,
                                                    'tempId': None,
                                                    'label': 'Sample',
                                                    'type': 'sample',
                                                    'titleTemplate': ['Sample ', 'positionOneBased'],
                                                    'dirty': True,
                                                    'fields': [
                                                        # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/randomChoiceInflow/fields/samples/fieldArgs/forms/sample/fields
                                                        {
                                                        # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/randomChoiceInflow/fields/samples/fieldArgs/forms/sample/fields/value
                                                            'fieldType': 'TEXT',
                                                            'fieldArgs': {
                                                                'displayAsTextArea': False,
                                                                'notEmpty': True,
                                                                'maxLength': 250,
                                                                'numberConfig': {
                                                                    'decimals': -1,
                                                                    'min': {
                                                                        'value': 0,
                                                                        'inclusive': True
                                                                    },
                                                                    'max': None
                                                                }
                                                            },
                                                            'propName': 'value',
                                                            'label': 'Value',
                                                            'valueData': '0',
                                                            'dirty': True
                                                        }
                                                        # end: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/randomChoiceInflow/fields/samples/fieldArgs/forms/sample/fields/value
                                                    ]
                                                # end: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/randomChoiceInflow/fields/samples/fieldArgs/forms/sample/fields
                                                }
                                                # end: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/randomChoiceInflow/fields/samples/fieldArgs/forms/sample
                                            ]
                                        # end: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/randomChoiceInflow/fields/samples/fieldArgs/forms
                                        },
                                    # end: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/randomChoiceInflow/fields/samples/fieldArgs
                                        'propName': 'samples',
                                        'label': 'Samples',
                                        'valueData': [
                                            # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/randomChoiceInflow/fields/samples/valueData
                                            {
                                            # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/randomChoiceInflow/fields/samples/valueData/sample
                                                'id': None,
                                                'tempId': None,
                                                'label': 'Sample',
                                                'type': 'sample',
                                                'titleTemplate': ['Sample ', 'positionOneBased'],
                                                'dirty': True,
                                                'fields': [
                                                    # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/randomChoiceInflow/fields/samples/valueData/sample/fields
                                                    {
                                                    # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/randomChoiceInflow/fields/samples/valueData/sample/fields/value
                                                        'fieldType': 'TEXT',
                                                        'fieldArgs': {
                                                            'displayAsTextArea': False,
                                                            'notEmpty': True,
                                                            'maxLength': 250,
                                                            'numberConfig': {
                                                                'decimals': -1,
                                                                'min': {
                                                                    'value': 0,
                                                                    'inclusive': True
                                                                },
                                                                'max': None
                                                            }
                                                        },
                                                        'propName': 'value',
                                                        'label': 'Value',
                                                        'valueData': '0',
                                                        'dirty': True
                                                    }
                                                    # end: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/randomChoiceInflow/fields/samples/valueData/sample/fields/value

                                                ]
                                            # end: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/randomChoiceInflow/fields/samples/valueData/sample/fields
                                            }
                                            # end: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/randomChoiceInflow/fields/samples/valueData/sample
                                        ],
                                    # end: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/randomChoiceInflow/fields/samples/valueData
                                        'dirty': True
                                    }
                                    # end: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/randomChoiceInflow/fields/samples
                                ]
                            # end: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/randomChoice/fields
                            },  # end: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/randomChoiceInflow
                            {
                            # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow

                                'id': None,
                                'tempId': None,
                                'label': 'Stochastic Function Inflow',
                                'type': 'stochasticFunctionInflow',
                                'titleTemplate': ['Period ', 'positionOneBased', ': ', 'label'],
                                'dirty': True,
                                'fields': [
                                    # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields
                                    # TODO: More distributions
                                    {
                                    # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf
                                        'fieldType': 'FORMS',
                                        'fieldArgs': {
                                        # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs
                                            'minForms': 1,
                                            'maxForms': 1,
                                            'forms': [
                                                # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms
                                                {
                                                    # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/normalDistribution
                                                    'id': None,
                                                    'tempId': None,
                                                    'label': 'Normal Distribution',
                                                    'type': 'normalDistribution',
                                                    'titleTemplate': ['', 'label'],
                                                    'dirty': True,
                                                    'fields': [
                                                        # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/normalDistribution/fields
                                                        {
                                                            # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/normalDistribution/fields/mean
                                                            'fieldType': 'TEXT',
                                                            'fieldArgs': {
                                                                'displayAsTextArea': False,
                                                                'notEmpty': True,
                                                                'maxLength': 250,
                                                                'numberConfig': {
                                                                    'decimals': -1,
                                                                    'min': None,
                                                                    'max': None
                                                                }
                                                            },
                                                            'propName': 'mean',
                                                            'label': 'Mean',
                                                            'valueData': '100',
                                                            'dirty': True
                                                        },
                                                        # end: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/normalDistribution/fields/mean
                                                        {
                                                            # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/normalDistribution/fields/variance
                                                            'fieldType': 'TEXT',
                                                            'fieldArgs': {
                                                                'displayAsTextArea': False,
                                                                'notEmpty': True,
                                                                'maxLength': 250,
                                                                'numberConfig': {
                                                                    'decimals': -1,
                                                                    'min': {
                                                                        'value': 0,
                                                                        'inclusive': True
                                                                    },
                                                                    'max': None
                                                                }
                                                            },
                                                            'propName': 'variance',
                                                            'label': 'Variance',
                                                            'valueData': '10',
                                                            'dirty': True
                                                        }
                                                        # end: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/normalDistribution/fields/variance
                                                    ]
                                                    # end: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/normalDistribution/fields
                                                },
                                                # end: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/normalDistribution
                                                {
                                                    # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/triangularDistribution
                                                    'id': None,
                                                    'tempId': None,
                                                    'label': 'Triangular Distribution',
                                                    'type': 'triangularDistribution',
                                                    'titleTemplate': ['', 'label'],
                                                    'dirty': True,
                                                    'fields': [
                                                        # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/triangularDistribution/fields
                                                        {
                                                            # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/triangularDistribution/fields/left
                                                            'fieldType': 'TEXT',
                                                            'fieldArgs': {
                                                                'displayAsTextArea': False,
                                                                'notEmpty': True,
                                                                'maxLength': 250,
                                                                'numberConfig': {
                                                                    'decimals': -1,
                                                                    'min': None,
                                                                    'max': None
                                                                }
                                                            },
                                                            'propName': 'left',
                                                            'label': 'Left',
                                                            'valueData': '0',
                                                            'dirty': True
                                                        },
                                                        # end: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/triangularDistribution/fields/left
                                                        {
                                                            # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/triangularDistribution/fields/mode
                                                            'fieldType': 'TEXT',
                                                            'fieldArgs': {
                                                                'displayAsTextArea': False,
                                                                'notEmpty': True,
                                                                'maxLength': 250,
                                                                'numberConfig': {
                                                                    'decimals': -1,
                                                                    'min': None,
                                                                    'max': None
                                                                }
                                                            },
                                                            'propName': 'mode',
                                                            'label': 'Mode',
                                                            'valueData': '0.5',
                                                            'dirty': True
                                                        },
                                                        # end: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/triangularDistribution/fields/mode
                                                        {
                                                            # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/triangularDistribution/fields/right
                                                            'fieldType': 'TEXT',
                                                            'fieldArgs': {
                                                                'displayAsTextArea': False,
                                                                'notEmpty': True,
                                                                'maxLength': 250,
                                                                'numberConfig': {
                                                                    'decimals': -1,
                                                                    'min': None,
                                                                    'max': None
                                                                }
                                                            },
                                                            'propName': 'right',
                                                            'label': 'Right',
                                                            'valueData': '1',
                                                            'dirty': True
                                                        }
                                                        # end: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/triangularDistribution/fields/right
                                                    ]
                                                    # end: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/triangularDistribution/fields
                                                },
                                                # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/triangularDistribution
                                                {
                                                    # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/uniformDistribution
                                                    'id': None,
                                                    'tempId': None,
                                                    'label': 'Uniform Distribution',
                                                    'type': 'uniformDistribution',
                                                    'titleTemplate': ['', 'label'],
                                                    'dirty': True,
                                                    'fields': [
                                                        # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/uniformDistribution/fields
                                                        {
                                                            # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/uniformDistribution/fields/low
                                                            'fieldType': 'TEXT',
                                                            'fieldArgs': {
                                                                'displayAsTextArea': False,
                                                                'notEmpty': True,
                                                                'maxLength': 250,
                                                                'numberConfig': {
                                                                    'decimals': -1,
                                                                    'min': None,
                                                                    'max': None
                                                                }
                                                            },
                                                            'propName': 'low',
                                                            'label': 'Low',
                                                            'valueData': '0',
                                                            'dirty': True
                                                        },
                                                        # end: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/uniformDistribution/fields/low
                                                        {
                                                            # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/uniformDistribution/fields/high
                                                            'fieldType': 'TEXT',
                                                            'fieldArgs': {
                                                                'displayAsTextArea': False,
                                                                'notEmpty': True,
                                                                'maxLength': 250,
                                                                'numberConfig': {
                                                                    'decimals': -1,
                                                                    'min': None,
                                                                    'max': None
                                                                }
                                                            },
                                                            'propName': 'high',
                                                            'label': 'High',
                                                            'valueData': '1',
                                                            'dirty': True
                                                        }
                                                        # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/uniformDistribution/fields/high
                                                    ]
                                                    # end: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/uniformDistribution/fields
                                                },
                                                # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/uniformDistribution
                                                {
                                                    # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/exponentialDistribution
                                                    'id': None,
                                                    'tempId': None,
                                                    'label': 'Exponential Distribution',
                                                    'type': 'exponentialDistribution',
                                                    'titleTemplate': ['', 'label'],
                                                    'dirty': True,
                                                    'fields': [
                                                        # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/exponentialDistribution/fields
                                                        {
                                                            # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/exponentialDistribution/fields/scale
                                                            'fieldType': 'TEXT',
                                                            'fieldArgs': {
                                                                'displayAsTextArea': False,
                                                                'notEmpty': True,
                                                                'maxLength': 250,
                                                                'numberConfig': {
                                                                    'decimals': -1,
                                                                    'min': {
                                                                        'value': 0,
                                                                        'inclusive': False
                                                                    },
                                                                    'max': None
                                                                }
                                                            },
                                                            'propName': 'scale',
                                                            'label': 'Scale (1 / lambda)',
                                                            'valueData': '1',
                                                            'dirty': True
                                                        },
                                                        # end: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/exponentialDistribution/fields/scale
                                                    ]
                                                    # end: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/exponentialDistribution/fields
                                                }
                                                # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/fieldArgs/forms/exponentialDistribution
                                                # TODO: more distributions
                                            ]
                                        },
                                        'propName': 'pdf',
                                        'label': 'Probability Density Function',
                                        'valueData': [
                                            # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/valueData
                                            {
                                                # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/valueData/normalDistribution
                                                'id': None,
                                                'tempId': None,
                                                'label': 'Normal Distribution',
                                                'type': 'normalDistribution',
                                                'titleTemplate': ['', 'label'],
                                                'dirty': True,
                                                'fields': [
                                                    # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/valueData/normalDistribution/fields
                                                    {
                                                        # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/valueData/normalDistribution/fields/mean
                                                        'fieldType': 'TEXT',
                                                        'fieldArgs': {
                                                            'displayAsTextArea': False,
                                                            'notEmpty': True,
                                                            'maxLength': 250,
                                                            'numberConfig': {
                                                                'decimals': -1,
                                                                'min': None,
                                                                'max': None
                                                            }
                                                        },
                                                        'propName': 'mean',
                                                        'label': 'Mean',
                                                        'valueData': '100',
                                                        'dirty': True
                                                    },
                                                    # end: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/valueData/normalDistribution/fields/mean
                                                    {
                                                        # start: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/valueData/normalDistribution/fields/variance
                                                        'fieldType': 'TEXT',
                                                        'fieldArgs': {
                                                            'displayAsTextArea': False,
                                                            'notEmpty': True,
                                                            'maxLength': 250,
                                                            'numberConfig': {
                                                                'decimals': -1,
                                                                'min': {
                                                                    'value': 0,
                                                                    'inclusive': True
                                                                },
                                                                'max': None
                                                            }
                                                        },
                                                        'propName': 'variance',
                                                        'label': 'Variance',
                                                        'valueData': '10',
                                                        'dirty': True
                                                    }
                                                    # end: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/valueData/normalDistribution/fields/variance
                                                ]
                                                # end: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/valueData/normalDistribution/fields
                                            }
                                            # end: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/valueData/normalDistribution
                                        ],
                                    # end: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf/valueData
                                        'dirty': True
                                    }
                                    # end: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields/pdf
                                ]
                            # end: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow/fields
                            }
                            # end: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms/stochasticFunctionInflow
                        ]  # end: externalListInflow/fields/singlePeriodInflows/fieldArgs/forms
                    },  # end: externalListInflow/fields/singlePeriodInflows/fieldArgs
                    'propName': 'singlePeriodInflows',
                    'label': 'Single Period Inflows',
                    'valueData': [  # start: externalListInflow/fields/singlePeriodInflows/valueData
                        {  # start: externalListInflow/fields/singlePeriodInflows/valueData/fixedValueInflow
                            'id': None,
                            'tempId': None,
                            'label': 'Fixed Value Inflow',
                            'type': 'fixedValueInflow',
                            'titleTemplate': ['Period ', 'positionOneBased', ': ', 'label'],
                            'dirty': True,
                            'fields': [
                                # start: externalListInflow/fields/singlePeriodInflows/valueData/fixedValueInflow/fields
                                {
                                # start: externalListInflow/fields/singlePeriodInflows/valueData/fixedValueInflow/fields/value
                                    'fieldType': 'TEXT',
                                    'fieldArgs': {
                                        'displayAsTextArea': False,
                                        'notEmpty': True,
                                        'maxLength': 250,
                                        'numberConfig': {
                                            'decimals': -1,
                                            'min': {
                                                'value': 0,
                                                'inclusive': True
                                            },
                                            'max': None
                                        }
                                    },
                                    'propName': 'value',
                                    'label': 'Value',
                                    'valueData': '1',
                                    'dirty': True
                                }
                                # end: externalListInflow/fields/singlePeriodInflows/valueData/fixedValueInflow/fields/value
                            ]  # end: externalListInflow/fields/singlePeriodInflows/valueData/fixedValueInflow/fields
                        }  # end: externalListInflow/fields/singlePeriodInflows/valueData/fixedValueInflow
                    ],  # end: externalListInflow/fields/singlePeriodInflows/valueData
                    'dirty': dirty
                }  # end: externalListInflow/fields/singlePeriodInflows
            ]  # end: externalFunctionInflow/fields
        }  # end: externalFunctionInflow


    @staticmethod
    def get_distribution_field_scaffold(min_forms, max_forms, prop_name, label, add_default, dirty):
        return {
            'fieldType': 'FORMS',
            'fieldArgs': {
                'minForms': min_forms,
                'maxForms': max_forms,
                'forms': [  # start: forms
                    {
                        # start: forms/normalDistribution
                        'id': None,
                        'tempId': None,
                        'label': 'Normal Distribution',
                        'type': 'normalDistribution',
                        'titleTemplate': ['', 'label'],
                        'dirty': True,
                        'fields': [
                            # start: forms/normalDistribution/fields
                            {
                                # start: forms/normalDistribution/fields/mean
                                'fieldType': 'TEXT',
                                'fieldArgs': {
                                    'displayAsTextArea': False,
                                    'notEmpty': True,
                                    'maxLength': 250,
                                    'numberConfig': {
                                        'decimals': -1,
                                        'min': None,
                                        'max': None
                                    }
                                },
                                'propName': 'mean',
                                'label': 'Mean',
                                'valueData': '0',
                                'dirty': True
                            },
                            # end: forms/normalDistribution/fields/mean
                            {
                                # start: forms/normalDistribution/fields/variance
                                'fieldType': 'TEXT',
                                'fieldArgs': {
                                    'displayAsTextArea': False,
                                    'notEmpty': True,
                                    'maxLength': 250,
                                    'numberConfig': {
                                        'decimals': -1,
                                        'min': {
                                            'value': 0,
                                            'inclusive': True
                                        },
                                        'max': None
                                    }
                                },
                                'propName': 'variance',
                                'label': 'Variance',
                                'valueData': '1',
                                'dirty': True
                            }
                            # end: forms/normalDistribution/fields/variance
                        ]
                        # end: forms/normalDistribution/fields
                    },
                    # end: forms/normalDistribution
                    {
                        # start: forms/triangularDistribution
                        'id': None,
                        'tempId': None,
                        'label': 'Triangular Distribution',
                        'type': 'triangularDistribution',
                        'titleTemplate': ['', 'label'],
                        'dirty': True,
                        'fields': [
                            # start: forms/triangularDistribution/fields
                            {
                                # start: forms/triangularDistribution/fields/left
                                'fieldType': 'TEXT',
                                'fieldArgs': {
                                    'displayAsTextArea': False,
                                    'notEmpty': True,
                                    'maxLength': 250,
                                    'numberConfig': {
                                        'decimals': -1,
                                        'min': None,
                                        'max': None
                                    }
                                },
                                'propName': 'left',
                                'label': 'Left',
                                'valueData': '0',
                                'dirty': True
                            },
                            # end: forms/triangularDistribution/fields/left
                            {
                                # start: forms/triangularDistribution/fields/mode
                                'fieldType': 'TEXT',
                                'fieldArgs': {
                                    'displayAsTextArea': False,
                                    'notEmpty': True,
                                    'maxLength': 250,
                                    'numberConfig': {
                                        'decimals': -1,
                                        'min': None,
                                        'max': None
                                    }
                                },
                                'propName': 'mode',
                                'label': 'Mode',
                                'valueData': '0.5',
                                'dirty': True
                            },
                            # end: forms/triangularDistribution/fields/mode
                            {
                                # start: forms/triangularDistribution/fields/right
                                'fieldType': 'TEXT',
                                'fieldArgs': {
                                    'displayAsTextArea': False,
                                    'notEmpty': True,
                                    'maxLength': 250,
                                    'numberConfig': {
                                        'decimals': -1,
                                        'min': None,
                                        'max': None
                                    }
                                },
                                'propName': 'right',
                                'label': 'Right',
                                'valueData': '1',
                                'dirty': True
                            }
                            # end: forms/triangularDistribution/fields/right
                        ]
                        # end: forms/triangularDistribution/fields
                    },
                    # start: forms/triangularDistribution
                    {
                        # start: forms/uniformDistribution
                        'id': None,
                        'tempId': None,
                        'label': 'Uniform Distribution',
                        'type': 'uniformDistribution',
                        'titleTemplate': ['', 'label'],
                        'dirty': True,
                        'fields': [
                            # start: forms/uniformDistribution/fields
                            {
                                # start: forms/uniformDistribution/fields/low
                                'fieldType': 'TEXT',
                                'fieldArgs': {
                                    'displayAsTextArea': False,
                                    'notEmpty': True,
                                    'maxLength': 250,
                                    'numberConfig': {
                                        'decimals': -1,
                                        'min': None,
                                        'max': None
                                    }
                                },
                                'propName': 'low',
                                'label': 'Low',
                                'valueData': '0',
                                'dirty': True
                            },
                            # end: forms/uniformDistribution/fields/low
                            {
                                # start: forms/uniformDistribution/fields/high
                                'fieldType': 'TEXT',
                                'fieldArgs': {
                                    'displayAsTextArea': False,
                                    'notEmpty': True,
                                    'maxLength': 250,
                                    'numberConfig': {
                                        'decimals': -1,
                                        'min': None,
                                        'max': None
                                    }
                                },
                                'propName': 'high',
                                'label': 'High',
                                'valueData': '1',
                                'dirty': True
                            }
                            # end: forms/uniformDistribution/fields/high
                        ]
                        # end: forms/uniformDistribution/fields
                    },
                    # start: forms/uniformDistribution
                    {
                        # start: forms/exponentialDistribution
                        'id': None,
                        'tempId': None,
                        'label': 'Exponential Distribution',
                        'type': 'exponentialDistribution',
                        'titleTemplate': ['', 'label'],
                        'dirty': True,
                        'fields': [
                            # start: forms/exponentialDistribution/fields
                            {
                                # start: forms/exponentialDistribution/fields/scale
                                'fieldType': 'TEXT',
                                'fieldArgs': {
                                    'displayAsTextArea': False,
                                    'notEmpty': True,
                                    'maxLength': 250,
                                    'numberConfig': {
                                        'decimals': -1,
                                        'min': {
                                            'value': 0,
                                            'inclusive': False
                                        },
                                        'max': None
                                    }
                                },
                                'propName': 'scale',
                                'label': 'Scale (1 / lambda)',
                                'valueData': '1',
                                'dirty': True
                            },
                            # end: forms/exponentialDistribution/fields/scale
                        ]
                        # end: forms/exponentialDistribution/fields
                    }
                    # end: forms/exponentialDistribution

                    # TODO: more distributions
                ]  # end: forms
            },
            'propName': prop_name,
            'label': label,
            'valueData': [],
            'dirty': dirty
        }