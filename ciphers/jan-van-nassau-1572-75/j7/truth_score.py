#!/usr/bin/env python3
"""J7: score the control's true key and the solver's best key under the same Problem (model vs search diagnosis)."""
import json, sys
sys.path.insert(0, '../../tools')
import nomenclator_anneal as na
na.set_lang('de')
res, truth, model, cipher = sys.argv[1:5]
t = json.load(open(truth)); r = json.load(open(res))
syl = "en er ch ge ei ie un in st an de te ben den sch uer ten ich ung gen el es et ar or ur ter ber ein au".split()
words = "und der die das zu uon nicht nit mit den dem in auch ist wir ich sich so es ein haben dasz".split()
words += [v for v in t['key'].values() if len(v) > 3 and v not in syl and v not in words]
pb = na.Problem(na.load_texts([cipher]), na.ing.Model(model), 'clear', 'vc', words, p_null=0.03, extra_syl=syl)
def key_of(d):
    return [pb.vid.get(d.get(s, ''), pb.null_v) for s in pb.signs]
kt, kb = key_of(t['key']), key_of(r['best']['key'])
print(json.dumps(dict(truth_score=round(pb.score(kt), 1), truth_lm=round(pb.lm_score(kt), 1),
                      best_score=round(pb.score(kb), 1), best_lm=round(pb.lm_score(kb), 1))))
