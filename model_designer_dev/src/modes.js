(function(rns) {
	'use strict';
	if (typeof rns.rgm == 'undefined') rns.rgm = {};
	if (typeof rns.rgm.modes == 'undefined') rns.rgm.modes = {};
})(window);




(function(ns, rns) {
	'use strict';
	if (typeof ns.UniqueStringGenerator == 'undefined') {
		ns.UniqueStringGenerator = function() {
			this.prv = [{
				me: this,
				currentPrefix: ns.UniqueStringGenerator.prv.GENERAL_PREFIX,
				counter: -1
			}];
		};
		
		ns.UniqueStringGenerator.prototype.mine = function() { return this.prv[0]; };
		
		ns.UniqueStringGenerator.prototype.next = function() {
			var prv = this.mine();
			
			if (prv.counter + 1 > ns.UniqueStringGenerator.COUNTER_MAX) {
				prv.counter = 0;
				prv.currentPrefix += ns.UniqueStringGenerator.OVERFLOW_PREFIX;
			} else {
				++prv.counter;
			}
			
			return prv.currentPrefix + prv.counter;
		};
		
		ns.UniqueStringGenerator.prv = {
			GENERAL_PREFIX: 'u',
			OVERFLOW_PREFIX: 'x',
			COUNTER_MAX: 999999999,
			instance: null
		};
		
		ns.UniqueStringGenerator.getInstance = function() {
			if (ns.UniqueStringGenerator.prv.instance == null) {
				ns.UniqueStringGenerator.prv.instance = new ns.UniqueStringGenerator();
			}
			return ns.UniqueStringGenerator.prv.instance;
		};
	}
})(window.rgm.modes, window);




(function(ns, rns) {
	'use strict';
	if (typeof ns.MessageTemplate == 'undefined') {
		ns.MessageTemplate = function(parts) {
			this.prv = [{
				me: this,
				parts: parts
			}];
		};
		
		ns.MessageTemplate.prototype.mine = function() { return this.prv[0]; };
		
		ns.MessageTemplate.prototype.render = function(messageArgs) {
			var prv = this.mine();
			var result = '';
			for (var i = 0; i < prv.parts.length; ++i) {
				var part = prv.parts[i];
				if (i % 2 == 0) {
					result += part;
				} else {
					if (typeof messageArgs[part] != 'undefined') {
						result += messageArgs[part];
					}
				}
			}
			return result;
		};
	}
})(window.rgm.modes, window);




(function(ns, rns) {
	'use strict';
	if (typeof ns.NumberBound == 'undefined') {
		ns.NumberBound = function(reference, lowerBound, inclusive) {
			this.prv = [{
				me: this,
				
				reference: reference,
				lowerBound: lowerBound,
				inclusive: inclusive,
				
				correctedReference: (lowerBound ? 1 : (-1)) * reference,
				factor: lowerBound ? 1 : (-1),
				
				firstNumberLarger: function(first, second, allowWeaklyLarger) {
					return first > second || (allowWeaklyLarger && first == second);
				}
			}];
		};
		
		ns.NumberBound.prototype.mine = function() { return this.prv[0]; };
		
		ns.NumberBound.prototype.getReference = function() { return this.mine().reference; };
		
		ns.NumberBound.prototype.isLowerBound = function() { return this.mine().lowerBound; };
		
		ns.NumberBound.prototype.isInclusive = function() { return this.mine().inclusive; };
		
		ns.NumberBound.prototype.allows = function(value) {
			var prv = this.mine();
			return prv.firstNumberLarger(prv.factor * value, prv.correctedReference, prv.inclusive);
		};
	}
})(window.rgm.modes, window);




(function(ns, rns) {
	'use strict';
	if (typeof ns.NumberValidator == 'undefined') {
		ns.NumberValidator = function(decimals, min, max) {
			this.prv = [{
				me: this,
				decimals: decimals,
				min: min,
				max: max,
				
				wrongFormatTemplate: null,
				tooManyDecimalsTemplate: null,
				tooSmallTemplate: null,
				tooLargeTemplate: null,
				
				getBooleanAsYesOrNo: function(value) {
					return value ? ns.NumberValidator.prv.LABEL_YES : ns.NumberValidator.prv.LABEL_NO;
				},
				
				renderMessageWrongFormat: function(value) {
					var prv = this;
					if (prv.wrongFormatTemplate == null) {
						prv.wrongFormatTemplate = new ns.MessageTemplate(ns.NumberValidator.prv.TPL_WRONG_FORMAT.slice());
					}
					var messageArgs = {};
					messageArgs[ns.NumberValidator.prv.ARG_FOUND_VALUE] = value;
					return prv.wrongFormatTemplate.render(messageArgs);
				},
				
				renderMessageTooManyDecimals: function(decimalCount) {
					var prv = this;
					if (prv.tooManyDecimalsTemplate == null) {
						prv.tooManyDecimalsTemplate = new ns.MessageTemplate(ns.NumberValidator.prv.TPL_TOO_MANY_DECIMALS.slice());
					}
					var messageArgs = {};
					messageArgs[ns.NumberValidator.prv.ARG_FOUND_DECIMALS] = decimalCount;
					messageArgs[ns.NumberValidator.prv.ARG_MAX_DECIMALS] = prv.decimals;
					return prv.tooManyDecimalsTemplate.render(messageArgs);
				},
				
				renderRangeMessage: function(template, value, bound) {
					var prv = this;
					var messageArgs = {};
					messageArgs[ns.NumberValidator.prv.ARG_FOUND_VALUE] = value;
					messageArgs[ns.NumberValidator.prv.ARG_REFERENCE_VALUE] = bound.getReference();
					messageArgs[ns.NumberValidator.prv.INCLUSIVE_YES_OR_NO] = prv.getBooleanAsYesOrNo(bound.isInclusive());
					return template.render(messageArgs);
				},
				
				renderMessageTooSmall: function(value) {
					var prv = this;
					if (prv.tooSmallTemplate == null) {
						prv.tooSmallTemplate = new ns.MessageTemplate(ns.NumberValidator.prv.TPL_TOO_SMALL.slice());
					}
					return prv.renderRangeMessage(prv.tooSmallTemplate, value, prv.min);
				},
				
				renderMessageTooLarge: function(value) {
					var prv = this;
					if (prv.tooLargeTemplate == null) {
						prv.tooLargeTemplate = new ns.MessageTemplate(ns.NumberValidator.prv.TPL_TOO_LARGE.slice());
					}
					return prv.renderRangeMessage(prv.tooLargeTemplate, value, prv.max);
				}
			}];
		};
		
		ns.NumberValidator.prototype.mine = function() { return this.prv[0]; };
		
		ns.NumberValidator.prototype.check = function(numberStr) {
			var prv = this.mine();
			
			var groups = (new RegExp('^-?(0|[1-9][0-9]*)(\\.[0-9]+)?$')).exec(numberStr);
			var decimalsGroupIndex = 2;
			if (groups) {
				var foundDecimals = 0;
				if (groups[decimalsGroupIndex]) {
					foundDecimals = groups[decimalsGroupIndex].length - 1;
				}
				if (prv.decimals >= 0 && foundDecimals > prv.decimals) {
					return prv.renderMessageTooManyDecimals(foundDecimals);
				}
				
				var nr = Number.parseFloat(numberStr);
				
				if (prv.min != null && !prv.min.allows(nr)) {
					return prv.renderMessageTooSmall(numberStr);
				}
				if (prv.max != null && !prv.max.allows(nr)) {
					return prv.renderMessageTooLarge(numberStr);
				}
				
			} else {
				return prv.renderMessageWrongFormat(numberStr);
			}
		};
		
		ns.NumberValidator.prv = {
			TPL_WRONG_FORMAT: ['The value "', 'foundValue', '" is not a correctly formatted number.'],
			TPL_TOO_MANY_DECIMALS: ['This value has too many decimals. The maximum allowed is ', 'maxDecimals', '. ', 'foundDecimals', ' was/were found.'],
			TPL_TOO_SMALL: ['The value ', 'foundValue', ' is too small. The minimum value is ', 'referenceValue', ' (inclusive: ', 'inclusiveYesOrNo', ').'],
			TPL_TOO_LARGE: ['The value ', 'foundValue', ' is too large. The maximum value is ', 'referenceValue', ' (inclusive: ', 'inclusiveYesOrNo', ').'],
			ARG_MAX_DECIMALS: 'maxDecimals',
			ARG_FOUND_DECIMALS: 'foundDecimals',
			ARG_REFERENCE_VALUE: 'referenceValue',
			ARG_FOUND_VALUE: 'foundValue',
			INCLUSIVE_YES_OR_NO: 'inclusiveYesOrNo',
			LABEL_YES: 'yes',
			LABEL_NO: 'no'
		};
		
		ns.NumberValidator.newFromConfig = function(config) {
			var min = null;
			if (typeof config['min'] != 'undefined' && config.min != null) {
				min = new ns.NumberBound(config.min.value, true, config.min.inclusive);
			}
			
			var max = null;
			if (typeof config['max'] != 'undefined' && config.max != null) {
				max = new ns.NumberBound(config.max.value, false, config.max.inclusive);
			}
			
			return new ns.NumberValidator(config.decimals, min, max);
		};
	}
})(window.rgm.modes, window);




(function(ns, rns) {
	'use strict';
	if (typeof ns.MapFieldFactory == 'undefined') {
		ns.MapFieldFactory = function() {
			this.prv = [{
				me: this,
				typeToFactoryMap: {}
			}];
		};
		
		ns.MapFieldFactory.prototype.mine = function() { return this.prv[0]; };
		
		ns.MapFieldFactory.prototype.putFactory = function(fieldType, factory) {
			this.mine().typeToFactoryMap[fieldType] = factory;
		};
		
		ns.MapFieldFactory.prototype.newField = function(fieldType, fieldArgs, propName, label, valueData, dirty) {
			var prv = this.mine();
			if (typeof prv.typeToFactoryMap[fieldType] == 'undefined') {
				throw 'Unknown field type "' + fieldType + '" in MapFieldFactory.newField(...)';
			}
			return prv.typeToFactoryMap[fieldType].newField(fieldType, fieldArgs, propName, label, valueData, dirty);
		};
		
		ns.MapFieldFactory.prototype.newFieldFromDef = function(fieldDef) {
			return this.newField(fieldDef.fieldType, fieldDef.fieldArgs, fieldDef.propName, fieldDef.label, fieldDef.valueData, fieldDef.dirty);
		};
	}
})(window.rgm.modes, window);




(function(ns, rns) {
	'use strict';
	if (typeof ns.TextFieldFactory == 'undefined') {
		ns.TextFieldFactory = function() {
			this.prv = [{ me: this }];
		};
		
		ns.TextFieldFactory.prototype.mine = function() { return this.prv[0]; };
		
		ns.TextFieldFactory.prototype.newField = function(fieldType, fieldArgs, propName, label, valueData, dirty) {
			return new ns.TextField(fieldType, fieldArgs, propName, label, valueData, dirty);
		};
		
		ns.TextFieldFactory.prototype.newFieldFromDef = function(fieldDef) {
			return this.newField(fieldDef.fieldType, fieldDef.fieldArgs, fieldDef.propName, fieldDef.label, fieldDef.valueData, fieldDef.dirty);
		};
	}
})(window.rgm.modes, window);




(function(ns, rns) {
	'use strict';
	if (typeof ns.CheckboxFieldFactory == 'undefined') {
		ns.CheckboxFieldFactory = function() {
			this.prv = [{ me: this }];
		};
		
		ns.CheckboxFieldFactory.prototype.mine = function() { return this.prv[0]; };
		
		ns.CheckboxFieldFactory.prototype.newField = function(fieldType, fieldArgs, propName, label, valueData, dirty) {
			return new ns.CheckboxField(fieldType, fieldArgs, propName, label, valueData, dirty);
		};
		
		ns.CheckboxFieldFactory.prototype.newFieldFromDef = function(fieldDef) {
			return this.newField(fieldDef.fieldType, fieldDef.fieldArgs, fieldDef.propName, fieldDef.label, fieldDef.valueData, fieldDef.dirty);
		};
	}
})(window.rgm.modes, window);




(function(ns, rns) {
	'use strict';
	if (typeof ns.SubformsFieldFactory == 'undefined') {
		ns.SubformsFieldFactory = function(fieldFactory) {
			this.prv = [{
				me: this,
				fieldFactory: fieldFactory
			}];
		};
		
		ns.SubformsFieldFactory.prototype.mine = function() { return this.prv[0]; };
		
		ns.SubformsFieldFactory.prototype.newField = function(fieldType, fieldArgs, propName, label, valueData, dirty) {
			var prv = this.mine();
			return new ns.SubformsField(prv.fieldFactory, fieldType, fieldArgs, propName, label, valueData, dirty);
		};
		
		ns.SubformsFieldFactory.prototype.newFieldFromDef = function(fieldDef) {
			return this.newField(fieldDef.fieldType, fieldDef.fieldArgs, fieldDef.propName, fieldDef.label, fieldDef.valueData, fieldDef.dirty);
		};
	}
})(window.rgm.modes, window);




(function(ns, rns) {
	'use strict';
	if (typeof ns.TextField == 'undefined') {
		ns.TextField = function(fieldType, fieldArgs, propName, label, valueData, dirty) {
			this.prv = [{
				me: this,
				fieldType: fieldType,
				fieldArgs: fieldArgs,
				propName: propName,
				label: label,
				cleanValue: valueData,
				value: valueData,
				knownDirty: dirty,
				
				groupQ: null,
				componentQ: null,
				feedbackQ: null,
				
				numberValidator: null,
				
				getNumberValidator: function() {
					var prv = this;
					if (prv.fieldArgs.numberConfig == null) return null;
					if (prv.numberValidator == null) {
						prv.numberValidator = ns.NumberValidator.newFromConfig(prv.fieldArgs.numberConfig);
					}
					return prv.numberValidator;
				},
				
				checkNumber: function(numberStr) {
					var prv = this;
					var numberValidator = prv.getNumberValidator();
					return numberValidator == null ? null : numberValidator.check(numberStr);
				},
				
				getFeedbackClass: function(type) {
					return ns.TextField.prv.FEEDBACK_CLASS_START + type + ns.TextField.prv.FEEDBACK_CLASS_END;
				},
				
				removeFeedbackClasses: function(elemQ) {
					var prv = this;
					elemQ.removeClass(prv.getFeedbackClass(ns.TextField.prv.FEEDBACK_ERROR)).removeClass(prv.getFeedbackClass(ns.TextField.prv.FEEDBACK_WARNING)).removeClass(prv.getFeedbackClass(ns.TextField.prv.FEEDBACK_SUCCESS));
				},
				
				showFeedback: function(message, type) {
					var prv = this;
					if (prv.groupQ != null) {
						prv.removeFeedbackClasses(prv.groupQ);
						prv.groupQ.addClass(prv.getFeedbackClass(type));
						
						if (prv.feedbackQ == null) {
							prv.feedbackQ = jQuery('<span class="help-block"></span>');
							prv.groupQ.append(prv.feedbackQ);
						}
						prv.feedbackQ.text(message);
					}
				},
				
				showErrorFeedback: function(message) {
					this.showFeedback(message, ns.TextField.prv.FEEDBACK_TYPE_ERROR);
				},
				
				showWarningFeedback: function(message) {
					this.showFeedback(message, ns.TextField.prv.FEEDBACK_TYPE_WARNING);
				},
				
				showSuccessFeedback: function(message) {
					this.showFeedback(message, ns.TextField.prv.FEEDBACK_TYPE_SUCCESS);
				},
				
				removeFeedback: function() {
					var prv = this;
					if (prv.groupQ != null) {
						prv.removeFeedbackClasses(prv.groupQ);
						
						if (prv.feedbackQ != null) {
							prv.feedbackQ.remove();
							prv.feedbackQ = null;
						}
					}
				},
			}];
		};
		
		ns.TextField.prototype.mine = function() { return this.prv[0]; };
		
		ns.TextField.prototype.addToDocument = function(parentQ) {
			var prv = this.mine();
			var idAttrVal = ns.UniqueStringGenerator.getInstance().next();
			var groupQ = jQuery('<div class="form-group"></div>');
			var labelQ = jQuery('<label class="control-label"></label>')
				.attr('for', idAttrVal)
				.text(prv.label);
			var componentQ = prv.fieldArgs.displayAsTextArea
				? componentQ = jQuery('<textarea class="form-control"></textarea>')
				: componentQ = jQuery('<input type="text" class="form-control" />');
			componentQ
				.attr('id', idAttrVal)
				.val(prv.value);
			groupQ.append(labelQ);
			groupQ.append(componentQ);
			parentQ.append(groupQ);
			
			prv.groupQ = groupQ;
			prv.componentQ = componentQ;
		};
		
		ns.TextField.prototype.prepareRemoveFromDocument = function() {
			var prv = this.mine();
			prv.groupQ = null;
			prv.componentQ = null;
			prv.feedbackQ = null;
		};
		
		ns.TextField.prototype.synchronize = function() {
			var prv = this.mine();
			prv.value = prv.componentQ.val();
		};
		
		ns.TextField.prototype.asDataObject = function() {
			var prv = this.mine();
			var me = this;
			
			var data = {
				fieldType: prv.fieldType,
				fieldArgs: prv.fieldArgs,
				propName: prv.propName,
				label: prv.label,
				valueData: prv.value,
				dirty: me.isDirty()
			};
			return data;
		};
		
		ns.TextField.prototype.isDirty = function() {
			var prv = this.mine();
			return prv.knownDirty || prv.value != prv.cleanValue;
		};
		
		ns.TextField.prototype.setClean = function(idMap) {
			var prv = this.mine();
			prv.knownDirty = false;
			prv.cleanValue = prv.value;
		};
		
		ns.TextField.prototype.check = function() {
			var prv = this.mine();
			prv.removeFeedback();
			if (prv.fieldArgs.notEmpty && prv.value.length == 0) {
				var message = ns.TextField.prv.LABEL_NON_EMPTY;
				prv.showErrorFeedback(message);
				return message;
			}
			if (prv.fieldArgs.maxLength != -1 && prv.value.length > prv.fieldArgs.maxLength) {
				var message = ns.TextField.prv.LABEL_MAX_LENGTH_START + prv.fieldArgs.maxLength + ns.TextField.prv.LABEL_MAX_LENGTH_END;
				prv.showErrorFeedback(message);
				return message;
			}
			
			var numberErrorMessage = prv.checkNumber(prv.value);
			if (numberErrorMessage != null) {
				prv.showErrorFeedback(numberErrorMessage);
				return numberErrorMessage;
			}
			
			return null;
		};
		
		ns.TextField.prv = {
			LABEL_NON_EMPTY: 'This field can not be empty',
			LABEL_MAX_LENGTH_START: 'This field can contain no more than ',
			LABEL_MAX_LENGTH_END: ' characters.',
			FEEDBACK_TYPE_ERROR: 'error',
			FEEDBACK_TYPE_WARNING: 'warning',
			FEEDBACK_TYPE_SUCCESS: 'success',
			FEEDBACK_CLASS_START: 'has-',
			FEEDBACK_CLASS_END: ''
		};
		
		ns.TextField.TYPE_NAME = 'TEXT';
	}
})(window.rgm.modes, window);




(function(ns, rns) {
	'use strict';
	if (typeof ns.CheckboxField == 'undefined') {
		ns.CheckboxField = function(fieldType, fieldArgs, propName, label, valueData, dirty) {
			this.prv = [{
				me: this,
				fieldType: fieldType,
				fieldArgs: fieldArgs,
				propName: propName,
				label: label,
				cleanValue: valueData,
				value: valueData,
				knownDirty: dirty,
				
				componentQ: null,
				
				setCheckboxChecked: function(checkboxQ, checked) {
					checkboxQ.prop('checked', checked);
				},
				
				isCheckboxChecked: function(checkboxQ) {
					return checkboxQ.is(':checked');
				}
			}];
		};
		
		ns.CheckboxField.prototype.mine = function() {
			return this.prv[0];
		};
		
		ns.CheckboxField.prototype.addToDocument = function(parentQ) {
			var prv = this.mine();
			
			var containerQ = jQuery('<div class="form-group"></div>');
			parentQ.append(containerQ);
			
			var labelQ = jQuery('<label></label>').text(prv.label);
			containerQ.append(labelQ);
			
			prv.componentQ = jQuery('<input type="checkbox" />');
			containerQ.prepend(prv.componentQ);
			
			prv.setCheckboxChecked(prv.componentQ, prv.value);
		};
		
		ns.CheckboxField.prototype.prepareRemoveFromDocument = function() {
			var prv = this.mine();
			prv.componentQ = null;
		};
		
		ns.CheckboxField.prototype.synchronize = function() {
			var prv = this.mine();
			prv.value = prv.componentQ.is(':checked');
		};
		
		ns.CheckboxField.prototype.asDataObject = function() {
			var prv = this.mine();
			var me = this;
			
			var data = {
				fieldType: prv.fieldType,
				fieldArgs: prv.fieldArgs,
				propName: prv.propName,
				label: prv.label,
				valueData: prv.value,
				dirty: me.isDirty()
			};
			return data;
		};
		
		ns.CheckboxField.prototype.isDirty = function() {
			var prv = this.mine();
			return prv.knownDirty || prv.value != prv.cleanValue;
		};
		
		ns.CheckboxField.prototype.setClean = function(idMap) {
			var prv = this.mine();
			prv.knownDirty = false;
			prv.cleanValue = prv.value;
		};
		
		ns.CheckboxField.prototype.check = function() {
			return null;
		};
		
		ns.CheckboxField.TYPE_NAME = 'CHECK';
	}
})(window.rgm.modes, window);




(function(ns, rns) {
	'use strict';
	if (typeof ns.Subform == 'undefined') {
		ns.Subform = function(id, tempId, label, type, fields, position, titleTemplateParts, ownerField, dirty) {
			this.prv = [{
				me: this,
				id: id,
				tempId: tempId,
				label: label,
				type: type,
				fields: fields,
				position: position,
				titleTemplateParts: titleTemplateParts,
				ownerField: ownerField,
				knownDirty: dirty,
				
				titleTemplate: null,
				
				prevForm: null,
				nextForm: null,
				containerQ: null,
				titleQ: null,
				upButtonQ: null,
				downButtonQ: null,
				
				renderTitle: function(position, label) {
					var prv = this;
					
					if (prv.titleTemplate == null) {
						prv.titleTemplate = new ns.MessageTemplate(prv.titleTemplateParts);
					}
					var messageArgs = {};
					messageArgs[ns.Subform.prv.ARG_POSITION] = position;
					messageArgs[ns.Subform.prv.ARG_POSITION_ONE_BASED] = position + 1;
					messageArgs[ns.Subform.prv.ARG_LABEL] = label;
					return prv.titleTemplate.render(messageArgs);
				},
				
				getTitle: function() {
					var prv = this;
					return prv.renderTitle(prv.position, prv.label);
				},
				
				newContainerQ: function() {
					return jQuery('<div class="panel panel-default"></div>').addClass(ns.Subform.prv.CLASS_CONTAINER);
				},
				
				finishInsert: function() {
					var prv = this;
					var me = this.me;
					
					prv.titleQ = jQuery('<div class="panel-heading"></div>').addClass(ns.Subform.prv.CLASS_TITLE);
					prv.containerQ.append(prv.titleQ);
					
					var contentQ = jQuery('<div class="panel-body"></div>').addClass(ns.Subform.prv.CLASS_CONTENT);
					prv.containerQ.append(contentQ);
					
					var btnsQ = jQuery('<div class="btn-group"></div>').addClass(ns.Subform.prv.CLASS_BUTTONS);
					contentQ.append(btnsQ);
					
					var upQ = jQuery('<button class="btn btn-default"></button>').addClass(ns.Subform.prv.CLASS_UP_BUTTON).text(ns.Subform.prv.LABEL_UP_BUTTON);
					btnsQ.append(upQ);
					prv.upButtonQ = upQ;
					upQ.click(function() { prv.upButtonClicked(); });
					
					var downQ  = jQuery('<button class="btn btn-default"></button>').addClass(ns.Subform.prv.CLASS_DOWN_BUTTON).text(ns.Subform.prv.LABEL_DOWN_BUTTON);
					btnsQ.append(downQ);
					prv.downButtonQ = downQ;
					downQ.click(function() { prv.downButtonClicked(); });
					
					var removeQ = jQuery('<button class="btn btn-default"></button>').addClass(ns.Subform.prv.CLASS_REMOVE_BUTTON).text(ns.Subform.prv.LABEL_REMOVE_BUTTON);
					removeQ.click(function(eventData) { prv.removeButtonClicked(eventData); });
					btnsQ.append(removeQ);
					
					me.updateButtonStates();
					
					var fieldsQ = jQuery('<div></div>').addClass(ns.Subform.prv.CLASS_FIELDS);
					contentQ.append(fieldsQ);
					
					for (var i = 0; i < prv.fields.length; ++i) {
						prv.fields[i].addToDocument(fieldsQ);
					}
					
					me.updateTitleDisplay();
				},
				
				move: function(moveUp) {
					var prv = this;
					var me = this.me;
					
					if (moveUp) {
						if (prv.prevForm != null) {
							var other = prv.prevForm;
							var above = other.getPreviousForm();
							var below = prv.nextForm;
							
							var upperPosition = other.getPosition();
							var lowerPosition = prv.position;
							
							prv.containerQ.insertBefore(other.getContainerQ());
							
							me.setPreviousForm(above);
							me.setNextForm(other);
							me.setPosition(upperPosition);
							me.updateTitleDisplay();
							
							other.setPreviousForm(me);
							other.setNextForm(below);
							other.setPosition(lowerPosition);
							other.updateTitleDisplay();
							
							me.updateButtonStates();
							other.updateButtonStates();
							
							if (above != null) {
								above.setNextForm(me);
								above.updateButtonStates();
							}
							
							if (below != null) {
								below.setPreviousForm(other);
								below.updateButtonStates();
							}
							
							prv.ownerField.formsSwapped(upperPosition, lowerPosition);
						}
					} else {
						if (prv.nextForm != null) {
							var other = prv.nextForm;
							var above = prv.prevForm;
							var below = other.getNextForm();
							
							var upperPosition = prv.position;
							var lowerPosition = other.getPosition();
							
							prv.containerQ.insertAfter(other.getContainerQ());
							
							me.setPreviousForm(other);
							me.setNextForm(below);
							me.setPosition(lowerPosition);
							me.updateTitleDisplay();
							
							other.setPreviousForm(above);
							other.setNextForm(me);
							other.setPosition(upperPosition);
							other.updateTitleDisplay();
							
							me.updateButtonStates();
							other.updateButtonStates();
							
							if (above != null) {
								above.setNextForm(other);
								above.updateButtonStates();
							}
							
							if (below != null) {
								below.setPreviousForm(me);
								below.updateButtonStates();
							}
							
							prv.ownerField.formsSwapped(upperPosition, lowerPosition);
						}
					}
				},
				
				setButtonEnabled: function(btnQ, enabled) {
					if (enabled) {
						btnQ.removeClass('disabled');
					} else {
						btnQ.addClass('disabled');
					}
				},
				
				upButtonClicked: function() {
					this.move(true);
				},
				
				downButtonClicked: function() {
					this.move(false);
				},
				
				removeButtonClicked: function(eventData) {
					var prv = this;
					
					if (prv.prevForm != null) {
						prv.prevForm.setNextForm(prv.nextForm);
						prv.prevForm.updateButtonStates();
					}
					
					if (prv.nextForm != null) {
						prv.nextForm.setPreviousForm(prv.prevForm);
						prv.nextForm.updateThisAndSubsequent(-1, true, true);
					}
					
					prv.containerQ.remove();
					prv.ownerField.formRemoved(prv.position);
				}
			}]
		};
		
		ns.Subform.prototype.mine = function() { return this.prv[0]; };
		
		ns.Subform.prototype.setId = function(id) { this.mine().id = id; };
		
		ns.Subform.prototype.getId = function() { return this.mine().id; };
		
		ns.Subform.prototype.setTempId = function(tempId) { this.mine().tempId = tempId; };
		
		ns.Subform.prototype.getTempId = function() { return this.mine().tempId; };
		
		ns.Subform.prototype.getLabel = function() { return this.mine().label; };
		
		ns.Subform.prototype.setPosition = function(position) { this.mine().position = position; };
		
		ns.Subform.prototype.getPosition = function() { return this.mine().position; };
		
		ns.Subform.prototype.updateThisAndSubsequent = function(increase, updateTitleDisplay, updateButtonStates) {
			var prv = this.mine();
			var me = this;
			
			prv.position += increase;
			
			if (updateTitleDisplay) {
				me.updateTitleDisplay();
			}
			
			if (updateButtonStates) {
				me.updateButtonStates();
			}
			
			if (prv.nextForm != null) {
				prv.nextForm.updateThisAndSubsequent(increase, updateTitleDisplay, updateButtonStates);
			}
		};
		
		ns.Subform.prototype.getFields = function() { return this.mine().fields; };
		
		ns.Subform.prototype.setPreviousForm = function(prevForm) { this.mine().prevForm = prevForm; };
		
		ns.Subform.prototype.getPreviousForm = function() { return this.mine().prevForm; };
		
		ns.Subform.prototype.setNextForm = function(nextForm) { this.mine().nextForm = nextForm; };
		
		ns.Subform.prototype.getNextForm = function() { return this.mine().nextForm; };
		
		ns.Subform.prototype.updateTitleDisplay = function() {
			var prv = this.mine();
			prv.titleQ.text(prv.getTitle());
		};
		
		ns.Subform.prototype.getContainerQ = function() {
			return this.mine().containerQ;
		};
		
		ns.Subform.prototype.appendTo = function(parentQ) {
			var prv = this.mine();
			prv.containerQ = prv.newContainerQ();
			parentQ.append(prv.containerQ);
			prv.finishInsert();
		};
		
		ns.Subform.prototype.insertBefore = function(nextSiblingQ) {
			var prv = this.mine();
			prv.containerQ = prv.newContainerQ();
			prv.containerQ.insertBefore(nextSiblingQ);
			prv.finishInsert();
		};
		
		ns.Subform.prototype.insertAfter = function(prevSiblingQ) {
			var prv = this.mine();
			prv.containerQ = prv.newContainerQ();
			prv.containerQ.insertAfter(prevSiblingQ);
			prv.finishInsert();
		};
		
		ns.Subform.prototype.updateButtonStates = function() {
			var prv = this.mine();
			prv.setButtonEnabled(prv.upButtonQ, prv.prevForm != null);
			prv.setButtonEnabled(prv.downButtonQ, prv.nextForm != null);
		};
		
		ns.Subform.prototype.prepareRemoveFromDocument = function() {
			var prv = this.mine();
			prv.containerQ = null;
			prv.titleQ = null;
			prv.upButtonQ = null;
			prv.downButtonQ = null;
		};
		
		ns.Subform.prototype.synchronize = function() {
			var prv = this.mine();
			
			for (var i = 0; i < prv.fields.length; ++i) {
				var field = prv.fields[i];
				field.synchronize();
			}
		};
		
		ns.Subform.prototype.check = function() {
			var prv = this.mine();
			
			for (var i = 0; i < prv.fields.length; ++i) {
				var field = prv.fields[i];
				if (field.check() != null) {
					return ns.Subform.prv.LABEL_INVALID_FIELDS_MESSAGE;
				}
			}
			
			return null;
		};
		
		ns.Subform.prototype.isDirty = function() {
			var prv = this.mine();
			
			if (prv.knownDirty) return true;
			
			for (var i = 0; i < prv.fields.length; ++i) {
				var field = prv.fields[i];
				if (field.isDirty()) {
					return true;
				}
			}
			
			return false;
		};
		
		ns.Subform.prototype.setClean = function(idMap) {
			var prv = this.mine();
			
			for (var i = 0; i < prv.fields.length; ++i) {
				var field = prv.fields[i];
				field.setClean(idMap);
			}
			
			if (prv.id == null && prv.tempId != null && typeof idMap[prv.tempId] != 'undefined') {
				prv.id = idMap[prv.tempId];
				prv.tempId = null;
			}
			
			prv.knownDirty = false;
		};
		
		ns.Subform.prototype.asDataObject = function() {
			var prv = this.mine();
			var me = this;
			
			var data = {
				id: prv.id,
				tempId: prv.tempId,
				label: prv.label,
				type: prv.type,
				titleTemplate: prv.titleTemplateParts.slice(),
				dirty: me.isDirty(),
				fields: []
			};
			
			for (var i = 0; i < prv.fields.length; ++i) {
				var field = prv.fields[i];
				data.fields.push(field.asDataObject());
			}
			
			return data;
		};
		
		ns.Subform.prv = {
			CLASS_CONTAINER: 'rgm-modes-subform-container',
			CLASS_TITLE: 'rgm-modes-subform-title',
			CLASS_CONTENT: 'rgm-modes-subform-content',
			CLASS_BUTTONS: 'rgm-modes-subform-btns',
			CLASS_MOVE_BUTTON: 'rgm-modes-subform-move-btn',
			CLASS_UP_BUTTON: 'rgm-modes-subform-up-btn',
			CLASS_DOWN_BUTTON: 'rgm-modes-subform-down-btn',
			CLASS_REMOVE_BUTTON: 'rgm-modes-subform-remove-btn',
			CLASS_FIELDS: 'rgm-modes-subform-fields',
			LABEL_UP_BUTTON: '\u25B2',
			LABEL_DOWN_BUTTON: '\u25BC',
			LABEL_REMOVE_BUTTON: '\uD83D\uDDD1',
			LABEL_INVALID_FIELDS_MESSAGE: 'There are invalid fields.',
			TEMP_ID_PREFIX: 'temp_subform',
			TEMP_ID_SEPARATOR: '_',
			ARG_POSITION: 'position',
			ARG_POSITION_ONE_BASED: 'positionOneBased',
			ARG_LABEL: 'label'
		};
		
		ns.Subform.newTempId = function() {
			return [ns.Subform.prv.TEMP_ID_PREFIX, (new Date()).getTime(), ns.UniqueStringGenerator.getInstance().next()].join(ns.Subform.prv.TEMP_ID_SEPARATOR);
		};
	}

})(window.rgm.modes, window);




(function(ns, rns) {
	'use strict';
	if (typeof ns.SubformsField == 'undefined') {
		ns.SubformsField = function(fieldFactory, fieldType, fieldArgs, propName, label, valueData, dirty) {
			this.prv = [{
				me: this,
				fieldFactory: fieldFactory,
				fieldType: fieldType,
				fieldArgs: fieldArgs,
				propName: propName,
				label: label,
				formDefs: valueData,
				knownDirty: dirty,
				
				feedbackContainerQ: null,
				feedbackQs: [],
				formsQ: null,
				addButtonQs: [],
				
				forms: [],
				formByTempId: {},
				
				initFormPositions: [],
				initFormCount: -1,
				
				tooFewFormsTemplate: null,
				tooManyFormsTemplate: null,
				
				init: function() {
					var prv = this;
					var me = this.me;
					
					var prevForm = null;
					for (var i = 0; i < prv.formDefs.length; ++i) {
						var formDef = prv.formDefs[i];
						
						var fields = [];
						for (var j = 0; j < formDef.fields.length; ++j) {
							var fieldDef = formDef.fields[j];
							var field = prv.fieldFactory.newFieldFromDef(fieldDef);
							fields.push(field);
						}
						
						var form = new ns.Subform(formDef.id, formDef.tempId, formDef.label, formDef.type, fields, i, formDef.titleTemplate, me, formDef.dirty);
						
						if (i > 0) {
							form.setPreviousForm(prevForm);
							prevForm.setNextForm(form);
						}
						
						prv.initFormPositions.push(i);
						prv.forms.push(form);
						prevForm = form;
					}
					
					prv.initFormCount = prv.forms.length;
				},
				
				addFeedback: function(message, typeClassSuffix) {
					var prv = this;
					
					var feedbackQ = jQuery('<div class="alert"></div>').addClass('alert-' + typeClassSuffix).text(message);
					prv.feedbackContainerQ.append(feedbackQ);
					prv.feedbackQs.push(feedbackQ);
				},
				
				addDangerFeedback: function(message) {
					var prv = this;
					prv.addFeedback(message, ns.SubformsField.prv.CLASS_SUFFIX_DANGER);
				},
				
				clearFeedback: function() {
					var prv = this;
					for (var i = 0; i < prv.feedbackQs.length; ++i) {
						var feedbackQ = prv.feedbackQs[i];
						feedbackQ.remove();
					}
				},
				
				renderTooFewFormsMessage: function(bound, actual) {
					var prv = this;
					if (prv.tooFewFormsTemplate == null) {
						prv.tooFewFormsTemplate = new ns.MessageTemplate(ns.SubformsField.prv.TPL_TOO_FEW_FORMS);
					}
					var msgArgs = {};
					msgArgs[ns.SubformsField.prv.ARG_BOUND] = bound;
					msgArgs[ns.SubformsField.prv.ARG_ACTUAL] = actual;
					return prv.tooFewFormsTemplate.render(msgArgs);
				},
				
				renderTooManyFormsMessage: function(bound, actual) {
					var prv = this;
					if (prv.tooManyFormsTemplate == null) {
						prv.tooManyFormsTemplate = new ns.MessageTemplate(ns.SubformsField.prv.TPL_TOO_MANY_FORMS);
					}
					var msgArgs = {};
					msgArgs[ns.SubformsField.prv.ARG_BOUND] = bound;
					msgArgs[ns.SubformsField.prv.ARG_ACTUAL] = actual;
					return prv.tooManyFormsTemplate.render(msgArgs);
				},
				
				addButtonClicked: function(formDef) {
					var prv = this;
					var me = this.me;
					
					if (prv.fieldArgs.maxForms == -1 || prv.forms.length < prv.fieldArgs.maxForms) {
						var tempId = ns.Subform.newTempId();
					
						var fields = [];
						for (var i = 0; i < formDef.fields.length; ++i) {
							var fieldDef = formDef.fields[i];
							var field = prv.fieldFactory.newFieldFromDef(fieldDef);
							fields.push(field);
						}
					
						var form = new ns.Subform(formDef.id, tempId, formDef.label, formDef.type, fields, prv.forms.length, formDef.titleTemplate, me, formDef.dirty);
					
						if (prv.forms.length > 0) {
							var prevForm = prv.forms[prv.forms.length - 1];
							prevForm.setNextForm(form);
							prevForm.updateButtonStates();
							form.setPreviousForm(prevForm);
						}
					
						form.appendTo(prv.formsQ);
					
						prv.initFormPositions.push(-1);
						prv.forms.push(form);
						prv.formByTempId[tempId] = form;
					
						prv.updateAddButtonStates();
					}
				},
				
				updateAddButtonStates: function() {
					var prv = this;
					var maxReached = prv.fieldArgs.maxForms != -1 && prv.forms.length >= prv.fieldArgs.maxForms;
					for (var i = 0; i < prv.addButtonQs.length; ++i) {
						var addButtonQ = prv.addButtonQs[i];
						if (maxReached) {
							addButtonQ.addClass('disabled');
						} else {
							addButtonQ.removeClass('disabled');
						}
					}
				}
			}];
			this.prv[0].init();
		};
		
		ns.SubformsField.prototype.mine = function() { return this.prv[0]; };
		
		ns.SubformsField.prototype.formsSwapped = function(upperPosition, lowerPosition) {
			var prv = this.mine();
			
			var temp = prv.forms[upperPosition];
			prv.forms[upperPosition] = prv.forms[lowerPosition];
			prv.forms[lowerPosition] = temp;
			
			var tempPosition = prv.initFormPositions[upperPosition];
			prv.initFormPositions[upperPosition] = prv.initFormPositions[lowerPosition];
			prv.initFormPositions[lowerPosition] = tempPosition;
		};
		
		ns.SubformsField.prototype.formRemoved = function(removedPosition) {
			var prv = this.mine();
			prv.forms.splice(removedPosition, 1);
			prv.initFormPositions.splice(removedPosition, 1);
			prv.updateAddButtonStates();
		};
		
		ns.SubformsField.prototype.addToDocument = function(parentQ) {
			var prv = this.mine();
			var i = 0;
			
			var containerQ = jQuery('<div class="panel panel-default"></div>').addClass(ns.SubformsField.prv.CLASS_CONTAINER);
			parentQ.append(containerQ);
			
			var titleQ = jQuery('<div class="panel-heading"></div>').addClass(ns.SubformsField.prv.CLASS_TITLE);
			titleQ.text(prv.label);
			containerQ.append(titleQ);
			
			var contentQ = jQuery('<div class="panel-body"></div>').addClass(ns.SubformsField.prv.CLASS_CONTENT);
			containerQ.append(contentQ);
			
			prv.feedbackContainerQ = jQuery('<div></div>').addClass(ns.SubformsField.prv.CLASS_FEEDBACK_CONTAINER);
			contentQ.append(prv.feedbackContainerQ);
			
			var addBtnsQ = jQuery('<div class="btn-group-vertical"></div>').addClass(ns.SubformsField.prv.CLASS_ADD_BUTTONS);
			contentQ.append(addBtnsQ);
			
			for (i = 0; i < prv.fieldArgs.forms.length; ++i) {(function(i) {
				var formDef = prv.fieldArgs.forms[i];
				
				var addBtnQ = jQuery('<button class="btn btn-default"></button>').addClass(ns.SubformsField.prv.CLASS_ADD_BUTTON).text(ns.SubformsField.prv.LABEL_ADD_BUTTON_START + formDef.label + ns.SubformsField.prv.LABEL_ADD_BUTTON_END);
				addBtnQ.click(function() { prv.addButtonClicked(formDef); });
				addBtnsQ.append(addBtnQ);
				prv.addButtonQs.push(addBtnQ);
			})(i);}
			
			var formsQ = jQuery('<div></div>').addClass(ns.SubformsField.prv.CLASS_FORMS);
			contentQ.append(formsQ);
			
			for (i = 0; i < prv.forms.length; ++i) {
				var form = prv.forms[i];
				form.appendTo(formsQ);
			}
			
			prv.formsQ = formsQ;
			prv.updateAddButtonStates();
		};
		
		ns.SubformsField.prototype.prepareRemoveFromDocument = function() {
			var prv = this.mine();
			prv.feedbackContainerQ = null;
			prv.feedbackQs = [];
			prv.formsQ = null;
			prv.addButtonQs = [];
			for (var i = 0; i < prv.forms.length; ++i) {
				var form = prv.forms[i];
				form.prepareRemoveFromDocument();
			}
		};
		
		ns.SubformsField.prototype.synchronize = function() {
			var prv = this.mine();
			for (var i = 0; i < prv.forms.length; ++i) {
				var form = prv.forms[i];
				form.synchronize();
			}
		};
		
		ns.SubformsField.prototype.asDataObject = function() {
			var prv = this.mine()
			var me = this;
			
			var data = {
				fieldType: prv.fieldType,
				fieldArgs: prv.fieldArgs,
				propName: prv.propName,
				label: prv.label,
				valueData: prv.value,
				dirty: me.isDirty(),
				valueData: []
			};
			
			for (var i = 0; i < prv.forms.length; ++i) {
				var form = prv.forms[i];
				data.valueData.push(form.asDataObject());
			}
			
			return data;
		};
		
		ns.SubformsField.prototype.isDirty = function() {
			var prv = this.mine();
			var i = 0;
			
			if (prv.knownDirty || prv.forms.length != prv.initFormCount) {
				return true;
			}
			
			var prevPosition = -1;
			for (i = 0; i < prv.initFormPositions.length; ++i) {
				var position = prv.initFormPositions[i];
				if (position != prevPosition + 1) {
					return true;
				}
				prevPosition = position;
			}
			
			for (i = 0; i < prv.forms.length; ++i) {
				var form = prv.forms[i];
				if (form.isDirty()) {
					return true;
				}
			}
			
			return false;
		};
		
		ns.SubformsField.prototype.setClean = function(idMap) {
			var prv = this.mine();
			var i = 0;
			
			prv.initFormCount = prv.forms.length;
			
			prv.initFormPositions = [];
			for (i = 0; i < prv.forms.length; ++i) {
				prv.initFormPositions.push(i);
			}
			
			prv.knownDirty = false;
			
			for (i = 0; i < prv.forms.length; ++i) {
				var form = prv.forms[i];
				form.setClean(idMap);
			}
		};
		
		ns.SubformsField.prototype.check = function() {
			var prv = this.mine();
			
			prv.clearFeedback();
			
			var minForms = prv.fieldArgs.minForms;
			var maxForms = prv.fieldArgs.maxForms;
			var formCount = prv.forms.length;
			
			if (minForms != -1 && formCount < minForms) {
				var boundMessage = prv.renderTooFewFormsMessage(minForms, formCount);
				prv.addDangerFeedback(boundMessage);
				return boundMessage;
			}
			
			if (maxForms != -1 && formCount > maxForms) {
				var boundMessage = prv.renderTooFewFormsMessage(maxForms, formCount);
				prv.addDangerFeedback(boundMessage);
				return boundMessage;
			}
			
			for (var i = 0; i < prv.forms.length; ++i) {
				var form = prv.forms[i];
				var formInvalidMessage = form.check();
				if (formInvalidMessage != null) {
					return ns.SubformsField.prv.LABEL_INVALID_FORMS_MESSAGE;
				}
			}
			
			return null;
		};
		
		ns.SubformsField.prv = {
			CLASS_CONTAINER: 'rgm-modes-forms-field-container',
			ClASS_TITLE: 'rgm-modes-forms-field-title',
			CLASS_FEEDBACK_CONTAINER: 'rgm-modes-forms-field-feedback-container',
			CLASS_CONTENT: 'rgm-modes-forms-field-content',
			CLASS_ADD_BUTTONS: 'rgm-modes-forms-field-add-buttons',
			CLASS_ADD_BUTTON: 'rgm-modes-forms-field-add-button',
			CLASS_FORMS: 'rgm-modes-forms-field-forms',
			CLASS_SUFFIX_DANGER: 'danger',
			TPL_TOO_FEW_FORMS: ['There are not enough forms (', 'actual', '): this field expects at least ', 'bound', ' form(s).'],
			TPL_TOO_MANY_FORMS: ['There are too many forms (', 'actual', '): this field allows no more than ', 'bound', ' form(s).'],
			ARG_BOUND: 'bound',
			ARG_ACTUAL: 'actual',
			LABEL_ADD_BUTTON_START: 'Add ',
			LABEL_ADD_BUTTON_END: '',
			LABEL_INVALID_FORMS_MESSAGE: 'There are invalid forms.'
		};
		
		ns.SubformsField.TYPE_NAME = 'FORMS';
	}
})(window.rgm.modes, window);




(function(ns, rns) {
	'use strict';
	
	if (typeof ns.Node == 'undefined') {
		ns.Node = function(nodeData, nodeIdentifier, fieldFactory, modelDesigner, connectionTypeDefs) {
			this.prv = [{
				me: this,
				nodeData: nodeData,
				nodeIdentifier: nodeIdentifier,
				fieldFactory: fieldFactory,
				modelDesigner: modelDesigner,
				connectionTypeDefs: connectionTypeDefs,
				
				connectionTypeDefByName: null,
				
				outConnections: [],
				outConnectionsByTargetIdentifier: {},
				inConnections: [],
				
				initX: -1,
				initY: -1,
				initConnectionHash: null,
				
				containerQ: null,
				titleQ: null,
				
				fields: [],
				fieldByPropName: {},
				
				jsPlumbInstance: null,
				
				modalTitleTemplate: null,
				extendedTitleTemplate: null,
				maxOutgoingExceededTemplate: null,
				confirmDeleteTemplate: null,
				nodeContextInfoTemplate: null,
				configureButtonContextInfoTemplate: null,
				deleteButtonContextInfoTemplate: null,
				sourceEndpointContextInfoTemplate: null,
				tooFewInConnctionsTemplate: null,
				tooManyInConnectionsTemplate: null,
				tooFewOutConnctionsTemplate: null,
				tooManyOutConnectionsTemplate: null,
				
				visitMark: 0,
				
				getConnectionTypeDef: function(connectionTypeName) {
					var prv = this;
					if (prv.connectionTypeDefByName == null) {
						prv.connectionTypeDefByName = {};
						for (var i = 0; i < prv.connectionTypeDefs.length; ++i) {
							var connectionTypeDef = prv.connectionTypeDefs[i];
							prv.connectionTypeDefByName[connectionTypeDef.typeName] = connectionTypeDef;
						}
					}
					return prv.connectionTypeDefByName[connectionTypeName];
				},
				
				renderModalTitle: function(titleLabel, extendedTitle) {
					var prv = this;
					if (prv.modalTitleTemplate == null) {
						prv.modalTitleTemplate = new ns.MessageTemplate(ns.Node.prv.TPL_MODAL_TITLE);
					}
					var msgArgs ={};
					msgArgs[ns.Node.prv.ARG_TITLE_LABEL] = titleLabel;
					msgArgs[ns.Node.prv.ARG_EXTENDED_TITLE] = extendedTitle;
					return prv.modalTitleTemplate.render(msgArgs);
				},
				
				renderConfirmDeleteMessage: function(titleLabel, extendedTitle) {
					var prv = this;
					if (prv.confirmDeleteTemplate == null) {
						prv.confirmDeleteTemplate = new ns.MessageTemplate(ns.Node.prv.TPL_CONFIRM_DELETE);
					}
					var msgArgs ={};
					msgArgs[ns.Node.prv.ARG_TITLE_LABEL] = titleLabel;
					msgArgs[ns.Node.prv.ARG_EXTENDED_TITLE] = extendedTitle;
					return prv.confirmDeleteTemplate.render(msgArgs);
				},
				
				renderNodeContextInfo: function(titleLabel, extendedTitle, typeLabel) {
					var prv = this;
					if (prv.nodeContextInfoTemplate == null) {
						prv.nodeContextInfoTemplate = new ns.MessageTemplate(ns.Node.prv.TPL_NODE_CONTEXT_INFO);
					}
					var msgArgs ={};
					msgArgs[ns.Node.prv.ARG_TITLE_LABEL] = titleLabel;
					msgArgs[ns.Node.prv.ARG_EXTENDED_TITLE] = extendedTitle;
					msgArgs[ns.Node.prv.ARG_TYPE_LABEL] = typeLabel;
					return prv.nodeContextInfoTemplate.render(msgArgs);
				},
				
				renderConfigureButtonContextInfo: function(titleLabel, extendedTitle, typeLabel) {
					var prv = this;
					if (prv.configureButtonContextInfoTemplate == null) {
						prv.configureButtonContextInfoTemplate = new ns.MessageTemplate(ns.Node.prv.TPL_CONFIGURE_BUTTON_CONTEXT_INFO);
					}
					var msgArgs ={};
					msgArgs[ns.Node.prv.ARG_TITLE_LABEL] = titleLabel;
					msgArgs[ns.Node.prv.ARG_EXTENDED_TITLE] = extendedTitle;
					msgArgs[ns.Node.prv.ARG_TYPE_LABEL] = typeLabel;
					return prv.configureButtonContextInfoTemplate.render(msgArgs);
				},
				
				renderDeleteButtonContextInfo: function(titleLabel, extendedTitle, typeLabel) {
					var prv = this;
					if (prv.deleteButtonContextInfoTemplate == null) {
						prv.deleteButtonContextInfoTemplate = new ns.MessageTemplate(ns.Node.prv.TPL_DELETE_BUTTON_CONTEXT_INFO);
					}
					var msgArgs ={};
					msgArgs[ns.Node.prv.ARG_TITLE_LABEL] = titleLabel;
					msgArgs[ns.Node.prv.ARG_EXTENDED_TITLE] = extendedTitle;
					msgArgs[ns.Node.prv.ARG_TYPE_LABEL] = typeLabel;
					return prv.deleteButtonContextInfoTemplate.render(msgArgs);
				},
				
				renderExtendedTitle: function(titleLabel, idTypeLabel, idOrTempId, beforeTitleLabel, afterTitleLabel) {
					var prv = this;
					if (prv.extendedTitleTemplate == null) {
						prv.extendedTitleTemplate = new ns.MessageTemplate(ns.Node.prv.TPL_EXTENDED_TITLE);
					}
					var msgArgs ={};
					msgArgs[ns.Node.prv.ARG_TITLE_LABEL] = titleLabel;
					msgArgs[ns.Node.prv.ARG_ID_TYPE_LABEL] = idTypeLabel;
					msgArgs[ns.Node.prv.ARG_ID_OR_TEMP_ID] = idOrTempId;
					msgArgs[ns.Node.prv.ARG_BEFORE_TITLE_LABEL] = beforeTitleLabel;
					msgArgs[ns.Node.prv.ARG_AFTER_TITLE_LABEL] = afterTitleLabel;
					return prv.extendedTitleTemplate.render(msgArgs);
				},
				
				getConnectionCountViolationTemplate: function(forIn, tooFew) {
					var prv = this;
					if (forIn) {
						if (tooFew) {
							if (prv.tooFewInConnctionsTemplate == null) {
								prv.tooFewInConnctionsTemplate = new ns.MessageTemplate(ns.Node.prv.TPL_TOO_FEW_IN_CONNECTIONS);
							}
							return prv.tooFewInConnctionsTemplate;
						} else {
							if (prv.tooManyInConnctionsTemplate == null) {
								prv.tooManyInConnctionsTemplate = new ns.MessageTemplate(ns.Node.prv.TPL_TOO_MANY_IN_CONNECTIONS);
							}
							return prv.tooManyInConnctionsTemplate;
						}
					} else {
						if (tooFew) {
							if (prv.tooFewOutConnctionsTemplate == null) {
								prv.tooFewOutConnctionsTemplate = new ns.MessageTemplate(ns.Node.prv.TPL_TOO_FEW_OUT_CONNECTIONS);
							}
							return prv.tooFewOutConnctionsTemplate;
						} else {
							if (prv.tooManyOutConnctionsTemplate == null) {
								prv.tooManyOutConnctionsTemplate = new ns.MessageTemplate(ns.Node.prv.TPL_TOO_MANY_OUT_CONNECTIONS);
							}
							return prv.tooManyOutConnctionsTemplate;
						}
					}
				},
				
				renderConnctionCountViolationMessage: function(forIn, tooFew, bound, extendedTitle) {
					var prv = this;
					var template = prv.getConnectionCountViolationTemplate(forIn, tooFew);
					var msgArgs = {};
					msgArgs[ns.Node.prv.ARG_BOUND] = bound;
					msgArgs[ns.Node.prv.ARG_EXTENDED_TITLE] = extendedTitle;
					return template.render(msgArgs);
				},
				
				getSingleConnectionHash: function(forInConnection, connection) {
					var typeName = connection.getTypeName();
					var endIdentifier = forInConnection ? connection.getSourceNode().getNodeIdentifier() : connection.getTargetNode().getNodeIdentifier();
					return [
						forInConnection ? '1' : '0',
						typeName.length,
						endIdentifier.length,
						typeName,
						endIdentifier
					].join('_');
				},
				
				getConnectionHash: function() {
					var prv = this;
					var i = 0;
					
					var singleHashes = [];
					for (i = 0; i < prv.inConnections.length; ++i) {
						var connection = prv.inConnections[i];
						singleHashes.push(prv.getSingleConnectionHash(true, connection));
					}
					for (i = 0; i < prv.outConnections.length; ++i) {
						var connection = prv.outConnections[i];
						singleHashes.push(prv.getSingleConnectionHash(false, connection));
					}
					singleHashes.sort();
					
					var hashParts = [];
					for (i = 0; i < singleHashes.length; ++i) {
						var singleHash = singleHashes[i];
						hashParts.push(singleHash.length);
						hashParts.push(singleHash);
					}
					
					return hashParts.join('_');
				},
				
				getIdTypeLabel: function() {
					var prv = this;
					return prv.nodeData.id != null ? ns.Node.prv.LABEL_ID : ns.Node.prv.LABEL_TEMP_ID;
				},
				
				getIdOrTempId: function() {
					var prv = this;
					return prv.nodeData.id != null ? prv.nodeData.id : prv.nodeData.tempId;
				},
				
				getFieldDataForPath: function(path, alt) {
					var prv = this;
					if (path == null) return alt;
					var field = prv.getField(path[0], null);
					if (field == null) return alt;
					var cur = field.asDataObject();
					for (var i = 1; i < path.length; ++i) {
						var segment = path[i];
						if (typeof cur[segment] == 'undefined') {
							return alt;
						}
						cur = cur[segment];
					}
					return cur;
				},
				
				updateTitleDisplay: function() {
					var prv = this;
					var me = this.me;
					
					prv.titleQ.text(me.getTitleLabel());
				},
				
				setAbsolutePosition: function(elemQ, x, y) {
					elemQ.css({ top: y + 'px', left: x + 'px' });
				},
				
				getAbsolutePosition: function(elemQ) {
					var elemPosition = elemQ.position();
					return { top: elemPosition.top, left: elemPosition.left };
				},
				
				addClasses: function(elemQ, classArr) {
					for (var i = 0; i < classArr.length; ++i) {
						elemQ.addClass(classArr[i]);
					}
				},
				
				putField: function(propName, field) {
					var prv = this;
					prv.fieldByPropName['pn' + propName] = field;
				},
				
				getField: function(propName, alt) {
					var prv = this;
					var key = 'pn' + propName;
					if (typeof prv.fieldByPropName[key] == 'undefined') return alt;
					return prv.fieldByPropName[key];
				},
				
				configureButtonClicked: function() {
					var prv = this;
					var me = this.me;
					
					prv.modelDesigner.showModal(
						function(modalQ, modalTitleQ, modalBodyQ, modalFooterQ, modalOkButtonQ) {
							for (var i = 0; i < prv.fields.length; ++i) {
								var field = prv.fields[i];
								field.addToDocument(modalBodyQ);
							}
							modalTitleQ.text(prv.renderModalTitle(me.getTitleLabel(), me.getExtendedTitleQuoted()));
							modalOkButtonQ.text(ns.Node.prv.LABEL_OK_BUTTON);
						},
						function() { return prv.modalOkButtonClicked(); }
					);
				},
				
				deleteButtonClicked: function() {
					var prv = this;
					var me = this.me;
					
					if (confirm(prv.renderConfirmDeleteMessage(me.getTitleLabel(), me.getExtendedTitleQuoted()))) {
						prv.modelDesigner.removeNode(me, true);
						prv.containerQ.remove();
					}
				},
				
				modalOkButtonClicked: function() {
					var prv = this;
					var i = 0;
					
					for (i = 0; i < prv.fields.length; ++i) {
						var field = prv.fields[i];
						field.synchronize();
						if (field.check() != null) {
							return false;
						}
					}
					
					for (i = 0; i < prv.fields.length; ++i) {
						var field = prv.fields[i];
						field.prepareRemoveFromDocument();
					}
					
					prv.updateTitleDisplay();
					return true;
				},
				
				onMaxConnections: function() {
					var prv = this;
					var me = this.me;
					
					if (prv.maxOutgoingExceededTemplate == null) {
						prv.maxOutgoingExceededTemplate = new ns.MessageTemplate(ns.Node.prv.TPL_MAX_CONNECTIONS_EXCEEDED);
					}
					var msgArgs ={};
					msgArgs[ns.Node.prv.ARG_EXTENDED_TITLE] = me.getExtendedTitleQuoted();
					msgArgs[ns.Node.prv.ARG_MAX_OUTGOING] = prv.nodeData.maxOutgoing;
					
					alert(prv.maxOutgoingExceededTemplate.render(msgArgs));
				},
				
				mouseOverContainer: function(eventData) {
					var prv = this;
					var me = this.me;
					prv.modelDesigner.showContextInfo(prv.renderNodeContextInfo(me.getTitleLabel(), me.getExtendedTitleNotQuoted(), prv.nodeData.typeLabel));
				},
				
				mouseLeftContainer: function(eventData) {
					var prv = this;
					prv.modelDesigner.hideContextInfo();
				},
				
				addMouseOverListenerToSourceEp: function(sourceEpQ, connectionTypeName, connectionTypeLabel) {
					var prv = this;
					sourceEpQ.mouseover(function(eventData) { prv.mouseOverSourceEndpoint(eventData, connectionTypeName, connectionTypeLabel); });
				},
				
				addMouseOutListenerToSourceEp: function(sourceEpQ) {
					var prv = this;
					sourceEpQ.mouseout(function(eventData) { prv.mouseLeftSourceEndpoint(eventData); });
				},
				
				mouseOverSourceEndpoint: function(eventData, connectionTypeName, connectionTypeLabel) {
					var prv = this;
					eventData.stopPropagation();
					if (prv.sourceEndpointContextInfoTemplate == null) {
						prv.sourceEndpointContextInfoTemplate = new ns.MessageTemplate(ns.Node.prv.TPL_SOURCE_ENDPOINT_CONTEXT_INFO);
					}
					var msgArgs ={};
					msgArgs[ns.Node.prv.ARG_CONNECTION_TYPE_LABEL] = connectionTypeLabel;
					var contextInfo = prv.sourceEndpointContextInfoTemplate.render(msgArgs);
					prv.modelDesigner.showContextInfo(contextInfo);
					
				},
				
				mouseLeftSourceEndpoint: function(eventData) {
					var prv = this;
					prv.modelDesigner.hideContextInfo();
				},
				
				mouseOverConfigureButton: function(eventData) {
					var prv = this;
					var me = this.me;
					eventData.stopPropagation();
					prv.modelDesigner.showContextInfo(prv.renderConfigureButtonContextInfo(me.getTitleLabel(), me.getExtendedTitleQuoted(), prv.nodeData.typeLabel));
				},
				
				mouseLeftConfigureButton: function(eventData) {
					var prv = this;
					prv.modelDesigner.hideContextInfo();
				},
				
				mouseOverDeleteButton: function(eventData) {
					var prv = this;
					var me = this.me;
					eventData.stopPropagation();
					prv.modelDesigner.showContextInfo(prv.renderDeleteButtonContextInfo(me.getTitleLabel(), me.getExtendedTitleQuoted(), prv.nodeData.typeLabel));
				},
				
				mouseLeftDeleteButton: function(eventData) {
					var prv = this;
					prv.modelDesigner.hideContextInfo();
				}
			}];
		};
		
		ns.Node.prototype.mine = function() {
			return this.prv[0];
		};
		
		ns.Node.prototype.setId = function(id) { this.mine().nodeData.id = id; };
		
		ns.Node.prototype.getId = function() { return this.mine().nodeData.id; };
		
		ns.Node.prototype.setTempId = function(tempId) { this.mine().nodeData.tempId = tempId; };
		
		ns.Node.prototype.getTempId = function() { return this.mine().nodeData.tempId; };
		
		ns.Node.prototype.getNodeIdentifier = function() { return this.mine().nodeIdentifier; };
		
		ns.Node.prototype.getTypeLabel = function() { return this.mine().nodeData.typeLabel; };
		
		ns.Node.prototype.getContainerQ = function() { return this.mine().containerQ; };
		
		ns.Node.prototype.getVisitMark = function() { return this.mine().visitMark; };
		
		ns.Node.prototype.setVisitMark = function(visitMark) { this.mine().visitMark = visitMark; };
		
		ns.Node.prototype.getTitleLabel = function() {
			var prv = this.mine();
			return prv.getFieldDataForPath(prv.nodeData.titleLabelPath, prv.nodeData.title);
		};
		
		ns.Node.prototype.getExtendedTitle = function(beforeTitleLabel, afterTitleLabel) {
			var prv = this.mine();
			var me = this;
			
			return prv.renderExtendedTitle(me.getTitleLabel(), prv.getIdTypeLabel(), prv.getIdOrTempId(), beforeTitleLabel, afterTitleLabel);
		};
		
		ns.Node.prototype.getExtendedTitleQuoted = function() {
			var me = this;
			return me.getExtendedTitle(ns.Node.prv.LABEL_QUOTE_LEFT, ns.Node.prv.LABEL_QUOTE_RIGHT);
		};
		
		ns.Node.prototype.getExtendedTitleNotQuoted = function() {
			var me = this;
			return me.getExtendedTitle('', '');
		};
		
		ns.Node.prototype.processOutConnections = function(processorFunction) {
			var prv = this.mine();
			
			for (var i = 0; i < prv.outConnections.length; ++i) {
				var outConnection = prv.outConnections[i];
				if (processorFunction.apply(outConnection, [outConnection]) === false) {
					break;
				}
			}
		};
		
		ns.Node.prototype.hasOutConnectionTo = function(targetNode) {
			var me = this;
			return me.countOutConnectionsTo(targetNode) > 0;
		};
		
		ns.Node.prototype.countOutConnectionsTo = function(targetNode) {
			var prv = this.mine();
			var targetIdentifier = targetNode.getNodeIdentifier();
			if (typeof prv.outConnectionsByTargetIdentifier[targetIdentifier] == 'undefined') {
				return 0;
			}
			return prv.outConnectionsByTargetIdentifier[targetIdentifier].length;
		};
		
		ns.Node.prototype.countOutConnections = function() {
			var prv = this.mine();
			return prv.outConnections.length;
		};
		
		ns.Node.prototype.setOutConnection = function(newConnection) {
			var prv = this.mine();
			var me = this;
			
			me.removeOutConnection(newConnection);
			
			prv.outConnections.push(newConnection);
			
			var targetIdentifier = newConnection.getTargetNode().getNodeIdentifier();
			if (typeof prv.outConnectionsByTargetIdentifier[targetIdentifier] == 'undefined') {
				prv.outConnectionsByTargetIdentifier[targetIdentifier] = [];
			}
			prv.outConnectionsByTargetIdentifier[targetIdentifier].push(newConnection);
		};
		
		ns.Node.prototype.removeOutConnection = function(removedConnection) {
			var prv = this.mine();
			
			var targetIdentifier = removedConnection.getTargetNode().getNodeIdentifier();
			if (typeof prv.outConnectionsByTargetIdentifier[targetIdentifier] != 'undefined') {
				var outConnectionsToTarget = prv.outConnectionsByTargetIdentifier[targetIdentifier];
				for (var i = 0; i < outConnectionsToTarget.length; ++i) {
					var outConnectionToTarget = outConnectionsToTarget[i];
					if (outConnectionToTarget.getTypeName() == removedConnection.getTypeName()) {
						outConnectionsToTarget.splice(i, 1);
						
						for (var j = 0; j < prv.outConnections.length; ++j) {
							var outConnection = prv.outConnections[j];
							if (outConnection.getTargetNode().isSameNode(removedConnection.getTargetNode()) && outConnection.getTypeName() == removedConnection.getTypeName()) {
								prv.outConnections.splice(j, 1);
								break;
							}
						}
						break;
					}
				}
				if (prv.outConnectionsByTargetIdentifier[targetIdentifier].length == 0) {
					delete prv.outConnectionsByTargetIdentifier[targetIdentifier];
				}
			}
		};
		
		ns.Node.prototype.countInConnections = function() { return this.mine().inConnections.length; };
		
		ns.Node.prototype.removeInConnection = function(removedConnection) {
			var prv = this.mine();
			
			for (var i = 0; i < prv.inConnections.length; ++i) {
				var connection = prv.inConnections[i];
				
				if (connection.getTypeName() == removedConnection.getTypeName() && connection.getSourceNode().isSameNode(removedConnection.getSourceNode())) {
					prv.inConnections.splice(i, 1);
					break;
				}
			}
		};
		
		ns.Node.prototype.processInConnections = function(processorFunction) {
			var prv = this.mine();
			
			for (var i = 0; i < prv.inConnections.length; ++i) {
				var inConnection = prv.inConnections[i];
				if (processorFunction.apply(inConnection, [inConnection]) === false) {
					break;
				}
			}
		};
		
		ns.Node.prototype.setInConnection = function(newConnection) {
			var prv = this.mine();
			var me = this;
			
			me.removeInConnection(newConnection);
			prv.inConnections.push(newConnection);
		};
		
		ns.Node.prototype.isSameNode = function(otherNode) {
			var prv = this.mine();
			return otherNode.getNodeIdentifier() == prv.nodeIdentifier;
		};
		
		ns.Node.prototype.compareToNode = function(otherNode) {
			var prv = this.mine();
			return prv.nodeIdentifier.localeCompare(otherNode.getNodeIdentifier());
		};
		
		ns.Node.prototype.isSelectableTargetNode = function() {
			var prv = this.mine();
			var me = this;
			
			return prv.nodeData.maxIncoming == -1 || me.countInConnections() < prv.nodeData.maxIncoming;
		};
		
		ns.Node.prototype.isSelectableSourceNodeFor = function(connectionTypeName) {
			var prv = this.mine();
			var me = this;
			
			if (prv.nodeData.outConnectionTypes.indexOf(connectionTypeName) == -1) {
				return false;
			}
			
			return prv.nodeData.maxOutgoing == -1 || me.countOutConnections() < prv.nodeData.maxOutgoing;
		};
		
		ns.Node.prototype.isSourceOf = function(connection) {
			var prv = this.mine();
			
			return connection.getSourceNode().getNodeIdentifier() == prv.nodeIdentifier;
		};
		
		ns.Node.prototype.isTargetOf = function(connection) {
			var prv = this.mine();
			
			return connection.getTargetNode().getNodeIdentifier() == prv.nodeIdentifier;
		};
		
		ns.Node.prototype.install = function(parentQ, jsPlumbInstance) {
			var prv = this.mine();
			var me = this;
			var i = 0;
			
			prv.jsPlumbInstance = jsPlumbInstance;
			
			prv.containerQ = jQuery('<div></div>').addClass(ns.Node.prv.CLASS_CONTAINER).attr('id', ns.Node.idAttrValueFromNodeIdentifier(prv.nodeIdentifier));
			prv.setAbsolutePosition(prv.containerQ, prv.nodeData.position.x, prv.nodeData.position.y);
			prv.addClasses(prv.containerQ, prv.nodeData.classes);
			parentQ.append(prv.containerQ);
			
			prv.initX = prv.nodeData.position.x;
			prv.initY = prv.nodeData.position.y;
			
			prv.containerQ.mouseover(function(eventData) { prv.mouseOverContainer(eventData); });
			prv.containerQ.mouseout(function(eventData) { prv.mouseLeftContainer(eventData); });
			
			var configureButtonQ = jQuery('<span></span>').addClass(ns.Node.prv.CLASS_CONFIGURE_BUTTON);
			configureButtonQ.click(function() { prv.configureButtonClicked(); });
			configureButtonQ.mouseover(function(eventData) { prv.mouseOverConfigureButton(eventData); });
			configureButtonQ.mouseout(function(eventData) { prv.mouseLeftConfigureButton(eventData); });
			prv.containerQ.append(configureButtonQ);
			
			var deleteButtonQ = jQuery('<span></span>').addClass(ns.Node.prv.CLASS_DELETE_BUTTON);
			deleteButtonQ.click(function() { prv.deleteButtonClicked(); });
			deleteButtonQ.mouseover(function(eventData) { prv.mouseOverDeleteButton(eventData); });
			deleteButtonQ.mouseout(function(eventData) { prv.mouseLeftDeleteButton(eventData); });
			prv.containerQ.append(deleteButtonQ);
			
			for (i = 0; i < prv.nodeData.fields.length; ++i) {
				var fieldData = prv.nodeData.fields[i];
				var field = prv.fieldFactory.newFieldFromDef(fieldData);
				var propName = fieldData.propName;
				prv.fields.push(field);
				prv.putField(propName, field);
			}
			
			var iconQ = jQuery('<span></span>').addClass(ns.Node.prv.CLASS_NODE_ICON);
			prv.containerQ.append(iconQ);
			
			var titleLabel = me.getTitleLabel();
			prv.titleQ = jQuery('<div></div>').addClass(ns.Node.prv.CLASS_TITLE).text(titleLabel);
			prv.containerQ.append(prv.titleQ);
			
			prv.jsPlumbInstance.draggable(prv.containerQ);
			
			if (prv.nodeData.maxOutgoing != 0) {
				for (var i = 0; i < prv.nodeData.outConnectionTypes.length; ++i) {
					var connectionTypeName = prv.nodeData.outConnectionTypes[i];
					var connectionTypeDef = prv.getConnectionTypeDef(connectionTypeName);
					var typeClass = ns.Node.prv.CLASS_PREFIX_SOURCE_ENDPOINT + connectionTypeDef.typeName;
					
					var sourceEpQ = jQuery('<div></div>').addClass(typeClass);
					prv.containerQ.append(sourceEpQ);
					
					prv.addMouseOverListenerToSourceEp(sourceEpQ, connectionTypeName, connectionTypeDef.typeLabel);
					prv.addMouseOutListenerToSourceEp(sourceEpQ);
					
					var src = prv.jsPlumbInstance.makeSource(prv.containerQ, {
						filter: '.' + typeClass,
						anchor: 'Continuous',
						connectorStyle: { stroke: '#7c786a', strokeWidth: 2, outlineStroke: 'transparent', outlineWidth: 4 },
						connectionType: connectionTypeDef.typeName,
						maxConnections: prv.nodeData.maxOutgoing,
						onMaxConnections: function() { prv.onMaxConnections() }
					});
				}
			}
			
			if (prv.nodeData.maxIncoming != 0) {
				prv.jsPlumbInstance.makeTarget(prv.containerQ, {
					anchor: 'Continuous',
					allowLoopback: false
				});
			}
		};
		
		ns.Node.prototype.updateInitConnectionHash = function() {
			var prv = this.mine();
			prv.initConnectionHash = prv.getConnectionHash();
		};
		
		ns.Node.prototype.synchronize = function() {
			var prv = this.mine();
			
			var nodePosition = prv.getAbsolutePosition(prv.containerQ);
			prv.nodeData.position.x = nodePosition.left;
			prv.nodeData.position.y = nodePosition.top;
		};
		
		ns.Node.prototype.check = function() {
			var prv = this.mine();
			var me = this;
			
			var inConnectionCount = me.countInConnections();
			var outConnectionCount = me.countOutConnections();
			var maxIncoming = prv.nodeData.maxIncoming;
			var minIncoming = prv.nodeData.minIncoming;
			var maxOutgoing = prv.nodeData.maxOutgoing;
			var minOutgoing = prv.nodeData.minOutgoing;
			
			if (maxIncoming != -1 && inConnectionCount > maxIncoming) {
				var message = prv.renderConnctionCountViolationMessage(true, false, minIncoming, me.getExtendedTitleQuoted());
				return message;
			}
			
			if (minIncoming != -1 && inConnectionCount < minIncoming) {
				var message = prv.renderConnctionCountViolationMessage(true, true, minIncoming, me.getExtendedTitleQuoted());
				return message;
			}
			
			if (maxOutgoing != -1 && outConnectionCount > maxOutgoing) {
				var message = prv.renderConnctionCountViolationMessage(false, false, maxOutgoing, me.getExtendedTitleQuoted());
				return message;
			}
			
			if (minOutgoing != -1 && outConnectionCount < minOutgoing) {
				var message = prv.renderConnctionCountViolationMessage(false, true, minOutgoing, me.getExtendedTitleQuoted());
				return message;
			}
			
			return null;
		};
		
		ns.Node.prototype.asDataObject = function() {
			var prv = this.mine();
			var me = this;
			
			var data = {
				title: prv.nodeData.title,
				titleLabelPath: prv.nodeData.title,
				typeName: prv.nodeData.typeName,
				typeLabel: prv.nodeData.typeLabel,
				id: prv.nodeData.id,
				tempId: prv.nodeData.tempId,
				position: {
					x: prv.nodeData.position.x,
					y: prv.nodeData.position.y
				},
				classes: prv.nodeData.classes.slice(),
				maxOutgoing: prv.nodeData.maxOutgoing,
				minOutgoing: prv.nodeData.minOutgoing,
				maxIncoming: prv.nodeData.maxIncoming,
				minIncoming: prv.nodeData.minIncoming,
				outConnectionTypes: prv.nodeData.outConnectionTypes.slice(),
				dirty: me.isDirty(),
				fields: []
			};
			
			for (var i = 0; i < prv.fields.length; ++i) {
				var field = prv.fields[i];
				data.fields.push(field.asDataObject());
			}
			
			return data;
		};
		
		ns.Node.prototype.isDirty = function() {
			var prv = this.mine();
			
			if (prv.nodeData.dirty) {
				return true;
			}
			
			if (prv.initX != prv.nodeData.position.x || prv.initY != prv.nodeData.position.y) {
				return true;
			}
			
			var connectionHash = prv.getConnectionHash();
			if (connectionHash != prv.initConnectionHash) {
				return true;
			}
			
			for (var i = 0; i < prv.fields.length; ++i) {
				var field = prv.fields[i];
				if (field.isDirty()) {
					return true;
				}
			}
			
			return false;
		};
		
		ns.Node.prototype.setClean = function(idMap) {
			var prv = this.mine();
			var me = this;
			
			if (prv.nodeData.id == null && prv.nodeData.tempId != null && typeof idMap[prv.nodeData.tempId] != 'undefined') {
				prv.nodeData.id = idMap[prv.nodeData.tempId];
				prv.nodeData.tempId = null;
			}
			
			for (var i = 0; i < prv.fields.length; ++i) {
				var field = prv.fields[i];
				field.setClean(idMap);
			}
			
			prv.initX = prv.nodeData.position.x;
			prv.initY = prv.nodeData.position.y;
			
			me.updateInitConnectionHash();
			
			prv.nodeData.dirty = false;
		};
		
		ns.Node.prv = {
			CLASS_CONTAINER: 'rgm-modes-node-container',
			CLASS_NODE_ICON: 'rgm-modes-node-node-icon',
			CLASS_TITLE: 'rgm-modes-node-title',
			CLASS_CONFIGURE_BUTTON: 'rgm-modes-node-configure-button',
			CLASS_DELETE_BUTTON: 'rgm-modes-node-delete-button',
			CLASS_PREFIX_SOURCE_ENDPOINT: 'rgm-modes-node-source-endpoint-',
			LABEL_OK_BUTTON: 'OK',
			TPL_MODAL_TITLE: ['Configure ', 'extendedTitle'],
			TPL_EXTENDED_TITLE: ['', 'beforeTitleLabel', '', 'titleLabel', '', 'afterTitleLabel', ' (', 'idTypeLabel', ': ', 'idOrTempId', ')'],
			TPL_MAX_CONNECTIONS_EXCEEDED: ['The source ', 'extendedTitle', ' allows no more than ', 'maxOutgoing', ' outgoing connections.'],
			TPL_CONFIRM_DELETE: ['Do your really want to delete the node ', 'extendedTitle', ' and all incoming and outgoing connections?'],
			TPL_SOURCE_ENDPOINT_CONTEXT_INFO: ['Start Dragging for New ', 'connectionTypeLabel'],
			TPL_NODE_CONTEXT_INFO: ['', 'titleLabel', ' (', 'typeLabel', ')'],
			TPL_CONFIGURE_BUTTON_CONTEXT_INFO: ['Configure ', 'typeLabel', ' ', 'extendedTitle'],
			TPL_DELETE_BUTTON_CONTEXT_INFO: ['Delete ', 'typeLabel', ' ', 'extendedTitle'],
			TPL_TOO_FEW_IN_CONNECTIONS: ['Too few incoming connections into node ', 'extendedTitle', ': the node requires at least ', 'bound', ' incoming connection(s).'],
			TPL_TOO_MANY_IN_CONNECTIONS: ['Too many incoming connections into node ', 'extendedTitle', ': the node allows at most ', 'bound', ' incoming connection(s).'],
			TPL_TOO_FEW_OUT_CONNECTIONS: ['Too few outgoing connections out of node ', 'extendedTitle', ': the node requires at least ', 'bound', ' outgoing connection(s).'],
			TPL_TOO_MANY_OUT_CONNECTIONS: ['Too many outgoing connections out of node ', 'extendedTitle', ': the node allows at most ', 'bound', ' outgoing connection(s).'],
			ARG_TITLE_LABEL: 'titleLabel',
			ARG_ID_TYPE_LABEL: 'idTypeLabel',
			ARG_ID_OR_TEMP_ID: 'idOrTempId',
			ARG_BEFORE_TITLE_LABEL: 'beforeTitleLabel',
			ARG_AFTER_TITLE_LABEL: 'afterTitleLabel',
			ARG_EXTENDED_TITLE: 'extendedTitle',
			ARG_MAX_OUTGOING: 'maxOutgoing',
			ARG_CONNECTION_TYPE_LABEL: 'connectionTypeLabel',
			ARG_TYPE_LABEL: 'typeLabel',
			ARG_BOUND: 'bound',
			LABEL_ID: 'id',
			LABEL_TEMP_ID: 'temp. id',
			LABEL_QUOTE_LEFT: '"',
			LABEL_QUOTE_RIGHT: '"',
			NODE_IDENTIFIER_PREFIX: 'node_',
			ID_ATTR_PREFIX: 'rgm-modes-node-',
			TEMP_ID_PREFIX: 'temp_node',
			TEMP_ID_SEPARATOR: '_'
		};
		
		ns.Node.idAttrValueFromNodeIdentifier = function(nodeIdentifier) {
			return ns.Node.prv.ID_ATTR_PREFIX + nodeIdentifier;
		};
		
		ns.Node.nodeIdentifierFromIdAttrValue = function(idAttrValue) {
			return idAttrValue.substring(ns.Node.prv.ID_ATTR_PREFIX.length);
		};
		
		ns.Node.newTempId = function() {
			return [ns.Node.prv.TEMP_ID_PREFIX, (new Date()).getTime(), ns.UniqueStringGenerator.getInstance().next()].join(ns.Node.prv.TEMP_ID_SEPARATOR);
		};
		
		ns.Node.newNodeIdentifier = function() {
			return ns.Node.prv.NODE_IDENTIFIER_PREFIX + ns.UniqueStringGenerator.getInstance().next()
		};
	}
})(window.rgm.modes, window);




(function(ns, rns) {
	'use strict';
	if (typeof ns.Connection == 'undefined') {
		ns.Connection = function(sourceNode, targetNode, connectionData, jspConnection, fieldFactory, modelDesigner) {
			this.prv = [{
				me: this,
				sourceNode: sourceNode,
				targetNode: targetNode,
				connectionData: connectionData,
				jspConnection: jspConnection,
				fieldFactory: fieldFactory,
				modelDesigner: modelDesigner,
				
				fields: [],
				fieldByPropName: {},
				
				initSourceNodeIdentifier: sourceNode.getNodeIdentifier(),
				initTargetNodeIdentifier: targetNode.getNodeIdentifier(),
				
				modalTitleTemplate: null,
				connectionContextInfoTemplate: null,
				
				init: function() {
					var prv = this;
					for (var i = 0; i < prv.connectionData.fields.length; ++i) {
						var fieldData = prv.connectionData.fields[i];
						var field = prv.fieldFactory.newFieldFromDef(fieldData);
						prv.fields.push(field);
						prv.putField(fieldData.propName, field);
					}
				},
				
				renderModalTitle: function(typeLabel, titleLabel) {
					var prv = this;
					if (prv.modalTitleTemplate == null) {
						prv.modalTitleTemplate = new ns.MessageTemplate(ns.Connection.prv.TPL_MODAL_TITLE);
					}
					var msgArgs = {};
					msgArgs[ns.Connection.prv.ARG_TYPE_LABEL] = typeLabel;
					msgArgs[ns.Connection.prv.ARG_TITLE_LABEL] = titleLabel;
					return prv.modalTitleTemplate.render(msgArgs);
				},
				
				renderConnectionContextInfo: function(typeLabel, titleLabel) {
					var prv = this;
					if (prv.connectionContextInfoTemplate == null) {
						prv.connectionContextInfoTemplate = new ns.MessageTemplate(ns.Connection.prv.TPL_CONNECTION_CONTEXT_INFO);
					}
					var msgArgs = {};
					msgArgs[ns.Connection.prv.ARG_TYPE_LABEL] = typeLabel;
					msgArgs[ns.Connection.prv.ARG_TITLE_LABEL] = titleLabel;
					return prv.connectionContextInfoTemplate.render(msgArgs);
				},
				
				putField: function(propName, field) {
					var prv = this;
					prv.fieldByPropName['pn' + propName] = field;
				},
				
				getField: function(propName, alt) {
					var prv = this;
					var key = 'pn' + propName;
					if (typeof prv.fieldByPropName[key] == 'undefined') return alt;
					return prv.fieldByPropName[key];
				},
				
				getFieldDataForPath: function(path, alt) {
					var prv = this;
					if (path == null) return alt;
					var field = prv.getField(path[0], null);
					if (field == null) return alt;
					var cur = field.asDataObject();
					for (var i = 1; i < path.length; ++i) {
						var segment = path[i];
						if (typeof cur[segment] == 'undefined') {
							return alt;
						}
						cur = cur[segment];
					}
					return cur;
				},
				
				updateTitleDisplay: function() {
					var prv = this;
					prv.jspConnection.setLabel(prv.getTitleLabel());
				},
				
				getTitleLabel: function() {
					var prv = this;
					return prv.getFieldDataForPath(prv.connectionData.titleLabelPath, prv.connectionData.title);
				},
				
				modalOkButtonClicked: function() {
					var prv = this;
					var me = this.me;
					var i = 0;
					
					for (var i = 0; i < prv.fields.length; ++i) {
						var field = prv.fields[i];
						field.synchronize();
						if (field.check() != null) {
							return false;
						}
					}
					
					for (var i = 0; i < prv.fields.length; ++i) {
						var field = prv.fields[i];
						field.prepareRemoveFromDocument();
					}
					
					prv.updateTitleDisplay();
					
					return true;
				},
				
				modalDeleteButtonClicked: function() {
					var prv = this;
					var me = this.me;
					
					prv.modelDesigner.removeConnection(me);
					prv.modelDesigner.detachJspConnection(prv.jspConnection);
					
					prv.modelDesigner.hideModal();
				},
				
				setUpModal: function(modalQ, modalTitleQ, modalBodyQ, modalFooterQ, modalOkButtonQ) {
					var prv = this;
					var me = this.me;
					var i = 0;
					
					modalTitleQ.text(prv.renderModalTitle(prv.connectionData.typeLabel, prv.getTitleLabel()));
					
					if (prv.fields.length > 0) {
						var fieldsTitleQ = jQuery('<h2></h2>').text(ns.Connection.prv.LABEL_FIELDS_TITLE);
						modalBodyQ.append(fieldsTitleQ);
						
						for (i = 0; i < prv.fields.length; ++i) {
							var field = prv.fields[i];
							field.addToDocument(modalBodyQ);
						}
					} else {
						var noFieldsMsgQ = jQuery('<div class="alert alert-info"></div>').text(ns.Connection.prv.LABEL_NO_FIELDS);
						modalBodyQ.append(noFieldsMsgQ);
					}
					
					var deleteButtonQ = jQuery('<button type="button" class="btn btn-default"></button>').text(ns.Connection.prv.LABEL_DELETE_BUTTON_TEXT);
					modalFooterQ.prepend(deleteButtonQ);
					
					deleteButtonQ.click(function() { prv.modalDeleteButtonClicked(); });
					
					modalOkButtonQ.text(ns.Connection.prv.LABEL_OK_BUTTON_TEXT);
				},
				
				connectionClicked: function(jspConnection, originalEvent) {
					var prv = this;
					prv.modelDesigner.showModal(
						function(modalQ, modalTitleQ, modalBodyQ, modalFooterQ, modalOkButtonQ) { prv.setUpModal(modalQ, modalTitleQ, modalBodyQ, modalFooterQ, modalOkButtonQ); },
						function() { return prv.modalOkButtonClicked(); }
					);
				},
				
				mouseOverConnection: function(jspConnection, originalEvent) {
					var prv = this;
					prv.modelDesigner.showContextInfo(prv.renderConnectionContextInfo(prv.connectionData.typeLabel, prv.getTitleLabel()));
				},
				
				mouseLeftConnection: function(jspConnection, originalEvent) {
					var prv = this;
					prv.modelDesigner.hideContextInfo();
				}
			}];
			this.prv[0].init();
		};
		
		ns.Connection.prototype.mine = function() {
			return this.prv[0];
		};
		
		ns.Connection.prototype.getTypeName = function() { return this.mine().connectionData.typeName; };
		
		ns.Connection.prototype.getSourceNode = function() { return this.mine().sourceNode; };
		
		ns.Connection.prototype.setSourceNode = function(sourceNode) { this.mine().sourceNode = sourceNode; };
		
		ns.Connection.prototype.getTargetNode = function() { return this.mine().targetNode; };
		
		ns.Connection.prototype.setTargetNode = function(targetNode) { this.mine().targetNode = targetNode; };
		
		ns.Connection.prototype.updateParams = function() {
			var prv = this.mine();
			
			prv.jspConnection.setParameter(ns.Connection.prv.PARAM_SOURCE_IDENTIFIER, prv.sourceNode.getNodeIdentifier());
			prv.jspConnection.setParameter(ns.Connection.prv.PARAM_TARGET_IDENTIFIER, prv.targetNode.getNodeIdentifier());
			prv.jspConnection.setParameter(ns.Connection.prv.PARAM_TYPE_NAME, prv.connectionData.typeName);
		};
		
		ns.Connection.prototype.detachJspConnection = function() {
			var prv = this.mine();
			
			prv.modelDesigner.detachJspConnection(prv.jspConnection);
		};
		
		ns.Connection.prototype.finishInstallation = function() {
			var prv = this.mine();
			var me = this;
			
			prv.jspConnection.bind('click', function(jspConnection, originalEvent) {
				prv.connectionClicked(jspConnection, originalEvent);
			});
			
			prv.jspConnection.bind('mouseover', function(jspConnection, originalEvent) {
				prv.mouseOverConnection(jspConnection, originalEvent);
			});
			
			prv.jspConnection.bind('mouseout', function(jspConnection, originalEvent) {
				prv.mouseLeftConnection(jspConnection, originalEvent);
			});
			
			me.updateParams();
			
			prv.updateTitleDisplay();
		};
		
		ns.Connection.prototype.synchronize = function() {
			var prv = this;
		};
		
		ns.Connection.prototype.setClean = function(idMap) {
			var prv = this.mine();
			
			if (prv.connectionData.id == null && prv.connectionData.tempId != null && typeof idMap[prv.connectionData.tempId] != 'undefined') {
				prv.connectionData.id = idMap[prv.connectionData.tempId];
				prv.connectionData.tempId = null;
			}
			
			for (var i = 0; i < prv.fields.length; ++i) {
				var field = prv.fields[i];
				field.setClean(idMap);
			}
			
			prv.initSourceNodeIdentifier = prv.sourceNode.getNodeIdentifier();
			prv.initTargetNodeIdentifier = prv.targetNode.getNodeIdentifier();
			
			prv.connectionData.dirty = false;
		};
		
		ns.Connection.prototype.isDirty = function() {
			var prv = this.mine();
			
			if (prv.connectionData.dirty) return true;
			
			if (prv.initSourceNodeIdentifier != prv.sourceNode.getNodeIdentifier() || prv.initTargetNode != prv.targetNode.getNodeIdentifier()) {
				return true;
			}
			
			for (var i = 0; i < prv.fields.length; ++i) {
				var field = prv.fields[i];
				if (field.isDirty()) {
					return true;
				}
			}
			
			return false;
		};
		
		ns.Connection.prototype.asDataObject = function() {
			var prv = this.mine();
			var me = this;
			
			var data = {
				id: prv.connectionData.id,
				tempId: prv.connectionData.tempId,
				typeName: prv.connectionData.typeName,
				typeLabel: prv.connectionData.typeLabel,
				title: prv.connectionData.title,
				titleLabelPath: prv.connectionData.titleLabelPath,
				sourceNode: {
					id: prv.sourceNode.getId(),
					tempId: prv.sourceNode.getTempId()
				},
				targetNode: {
					id: prv.targetNode.getId(),
					tempId: prv.targetNode.getTempId()
				},
				dirty: me.isDirty(),
				fields: []
			};
			
			for (var i = 0; i < prv.fields.length; ++i) {
				var field = prv.fields[i];
				data.fields.push(field.asDataObject());
			}
			
			return data;
		};
		
		ns.Connection.prv = {
			TPL_MODAL_TITLE: ['Configure ', 'typeLabel', ' "', 'titleLabel', '"'],
			TPL_CONNECTION_CONTEXT_INFO: ['', 'titleLabel', ' (', 'typeLabel', ')'],
			ARG_TYPE_LABEL: 'typeLabel',
			ARG_TITLE_LABEL: 'titleLabel',
			LABEL_FIELDS_TITLE: 'Properties',
			LABEL_DELETE_BUTTON_TEXT: 'Delete',
			LABEL_OK_BUTTON_TEXT: 'OK',
			LABEL_NO_FIELDS: 'There are no properties to configure',
			PARAM_SOURCE_IDENTIFIER: 'sourceIdentifier',
			PARAM_TARGET_IDENTIGIER: 'targetIdentifier',
			PARAM_TYPE_NAME: 'typeName',
			TEMP_ID_PREFIX: 'temp_connection',
			TEMP_ID_SEPARATOR: '_'
		};
		
		ns.Connection.getSourceIdentifierFromParams = function(jspConnection) {
			var identifier = jspConnection.getParameter(ns.Connection.prv.PARAM_SOURCE_IDENTIFIER);
			if (identifier) return identifier;
			return null;
		};
		
		ns.Connection.getTargetIdentifierFromParams = function(jspConnection) {
			var identifier = jspConnection.getParameter(ns.Connection.prv.PARAM_TARGET_IDENTIFIER);
			if (identifier) return identifier;
			return null;
		};
		
		ns.Connection.getTypeNameFromParams = function(jspConnection) {
			var typeName = jspConnection.getParameter(ns.Connection.prv.PARAM_TYPE_NAME);
			if (typeName) return typeName;
			return null;
		};
		
		ns.Connection.newTempId = function() {
			return [ns.Connection.prv.TEMP_ID_PREFIX, (new Date()).getTime(), ns.UniqueStringGenerator.getInstance().next()].join(ns.Connection.prv.TEMP_ID_SEPARATOR);
		};
	}
})(window.rgm.modes, window);




(function(ns, rns) {
	'use strict';
	if (typeof ns.ModelDesigner == 'undefined') {
		ns.ModelDesigner = function(fieldFactory) {
			this.prv = [{
				me: this,
				fieldFactory: fieldFactory,
				
				containerQ: null,
				drawingQ: null,
				contextInfoContainerQ: null,
				nodeInsertDropdownToggleQ: null,
				nodeInsertDropupQ: null,
				modalQ: null,
				modalTitleQ: null,
				modalBodyQ: null,
				modalFooterQ: null,
				modalOkButtonQ: null,
				modalOkHandler: null,
				
				savingInProgress: false,
				savingModalTitleQ: null,
				savingModalBodyQ: null,
				savingModalOkButtonQ: null,
				
				modelData: null,
				saveUrl: null,
				
				nodeByIdentifier: {},
				nodeIdentifiers: [],
				nodeById: {},
				nodeByTempId: {},
				
				connectionByKey: {},
				connectionKeys: [],
				
				jsPlumbInstance: null,
				ignoreConnectionDetached: false,
				
				contextInfoDefaultText: '',
				selectedInsertNodeTypeDef: null,
				
				nodeInvalidConfirmSaveTemplate: null,
				
				processNodes: function(processorFunction) {
					var prv = this;
					var me = this.me;
					
					for (var i = 0; i < prv.nodeIdentifiers.length; ++i) {
						var nodeIdentifier = prv.nodeIdentifiers[i];
						var node = prv.nodeByIdentifier[nodeIdentifier];
						if (processorFunction.apply(me, [node]) === false) break;
					}
				},
				
				processConnections: function(processorFunction) {
					var prv = this;
					var me = this.me;
					
					for (var i = 0; i < prv.connectionKeys.length; ++i) {
						var connectionKey = prv.connectionKeys[i];
						var connection = prv.connectionByKey[connectionKey];
						if (processorFunction.apply(me, [connection]) === false) break;
					}
				},
				
				renderNodeInvalidConfirmSaveMessage: function(node, message) {
					var prv = this;
					if (prv.nodeInvalidConfirmSaveTemplate == null) {
						prv.nodeInvalidConfirmSaveTemplate = new ns.MessageTemplate(ns.ModelDesigner.prv.TPL_NODE_INVALID_CONFIRM_SAVE);
					}
					var msgArgs = {};
					msgArgs[ns.ModelDesigner.prv.ARG_EXTENDED_TITLE] = node.getExtendedTitleQuoted();
					msgArgs[ns.ModelDesigner.prv.ARG_TYPE_LABEL] = node.getTypeLabel();
					msgArgs[ns.ModelDesigner.prv.ARG_INVALID_MESSAGE] = message;
					return prv.nodeInvalidConfirmSaveTemplate.render(msgArgs);
				},
				
				getNextNodes: function(startNode, replacedConnection, replacementSource, replacementTarget) {
					var i = 0;
					
					var nextNodes = [];
					startNode.processOutConnections(function(outConnection) {
						if (
							replacedConnection == null
							|| !replacedConnection.getSourceNode().isSameNode(startNode)
							|| !replacedConnection.getTargetNode().isSameNode(outConnection.getTargetNode())
							|| outConnection.getTypeName() != replacedConnection.getTypeName()
						) {
							nextNodes.push(outConnection.getTargetNode());
						}
						return true;
					});
					
					if (replacementSource != null && replacementSource.isSameNode(startNode)) {
						nextNodes.push(replacementTarget);
					}
					
					nextNodes.sort(function(node1, node2) { return node1.compareToNode(node2); });
					for (i = nextNodes.length - 2; i >= 0; --i) {
						if (nextNodes[i].isSameNode(nextNodes[i + 1])) {
							nextNodes.splice(i, 1);
						}
					}
					
					return nextNodes;
				},
				
				getConnectionKey: function(sourceIdentifier, targetIdentifier, connectionTypeName) {
					return sourceIdentifier.length + '_' + targetIdentifier.length + '_' + connectionTypeName.length + '_' + sourceIdentifier + '_' + targetIdentifier + '_' + connectionTypeName;
				},
				
				getConnectionKeyForNodes: function(sourceNode, targetNode, connectionTypeName) {
					var prv = this;
					return prv.getConnectionKey(sourceNode.getNodeIdentifier(), targetNode.getNodeIdentifier(), connectionTypeName);
				},
				
				getKeyForConnection: function(connection) {
					var prv = this;
					return prv.getConnectionKeyForNodes(connection.getSourceNode(), connection.getTargetNode(), connection.getTypeName());
				},
				
				connectionDetached: function(info, originalEvent) {
					var prv = this;
					var me = this.me;
					
					if (prv.ignoreConnectionDetached) return;
					
					var sourceNodeIdentifier = ns.Node.nodeIdentifierFromIdAttrValue(info.sourceId);
					var targetNodeIdentifier = ns.Node.nodeIdentifierFromIdAttrValue(info.targetId);
					
					var connectionTypeDef = prv.getFirstConnectionTypeDef(info.connection.getType());
					var connectionTypeName = connectionTypeDef.typeName;
					
					var connectionKey = prv.getConnectionKey(sourceNodeIdentifier, targetNodeIdentifier, connectionTypeName);
					var connection = prv.connectionByKey[connectionKey];
					
					me.removeConnection(connection);
				},
				
				beforeDropConnection: function(info) {
					var prv = this;
					var me = this.me;
					
					var newSourceIdentifier = ns.Node.nodeIdentifierFromIdAttrValue(info.sourceId);
					var newTargetIdentifier = ns.Node.nodeIdentifierFromIdAttrValue(info.targetId);
					
					var newSourceNode = prv.nodeByIdentifier[newSourceIdentifier];
					var newTargetNode = prv.nodeByIdentifier[newTargetIdentifier];
					
					var origSourceIdentifier = ns.Connection.getSourceIdentifierFromParams(info.connection);
					
					if (origSourceIdentifier != null) {
						var typeName = ns.Connection.getTypeNameFromParams(info.connection);
						var origTargetIdentifier = ns.Connection.getTargetIdentifierFromParams(info.connection);
						
						var connectionKey = prv.getConnectionKey(origSourceIdentifier, origTargetIdentifier, typeName);
						var connection = prv.connectionByKey[connectionKey];
						
						var notAllowedMessage = me.checkChangeConnectionAllowed(newSourceNode, newTargetNode, connection);
						if (notAllowedMessage != null) {
							alert(notAllowedMessage);
							return false;
						}
						
						me.changeConnectionEndpoints(connection, newSourceNode, newTargetNode);
						
						return true;
					} else {
						var connectionTypeDef = prv.getFirstConnectionTypeDef(info.connection.getType());
						if (connectionTypeDef == null) return false;
						
						var connectionData = prv.deepCopyDataObject(connectionTypeDef);
						connectionData.tempId = ns.Connection.newTempId();
						
						if (!newSourceNode.isSelectableSourceNodeFor(connectionData.typeName)) {
							alert(ns.ModelDesigner.prv.LABEL_SOURCE_REJECTED_CONNECTION);
							return false;
						}
				
						if (!newTargetNode.isSelectableTargetNode()) {
							alert(ns.ModelDesigner.prv.LABEL_TARGET_REJECTED_CONNECTION);
							return false;
						}
						
						var parallelMessage = me.checkForParallel(newSourceNode, newTargetNode, null);
						if (parallelMessage != null) {
							alert(parallelMessage);
							return false;
						}
						
						var cycleMessage = me.checkForCycle(null, newSourceNode, newTargetNode);
						if (cycleMessage != null) {
							alert(cycleMessage);
							return false;
						}
						
						var connection = new ns.Connection(newSourceNode, newTargetNode, connectionData, info.connection, prv.fieldFactory, me);
						newSourceNode.setOutConnection(connection);
						newTargetNode.setInConnection(connection);
						connection.finishInstallation();
						
						var connectionKey = prv.getKeyForConnection(connection);
						prv.connectionKeys.push(connectionKey);
						prv.connectionByKey[connectionKey] = connection;
						
						return true;
					}
				},
				
				getNodeById: function(nodeId, altReturn) {
					var prv = this;
					return (typeof prv.nodeById[ns.ModelDesigner.prv.NODE_ID_KEY_PREFIX + nodeId] != 'undefined') ? prv.nodeById[ns.ModelDesigner.prv.NODE_ID_KEY_PREFIX + nodeId] : altReturn;
				},
				
				getNodeByTempId: function(nodeTempId, altReturn) {
					var prv = this;
					return (typeof prv.nodeById[nodeTempId] != 'undefined') ? prv.nodeById[nodeTempId] : altReturn;
				},
				
				getNodeByIdOrTempId: function(nodeId, nodeTempId) {
					var prv = this;
					return prv.getNodeById(nodeId, prv.getNodeByTempId(nodeTempId, null));
				},
				
				getFirstConnectionTypeDef: function(strings) {
					var prv = this;
					for (var i = 0; i < prv.modelData.connectionTypes.length; ++i) {
						var connectionTypeDef = prv.modelData.connectionTypes[i];
						if (strings.indexOf(connectionTypeDef.typeName) != -1) {
							return connectionTypeDef;
						}
					}
					return null;
				},
				
				deepCopyDataObject: function(refObj) {
					return JSON.parse(JSON.stringify(refObj));
				},
				
				installModel: function() {
					var prv = this;
					var me = this.me;
					var i = 0;
					
					for (i = 0; i < prv.modelData.nodes.length; ++i) {(function(i) {
						var nodeIdentifier = ns.Node.newNodeIdentifier();
						
						var nodeData = prv.modelData.nodes[i];
						var node = new ns.Node(nodeData, nodeIdentifier, prv.fieldFactory, me, prv.modelData.connectionTypes);
						node.install(prv.drawingQ, prv.jsPlumbInstance);
						if (nodeData.id != null) {
							prv.nodeById[ns.ModelDesigner.prv.NODE_ID_KEY_PREFIX + nodeData.id] = node;
						} else {
							prv.nodeByTempId[nodeData.tempId] = node;
						}
						prv.nodeByIdentifier[nodeIdentifier] = node;
						prv.nodeIdentifiers.push(nodeIdentifier);
					})(i);}
					
					for (i = 0; i < prv.modelData.connections.length; ++i) {(function(i) {
						var connectionData = prv.modelData.connections[i];
						var typeName = connectionData.typeName;
						
						var sourceNode = prv.getNodeByIdOrTempId(connectionData.sourceNode.id, connectionData.sourceNode.tempId);
						var targetNode = prv.getNodeByIdOrTempId(connectionData.targetNode.id, connectionData.targetNode.tempId);
						
						var jspConnection = prv.jsPlumbInstance.connect({
							source: sourceNode.getContainerQ(),
							target: targetNode.getContainerQ(),
							type: typeName
						});
						
						var connection = new ns.Connection(sourceNode, targetNode, connectionData, jspConnection, prv.fieldFactory, me);
						sourceNode.setOutConnection(connection);
						targetNode.setInConnection(connection);
						
						connection.finishInstallation();
						
						var connectionKey = prv.getKeyForConnection(connection);
						prv.connectionByKey[connectionKey] = connection;
						prv.connectionKeys.push(connectionKey);
					})(i);}
					
					prv.processNodes(function(node) {
						node.updateInitConnectionHash();
						return true;
					});
				},
				
				buildConnectionOverlay: function(connectionTypeName) {
					var drawingQ = jQuery('<div></div>').addClass(ns.ModelDesigner.prv.CLASS_PREFIX_CONNECTION_OVERLAY + connectionTypeName);
					var outerQ = jQuery('<div></div>');
					outerQ.append(drawingQ);
					return outerQ;
				},
				
				registerConnectionType: function(jsPlumbInstance, connectionTypeDef) {
					var prv = this;
					
					var connectionTypeName = connectionTypeDef.typeName;
					
					jsPlumbInstance.registerConnectionType(connectionTypeName, {
						anchor: 'Continuous',
						connector: 'StateMachine',
						hoverPaintStyle:{ stroke: '#00ff00', strokeWidth: 2 },
						// detachable: false,
						overlays: [
							['Arrow', { width:10, length: 14, foldback: 0.8, location:1, id: 'arrow' } ],
							['Custom', {
								create: function(component) { return prv.buildConnectionOverlay(connectionTypeName) },
								location: 0.7,
								id: 'typeOverlay'
							}]
						]
					});
				},
				
				registerConnectionTypes: function() {
					var prv = this;
					for (var i = 0; i < prv.modelData.connectionTypes.length; ++i) {
						var connectionTypeDef = prv.modelData.connectionTypes[i];
						prv.registerConnectionType(prv.jsPlumbInstance, connectionTypeDef);
					}
				},
				
				setUpJsPlumbInstance: function() {
					var prv = this;
					var me = this.me;
					
					if (prv.jsPlumbInstance == null) {
						prv.jsPlumbInstance = jsPlumb.getInstance({
							Endpoint: ['Dot', {radius: 7}],
							Connector: 'StateMachine',
							Container: prv.drawingQ
						});
						
						prv.jsPlumbInstance.bind('beforeDrop', function(info) { return prv.beforeDropConnection(info); });
						
						prv.jsPlumbInstance.bind('connectionDetached', function(info, originalEvent) { prv.connectionDetached(info, originalEvent); });
					}
				},
				
				setVisitMarkToAllNodes: function(visitMark) {
					var prv = this;
					prv.processNodes(function(node) {
						node.setVisitMark(visitMark);
						return true;
					});
				},
				
				reachesCycle: function(currentNode, pathNodes, replacedConnection, replacementSource, replacementTarget) {
					var prv = this;
					
					pathNodes.push(currentNode);
					
					if (currentNode.getVisitMark() == 1) {
						return true;
					} else if (currentNode.getVisitMark() == 0) {
						currentNode.setVisitMark(1);
						
						var nextNodes = prv.getNextNodes(currentNode, replacedConnection, replacementSource, replacementTarget);
						for (var i = 0; i < nextNodes.length; ++i) {
							var nextNode = nextNodes[i];
							if (prv.reachesCycle(nextNode, pathNodes, replacedConnection, replacementSource, replacementTarget)) {
								return true;
							}
						}
						
						currentNode.setVisitMark(2);
					}
					
					pathNodes.pop();
					
					return false;
				},
				
				installModal: function() {
					var prv = this;
					
					var modalId = ns.UniqueStringGenerator.getInstance().next();
					
					prv.modalQ = jQuery('<div class="modal fade" tabindex="-1" role="dialog" data-backdrop="static" data-keyboard="false"></div>').attr('id', modalId);
				
					var inner1Q = jQuery('<div class="modal-dialog" role="document"></div>');
					prv.modalQ.append(inner1Q);
					
					var inner2Q = jQuery('<div class="modal-content"></div>');
					inner1Q.append(inner2Q);
					
					var modalHeaderQ = jQuery('<div class="modal-header"></div>');
					inner2Q.append(modalHeaderQ);
					
					prv.modalTitleQ = jQuery('<h1></h1>');
					modalHeaderQ.append(prv.modalTitleQ);
					
					prv.modalBodyQ = jQuery('<div class="modal-body"></div>');
					inner2Q.append(prv.modalBodyQ);
					
					prv.modalFooterQ = jQuery('<div class="modal-footer"></div>');
					inner2Q.append(prv.modalFooterQ);
					
					prv.modalOkButtonQ = jQuery('<button type="button" class="btn btn-default"></button>');
					prv.modalFooterQ.append(prv.modalOkButtonQ);
					
					prv.modalOkButtonQ.click(function(event) { return prv.modalOkButtonClicked(event); });
					
					prv.containerQ.append(prv.modalQ);
					prv.modalQ.modal('hide');
				},
				
				installNodeInsertItems: function(listQ) {
					var prv = this;
					for (var i = 0; i < prv.modelData.nodeTypes.length; ++i) {
						var typeDef = prv.modelData.nodeTypes[i];
						
						var itemQ = jQuery('<li></li>').addClass(ns.ModelDesigner.prv.CLASS_PREFIX_INSERT_NODE_ITEM + typeDef.typeName);
						listQ.append(itemQ);
						
						var linkQ = jQuery('<a></a>').text(typeDef.typeLabel);
						(function(typeDef) { linkQ.click(function(event) { return prv.insertNodeItemClicked(event, typeDef); }); })(typeDef);
						itemQ.append(linkQ);
						
						var iconQ = jQuery('<span></span>').addClass(ns.ModelDesigner.prv.CLASS_NODE_INSERT_ITEM_ICON);
						linkQ.prepend(iconQ);
					}
				},
				
				modalOkButtonClicked: function(event) {
					var prv = this;
					var me = this.me;
					var close = typeof prv.modalOkHandler != 'function' || prv.modalOkHandler.apply(prv.modalQ, []);
					if (close) {
						me.hideModal();
					} else {
						event.preventDefault();
						event.stopImmediatePropagation();
						return false; 
					}
				},
				
				insertNodeItemClicked: function(event, nodeTypeDef) {
					var prv = this;
					var me = this.me;
					
					event.preventDefault();
					
					prv.nodeInsertDropupQ.removeClass('open');
					prv.nodeInsertDropdownToggleQ.attr('aria-expanded', 'false');
					
					prv.selectedInsertNodeTypeDef = nodeTypeDef;
					prv.drawingQ.addClass(ns.ModelDesigner.prv.CLASS_INSERTING_NODE);
					
					me.setContextInfoDefaultText(ns.ModelDesigner.prv.LABEL_NODE_INSERT_CLICK_INSTRUCTION);
					me.showContextInfo(ns.ModelDesigner.prv.LABEL_NODE_INSERT_CLICK_INSTRUCTION);
					
					return false;
				},
				
				drawingAreaClicked: function(event) {
					var prv = this;
					var me = this.me;
					
					if (prv.selectedInsertNodeTypeDef != null) {
						var nodeIdentifier = ns.Node.newNodeIdentifier();
						var tempId = ns.Node.newTempId();
						
						var matrix = prv.drawingQ.css('transform');
						var matrixScale = 1;
						if (typeof matrix != 'undefined' && matrix != null) {
							var matrixEntries = [];
							var numberRegex = new RegExp('[0-9\\.]+', 'g');
							for (var match = numberRegex.exec(matrix); match != null; match = numberRegex.exec(matrix)) {
								matrixEntries.push(match);
							}
							if (matrixEntries.length == 6) {
								matrixScale = matrixEntries[0];
							}
						}
						var typeDef = prv.deepCopyDataObject(prv.selectedInsertNodeTypeDef);
						typeDef.position = {
							x: (event.pageX - prv.drawingQ.offset().left) / matrixScale,
							y: (event.pageY - prv.drawingQ.offset().top) / matrixScale
						}
						typeDef.tempId = tempId;
						
						var node = new ns.Node(typeDef, nodeIdentifier, prv.fieldFactory, me, prv.modelData.connectionTypes);
						node.install(prv.drawingQ, prv.jsPlumbInstance);
						prv.nodeByTempId[tempId] = node;
						prv.nodeByIdentifier[nodeIdentifier] = node;
						prv.nodeIdentifiers.push(nodeIdentifier);
						
						prv.drawingQ.removeClass(ns.ModelDesigner.prv.CLASS_INSERTING_NODE);
						me.clearContextInfoDefaultText();
						me.hideContextInfo();
						prv.selectedInsertNodeTypeDef = null;
					}
				},
				
				mouseOverZoomInButton: function(eventData) {
					var me = this.me;
					me.showContextInfo(ns.ModelDesigner.prv.LABEL_ZOOM_IN);
				},
				
				mouseLeftZoomInButton: function(eventData) {
					var me = this.me;
					me.hideContextInfo();
				},
				
				mouseOverZoomOutButton: function(eventData) {
					var me = this.me;
					me.showContextInfo(ns.ModelDesigner.prv.LABEL_ZOOM_OUT);
				},
				
				mouseLeftZoomOutButton: function(eventData) {
					var me = this.me;
					me.hideContextInfo();
				},
				
				mouseOverNodeInsertToggleButton: function(eventData) {
					var me = this.me;
					me.showContextInfo(ns.ModelDesigner.prv.LABEL_NODE_INSERT_BUTTON_CONTEXT_INFO);
				},
				
				mouseLeftNodeInsertToggleButton: function(eventData) {
					var me = this.me;
					me.hideContextInfo();
				},
				
				setUpSavingModal: function(modalQ, modalTitleQ, modalBodyQ, modalFooterQ, modalOkButtonQ) {
					var prv = this;
					
					modalTitleQ.text(ns.ModelDesigner.prv.LABEL_SAVING_TITLE);
					
					var savingInfoQ = jQuery('<p></p>').text(ns.ModelDesigner.prv.LABEL_SAVING_BODY);
					modalBodyQ.append(savingInfoQ);
					
					var savingSpinnerQ = jQuery('<div></div>').addClass(ns.ModelDesigner.prv.CLASS_SAVING_SPINNER);
					modalBodyQ.append(savingSpinnerQ);
					
					modalOkButtonQ.addClass('disabled').text(ns.ModelDesigner.prv.LABEL_SAVING_MODAL_OK);
					
					prv.savingModalTitleQ = modalTitleQ;
					prv.savingModalBodyQ = modalBodyQ;
					prv.savingModalOkButtonQ = modalOkButtonQ;
				},
				
				savingSuccessful: function(data) {
					var prv = this;
					
					prv.savingInProgress = false;
					
					prv.savingModalTitleQ.text(ns.ModelDesigner.prv.LABEL_SAVING_SUCCESS_TITLE);
					
					var successInfoQ = jQuery('<p></p>').text(ns.ModelDesigner.prv.LABEL_SAVING_SUCCESS_BODY);
					prv.savingModalBodyQ.empty();
					prv.savingModalBodyQ.append(successInfoQ);
					
					prv.modalOkButtonQ.removeClass('disabled');
					
					prv.processNodes(function(node) {
						node.setClean(data);
					});
					
					prv.processConnections(function(connection) {
						connection.setClean(data);
					});
				},
				
				savingFailed: function(data) {
					var prv = this;
					
					prv.savingInProgress = false;
					
					prv.savingModalTitleQ.text(ns.ModelDesigner.prv.LABEL_SAVING_FAILED_TITLE);
					
					var failInfoQ = jQuery('<p></p>').text(ns.ModelDesigner.prv.LABEL_SAVING_FAILED_BODY);
					prv.savingModalBodyQ.empty();
					prv.savingModalBodyQ.append(failInfoQ);
					
					prv.savingModalOkButtonQ.removeClass('disabled');
				},
				
				savingModalOkButtonClicked: function() {
					var prv = this;
					if (!prv.savingInProgress) {
						prv.savingModalTitleQ = null;
						prv.savingModalBodyQ = null;
						prv.savingModalOkButtonQ = null;
						return true;
					} else {
						return false;
					}
				},
				
				saveButtonClicked: function(eventData) {
					var prv = this;
					var me = this.me;
					if (prv.saveUrl != null) {
						var valid = true;
						var abortSave = false;
						
						prv.processNodes(function(node) {
							node.synchronize()
						});
						
						prv.processNodes(function(node) {
							var nodeInvalidMessage = node.check();
							if (nodeInvalidMessage != null) {
								if (!confirm(prv.renderNodeInvalidConfirmSaveMessage(node, nodeInvalidMessage))) {
									abortSave = true;
								}
								return false;
							}
							return true;
						});
						if (!abortSave) {
							prv.savingInProgress = true;
							var nodeData = [];
							prv.processNodes(function(node) {
								nodeData.push(prv.deepCopyDataObject(node.asDataObject()));
							});
							
							var connectionData = [];
							prv.processConnections(function(connection) {
								connectionData.push(prv.deepCopyDataObject(connection.asDataObject()));
							});
							
							var data = {
								id: 1,
								valid: valid,
								cyclesAllowed: prv.modelData.cyclesAllowed,
								parallelsAllowed: prv.modelData.parallelsAllowed,
								nodes: nodeData,
								connections: connectionData,
								nodeTypes: prv.modelData.nodeTypes,
								connectionTypes: prv.modelData.connectionTypes
							};
							
							me.showModal(
								function(modalQ, modalTitleQ, modalBodyQ, modalFooterQ, modalOkButtonQ) { prv.setUpSavingModal(modalQ, modalTitleQ, modalBodyQ, modalFooterQ, modalOkButtonQ); },
								function() { return prv.savingModalOkButtonClicked(); }
							);
							
							jQuery.post(prv.saveUrl, JSON.stringify(data))
								.done(function(data) { prv.savingSuccessful(data); })
								.fail(function() { prv.savingFailed(); });
						}
					}
				},
				
				mouseOverSaveButton: function(eventData) {
					var me = this.me;
					me.showContextInfo(ns.ModelDesigner.prv.LABEL_SAVE_CONTEXT_INFO);
				},
				
				mouseLeftSaveButton: function(eventData) {
					var me = this.me;
					me.hideContextInfo();
				},
				
				jsPlumbCurrentlyDragging: function() {
					var prv = this;
					return prv.drawingQ.parents('.' + ns.ModelDesigner.prv.JS_PLUMB_DRAGGING_CLASS).length > 0;
				},
				
				beforePanEdgeMove: function(dragging) {
					var prv = this;
					return prv.jsPlumbCurrentlyDragging();
				}
			}];
		};
		
		ns.ModelDesigner.prototype.mine = function() {
			return this.prv[0];
		};
				
		ns.ModelDesigner.prototype.detachJspConnection = function(jspConnection) {
			var prv = this.mine();
			prv.ignoreConnectionDetached = true;
			prv.jsPlumbInstance.deleteConnection(jspConnection);
			prv.ignoreConnectionDetached = false;
		};
				
		ns.ModelDesigner.prototype.showModal = function(setUpHandler, modalOkHandler) {
			var prv = this.mine();
			prv.modalTitleQ.empty();
			prv.modalBodyQ.empty();
			prv.modalOkButtonQ.empty();
			prv.modalFooterQ.children().not(prv.modalOkButtonQ).remove();
			setUpHandler.apply(prv.modalQ, [prv.modalQ, prv.modalTitleQ, prv.modalBodyQ, prv.modalFooterQ, prv.modalOkButtonQ]);
			prv.modalOkHandler = modalOkHandler;
			prv.modalQ.modal('show');
		};
		
		ns.ModelDesigner.prototype.hideModal = function() {
			var prv = this.mine();
			prv.modalQ.modal('hide');
		};
		
		ns.ModelDesigner.prototype.showContextInfo = function(infoText) {
			var prv = this.mine();
			prv.contextInfoContainerQ.text(infoText);
		};
		
		ns.ModelDesigner.prototype.hideContextInfo = function() {
			var prv = this.mine();
			prv.contextInfoContainerQ.text(prv.contextInfoDefaultText);
		};
		
		ns.ModelDesigner.prototype.setContextInfoDefaultText = function(contextInfoDefaultText) { this.mine().contextInfoDefaultText = contextInfoDefaultText; };
		
		ns.ModelDesigner.prototype.clearContextInfoDefaultText = function() { this.mine().contextInfoDefaultText = ''; };
		
		ns.ModelDesigner.prototype.checkForCycle = function(replacedConnection, replacementSource, replacementTarget) {
			var prv = this.mine();
			
			if (prv.modelData.cyclesAllowed) return null;
			
			prv.setVisitMarkToAllNodes(0);
			
			var message = null;
			prv.processNodes(function(node) {
				var pathNodes = [];
				if (prv.reachesCycle(node, pathNodes, replacedConnection, replacementSource, replacementTarget)) {
					var cycleEnd = pathNodes[pathNodes.length - 1];
					var cycleString = cycleEnd.getExtendedTitleNotQuoted();
					for (var i = pathNodes.length - 2; i >= 0; --i) {
						var stepNode = pathNodes[i];
						cycleString = stepNode.getExtendedTitleNotQuoted() + ns.ModelDesigner.prv.LABEL_CYCLE_MESSAGE_GLUE + cycleString;
						if (stepNode.isSameNode(cycleEnd)) {
							break;
						}
					}
					
					message = ns.ModelDesigner.prv.LABEL_CYCLE_MESSAGE_START + cycleString + ns.ModelDesigner.prv.LABEL_CYCLE_MESSAGE_END;
					return false;
				}
				return true;
			});
			
			return message;
		};
		
		ns.ModelDesigner.prototype.checkForParallel = function(sourceNode, targetNode, changingConnection) {
			var prv = this.mine();
			
			if (prv.modelData.parallelsAllowed) return null;
			
			if (changingConnection != null
				&& changingConnection.getSourceNode().isSameNode(sourceNode)
				&& changingConnection.getTargetNode().isSameNode(targetNode)
			) {
				return null;
			}
			
			if (sourceNode.hasOutConnectionTo(targetNode)) {
				return ns.ModelDesigner.prv.LABEL_PARALLEL_MESSAGE;
			}
			
			return null;
		};
		
		ns.ModelDesigner.prototype.checkChangeConnectionAllowed = function(newSourceNode, newTargetNode, connection) {
			var me = this;
			
			if (!connection.getSourceNode().isSameNode(newSourceNode)) {
				if (!newSourceNode.isSelectableSourceNodeFor(connection.getTypeName())) {
					return ns.ModelDesigner.prv.LABEL_SOURCE_REJECTED_CONNECTION;
				}
			}
			
			if (!connection.getTargetNode().isSameNode(newTargetNode)) {
				if (!newTargetNode.isSelectableTargetNode()) {
					return ns.ModelDesigner.prv.LABEL_TARGET_REJECTED_CONNECTION;
				}
			}
			
			var parallelErrorMessage = me.checkForParallel(newSourceNode, newTargetNode, connection);
			if (parallelErrorMessage != null) {
				return parallelErrorMessage;
			}
			
			var cycleErrorMessage = me.checkForCycle(connection, newSourceNode, newTargetNode);
			if (cycleErrorMessage != null) {
				return cycleErrorMessage;
			}
			
			return null;
		};
		
		ns.ModelDesigner.prototype.getJsPlumbInstance = function() { return this.mine().jsPlumbInstance; };
		
		ns.ModelDesigner.prototype.changeConnectionEndpoints = function(connection, newSourceNode, newTargetNode) {
			var prv = this.mine();
			
			var oldKey = prv.getKeyForConnection(connection);
			prv.connectionKeys.splice(prv.connectionKeys.indexOf(oldKey), 1);
			delete prv.connectionByKey[oldKey];
			
			connection.getSourceNode().removeOutConnection(connection);
			connection.getTargetNode().removeInConnection(connection);
			
			connection.setSourceNode(newSourceNode);
			connection.setTargetNode(newTargetNode);
			connection.updateParams();
			
			var newKey = prv.getKeyForConnection(connection);
			
			newSourceNode.setOutConnection(connection);
			newTargetNode.setInConnection(connection);
			
			prv.connectionKeys.push(newKey);
			prv.connectionByKey[newKey] = connection;
		};
		
		ns.ModelDesigner.prototype.removeConnection = function(connection) {
			var prv = this.mine();
			
			var key = prv.getKeyForConnection(connection);
			var index = prv.connectionKeys.indexOf(key);
			
			if (index != -1) {
				delete prv.connectionByKey[key];
				prv.connectionKeys.splice(index, 1);
				
				connection.getSourceNode().removeOutConnection(connection);
				connection.getTargetNode().removeInConnection(connection);
			}
		};
		
		ns.ModelDesigner.prototype.removeNode = function(node, detachJspConnections) {
			var prv = this.mine();
			var me = this;
			
			var removedConnectionStack = [];
			
			node.processInConnections(function(inConnection) {
				removedConnectionStack.push(inConnection);
				return true;
			});
			while (removedConnectionStack.length > 0) {
				var removedConnection = removedConnectionStack.pop();
				me.removeConnection(removedConnection);
				if (detachJspConnections) {
					removedConnection.detachJspConnection();
				}
			}
			
			node.processOutConnections(function(outConnection) {
				removedConnectionStack.push(outConnection);
				return true;
			});
			while (removedConnectionStack.length > 0) {
				var removedConnection = removedConnectionStack.pop();
				me.removeConnection(removedConnection);
				if (detachJspConnections) {
					removedConnection.detachJspConnection();
				}
			}
			
			var nodeIdentifier = node.getNodeIdentifier();
			if (typeof prv.nodeByIdentifier[nodeIdentifier] != 'undefined') {
				delete prv.nodeByIdentifier[nodeIdentifier];
				prv.nodeIdentifiers.splice(prv.nodeIdentifiers.indexOf(nodeIdentifier), 1);
			}
			
			var nodeId = node.getId();
			if (nodeId != null && typeof prv.nodeById[ns.ModelDesigner.prv.NODE_ID_KEY_PREFIX + nodeId] != 'undefined') {
				delete prv.nodeById[ns.ModelDesigner.prv.NODE_ID_KEY_PREFIX + nodeId];
			}
			
			var nodeTempId = node.getTempId();
			if (nodeTempId != null && typeof prv.nodeByTempId[nodeTempId] != 'undefined') {
				delete prv.nodeByTempId[nodeTempId];
			}
		};
		
		ns.ModelDesigner.prototype.getNodeByIdentifier = function(nodeIdentifier, altReturn) {
			var prv = this.mine();
			return (typeof prv.nodeByIdentifier[nodeIdentifier] == 'undefined') ? altReturn : prv.nodeByIdentifier[nodeIdentifier];
		};
		
		ns.ModelDesigner.prototype.install = function(containerQ) {
			var prv = this.mine();
			
			prv.containerQ = containerQ;
			
			prv.contextInfoContainerQ = jQuery('<div></div>').addClass(ns.ModelDesigner.prv.CLASS_CONTEXT_INFO_CONTANER);
			prv.containerQ.append(prv.contextInfoContainerQ);
			
			var viewportQ = jQuery('<div></div>').addClass(ns.ModelDesigner.prv.CLASS_VIEWPORT);
			prv.containerQ.append(viewportQ);
			
			prv.drawingQ = jQuery('<div></div>').addClass(ns.ModelDesigner.prv.CLASS_DRAWING_CONTAINER);
			prv.drawingQ.click(function(eventData) { prv.drawingAreaClicked(eventData); });
			viewportQ.append(prv.drawingQ);
			
			prv.modelData = prv.containerQ.data(ns.ModelDesigner.prv.DATA_MODEL);
			
			var saveUrl = prv.containerQ.data(ns.ModelDesigner.prv.DATA_SAVE_URL);
			if (typeof saveUrl != 'undefined' && saveUrl != null && saveUrl != false && saveUrl != '') {
				prv.saveUrl = saveUrl;
			}
			
			prv.setUpJsPlumbInstance();
			prv.registerConnectionTypes();
			
			var controlsQ = jQuery('<div></div>').addClass(ns.ModelDesigner.prv.CLASS_CONTROLS_CONTAINER);
			prv.containerQ.append(controlsQ);
			
			var zoomControlsQ = jQuery('<div></div>').addClass(ns.ModelDesigner.prv.CLASS_ZOOM_CONTROLS);
			controlsQ.append(zoomControlsQ);
			
			var zoomInQ= jQuery('<button type="button" class="btn btn-default"></button>').addClass(ns.ModelDesigner.prv.CLASS_ZOOM_IN).text(ns.ModelDesigner.prv.LABEL_ZOOM_IN);
			zoomInQ.mouseover(function(eventData) { prv.mouseOverZoomInButton(eventData); });
			zoomInQ.mouseout(function(eventData) { prv.mouseLeftZoomInButton(eventData); });
			zoomControlsQ.append(zoomInQ);
			
			var zoomOutQ = jQuery('<button type="button" class="btn btn-default"></button>').addClass(ns.ModelDesigner.prv.CLASS_ZOOM_OUT).text(ns.ModelDesigner.prv.LABEL_ZOOM_OUT);
			zoomOutQ.mouseover(function(eventData) { prv.mouseOverZoomOutButton(eventData); });
			zoomOutQ.mouseout(function(eventData) { prv.mouseLeftZoomOutButton(eventData); });
			zoomControlsQ.append(zoomOutQ);
			
			var nodeInsertControls1Q = jQuery('<div></div>').addClass(ns.ModelDesigner.prv.CLASS_NODE_INSERT_CONTROLS);
			controlsQ.append(nodeInsertControls1Q);
			
			prv.nodeInsertDropupQ = jQuery('<div class="dropup"></div>');
			nodeInsertControls1Q.append(prv.nodeInsertDropupQ);
			
			prv.nodeInsertDropdownToggleQ = jQuery('<button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown"></button>').text(ns.ModelDesigner.prv.LABEL_INSERT_CONTROLS_TOGGLE);
			prv.nodeInsertDropdownToggleQ.mouseover(function(eventData) { prv.mouseOverNodeInsertToggleButton(eventData); });
			prv.nodeInsertDropdownToggleQ.mouseout(function(eventData) { prv.mouseLeftNodeInsertToggleButton(eventData); });
			prv.nodeInsertDropupQ.append(prv.nodeInsertDropdownToggleQ);
			
			var nodeInsertListQ = jQuery('<ul class="dropdown-menu"></ul>');
			prv.nodeInsertDropupQ.append(nodeInsertListQ);
			
			prv.installNodeInsertItems(nodeInsertListQ);
			
			var saveControlsQ = jQuery('<div></div>').addClass(ns.ModelDesigner.prv.CLASS_SAVE_CONTROLS);
			controlsQ.append(saveControlsQ);
			
			var saveButtonQ = jQuery('<button type="button" class="btn btn-default"></button>').addClass(ns.ModelDesigner.prv.CLASS_SAVE).text(ns.ModelDesigner.prv.LABEL_SAVE);
			saveButtonQ.click(function(eventData) { prv.saveButtonClicked(eventData); });
			saveButtonQ.mouseover(function(eventData) { prv.mouseOverSaveButton(eventData); });
			saveButtonQ.mouseout(function(eventData) { prv.mouseLeftSaveButton(eventData); });
			saveControlsQ.append(saveButtonQ);
			
			viewportQ.pan({
				mouseControl: 'edge',
				mouseEdgeSpeed: 20,
				mouseEdgeWidth: 30,
				beforeEdgeMove: function(dragging) { return prv.beforePanEdgeMove(dragging); }
			});
			
			
			var zoomFocal = {
				get clientX() {
					return viewportQ.position().left
						+ viewportQ.width() / 2
						- jQuery(document).scrollLeft()
						- parseFloat(prv.drawingQ.css('left'));
				},
				get clientY() {
					return viewportQ.position().top
						+ viewportQ.height() / 2
						- jQuery(document).scrollTop()
						- parseFloat(prv.drawingQ.css('top'));
				}
			};
			
			prv.drawingQ.panzoom({
				$zoomIn: zoomInQ,
				$zoomOut: zoomOutQ,
				focal: zoomFocal
			});
			prv.drawingQ.css('cursor', '');
			
			prv.installModel();
			
			prv.installModal();
		};
		
		ns.ModelDesigner.installAllEventually = function(startHandler, endHandler, beforeHandler, afterHandler, fieldFactorySetupHandler) {
			jsPlumb.ready(function() {
				jQuery(document).ready(function() {
					if (typeof startHandler == 'function') {
						startHandler.apply({}, []);
					}
					var instances = [];
					jQuery(ns.ModelDesigner.prv.SELECTOR_CONTAINER).each(function() {
						var fieldFactory = ns.ModelDesigner.prv.createDefaultFieldFactory();
						if (typeof fieldFactorySetupHandler == 'function') {
							fieldFactorySetupHandler.apply(fieldFactory, [fieldFactory]);
						}
						
						var containerQ = jQuery(this);
						var modelDesigner = new ns.ModelDesigner(fieldFactory);
						
						if (typeof beforeHandler == 'function') {
							beforeHandler.apply(containerQ, [modelDesigner, containerQ]);
						}
						
						modelDesigner.install(containerQ);
						instances.push(modelDesigner);
						
						if (typeof afterHandler == 'function') {
							afterHandler.apply(modelDesigner, [modelDesigner, containerQ]);
						}
					});
					if (typeof endHandler == 'function') {
						endHandler.apply({}, [instances]);
					}
				});
			});
		};
		
		ns.ModelDesigner.prv = {
			SELECTOR_CONTAINER: '.rgm-modes-container',
			CLASS_VIEWPORT: 'rgm-modes-viewport',
			CLASS_DRAWING_CONTAINER: 'rgm-modes-drawing-container',
			CLASS_CONTEXT_INFO_CONTANER: 'rgm-modes-context-info-container',
			CLASS_CONTROLS_CONTAINER: 'rgm-modes-controls-container',
			CLASS_ZOOM_CONTROLS: 'rgm-modes-zoom-controls',
			CLASS_ZOOM_IN: 'rgm-modes-zoom-in-btn',
			CLASS_ZOOM_OUT: 'rgm-modes-zoom-out-btn',
			CLASS_ZOOM_RESET: 'rgm-modes-zoom-reset-btn',
			CLASS_NODE_INSERT_CONTROLS: 'rgm-modes-node-insert-controls',
			CLASS_NODE_INSERT_ITEM_ICON: 'rgm-modes-node-insert-item-icon',
			CLASS_INSERTING_NODE: 'rgm-modes-inserting-node',
			CLASS_SAVE_CONTROLS: 'rgm-modes-save-controls',
			CLASS_SAVE: 'rgm-modes-save-btn',
			CLASS_SAVING_SPINNER: 'rgm-modes-saving-spinner',
			JS_PLUMB_DRAGGING_CLASS: 'jtk-drag-select',
			DATA_MODEL: 'model',
			DATA_SAVE_URL: 'saveurl',
			NODE_ID_KEY_PREFIX: 'node_',
			CLASS_PREFIX_CONNECTION_OVERLAY: 'rmg-modes-connection-overlay-',
			CLASS_PREFIX_INSERT_NODE_ITEM: 'rgm-modes-insert-node-item-',
			TPL_NODE_INVALID_CONFIRM_SAVE: ['The node ', 'extendedTitle', ' (', 'typeLabel', ')  is not configured correctly.\r\n\r\n', 'invalidMessage', '\r\n\r\nDo you want to save the model in an invalid state?'],
			ARG_EXTENDED_TITLE: 'extendedTitle',
			ARG_TYPE_LABEL: 'typeLabel',
			ARG_INVALID_MESSAGE: 'invalidMessage',
			LABEL_ZOOM_IN: '\uD83D\uDD0D+ Zoom In',
			LABEL_ZOOM_OUT: '\uD83D\uDD0D- Zoom Out',
			LABEL_INSERT_CONTROLS_TOGGLE: '\u271a Insert Node \u25B4',
			LABEL_SAVE: '\uD83D\uDCBE Save',
			LABEL_CYCLE_MESSAGE_START: 'The model is not allowed to be cyclic. The flowing cycle was detected: "',
			LABEL_CYCLE_MESSAGE_GLUE: '" \u2192 "',
			LABEL_CYCLE_MESSAGE_END: '".',
			LABEL_TARGET_REJECTED_CONNECTION: 'The new target rejected the connection.',
			LABEL_SOURCE_REJECTED_CONNECTION: 'The new source rejected the connection.',
			LABEL_PARALLEL_MESSAGE: 'Parallel connections are not allowed.',
			LABEL_NODE_INSERT_BUTTON_CONTEXT_INFO: 'Insert New Node (select the type, then click on drawing area)',
			LABEL_NODE_INSERT_CLICK_INSTRUCTION: 'Now click on the drawing area to place the node.',
			LABEL_SAVE_CONTEXT_INFO: 'Save Model',
			LABEL_SAVING_TITLE: 'Saving in Progress',
			LABEL_SAVING_BODY: 'The model is being saved.',
			LABEL_SAVING_MODAL_OK: 'OK',
			LABEL_SAVING_SUCCESS_TITLE: 'Model Saved',
			LABEL_SAVING_SUCCESS_BODY: 'The model was saved successfully.',
			LABEL_SAVING_FAILED_TITLE: 'Saving Failed',
			LABEL_SAVING_FAILED_BODY: 'The model could not be saved.',
			
			createDefaultFieldFactory: function() {
				var mapFieldFactory = new ns.MapFieldFactory();
				
				var textFieldFactory = new ns.TextFieldFactory();
				mapFieldFactory.putFactory(ns.TextField.TYPE_NAME, textFieldFactory);
				
				var checkboxFieldFactory = new ns.CheckboxFieldFactory();
				mapFieldFactory.putFactory(ns.CheckboxField.TYPE_NAME, checkboxFieldFactory);
				
				var subformsFieldFactory = new ns.SubformsFieldFactory(mapFieldFactory);
				mapFieldFactory.putFactory(ns.SubformsField.TYPE_NAME, subformsFieldFactory);
				
				return mapFieldFactory;
			}
		};
	}
})(window.rgm.modes, window);




(function(ns, rns) {
	'use strict';
	
	if (typeof rns.rgm == 'undefined') rns.rgm = {};
	if (typeof rns.rgm.modes == 'undefined') rns.rgm.modes = {};
	
	if (typeof rns.rgm.modes.ModelDesigner == 'undefined') {
		rns.rgm.modes.ModelDesigner = {
			installAllEventually: ns.ModelDesigner.installAllEventually
		};
	}
})(window.rgm.modes, window);
