#!/usr/bin/env python3
"""R12A-SEUT2 (6 Oct 2026): PREREG-SEUT2 held-out-half gate. Learn the sign->letter key on fo. 22r lines L01-L06 against the slip,
decode L07-L13 with it, score against the slip vs 40 wrong texts. Power control first (PREREG-SEUT synthetic design at err 0.32,
split at passR's L06/L07 fraction). Writes result_seut2.json; --check re-runs and compares."""
import sys, os, json, random
import numpy as np
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
import seut_gate as g
sa = g.sa
def build_n(p):
    n = 0
    for l in open(os.path.join(here, p)):
        if l.startswith('L') and int(l[1:3]) <= 6:
            n += len([x for x in l.rstrip('\n').split('\t')[1].split() if x != 'NONE'])
    return n
def H(sym, let, k):
    b, s = sym[:k], sym[k:]
    counts, _ = sa.learn(b, let, max(sym) + 1, slope=len(let) / len(sym), **g.SET)
    return float(sa.nw_score(sa.decode(counts)[np.asarray(s)], let))
def nulls(sym, words, n_let, C, k):
    r = random.Random(12); out = []
    for _ in range(20):
        s = r.randrange(len(C) - n_let); out.append(H(sym, C[s:s + n_let], k))
    r = random.Random(13)
    for _ in range(20):
        w = words[:]; r.shuffle(w); out.append(H(sym, g.letters(' '.join(w)), k))
    return out
def row(sym, let, k, words, C):
    h = H(sym, let, k); nl = nulls(sym, words, len(let), C, k); p95 = float(np.percentile(nl, 95))
    return {'n_sym': len(sym), 'n_build': k, 'H': round(h, 4), 'null_mean': round(float(np.mean(nl)), 4),
            'null_p95': round(p95, 4), 'null_max': round(float(max(nl)), 4), 'pass': bool(h > p95)}
def main():
    words = g.slip_text().split(); let = g.letters(' '.join(words)); C = g.corpus()
    symR, _ = g.stream('passR.tsv'); frac = build_n('passR.tsv') / len(symR)
    res = {'settings': g.SET, 'n_letters': len(let), 'build_frac': round(frac, 4), 'control': [], 'targets': {}}
    for seed in (21, 22, 23):
        sym, sl = g.synth(words, seed, 0.32); r = row(sym, sl, int(round(len(sym) * frac)), words, C); r['seed'] = seed
        res['control'].append(r)
    res['power'] = sum(c['pass'] for c in res['control']) >= 2
    if res['power']:
        for p in ('passR.tsv', 'passA.tsv', 'passB.tsv'):
            sym, ids = g.stream(p); r = row(sym, let, build_n(p), words, C); r['n_ids'] = len(ids); res['targets'][p] = r
    return res
if __name__ == '__main__':
    r = main(); out = os.path.join(here, 'result_seut2.json')
    if '--check' in sys.argv:
        ok = json.load(open(out)) == json.loads(json.dumps(r)); print('check', 'OK' if ok else 'STALE'); sys.exit(0 if ok else 1)
    json.dump(r, open(out, 'w'), indent=1); print(json.dumps(r, indent=1))
