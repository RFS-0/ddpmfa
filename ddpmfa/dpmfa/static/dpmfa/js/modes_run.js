(function(ModelDesigner) {
	'use strict';
	
	var attachTestData = function(elemQ) {
		var modelData = elemQ.data('model');
		if (typeof modelData != 'undefined' && modelData != null && modelData != false && modelData != '') {
			return;
		}
		var testData = {
			id: 1,
			valid: true,
			cyclesAllowed: false,
			parallelsAllowed: false,
			nodes: [],
			nodeTypes: [],
			connections: [],
			connectionTypes: []
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
		function(fieldFactory) {} // Called for configuration of `fieldFactory` (experimental)
	);
})(window.rgm.modes.ModelDesigner);
