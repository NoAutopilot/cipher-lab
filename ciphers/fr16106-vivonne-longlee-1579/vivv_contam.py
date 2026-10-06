#!/usr/bin/env python3
"""D4-VIVV (verifier) contamination re-scores of D4-VIVMOUS. Uses vivmous.py's own functions unchanged.

    python3 vivv_contam.py [--nshuf N]   # writes vivv_contam_result.json
Variants on pass A: (a) copy line 1 excluded and the cipher tokens aligned to it excluded (cut taken from the real
alignment's traceback); (b) cipher row L01 and copy line 1 excluded; (c) each of the 9 'multi' labels fixed to its
second value in turn (baseline uses the first); (d) all 9 at the second value. Same statistic and value-permutation null.
"""
import json, os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import vivmous as vm
t1, sa = vm.t1, vm.sa
NS = int(sys.argv[sys.argv.index('--nshuf') + 1]) if '--nshuf' in sys.argv else 1000
vm.NSHUF = NS
NW = int(sys.argv[sys.argv.index('--nw') + 1]) if '--nw' in sys.argv else 100

cw = vm.crosswalk()
lm = vm.lab_map(cw)
plain = t1.lets(t1.plain_words())
first = [l for l in open(os.path.join(HERE, 'tx', 'plain_c110_f105r.txt')) if not l.startswith('#')][0]
import re
L1 = len(t1.lets(re.findall(r'[a-z]+', t1.fold(first).lower().replace("'", ' '))))
lines = t1.load_pass('A')
toks = [t for ln in lines for t in vm.tokens(ln)]
res = {'nshuf': NS, 'copy_line1_letters': L1}
res['baseline'] = vm.score(toks, lm, plain, np.random.default_rng(1))

# (a) traceback cut
dec, owner = [], []
for k, t in enumerate(toks):
    v = lm.get(t)
    if v:
        for c in v:
            dec.append(ord(c) - 97); owner.append(k)
dec = np.array(dec)
W = min(len(plain), int(len(dec) * 1.2)); ref = plain[:W]
A = sa.A
E = np.full((A + 1, A), -1.0); E[np.arange(A), np.arange(A)] = 2.0
N = len(dec)
ref_line = np.linspace(0, min(W, N), N + 1) if W >= N else np.arange(N + 1) * (W / N)
path, _, _ = sa.band_dp(dec, ref, E, ref_line, max(200, abs(W - len(dec)) + 200), 1.0, 1.0, free_start=True)
cut_i = max((i for i, j in path if j < L1), default=-1)
cut_tok = owner[cut_i] + 1 if cut_i >= 0 else 0
res['a_traceback_cut'] = dict(dec_letters_dropped=int(cut_i + 1), tokens_dropped=int(cut_tok),
                              **vm.score(toks[cut_tok:], lm, plain[L1:], np.random.default_rng(1)))
# (b) row L01 dropped
n01 = len(vm.tokens(lines[0]))
res['b_row_L01_dropped'] = dict(tokens_dropped=n01, **vm.score(toks[n01:], lm, plain[L1:], np.random.default_rng(1)))
# (c)/(d)
multi = [k for k, (v, m) in cw.items() if m == 'multi']
res['c_multi_second'] = {}
for k in multi:
    m2 = dict(lm); m2[k] = cw[k][0][1]
    res['c_multi_second'][f'{k}={m2[k]}'] = vm.score(toks, m2, plain, np.random.default_rng(1))
m2 = dict(lm); m2.update({k: cw[k][0][1] for k in multi})
res['d_all_second'] = vm.score(toks, m2, plain, np.random.default_rng(1))
json.dump(res, open(os.path.join(HERE, 'vivv_contam_result.json'), 'w'), indent=1)
print(json.dumps(res, indent=1))

# (e) wrong-text null: the real decode (pass A, unchanged map) against 30 random windows of the same length W from fr16
# period French (Catherine de Medicis letters, tools/data/fr16), and (f) the real map with token order shuffled (30 draws).
# These test whether the 0.454 needs THIS text in THIS order, or only French letter statistics: the value-permutation null
# changes the decoded letter frequencies as well as the order, so beating it does not by itself show text-specific alignment.
import gzip, re as _re
rng = np.random.default_rng(7)
corp = gzip.open(os.path.join(HERE, '..', '..', 'tools', 'data', 'fr16', 'lettresdecatheri01cathuoft_djvu.txt.gz'), 'rt', errors='ignore').read()
corp = _re.sub(r'[^a-z]', '', t1.fold(corp).lower())
cl = np.array([ord(c) - 97 for c in corp], dtype=np.int64)
def stream(map_, tk):
    return np.array([ord(c) - 97 for t in tk for c in (map_.get(t) or '')], dtype=np.int64)
wt = []
for _ in range(NW):
    s = int(rng.integers(len(cl) // 10, len(cl) - W - 1))
    wt.append(sa.nw_score(dec, cl[s:s + W]))
wt = np.array(wt)
res['e_wrong_text'] = dict(real_vs_copy=round(float(sa.nw_score(dec, ref)), 4), n=NW, mean=round(float(wt.mean()), 4),
                           max=round(float(wt.max()), 4), p95=round(float(np.percentile(wt, 95)), 4), p99=round(float(np.percentile(wt, 99)), 4))
osh = []
for _ in range(NW):
    tk = list(toks); rng.shuffle(tk)
    osh.append(sa.nw_score(stream(lm, tk), ref))
osh = np.array(osh)
res['f_order_shuffle'] = dict(n=NW, mean=round(float(osh.mean()), 4), max=round(float(osh.max()), 4),
                              p95=round(float(np.percentile(osh, 95)), 4), p99=round(float(np.percentile(osh, 99)), 4))
# control decode (seed 0) against the wrong text too, to show the instrument CAN separate text identity at e=0.576
rc = np.random.default_rng(0)
inv = {}
for k, v in lm.items():
    if len(v) == 1:
        inv.setdefault(v, []).append(k)
from collections import Counter
fq = Counter(toks); labs, p = zip(*sorted(fq.items())); p = np.array(p, float); p /= p.sum()
ct = []
for c in plain:
    ch = chr(c + 97); ct.append(rc.choice(inv[ch]) if ch in inv else 'UNK')
ct = ct[:len(toks)]; noisy = []
for t in ct:
    r = rc.random()
    if r < vm.E_READER / 2: noisy.append(rc.choice(labs, p=p))
    elif r < vm.E_READER * 0.75: continue
    elif r < vm.E_READER: noisy += [t, rc.choice(labs, p=p)]
    else: noisy.append(t)
cd = stream(lm, noisy); Wc = min(len(plain), int(len(cd) * 1.2))
cwt = [sa.nw_score(cd, cl[s:s + Wc]) for s in rng.integers(len(cl) // 10, len(cl) - Wc - 1, NW)]
res['g_control_seed0'] = dict(vs_copy=round(float(sa.nw_score(cd, plain[:Wc])), 4), vs_wrong_text_mean=round(float(np.mean(cwt)), 4),
                              vs_wrong_text_max=round(float(np.max(cwt)), 4))
res['path_start_copy_letter'] = int(min(j for i, j in path))
json.dump(res, open(os.path.join(HERE, 'vivv_contam_result.json'), 'w'), indent=1)
print(json.dumps({k: res[k] for k in ('e_wrong_text', 'f_order_shuffle', 'g_control_seed0', 'path_start_copy_letter')}, indent=1))
