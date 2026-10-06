#!/usr/bin/env python3
"""R9-BAL103: context rule for the ambiguous sign 9 (i|r|s), registered in r9/PREREG.md.
Control A (held-out Mazarin t.1, matched context noise), A' (letter-shuffled model), B (calib f.171r, 3 occurrences);
on gate PASS writes exceptions.tsv for the f.50 i|r|s tokens. Writes r9/result.tsv and r9/f50_choices.tsv; --check exits 1 if stale."""
import sys, os, random, csv, gzip
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H); R = os.path.dirname(os.path.dirname(T))
sys.path.insert(0, os.path.join(R, 'tools'))
import judge_plaintext as jp
D = os.path.join(R, 'tools', 'data', 'fr17')
files = sorted(f for f in os.listdir(D) if f.endswith('.txt.gz'))
HELD = 'lettresducardina01maza.txt.gz'
txt = {f: jp.read_corpus(os.path.join(D, f)) for f in files}
def model(names, shuffle=False):
    ts = [txt[f] for f in names]
    if shuffle:
        rs = random.Random(7); ts2 = []
        for t in ts:
            L = list(jp.fold(t)); rs.shuffle(L); ts2.append(''.join(L))
        ts = ts2
    return jp.NgramModel(ts)
def lp(m, g):
    import math
    return math.log10((m.c.get(g, 0) + m.k) / (m.ctx.get(g[:-1], 0) + m.V * m.k))
def choose(m, left, right):
    best, bv = None, None
    for v in 'sir':   # order puts s first so ties -> s
        s = left[-3:] + v + right[:3]; p = len(left[-3:])
        sc = sum(lp(m, s[i - 3:i + 1]) for i in range(max(3, p), min(len(s), p + 4)))
        if bv is None or sc > bv + 1e-12: best, bv = v, sc
    return best
out = []
# Control A / A'
train = [f for f in files if f != HELD]
mA, mS = model(train), model(train, shuffle=True)
held = jp.fold(txt[HELD]); rng = random.Random(1644)
pos = [i for i in range(3, len(held) - 3) if held[i] in 'irs']
samp = rng.sample(pos, 2000)
cnt = {v: sum(1 for i in samp if held[i] == v) for v in 'irs'}; const = max(cnt, key=cnt.get)
out.append(f"control_A_N\t2000\nconst_letter\t{const}\nconst_acc\t{cnt[const]/2000:.3f}\nrandom_acc\t0.333")
abc = 'abcdefghijklmnopqrstuvwxyz'
accs = {}
for noise in (0, 15, 27, 35):
    rn = random.Random(1000 + noise)
    def nz(s): return ''.join(rn.choice(abc) if rn.random() < noise / 100 else c for c in s)
    a = s_ = 0
    for i in samp:
        l, r = nz(held[i - 3:i]), nz(held[i + 1:i + 4])
        a += choose(mA, l, r) == held[i]; s_ += choose(mS, l, r) == held[i]
    accs[noise] = (a / 2000, s_ / 2000)
    out.append(f"noise{noise}_rule_acc\t{a/2000:.3f}\nnoise{noise}_shuffled_model_acc\t{s_/2000:.3f}")
# full model for B and f.50
mF = model(files)
key = {}
for ln in open(os.path.join(T, 'key_decode.tsv')):
    if ln.startswith('#') or ln.startswith('code\t'): continue
    c, v = ln.rstrip('\n').split('\t')[:2]; key[c] = v
# Control B: calib pass A, same token parsing as calib/calib.py (c = q, registered test)
key_b = dict(key); key_b['c'] = 'q'
toks = []
for ln in open(os.path.join(T, 'calib', 'f171r_passA.tsv')):
    if ln.startswith('#') or not ln.strip(): continue
    cid, tt = ln.rstrip('\n').split('\t'); seg = cid.split('_')[2]; tt = tt.split(' ')
    o, buf = [], None
    for t in tt:
        if buf is not None:
            buf += ' ' + t
            if '}' in t: o.append(buf); buf = None
        elif t.startswith('?{') and '}' not in t: buf = t
        else: o.append(t)
    if seg == 's2':
        i = next((k for k, t in enumerate(o) if t.startswith('|>')), None)
        o = [] if i is None else [o[i][2:]] + o[i + 1:]
    line = [t.split('|')[0] if not t.startswith('?') else t for t in o]
    toks.append(line)
def letters(vals): return jp.fold(''.join(vals))
truth = []
for ln in open(os.path.join(T, 'calib', 'sign_table.tsv')):
    f = ln.rstrip('\n').split('\t')
    if f[0] == '9': truth = list(f[3])
B = []
for line in toks:   # calib.py decodes the whole pass as one string; context is taken across lines there too
    pass
flat = [t for line in toks for t in line]
vals = [key_b.get(t, '') for t in flat]
for k, t in enumerate(flat):
    if t == '9':
        L = letters(v.split('|')[0] for v in vals[:k]); Rr = letters(v.split('|')[0] for v in vals[k + 1:])
        B.append(choose(mF, L, Rr))
hit = sum(a == b for a, b in zip(B, truth))
out.append(f"control_B_rule\t{''.join(B)}\ncontrol_B_truth\t{''.join(truth)}\ncontrol_B_hits\t{hit}/{len(truth)}")
a27, s27 = accs[27]
gate = 'PASS' if (a27 - cnt[const] / 2000 >= 0.10 and a27 - s27 >= 0.10 and hit >= 2) else 'FAIL'
out.append(f"gate\t{gate}")
# f.50 choices
rows = list(csv.DictReader(open(os.path.join(T, 'reading_tokens.tsv')), delimiter='\t'))
ch = ['folio\tline\tposition\tleft\tright\tchoice']
from itertools import groupby
for (fo, li), grp in groupby(rows, key=lambda r: (r['folio'], r['line'])):
    g = list(grp)
    # exceptions.tsv (written from this file) reorders i|r|s; read every such token as the key's own i|r|s so --check is stable
    for r in g:
        if sorted(r['value'].split('|')) == ['i', 'r', 's']: r['value'] = 'i|r|s'
    vv = ['' if (r['grade'] == 'U' or r['value'] in ('', '?')) else r['value'] for r in g]
    for k, r in enumerate(g):
        if r['value'] == 'i|r|s':
            L = letters(v.split('|')[0] for v in vv[:k]); Rr = letters(v.split('|')[0] for v in vv[k + 1:])
            ch.append(f"{fo}\t{li}\t{r['position']}\t{L[-3:]}\t{Rr[:3]}\t{choose(mF, L, Rr)}")
files_out = {'result.tsv': '\n'.join(out) + '\n', 'f50_choices.tsv': '\n'.join(ch) + '\n'}
if '--check' in sys.argv:
    bad = [f for f, c in files_out.items() if open(os.path.join(H, f)).read() != c]
    print('stale: ' + ', '.join(bad) if bad else 'r9 up to date'); sys.exit(1 if bad else 0)
for f, c in files_out.items(): open(os.path.join(H, f), 'w').write(c)
print(files_out['result.tsv'])
