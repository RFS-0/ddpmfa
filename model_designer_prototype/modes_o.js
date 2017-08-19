(function(a_e) {
	'use strict';
	if (typeof a_e.snOoPy == 'undefined') a_e.snOoPy = {};
	if (typeof a_e.snOoPy.SNooPY == 'undefined') a_e.snOoPy.SNooPY = {};
})(window);




(function(a_d, a_e) {
	'use strict';
	if (typeof a_d.a_6 == 'undefined') {
		a_d.a_6 = function() {
			this.a_y = [{
				a_bn: this,
				a_fa: a_d.a_6.a_y.a_e8,
				a_e9: -1
			}];
		};
		
		a_d.a_6.prototype.a_O = function() { return this.a_y[0]; };
		
		a_d.a_6.prototype.a_4 = function() {
			var a_y = this.a_O();
			
			if (a_y.a_e9 + 1 > a_d.a_6.a_e6) {
				a_y.a_e9 = 0;
				a_y.a_fa += a_d.a_6.a_e7;
			} else {
				++a_y.a_e9;
			}
			
			return a_y.a_fa + a_y.a_e9;
		};
		
		a_d.a_6.a_y = {
			a_e8: 'u',
			a_e7: 'x',
			a_e6: 999999999,
			a_e5: null
		};
		
		a_d.a_6.a_5 = function() {
			if (a_d.a_6.a_y.a_e5 == null) {
				a_d.a_6.a_y.a_e5 = new a_d.a_6();
			}
			return a_d.a_6.a_y.a_e5;
		};
	}
})(window.snOoPy.SNooPY, window);




(function(a_d, a_e) {
	'use strict';
	if (typeof a_d.a_cj == 'undefined') {
		a_d.a_cj = function(a_e4) {
			this.a_y = [{
				a_bn: this,
				a_e4: a_e4
			}];
		};
		
		a_d.a_cj.prototype.a_O = function() { return this.a_y[0]; };
		
		a_d.a_cj.prototype.a_ch = function(a_eJ) {
			var a_y = this.a_O();
			var a_e2 = '';
			for (var a_be = 0; a_be < a_y.a_e4.length; ++a_be) {
				var a_e3 = a_y.a_e4[a_be];
				if (a_be % 2 == 0) {
					a_e2 += a_e3;
				} else {
					if (typeof a_eJ[a_e3] != 'undefined') {
						a_e2 += a_eJ[a_e3];
					}
				}
			}
			return a_e2;
		};
	}
})(window.snOoPy.SNooPY, window);




(function(a_d, a_e) {
	'use strict';
	if (typeof a_d.a_ek == 'undefined') {
		a_d.a_ek = function(a_eY, a_eW, a_eS) {
			this.a_y = [{
				a_bn: this,
				
				a_eY: a_eY,
				a_eW: a_eW,
				a_eS: a_eS,
				
				a_eT: (a_eW ? 1 : (-1)) * a_eY,
				a_eU: a_eW ? 1 : (-1),
				
				a_eV: function(a_e0, a_eZ, a_e1) {
					return a_e0 > a_eZ || (a_e1 && a_e0 == a_eZ);
				}
			}];
		};
		
		a_d.a_ek.prototype.a_O = function() { return this.a_y[0]; };
		
		a_d.a_ek.prototype.a_eO = function() { return this.a_O().a_eY; };
		
		a_d.a_ek.prototype.a_eX = function() { return this.a_O().a_eW; };
		
		a_d.a_ek.prototype.a_eL = function() { return this.a_O().a_eS; };
		
		a_d.a_ek.prototype.a_ez = function(a_dC) {
			var a_y = this.a_O();
			return a_y.a_eV(a_y.a_eU * a_dC, a_y.a_eT, a_y.a_eS);
		};
	}
})(window.snOoPy.SNooPY, window);




(function(a_d, a_e) {
	'use strict';
	if (typeof a_d.a_ed == 'undefined') {
		a_d.a_ed = function(a_eD, a_ei, a_eh) {
			this.a_y = [{
				a_bn: this,
				a_eD: a_eD,
				a_ei: a_ei,
				a_eh: a_eh,
				
				a_eR: null,
				a_eP: null,
				a_eI: null,
				a_eG: null,
				
				a_eN: function(a_dC) {
					return a_dC ? a_d.a_ed.a_y.a_em : a_d.a_ed.a_y.a_el;
				},
				
				a_ew: function(a_dC) {
					var a_y = this;
					if (a_y.a_eR == null) {
						a_y.a_eR = new a_d.a_cj(a_d.a_ed.a_y.a_ev.slice());
					}
					var a_eJ = {};
					a_eJ[a_d.a_ed.a_y.a_eo] = a_dC;
					return a_y.a_eR.a_ch(a_eJ);
				},
				
				a_eC: function(a_eQ) {
					var a_y = this;
					if (a_y.a_eP == null) {
						a_y.a_eP = new a_d.a_cj(a_d.a_ed.a_y.a_eu.slice());
					}
					var a_eJ = {};
					a_eJ[a_d.a_ed.a_y.a_eq] = a_eQ;
					a_eJ[a_d.a_ed.a_y.a_er] = a_y.a_eD;
					return a_y.a_eP.a_ch(a_eJ);
				},
				
				a_eH: function(a_eK, a_dC, a_eM) {
					var a_y = this;
					var a_eJ = {};
					a_eJ[a_d.a_ed.a_y.a_eo] = a_dC;
					a_eJ[a_d.a_ed.a_y.a_ep] = a_eM.a_eO();
					a_eJ[a_d.a_ed.a_y.a_en] = a_y.a_eN(a_eM.a_eL());
					return a_eK.a_ch(a_eJ);
				},
				
				a_eA: function(a_dC) {
					var a_y = this;
					if (a_y.a_eI == null) {
						a_y.a_eI = new a_d.a_cj(a_d.a_ed.a_y.a_et.slice());
					}
					return a_y.a_eH(a_y.a_eI, a_dC, a_y.a_ei);
				},
				
				a_ex: function(a_dC) {
					var a_y = this;
					if (a_y.a_eG == null) {
						a_y.a_eG = new a_d.a_cj(a_d.a_ed.a_y.a_es.slice());
					}
					return a_y.a_eH(a_y.a_eG, a_dC, a_y.a_eh);
				}
			}];
		};
		
		a_d.a_ed.prototype.a_O = function() { return this.a_y[0]; };
		
		a_d.a_ed.prototype.a_bZ = function(a_d9) {
			var a_y = this.a_O();
			
			var a_eF = (new RegExp('^-?(0|[1-9][0-9]*)(\\.[0-9]+)?$')).exec(a_d9);
			var a_eE = 2;
			if (a_eF) {
				var a_eB = 0;
				if (a_eF[a_eE]) {
					a_eB = a_eF[a_eE].length - 1;
				}
				if (a_y.a_eD >= 0 && a_eB > a_y.a_eD) {
					return a_y.a_eC(a_eB);
				}
				
				var a_ey = Number.parseFloat(a_d9);
				
				if (a_y.a_ei != null && !a_y.a_ei.a_ez(a_ey)) {
					return a_y.a_eA(a_d9);
				}
				if (a_y.a_eh != null && !a_y.a_eh.a_ez(a_ey)) {
					return a_y.a_ex(a_d9);
				}
				
			} else {
				return a_y.a_ew(a_d9);
			}
		};
		
		a_d.a_ed.a_y = {
			a_ev: ['The value "', 'foundValue', '" is not a correctly formatted number.'],
			a_eu: ['This value has too many decimals. The maximum allowed is ', 'maxDecimals', '. ', 'foundDecimals', ' was/were found.'],
			a_et: ['The value ', 'foundValue', ' is too small. The minimum value is ', 'referenceValue', ' (inclusive: ', 'inclusiveYesOrNo', ').'],
			a_es: ['The value ', 'foundValue', ' is too large. The maximum value is ', 'referenceValue', ' (inclusive: ', 'inclusiveYesOrNo', ').'],
			a_er: 'maxDecimals',
			a_eq: 'foundDecimals',
			a_ep: 'referenceValue',
			a_eo: 'foundValue',
			a_en: 'inclusiveYesOrNo',
			a_em: 'yes',
			a_el: 'no'
		};
		
		a_d.a_ed.a_ec = function(a_ej) {
			var a_ei = null;
			if (typeof a_ej['min'] != 'undefined' && a_ej.min != null) {
				a_ei = new a_d.a_ek(a_ej.min.value, true, a_ej.min.inclusive);
			}
			
			var a_eh = null;
			if (typeof a_ej['max'] != 'undefined' && a_ej.max != null) {
				a_eh = new a_d.a_ek(a_ej.max.value, false, a_ej.max.inclusive);
			}
			
			return new a_d.a_ed(a_ej.decimals, a_ei, a_eh);
		};
	}
})(window.snOoPy.SNooPY, window);




(function(a_d, a_e) {
	'use strict';
	if (typeof a_d.a_r == 'undefined') {
		a_d.a_r = function() {
			this.a_y = [{
				a_bn: this,
				a_ef: {}
			}];
		};
		
		a_d.a_r.prototype.a_O = function() { return this.a_y[0]; };
		
		a_d.a_r.prototype.a_j = function(a_cV, a_eg) {
			this.a_O().a_ef[a_cV] = a_eg;
		};
		
		a_d.a_r.prototype.a_ee = function(a_cV, a_cH, a_bM, a_cI, a_cU, a_cS) {
			var a_y = this.a_O();
			if (typeof a_y.a_ef[a_cV] == 'undefined') {
				throw 'Unknown field type "' + a_cV + '" in a_r.a_ee(...)';
			}
			return a_y.a_ef[a_cV].a_ee(a_cV, a_cH, a_bM, a_cI, a_cU, a_cS);
		};
		
		a_d.a_r.prototype.a_bQ = function(a_cP) {
			return this.a_ee(a_cP.fieldType, a_cP.fieldArgs, a_cP.propName, a_cP.label, a_cP.valueData, a_cP.dirty);
		};
	}
})(window.snOoPy.SNooPY, window);




(function(a_d, a_e) {
	'use strict';
	if (typeof a_d.a_q == 'undefined') {
		a_d.a_q = function() {
			this.a_y = [{ a_bn: this }];
		};
		
		a_d.a_q.prototype.a_O = function() { return this.a_y[0]; };
		
		a_d.a_q.prototype.a_ee = function(a_cV, a_cH, a_bM, a_cI, a_cU, a_cS) {
			return new a_d.a_p(a_cV, a_cH, a_bM, a_cI, a_cU, a_cS);
		};
		
		a_d.a_q.prototype.a_bQ = function(a_cP) {
			return this.a_ee(a_cP.fieldType, a_cP.fieldArgs, a_cP.propName, a_cP.label, a_cP.valueData, a_cP.dirty);
		};
	}
})(window.snOoPy.SNooPY, window);




(function(a_d, a_e) {
	'use strict';
	if (typeof a_d.a_n == 'undefined') {
		a_d.a_n = function() {
			this.a_y = [{ a_bn: this }];
		};
		
		a_d.a_n.prototype.a_O = function() { return this.a_y[0]; };
		
		a_d.a_n.prototype.a_ee = function(a_cV, a_cH, a_bM, a_cI, a_cU, a_cS) {
			return new a_d.a_m(a_cV, a_cH, a_bM, a_cI, a_cU, a_cS);
		};
		
		a_d.a_n.prototype.a_bQ = function(a_cP) {
			return this.a_ee(a_cP.fieldType, a_cP.fieldArgs, a_cP.propName, a_cP.label, a_cP.valueData, a_cP.dirty);
		};
	}
})(window.snOoPy.SNooPY, window);




(function(a_d, a_e) {
	'use strict';
	if (typeof a_d.a_k == 'undefined') {
		a_d.a_k = function(a_bo) {
			this.a_y = [{
				a_bn: this,
				a_bo: a_bo
			}];
		};
		
		a_d.a_k.prototype.a_O = function() { return this.a_y[0]; };
		
		a_d.a_k.prototype.a_ee = function(a_cV, a_cH, a_bM, a_cI, a_cU, a_cS) {
			var a_y = this.a_O();
			return new a_d.a_i(a_y.a_bo, a_cV, a_cH, a_bM, a_cI, a_cU, a_cS);
		};
		
		a_d.a_k.prototype.a_bQ = function(a_cP) {
			return this.a_ee(a_cP.fieldType, a_cP.fieldArgs, a_cP.propName, a_cP.label, a_cP.valueData, a_cP.dirty);
		};
	}
})(window.snOoPy.SNooPY, window);




(function(a_d, a_e) {
	'use strict';
	if (typeof a_d.a_p == 'undefined') {
		a_d.a_p = function(a_cV, a_cH, a_bM, a_cI, a_cU, a_cS) {
			this.a_y = [{
				a_bn: this,
				a_cV: a_cV,
				a_cH: a_cH,
				a_bM, a_bM,
				a_cI: a_cI,
				a_dI: a_cU,
				a_dC: a_cU,
				a_cT: a_cS,
				
				a_dY: null,
				a_dB: null,
				a_dX: null,
				
				a_ea: null,
				
				a_eb: function() {
					var a_y = this;
					if (a_y.a_cH.numberConfig == null) return null;
					if (a_y.a_ea == null) {
						a_y.a_ea = a_d.a_ed.a_ec(a_y.a_cH.numberConfig);
					}
					return a_y.a_ea;
				},
				
				a_dT: function(a_d9) {
					var a_y = this;
					var a_ea = a_y.a_eb();
					return a_ea == null ? null : a_ea.a_bZ(a_d9);
				},
				
				a_d5: function(a_d4) {
					return a_d.a_p.a_y.a_dK + a_d4 + a_d.a_p.a_y.a_dJ;
				},
				
				a_d0: function(a_b7) {
					var a_y = this;
					a_b7.removeClass(a_y.a_d5(a_d.a_p.a_y.a_d8)).removeClass(a_y.a_d5(a_d.a_p.a_y.a_d7)).removeClass(a_y.a_d5(a_d.a_p.a_y.a_d6));
				},
				
				a_d1: function(a_dU, a_d4) {
					var a_y = this;
					if (a_y.a_dY != null) {
						a_y.a_d0(a_y.a_dY);
						a_y.a_dY.addClass(a_y.a_d5(a_d4));
						
						if (a_y.a_dX == null) {
							a_y.a_dX = jQuery('<span class="help-block"></span>');
							a_y.a_dY.append(a_y.a_dX);
						}
						a_y.a_dX.text(a_dU);
					}
				},
				
				a_dS: function(a_dU) {
					this.a_d1(a_dU, a_d.a_p.a_y.a_dN);
				},
				
				a_d3: function(a_dU) {
					this.a_d1(a_dU, a_d.a_p.a_y.a_dM);
				},
				
				a_d2: function(a_dU) {
					this.a_d1(a_dU, a_d.a_p.a_y.a_dL);
				},
				
				a_dV: function() {
					var a_y = this;
					if (a_y.a_dY != null) {
						a_y.a_d0(a_y.a_dY);
						
						if (a_y.a_dX != null) {
							a_y.a_dX.remove();
							a_y.a_dX = null;
						}
					}
				},
			}];
		};
		
		a_d.a_p.prototype.a_O = function() { return this.a_y[0]; };
		
		a_d.a_p.prototype.a_b1 = function(a_bT) {
			var a_y = this.a_O();
			var a_dZ = a_d.a_6.a_5().a_4();
			var a_dY = jQuery('<div class="form-group"></div>');
			var a_dE = jQuery('<label class="control-label"></label>')
				.attr('for', a_dZ)
				.text(a_y.a_cI);
			var a_dB = a_y.a_cH.displayAsTextArea
				? a_dB = jQuery('<textarea class="form-control"></textarea>')
				: a_dB = jQuery('<input type="text" class="form-control" />');
			a_dB
				.attr('id', a_dZ)
				.val(a_y.a_dC);
			a_dY.append(a_dE);
			a_dY.append(a_dB);
			a_bT.append(a_dY);
			
			a_y.a_dY = a_dY;
			a_y.a_dB = a_dB;
		};
		
		a_d.a_p.prototype.a_cx = function() {
			var a_y = this.a_O();
			a_y.a_dY = null;
			a_y.a_dB = null;
			a_y.a_dX = null;
		};
		
		a_d.a_p.prototype.a_bD = function() {
			var a_y = this.a_O();
			a_y.a_dC = a_y.a_dB.val();
		};
		
		a_d.a_p.prototype.a_cf = function() {
			var a_y = this.a_O();
			var a_dW = {
				fieldType: a_y.a_cV,
				fieldArgs: a_y.a_cH,
				propName: a_y.a_bM,
				label: a_y.a_cI,
				valueData: a_y.a_dC,
				dirty: this.a_cw()
			};
			return a_dW;
		};
		
		a_d.a_p.prototype.a_cw = function() {
			var a_y = this.a_O();
			return a_y.a_cT || a_y.a_dC != a_y.a_dI;
		};
		
		a_d.a_p.prototype.a_cv = function(a_cu) {
			var a_y = this.a_O();
			a_y.a_cT = false;
			a_y.a_dI = a_y.a_dC;
		};
		
		a_d.a_p.prototype.a_bZ = function() {
			var a_y = this.a_O();
			a_y.a_dV();
			if (a_y.a_cH.notEmpty && a_y.a_dC.length == 0) {
				var a_dU = a_d.a_p.a_y.a_dQ;
				a_y.a_dS(a_dU);
				return a_dU;
			}
			if (a_y.a_cH.maxLength != -1 && a_y.a_dC.length > a_y.a_cH.maxLength) {
				var a_dU = a_d.a_p.a_y.a_dP + a_y.a_cH.maxLength + a_d.a_p.a_y.a_dO;
				a_y.a_dS(a_dU);
				return a_dU;
			}
			
			var a_dR = a_y.a_dT(a_y.a_dC);
			if (a_dR != null) {
				a_y.a_dS(a_dR);
				return a_dR;
			}
			
			return null;
		};
		
		a_d.a_p.a_y = {
			a_dQ: 'This field can not be empty',
			a_dP: 'This field can contain no more than ',
			a_dO: ' characters.',
			a_dN: 'error',
			a_dM: 'warning',
			a_dL: 'success',
			a_dK: 'has-',
			a_dJ: ''
		};
		
		a_d.a_p.a_h = 'TEXT';
	}
})(window.snOoPy.SNooPY, window);




(function(a_d, a_e) {
	'use strict';
	if (typeof a_d.a_m == 'undefined') {
		a_d.a_m = function(a_cV, a_cH, a_bM, a_cI, a_cU, a_cS) {
			this.a_y = [{
				a_bn: this,
				a_cV: a_cV,
				a_cH: a_cH,
				a_bM, a_bM,
				a_cI: a_cI,
				a_dI: a_cU,
				a_dC: a_cU,
				a_cT: a_cS,
				
				a_dB: null,
				
				a_dD: function(a_dF, a_dH) {
					a_dF.prop('checked', a_dH);
				},
				
				a_dG: function(a_dF) {
					return a_dF.is(':checked');
				}
			}];
		};
		
		a_d.a_m.prototype.a_O = function() {
			return this.a_y[0];
		};
		
		a_d.a_m.prototype.a_b1 = function(a_bT) {
			var a_y = this.a_O();
			
			var a_B = jQuery('<div class="checkbox"></div>');
			a_bT.append(a_B);
			
			var a_dE = jQuery('<label></label>').text(a_y.a_cI);
			a_B.append(a_dE);
			
			a_y.a_dB = jQuery('<input type="checkbox" />');
			a_B.prepend(a_y.a_dB);
			
			a_y.a_dD(a_y.a_dB, a_y.a_dC);
		};
		
		a_d.a_m.prototype.a_cx = function() {
			var a_y = this.a_O();
			a_y.a_dB = null;
		};
		
		a_d.a_m.prototype.a_bD = function() {
			var a_y = this.a_O();
// TODO
		};
		
		a_d.a_m.prototype.a_cf = function() {
			var a_y = this.a_O();
// TODO
		};
		
		a_d.a_m.prototype.a_cw = function() {
			var a_y = this.a_O();
// TODO
		};
		
		a_d.a_m.prototype.a_cv = function(a_cu) {
			var a_y = this.a_O();
// TODO
		};
		
		a_d.a_m.prototype.a_bZ = function() {
			var a_y = this.a_O();
// TODO
			return null;
		};
		
		a_d.a_m.a_h = 'CHECK';
	}
})(window.snOoPy.SNooPY, window);




(function(a_d, a_e) {
	'use strict';
	if (typeof a_d.a_cl == 'undefined') {
		a_d.a_cl = function(a_dj, a_bW, a_cI, a_bO) {
			this.a_y = [{
				a_bn: this,
				a_dj: a_dj,
				a_bW: a_bW,
				a_cI: a_cI,
				a_bO: a_bO,
				
				a_cL: null,
				a_c5: null,
				a_B: null,
				a_c4: null,
				a_c3: null,
				
				a_c9: function() {
					return jQuery('<div class="panel panel-default"></div>').addClass(a_d.a_cl.a_y.a_bC);
				},
				
				a_c7: function() {
					var a_y = this;
					
					var a_bI = jQuery('<div class="panel-heading"></div>').addClass(a_d.a_cl.a_y.a_bB).text(a_y.a_cI);
					a_y.a_B.append(a_bI);
					
					var a_cC = jQuery('<div class="panel-body"></div>').addClass(a_d.a_cl.a_y.a_cs);
					a_y.a_B.append(a_cC);
					
					var a_dx = jQuery('<div class="btn-group"></div>').addClass(a_d.a_cl.a_y.a_c2);
					a_cC.append(a_dx);
					
					var a_dz = jQuery('<button class="btn btn-default"></button>').addClass(a_d.a_cl.a_y.a_dA).text(a_d.a_cl.a_y.a_cX);
					a_dx.append(a_dz);
					a_y.a_c4 = a_dz;
					a_dz.click(function() { a_y.a_do(); });
					
					var a_dw  = jQuery('<button class="btn btn-default"></button>').addClass(a_d.a_cl.a_y.a_dy).text(a_d.a_cl.a_y.a_cW);
					a_dx.append(a_dw);
					a_y.a_c3 = a_dw;
					a_dw.click(function() { a_y.a_dn(); });
					
					a_y.a_bn.a_cN();
					
					var a_dv = jQuery('<div></div>').addClass(a_d.a_cl.a_y.a_cY);
					a_cC.append(a_dv);
					
					for (var a_be = 0; a_be < a_y.a_bO.length; ++a_be) {
						a_y.a_bO[a_be].a_b1(a_dv);
					}
				},
				
				a_dm: function(a_du) {
					var a_y = this;
					
					if (a_du) {
						if (a_y.a_cL != null) {
							var a_dt = a_y.a_cL;
							var a_ds = a_dt.a_df();
							var a_dr = a_y.a_c5;
							
							a_y.a_B.insertBefore(a_dt.a_dd());
							
							a_y.a_bn.a_cM(a_ds);
							a_y.a_bn.a_cO(a_dt);
							
							a_dt.a_cM(a_y.a_bn);
							a_dt.a_cO(a_dr);
							
							a_y.a_bn.a_cN();
							a_dt.a_cN();
							
							if (a_ds != null) {
								a_ds.a_cO(a_y.a_bn);
								a_ds.a_cN();
							}
							
							if (a_dr != null) {
								a_dr.a_cM(a_dt);
								a_dr.a_cN();
							}
						}
					} else {
						if (a_y.a_c5 != null) {
							var a_dt = a_y.a_c5;
							var a_ds = a_y.a_cL;
							var a_dr = a_dt.a_de();
							
							a_y.a_B.insertAfter(a_dt.a_dd());
							
							a_y.a_bn.a_cM(a_dt);
							a_y.a_bn.a_cO(a_dr);
							
							a_dt.a_cM(a_ds);
							a_dt.a_cO(a_y.a_bn);
							
							a_y.a_bn.a_cN();
							a_dt.a_cN();
							
							if (a_ds != null) {
								a_ds.a_cO(a_dt);
								a_ds.a_cN();
							}
							
							if (a_dr != null) {
								a_dr.a_cM(a_y.a_bn);
								a_dr.a_cN();
							}
						}
					}
				},
				
				a_c6: function(a_dp, a_dq) {
					if (a_dq) {
						a_dp.removeClass('disabled');
					} else {
						a_dp.addClass('disabled');
					}
				},
				
				a_do: function() {
					this.a_dm(true);
				},
				
				a_dn: function() {
					this.a_dm(false);
				}
			}]
		};
		
		a_d.a_cl.prototype.a_O = function() { return this.a_y[0]; };
		
		a_d.a_cl.prototype.a_dl = function(a_dj) { this.a_O().a_dj = a_dj; };
		
		a_d.a_cl.prototype.a_dk = function() { return this.a_O().a_dj; };
		
		a_d.a_cl.prototype.a_bX = function(a_bW) { this.a_O().a_bW = a_bW; };
		
		a_d.a_cl.prototype.a_di = function() { return this.a_O().a_bW; };
		
		a_d.a_cl.prototype.a_dh = function() { return this.a_O().a_cI; };
		
		a_d.a_cl.prototype.a_dg = function() { return this.a_O().a_bO; };
		
		a_d.a_cl.prototype.a_cM = function(a_cL) { this.a_O().a_cL = a_cL; };
		
		a_d.a_cl.prototype.a_df = function() { return this.a_O().a_cL; };
		
		a_d.a_cl.prototype.a_cO = function(a_c5) { this.a_O().a_c5 = a_c5; };
		
		a_d.a_cl.prototype.a_de = function() { return this.a_O().a_c5; };
		
		a_d.a_cl.prototype.a_dd = function() {
			return this.a_O().a_B;
		};
		
		a_d.a_cl.prototype.a_cA = function(a_bT) {
			var a_y = this.a_O();
			a_y.a_B = a_y.a_c9();
			a_bT.append(a_y.a_B);
			a_y.a_c7();
		};
		
		a_d.a_cl.prototype.a_dc = function(a_db) {
			var a_y = this.a_O();
			a_y.a_B = a_y.a_c9();
			a_y.a_B.insertBefore(a_db);
			a_y.a_c7();
		};
		
		a_d.a_cl.prototype.a_da = function(a_c8) {
			var a_y = this.a_O();
			a_y.a_B = a_y.a_c9();
			a_y.a_B.insertAfter(a_c8);
			a_y.a_c7();
		};
		
		a_d.a_cl.prototype.a_cN = function() {
			var a_y = this.a_O();
			a_y.a_c6(a_y.a_c4, a_y.a_cL != null);
			a_y.a_c6(a_y.a_c3, a_y.a_c5 != null);
		};
		
		a_d.a_cl.prototype.a_cx = function() {
			var a_y = this.a_O();
			a_y.a_B = null;
			a_y.a_c4 = null;
			a_y.a_c3 = null;
		};
		
		a_d.a_cl.prototype.a_cf = function() {
// TODO
		};
		
		a_d.a_cl.a_y = {
			a_bC: 'rgm-modes-subform-container',
			a_bB: 'rgm-modes-subform-title',
			a_cs: 'rgm-modes-subform-content',
			a_c2: 'rgm-modes-subform-move-btns',
			a_c1: 'rgm-modes-subform-move-btn',
			a_c0: 'rgm-modes-subform-up-btn',
			a_cZ: 'rgm-modes-subform-down-btn',
			a_cY: 'rgm-modes-subform-fields',
			a_cX: '\u25B2',
			a_cW: '\u25BC'
		};
	}

})(window.snOoPy.SNooPY, window);




(function(a_d, a_e) {
	'use strict';
	if (typeof a_d.a_i == 'undefined') {
		a_d.a_i = function(a_bo, a_cV, a_cH, a_bM, a_cI, a_cU, a_cS) {
// TODO: remove subforms
			this.a_y = [{
				a_bn: this,
				a_bo: a_bo,
				a_cV: a_cV,
				a_cH: a_cH,
				a_bM, a_bM,
				a_cI: a_cI,
				a_cR: a_cU,
				a_cT: a_cS,
				
				a_cz: null,
				a_cB: [],
				a_cK: {},
				
				a_cJ: function() {
					var a_y = this;
					
					var a_cL = null;
					for (var a_be = 0; a_be < a_y.a_cR.length; ++a_be) {
						var a_cF = a_y.a_cR[a_be];
						
						var a_bO = [];
						for (var a_cQ = 0; a_cQ < a_cF.fields.length; ++a_cQ) {
							var a_cP = a_cF.fields[a_cQ];
							var a_bL = a_y.a_bo.a_bQ(a_cP);
							a_bO.push(a_bL);
						}
						
						var a_cy = new a_d.a_cl(a_cF.id, a_cF.tempId, a_cF.label, a_bO);
						
						if (a_be > 0) {
							a_cy.a_cM(a_cL);
							a_cL.a_cO(a_cy);
						}
						
						a_y.a_cB.push(a_cy);
						a_cL = a_cy;
					}
				},
				
				a_cG: function(a_cF) {
					var a_y = this;
					
					var a_bW = a_d.a_i.a_y.a_cm + a_d.a_6.a_5().a_4();
					
					var a_bO = [];
					for (var a_be = 0; a_be < a_cF.fields.length; ++a_be) {
						var a_cP = a_cF.fields[a_be];
						var a_bL = a_y.a_bo.a_bQ(a_cP);
						a_bO.push(a_bL);
					}
					
					var a_cy = new a_d.a_cl(a_cF.id, a_bW, a_cF.label, a_bO);
					
					if (a_y.a_cB.length > 0) {
						var a_cL = a_y.a_cB[a_y.a_cB.length - 1];
						a_cL.a_cO(a_cy);
						a_cL.a_cN();
						a_cy.a_cM(a_cL);
					}
					
					a_cy.a_cA(a_y.a_cz);
					
					a_y.a_cB.push(a_cy);
					a_y.a_cK[a_bW] = a_cy;
				}
			}];
			this.a_y[0].a_cJ();
		};
		
		a_d.a_i.prototype.a_O = function() { return this.a_y[0]; };
		
		a_d.a_i.prototype.a_b1 = function(a_bT) {
			var a_y = this.a_O();
			var a_be = 0;
			
			var a_B = jQuery('<div class="panel panel-default"></div>').addClass(a_d.a_i.a_y.a_bC);
			a_bT.append(a_B);
			
			var a_bI = jQuery('<div class="panel-heading"></div>').addClass(a_d.a_i.a_y.a_bB);
			a_bI.text(a_y.a_cI);
			a_B.append(a_bI);
			
			var a_cC = jQuery('<div class="panel-body"></div>').addClass(a_d.a_i.a_y.a_cs);
			a_B.append(a_cC);
			
			var a_cE = jQuery('<div class="btn-group-vertical"></div>').addClass(a_d.a_i.a_y.a_cr);
			a_cC.append(a_cE);
			
			for (a_be = 0; a_be < a_y.a_cH.forms.length; ++a_be) {(function(a_be) {
				var a_cF = a_y.a_cH.forms[a_be];
				
				var a_cD = jQuery('<button class="btn btn-default"></button>').addClass(a_d.a_i.a_y.a_cq).text(a_d.a_i.a_y.a_co + a_cF.label + a_d.a_i.a_y.a_cn);
				a_cD.click(function() { a_y.a_cG(a_cF); });
				a_cE.append(a_cD);
			})(a_be);}
			
			var a_cz = jQuery('<div></div>').addClass(a_d.a_i.a_y.a_cp);
			a_cC.append(a_cz);
			
			for (a_be = 0; a_be < a_y.a_cB.length; ++a_be) {
				var a_cy = a_y.a_cB[a_be];
				a_cy.a_cA(a_cz);
			}
			
			a_y.a_cz = a_cz;
		};
		
		a_d.a_i.prototype.a_cx = function() {
			var a_y = this.a_O();
			a_y.a_cz = null;
			for (a_be = 0; a_be < a_y.a_cB.length; ++a_be) {
				var a_cy = a_y.a_cB[a_be];
				a_cy.a_cA(a_cz);
				a_cy.a_cx();
			}
		};
		
		a_d.a_i.prototype.a_bD = function() {
			var a_y = this.a_O();
// TODO
		};
		
		a_d.a_i.prototype.a_cf = function() {
			var a_y = this.a_O();
// TODO
		};
		
		a_d.a_i.prototype.a_cw = function() {
			var a_y = this.a_O();
// TODO
		};
		
		a_d.a_i.prototype.a_cv = function(a_cu) {
			var a_y = this.a_O();
// TODO
		};
		
		a_d.a_i.prototype.a_bZ = function() {
			var a_y = this.a_O();
// TODO
		};
		
		a_d.a_i.a_y = {
			a_bC: 'rgm-modes-forms-field-container',
			a_ct: 'rgm-modes-forms-field-title',
			a_cs: 'rgm-modes-forms-field-content',
			a_cr: 'rgm-modes-forms-field-add-buttons',
			a_cq: 'rgm-modes-forms-field-add-button',
			a_cp: 'rgm-modes-forms-field-forms',
			a_co: 'Add new ',
			a_cn: '',
			a_cm: 'temp_'
		};
		
		a_d.a_i.a_h = 'FORMS';
	}
})(window.snOoPy.SNooPY, window);




(function(a_d, a_e) {
	'use strict';
	
	if (typeof a_d.a_bq == 'undefined') {
		a_d.a_bq = function(a_bp, a_bi, a_bo, a_C, a_bH) {
// TODO (Could): a_bq should work like a_cl: unpack/repack a_bp
			this.a_y = [{
				a_bn: this,
				a_bp: a_bp,
				a_bi: a_bi,
				a_bo: a_bo,
				a_C: a_C,
				a_bH: a_bH,
				
				a_B: null,
				a_bI: null,
				
				a_bO: [],
				a_b3: {},
				
				a_ba: null,
				
				a_ci: null,
				
				a_b0: function(a_bJ) {
					var a_y = this;
					if (a_y.a_ck == null) {
						a_y.a_ci = new a_d.a_cj(a_d.a_bq.a_y.a_bx);
					}
					var a_cg ={};
					a_cg[a_d.a_bq.a_y.a_bw] = a_bJ;
					return a_y.a_ci.a_ch(a_cg);
				},
				
				a_cb: function(a_ce, a_b4) {
					var a_y = this;
					var a_bL = a_y.a_b5(a_ce[0], null);
					if (a_bL == null) return a_b4;
					var a_cc = a_bL.a_cf();
					for (var a_be = 1; a_be < a_ce.length; ++a_be) {
						var a_cd = a_ce[a_be];
						if (typeof a_cc[a_cd] == 'undefined') {
							return a_b4;
						}
						a_cc = a_cc[a_cd];
					}
					return a_cc;
				},
				
				a_bY: function() {
					var a_y = this;
					a_y.a_bI.text(a_y.a_bK());
				},
				
				a_bK: function() {
					var a_y = this;
					return a_y.a_cb(a_y.a_bp.titleLabelPath, '');
				},
				
				a_bV: function(a_b7, a_b9, a_ca) {
					a_b7.css({ top: a_ca + 'px', left: a_b9 + 'px' });
				},
				
				a_b8: function(a_b7) {
// TODO
				},
				
				a_bU: function(a_b7, a_b6) {
					for (var a_be = 0; a_be < a_b6.length; ++a_be) {
						a_b7.addClass(a_b6[a_be]);
					}
				},
				
				a_bN: function(a_bM, a_bL) {
					var a_y = this;
					a_y.a_b3['pn' + a_bM] = a_bL;
				},
				
				a_b5: function(a_bM, a_b4) {
					var a_y = this;
					var a_b2 = 'pn' + a_bM;
					if (typeof a_y.a_b3[a_b2] == 'undefined') return a_b4;
					return a_y.a_b3[a_b2];
				},
				
				a_bS: function() {
					var a_y = this;
					a_y.a_C.a_V(
						function(a_P, a_T, a_S, a_R) {
							for (var a_be = 0; a_be < a_y.a_bO.length; ++a_be) {
								var a_bL = a_y.a_bO[a_be];
								a_bL.a_b1(a_S);
							}
							a_T.text(a_y.a_b0(a_y.a_bK()));
							a_R.text(a_d.a_bq.a_y.a_by);
						},
						function() { return a_y.a_Y(); }
					);
				},
				
				a_Y: function() {
					var a_y = this;
					for (var a_be = 0; a_be < a_y.a_bO.length; ++a_be) {
						var a_bL = a_y.a_bO[a_be];
						a_bL.a_bD();
						if (a_bL.a_bZ() != null) {
							return false;
						}
					}
					a_y.a_bY();
					return true;
				}
			}];
		};
		
		a_d.a_bq.prototype.a_O = function() {
			return this.a_y[0];
		};
		
		a_d.a_bq.prototype.a_bX = function(a_bW) {
			var a_y = this.a_O();
			a_y.a_bp.tempId = a_bW;
		};
		
		a_d.a_bq.prototype.a_E = function(a_bT, a_ba) {
			var a_y = this.a_O();
			var a_be = 0;
			
			a_y.a_ba = a_ba;
			
			a_y.a_B = jQuery('<div></div>').addClass(a_d.a_bq.a_y.a_bC).attr('id', a_y.a_bi);
			a_y.a_bV(a_y.a_B, a_y.a_bp.position.x, a_y.a_bp.position.y);
			a_y.a_bU(a_y.a_B, a_y.a_bp.classes);
			a_bT.append(a_y.a_B);
			
			var a_bR = jQuery('<span></span>').addClass(a_d.a_bq.a_y.a_bA);
			a_bR.click(function() { a_y.a_bS(); });
			a_y.a_B.append(a_bR);
			
			for (a_be = 0; a_be < a_y.a_bp.fields.length; ++a_be) {
				var a_bP = a_y.a_bp.fields[a_be];
				var a_bL = a_y.a_bo.a_bQ(a_bP);
				var a_bM = a_bP.propName;
				a_y.a_bO.push(a_bL);
				a_y.a_bN(a_bM, a_bL);
			}
			
			var a_bJ = a_y.a_bK();
			a_y.a_bI = jQuery('<div></div>').addClass(a_d.a_bq.a_y.a_bB).text(a_bJ);
			a_y.a_B.append(a_y.a_bI);
			
			a_y.a_ba.draggable(a_y.a_B);
			
			if (a_y.a_bp.maxOutgoing != 0) {
				for (var a_be = 0; a_be < a_y.a_bH.length; ++a_be) {
					var a_bc = a_y.a_bH[a_be];
					var a_bE = a_d.a_bq.a_y.a_bz + a_bc.typeName;
					
					var a_bG = jQuery('<div></div>').addClass(a_bE);
// TODO: Add data so that we can later know which type of connection was created?
					a_y.a_B.append(a_bG);
					
					var a_bF = a_y.a_ba.makeSource(a_y.a_B, {
						filter: '.' + a_bE,
						anchor: 'Continuous',
						connectorStyle: { stroke: '#000000', strokeWidth: 2, outlineStroke: 'transparent', outlineWidth: 4 },
						connectionType: a_bc.typeName,
						maxConnections: a_y.a_bp.maxOutgoing
					});
				}
			}
			
			if (a_y.a_bp.maxIncoming != 0) {
				a_y.a_ba.makeTarget(a_y.a_B, {
					anchor: 'Continuous',
					allowLoopback: false
				});
			}
		};
		
		a_d.a_bq.prototype.a_bD = function() {
// TODO
// - sync (directly into nodeData):
//   - position
//   - fields
		};
		
		a_d.a_bq.a_y = {
			a_bC: 'rgm-modes-node-container',
			a_bB: 'rgm-modes-node-title',
			a_bA: 'rgm-modes-node-configure-button',
			a_bz: 'rgm-modes-node-source-endpoint-',
			a_by: 'OK',
			a_bx: ['Configure "', 'titleLabel', '"'],
			a_bw: 'titleLabel'
		};
	}
})(window.snOoPy.SNooPY, window);




(function(a_d, a_e) {
	'use strict';
	if (typeof a_d.a_c == 'undefined') {
		a_d.a_c = function(a_bo) {
			this.a_y = [{
				a_bn: this,
				a_bo: a_bo,
				
				a_B: null,
				a_N: null,
				a_P: null,
				a_T: null,
				a_S: null,
				a_R: null,
				a_Q: null,
				
				a_M: null,
				
				a_bm: [],
				a_bl: {},
				a_bj: [],
				
				a_ba: null,
				a_br: false,
				
				a_bb: function(a_8, a_7) {
					var a_y = this;
					if (a_7) {
					
// TODO implement (the following is demo code)
						var a_bv = a_y.a_bl[a_8.sourceId];
						var a_bu = a_y.a_bl[a_8.targetId];
						var a_bs = a_8.connection;
						a_bs.setLabel('Here some label');
						// a_y.a_bt(a_bs);						
					}
				},
				
				a_9: function(a_8, a_7) {
					var a_y = this;
					if (a_y.a_br) return;
// TODO
					alert('Connection detached');
				},
				
				a_bt: function(a_bs) {
					var a_y = this;
					a_y.a_br = true;
					a_y.a_ba.deleteConnection(a_bs);
					a_y.a_br = false;
				},
				
				a_J: function() {
					var a_y = this;
					
					for (var a_be = 0; a_be < a_y.a_M.nodes.length; ++a_be) {(function(a_be) {
						var a_bi = a_d.a_c.a_y.a_u + a_d.a_6.a_5().a_4();
						
						var a_bp = a_y.a_M.nodes[a_be];
						var a_bk = new a_d.a_bq(a_bp, a_bi, a_y.a_bo, a_y.a_bn, a_y.a_M.connectionTypes);
						a_bk.a_E(a_y.a_N, a_y.a_ba);
						a_y.a_bm.push(a_bk);
						a_y.a_bl[a_bi] = a_bk;
						a_y.a_bj.push(a_bi);
					})(a_be);}
				},
				
				a_bg: function(a_bf) {
					var a_N = jQuery('<div></div>').addClass(a_d.a_c.a_y.a_t + a_bf);
					var a_bh = jQuery('<div></div>');
					a_bh.append(a_N);
					return a_bh;
				},
				
				a_bd: function(a_ba, a_bc) {
					var a_y = this;
					
					var a_bf = a_bc.typeName;
					
					a_ba.registerConnectionType(a_bf, {
						anchor: 'Continuous',
						connector: 'StateMachine',
						hoverPaintStyle:{ stroke: '#00ff00', strokeWidth: 2 },
						overlays: [
							['Arrow', { width:10, length: 14, foldback: 0.8, location:1, id: 'arrow' } ],
							['Custom', {
								create: function(component) { return a_y.a_bg(a_bf) },
								location: 0.7,
								id: 'typeOverlay'
							}]
						]
					});
				},
				
				a_K: function() {
					var a_y = this;
					for (var a_be = 0; a_be < a_y.a_M.connectionTypes.length; ++a_be) {
						var a_bc = a_y.a_M.connectionTypes[a_be];
						a_y.a_bd(a_y.a_ba, a_bc);
					}
				},
				
				a_L: function() {
					var a_y = this;
					
					if (a_y.a_ba == null) {
// TODO: clean
						a_y.a_ba = jsPlumb.getInstance({
							Endpoint: ['Dot', {radius: 2}],
							Connector: 'StateMachine',
							Container: a_y.a_N
						});
					
						a_y.a_ba.bind('connection', function(a_8, a_7) {
							a_y.a_bb(a_8, a_7);
						});
						
						a_y.a_ba.bind('connectionDetached', function(a_8, a_7) {
							a_y.a_9(a_8, a_7);
						});
					}
				},
				
				a_I: function() {
					var a_y = this;
					
					var a_3 = a_d.a_6.a_5().a_4();
					
					a_y.a_P = jQuery('<div class="modal fade" tabindex="-1" role="dialog" data-backdrop="static" data-keyboard="false"></div>').attr('id', a_3);
				
					var a_2 = jQuery('<div class="modal-dialog" role="document"></div>');
					a_y.a_P.append(a_2);
					
					var a_0 = jQuery('<div class="modal-content"></div>');
					a_2.append(a_0);
					
					var a_1 = jQuery('<div class="modal-header"></div>');
					a_0.append(a_1);
					
					a_y.a_T = jQuery('<h1></h1>');
					a_1.append(a_y.a_T);
					
					a_y.a_S = jQuery('<div class="modal-body"></div>');
					a_0.append(a_y.a_S);
					
					var a_Z = jQuery('<div class="modal-footer"></div>');
					a_0.append(a_Z);
					
					a_y.a_R = jQuery('<button type="button" class="btn btn-default"></button>');
					a_Z.append(a_y.a_R);
					
					a_y.a_R.click(function(event) { return a_y.a_Y(event); });
					
					a_y.a_P.insertAfter(a_y.a_B);
					a_y.a_P.modal('hide');
				},
				
				a_Y: function(a_W) {
					var a_y = this;
					var a_X = typeof a_y.a_Q != 'function' || a_y.a_Q.apply(a_y.a_P, []);
					if (a_X) {
						a_y.a_P.modal('hide');
					} else {
						a_W.preventDefault();
						a_W.stopImmediatePropagation();
						return false; 
					}
				}
			}];
		};
		
		a_d.a_c.prototype.a_O = function() {
			return this.a_y[0];
		};
				
		a_d.a_c.prototype.a_V = function(a_U, a_Q) {
			var a_y = this.a_O();
			a_y.a_T.empty();
			a_y.a_S.empty();
			a_y.a_R.empty();
			a_U.apply(a_y.a_P, [a_y.a_P, a_y.a_T, a_y.a_S, a_y.a_R]);
			a_y.a_Q = a_Q;
			a_y.a_P.modal('show');
		};
		
		a_d.a_c.prototype.a_E = function(a_B) {
			var a_y = this.a_O();
			
			a_y.a_B = a_B;
			
			
			
			a_y.a_N = jQuery('<div></div>').addClass(a_d.a_c.a_y.a_w);
			a_y.a_B.append(a_y.a_N);
			
			a_y.a_M = a_y.a_B.data(a_d.a_c.a_y.a_v);
			
			a_y.a_L();
			a_y.a_K();
			
// TODO: remove demo code below
			
			jQuery('.rgm-modes-container').pan({
				mouseControl: 'edge',
				mouseSpeed: 150
			});
// TODO: remove demo code above
			
			a_y.a_J();
			
			a_y.a_I();
		};
		
		a_d.a_c.a_b = function(a_H, a_A, a_F, a_D) {
			var a_G = a_d.a_c.a_y.a_s();
			
			jsPlumb.ready(function() {
				jQuery(document).ready(function() {					
					if (typeof a_H == 'function') {
						a_H.apply({}, []);
					}
					var a_z = [];
					jQuery(a_d.a_c.a_y.a_x).each(function() {
						var a_B = jQuery(this);
						var a_C = new a_d.a_c(a_G);
						
						if (typeof a_F == 'function') {
							a_F.apply(a_B, [a_C, a_B]);
						}
						
						a_C.a_E(jQuery(this));
						a_z.push(a_C);
						
						if (typeof a_D == 'function') {
							a_D.apply(a_C, [a_C, a_B]);
						}
					});
					if (typeof a_A == 'function') {
						a_A.apply({}, [a_z]);
					}
				});
			});
		};
		
		a_d.a_c.a_y = {
			a_x: '.rgm-modes-container',
			a_w: 'rgm-modes-inner-container',
			a_v: 'model',
			a_u: 'rgm_modes_node_',
			a_t: 'rmg-modes-connection-overlay-',
			
			a_s: function() {
				var a_f = new a_d.a_r();
				
				var a_o = new a_d.a_q();
				a_f.a_j(a_d.a_p.a_h, a_o);
				
				var a_l = new a_d.a_n();
				a_f.a_j(a_d.a_m.a_h, a_l);
				
				var a_g = new a_d.a_k(a_f);
				a_f.a_j(a_d.a_i.a_h, a_g);
				
				return a_f;
			}
		};
	}
})(window.snOoPy.SNooPY, window);




(function(a_d, a_e) {
	'use strict';
	
	if (typeof a_e.rgm == 'undefined') a_e.rgm = {};
	if (typeof a_e.rgm.modes == 'undefined') a_e.rgm.modes = {};
	
	if (typeof a_e.rgm.modes.ModelDesigner == 'undefined') {
		a_e.rgm.modes.ModelDesigner = {
			installAllEventually: a_d.a_c.a_b
		};
	}
})(window.snOoPy.SNooPY, window);
