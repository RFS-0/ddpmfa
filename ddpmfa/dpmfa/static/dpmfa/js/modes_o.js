(function(a_e) {
	'use strict';
	if (typeof a_e.snOoPy == 'undefined') a_e.snOoPy = {};
	if (typeof a_e.snOoPy.SNooPY == 'undefined') a_e.snOoPy.SNooPY = {};
})(window);




(function(a_d, a_e) {
	'use strict';
	if (typeof a_d.a_bs == 'undefined') {
		a_d.a_bs = function() {
			this.a_H = [{
				a_bJ: this,
				a_fv: a_d.a_bs.a_H.a_ft,
				a_fu: -1
			}];
		};
		
		a_d.a_bs.prototype.a_5 = function() { return this.a_H[0]; };
		
		a_d.a_bs.prototype.a_bq = function() {
			var a_H = this.a_5();
			
			if (a_H.a_fu + 1 > a_d.a_bs.a_fr) {
				a_H.a_fu = 0;
				a_H.a_fv += a_d.a_bs.a_fs;
			} else {
				++a_H.a_fu;
			}
			
			return a_H.a_fv + a_H.a_fu;
		};
		
		a_d.a_bs.a_H = {
			a_ft: 'u',
			a_fs: 'x',
			a_fr: 999999999,
			a_fq: null
		};
		
		a_d.a_bs.a_br = function() {
			if (a_d.a_bs.a_H.a_fq == null) {
				a_d.a_bs.a_H.a_fq = new a_d.a_bs();
			}
			return a_d.a_bs.a_H.a_fq;
		};
	}
})(window.snOoPy.SNooPY, window);




(function(a_d, a_e) {
	'use strict';
	if (typeof a_d.a_cE == 'undefined') {
		a_d.a_cE = function(a_fp) {
			this.a_H = [{
				a_bJ: this,
				a_fp: a_fp
			}];
		};
		
		a_d.a_cE.prototype.a_5 = function() { return this.a_H[0]; };
		
		a_d.a_cE.prototype.a_cC = function(a_e4) {
			var a_H = this.a_5();
			var a_fn = '';
			for (var a_bA = 0; a_bA < a_H.a_fp.length; ++a_bA) {
				var a_fo = a_H.a_fp[a_bA];
				if (a_bA % 2 == 0) {
					a_fn += a_fo;
				} else {
					if (typeof a_e4[a_fo] != 'undefined') {
						a_fn += a_e4[a_fo];
					}
				}
			}
			return a_fn;
		};
	}
})(window.snOoPy.SNooPY, window);




(function(a_d, a_e) {
	'use strict';
	if (typeof a_d.a_eF == 'undefined') {
		a_d.a_eF = function(a_fj, a_fh, a_fd) {
			this.a_H = [{
				a_bJ: this,
				
				a_fj: a_fj,
				a_fh: a_fh,
				a_fd: a_fd,
				
				a_fe: (a_fh ? 1 : (-1)) * a_fj,
				a_ff: a_fh ? 1 : (-1),
				
				a_fg: function(a_fl, a_fk, a_fm) {
					return a_fl > a_fk || (a_fm && a_fl == a_fk);
				}
			}];
		};
		
		a_d.a_eF.prototype.a_5 = function() { return this.a_H[0]; };
		
		a_d.a_eF.prototype.a_e9 = function() { return this.a_5().a_fj; };
		
		a_d.a_eF.prototype.a_fi = function() { return this.a_5().a_fh; };
		
		a_d.a_eF.prototype.a_e6 = function() { return this.a_5().a_fd; };
		
		a_d.a_eF.prototype.a_eU = function(a_dX) {
			var a_H = this.a_5();
			return a_H.a_fg(a_H.a_ff * a_dX, a_H.a_fe, a_H.a_fd);
		};
	}
})(window.snOoPy.SNooPY, window);




(function(a_d, a_e) {
	'use strict';
	if (typeof a_d.a_ey == 'undefined') {
		a_d.a_ey = function(a_eY, a_eD, a_eC) {
			this.a_H = [{
				a_bJ: this,
				a_eY: a_eY,
				a_eD: a_eD,
				a_eC: a_eC,
				
				a_fc: null,
				a_fa: null,
				a_e3: null,
				a_e1: null,
				
				a_e8: function(a_dX) {
					return a_dX ? a_d.a_ey.a_H.a_eH : a_d.a_ey.a_H.a_eG;
				},
				
				a_eR: function(a_dX) {
					var a_H = this;
					if (a_H.a_fc == null) {
						a_H.a_fc = new a_d.a_cE(a_d.a_ey.a_H.a_eQ.slice());
					}
					var a_e4 = {};
					a_e4[a_d.a_ey.a_H.a_eJ] = a_dX;
					return a_H.a_fc.a_cC(a_e4);
				},
				
				a_eX: function(a_fb) {
					var a_H = this;
					if (a_H.a_fa == null) {
						a_H.a_fa = new a_d.a_cE(a_d.a_ey.a_H.a_eP.slice());
					}
					var a_e4 = {};
					a_e4[a_d.a_ey.a_H.a_eL] = a_fb;
					a_e4[a_d.a_ey.a_H.a_eM] = a_H.a_eY;
					return a_H.a_fa.a_cC(a_e4);
				},
				
				a_e2: function(a_e5, a_dX, a_e7) {
					var a_H = this;
					var a_e4 = {};
					a_e4[a_d.a_ey.a_H.a_eJ] = a_dX;
					a_e4[a_d.a_ey.a_H.a_eK] = a_e7.a_e9();
					a_e4[a_d.a_ey.a_H.a_eI] = a_H.a_e8(a_e7.a_e6());
					return a_e5.a_cC(a_e4);
				},
				
				a_eV: function(a_dX) {
					var a_H = this;
					if (a_H.a_e3 == null) {
						a_H.a_e3 = new a_d.a_cE(a_d.a_ey.a_H.a_eO.slice());
					}
					return a_H.a_e2(a_H.a_e3, a_dX, a_H.a_eD);
				},
				
				a_eS: function(a_dX) {
					var a_H = this;
					if (a_H.a_e1 == null) {
						a_H.a_e1 = new a_d.a_cE(a_d.a_ey.a_H.a_eN.slice());
					}
					return a_H.a_e2(a_H.a_e1, a_dX, a_H.a_eC);
				}
			}];
		};
		
		a_d.a_ey.prototype.a_5 = function() { return this.a_H[0]; };
		
		a_d.a_ey.prototype.a_cl = function(a_eu) {
			var a_H = this.a_5();
			
			var a_e0 = (new RegExp('^-?(0|[1-9][0-9]*)(\\.[0-9]+)?$')).exec(a_eu);
			var a_eZ = 2;
			if (a_e0) {
				var a_eW = 0;
				if (a_e0[a_eZ]) {
					a_eW = a_e0[a_eZ].length - 1;
				}
				if (a_H.a_eY >= 0 && a_eW > a_H.a_eY) {
					return a_H.a_eX(a_eW);
				}
				
				var a_eT = Number.parseFloat(a_eu);
				
				if (a_H.a_eD != null && !a_H.a_eD.a_eU(a_eT)) {
					return a_H.a_eV(a_eu);
				}
				if (a_H.a_eC != null && !a_H.a_eC.a_eU(a_eT)) {
					return a_H.a_eS(a_eu);
				}
				
			} else {
				return a_H.a_eR(a_eu);
			}
		};
		
		a_d.a_ey.a_H = {
			a_eQ: ['The value "', 'foundValue', '" is not a correctly formatted number.'],
			a_eP: ['This value has too many decimals. The maximum allowed is ', 'maxDecimals', '. ', 'foundDecimals', ' was/were found.'],
			a_eO: ['The value ', 'foundValue', ' is too small. The minimum value is ', 'referenceValue', ' (inclusive: ', 'inclusiveYesOrNo', ').'],
			a_eN: ['The value ', 'foundValue', ' is too large. The maximum value is ', 'referenceValue', ' (inclusive: ', 'inclusiveYesOrNo', ').'],
			a_eM: 'maxDecimals',
			a_eL: 'foundDecimals',
			a_eK: 'referenceValue',
			a_eJ: 'foundValue',
			a_eI: 'inclusiveYesOrNo',
			a_eH: 'yes',
			a_eG: 'no'
		};
		
		a_d.a_ey.a_ex = function(a_eE) {
			var a_eD = null;
			if (typeof a_eE['min'] != 'undefined' && a_eE.min != null) {
				a_eD = new a_d.a_eF(a_eE.min.value, true, a_eE.min.inclusive);
			}
			
			var a_eC = null;
			if (typeof a_eE['max'] != 'undefined' && a_eE.max != null) {
				a_eC = new a_d.a_eF(a_eE.max.value, false, a_eE.max.inclusive);
			}
			
			return new a_d.a_ey(a_eE.decimals, a_eD, a_eC);
		};
	}
})(window.snOoPy.SNooPY, window);




(function(a_d, a_e) {
	'use strict';
	if (typeof a_d.a_r == 'undefined') {
		a_d.a_r = function() {
			this.a_H = [{
				a_bJ: this,
				a_eA: {}
			}];
		};
		
		a_d.a_r.prototype.a_5 = function() { return this.a_H[0]; };
		
		a_d.a_r.prototype.a_j = function(a_dg, a_eB) {
			this.a_5().a_eA[a_dg] = a_eB;
		};
		
		a_d.a_r.prototype.a_ez = function(a_dg, a_c2, a_b8, a_c3, a_df, a_dd) {
			var a_H = this.a_5();
			if (typeof a_H.a_eA[a_dg] == 'undefined') {
				throw 'Unknown field type "' + a_dg + '" in a_r.a_ez(...)';
			}
			return a_H.a_eA[a_dg].a_ez(a_dg, a_c2, a_b8, a_c3, a_df, a_dd);
		};
		
		a_d.a_r.prototype.a_cc = function(a_da) {
			return this.a_ez(a_da.fieldType, a_da.fieldArgs, a_da.propName, a_da.label, a_da.valueData, a_da.dirty);
		};
	}
})(window.snOoPy.SNooPY, window);




(function(a_d, a_e) {
	'use strict';
	if (typeof a_d.a_q == 'undefined') {
		a_d.a_q = function() {
			this.a_H = [{ a_bJ: this }];
		};
		
		a_d.a_q.prototype.a_5 = function() { return this.a_H[0]; };
		
		a_d.a_q.prototype.a_ez = function(a_dg, a_c2, a_b8, a_c3, a_df, a_dd) {
			return new a_d.a_p(a_dg, a_c2, a_b8, a_c3, a_df, a_dd);
		};
		
		a_d.a_q.prototype.a_cc = function(a_da) {
			return this.a_ez(a_da.fieldType, a_da.fieldArgs, a_da.propName, a_da.label, a_da.valueData, a_da.dirty);
		};
	}
})(window.snOoPy.SNooPY, window);




(function(a_d, a_e) {
	'use strict';
	if (typeof a_d.a_n == 'undefined') {
		a_d.a_n = function() {
			this.a_H = [{ a_bJ: this }];
		};
		
		a_d.a_n.prototype.a_5 = function() { return this.a_H[0]; };
		
		a_d.a_n.prototype.a_ez = function(a_dg, a_c2, a_b8, a_c3, a_df, a_dd) {
			return new a_d.a_m(a_dg, a_c2, a_b8, a_c3, a_df, a_dd);
		};
		
		a_d.a_n.prototype.a_cc = function(a_da) {
			return this.a_ez(a_da.fieldType, a_da.fieldArgs, a_da.propName, a_da.label, a_da.valueData, a_da.dirty);
		};
	}
})(window.snOoPy.SNooPY, window);




(function(a_d, a_e) {
	'use strict';
	if (typeof a_d.a_k == 'undefined') {
		a_d.a_k = function(a_bK) {
			this.a_H = [{
				a_bJ: this,
				a_bK: a_bK
			}];
		};
		
		a_d.a_k.prototype.a_5 = function() { return this.a_H[0]; };
		
		a_d.a_k.prototype.a_ez = function(a_dg, a_c2, a_b8, a_c3, a_df, a_dd) {
			var a_H = this.a_5();
			return new a_d.a_i(a_H.a_bK, a_dg, a_c2, a_b8, a_c3, a_df, a_dd);
		};
		
		a_d.a_k.prototype.a_cc = function(a_da) {
			return this.a_ez(a_da.fieldType, a_da.fieldArgs, a_da.propName, a_da.label, a_da.valueData, a_da.dirty);
		};
	}
})(window.snOoPy.SNooPY, window);




(function(a_d, a_e) {
	'use strict';
	if (typeof a_d.a_p == 'undefined') {
		a_d.a_p = function(a_dg, a_c2, a_b8, a_c3, a_df, a_dd) {
			this.a_H = [{
				a_bJ: this,
				a_dg: a_dg,
				a_c2: a_c2,
				a_b8, a_b8,
				a_c3: a_c3,
				a_d3: a_df,
				a_dX: a_df,
				a_de: a_dd,
				
				a_ej: null,
				a_dW: null,
				a_ei: null,
				
				a_ev: null,
				
				a_ew: function() {
					var a_H = this;
					if (a_H.a_c2.numberConfig == null) return null;
					if (a_H.a_ev == null) {
						a_H.a_ev = a_d.a_ey.a_ex(a_H.a_c2.numberConfig);
					}
					return a_H.a_ev;
				},
				
				a_ee: function(a_eu) {
					var a_H = this;
					var a_ev = a_H.a_ew();
					return a_ev == null ? null : a_ev.a_cl(a_eu);
				},
				
				a_eq: function(a_ep) {
					return a_d.a_p.a_H.a_d5 + a_ep + a_d.a_p.a_H.a_d4;
				},
				
				a_el: function(a_be) {
					var a_H = this;
					a_be.removeClass(a_H.a_eq(a_d.a_p.a_H.a_et)).removeClass(a_H.a_eq(a_d.a_p.a_H.a_es)).removeClass(a_H.a_eq(a_d.a_p.a_H.a_er));
				},
				
				a_em: function(a_ef, a_ep) {
					var a_H = this;
					if (a_H.a_ej != null) {
						a_H.a_el(a_H.a_ej);
						a_H.a_ej.addClass(a_H.a_eq(a_ep));
						
						if (a_H.a_ei == null) {
							a_H.a_ei = jQuery('<span class="help-block"></span>');
							a_H.a_ej.append(a_H.a_ei);
						}
						a_H.a_ei.text(a_ef);
					}
				},
				
				a_ed: function(a_ef) {
					this.a_em(a_ef, a_d.a_p.a_H.a_d8);
				},
				
				a_eo: function(a_ef) {
					this.a_em(a_ef, a_d.a_p.a_H.a_d7);
				},
				
				a_en: function(a_ef) {
					this.a_em(a_ef, a_d.a_p.a_H.a_d6);
				},
				
				a_eg: function() {
					var a_H = this;
					if (a_H.a_ej != null) {
						a_H.a_el(a_H.a_ej);
						
						if (a_H.a_ei != null) {
							a_H.a_ei.remove();
							a_H.a_ei = null;
						}
					}
				},
			}];
		};
		
		a_d.a_p.prototype.a_5 = function() { return this.a_H[0]; };
		
		a_d.a_p.prototype.a_cn = function(a_cf) {
			var a_H = this.a_5();
			var a_ek = a_d.a_bs.a_br().a_bq();
			var a_ej = jQuery('<div class="form-group"></div>');
			var a_dZ = jQuery('<label class="control-label"></label>')
				.attr('for', a_ek)
				.text(a_H.a_c3);
			var a_dW = a_H.a_c2.displayAsTextArea
				? a_dW = jQuery('<textarea class="form-control"></textarea>')
				: a_dW = jQuery('<input type="text" class="form-control" />');
			a_dW
				.attr('id', a_ek)
				.val(a_H.a_dX);
			a_ej.append(a_dZ);
			a_ej.append(a_dW);
			a_cf.append(a_ej);
			
			a_H.a_ej = a_ej;
			a_H.a_dW = a_dW;
		};
		
		a_d.a_p.prototype.a_cS = function() {
			var a_H = this.a_5();
			a_H.a_ej = null;
			a_H.a_dW = null;
			a_H.a_ei = null;
		};
		
		a_d.a_p.prototype.a_bZ = function() {
			var a_H = this.a_5();
			a_H.a_dX = a_H.a_dW.val();
		};
		
		a_d.a_p.prototype.a_cA = function() {
			var a_H = this.a_5();
			var a_eh = {
				fieldType: a_H.a_dg,
				fieldArgs: a_H.a_c2,
				propName: a_H.a_b8,
				label: a_H.a_c3,
				valueData: a_H.a_dX,
				dirty: this.a_cR()
			};
			return a_eh;
		};
		
		a_d.a_p.prototype.a_cR = function() {
			var a_H = this.a_5();
			return a_H.a_de || a_H.a_dX != a_H.a_d3;
		};
		
		a_d.a_p.prototype.a_cQ = function(a_cP) {
			var a_H = this.a_5();
			a_H.a_de = false;
			a_H.a_d3 = a_H.a_dX;
		};
		
		a_d.a_p.prototype.a_cl = function() {
			var a_H = this.a_5();
			a_H.a_eg();
			if (a_H.a_c2.notEmpty && a_H.a_dX.length == 0) {
				var a_ef = a_d.a_p.a_H.a_eb;
				a_H.a_ed(a_ef);
				return a_ef;
			}
			if (a_H.a_c2.maxLength != -1 && a_H.a_dX.length > a_H.a_c2.maxLength) {
				var a_ef = a_d.a_p.a_H.a_ea + a_H.a_c2.maxLength + a_d.a_p.a_H.a_d9;
				a_H.a_ed(a_ef);
				return a_ef;
			}
			
			var a_ec = a_H.a_ee(a_H.a_dX);
			if (a_ec != null) {
				a_H.a_ed(a_ec);
				return a_ec;
			}
			
			return null;
		};
		
		a_d.a_p.a_H = {
			a_eb: 'This field can not be empty',
			a_ea: 'This field can contain no more than ',
			a_d9: ' characters.',
			a_d8: 'error',
			a_d7: 'warning',
			a_d6: 'success',
			a_d5: 'has-',
			a_d4: ''
		};
		
		a_d.a_p.a_h = 'TEXT';
	}
})(window.snOoPy.SNooPY, window);




(function(a_d, a_e) {
	'use strict';
	if (typeof a_d.a_m == 'undefined') {
		a_d.a_m = function(a_dg, a_c2, a_b8, a_c3, a_df, a_dd) {
			this.a_H = [{
				a_bJ: this,
				a_dg: a_dg,
				a_c2: a_c2,
				a_b8, a_b8,
				a_c3: a_c3,
				a_d3: a_df,
				a_dX: a_df,
				a_de: a_dd,
				
				a_dW: null,
				
				a_dY: function(a_d0, a_d2) {
					a_d0.prop('checked', a_d2);
				},
				
				a_d1: function(a_d0) {
					return a_d0.is(':checked');
				}
			}];
		};
		
		a_d.a_m.prototype.a_5 = function() {
			return this.a_H[0];
		};
		
		a_d.a_m.prototype.a_cn = function(a_cf) {
			var a_H = this.a_5();
			
			var a_K = jQuery('<div class="checkbox"></div>');
			a_cf.append(a_K);
			
			var a_dZ = jQuery('<label></label>').text(a_H.a_c3);
			a_K.append(a_dZ);
			
			a_H.a_dW = jQuery('<input type="checkbox" />');
			a_K.prepend(a_H.a_dW);
			
			a_H.a_dY(a_H.a_dW, a_H.a_dX);
		};
		
		a_d.a_m.prototype.a_cS = function() {
			var a_H = this.a_5();
			a_H.a_dW = null;
		};
		
		a_d.a_m.prototype.a_bZ = function() {
			var a_H = this.a_5();
// TODO
		};
		
		a_d.a_m.prototype.a_cA = function() {
			var a_H = this.a_5();
// TODO
		};
		
		a_d.a_m.prototype.a_cR = function() {
			var a_H = this.a_5();
// TODO
		};
		
		a_d.a_m.prototype.a_cQ = function(a_cP) {
			var a_H = this.a_5();
// TODO
		};
		
		a_d.a_m.prototype.a_cl = function() {
			var a_H = this.a_5();
// TODO
			return null;
		};
		
		a_d.a_m.a_h = 'CHECK';
	}
})(window.snOoPy.SNooPY, window);




(function(a_d, a_e) {
	'use strict';
	if (typeof a_d.a_cG == 'undefined') {
		a_d.a_cG = function(a_dE, a_ci, a_c3, a_ca) {
			this.a_H = [{
				a_bJ: this,
				a_dE: a_dE,
				a_ci: a_ci,
				a_c3: a_c3,
				a_ca: a_ca,
				
				a_c6: null,
				a_dq: null,
				a_K: null,
				a_dp: null,
				a_do: null,
				
				a_du: function() {
					return jQuery('<div class="panel panel-default"></div>').addClass(a_d.a_cG.a_H.a_bY);
				},
				
				a_ds: function() {
					var a_H = this;
					
					var a_b4 = jQuery('<div class="panel-heading"></div>').addClass(a_d.a_cG.a_H.a_bX).text(a_H.a_c3);
					a_H.a_K.append(a_b4);
					
					var a_cX = jQuery('<div class="panel-body"></div>').addClass(a_d.a_cG.a_H.a_cN);
					a_H.a_K.append(a_cX);
					
					var a_dS = jQuery('<div class="btn-group"></div>').addClass(a_d.a_cG.a_H.a_dn);
					a_cX.append(a_dS);
					
					var a_dU = jQuery('<button class="btn btn-default"></button>').addClass(a_d.a_cG.a_H.a_dV).text(a_d.a_cG.a_H.a_di);
					a_dS.append(a_dU);
					a_H.a_dp = a_dU;
					a_dU.click(function() { a_H.a_dJ(); });
					
					var a_dR  = jQuery('<button class="btn btn-default"></button>').addClass(a_d.a_cG.a_H.a_dT).text(a_d.a_cG.a_H.a_dh);
					a_dS.append(a_dR);
					a_H.a_do = a_dR;
					a_dR.click(function() { a_H.a_dI(); });
					
					a_H.a_bJ.a_c8();
					
					var a_dQ = jQuery('<div></div>').addClass(a_d.a_cG.a_H.a_dj);
					a_cX.append(a_dQ);
					
					for (var a_bA = 0; a_bA < a_H.a_ca.length; ++a_bA) {
						a_H.a_ca[a_bA].a_cn(a_dQ);
					}
				},
				
				a_dH: function(a_dP) {
					var a_H = this;
					
					if (a_dP) {
						if (a_H.a_c6 != null) {
							var a_dO = a_H.a_c6;
							var a_dN = a_dO.a_dA();
							var a_dM = a_H.a_dq;
							
							a_H.a_K.insertBefore(a_dO.a_dy());
							
							a_H.a_bJ.a_c7(a_dN);
							a_H.a_bJ.a_c9(a_dO);
							
							a_dO.a_c7(a_H.a_bJ);
							a_dO.a_c9(a_dM);
							
							a_H.a_bJ.a_c8();
							a_dO.a_c8();
							
							if (a_dN != null) {
								a_dN.a_c9(a_H.a_bJ);
								a_dN.a_c8();
							}
							
							if (a_dM != null) {
								a_dM.a_c7(a_dO);
								a_dM.a_c8();
							}
						}
					} else {
						if (a_H.a_dq != null) {
							var a_dO = a_H.a_dq;
							var a_dN = a_H.a_c6;
							var a_dM = a_dO.a_dz();
							
							a_H.a_K.insertAfter(a_dO.a_dy());
							
							a_H.a_bJ.a_c7(a_dO);
							a_H.a_bJ.a_c9(a_dM);
							
							a_dO.a_c7(a_dN);
							a_dO.a_c9(a_H.a_bJ);
							
							a_H.a_bJ.a_c8();
							a_dO.a_c8();
							
							if (a_dN != null) {
								a_dN.a_c9(a_dO);
								a_dN.a_c8();
							}
							
							if (a_dM != null) {
								a_dM.a_c7(a_H.a_bJ);
								a_dM.a_c8();
							}
						}
					}
				},
				
				a_dr: function(a_dK, a_dL) {
					if (a_dL) {
						a_dK.removeClass('disabled');
					} else {
						a_dK.addClass('disabled');
					}
				},
				
				a_dJ: function() {
					this.a_dH(true);
				},
				
				a_dI: function() {
					this.a_dH(false);
				}
			}]
		};
		
		a_d.a_cG.prototype.a_5 = function() { return this.a_H[0]; };
		
		a_d.a_cG.prototype.a_dG = function(a_dE) { this.a_5().a_dE = a_dE; };
		
		a_d.a_cG.prototype.a_dF = function() { return this.a_5().a_dE; };
		
		a_d.a_cG.prototype.a_cj = function(a_ci) { this.a_5().a_ci = a_ci; };
		
		a_d.a_cG.prototype.a_dD = function() { return this.a_5().a_ci; };
		
		a_d.a_cG.prototype.a_dC = function() { return this.a_5().a_c3; };
		
		a_d.a_cG.prototype.a_dB = function() { return this.a_5().a_ca; };
		
		a_d.a_cG.prototype.a_c7 = function(a_c6) { this.a_5().a_c6 = a_c6; };
		
		a_d.a_cG.prototype.a_dA = function() { return this.a_5().a_c6; };
		
		a_d.a_cG.prototype.a_c9 = function(a_dq) { this.a_5().a_dq = a_dq; };
		
		a_d.a_cG.prototype.a_dz = function() { return this.a_5().a_dq; };
		
		a_d.a_cG.prototype.a_dy = function() {
			return this.a_5().a_K;
		};
		
		a_d.a_cG.prototype.a_cV = function(a_cf) {
			var a_H = this.a_5();
			a_H.a_K = a_H.a_du();
			a_cf.append(a_H.a_K);
			a_H.a_ds();
		};
		
		a_d.a_cG.prototype.a_dx = function(a_dw) {
			var a_H = this.a_5();
			a_H.a_K = a_H.a_du();
			a_H.a_K.insertBefore(a_dw);
			a_H.a_ds();
		};
		
		a_d.a_cG.prototype.a_dv = function(a_dt) {
			var a_H = this.a_5();
			a_H.a_K = a_H.a_du();
			a_H.a_K.insertAfter(a_dt);
			a_H.a_ds();
		};
		
		a_d.a_cG.prototype.a_c8 = function() {
			var a_H = this.a_5();
			a_H.a_dr(a_H.a_dp, a_H.a_c6 != null);
			a_H.a_dr(a_H.a_do, a_H.a_dq != null);
		};
		
		a_d.a_cG.prototype.a_cS = function() {
			var a_H = this.a_5();
			a_H.a_K = null;
			a_H.a_dp = null;
			a_H.a_do = null;
		};
		
		a_d.a_cG.prototype.a_cA = function() {
// TODO
		};
		
		a_d.a_cG.a_H = {
			a_bY: 'rgm-modes-subform-container',
			a_bX: 'rgm-modes-subform-title',
			a_cN: 'rgm-modes-subform-content',
			a_dn: 'rgm-modes-subform-move-btns',
			a_dm: 'rgm-modes-subform-move-btn',
			a_dl: 'rgm-modes-subform-up-btn',
			a_dk: 'rgm-modes-subform-down-btn',
			a_dj: 'rgm-modes-subform-fields',
			a_di: '\u25B2',
			a_dh: '\u25BC'
		};
	}

})(window.snOoPy.SNooPY, window);




(function(a_d, a_e) {
	'use strict';
	if (typeof a_d.a_i == 'undefined') {
		a_d.a_i = function(a_bK, a_dg, a_c2, a_b8, a_c3, a_df, a_dd) {
// TODO: remove subforms
			this.a_H = [{
				a_bJ: this,
				a_bK: a_bK,
				a_dg: a_dg,
				a_c2: a_c2,
				a_b8, a_b8,
				a_c3: a_c3,
				a_dc: a_df,
				a_de: a_dd,
				
				a_cU: null,
				a_cW: [],
				a_c5: {},
				
				a_c4: function() {
					var a_H = this;
					
					var a_c6 = null;
					for (var a_bA = 0; a_bA < a_H.a_dc.length; ++a_bA) {
						var a_c0 = a_H.a_dc[a_bA];
						
						var a_ca = [];
						for (var a_db = 0; a_db < a_c0.fields.length; ++a_db) {
							var a_da = a_c0.fields[a_db];
							var a_b7 = a_H.a_bK.a_cc(a_da);
							a_ca.push(a_b7);
						}
						
						var a_cT = new a_d.a_cG(a_c0.id, a_c0.tempId, a_c0.label, a_ca);
						
						if (a_bA > 0) {
							a_cT.a_c7(a_c6);
							a_c6.a_c9(a_cT);
						}
						
						a_H.a_cW.push(a_cT);
						a_c6 = a_cT;
					}
				},
				
				a_c1: function(a_c0) {
					var a_H = this;
					
					var a_ci = a_d.a_i.a_H.a_cH + a_d.a_bs.a_br().a_bq();
					
					var a_ca = [];
					for (var a_bA = 0; a_bA < a_c0.fields.length; ++a_bA) {
						var a_da = a_c0.fields[a_bA];
						var a_b7 = a_H.a_bK.a_cc(a_da);
						a_ca.push(a_b7);
					}
					
					var a_cT = new a_d.a_cG(a_c0.id, a_ci, a_c0.label, a_ca);
					
					if (a_H.a_cW.length > 0) {
						var a_c6 = a_H.a_cW[a_H.a_cW.length - 1];
						a_c6.a_c9(a_cT);
						a_c6.a_c8();
						a_cT.a_c7(a_c6);
					}
					
					a_cT.a_cV(a_H.a_cU);
					
					a_H.a_cW.push(a_cT);
					a_H.a_c5[a_ci] = a_cT;
				}
			}];
			this.a_H[0].a_c4();
		};
		
		a_d.a_i.prototype.a_5 = function() { return this.a_H[0]; };
		
		a_d.a_i.prototype.a_cn = function(a_cf) {
			var a_H = this.a_5();
			var a_bA = 0;
			
			var a_K = jQuery('<div class="panel panel-default"></div>').addClass(a_d.a_i.a_H.a_bY);
			a_cf.append(a_K);
			
			var a_b4 = jQuery('<div class="panel-heading"></div>').addClass(a_d.a_i.a_H.a_bX);
			a_b4.text(a_H.a_c3);
			a_K.append(a_b4);
			
			var a_cX = jQuery('<div class="panel-body"></div>').addClass(a_d.a_i.a_H.a_cN);
			a_K.append(a_cX);
			
			var a_cZ = jQuery('<div class="btn-group-vertical"></div>').addClass(a_d.a_i.a_H.a_cM);
			a_cX.append(a_cZ);
			
			for (a_bA = 0; a_bA < a_H.a_c2.forms.length; ++a_bA) {(function(a_bA) {
				var a_c0 = a_H.a_c2.forms[a_bA];
				
				var a_cY = jQuery('<button class="btn btn-default"></button>').addClass(a_d.a_i.a_H.a_cL).text(a_d.a_i.a_H.a_cJ + a_c0.label + a_d.a_i.a_H.a_cI);
				a_cY.click(function() { a_H.a_c1(a_c0); });
				a_cZ.append(a_cY);
			})(a_bA);}
			
			var a_cU = jQuery('<div></div>').addClass(a_d.a_i.a_H.a_cK);
			a_cX.append(a_cU);
			
			for (a_bA = 0; a_bA < a_H.a_cW.length; ++a_bA) {
				var a_cT = a_H.a_cW[a_bA];
				a_cT.a_cV(a_cU);
			}
			
			a_H.a_cU = a_cU;
		};
		
		a_d.a_i.prototype.a_cS = function() {
			var a_H = this.a_5();
			a_H.a_cU = null;
			for (a_bA = 0; a_bA < a_H.a_cW.length; ++a_bA) {
				var a_cT = a_H.a_cW[a_bA];
				a_cT.a_cV(a_cU);
				a_cT.a_cS();
			}
		};
		
		a_d.a_i.prototype.a_bZ = function() {
			var a_H = this.a_5();
// TODO
		};
		
		a_d.a_i.prototype.a_cA = function() {
			var a_H = this.a_5();
// TODO
		};
		
		a_d.a_i.prototype.a_cR = function() {
			var a_H = this.a_5();
// TODO
		};
		
		a_d.a_i.prototype.a_cQ = function(a_cP) {
			var a_H = this.a_5();
// TODO
		};
		
		a_d.a_i.prototype.a_cl = function() {
			var a_H = this.a_5();
// TODO
		};
		
		a_d.a_i.a_H = {
			a_bY: 'rgm-modes-forms-field-container',
			a_cO: 'rgm-modes-forms-field-title',
			a_cN: 'rgm-modes-forms-field-content',
			a_cM: 'rgm-modes-forms-field-add-buttons',
			a_cL: 'rgm-modes-forms-field-add-button',
			a_cK: 'rgm-modes-forms-field-forms',
			a_cJ: 'Add new ',
			a_cI: '',
			a_cH: 'temp_'
		};
		
		a_d.a_i.a_h = 'FORMS';
	}
})(window.snOoPy.SNooPY, window);




(function(a_d, a_e) {
	'use strict';
	
	if (typeof a_d.a_bM == 'undefined') {
		a_d.a_bM = function(a_bL, a_bE, a_bK, a_L, a_b3) {
// TODO (Could): a_bM should work like a_cG: unpack/repack a_bL
			this.a_H = [{
				a_bJ: this,
				a_bL: a_bL,
				a_bE: a_bE,
				a_bK: a_bK,
				a_L: a_L,
				a_b3: a_b3,
				
				a_K: null,
				a_b4: null,
				
				a_ca: [],
				a_cp: {},
				
				a_bw: null,
				
				a_cD: null,
				
				a_cm: function(a_b5) {
					var a_H = this;
					if (a_H.a_cF == null) {
						a_H.a_cD = new a_d.a_cE(a_d.a_bM.a_H.a_bT);
					}
					var a_cB ={};
					a_cB[a_d.a_bM.a_H.a_bS] = a_b5;
					return a_H.a_cD.a_cC(a_cB);
				},
				
				a_cw: function(a_cz, a_cq) {
					var a_H = this;
					var a_b7 = a_H.a_cr(a_cz[0], null);
					if (a_b7 == null) return a_cq;
					var a_cx = a_b7.a_cA();
					for (var a_bA = 1; a_bA < a_cz.length; ++a_bA) {
						var a_cy = a_cz[a_bA];
						if (typeof a_cx[a_cy] == 'undefined') {
							return a_cq;
						}
						a_cx = a_cx[a_cy];
					}
					return a_cx;
				},
				
				a_ck: function() {
					var a_H = this;
					a_H.a_b4.text(a_H.a_b6());
				},
				
				a_b6: function() {
					var a_H = this;
					return a_H.a_cw(a_H.a_bL.titleLabelPath, '');
				},
				
				a_ch: function(a_be, a_cu, a_cv) {
					a_be.css({ top: a_cv + 'px', left: a_cu + 'px' });
				},
				
				a_ct: function(a_be) {
// TODO
				},
				
				a_cg: function(a_be, a_cs) {
					for (var a_bA = 0; a_bA < a_cs.length; ++a_bA) {
						a_be.addClass(a_cs[a_bA]);
					}
				},
				
				a_b9: function(a_b8, a_b7) {
					var a_H = this;
					a_H.a_cp['pn' + a_b8] = a_b7;
				},
				
				a_cr: function(a_b8, a_cq) {
					var a_H = this;
					var a_co = 'pn' + a_b8;
					if (typeof a_H.a_cp[a_co] == 'undefined') return a_cq;
					return a_H.a_cp[a_co];
				},
				
				a_ce: function() {
					var a_H = this;
					a_H.a_L.a_bd(
						function(a_6, a_bb, a_ba, a_9, a_8) {
							for (var a_bA = 0; a_bA < a_H.a_ca.length; ++a_bA) {
								var a_b7 = a_H.a_ca[a_bA];
								a_b7.a_cn(a_ba);
							}
							a_bb.text(a_H.a_cm(a_H.a_b6()));
							a_8.text(a_d.a_bM.a_H.a_bU);
						},
						function() { return a_H.a_bl(); }
					);
				},
				
				a_bl: function() {
					var a_H = this;
					for (var a_bA = 0; a_bA < a_H.a_ca.length; ++a_bA) {
						var a_b7 = a_H.a_ca[a_bA];
						a_b7.a_bZ();
						if (a_b7.a_cl() != null) {
							return false;
						}
					}
					a_H.a_ck();
					return true;
				}
			}];
		};
		
		a_d.a_bM.prototype.a_5 = function() {
			return this.a_H[0];
		};
		
		a_d.a_bM.prototype.a_cj = function(a_ci) {
			var a_H = this.a_5();
			a_H.a_bL.tempId = a_ci;
		};
		
		a_d.a_bM.prototype.a_N = function(a_cf, a_bw) {
			var a_H = this.a_5();
			var a_bA = 0;
			
			a_H.a_bw = a_bw;
			
			a_H.a_K = jQuery('<div></div>').addClass(a_d.a_bM.a_H.a_bY).attr('id', a_H.a_bE);
			a_H.a_ch(a_H.a_K, a_H.a_bL.position.x, a_H.a_bL.position.y);
			a_H.a_cg(a_H.a_K, a_H.a_bL.classes);
			a_cf.append(a_H.a_K);
			
			var a_cd = jQuery('<span></span>').addClass(a_d.a_bM.a_H.a_bW);
			a_cd.click(function() { a_H.a_ce(); });
			a_H.a_K.append(a_cd);
			
			for (a_bA = 0; a_bA < a_H.a_bL.fields.length; ++a_bA) {
				var a_cb = a_H.a_bL.fields[a_bA];
				var a_b7 = a_H.a_bK.a_cc(a_cb);
				var a_b8 = a_cb.propName;
				a_H.a_ca.push(a_b7);
				a_H.a_b9(a_b8, a_b7);
			}
			
			var a_b5 = a_H.a_b6();
			a_H.a_b4 = jQuery('<div></div>').addClass(a_d.a_bM.a_H.a_bX).text(a_b5);
			a_H.a_K.append(a_H.a_b4);
			
			a_H.a_bw.draggable(a_H.a_K);
			
			if (a_H.a_bL.maxOutgoing != 0) {
				for (var a_bA = 0; a_bA < a_H.a_b3.length; ++a_bA) {
					var a_by = a_H.a_b3[a_bA];
					var a_b0 = a_d.a_bM.a_H.a_bV + a_by.typeName;
					
					var a_b2 = jQuery('<div></div>').addClass(a_b0);
// TODO: Add data so that we can later know which type of connection was created?
					a_H.a_K.append(a_b2);
					
					var a_b1 = a_H.a_bw.makeSource(a_H.a_K, {
						filter: '.' + a_b0,
						anchor: 'Continuous',
						connectorStyle: { stroke: '#000000', strokeWidth: 2, outlineStroke: 'transparent', outlineWidth: 4 },
						connectionType: a_by.typeName,
						maxConnections: a_H.a_bL.maxOutgoing
					});
				}
			}
			
			if (a_H.a_bL.maxIncoming != 0) {
				a_H.a_bw.makeTarget(a_H.a_K, {
					anchor: 'Continuous',
					allowLoopback: false
				});
			}
		};
		
		a_d.a_bM.prototype.a_bZ = function() {
// TODO
// - sync (directly into nodeData):
//   - position
//   - fields
		};
		
		a_d.a_bM.a_H = {
			a_bY: 'rgm-modes-node-container',
			a_bX: 'rgm-modes-node-title',
			a_bW: 'rgm-modes-node-configure-button',
			a_bV: 'rgm-modes-node-source-endpoint-',
			a_bU: 'OK',
			a_bT: ['Configure "', 'titleLabel', '"'],
			a_bS: 'titleLabel'
		};
	}
})(window.snOoPy.SNooPY, window);




(function(a_d, a_e) {
	'use strict';
	if (typeof a_d.a_c == 'undefined') {
		a_d.a_c = function(a_bK) {
			this.a_H = [{
				a_bJ: this,
				a_bK: a_bK,
				
				a_K: null,
				a_T: null,
				a_6: null,
				a_bb: null,
				a_ba: null,
				a_9: null,
				a_8: null,
				a_7: null,
				
				a_4: null,
				
				a_bI: [],
				a_bH: {},
				a_bF: [],
				
				a_bw: null,
				a_bN: false,
				
				a_bx: function(a_bu, a_bt) {
					var a_H = this;
					if (a_bt) {
					
// TODO implement (the following is demo code)
						var a_bR = a_H.a_bH[a_bu.sourceId];
						var a_bQ = a_H.a_bH[a_bu.targetId];
						var a_bO = a_bu.connection;
						a_bO.setLabel('Here some label');
						// a_H.a_bP(a_bO);						
					}
				},
				
				a_bv: function(a_bu, a_bt) {
					var a_H = this;
					if (a_H.a_bN) return;
// TODO
					alert('Connection detached');
				},
				
				a_bP: function(a_bO) {
					var a_H = this;
					a_H.a_bN = true;
					a_H.a_bw.deleteConnection(a_bO);
					a_H.a_bN = false;
				},
				
				a_S: function() {
					var a_H = this;
					
					for (var a_bA = 0; a_bA < a_H.a_4.nodes.length; ++a_bA) {(function(a_bA) {
						var a_bE = a_d.a_c.a_H.a_w + a_d.a_bs.a_br().a_bq();
						
						var a_bL = a_H.a_4.nodes[a_bA];
						var a_bG = new a_d.a_bM(a_bL, a_bE, a_H.a_bK, a_H.a_bJ, a_H.a_4.connectionTypes);
						a_bG.a_N(a_H.a_T, a_H.a_bw);
						a_H.a_bI.push(a_bG);
						a_H.a_bH[a_bE] = a_bG;
						a_H.a_bF.push(a_bE);
					})(a_bA);}
				},
				
				a_bC: function(a_bB) {
					var a_T = jQuery('<div></div>').addClass(a_d.a_c.a_H.a_v + a_bB);
					var a_bD = jQuery('<div></div>');
					a_bD.append(a_T);
					return a_bD;
				},
				
				a_bz: function(a_bw, a_by) {
					var a_H = this;
					
					var a_bB = a_by.typeName;
					
					a_bw.registerConnectionType(a_bB, {
						anchor: 'Continuous',
						connector: 'StateMachine',
						hoverPaintStyle:{ stroke: '#00ff00', strokeWidth: 2 },
						overlays: [
							['Arrow', { width:10, length: 14, foldback: 0.8, location:1, id: 'arrow' } ],
							['Custom', {
								create: function(component) { return a_H.a_bC(a_bB) },
								location: 0.7,
								id: 'typeOverlay'
							}]
						]
					});
				},
				
				a_2: function() {
					var a_H = this;
					for (var a_bA = 0; a_bA < a_H.a_4.connectionTypes.length; ++a_bA) {
						var a_by = a_H.a_4.connectionTypes[a_bA];
						a_H.a_bz(a_H.a_bw, a_by);
					}
				},
				
				a_3: function() {
					var a_H = this;
					
					if (a_H.a_bw == null) {
// TODO: clean
						a_H.a_bw = jsPlumb.getInstance({
							Endpoint: ['Dot', {radius: 2}],
							Connector: 'StateMachine',
							Container: a_H.a_T
						});
					
						a_H.a_bw.bind('connection', function(a_bu, a_bt) {
							a_H.a_bx(a_bu, a_bt);
						});
						
						a_H.a_bw.bind('connectionDetached', function(a_bu, a_bt) {
							a_H.a_bv(a_bu, a_bt);
						});
					}
				},
				
				a_R: function() {
					var a_H = this;
					
					var a_bp = a_d.a_bs.a_br().a_bq();
					
					a_H.a_6 = jQuery('<div class="modal fade" tabindex="-1" role="dialog" data-backdrop="static" data-keyboard="false"></div>').attr('id', a_bp);
				
					var a_bo = jQuery('<div class="modal-dialog" role="document"></div>');
					a_H.a_6.append(a_bo);
					
					var a_bm = jQuery('<div class="modal-content"></div>');
					a_bo.append(a_bm);
					
					var a_bn = jQuery('<div class="modal-header"></div>');
					a_bm.append(a_bn);
					
					a_H.a_bb = jQuery('<h1></h1>');
					a_bn.append(a_H.a_bb);
					
					a_H.a_ba = jQuery('<div class="modal-body"></div>');
					a_bm.append(a_H.a_ba);
					
					a_H.a_9 = jQuery('<div class="modal-footer"></div>');
					a_bm.append(a_H.a_9);
					
					a_H.a_8 = jQuery('<button type="button" class="btn btn-default"></button>');
					a_H.a_9.append(a_H.a_8);
					
					a_H.a_8.click(function(event) { return a_H.a_bl(event); });
					
					a_H.a_K.append(a_H.a_6);
					a_H.a_6.modal('hide');
				},
				
				a_bl: function(a_bj) {
					var a_H = this;
					var a_bk = typeof a_H.a_7 != 'function' || a_H.a_7.apply(a_H.a_6, []);
					if (a_bk) {
						a_H.a_6.modal('hide');
					} else {
						a_bj.preventDefault();
						a_bj.stopImmediatePropagation();
						return false; 
					}
				},
				
				a_bi: function() {
					var a_H = this;
					return a_H.a_T.parents('.' + a_d.a_c.a_H.a_y).length > 0;
				},
				
				a_Z: function(a_Y) {
					var a_H = this;
					return a_H.a_bi();
				},
				
				a_bh: function(a_be) {
					var a_bg = a_be.css('left');
					
				},
				
				a_bf: function(a_be) {
				
				}
			}];
		};
		
		a_d.a_c.prototype.a_5 = function() {
			return this.a_H[0];
		};
				
		a_d.a_c.prototype.a_bd = function(a_bc, a_7) {
			var a_H = this.a_5();
			a_H.a_bb.empty();
			a_H.a_ba.empty();
			a_H.a_8.empty();
			a_H.a_9.children().not(a_H.a_8).remove();
			a_bc.apply(a_H.a_6, [a_H.a_6, a_H.a_bb, a_H.a_ba, a_H.a_9, a_H.a_8]);
			a_H.a_7 = a_7;
			a_H.a_6.modal('show');
		};
		
		a_d.a_c.prototype.a_N = function(a_K) {
			var a_H = this.a_5();
			
			a_H.a_K = a_K;
			
			var a_X = jQuery('<div></div>').addClass(a_d.a_c.a_H.a_F);
			a_H.a_K.append(a_X);
			
			a_H.a_T = jQuery('<div></div>').addClass(a_d.a_c.a_H.a_E);
			a_X.append(a_H.a_T);
			
			a_H.a_4 = a_H.a_K.data(a_d.a_c.a_H.a_x);
			
			a_H.a_3();
			a_H.a_2();
			
			var a_1 = jQuery('<div></div>').addClass(a_d.a_c.a_H.a_D);
			a_H.a_K.append(a_1);
			
			var a_0 = jQuery('<div></div>').addClass(a_d.a_c.a_H.a_C);
			a_1.append(a_0);
			
			var a_W	= jQuery('<button type="button" class="btn btn-default"></button>').addClass(a_d.a_c.a_H.a_B).text(a_d.a_c.a_H.a_u);
			a_0.append(a_W);
			
			var a_V	= jQuery('<button type="button" class="btn btn-default"></button>').addClass(a_d.a_c.a_H.a_A).text(a_d.a_c.a_H.a_t);
			a_0.append(a_V);
			

// TODO: Mouse wheel / keyboard shortcuts for zooming?
// TODO: Infinite or very large canvas (still don't zoom in too quickly -> step?)
			
			a_X.pan({
				mouseControl: 'edge',
				mouseEdgeSpeed: 20,
				beforeEdgeMove: function(a_Y) { return a_H.a_Z(a_Y); }
			});
			
			
			var a_U = {
				get clientX() {
					var cX = a_X.position().left
						+ a_X.width() / 2
						- jQuery(document).scrollLeft()
						- parseFloat(a_H.a_T.css('left'));
					return cX;
				},
				get clientY() {
					var cY = a_X.position().top
						+ a_X.height() / 2
						- jQuery(document).scrollTop()
						- parseFloat(a_H.a_T.css('top'));
					console.log('cY', cY);
					return cY;
				}
			};
			
			a_H.a_T.panzoom({
				$zoomIn: a_W,
            	$zoomOut: a_V,
            	focal: a_U
			});
			
			//a_H.a_T.find('div').on('mousedown touchstart', function( e ) {
			//	e.stopImmediatePropagation();
			//});
			
			a_H.a_S();
			
			a_H.a_R();
		};
		
		a_d.a_c.a_b = function(a_Q, a_J, a_O, a_M) {
			var a_P = a_d.a_c.a_H.a_s();
			
			jsPlumb.ready(function() {
				jQuery(document).ready(function() {					
					if (typeof a_Q == 'function') {
						a_Q.apply({}, []);
					}
					var a_I = [];
					jQuery(a_d.a_c.a_H.a_G).each(function() {
						var a_K = jQuery(this);
						var a_L = new a_d.a_c(a_P);
						
						if (typeof a_O == 'function') {
							a_O.apply(a_K, [a_L, a_K]);
						}
						
						a_L.a_N(jQuery(this));
						a_I.push(a_L);
						
						if (typeof a_M == 'function') {
							a_M.apply(a_L, [a_L, a_K]);
						}
					});
					if (typeof a_J == 'function') {
						a_J.apply({}, [a_I]);
					}
				});
			});
		};
		
		a_d.a_c.a_H = {
			a_G: '.rgm-modes-container',
			a_F: 'rgm-modes-viewport',
			a_E: 'rgm-modes-drawing-container',
			a_D: 'rgm-modes-controls-container',
			a_C: 'rgm-modes-zoom-controls',
			a_B: 'rgm-modes-zoom-in-btn',
			a_A: 'rgm-modes-zoom-out-btn',
			a_z: 'rgm-modes-zoom-reset-btn',
			a_y: 'jtk-drag-select',
			a_x: 'model',
			a_w: 'rgm_modes_node_',
			a_v: 'rmg-modes-connection-overlay-',
			a_u: '\uD83D\uDD0D+ Zoom In',
			a_t: '\uD83D\uDD0D- Zoom Out',
			
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
