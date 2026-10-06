"""D22-COL26P (account 2, LANE DEFAULT-account-2-20261006-2209, 6 Oct 2026): per-code POSITIONAL test of the open f.23 codes listed in
key_f23_anchor_r10.tsv (R10-COL26B). Pre-registered: this file is committed and pushed BEFORE its first run (rule 3); nothing below is
changed after the run. Scripts and disk only.

Why a new statistic: R9-COL26 / R10-COL26B-D scored H = "span text contains the value", which a common letter (e) meets in almost every
span, so 15 = e was UNDERPOWERED twice. Here the statistic asks whether the value sits WHERE the anchors predict, not merely in the span.

Codes tested (fixed now): every row of key_f23_anchor_r10.tsv with a single (non-tied) value -- 26 codes:
  11 e, 15 e, 16 se, 20 i, 21 t, 27 u, 29 r, 30 s, 31 t, 32 u, 39 e, 46 ce, 47 e, 54 e, 61 e, 67 leur, 70 e, 71 e, 75 la, 76 e, 77 l,
  81 me, 83 mo, 85 na, 86 e, 96 que.
  The five tied rows (13 o|r, 17 e|g|s, 57 f|i, 87 i|n|o|s, 90 e|t) are not a single hypothesis and are not tested.
  No code is a key_f23 C anchor. Bonferroni over n = 26: alpha = 0.05/26 = 0.00192.

Units (scored): the 14 cleared units of R10-COL26B, read exactly as siblings/anchor_split_r10.py (f23, c32, c33, c3536, c3940, c47,
  c48, c49, c50, c54, c55, c56, c62, c63); anchors = key_f23 C codes as committed (23 = n, 12 = c included), ordered greedy walk;
  interior spans between consecutive anchors; eligible: 1-3 span codes, 1-12 letters (unchanged).
Held-out units (named now; none was used to pick the values in key_f23_anchor_r10.tsv): the f.23 rotated margin postscript
  (margin/f23m_reconciled.tsv, M1-M3; part of f.23, which cleared) and canvas 51 (siblings/c5051_reconciled.tsv lines 51*; its letter
  49-51 cleared). Same span construction. Canvas 30 (did NOT clear its own control) is reported separately, never counted.

Positional statistic. In an eligible span with codes (c_0..c_{k-1}) and text t of length L, the anchor-predicted offset of code c_j is
  o_j = round(j * L / k). Text is read CIRCULARLY (index mod L). A span-occurrence of code c with hypothesised value v is a HIT iff
  len(v) <= L and v occurs in the circular text starting at one of o_j-1, o_j, o_j+1 (mod L). H(c) = hits over all eligible
  span-occurrences of c (a code twice in one span counts twice).
Control R (rotation; can vary on this statistic): each span text is rotated circularly by an independent uniform offset in 0..L-1.
  This keeps every span's letters AND its set of circular n-gram occurrences exactly (so the R10-COL26B selection, which chose each
  value because spans CONTAIN it, is held fixed by construction) and changes only WHERE the value sits relative to the predicted
  offset -- the statistic's own axis. 10000 draws, seed 20261006 + 2209.
Power check per code: P_min = P(H_ctrl >= number of span-occurrences); P_min >= alpha => UNDERPOWERED (no PASS possible, logged as
  untestable by this statistic at this N, not a negative).
GATE per code: PASS iff H_real > p95(control R) AND P(ctrl >= real) < 0.00192 AND (held-out: if the code has >= 1 eligible
  span-occurrence on margin + c51, then held-out H >= 1; if it has none, the result is HELD-OUT-UNTESTABLE, not a PASS).
  Otherwise FAIL (or UNDERPOWERED as above).
Grade rule: a PASS code is listed as grade S (cryptanalytic with a control), never C, and is NOT merged into key_f23.tsv or key.tsv by
  this script (no merge registered). Output: siblings/positional_r22_out.txt (stdout).
Usage: python3 siblings/positional_r22.py
"""
import csv, random, re, os, collections
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
def norm(s): return re.sub(r'[^a-z]', '', re.sub(r'\[[^\]]*\]', '', s.lower())).replace('v', 'u').replace('j', 'i')
key = {r['code']: (norm(r['value']), r['grade']) for r in csv.DictReader(open(f'{T}/key_f23.tsv'), delimiter='\t')}
C = {c for c, (v, g) in key.items() if g == 'C'}
HYP = {}
for r in csv.DictReader(open(f'{T}/key_f23_anchor_r10.tsv'), delimiter='\t'):
    if '|' not in r['value']: HYP[r['code']] = norm(r['value'])
assert len(HYP) == 26 and not (set(HYP) & C), (len(HYP), set(HYP) & C)
N = len(HYP); ALPHA = 0.05 / N
lines = []  # (unit, line id, codes, gloss)
ids = {r['id']: r['sign'] for r in csv.DictReader(open(f'{T}/interlinear/sign_ids.tsv'), delimiter='\t')}
f23 = collections.OrderedDict()
for r in csv.DictReader(open(f'{T}/interlinear/f23w_pairs.tsv'), delimiter='\t'):
    P = r['cipher_line'][:3]; f23.setdefault(P, ([], []))
    f23[P][0].extend(ids.get(t, t) for t in r['cipher_raw'].split()); f23[P][1].append(r['plain_raw'])
for P, (cs, gs) in f23.items(): lines.append(('f23', P, [c for c in cs if c.isdigit()], norm(' '.join(gs))))
for fn, pre in (('c32', {'L'}), ('c33', {'T', 'B'}), ('c3536', {'35', '36'}), ('c3940', {'39', '40'}),
                ('c4749', {'47', '48', '49'}), ('c5051', {'50'}), ('c5456', {'54', '55', '56'}), ('c6263', {'62', '63'})):
    for r in csv.DictReader(open(f'{H}/{fn}_reconciled.tsv'), delimiter='\t'):
        L = r['line']; p = L[:2] if L[:2].isdigit() else L[0]
        if p not in pre: continue
        unit = f'c{p}' if fn in ('c4749', 'c5051', 'c5456', 'c6263') else fn
        lines.append((unit, L, [t for t in r['tokens'].split() if t.isdigit()], norm(r['gloss'])))
held = []
for r in csv.DictReader(open(f'{T}/margin/f23m_reconciled.tsv'), delimiter='\t'):
    held.append(('margin', r['unit'], [t for t in r['codes'].split() if t.isdigit()], norm(r['gloss'])))
for r in csv.DictReader(open(f'{H}/c5051_reconciled.tsv'), delimiter='\t'):
    if r['line'].startswith('51'): held.append(('c51', r['line'], [t for t in r['tokens'].split() if t.isdigit()], norm(r['gloss'])))
runs = collections.defaultdict(list)
for r in csv.DictReader(open(f'{T}/ciphertext.tsv'), delimiter='\t'):
    if r['canvas'] == '30': runs[int(r['line'])].append(r['token'])
c30 = [('c30', r['line'], [t for t in runs.get(int(r['line']), []) if t.isdigit()], norm(r['gloss']))
       for r in csv.DictReader(open(f'{H}/c30_gloss_reconciled.tsv'), delimiter='\t')]
def mkspans(ls):
    out = []
    for unit, L, codes, gl in ls:
        if not gl: continue
        p = 0; prev = None; between = []
        for c in codes:
            if c in C:
                i = gl.find(key[c][0], p)
                if i < 0: continue
                if prev is not None: out.append((unit, L, tuple(between), gl[prev:i]))
                prev = p = i + len(key[c][0]); between = []
            elif prev is not None: between.append(c)
    return [s for s in out if 1 <= len(s[2]) <= 3 and 1 <= len(s[3]) <= 12]
def occs(sp):  # (span index, code, predicted offset)
    return [(i, c, round(j * len(t) / len(cs))) for i, (u, L, cs, t) in enumerate(sp) for j, c in enumerate(cs) if c in HYP]
def hit(t, v, o):
    L = len(t)
    if len(v) > L: return False
    tt = t + t
    return any(tt[(o + d) % L:(o + d) % L + len(v)] == v for d in (-1, 0, 1))
def score(sp, oc, texts):
    h = collections.Counter()
    for i, c, o in oc:
        if hit(texts[i], HYP[c], o): h[c] += 1
    return h
def pct(xs, q): xs = sorted(xs); return xs[min(len(xs) - 1, int(q * len(xs)))]
SP = mkspans(lines); OC = occs(SP); real = [s[3] for s in SP]
HS = mkspans(held); HO = occs(HS); HR = score(HS, HO, [s[3] for s in HS])
S30 = mkspans(c30); O30 = occs(S30); R30 = score(S30, O30, [s[3] for s in S30])
R = score(SP, OC, real)
nocc = collections.Counter(c for _, c, _ in OC); hocc = collections.Counter(c for _, c, _ in HO); occ30 = collections.Counter(c for _, c, _ in O30)
print(f"scored: lines {len(lines)} eligible spans {len(SP)} code-occurrences tested {len(OC)}; held-out (margin+c51) spans {len(HS)} "
      f"occ {len(HO)}; c30 spans {len(S30)} occ {len(O30)}; n codes {N}, alpha {ALPHA:.5f}")
rng = random.Random(20261006 + 2209)
draws = []
for _ in range(10000):
    tx = []
    for t in real:
        r = rng.randrange(len(t)); tx.append(t[r:] + t[:r])
    draws.append(score(SP, OC, tx))
print('\ncode\tvalue\tocc\tH_real\tctrl_mean\tp95\tmax\tP\tP_min\theld_H/occ\tc30_H/occ(not counted)\tgate')
res = {}
for c in sorted(HYP, key=int):
    h = R[c]; n = nocc[c]; ch = [d[c] for d in draws]
    P = sum(x >= h for x in ch) / len(ch); Pmin = sum(x >= n for x in ch) / len(ch) if n else 1.0
    if n == 0 or Pmin >= ALPHA: g = 'UNDERPOWERED'
    elif not (h > pct(ch, .95) and P < ALPHA): g = 'FAIL'
    elif hocc[c] == 0: g = 'HELD-OUT-UNTESTABLE'
    else: g = 'PASS' if HR[c] >= 1 else 'FAIL'
    res[c] = g
    print(f"{c}\t{HYP[c]}\t{n}\t{h}\t{sum(ch)/len(ch):.2f}\t{pct(ch,.95)}\t{max(ch)}\t{P:.4f}\t{Pmin:.4f}\t{HR[c]}/{hocc[c]}\t{R30[c]}/{occ30[c]}\t{g}")
print('\nsummary:', dict(collections.Counter(res.values())))
print('grade S (listed, not merged):', ' '.join(f'{c}={HYP[c]}' for c in sorted(res, key=int) if res[c] == 'PASS') or 'none')
