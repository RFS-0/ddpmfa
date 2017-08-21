(function(ModelDesigner) {
	'use strict';
	
	var attachTestData = function(elemQ) {
		var testData = {
			nodes: [
				{
					titleLabelPath: ['name', 'valueData'],
					id: '1',
					tempId: null,
					position: { x: 5040, y: 5030 },
					classes: ['inflow', 'external-list-inflow'],
					maxOutgoing: 1,
					minOutgoing: 1,
					maxIncoming: 0,
					minIncoming: 0,
					props: {
						type: 'EXTERNAL_LIST_INFLOW'
					},
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
								forms: [
									{
										id: null,
										tempId: null,
										label: 'Fixed Value Inflow',
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
											valueData: '0.3',
											dirty: false
										}
									]
								},
								{
									id: 2,
									tempId: null,
									label: 'Stochastic Function Inflow',
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
					titleLabelPath: ['name', 'valueData'],
					id: '2',
					tempId: null,
					position: { x: 5350, y: 5200 },
					classes: ['compartment', 'flow-compartment'],
					maxOutgoing: -1,
					minOutgoing: 1,
					maxIncoming: -1,
					minIncoming: 1,
					props: {
						type: 'FLOW_COMPARTMENT'
					},
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
					titleLabelPath: ['name', 'valueData'],
					id: '3',
					tempId: null,
					position: { x: 5650, y: 5040 },
					classes: ['compartment', 'flow-compartment'],
					maxOutgoing: -1,
					minOutgoing: 1,
					maxIncoming: -1,
					minIncoming: 1,
					props: {
						type: 'FLOW_COMPARTMENT'
					},
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
				}
				
				
				
				
				
				
				
				
			],
			
			
			
			
			
			
			
			
			
			
			
			
			connections: [
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			],
			connectionTypes: [
				{
					typeName: 'constantTransfer',
					fields: []
				},
				{
					typeName: 'randomChoiceTransfer',
					fields: []
				},
				{
					typeName: 'aggregatedTransfer',
					fields: []
				},
				{
					typeName: 'stochasticTransfer',
					fields: []
				}
			]
		};
		elemQ.data('model', testData);
	};
	
	ModelDesigner.installAllEventually(
		function() {}, // Called when installation of ModelDesigners start
		function(instances) {}, // Called when all ModelDesigners have been installed
		function(modelDesigner, containerQ) { // Called before modelDesigner is installed in containerQ
			attachTestData(containerQ);
		},
		function(modelDesigner, containerQ) { // Called after modelDesigner was installed in containerQ
			
		}
	);
})(window.rgm.modes.ModelDesigner);


	
/*
	var cQ = jQuery('.rgm-modes-form-demo');
	// jQuery('[data-toggle=modal]').click();
	var ns = window.%rgm.%modes;
	
// 	var nv = new ns.%NumberValidator(
// 		2,
// 		new ns.%NumberBound(0, true, false),
// 		new ns.%NumberBound(1000, false, true)
// 	);
// 	var nv = ns.%NumberValidator.%newFromConfig({
// 		decimals: 2,
// 		min: {
// 			value: 0,
// 			inclusive: false
// 		},
// 		max: {
// 			value: 1000,
// 			inclusive: true
// 		}
// 	});
// 	console.log(nv.%check('-1.0'));
// 	console.log(nv.%check('0.00'));
// 	console.log(nv.%check('1.22'));
// 	console.log(nv.%check('999.9999999999999'));
// 	console.log(nv.%check('1000'));
// 	console.log(nv.%check('1000.01'));
// 	console.log(nv.%check(''));
// 	console.log(nv.%check('-.'));
// 	console.log(nv.%check('1.0.0'));
// 	console.log(nv.%check('.1'));
// 	console.log(nv.%check('1.'));
// 	console.log(nv.%check('01'));

	
	var mapFieldFactory = new ns.%MapFieldFactory();
	var textFieldFactory = new ns.%TextFieldFactory();
	var SubformsFieldFactory = new ns.%SubformsFieldFactory(mapFieldFactory);
	
	mapFieldFactory.%putFactory('TEXT', textFieldFactory);
	mapFieldFactory.%putFactory('FORMS', SubformsFieldFactory);
	
	var fieldDefs = [
	
	
	
		{
			fieldType: 'TEXT',
			fieldArgs: {
				displayAsTextArea: false,
				notEmpty: true,
				maxLength: 200,
				numberConfig: {
					decimals: 0,
					min: {
						value: 0,
						inclusive: false
					},
					max: null
				}
			},
			propName: 'runs',
			label: 'Runs',
			valueData: '10',
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
				forms: [
					{
						id: null,
						label: 'Fixed Value Inflow',
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
						label: 'Stochastic Function Inflow',
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
					label: 'Fixed Value Inflow',
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
							valueData: '0.3',
							dirty: false
						}
					]
				},
				{
					id: 2,
					label: 'Stochastic Function Inflow',
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
		
		
		
	];
	var fields = [];
	
	for (var i = 0; i < fieldDefs.length; ++i) {
		var fieldDef = fieldDefs[i];
		var field = mapFieldFactory.%newFieldFromDef(fieldDef);
		field.%addToDocument(cQ);
		fields.push(field);
	}
	
	$('#exampleModalLong').modal('show');
	$('#exampleModalLong').on('hide.bs.modal', function (event) {
		for (var i = 0; i < fields.length; ++i) {
			var field = fields[i];
			field.%synchronize();
			field.%isDirty();
			console.log(field.%asDataObject());
			console.log(field.%check());
		}
		
		
		event.preventDefault();
     	event.stopImmediatePropagation();
     	return false; 
	});
*/