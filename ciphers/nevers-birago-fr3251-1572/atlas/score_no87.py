# TX-ATLAS-B72 (3 Oct 2026): err_true of the atlas top-1 (and top-3 coverage) on no.87's HELD-OUT lines (f.178v L13-L23,
# f.179r L01-L03) against the clerk's clear sheet, beside the committed line-read reconciliation on the SAME signs.
# A sign counts when no87_map.py mapped one box to one token and the clerk sheet aligns a letter there (align_real.tsv).
# Both sides go through one value map (keys/key_1572_clerk.tsv, else the printed sheet), no per-token exceptions, so
# the difference is the sign label alone. Unvalued labels ('_', X_*, ?) count as errors ("wrong+U").
# Run from the repo root after classify: python3 ciphers/nevers-birago-fr3251-1572/atlas/score_no87.py [topk.tsv]
import csv, os, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from name_clusters import value_map
R = os.path.dirname(os.path.abspath(__file__))
V = value_map()
tk = sys.argv[1] if len(sys.argv) > 1 else os.path.join(R, 'topk', 'no87.tsv')
K = {r['box']: r for r in csv.DictReader(open(tk), delimiter='\t')}
M = [r for r in csv.DictReader(open(os.path.join(R, 'no87_box_token.tsv')), delimiter='\t')]
ho = [r for r in M if r['split'] == 'heldout']
tot_tok = len(ho)
S = [r for r in ho if r['op'] == '1:1' and r['truth'] and r['sid'] in K]
c = collections.Counter()
for r in S:
    k = K[r['sid']]; t = r['truth']
    lr, a1 = V.get(r['sign']), V.get(k['k1'] if 'k1' in k else k['code'])
    a3 = {V.get(k.get(f'k{i}', '')) for i in (1, 2, 3)}
    c['n'] += 1
    c['lr_wrong'] += lr is not None and lr != t; c['lr_U'] += lr is None
    c['at_wrong'] += a1 is not None and a1 != t; c['at_U'] += a1 is None
    c['at3_miss'] += t not in a3
    c['both_wrong'] += (lr != t) and (a1 != t)
    c['sign_agree'] += r['sign'] == (k.get('k1') or k['code'])
n = c['n']
f = lambda x: f'{x / n:.3f}'
print(f"no.87 held-out: {n} signs scored (of {tot_tok} held-out tokens; 1:1 box mapping, clerk letter aligned)")
print(f"  line-read reconciliation: err_true {f(c['lr_wrong'])}  (wrong+U {f(c['lr_wrong'] + c['lr_U'])})")
print(f"  atlas top-1:              err_true {f(c['at_wrong'])}  (wrong+U {f(c['at_wrong'] + c['at_U'])})")
print(f"  atlas top-3 miss (truth not among the 3 codes' values): {f(c['at3_miss'])}")
print(f"  both wrong {f(c['both_wrong'])}; atlas label = line-read label on {f(c['sign_agree'])}")
