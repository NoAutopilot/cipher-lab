"""R9-COL26 (account 1, LANE-RUN9-account-1, 6 Oct 2026): pre-registered per-code control for the anchor leads.
Pre-registered: this file is committed and pushed BEFORE its first run (rule 3); nothing below is changed after the run.

Codes and hypotheses (named in the folder's Verdict line before this run): 21 = t, 20 = i, 23 = n, 83 = s (R7A-COL26 post hoc,
siblings/anchor_split_5456_diag_out.txt), and 12 = c (key_f23 grade C; 38 of 58 ordered-walk hits off f.23, R8-COL26).

Units: the 14 units that each cleared their own length-matched key_f23 C test: f23, c32, c33, c3536, c3940, c47, c48, c49, c50, c54,
c55, c56 (as in anchor_split_5456.py) plus c62 and c63 (R8-COL26, siblings/c6263_reconciled.tsv, line prefixes 62/63). Canvas 30 and 51
are never read. Token and gloss normalisation unchanged (digit-only groups; letters only, v->u, j->i, brackets removed).

Part A -- codes 21, 20, 23, 83 (non-anchor codes; the leads came from the anchor-split, so they are tested with it).
  Spans, eligibility and anchors exactly as anchor_split_5456.py (interior spans between consecutive key_f23 C anchors of the ordered
  walk; 1-3 span codes, 1-12 letters), with c62 and c63 added.
  Statistic per code c with value v: H(c) = number of eligible spans containing c whose text contains v (all 14 units); also reported
  per unit, and the number of distinct units with such a span.
  Control B (unchanged design): span texts permuted among eligible spans of equal letter length, pooled across units, 5000 draws,
  seed 20261006 + 26. The control moves which text meets which code, so H(c) can differ from the real value (rule 3 orthogonality).
  Per-unit breakdown: each unit's real hit count vs its control mean and p95 under the same draws.
  Held-out: c62 and c63 were NOT in R7A-COL26's 12 units, where these four leads were picked out of 21 candidates; the held-out
  count is H(c) restricted to c62 + c63.
Part B -- code 12 = c (an anchor itself, so it is tested by the ordered walk instead).
  Units: the 13 cleared units off f.23 (f.23 is where 12 = c was fitted, so it is excluded). For each line, the ordered greedy walk of
  key_f23 C codes (c6263_test.py's walk) over the line's gloss; W = number of occurrences of code 12 the walk scores.
  Control: the LENGTH-MATCHED f23-window control (each line's gloss replaced by a random window of the same length from the f.23
  gloss bank), 5000 draws, same seed stream; per-unit breakdown as in Part A.
GATE (per code; five codes tested, Bonferroni 0.05/5 = 0.01):
  Part A code PASS iff H_real > p95(control B) AND P(ctrl >= real) < 0.01 AND held-out H on c62+c63 >= 1.
    A code with no eligible span on c62+c63 is HELD-OUT-UNTESTABLE: not a PASS, no key change.
  Part B PASS iff W_real > p95(control) AND P(ctrl >= real) < 0.01.
Key rule (per unit, rule 3): every unit read has cleared its own control. With --write, and only for a PASS:
  20 -> key_f23 grade C (value i); 23 -> grade C (value n); 21 -> value t grade C (was M 'e'); 83 -> new row, value s grade C;
  12 = c is already C: PASS or FAIL, no change (a FAIL is logged, not acted on). Source column 'R9-COL26 per-code control'.
  Nothing else in key_f23.tsv changes; key_f24.tsv and the anchor files are untouched.
Usage: python3 siblings/percode_control.py [--write]"""
import csv, random, re, os, sys, collections
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
def norm(s): return re.sub(r'[^a-z]', '', re.sub(r'\[[^\]]*\]', '', s.lower())).replace('v', 'u').replace('j', 'i')
key = {r['code']: (norm(r['value']), r['grade']) for r in csv.DictReader(open(f'{T}/key_f23.tsv'), delimiter='\t')}
C = {c for c, (v, g) in key.items() if g == 'C'}
ids = {r['id']: r['sign'] for r in csv.DictReader(open(f'{T}/interlinear/sign_ids.tsv'), delimiter='\t')}
lines = []  # (unit, line id, codes, gloss)
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
UNITS = ['f23', 'c32', 'c33', 'c3536', 'c3940', 'c47', 'c48', 'c49', 'c50', 'c54', 'c55', 'c56', 'c62', 'c63']
HELD = {'c62', 'c63'}
def pct(xs, q): xs = sorted(xs); return xs[min(len(xs) - 1, int(q * len(xs)))]
rng = random.Random(20261006 + 26)
print(f"lines {len(lines)}  units {sorted({l[0] for l in lines})}")

# Part A
spans = []
for unit, L, codes, gl in lines:
    if not gl: continue
    p = 0; prev = None; between = []
    for c in codes:
        if c in C:
            i = gl.find(key[c][0], p)
            if i < 0: continue
            if prev is not None: spans.append((unit, L, tuple(between), gl[prev:i]))
            prev = p = i + len(key[c][0]); between = []
        elif prev is not None: between.append(c)
elig = [s for s in spans if 1 <= len(s[2]) <= 3 and 1 <= len(s[3]) <= 12]
real = [s[3] for s in elig]
cls = collections.defaultdict(list)
for i, s in enumerate(elig): cls[len(s[3])].append(i)
print(f"interior spans {len(spans)}  eligible {len(elig)}  per unit {dict(collections.Counter(s[0] for s in elig))}  "
      f"spans in a length class of one {sum(len(v) for v in cls.values() if len(v) == 1)}")
HYP = {'21': 't', '20': 'i', '23': 'n', '83': 's'}
def hits(texts):
    out = {c: collections.Counter() for c in HYP}
    for (unit, L, cs, _), t in zip(elig, texts):
        for c in HYP:
            if c in cs and HYP[c] in t: out[c][unit] += 1
    return out
R = hits(real)
occ = {c: collections.Counter(s[0] for s in elig if c in s[2]) for c in HYP}
draws = []
for _ in range(5000):
    tx = list(real)
    for v in cls.values():
        perm = [real[i] for i in v]; rng.shuffle(perm)
        for i, t in zip(v, perm): tx[i] = t
    draws.append(hits(tx))
result = {}
print('\nPart A: per-code anchor-span control (control B, 5000 draws)')
print('code\tvalue\tspans_with_code\tH_real\tunits\tctrl_mean\tp95\tmax\tP\theld_out_H\theld_out_spans\tgate')
for c, v in HYP.items():
    h = sum(R[c].values()); ch = [sum(d[c].values()) for d in draws]; P = sum(x >= h for x in ch) / len(ch)
    ho = sum(R[c][u] for u in HELD); hos = sum(occ[c][u] for u in HELD)
    if hos == 0: gate = 'HELD-OUT-UNTESTABLE' if (h > pct(ch, .95) and P < 0.01) else 'FAIL'
    else: gate = 'PASS' if (h > pct(ch, .95) and P < 0.01 and ho >= 1) else 'FAIL'
    result[c] = gate
    print(f"{c}\t{v}\t{sum(occ[c].values())}\t{h}\t{len(R[c])}\t{sum(ch)/len(ch):.2f}\t{pct(ch,.95)}\t{max(ch)}\t{P:.4f}\t{ho}\t{hos}\t{gate}")
print('\nper-unit breakdown (code unit spans_with_code real ctrl_mean ctrl_p95)')
for c in HYP:
    for u in UNITS:
        if occ[c][u] == 0: continue
        cu = [d[c][u] for d in draws]
        print(f"{c}\t{u}\t{occ[c][u]}\t{R[c][u]}\t{sum(cu)/len(cu):.2f}\t{pct(cu,.95)}{'  held-out' if u in HELD else ''}")

# Part B
bank = norm(''.join(r['plain_raw'] for r in csv.DictReader(open(f'{T}/interlinear/f23w_pairs.tsv'), delimiter='\t')))
def walk12(codes, gloss):
    p = 0; n = 0
    for c in codes:
        if c not in C: continue
        i = gloss.find(key[c][0], p)
        if i >= 0:
            p = i + len(key[c][0])
            if c == '12': n += 1
    return n
B = [(u, L, cs, gl) for u, L, cs, gl in lines if u != 'f23' and gl and '12' in cs]
occ12 = collections.Counter()
for u, L, cs, gl in B: occ12[u] += cs.count('12')
real12 = collections.Counter()
for u, L, cs, gl in B: real12[u] += walk12(cs, gl)
ctl12 = []
for _ in range(5000):
    d = collections.Counter()
    for u, L, cs, gl in B:
        st = rng.randrange(0, len(bank) - len(gl)); d[u] += walk12(cs, bank[st:st + len(gl)])
    ctl12.append(d)
w = sum(real12.values()); cw = [sum(d.values()) for d in ctl12]; P = sum(x >= w for x in cw) / len(cw)
result['12'] = 'PASS' if (w > pct(cw, .95) and P < 0.01) else 'FAIL'
print('\nPart B: code 12 = c, ordered walk vs length-matched f23-window control (5000 draws), 13 units off f.23')
print('code\tvalue\toccurrences\tW_real\tctrl_mean\tp95\tmax\tP\tgate')
print(f"12\tc\t{sum(occ12.values())}\t{w}\t{sum(cw)/len(cw):.2f}\t{pct(cw,.95)}\t{max(cw)}\t{P:.4f}\t{result['12']}")
print('per-unit breakdown (unit occurrences real ctrl_mean ctrl_p95)')
for u in UNITS:
    if occ12[u] == 0: continue
    cu = [d[u] for d in ctl12]
    print(f"12\t{u}\t{occ12[u]}\t{real12[u]}\t{sum(cu)/len(cu):.2f}\t{pct(cu,.95)}")
print('\nverdicts:', ' '.join(f'{c}={g}' for c, g in result.items()))

if '--write' in sys.argv:
    rows = list(csv.DictReader(open(f'{T}/key_f23.tsv'), delimiter='\t')); fields = list(rows[0].keys())
    changed = []
    for c in HYP:
        if result[c] != 'PASS': continue
        r = next((r for r in rows if r['code'] == c), None)
        if r is None:
            r = {k: '' for k in fields}; r['code'] = c; rows.append(r); old = 'absent'
        else: old = f"{r['value']}({r['grade']})"
        r['value'] = HYP[c]; r['grade'] = 'C'; r['source'] = 'R9-COL26 per-code control (siblings/percode_control.py)'
        r['note'] = f"was {old}; anchor-span H vs control B, Bonferroni 0.01, held-out c62+c63 >= 1"
        changed.append(c)
    rows.sort(key=lambda r: int(r['code']))
    with open(f'{T}/key_f23.tsv', 'w') as f:
        f.write('\t'.join(fields) + '\n')
        for r in rows: f.write('\t'.join(r[k] for k in fields) + '\n')
    print('key_f23.tsv changed for:', changed or 'none')
