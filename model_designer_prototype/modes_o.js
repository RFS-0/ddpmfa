(function(a_e) {
	'use strict';
	if (typeof a_e.snOoPy == 'undefined') a_e.snOoPy = {};
	if (typeof a_e.snOoPy.SNooPY == 'undefined') a_e.snOoPy.SNooPY = {};
})(window);




(function(a_d, a_e) {
	'use strict';
	if (typeof a_d.a_br == 'undefined') {
		a_d.a_br = function() {
			this.a_I = [{
				a_bI: this,
				a_fv: a_d.a_br.a_I.a_ft,
				a_fu: -1
			}];
		};
		
		a_d.a_br.prototype.a_8 = function() { return this.a_I[0]; };
		
		a_d.a_br.prototype.a_bp = function() {
			var a_I = this.a_8();
			
			if (a_I.a_fu + 1 > a_d.a_br.a_fr) {
				a_I.a_fu = 0;
				a_I.a_fv += a_d.a_br.a_fs;
			} else {
				++a_I.a_fu;
			}
			
			return a_I.a_fv + a_I.a_fu;
		};
		
		a_d.a_br.a_I = {
			a_ft: 'u',
			a_fs: 'x',
			a_fr: 999999999,
			a_fq: null
		};
		
		a_d.a_br.a_bq = function() {
			if (a_d.a_br.a_I.a_fq == null) {
				a_d.a_br.a_I.a_fq = new a_d.a_br();
			}
			return a_d.a_br.a_I.a_fq;
		};
	}
})(window.snOoPy.SNooPY, window);




(function(a_d, a_e) {
	'use strict';
	if (typeof a_d.a_cE == 'undefined') {
		a_d.a_cE = function(a_fp) {
			this.a_I = [{
				a_bI: this,
				a_fp: a_fp
			}];
		};
		
		a_d.a_cE.prototype.a_8 = function() { return this.a_I[0]; };
		
		a_d.a_cE.prototype.a_cC = function(a_e4) {
			var a_I = this.a_8();
			var a_fn = '';
			for (var a_bz = 0; a_bz < a_I.a_fp.length; ++a_bz) {
				var a_fo = a_I.a_fp[a_bz];
				if (a_bz % 2 == 0) {
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
			this.a_I = [{
				a_bI: this,
				
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
		
		a_d.a_eF.prototype.a_8 = function() { return this.a_I[0]; };
		
		a_d.a_eF.prototype.a_e9 = function() { return this.a_8().a_fj; };
		
		a_d.a_eF.prototype.a_fi = function() { return this.a_8().a_fh; };
		
		a_d.a_eF.prototype.a_e6 = function() { return this.a_8().a_fd; };
		
		a_d.a_eF.prototype.a_eU = function(a_dX) {
			var a_I = this.a_8();
			return a_I.a_fg(a_I.a_ff * a_dX, a_I.a_fe, a_I.a_fd);
		};
	}
})(window.snOoPy.SNooPY, window);




(function(a_d, a_e) {
	'use strict';
	if (typeof a_d.a_ey == 'undefined') {
		a_d.a_ey = function(a_eY, a_eD, a_eC) {
			this.a_I = [{
				a_bI: this,
				a_eY: a_eY,
				a_eD: a_eD,
				a_eC: a_eC,
				
				a_fc: null,
				a_fa: null,
				a_e3: null,
				a_e1: null,
				
				a_e8: function(a_dX) {
					return a_dX ? a_d.a_ey.a_I.a_eH : a_d.a_ey.a_I.a_eG;
				},
				
				a_eR: function(a_dX) {
					var a_I = this;
					if (a_I.a_fc == null) {
						a_I.a_fc = new a_d.a_cE(a_d.a_ey.a_I.a_eQ.slice());
					}
					var a_e4 = {};
					a_e4[a_d.a_ey.a_I.a_eJ] = a_dX;
					return a_I.a_fc.a_cC(a_e4);
				},
				
				a_eX: function(a_fb) {
					var a_I = this;
					if (a_I.a_fa == null) {
						a_I.a_fa = new a_d.a_cE(a_d.a_ey.a_I.a_eP.slice());
					}
					var a_e4 = {};
					a_e4[a_d.a_ey.a_I.a_eL] = a_fb;
					a_e4[a_d.a_ey.a_I.a_eM] = a_I.a_eY;
					return a_I.a_fa.a_cC(a_e4);
				},
				
				a_e2: function(a_e5, a_dX, a_e7) {
					var a_I = this;
					var a_e4 = {};
					a_e4[a_d.a_ey.a_I.a_eJ] = a_dX;
					a_e4[a_d.a_ey.a_I.a_eK] = a_e7.a_e9();
					a_e4[a_d.a_ey.a_I.a_eI] = a_I.a_e8(a_e7.a_e6());
					return a_e5.a_cC(a_e4);
				},
				
				a_eV: function(a_dX) {
					var a_I = this;
					if (a_I.a_e3 == null) {
						a_I.a_e3 = new a_d.a_cE(a_d.a_ey.a_I.a_eO.slice());
					}
					return a_I.a_e2(a_I.a_e3, a_dX, a_I.a_eD);
				},
				
				a_eS: function(a_dX) {
					var a_I = this;
					if (a_I.a_e1 == null) {
						a_I.a_e1 = new a_d.a_cE(a_d.a_ey.a_I.a_eN.slice());
					}
					return a_I.a_e2(a_I.a_e1, a_dX, a_I.a_eC);
				}
			}];
		};
		
		a_d.a_ey.prototype.a_8 = function() { return this.a_I[0]; };
		
		a_d.a_ey.prototype.a_ck = function(a_eu) {
			var a_I = this.a_8();
			
			var a_e0 = (new RegExp('^-?(0|[1-9][0-9]*)(\\.[0-9]+)?$')).exec(a_eu);
			var a_eZ = 2;
			if (a_e0) {
				var a_eW = 0;
				if (a_e0[a_eZ]) {
					a_eW = a_e0[a_eZ].length - 1;
				}
				if (a_I.a_eY >= 0 && a_eW > a_I.a_eY) {
					return a_I.a_eX(a_eW);
				}
				
				var a_eT = Number.parseFloat(a_eu);
				
				if (a_I.a_eD != null && !a_I.a_eD.a_eU(a_eT)) {
					return a_I.a_eV(a_eu);
				}
				if (a_I.a_eC != null && !a_I.a_eC.a_eU(a_eT)) {
					return a_I.a_eS(a_eu);
				}
				
			} else {
				return a_I.a_eR(a_eu);
			}
		};
		
		a_d.a_ey.a_I = {
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
			this.a_I = [{
				a_bI: this,
				a_eA: {}
			}];
		};
		
		a_d.a_r.prototype.a_8 = function() { return this.a_I[0]; };
		
		a_d.a_r.prototype.a_j = function(a_dg, a_eB) {
			this.a_8().a_eA[a_dg] = a_eB;
		};
		
		a_d.a_r.prototype.a_ez = function(a_dg, a_c2, a_b7, a_c3, a_df, a_dd) {
			var a_I = this.a_8();
			if (typeof a_I.a_eA[a_dg] == 'undefined') {
				throw 'Unknown field type "' + a_dg + '" in a_r.a_ez(...)';
			}
			return a_I.a_eA[a_dg].a_ez(a_dg, a_c2, a_b7, a_c3, a_df, a_dd);
		};
		
		a_d.a_r.prototype.a_cb = function(a_da) {
			return this.a_ez(a_da.fieldType, a_da.fieldArgs, a_da.propName, a_da.label, a_da.valueData, a_da.dirty);
		};
	}
})(window.snOoPy.SNooPY, window);




(function(a_d, a_e) {
	'use strict';
	if (typeof a_d.a_q == 'undefined') {
		a_d.a_q = function() {
			this.a_I = [{ a_bI: this }];
		};
		
		a_d.a_q.prototype.a_8 = function() { return this.a_I[0]; };
		
		a_d.a_q.prototype.a_ez = function(a_dg, a_c2, a_b7, a_c3, a_df, a_dd) {
			return new a_d.a_p(a_dg, a_c2, a_b7, a_c3, a_df, a_dd);
		};
		
		a_d.a_q.prototype.a_cb = function(a_da) {
			return this.a_ez(a_da.fieldType, a_da.fieldArgs, a_da.propName, a_da.label, a_da.valueData, a_da.dirty);
		};
	}
})(window.snOoPy.SNooPY, window);




(function(a_d, a_e) {
	'use strict';
	if (typeof a_d.a_n == 'undefined') {
		a_d.a_n = function() {
			this.a_I = [{ a_bI: this }];
		};
		
		a_d.a_n.prototype.a_8 = function() { return this.a_I[0]; };
		
		a_d.a_n.prototype.a_ez = function(a_dg, a_c2, a_b7, a_c3, a_df, a_dd) {
			return new a_d.a_m(a_dg, a_c2, a_b7, a_c3, a_df, a_dd);
		};
		
		a_d.a_n.prototype.a_cb = function(a_da) {
			return this.a_ez(a_da.fieldType, a_da.fieldArgs, a_da.propName, a_da.label, a_da.valueData, a_da.dirty);
		};
	}
})(window.snOoPy.SNooPY, window);




(function(a_d, a_e) {
	'use strict';
	if (typeof a_d.a_k == 'undefined') {
		a_d.a_k = function(a_bJ) {
			this.a_I = [{
				a_bI: this,
				a_bJ: a_bJ
			}];
		};
		
		a_d.a_k.prototype.a_8 = function() { return this.a_I[0]; };
		
		a_d.a_k.prototype.a_ez = function(a_dg, a_c2, a_b7, a_c3, a_df, a_dd) {
			var a_I = this.a_8();
			return new a_d.a_i(a_I.a_bJ, a_dg, a_c2, a_b7, a_c3, a_df, a_dd);
		};
		
		a_d.a_k.prototype.a_cb = function(a_da) {
			return this.a_ez(a_da.fieldType, a_da.fieldArgs, a_da.propName, a_da.label, a_da.valueData, a_da.dirty);
		};
	}
})(window.snOoPy.SNooPY, window);




(function(a_d, a_e) {
	'use strict';
	if (typeof a_d.a_p == 'undefined') {
		a_d.a_p = function(a_dg, a_c2, a_b7, a_c3, a_df, a_dd) {
			this.a_I = [{
				a_bI: this,
				a_dg: a_dg,
				a_c2: a_c2,
				a_b7, a_b7,
				a_c3: a_c3,
				a_d3: a_df,
				a_dX: a_df,
				a_de: a_dd,
				
				a_ej: null,
				a_dW: null,
				a_ei: null,
				
				a_ev: null,
				
				a_ew: function() {
					var a_I = this;
					if (a_I.a_c2.numberConfig == null) return null;
					if (a_I.a_ev == null) {
						a_I.a_ev = a_d.a_ey.a_ex(a_I.a_c2.numberConfig);
					}
					return a_I.a_ev;
				},
				
				a_ee: function(a_eu) {
					var a_I = this;
					var a_ev = a_I.a_ew();
					return a_ev == null ? null : a_ev.a_ck(a_eu);
				},
				
				a_eq: function(a_ep) {
					return a_d.a_p.a_I.a_d5 + a_ep + a_d.a_p.a_I.a_d4;
				},
				
				a_el: function(a_cs) {
					var a_I = this;
					a_cs.removeClass(a_I.a_eq(a_d.a_p.a_I.a_et)).removeClass(a_I.a_eq(a_d.a_p.a_I.a_es)).removeClass(a_I.a_eq(a_d.a_p.a_I.a_er));
				},
				
				a_em: function(a_ef, a_ep) {
					var a_I = this;
					if (a_I.a_ej != null) {
						a_I.a_el(a_I.a_ej);
						a_I.a_ej.addClass(a_I.a_eq(a_ep));
						
						if (a_I.a_ei == null) {
							a_I.a_ei = jQuery('<span class="help-block"></span>');
							a_I.a_ej.append(a_I.a_ei);
						}
						a_I.a_ei.text(a_ef);
					}
				},
				
				a_ed: function(a_ef) {
					this.a_em(a_ef, a_d.a_p.a_I.a_d8);
				},
				
				a_eo: function(a_ef) {
					this.a_em(a_ef, a_d.a_p.a_I.a_d7);
				},
				
				a_en: function(a_ef) {
					this.a_em(a_ef, a_d.a_p.a_I.a_d6);
				},
				
				a_eg: function() {
					var a_I = this;
					if (a_I.a_ej != null) {
						a_I.a_el(a_I.a_ej);
						
						if (a_I.a_ei != null) {
							a_I.a_ei.remove();
							a_I.a_ei = null;
						}
					}
				},
			}];
		};
		
		a_d.a_p.prototype.a_8 = function() { return this.a_I[0]; };
		
		a_d.a_p.prototype.a_cm = function(a_ce) {
			var a_I = this.a_8();
			var a_ek = a_d.a_br.a_bq().a_bp();
			var a_ej = jQuery('<div class="form-group"></div>');
			var a_dZ = jQuery('<label class="control-label"></label>')
				.attr('for', a_ek)
				.text(a_I.a_c3);
			var a_dW = a_I.a_c2.displayAsTextArea
				? a_dW = jQuery('<textarea class="form-control"></textarea>')
				: a_dW = jQuery('<input type="text" class="form-control" />');
			a_dW
				.attr('id', a_ek)
				.val(a_I.a_dX);
			a_ej.append(a_dZ);
			a_ej.append(a_dW);
			a_ce.append(a_ej);
			
			a_I.a_ej = a_ej;
			a_I.a_dW = a_dW;
		};
		
		a_d.a_p.prototype.a_cS = function() {
			var a_I = this.a_8();
			a_I.a_ej = null;
			a_I.a_dW = null;
			a_I.a_ei = null;
		};
		
		a_d.a_p.prototype.a_bY = function() {
			var a_I = this.a_8();
			a_I.a_dX = a_I.a_dW.val();
		};
		
		a_d.a_p.prototype.a_cA = function() {
			var a_I = this.a_8();
			var a_eh = {
				fieldType: a_I.a_dg,
				fieldArgs: a_I.a_c2,
				propName: a_I.a_b7,
				label: a_I.a_c3,
				valueData: a_I.a_dX,
				dirty: this.a_cR()
			};
			return a_eh;
		};
		
		a_d.a_p.prototype.a_cR = function() {
			var a_I = this.a_8();
			return a_I.a_de || a_I.a_dX != a_I.a_d3;
		};
		
		a_d.a_p.prototype.a_cQ = function(a_cP) {
			var a_I = this.a_8();
			a_I.a_de = false;
			a_I.a_d3 = a_I.a_dX;
		};
		
		a_d.a_p.prototype.a_ck = function() {
			var a_I = this.a_8();
			a_I.a_eg();
			if (a_I.a_c2.notEmpty && a_I.a_dX.length == 0) {
				var a_ef = a_d.a_p.a_I.a_eb;
				a_I.a_ed(a_ef);
				return a_ef;
			}
			if (a_I.a_c2.maxLength != -1 && a_I.a_dX.length > a_I.a_c2.maxLength) {
				var a_ef = a_d.a_p.a_I.a_ea + a_I.a_c2.maxLength + a_d.a_p.a_I.a_d9;
				a_I.a_ed(a_ef);
				return a_ef;
			}
			
			var a_ec = a_I.a_ee(a_I.a_dX);
			if (a_ec != null) {
				a_I.a_ed(a_ec);
				return a_ec;
			}
			
			return null;
		};
		
		a_d.a_p.a_I = {
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
		a_d.a_m = function(a_dg, a_c2, a_b7, a_c3, a_df, a_dd) {
			this.a_I = [{
				a_bI: this,
				a_dg: a_dg,
				a_c2: a_c2,
				a_b7, a_b7,
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
		
		a_d.a_m.prototype.a_8 = function() {
			return this.a_I[0];
		};
		
		a_d.a_m.prototype.a_cm = function(a_ce) {
			var a_I = this.a_8();
			
			var a_L = jQuery('<div class="checkbox"></div>');
			a_ce.append(a_L);
			
			var a_dZ = jQuery('<label></label>').text(a_I.a_c3);
			a_L.append(a_dZ);
			
			a_I.a_dW = jQuery('<input type="checkbox" />');
			a_L.prepend(a_I.a_dW);
			
			a_I.a_dY(a_I.a_dW, a_I.a_dX);
		};
		
		a_d.a_m.prototype.a_cS = function() {
			var a_I = this.a_8();
			a_I.a_dW = null;
		};
		
		a_d.a_m.prototype.a_bY = function() {
			var a_I = this.a_8();
// TODO
		};
		
		a_d.a_m.prototype.a_cA = function() {
			var a_I = this.a_8();
// TODO
		};
		
		a_d.a_m.prototype.a_cR = function() {
			var a_I = this.a_8();
// TODO
		};
		
		a_d.a_m.prototype.a_cQ = function(a_cP) {
			var a_I = this.a_8();
// TODO
		};
		
		a_d.a_m.prototype.a_ck = function() {
			var a_I = this.a_8();
// TODO
			return null;
		};
		
		a_d.a_m.a_h = 'CHECK';
	}
})(window.snOoPy.SNooPY, window);




(function(a_d, a_e) {
	'use strict';
	if (typeof a_d.a_cG == 'undefined') {
		a_d.a_cG = function(a_dE, a_ch, a_c3, a_b9) {
			this.a_I = [{
				a_bI: this,
				a_dE: a_dE,
				a_ch: a_ch,
				a_c3: a_c3,
				a_b9: a_b9,
				
				a_c6: null,
				a_dq: null,
				a_L: null,
				a_dp: null,
				a_do: null,
				
				a_du: function() {
					return jQuery('<div class="panel panel-default"></div>').addClass(a_d.a_cG.a_I.a_bX);
				},
				
				a_ds: function() {
					var a_I = this;
					
					var a_b3 = jQuery('<div class="panel-heading"></div>').addClass(a_d.a_cG.a_I.a_bW).text(a_I.a_c3);
					a_I.a_L.append(a_b3);
					
					var a_cX = jQuery('<div class="panel-body"></div>').addClass(a_d.a_cG.a_I.a_cN);
					a_I.a_L.append(a_cX);
					
					var a_dS = jQuery('<div class="btn-group"></div>').addClass(a_d.a_cG.a_I.a_dn);
					a_cX.append(a_dS);
					
					var a_dU = jQuery('<button class="btn btn-default"></button>').addClass(a_d.a_cG.a_I.a_dV).text(a_d.a_cG.a_I.a_di);
					a_dS.append(a_dU);
					a_I.a_dp = a_dU;
					a_dU.click(function() { a_I.a_dJ(); });
					
					var a_dR  = jQuery('<button class="btn btn-default"></button>').addClass(a_d.a_cG.a_I.a_dT).text(a_d.a_cG.a_I.a_dh);
					a_dS.append(a_dR);
					a_I.a_do = a_dR;
					a_dR.click(function() { a_I.a_dI(); });
					
					a_I.a_bI.a_c8();
					
					var a_dQ = jQuery('<div></div>').addClass(a_d.a_cG.a_I.a_dj);
					a_cX.append(a_dQ);
					
					for (var a_bz = 0; a_bz < a_I.a_b9.length; ++a_bz) {
						a_I.a_b9[a_bz].a_cm(a_dQ);
					}
				},
				
				a_dH: function(a_dP) {
					var a_I = this;
					
					if (a_dP) {
						if (a_I.a_c6 != null) {
							var a_dO = a_I.a_c6;
							var a_dN = a_dO.a_dA();
							var a_dM = a_I.a_dq;
							
							a_I.a_L.insertBefore(a_dO.a_dy());
							
							a_I.a_bI.a_c7(a_dN);
							a_I.a_bI.a_c9(a_dO);
							
							a_dO.a_c7(a_I.a_bI);
							a_dO.a_c9(a_dM);
							
							a_I.a_bI.a_c8();
							a_dO.a_c8();
							
							if (a_dN != null) {
								a_dN.a_c9(a_I.a_bI);
								a_dN.a_c8();
							}
							
							if (a_dM != null) {
								a_dM.a_c7(a_dO);
								a_dM.a_c8();
							}
						}
					} else {
						if (a_I.a_dq != null) {
							var a_dO = a_I.a_dq;
							var a_dN = a_I.a_c6;
							var a_dM = a_dO.a_dz();
							
							a_I.a_L.insertAfter(a_dO.a_dy());
							
							a_I.a_bI.a_c7(a_dO);
							a_I.a_bI.a_c9(a_dM);
							
							a_dO.a_c7(a_dN);
							a_dO.a_c9(a_I.a_bI);
							
							a_I.a_bI.a_c8();
							a_dO.a_c8();
							
							if (a_dN != null) {
								a_dN.a_c9(a_dO);
								a_dN.a_c8();
							}
							
							if (a_dM != null) {
								a_dM.a_c7(a_I.a_bI);
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
		
		a_d.a_cG.prototype.a_8 = function() { return this.a_I[0]; };
		
		a_d.a_cG.prototype.a_dG = function(a_dE) { this.a_8().a_dE = a_dE; };
		
		a_d.a_cG.prototype.a_dF = function() { return this.a_8().a_dE; };
		
		a_d.a_cG.prototype.a_ci = function(a_ch) { this.a_8().a_ch = a_ch; };
		
		a_d.a_cG.prototype.a_dD = function() { return this.a_8().a_ch; };
		
		a_d.a_cG.prototype.a_dC = function() { return this.a_8().a_c3; };
		
		a_d.a_cG.prototype.a_dB = function() { return this.a_8().a_b9; };
		
		a_d.a_cG.prototype.a_c7 = function(a_c6) { this.a_8().a_c6 = a_c6; };
		
		a_d.a_cG.prototype.a_dA = function() { return this.a_8().a_c6; };
		
		a_d.a_cG.prototype.a_c9 = function(a_dq) { this.a_8().a_dq = a_dq; };
		
		a_d.a_cG.prototype.a_dz = function() { return this.a_8().a_dq; };
		
		a_d.a_cG.prototype.a_dy = function() {
			return this.a_8().a_L;
		};
		
		a_d.a_cG.prototype.a_cV = function(a_ce) {
			var a_I = this.a_8();
			a_I.a_L = a_I.a_du();
			a_ce.append(a_I.a_L);
			a_I.a_ds();
		};
		
		a_d.a_cG.prototype.a_dx = function(a_dw) {
			var a_I = this.a_8();
			a_I.a_L = a_I.a_du();
			a_I.a_L.insertBefore(a_dw);
			a_I.a_ds();
		};
		
		a_d.a_cG.prototype.a_dv = function(a_dt) {
			var a_I = this.a_8();
			a_I.a_L = a_I.a_du();
			a_I.a_L.insertAfter(a_dt);
			a_I.a_ds();
		};
		
		a_d.a_cG.prototype.a_c8 = function() {
			var a_I = this.a_8();
			a_I.a_dr(a_I.a_dp, a_I.a_c6 != null);
			a_I.a_dr(a_I.a_do, a_I.a_dq != null);
		};
		
		a_d.a_cG.prototype.a_cS = function() {
			var a_I = this.a_8();
			a_I.a_L = null;
			a_I.a_dp = null;
			a_I.a_do = null;
		};
		
		a_d.a_cG.prototype.a_cA = function() {
// TODO
		};
		
		a_d.a_cG.a_I = {
			a_bX: 'rgm-modes-subform-container',
			a_bW: 'rgm-modes-subform-title',
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
		a_d.a_i = function(a_bJ, a_dg, a_c2, a_b7, a_c3, a_df, a_dd) {
// TODO: remove subforms
			this.a_I = [{
				a_bI: this,
				a_bJ: a_bJ,
				a_dg: a_dg,
				a_c2: a_c2,
				a_b7, a_b7,
				a_c3: a_c3,
				a_dc: a_df,
				a_de: a_dd,
				
				a_cU: null,
				a_cW: [],
				a_c5: {},
				
				a_c4: function() {
					var a_I = this;
					
					var a_c6 = null;
					for (var a_bz = 0; a_bz < a_I.a_dc.length; ++a_bz) {
						var a_c0 = a_I.a_dc[a_bz];
						
						var a_b9 = [];
						for (var a_db = 0; a_db < a_c0.fields.length; ++a_db) {
							var a_da = a_c0.fields[a_db];
							var a_b6 = a_I.a_bJ.a_cb(a_da);
							a_b9.push(a_b6);
						}
						
						var a_cT = new a_d.a_cG(a_c0.id, a_c0.tempId, a_c0.label, a_b9);
						
						if (a_bz > 0) {
							a_cT.a_c7(a_c6);
							a_c6.a_c9(a_cT);
						}
						
						a_I.a_cW.push(a_cT);
						a_c6 = a_cT;
					}
				},
				
				a_c1: function(a_c0) {
					var a_I = this;
					
					var a_ch = a_d.a_i.a_I.a_cH + a_d.a_br.a_bq().a_bp();
					
					var a_b9 = [];
					for (var a_bz = 0; a_bz < a_c0.fields.length; ++a_bz) {
						var a_da = a_c0.fields[a_bz];
						var a_b6 = a_I.a_bJ.a_cb(a_da);
						a_b9.push(a_b6);
					}
					
					var a_cT = new a_d.a_cG(a_c0.id, a_ch, a_c0.label, a_b9);
					
					if (a_I.a_cW.length > 0) {
						var a_c6 = a_I.a_cW[a_I.a_cW.length - 1];
						a_c6.a_c9(a_cT);
						a_c6.a_c8();
						a_cT.a_c7(a_c6);
					}
					
					a_cT.a_cV(a_I.a_cU);
					
					a_I.a_cW.push(a_cT);
					a_I.a_c5[a_ch] = a_cT;
				}
			}];
			this.a_I[0].a_c4();
		};
		
		a_d.a_i.prototype.a_8 = function() { return this.a_I[0]; };
		
		a_d.a_i.prototype.a_cm = function(a_ce) {
			var a_I = this.a_8();
			var a_bz = 0;
			
			var a_L = jQuery('<div class="panel panel-default"></div>').addClass(a_d.a_i.a_I.a_bX);
			a_ce.append(a_L);
			
			var a_b3 = jQuery('<div class="panel-heading"></div>').addClass(a_d.a_i.a_I.a_bW);
			a_b3.text(a_I.a_c3);
			a_L.append(a_b3);
			
			var a_cX = jQuery('<div class="panel-body"></div>').addClass(a_d.a_i.a_I.a_cN);
			a_L.append(a_cX);
			
			var a_cZ = jQuery('<div class="btn-group-vertical"></div>').addClass(a_d.a_i.a_I.a_cM);
			a_cX.append(a_cZ);
			
			for (a_bz = 0; a_bz < a_I.a_c2.forms.length; ++a_bz) {(function(a_bz) {
				var a_c0 = a_I.a_c2.forms[a_bz];
				
				var a_cY = jQuery('<button class="btn btn-default"></button>').addClass(a_d.a_i.a_I.a_cL).text(a_d.a_i.a_I.a_cJ + a_c0.label + a_d.a_i.a_I.a_cI);
				a_cY.click(function() { a_I.a_c1(a_c0); });
				a_cZ.append(a_cY);
			})(a_bz);}
			
			var a_cU = jQuery('<div></div>').addClass(a_d.a_i.a_I.a_cK);
			a_cX.append(a_cU);
			
			for (a_bz = 0; a_bz < a_I.a_cW.length; ++a_bz) {
				var a_cT = a_I.a_cW[a_bz];
				a_cT.a_cV(a_cU);
			}
			
			a_I.a_cU = a_cU;
		};
		
		a_d.a_i.prototype.a_cS = function() {
			var a_I = this.a_8();
			a_I.a_cU = null;
			for (a_bz = 0; a_bz < a_I.a_cW.length; ++a_bz) {
				var a_cT = a_I.a_cW[a_bz];
				a_cT.a_cV(a_cU);
				a_cT.a_cS();
			}
		};
		
		a_d.a_i.prototype.a_bY = function() {
			var a_I = this.a_8();
// TODO
		};
		
		a_d.a_i.prototype.a_cA = function() {
			var a_I = this.a_8();
// TODO
		};
		
		a_d.a_i.prototype.a_cR = function() {
			var a_I = this.a_8();
// TODO
		};
		
		a_d.a_i.prototype.a_cQ = function(a_cP) {
			var a_I = this.a_8();
// TODO
		};
		
		a_d.a_i.prototype.a_ck = function() {
			var a_I = this.a_8();
// TODO
		};
		
		a_d.a_i.a_I = {
			a_bX: 'rgm-modes-forms-field-container',
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
	
	if (typeof a_d.a_bL == 'undefined') {
		a_d.a_bL = function(a_bK, a_bD, a_bJ, a_M, a_b2) {
// TODO (Could): a_bL should work like a_cG: unpack/repack a_bK
			this.a_I = [{
				a_bI: this,
				a_bK: a_bK,
				a_bD: a_bD,
				a_bJ: a_bJ,
				a_M: a_M,
				a_b2: a_b2,
				
				a_L: null,
				a_b3: null,
				
				a_b9: [],
				a_co: {},
				
				a_bv: null,
				
				a_cD: null,
				
				a_cl: function(a_b4) {
					var a_I = this;
					if (a_I.a_cF == null) {
						a_I.a_cD = new a_d.a_cE(a_d.a_bL.a_I.a_bS);
					}
					var a_cB ={};
					a_cB[a_d.a_bL.a_I.a_bR] = a_b4;
					return a_I.a_cD.a_cC(a_cB);
				},
				
				a_cw: function(a_cz, a_cp) {
					var a_I = this;
					var a_b6 = a_I.a_cq(a_cz[0], null);
					if (a_b6 == null) return a_cp;
					var a_cx = a_b6.a_cA();
					for (var a_bz = 1; a_bz < a_cz.length; ++a_bz) {
						var a_cy = a_cz[a_bz];
						if (typeof a_cx[a_cy] == 'undefined') {
							return a_cp;
						}
						a_cx = a_cx[a_cy];
					}
					return a_cx;
				},
				
				a_cj: function() {
					var a_I = this;
					a_I.a_b3.text(a_I.a_b5());
				},
				
				a_b5: function() {
					var a_I = this;
					return a_I.a_cw(a_I.a_bK.titleLabelPath, '');
				},
				
				a_cg: function(a_cs, a_cu, a_cv) {
					a_cs.css({ top: a_cv + 'px', left: a_cu + 'px' });
				},
				
				a_ct: function(a_cs) {
// TODO
				},
				
				a_cf: function(a_cs, a_cr) {
					for (var a_bz = 0; a_bz < a_cr.length; ++a_bz) {
						a_cs.addClass(a_cr[a_bz]);
					}
				},
				
				a_b8: function(a_b7, a_b6) {
					var a_I = this;
					a_I.a_co['pn' + a_b7] = a_b6;
				},
				
				a_cq: function(a_b7, a_cp) {
					var a_I = this;
					var a_cn = 'pn' + a_b7;
					if (typeof a_I.a_co[a_cn] == 'undefined') return a_cp;
					return a_I.a_co[a_cn];
				},
				
				a_cd: function() {
					var a_I = this;
					a_I.a_M.a_bg(
						function(a_9, a_be, a_bd, a_bc, a_bb) {
							for (var a_bz = 0; a_bz < a_I.a_b9.length; ++a_bz) {
								var a_b6 = a_I.a_b9[a_bz];
								a_b6.a_cm(a_bd);
							}
							a_be.text(a_I.a_cl(a_I.a_b5()));
							a_bb.text(a_d.a_bL.a_I.a_bT);
						},
						function() { return a_I.a_bk(); }
					);
				},
				
				a_bk: function() {
					var a_I = this;
					for (var a_bz = 0; a_bz < a_I.a_b9.length; ++a_bz) {
						var a_b6 = a_I.a_b9[a_bz];
						a_b6.a_bY();
						if (a_b6.a_ck() != null) {
							return false;
						}
					}
					a_I.a_cj();
					return true;
				}
			}];
		};
		
		a_d.a_bL.prototype.a_8 = function() {
			return this.a_I[0];
		};
		
		a_d.a_bL.prototype.a_ci = function(a_ch) {
			var a_I = this.a_8();
			a_I.a_bK.tempId = a_ch;
		};
		
		a_d.a_bL.prototype.a_O = function(a_ce, a_bv) {
			var a_I = this.a_8();
			var a_bz = 0;
			
			a_I.a_bv = a_bv;
			
			a_I.a_L = jQuery('<div></div>').addClass(a_d.a_bL.a_I.a_bX).attr('id', a_I.a_bD);
			a_I.a_cg(a_I.a_L, a_I.a_bK.position.x, a_I.a_bK.position.y);
			a_I.a_cf(a_I.a_L, a_I.a_bK.classes);
			a_ce.append(a_I.a_L);
			
			var a_cc = jQuery('<span></span>').addClass(a_d.a_bL.a_I.a_bV);
			a_cc.click(function() { a_I.a_cd(); });
			a_I.a_L.append(a_cc);
			
			for (a_bz = 0; a_bz < a_I.a_bK.fields.length; ++a_bz) {
				var a_ca = a_I.a_bK.fields[a_bz];
				var a_b6 = a_I.a_bJ.a_cb(a_ca);
				var a_b7 = a_ca.propName;
				a_I.a_b9.push(a_b6);
				a_I.a_b8(a_b7, a_b6);
			}
			
			var a_b4 = a_I.a_b5();
			a_I.a_b3 = jQuery('<div></div>').addClass(a_d.a_bL.a_I.a_bW).text(a_b4);
			a_I.a_L.append(a_I.a_b3);
			
			a_I.a_bv.draggable(a_I.a_L);
			
			if (a_I.a_bK.maxOutgoing != 0) {
				for (var a_bz = 0; a_bz < a_I.a_b2.length; ++a_bz) {
					var a_bx = a_I.a_b2[a_bz];
					var a_bZ = a_d.a_bL.a_I.a_bU + a_bx.typeName;
					
					var a_b1 = jQuery('<div></div>').addClass(a_bZ);
// TODO: Add data so that we can later know which type of connection was created?
					a_I.a_L.append(a_b1);
					
					var a_b0 = a_I.a_bv.makeSource(a_I.a_L, {
						filter: '.' + a_bZ,
						anchor: 'Continuous',
						connectorStyle: { stroke: '#000000', strokeWidth: 2, outlineStroke: 'transparent', outlineWidth: 4 },
						connectionType: a_bx.typeName,
						maxConnections: a_I.a_bK.maxOutgoing
					});
				}
			}
			
			if (a_I.a_bK.maxIncoming != 0) {
				a_I.a_bv.makeTarget(a_I.a_L, {
					anchor: 'Continuous',
					allowLoopback: false
				});
			}
		};
		
		a_d.a_bL.prototype.a_bY = function() {
// TODO
// - sync (directly into nodeData):
//   - position
//   - fields
		};
		
		a_d.a_bL.a_I = {
			a_bX: 'rgm-modes-node-container',
			a_bW: 'rgm-modes-node-title',
			a_bV: 'rgm-modes-node-configure-button',
			a_bU: 'rgm-modes-node-source-endpoint-',
			a_bT: 'OK',
			a_bS: ['Configure "', 'titleLabel', '"'],
			a_bR: 'titleLabel'
		};
	}
})(window.snOoPy.SNooPY, window);




(function(a_d, a_e) {
	'use strict';
	if (typeof a_d.a_c == 'undefined') {
		a_d.a_c = function(a_bJ) {
			this.a_I = [{
				a_bI: this,
				a_bJ: a_bJ,
				
				a_L: null,
				a_4: null,
				a_9: null,
				a_be: null,
				a_bd: null,
				a_bc: null,
				a_bb: null,
				a_ba: null,
				
				a_1: null,
				
				a_bH: [],
				a_bG: {},
				a_bE: [],
				
				a_bv: null,
				a_bM: false,
				
				a_bw: function(a_bt, a_bs) {
					var a_I = this;
					if (a_bs) {
					
// TODO implement (the following is demo code)
						var a_bQ = a_I.a_bG[a_bt.sourceId];
						var a_bP = a_I.a_bG[a_bt.targetId];
						var a_bN = a_bt.connection;
						a_bN.setLabel('Here some label');
						// a_I.a_bO(a_bN);						
					}
				},
				
				a_bu: function(a_bt, a_bs) {
					var a_I = this;
					if (a_I.a_bM) return;
// TODO
					alert('Connection detached');
				},
				
				a_bO: function(a_bN) {
					var a_I = this;
					a_I.a_bM = true;
					a_I.a_bv.deleteConnection(a_bN);
					a_I.a_bM = false;
				},
				
				a_T: function() {
					var a_I = this;
					
					for (var a_bz = 0; a_bz < a_I.a_1.nodes.length; ++a_bz) {(function(a_bz) {
						var a_bD = a_d.a_c.a_I.a_x + a_d.a_br.a_bq().a_bp();
						
						var a_bK = a_I.a_1.nodes[a_bz];
						var a_bF = new a_d.a_bL(a_bK, a_bD, a_I.a_bJ, a_I.a_bI, a_I.a_1.connectionTypes);
						a_bF.a_O(a_I.a_4, a_I.a_bv);
						a_I.a_bH.push(a_bF);
						a_I.a_bG[a_bD] = a_bF;
						a_I.a_bE.push(a_bD);
					})(a_bz);}
				},
				
				a_bB: function(a_bA) {
					var a_4 = jQuery('<div></div>').addClass(a_d.a_c.a_I.a_w + a_bA);
					var a_bC = jQuery('<div></div>');
					a_bC.append(a_4);
					return a_bC;
				},
				
				a_by: function(a_bv, a_bx) {
					var a_I = this;
					
					var a_bA = a_bx.typeName;
					
					a_bv.registerConnectionType(a_bA, {
						anchor: 'Continuous',
						connector: 'StateMachine',
						hoverPaintStyle:{ stroke: '#00ff00', strokeWidth: 2 },
						overlays: [
							['Arrow', { width:10, length: 14, foldback: 0.8, location:1, id: 'arrow' } ],
							['Custom', {
								create: function(component) { return a_I.a_bB(a_bA) },
								location: 0.7,
								id: 'typeOverlay'
							}]
						]
					});
				},
				
				a_Z: function() {
					var a_I = this;
					for (var a_bz = 0; a_bz < a_I.a_1.connectionTypes.length; ++a_bz) {
						var a_bx = a_I.a_1.connectionTypes[a_bz];
						a_I.a_by(a_I.a_bv, a_bx);
					}
				},
				
				a_0: function() {
					var a_I = this;
					
					if (a_I.a_bv == null) {
// TODO: clean
						a_I.a_bv = jsPlumb.getInstance({
							Endpoint: ['Dot', {radius: 2}],
							Connector: 'StateMachine',
							Container: a_I.a_4
						});
					
						a_I.a_bv.bind('connection', function(a_bt, a_bs) {
							a_I.a_bw(a_bt, a_bs);
						});
						
						a_I.a_bv.bind('connectionDetached', function(a_bt, a_bs) {
							a_I.a_bu(a_bt, a_bs);
						});
					}
				},
				
				a_S: function() {
					var a_I = this;
					
					var a_bo = a_d.a_br.a_bq().a_bp();
					
					a_I.a_9 = jQuery('<div class="modal fade" tabindex="-1" role="dialog" data-backdrop="static" data-keyboard="false"></div>').attr('id', a_bo);
				
					var a_bn = jQuery('<div class="modal-dialog" role="document"></div>');
					a_I.a_9.append(a_bn);
					
					var a_bl = jQuery('<div class="modal-content"></div>');
					a_bn.append(a_bl);
					
					var a_bm = jQuery('<div class="modal-header"></div>');
					a_bl.append(a_bm);
					
					a_I.a_be = jQuery('<h1></h1>');
					a_bm.append(a_I.a_be);
					
					a_I.a_bd = jQuery('<div class="modal-body"></div>');
					a_bl.append(a_I.a_bd);
					
					a_I.a_bc = jQuery('<div class="modal-footer"></div>');
					a_bl.append(a_I.a_bc);
					
					a_I.a_bb = jQuery('<button type="button" class="btn btn-default"></button>');
					a_I.a_bc.append(a_I.a_bb);
					
					a_I.a_bb.click(function(event) { return a_I.a_bk(event); });
					
					a_I.a_L.append(a_I.a_9);
					a_I.a_9.modal('hide');
				},
				
				a_bk: function(a_bi) {
					var a_I = this;
					var a_bj = typeof a_I.a_ba != 'function' || a_I.a_ba.apply(a_I.a_9, []);
					if (a_bj) {
						a_I.a_9.modal('hide');
					} else {
						a_bi.preventDefault();
						a_bi.stopImmediatePropagation();
						return false; 
					}
				},
				
				a_bh: function() {
					var a_I = this;
					return a_I.a_4.parents('.' + a_d.a_c.a_I.a_z).length > 0;
				},
				
				a_6: function(a_5) {
					var a_I = this;
					return a_I.a_bh();
				}
			}];
		};
		
		a_d.a_c.prototype.a_8 = function() {
			return this.a_I[0];
		};
				
		a_d.a_c.prototype.a_bg = function(a_bf, a_ba) {
			var a_I = this.a_8();
			a_I.a_be.empty();
			a_I.a_bd.empty();
			a_I.a_bb.empty();
			a_I.a_bc.children().not(a_I.a_bb).remove();
			a_bf.apply(a_I.a_9, [a_I.a_9, a_I.a_be, a_I.a_bd, a_I.a_bc, a_I.a_bb]);
			a_I.a_ba = a_ba;
			a_I.a_9.modal('show');
		};
		
		a_d.a_c.prototype.a_O = function(a_L) {
			var a_I = this.a_8();
			
			a_I.a_L = a_L;
			
			var a_7 = jQuery('<div></div>').addClass(a_d.a_c.a_I.a_G);
			a_I.a_L.append(a_7);
			
			a_I.a_4 = jQuery('<div></div>').addClass(a_d.a_c.a_I.a_F);
			a_7.append(a_I.a_4);
			
			a_I.a_1 = a_I.a_L.data(a_d.a_c.a_I.a_y);
			
			a_I.a_0();
			a_I.a_Z();
			
			var a_Y = jQuery('<div></div>').addClass(a_d.a_c.a_I.a_E);
			a_I.a_L.append(a_Y);
			
			var a_X = jQuery('<div></div>').addClass(a_d.a_c.a_I.a_D);
			a_Y.append(a_X);
			
			var a_W	= jQuery('<button type="button"></button>').addClass(a_d.a_c.a_I.a_C).text(a_d.a_c.a_I.a_v);
			a_X.append(a_W);
			
			var a_V	= jQuery('<button type="button"></button>').addClass(a_d.a_c.a_I.a_B).text(a_d.a_c.a_I.a_u);
			a_X.append(a_V);
			
			var a_U	= jQuery('<button type="button"></button>').addClass(a_d.a_c.a_I.a_A).text(a_d.a_c.a_I.a_t);
			a_X.append(a_U);
			
			a_7.pan({
				mouseControl: 'edge',
				mouseEdgeSpeed: 20,
				beforeEdgeMove: function(a_5) { return a_I.a_6(a_5); }
			});
			
			a_I.a_4.panzoom({
				$zoomIn: a_W,
            	$zoomOut: a_V,
            	$reset: a_U,
            	maxScale: 1
			});
			
			a_I.a_T();
			
			a_I.a_S();
/*			
			
			
			a_I.a_2 = jQuery('<div></div>').addClass(a_d.a_c.a_I.a_3);
			a_I.a_L.append(a_I.a_2);
			
			a_I.a_1 = a_I.a_L.data(a_d.a_c.a_I.a_y);
			
			a_I.a_0();
			a_I.a_Z();
			
			var a_Y = jQuery('<div></div>').addClass(a_d.a_c.a_I.a_E);
// TODO: currently a_Y is added after a_L. Should find way to add everything underneath a common root (including modal)
			a_Y.insertAfter(a_I.a_L);
			
			var a_X = jQuery('<div></div>').addClass(a_d.a_c.a_I.a_D);
			a_Y.append(a_X);
			
			var a_W	= jQuery('<button type="button"></button>').addClass(a_d.a_c.a_I.a_C).text(a_d.a_c.a_I.a_v);
			a_X.append(a_W);
			
			var a_V	= jQuery('<button type="button"></button>').addClass(a_d.a_c.a_I.a_B).text(a_d.a_c.a_I.a_u);
			a_X.append(a_V);
			
			var a_U	= jQuery('<button type="button"></button>').addClass(a_d.a_c.a_I.a_A).text(a_d.a_c.a_I.a_t);
			a_X.append(a_U);
			
// TODO: only activated while dragging
			jQuery('.rgm-modes-container').pan({
				mouseControl: 'edge',
				mouseSpeed: 150
			});

// TODO: Mouse wheel / keyboard shortcuts for zooming
// TODO: Infinite or very large canvas (still don't zoom in too quickly -> step?)
			var containerQ = jQuery('.rgm-modes-inner-container');
			containerQ.panzoom({
				$zoomIn: a_W,
            	$zoomOut: a_V,
            	$reset: a_U,
            	maxScale: 1
			});
			
			a_I.a_T();
			
			a_I.a_S();
*/
		};
		
		a_d.a_c.a_b = function(a_R, a_K, a_P, a_N) {
			var a_Q = a_d.a_c.a_I.a_s();
			
			jsPlumb.ready(function() {
				jQuery(document).ready(function() {					
					if (typeof a_R == 'function') {
						a_R.apply({}, []);
					}
					var a_J = [];
					jQuery(a_d.a_c.a_I.a_H).each(function() {
						var a_L = jQuery(this);
						var a_M = new a_d.a_c(a_Q);
						
						if (typeof a_P == 'function') {
							a_P.apply(a_L, [a_M, a_L]);
						}
						
						a_M.a_O(jQuery(this));
						a_J.push(a_M);
						
						if (typeof a_N == 'function') {
							a_N.apply(a_M, [a_M, a_L]);
						}
					});
					if (typeof a_K == 'function') {
						a_K.apply({}, [a_J]);
					}
				});
			});
		};
		
		a_d.a_c.a_I = {
			a_H: '.rgm-modes-container',
			a_G: 'rgm-modes-viewport',
			a_F: 'rgm-modes-drawing-container',
			a_E: 'rgm-modes-controls-container',
			a_D: 'rgm-modes-zoom-controls',
			a_C: 'rgm-modes-zoom-in-btn',
			a_B: 'rgm-modes-zoom-out-btn',
			a_A: 'rgm-modes-zoom-reset-btn',
			a_z: 'jtk-drag-select',
			a_y: 'model',
			a_x: 'rgm_modes_node_',
			a_w: 'rmg-modes-connection-overlay-',
// TODO: Unicode icons for zoom in/out
			a_v: 'Zoom In',
			a_u: 'Zoom Out',
			a_t: 'Reset Zoom',
			
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
