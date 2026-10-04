#!/usr/bin/env python3
"""BIR-KEYFIT (4 Oct 2026): constrained key refit on the owner-right labels, per PREREG.md beside this file.
Run from the repo root: python3 ciphers/nevers-birago-fr3251-1572/harvest/keyfit/keyfit.py [--control-only]
Known-answer control on no.87 first (gate: mean recovery >= 8/10 at matched length); the target refit runs only if it passes.
Tile -> position, base tokens and the judge models are ownersort.py's (imported, not copied). Disk only."""
import csv, json, os, random, sys
from collections import defaultdict, Counter
from multiprocessing import Pool
sys.argv = sys.argv[:1] + [a for a in sys.argv[1:] if a == '--control-only']
CONTROL_ONLY = '--control-only' in sys.argv
sys.argv = sys.argv[:1]
N = 'ciphers/nevers-birago-fr3251-1572'
sys.path.insert(0, N + '/harvest/ownersort'); sys.path.insert(0, 'tools')
import ownersort as OS
import judge_plaintext as jp
H = os.path.dirname(os.path.abspath(__file__)); SEED = 20261004; NNULL = 100
def tsv(p): return list(csv.DictReader(open(p), delimiter='\t'))
sheet = OS.key
clerk = {r['sign']: r for r in tsv(N + '/keys/key_1572_clerk.tsv')}
FIXED = {s for s, r in clerk.items() if r['grade'] == 'C' and r['relation'] == 'agrees' and s in sheet}
LETTERS = sorted({v for v in sheet.values() if len(v) == 1 and v.isalpha()})
BAGS = {'X_NEW', 'X_EQ', 'X_S', 'X_K', 'X_A', '?'}

def fold(v): return '' if v in ('?', 'NULL', '') else v.lower()

class Fit:
    """leaves: {name: (model, [(sign, fixed_value_or_None)], L0)}; free signs take values from vals."""
    def __init__(self, leaves): self.leaves = leaves
    def text(self, lf, vals):
        return ''.join(fold(vals[s]) if fv is None else fv for s, fv in self.leaves[lf][1])
    def obj(self, lfs, vals):
        t = 0.0
        for lf in lfs:
            m, _, L0 = self.leaves[lf]; t += m.score(self.text(lf, vals)) * L0
        return t
    def fit(self, lfs, free, start, rounds=6):
        vals = dict(start); occ = {s: [lf for lf in lfs if any(x == s and fv is None for x, fv in self.leaves[lf][1])] for s in free}
        for _ in range(rounds):
            changed = False
            for s in sorted(free):
                if not occ[s]: continue
                old = vals[s]; best, bv = None, old
                for v in LETTERS:
                    vals[s] = v; o = self.obj(occ[s], vals)
                    if best is None or o > best + 1e-12: best, bv = o, v
                changed |= bv != old; vals[s] = bv
            if not changed: break
        return vals

# ---------------- known-answer control on no.87
def control():
    m = OS.models['f168']  # it16dip (spec nevers-birago-fr3251-1572)
    toks = []
    for f in ('f178r', 'f178v', 'f179r'):
        toks += [r for r in tsv(N + f'/harvest/reading_{f}_tokens.tsv')]
    # matched length: the FWD fit side's letter count (f117 + f144r base texts)
    target_len = len(OS.text('f117', {})) + len(OS.text('f144r', {}))
    rows = []; out = {}
    for mode in ('matched', 'full'):
        recs = []
        for seed in (1, 2, 3):
            rnd = random.Random(seed)
            if mode == 'matched':
                # window of tokens whose base letter count ~ target_len
                cum = []; c = 0
                for r in toks: c += len(fold(r['value'])); cum.append(c)
                maxstart = next(i for i in range(len(toks)) if cum[-1] - (cum[i - 1] if i else 0) < target_len) - 1
                a = rnd.randrange(0, max(1, maxstart)); base0 = cum[a - 1] if a else 0
                b = next(i for i in range(a, len(toks)) if cum[i] - base0 >= target_len) + 1
                win = toks[a:b]
            else:
                win = toks; rnd.random()
            cnt = Counter(r['sign'] for r in win)
            pool = sorted(s for s in FIXED if len(sheet[s]) == 1 and cnt[s] >= 3)
            blank = sorted(rnd.sample(pool, 10))
            seq = [(r['sign'], None) if r['sign'] in blank else (r['sign'], fold(r['value'])) for r in win]
            F = Fit({'no87': (m, seq, sum(len(fold(r['value'])) for r in win))})
            vals = F.fit(['no87'], blank, {s: 'e' for s in blank})
            hit = [s for s in blank if vals[s] == clerk[s]['value']]
            recs.append(len(hit))
            for s in blank:
                rows.append(dict(mode=mode, seed=seed, letters=sum(len(fold(r['value'])) for r in win), sign=s, n_in_window=cnt[s],
                                 truth=clerk[s]['value'], fitted=vals[s], ok=int(vals[s] == clerk[s]['value'])))
        out[mode] = dict(recovered=recs, mean=sum(recs) / 3)
    out['target_len'] = target_len; out['PASS'] = out['matched']['mean'] >= 8
    with open(H + '/control_no87.tsv', 'w') as f:
        cols = list(rows[0]); f.write('\t'.join(cols) + '\n')
        for r in rows: f.write('\t'.join(str(r[c]) for c in cols) + '\n')
    json.dump(out, open(H + '/control_no87.json', 'w'), indent=1)
    return out

if __name__ == '__main__':
    c = control(); print(json.dumps(c))
    if not c['PASS']:
        print('CONTROL BELOW GATE: untested-by-this-tool; no target fit run'); sys.exit(3)
    if CONTROL_ONLY: sys.exit(0)
    raise SystemExit('target refit not implemented in this job: the control passed, re-brief')
