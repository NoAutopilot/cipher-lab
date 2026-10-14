"""VER-COL50 (verifier, account 4, LANE DEFAULT-A4-2135-14, 14 Oct 2026): per-token word-grain check of the 65 canvas 50 C tokens
(COL26-C50, reading_tokens_c50.tsv) against the leaf's own gloss, registered in PREREG-VER-COL50.md before it was run. Demotion only.

A C token keeps C iff, under at least one of the two blind word pairings of canvas 50 already on disk (DA1-COL siblings/word_pairs_da1.tsv,
DA1-COL2 siblings/word_pairs_col2.tsv), it sits in a paired gloss-word span and word_da1.py's hit rule (value at the token's proportional
slot +-1 inside that word) is true. Otherwise it goes to M ('word-grain-miss', or 'no-word-pairing' if neither pass covers it).
Reported, not gated: per reader, the hits of the 65 tokens against Control W (word texts permuted over the canvas's word spans, 10000
draws, seed 20261014 + 2135), so the reader can see whether the kept set beats chance at word grain.
Writes siblings/verify_c50_lower.tsv (read by c50_reading_inputs.py) and prints the table. Usage: python3 siblings/verify_c50.py [--check]"""
import csv, re, os, sys, collections
import numpy as np
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
def norm(s): return re.sub(r'[^a-z]', '', re.sub(r'\[[^\]]*\]', '', s.lower())).replace('v', 'u').replace('j', 'i')
def hit(t, j, k, v):  # word_da1.py's rule, unchanged
    L = len(t); o = round(j * L / k)
    return any(0 <= s and s + len(v) <= L and t[s:s + len(v)] == v for s in (o - 1, o, o + 1))
toks = {r['line']: r['tokens'].split() for r in csv.DictReader(open(f'{H}/c5051_reconciled.tsv'), delimiter='\t') if r['line'].startswith('50')}
Ctok = [(r['line'], int(r['pos']), r['sign'], norm(r['value'])) for r in csv.DictReader(open(f'{T}/reading_tokens_c50.tsv'), delimiter='\t')
        if r['grade'] == 'C']
assert len(Ctok) == 65, len(Ctok)
def spans(fn):
    out = []
    for r in csv.DictReader(open(f'{H}/{fn}'), delimiter='\t'):
        if not r['line'].startswith('50'): continue
        a, b = int(r['first']), int(r['last']); out.append((r['line'], a, b, norm(r['word'])))
    return out
readers = {'DA1-COL': spans('word_pairs_da1.tsv'), 'DA1-COL2': spans('word_pairs_col2.tsv')}
def locate(sp, L, pos):  # pos 1-based -> (span index, slot j, k)
    for i, (l, a, b, w) in enumerate(sp):
        if l == L and a <= pos - 1 <= b: return i, pos - 1 - a, b - a + 1
    return None
rng = np.random.default_rng(20261014 + 2135); D = 10000
res = {}; print('reader\tcovered\thits\tctrl_mean\tp95\tmax\tP')
for name, sp in readers.items():
    W = [s[3] for s in sp]; loc = [locate(sp, L, p) for L, p, _, _ in Ctok]
    real = [bool(l) and hit(W[l[0]], l[1], l[2], v) for l, (_, _, _, v) in zip(loc, Ctok)]
    cov = [l for l in loc if l]; vals = [v for l, (_, _, _, v) in zip(loc, Ctok) if l]
    ctrl = np.zeros(D, int)
    for d in range(D):
        P = rng.permutation(len(W)); ctrl[d] = sum(hit(W[P[i]], j, k, v) for (i, j, k), v in zip(cov, vals))
    hr = sum(real); res[name] = (loc, real)
    print(f'{name}\t{len(cov)}\t{hr}\t{ctrl.mean():.2f}\t{np.percentile(ctrl, 95):.0f}\t{ctrl.max()}\t{(ctrl >= hr).mean():.4f}')
rows = ['line\tpos\tcode\tvalue\tda1\tcol2\tverdict']; low = ['line\tpos\treason']; kept = 0
for n, (L, p, c, v) in enumerate(Ctok):
    st = []
    for name in readers:
        loc, real = res[name]; i = loc[n]
        st.append('-' if not i else ('hit:' if real[n] else 'miss:') + readers[name][i[0]][3])
    keep = any(s.startswith('hit') for s in st); kept += keep
    why = '' if keep else ('no-word-pairing' if all(s == '-' for s in st) else 'word-grain-miss')
    rows.append(f'{L}\t{p}\t{c}\t{v}\t{st[0]}\t{st[1]}\t{"C" if keep else "M " + why}')
    if not keep: low.append(f'{L}\t{p}\t{why}')
print('\n'.join(rows)); print(f'kept C {kept} of 65; lowered to M {65 - kept}')
out = '\n'.join(low) + '\n'; fp = f'{H}/verify_c50_lower.tsv'
if '--check' in sys.argv:
    ok = os.path.exists(fp) and open(fp).read() == out; print('verify_c50_lower.tsv ' + ('up to date' if ok else 'stale')); sys.exit(0 if ok else 1)
open(fp, 'w').write(out)
