#!/usr/bin/env python3
"""TX-DECODE (3 Oct 2026): no.87 known answer with TX-ATLAS-B72's top-k. Run from harvest/: python3 tx_decode/atlas_mix.py
Lattices over the committed no.87 skeleton: (a) two-pass (no87_topk.tsv), (b) atlas only (atlas/topk/no87_heldout.tsv,
held-out lines kept out of the atlas vote; prior = vote share with a 0.05 floor per listed candidate), (c) two-pass 0.8 +
atlas 0.2 (mixing weight fixed before the run). Scored on the atlas's held-out split only (no87_box_token.tsv split=heldout),
truth = clerk sheet. lam 4, printed key, it16dip. Writes tx_decode/atlas_mix.json."""
import csv, json, sys
sys.path.insert(0, '../../../tools'); import key_decode_lattice as K
from judge_plaintext import LANG_CORPORA, NgramModel, read_corpus
R = lambda p: list(csv.DictReader(open(p), delimiter='\t'))
key = K.read_key('key_1572_sheet.tsv'); lat2 = K.read_topk('tx_decode/no87_topk.tsv')
truth = {(r['line'], int(r['pos'])): r['value'] for r in R('tx_decode/truth87.tsv')}
bt = {r['sid']: r for r in R('../atlas/no87_box_token.tsv')}
atl = {}
for r in R('../atlas/topk/no87_heldout.tsv'):
    b = bt.get(r['box'])
    if not b: continue
    m = {}
    for i in (1, 2, 3):
        k = r.get(f'k{i}') or ''
        if k and k != '_':
            m[k] = m.get(k, 0) + max(float(r.get(f's{i}') or 0), 0.05)
    t = sum(m.values())
    if t: atl[(b['line'], int(b['pos']))] = ({k: v / t for k, v in m.items()}, b['split'])
evalpos = {k for k, (_, s) in atl.items() if s == 'heldout'}
lata = [(k, atl[k][0] if k in atl else {'?': 1.0}) for k, _ in lat2]
latm = []
for k, c in lat2:
    a = atl.get(k, (None,))[0]
    if not a: latm.append((k, c)); continue
    m = {x: 0.8 * c.get(x, 0) + 0.2 * a.get(x, 0) for x in set(c) | set(a)}
    latm.append((k, K.finish(m) if False else {x: v for x, v in m.items() if v > 0}))
model = NgramModel([read_corpus(p) for p in LANG_CORPORA['it16dip']]); lm = K.LM(model)
def ev(lat, seq):
    t = w = u = cov = 0
    for (k, c), s in zip(lat, seq):
        if k not in evalpos or k not in truth: continue
        t += 1
        if s not in key: u += 1
        elif key[s] != truth[k]: w += 1
        cov += any(x in key and key[x] == truth[k] for x in c)
    return {'n': t, 'err': round(w / t, 4), 'err_U': round((w + u) / t, 4), 'truth_in_lattice': round(cov / t, 4)}
out = {}
for name, lat in [('two_pass', lat2), ('atlas', lata), ('mix_0.8_0.2', latm)]:
    seq, _ = K.viterbi(lat, key, lm, 4.0, 64)
    c = K.control(lat, key, lm, model, 200, 1, 4.0, 64)
    out[name] = {'top1': ev(lat, K.top1(lat)), 'lattice_lam4': ev(lat, seq),
                 'rank_z_lattice': (c['lattice']['rank'], round(c['lattice']['z'], 2)), 'rank_z_top1': (c['top1']['rank'], round(c['top1']['z'], 2))}
    print(name, out[name])
json.dump(out, open('tx_decode/atlas_mix.json', 'w'), indent=1)
