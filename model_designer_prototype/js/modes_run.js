(function(ModelDesigner) {
	'use strict';
	
	var attachTestData = function(elemQ) {
		var testData = {
			id: 1,
			valid: true,
			cyclesAllowed: false,
			parallelsAllowed: false,
			nodes: [
				{
					title: null,
					titleLabelPath: ['name', 'valueData'],
					typeName: 'externalListInflow',
					typeLabel: 'External List Inflow',
					id: '1',
					tempId: null,
					position: { x: 5040, y: 5030 },
					classes: ['inflow', 'external-list-inflow'],
					maxOutgoing: 1,
					minOutgoing: 1,
					maxIncoming: 0,
					minIncoming: 0,
					outConnectionTypes: ['inflowTarget'],
					dirty: false,
					fields: [
						{
							fieldType: 'TEXT',
							fieldArgs: {
								displayAsTextArea: false,
								notEmpty: true,
								maxLength: 200,
								numberConfig: null
							},
							propName: 'name',
							label: 'Name',
							valueData: 'Some inflow',
							dirty: false
						},
						{
							fieldType: 'TEXT',
							fieldArgs: {
								displayAsTextArea: true,
								notEmpty: false,
								maxLength: -1,
								numberConfig: null
							},
							propName: 'description',
							label: 'Description',
							valueData: 'A description',
							dirty: false
						},
						{
							fieldType: 'FORMS',
							fieldArgs: {
								minForms: 1,
								maxForms: -1,
								forms: [
									{
										id: null,
										tempId: null,
										label: 'Fixed Value Inflow',
										titleTemplate: ['Period ', 'positionOneBased', ': ', 'label'],
										dirty: true,
										fields: [
											{
												fieldType: 'TEXT',
												fieldArgs: {
													displayAsTextArea: false,
													notEmpty: true,
													maxLength: 200,
													numberConfig: {
														decimals: -1,
														min: {
															value: 0,
															inclusive: true
														},
														max: null
													}
												},
												propName: 'value',
												label: 'Value',
												valueData: '0',
												dirty: true
											}
										]
									},
									{
										id: null,
										tempId: null,
										label: 'Stochastic Function Inflow',
										titleTemplate: ['Period ', 'positionOneBased', ': ', 'label'],
										dirty: true,
										fields: [
											{
												fieldType: 'TEXT',
												fieldArgs: {
													displayAsTextArea: false,
													notEmpty: true,
													maxLength: 200,
													numberConfig: null
												},
												propName: 'functionName',
												label: 'Function Name',
												valueData: 'normal',
												dirty: false
											},
											{
												fieldType: 'TEXT',
												fieldArgs: {
													displayAsTextArea: false,
													notEmpty: true,
													maxLength: 200,
													numberConfig: null
												},
												propName: 'parameters',
												label: 'Parameters',
												valueData: 'hans,peter,1,2,3',
												dirty: false
											}
										],
										dirty: true
									}
								]
							},
							propName: 'singlePeriodInflows',
							label: 'Single Period Inflows',
							valueData: [
								{
									id: 1,
									tempId: null,
									label: 'Fixed Value Inflow',
									titleTemplate: ['Period ', 'positionOneBased', ': ', 'label'],
									dirty: false,
									fields: [
										{
											fieldType: 'TEXT',
											fieldArgs: {
												displayAsTextArea: false,
												notEmpty: true,
												maxLength: 200,
												numberConfig: {
													decimals: -1,
													min: {
														value: 0,
														inclusive: true
													},
													max: null
												}
											},
											propName: 'value',
											label: 'Value',
											valueData: '0.3',
											dirty: false
										}
									]
								},
								{
									id: 2,
									tempId: null,
									label: 'Stochastic Function Inflow',
									titleTemplate: ['Period ', 'positionOneBased', ': ', 'label'],
									dirty: false,
									fields: [
										{
											fieldType: 'TEXT',
											fieldArgs: {
												displayAsTextArea: false,
												notEmpty: true,
												maxLength: 200,
												numberConfig: null
											},
											propName: 'functionName',
											label: 'Function Name',
											valueData: 'normal',
											dirty: false
										},
										{
											fieldType: 'TEXT',
											fieldArgs: {
												displayAsTextArea: false,
												notEmpty: true,
												maxLength: 200,
												numberConfig: null
											},
											propName: 'parameters',
											label: 'Parameters',
											valueData: 'hans,peter,1,2,3',
											dirty: false
										}
									],
									dirty: false
								}
							]
						}
					]
				},
				
				
				
				{
					title: null,
					titleLabelPath: ['name', 'valueData'],
					typeName: 'flowCompartment',
					typeLabel: 'Flow Compartment',
					id: '2',
					tempId: null,
					position: { x: 5350, y: 5200 },
					classes: ['compartment', 'flow-compartment'],
					maxOutgoing: -1,
					minOutgoing: 1,
					maxIncoming: -1,
					minIncoming: 1,
					outConnectionTypes: ['constantTransfer', 'randomChoiceTransfer', 'aggregatedTransfer', 'stochasticTransfer'],
					dirty: false,
					fields: [
						{
							fieldType: 'TEXT',
							fieldArgs: {
								displayAsTextArea: false,
								notEmpty: true,
								maxLength: 200,
								numberConfig: null
							},
							propName: 'name',
							label: 'Name',
							valueData: 'A flow compartment',
							dirty: false
						},
						{
							fieldType: 'TEXT',
							fieldArgs: {
								displayAsTextArea: true,
								notEmpty: false,
								maxLength: -1,
								numberConfig: null
							},
							propName: 'description',
							label: 'Description',
							valueData: 'A description',
							dirty: false
						},
						{
							fieldType: 'CHECK',
							fieldArgs: {},
							propName: 'logInflows',
							label: 'Log inflows',
							valueData: true,
							dirty: false
						},
						{
							fieldType: 'CHECK',
							fieldArgs: {},
							propName: 'logOutflows',
							label: 'Log outflows',
							valueData: false,
							dirty: false
						},
						{
							fieldType: 'CHECK',
							fieldArgs: {},
							propName: 'adjustOutgoingTcs',
							label: 'Adjust Outgoing TCs',
							valueData: true,
							dirty: false
						}
					]
				},
				
				
				
				
				
				
				
				
				{
					title: null,
					titleLabelPath: ['name', 'valueData'],
					typeName: 'flowCompartment',
					typeLabel: 'Flow Compartment',
					id: '3',
					tempId: null,
					position: { x: 5650, y: 5040 },
					classes: ['compartment', 'flow-compartment'],
					maxOutgoing: -1,
					minOutgoing: 1,
					maxIncoming: -1,
					minIncoming: 1,
					outConnectionTypes: ['constantTransfer', 'randomChoiceTransfer', 'aggregatedTransfer', 'stochasticTransfer'],
					dirty: false,
					fields: [
						{
							fieldType: 'TEXT',
							fieldArgs: {
								displayAsTextArea: false,
								notEmpty: true,
								maxLength: 200,
								numberConfig: null
							},
							propName: 'name',
							label: 'Name',
							valueData: 'Another flow compartment',
							dirty: false
						},
						{
							fieldType: 'TEXT',
							fieldArgs: {
								displayAsTextArea: true,
								notEmpty: false,
								maxLength: -1,
								numberConfig: null
							},
							propName: 'description',
							label: 'Description',
							valueData: 'A description',
							dirty: false
						},
						{
							fieldType: 'CHECK',
							fieldArgs: {},
							propName: 'logInflows',
							label: 'Log inflows',
							valueData: true,
							dirty: false
						},
						{
							fieldType: 'CHECK',
							fieldArgs: {},
							propName: 'logOutflows',
							label: 'Log outflows',
							valueData: false,
							dirty: false
						},
						{
							fieldType: 'CHECK',
							fieldArgs: {},
							propName: 'adjustOutgoingTcs',
							label: 'Adjust Outgoing TCs',
							valueData: true,
							dirty: false
						}
					]
				},
				
				
				
				
				
				
				
				{
					title: null,
					titleLabelPath: ['name', 'valueData'],
					typeName: 'flowCompartment',
					typeLabel: 'Flow Compartment',
					id: '4',
					tempId: null,
					position: { x: 5750, y: 5340 },
					classes: ['compartment', 'flow-compartment'],
					maxOutgoing: -1,
					minOutgoing: 1,
					maxIncoming: -1,
					minIncoming: 1,
					outConnectionTypes: ['constantTransfer', 'randomChoiceTransfer', 'aggregatedTransfer', 'stochasticTransfer'],
					dirty: false,
					fields: [
						{
							fieldType: 'TEXT',
							fieldArgs: {
								displayAsTextArea: false,
								notEmpty: true,
								maxLength: 200,
								numberConfig: null
							},
							propName: 'name',
							label: 'Name',
							valueData: 'Yet an other flow compartment',
							dirty: false
						},
						{
							fieldType: 'TEXT',
							fieldArgs: {
								displayAsTextArea: true,
								notEmpty: false,
								maxLength: -1,
								numberConfig: null
							},
							propName: 'description',
							label: 'Description',
							valueData: 'A description',
							dirty: false
						},
						{
							fieldType: 'CHECK',
							fieldArgs: {},
							propName: 'logInflows',
							label: 'Log inflows',
							valueData: true,
							dirty: false
						},
						{
							fieldType: 'CHECK',
							fieldArgs: {},
							propName: 'logOutflows',
							label: 'Log outflows',
							valueData: false,
							dirty: false
						},
						{
							fieldType: 'CHECK',
							fieldArgs: {},
							propName: 'adjustOutgoingTcs',
							label: 'Adjust Outgoing TCs',
							valueData: true,
							dirty: false
						}
					]
				},
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				{
					title: null,
					titleLabelPath: ['name', 'valueData'],
					typeName: 'externalFunctionInflow',
					typeLabel: 'External Function Inflow',
					id: '5',
					tempId: null,
					position: { x: 5150, y: 5400 },
					classes: ['inflow', 'external-function-inflow'],
					maxOutgoing: 1,
					minOutgoing: 1,
					maxIncoming: 0,
					minIncoming: 0,
					outConnectionTypes: ['inflowTarget'],
					dirty: false,
					fields: [
						{
							fieldType: 'TEXT',
							fieldArgs: {
								displayAsTextArea: false,
								notEmpty: true,
								maxLength: 200,
								numberConfig: null
							},
							propName: 'name',
							label: 'Name',
							valueData: 'An external function inflow',
							dirty: false
						},
					]
				},
				
				
				{
					title: null,
					titleLabelPath: ['name', 'valueData'],
					typeName: 'stock',
					typeLabel: 'Stock',
					id: '6',
					tempId: null,
					position: { x: 5350, y: 5400 },
					classes: ['compartment', 'stock'],
					maxOutgoing: -1,
					minOutgoing: 1,
					maxIncoming: -1,
					minIncoming: 1,
					outConnectionTypes: ['constantTransfer', 'randomChoiceTransfer', 'aggregatedTransfer', 'stochasticTransfer'],
					dirty: false,
					fields: [
						{
							fieldType: 'TEXT',
							fieldArgs: {
								displayAsTextArea: false,
								notEmpty: true,
								maxLength: 200,
								numberConfig: null
							},
							propName: 'name',
							label: 'Name',
							valueData: 'A stock',
							dirty: false
						},
					]
				},
				
				
				{
					title: null,
					titleLabelPath: ['name', 'valueData'],
					typeName: 'sink',
					typeLabel: 'Sink',
					id: '7',
					tempId: null,
					position: { x: 5550, y: 5400 },
					classes: ['compartment', 'sink'],
					maxOutgoing: 0,
					minOutgoing: 0,
					maxIncoming: -1,
					minIncoming: 1,
					outConnectionTypes: [],
					dirty: false,
					fields: [
						{
							fieldType: 'TEXT',
							fieldArgs: {
								displayAsTextArea: false,
								notEmpty: true,
								maxLength: 200,
								numberConfig: null
							},
							propName: 'name',
							label: 'Name',
							valueData: 'A Sink',
							dirty: false
						},
					]
				},
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
			],
			
			
			
			
			
			
			
			
			
			
			
			
			
			nodeTypes: [
			
			
			
				{ // Node type external list inflow
					title: null,
					titleLabelPath: ['name', 'valueData'],
					typeName: 'externalListInflow',
					typeLabel: 'External List Inflow',
					id: null,
					tempId: null,
					position: null,
					classes: ['inflow', 'external-list-inflow'],
					maxOutgoing: 1,
					minOutgoing: 1,
					maxIncoming: 0,
					minIncoming: 0,
					outConnectionTypes: ['inflowTarget'],
					dirty: true,
					fields: [
						{
							fieldType: 'TEXT',
							fieldArgs: {
								displayAsTextArea: false,
								notEmpty: true,
								maxLength: 200,
								numberConfig: null
							},
							propName: 'name',
							label: 'Name',
							valueData: 'New External List Inflow',
							dirty: false
						},
						{
							fieldType: 'TEXT',
							fieldArgs: {
								displayAsTextArea: true,
								notEmpty: false,
								maxLength: -1,
								numberConfig: null
							},
							propName: 'description',
							label: 'Description',
							valueData: '',
							dirty: false
						},
						{
							fieldType: 'FORMS',
							fieldArgs: {
								minForms: 1,
								maxForms: -1,
								forms: [
									{
										id: null,
										tempId: null,
										label: 'Fixed Value Inflow',
										titleTemplate: ['Period ', 'positionOneBased', ': ', 'label'],
										dirty: true,
										fields: [
											{
												fieldType: 'TEXT',
												fieldArgs: {
													displayAsTextArea: false,
													notEmpty: true,
													maxLength: 200,
													numberConfig: null
												},
												propName: 'value',
												label: 'Value',
												valueData: '0',
												dirty: true
											}
										]
									},
									{
										id: null,
										tempId: null,
										label: 'Stochastic Function Inflow',
										titleTemplate: ['Period ', 'positionOneBased', ': ', 'label'],
										dirty: true,
										fields: [
											{
												fieldType: 'TEXT',
												fieldArgs: {
													displayAsTextArea: false,
													notEmpty: true,
													maxLength: 200,
													numberConfig: null
												},
												propName: 'functionName',
												label: 'Function Name',
												valueData: 'normal',
												dirty: false
											},
											{
												fieldType: 'TEXT',
												fieldArgs: {
													displayAsTextArea: false,
													notEmpty: true,
													maxLength: 200,
													numberConfig: null
												},
												propName: 'parameters',
												label: 'Parameters',
												valueData: 'hans,peter,1,2,3',
												dirty: false
											}
										],
										dirty: true
									}
								]
							},
							propName: 'singlePeriodInflows',
							label: 'Single Period Inflows',
							valueData: []
						}
					]
				}, // end of node type external list inflow
			
			
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				{
					title: null,
					titleLabelPath: ['name', 'valueData'],
					typeName: 'externalFunctionInflow',
					typeLabel: 'External Function Inflow',
					id: null,
					tempId: null,
					position: null,
					classes: ['inflow', 'external-function-inflow'],
					maxOutgoing: 1,
					minOutgoing: 1,
					maxIncoming: 0,
					minIncoming: 0,
					outConnectionTypes: ['inflowTarget'],
					dirty: true,
					fields: [
						{
							fieldType: 'TEXT',
							fieldArgs: {
								displayAsTextArea: false,
								notEmpty: true,
								maxLength: 200,
								numberConfig: null
							},
							propName: 'name',
							label: 'Name',
							valueData: 'New External Function Inflow',
							dirty: false
						}
					]
				},
			
			
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				{
					title: null,
					titleLabelPath: ['name', 'valueData'],
					typeName: 'flowCompartment',
					typeLabel: 'Flow Compartment',
					id: null,
					tempId: null,
					position: null,
					classes: ['compartment', 'flow-compartment'],
					maxOutgoing: -1,
					minOutgoing: 1,
					maxIncoming: -1,
					minIncoming: 1,
					outConnectionTypes: ['constantTransfer', 'randomChoiceTransfer', 'aggregatedTransfer', 'stochasticTransfer'],
					dirty: true,
					fields: [
						{
							fieldType: 'TEXT',
							fieldArgs: {
								displayAsTextArea: false,
								notEmpty: true,
								maxLength: 200,
								numberConfig: null
							},
							propName: 'name',
							label: 'Name',
							valueData: 'New Flow Compartment',
							dirty: false
						},
						{
							fieldType: 'TEXT',
							fieldArgs: {
								displayAsTextArea: true,
								notEmpty: false,
								maxLength: -1,
								numberConfig: null
							},
							propName: 'description',
							label: 'Description',
							valueData: 'A description',
							dirty: false
						},
						{
							fieldType: 'CHECK',
							fieldArgs: {},
							propName: 'logInflows',
							label: 'Log inflows',
							valueData: true,
							dirty: false
						},
						{
							fieldType: 'CHECK',
							fieldArgs: {},
							propName: 'logOutflows',
							label: 'Log outflows',
							valueData: false,
							dirty: false
						},
						{
							fieldType: 'CHECK',
							fieldArgs: {},
							propName: 'adjustOutgoingTcs',
							label: 'Adjust Outgoing TCs',
							valueData: true,
							dirty: false
						}
					]
				},
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				{
					title: null,
					titleLabelPath: ['name', 'valueData'],
					typeName: 'stock',
					typeLabel: 'Stock',
					id: null,
					tempId: null,
					position: null,
					classes: ['compartment', 'stock'],
					maxOutgoing: -1,
					minOutgoing: 1,
					maxIncoming: -1,
					minIncoming: 1,
					outConnectionTypes: ['constantTransfer', 'randomChoiceTransfer', 'aggregatedTransfer', 'stochasticTransfer'],
					dirty: true,
					fields: [
						{
							fieldType: 'TEXT',
							fieldArgs: {
								displayAsTextArea: false,
								notEmpty: true,
								maxLength: 200,
								numberConfig: null
							},
							propName: 'name',
							label: 'Name',
							valueData: 'New Stock',
							dirty: false
						},
						{
							fieldType: 'TEXT',
							fieldArgs: {
								displayAsTextArea: true,
								notEmpty: false,
								maxLength: -1,
								numberConfig: null
							},
							propName: 'description',
							label: 'Description',
							valueData: 'A description',
							dirty: false
						},
						{
							fieldType: 'CHECK',
							fieldArgs: {},
							propName: 'logInflows',
							label: 'Log inflows',
							valueData: true,
							dirty: false
						},
						{
							fieldType: 'CHECK',
							fieldArgs: {},
							propName: 'logOutflows',
							label: 'Log outflows',
							valueData: false,
							dirty: false
						},
						{
							fieldType: 'CHECK',
							fieldArgs: {},
							propName: 'adjustOutgoingTcs',
							label: 'Adjust Outgoing TCs',
							valueData: true,
							dirty: false
						}
					]
				},
				
				
				
				
				
				
				
				
				
				
				{
					title: null,
					titleLabelPath: ['name', 'valueData'],
					typeName: 'sink',
					typeLabel: 'Sink',
					id: null,
					tempId: null,
					position: null,
					classes: ['compartment', 'sink'],
					maxOutgoing: -1,
					minOutgoing: 0,
					maxIncoming: -1,
					minIncoming: 1,
					outConnectionTypes: [],
					dirty: true,
					fields: [
						{
							fieldType: 'TEXT',
							fieldArgs: {
								displayAsTextArea: false,
								notEmpty: true,
								maxLength: 200,
								numberConfig: null
							},
							propName: 'name',
							label: 'Name',
							valueData: 'New Sink',
							dirty: false
						},
						{
							fieldType: 'TEXT',
							fieldArgs: {
								displayAsTextArea: true,
								notEmpty: false,
								maxLength: -1,
								numberConfig: null
							},
							propName: 'description',
							label: 'Description',
							valueData: 'A description',
							dirty: false
						},
						{
							fieldType: 'CHECK',
							fieldArgs: {},
							propName: 'logInflows',
							label: 'Log inflows',
							valueData: true,
							dirty: false
						},
						{
							fieldType: 'CHECK',
							fieldArgs: {},
							propName: 'logOutflows',
							label: 'Log outflows',
							valueData: false,
							dirty: false
						},
						{
							fieldType: 'CHECK',
							fieldArgs: {},
							propName: 'adjustOutgoingTcs',
							label: 'Adjust Outgoing TCs',
							valueData: true,
							dirty: false
						}
					]
				}
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			], // end of nodeTypes
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			connections: [
			
				
				
				{
					id: '1',
					tempId: null,
					typeName: 'inflowTarget',
					typeLabel: 'Inflow Target',
					title: 'into',
					titleLabelPath: null,
					sourceNode: {
						id: '1',
						tempId: null
					},
					targetNode: {
						id: '2',
						tempId: null
					},
					dirty: false,
					fields: []
				},
				
				
				
			
				{
					id: '2',
					tempId: null,
					typeName: 'constantTransfer',
					typeLabel: 'Constant Transfer',
					title: null,
					titleLabelPath: ['name', 'valueData'],
					sourceNode: {
						id: '2',
						tempId: null
					},
					targetNode: {
						id: '3',
						tempId: null
					},
					dirty: false,
					fields: [
						{
							fieldType: 'TEXT',
							fieldArgs: {
								displayAsTextArea: false,
								notEmpty: true,
								maxLength: 200,
								numberConfig: null
							},
							propName: 'name',
							label: 'Name',
							valueData: 'My First Contant Transfer',
							dirty: false
						}
					]
				},
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			],
			connectionTypes: [
				{
					id: null,
					tempId: null,
					typeName: 'inflowTarget',
					typeLabel: 'Inflow Target Connection',
					title: 'Inflow Target',
					titleLabelPath: null,
					dirty: true,
					fields: []
				},
				{
					id: null,
					tempId: null,
					typeName: 'constantTransfer',
					typeLabel: 'Constant Transfer',
					title: null,
					titleLabelPath: ['name', 'valueData'],
					dirty: true,
					fields: [
						{
							fieldType: 'TEXT',
							fieldArgs: {
								displayAsTextArea: false,
								notEmpty: true,
								maxLength: 200,
								numberConfig: null
							},
							propName: 'name',
							label: 'Name',
							valueData: 'New Constant Transfer',
							dirty: false
						}
					]
				},
				{
					id: null,
					tempId: null,
					typeName: 'randomChoiceTransfer',
					typeLabel: 'Random Choice Transfer',
					title: null,
					titleLabelPath: ['name', 'valueData'],
					dirty: true,
					fields: [
						{
							fieldType: 'TEXT',
							fieldArgs: {
								displayAsTextArea: false,
								notEmpty: true,
								maxLength: 200,
								numberConfig: null
							},
							propName: 'name',
							label: 'Name',
							valueData: 'New Random Choice Transfer',
							dirty: false
						}
					]
				},
				{
					id: null,
					tempId: null,
					typeName: 'aggregatedTransfer',
					typeLabel: 'Aggregated Transfer',
					title: null,
					titleLabelPath: ['name', 'valueData'],
					dirty: true,
					fields: [
						{
							fieldType: 'TEXT',
							fieldArgs: {
								displayAsTextArea: false,
								notEmpty: true,
								maxLength: 200,
								numberConfig: null
							},
							propName: 'name',
							label: 'Name',
							valueData: 'New Aggregated Transfer',
							dirty: false
						}
					]
				},
				{
					id: null,
					tempId: null,
					typeName: 'stochasticTransfer',
					typeLabel: 'Stochastic Transfer',
					title: null,
					titleLabelPath: ['name', 'valueData'],
					dirty: true,
					fields: [
						{
							fieldType: 'TEXT',
							fieldArgs: {
								displayAsTextArea: false,
								notEmpty: true,
								maxLength: 200,
								numberConfig: null
							},
							propName: 'name',
							label: 'Name',
							valueData: 'New Stochastic Transfer',
							dirty: false
						}
					]
				}
			]
		};
		elemQ.data('model', testData);
		
		var saveUrl = elemQ.data('saveurl');
		if (typeof saveUrl == 'undefined' || saveUrl == null || saveUrl == false || saveUrl == '') {
			saveUrl = '/this/is/a/fake/url/';
			elemQ.data('saveurl', saveUrl);
		}
	};
	
	ModelDesigner.installAllEventually(
		function() {}, // Called when installation of `ModelDesigner`s start
		function(instances) {}, // Called when all `ModelDesigner`s have been installed
		function(modelDesigner, containerQ) { // Called before `modelDesigner` is installed in `containerQ`
			attachTestData(containerQ);
		},
		function(modelDesigner, containerQ) {}, // Called after `modelDesigner` was installed in `containerQ`
		function(fieldFactory) {} // Lets you put custom `FieldFactory`s to the `fieldFactory` of the `ModelDesigner` being installed
	);
})(window.rgm.modes.ModelDesigner);
