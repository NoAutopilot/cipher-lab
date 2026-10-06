"""R10-COL26B (account 1, LANE-RUN10-account-1, 6 Oct 2026): anchor_split re-run on the 14 cleared units with 23 = n now a key_f23 C
anchor (R9-COL26 per-code PASS), then a per-code control for any new lead. Pre-registered: committed and pushed BEFORE its first run
(rule 3); nothing below is changed after the run.

Phase 1 (gate, unchanged design). A copy of anchor_split_5456.py (R7A-COL26), changes ONLY: (1) units c62, c63 added from
siblings/c6263_reconciled.tsv (line prefixes 62/63; R8-COL26, each cleared its own length-matched key_f23 C test), so 14 units: f23, c32,
c33, c3536, c3940, c47, c48, c49, c50, c54, c55, c56, c62, c63 (canvas 30 and 51 never read); (2) anchors are key_f23's C codes as now
committed, which includes 23 = n (so 23 is no longer a candidate and spans around it split); (3) candidates go to key_f23_anchor_r10.tsv
(source R10-COL26B), never over key_f23_anchor*.tsv. Statistic S, S_exact, spans, eligibility, control B (2000 draws, same seed
20261003 + 16), gate (PASS iff S > p95 and P < 0.05) unchanged.

Phase 2 (lead selection, run only if phase 1 PASSes). Per-code agreement diagnostic as anchor_split_5456_diag.py (share of 2000
control-B draws, seed 7, in which the code reaches its real max cross-unit agreement), but computed on the 12 units WITHOUT c62 and c63
(named held-out now, before the run). A lead = a candidate with diag P < 0.05 on the 12 units, excluding codes R9-COL26 already tested
(21, 20, 83; 23 and 12 are anchors). Its hypothesised value = its best n-gram on the 12 units (unique best only; a tied best is not a lead).

Phase 3 (per-code control, one per lead). R9-COL26 Part A's statistic: H(c) = eligible spans (all 14 units) containing c whose text
contains the value; control B, 5000 draws, seed 20261006 + 262. GATE per lead, Bonferroni over the number of leads n: PASS iff
H > p95(control) AND P(ctrl >= real) < 0.05/n AND held-out H on c62+c63 >= 1; no eligible span on c62+c63 = HELD-OUT-UNTESTABLE (no key
change). Key rule with --write, PASS only: key_f23.tsv code -> value, grade C, source 'R10-COL26B per-code control' (old value kept in
the note). Nothing else in key_f23.tsv changes; key_f24.tsv and the anchor files untouched.
Usage: python3 siblings/anchor_split_r10.py [--write]
"""
import csv, random, re, os, sys, collections
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
def norm(s): return re.sub(r'[^a-z]', '', re.sub(r'\[[^\]]*\]', '', s.lower())).replace('v', 'u').replace('j', 'i')
key = {r['code']: (norm(r['value']), r['grade']) for r in csv.DictReader(open(f'{T}/key_f23.tsv'), delimiter='\t')}
C = {c for c, (v, g) in key.items() if g == 'C'}
lines = []  # (unit, line id, codes, gloss)
ids = {r['id']: r['sign'] for r in csv.DictReader(open(f'{T}/interlinear/sign_ids.tsv'), delimiter='\t')}
f23 = collections.OrderedDict()
for r in csv.DictReader(open(f'{T}/interlinear/f23w_pairs.tsv'), delimiter='\t'):
    P = r['cipher_line'][:3]; f23.setdefault(P, ([], []))
    f23[P][0].extend(ids.get(t, t) for t in r['cipher_raw'].split()); f23[P][1].append(r['plain_raw'])
for P, (cs, gs) in f23.items(): lines.append(('f23', P, [c for c in cs if c.isdigit()], norm(' '.join(gs))))
for fn, pre in (('c32', {'L'}), ('c33', {'T', 'B'}), ('c3536', {'35', '36'}), ('c3940', {'39', '40'}),
                ('c4749', {'47', '48', '49'}), ('c5051', {'50'}),
                ('c5456', {'54', '55', '56'}), ('c6263', {'62', '63'})):
    for r in csv.DictReader(open(f'{H}/{fn}_reconciled.tsv'), delimiter='\t'):
        L = r['line']; p = L[:2] if L[:2].isdigit() else L[0]
        if p not in pre: continue
        unit = f'c{p}' if fn in ('c4749', 'c5051', 'c5456', 'c6263') else fn
        lines.append((unit, L, [t for t in r['tokens'].split() if t.isdigit()], norm(r['gloss'])))
spans = []  # (unit, line, codes tuple, text)
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
def grams(t): return {t[i:i + n] for n in range(1, 5) for i in range(len(t) - n + 1)}
def stat(texts):
    U = collections.defaultdict(lambda: collections.defaultdict(set)); E = collections.defaultdict(lambda: collections.defaultdict(set))
    for (unit, L, cs, _), t in zip(elig, texts):
        for c in set(cs):
            for g in grams(t): U[c][g].add(unit)
            if len(cs) == 1: E[c][t].add(unit)
    S = sum(max(0, max(len(v) for v in U[c].values()) - 1) for c in U)
    SE = sum(max(0, max(len(v) for v in E[c].values()) - 1) for c in E)
    return S, SE, U
real = [s[3] for s in elig]
S, SE, U = stat(real)
cls = collections.defaultdict(list)
for i, s in enumerate(elig): cls[len(s[3])].append(i)
fixed = sum(len(v) for v in cls.values() if len(v) == 1)
print(f"lines {len(lines)}  interior spans {len(spans)}  eligible {len(elig)}  units with eligible spans "
      f"{len({s[0] for s in elig})}  spans in a length class of one {fixed}")
print('per unit eligible:', dict(collections.Counter(s[0] for s in elig)))
rng = random.Random(20261003 + 16)
cS, cE = [], []
for _ in range(2000):
    tx = list(real)
    for v in cls.values():
        perm = [real[i] for i in v]; rng.shuffle(perm)
        for i, t in zip(v, perm): tx[i] = t
    a, b, _ = stat(tx); cS.append(a); cE.append(b)
def pct(xs, q): xs = sorted(xs); return xs[min(len(xs) - 1, int(q * len(xs)))]
print('\nstat\treal\tctrl\tmean\tp95\tmax\tP(ctrl>=real)\tgate')
for nm, r, c in (('S', S, cS), ('S_exact', SE, cE)):
    P = sum(x >= r for x in c) / len(c)
    gate = ('PASS' if r > pct(c, .95) and P < 0.05 else 'FAIL') if nm == 'S' else '-'
    print(f"{nm}\t{r}\tcontrol-B\t{sum(c)/len(c):.2f}\t{pct(c,.95)}\t{max(c)}\t{P:.4f}\t{gate}")
passed = S > pct(cS, .95) and sum(x >= S for x in cS) / len(cS) < 0.05
print('\ncode\tbest\tunits\tkey_f23\tunits_list')
cand = []
for c in sorted(U, key=int):
    m = max(len(v) for v in U[c].values())
    if m < 2: continue
    best = [g for g, v in U[c].items() if len(v) == m]; lmax = max(map(len, best)); top = [g for g in best if len(g) == lmax]
    g = top[0] if len(top) == 1 else '|'.join(sorted(top))
    kv = f"{key[c][0]}({key[c][1]})" if c in key else '-'
    print(f"{c}\t{g}\t{m}\t{kv}\t{','.join(sorted(U[c][top[0]]))}")
    cand.append((c, g, m, len(top) == 1, kv, sorted(U[c][top[0]])))
if passed:
    with open(f'{T}/key_f23_anchor_r10.tsv', 'w') as f:
        f.write('code\tvalue\tgrade\tsource\tnote\n')
        for c, g, m, uniq, kv, us in cand:
            f.write(f"{c}\t{g}\t{'C' if uniq and m >= 2 else 'M'}\tR10-COL26B anchor-split pairing, 14 cleared units\tunits={m} ({','.join(us)}); key_f23 {kv}\n")
    print('wrote key_f23_anchor_r10.tsv')

if not passed: print('phase 1 FAIL: no phase 2/3'); sys.exit(0)
# Phase 2: lead selection on the 12 units without the held-out pair
HELD = {'c62', 'c63'}
sel = [i for i, s in enumerate(elig) if s[0] not in HELD]
def statU(idx, texts):
    U = collections.defaultdict(lambda: collections.defaultdict(set))
    for i in idx:
        for c in set(elig[i][2]):
            for g in grams(texts[i]): U[c][g].add(elig[i][0])
    return U
U12 = statU(sel, real); realm = {c: max(len(v) for v in U12[c].values()) for c in U12}
cls12 = collections.defaultdict(list)
for i in sel: cls12[len(real[i])].append(i)
cnt = collections.Counter(); rng2 = random.Random(7)
for _ in range(2000):
    tx = list(real)
    for v in cls12.values():
        p = [real[i] for i in v]; rng2.shuffle(p)
        for i, t in zip(v, p): tx[i] = t
    Uc = statU(sel, tx)
    for c in realm:
        if realm[c] >= 2 and max(len(v) for v in Uc[c].values()) >= realm[c]: cnt[c] += 1
print('\nphase 2: per-code diag on 12 units (c62, c63 held out), 2000 draws seed 7')
print('code\tunits\tbest\tdiag_P\tlead')
leads = {}
for c in sorted(realm, key=int):
    if realm[c] < 2: continue
    best = [g for g, v in U12[c].items() if len(v) == realm[c]]; lm = max(map(len, best)); top = [g for g in best if len(g) == lm]
    P = cnt[c] / 2000; isl = P < 0.05 and c not in ('21', '20', '83') and len(top) == 1
    if isl: leads[c] = top[0]
    print(f"{c}\t{realm[c]}\t{'|'.join(sorted(top))}\t{P:.3f}\t{'LEAD' if isl else ''}")
if not leads: print('no lead: phase 3 not run'); sys.exit(0)
# Phase 3: per-code control
n = len(leads); rng3 = random.Random(20261006 + 262)
def hits(texts):
    out = {c: collections.Counter() for c in leads}
    for (unit, L, cs, _), t in zip(elig, texts):
        for c in leads:
            if c in cs and leads[c] in t: out[c][unit] += 1
    return out
R = hits(real); occ = {c: collections.Counter(s[0] for s in elig if c in s[2]) for c in leads}
draws = []
for _ in range(5000):
    tx = list(real)
    for v in cls.values():
        p = [real[i] for i in v]; rng3.shuffle(p)
        for i, t in zip(v, p): tx[i] = t
    draws.append(hits(tx))
print(f'\nphase 3: per-code control, 5000 draws, Bonferroni 0.05/{n}')
print('code\tvalue\tspans\tH_real\tunits\tctrl_mean\tp95\tmax\tP\theld_out_H/spans\tgate')
res = {}
for c, v in leads.items():
    h = sum(R[c].values()); ch = [sum(d[c].values()) for d in draws]; P = sum(x >= h for x in ch) / len(ch)
    ho = sum(R[c][u] for u in HELD); hos = sum(occ[c][u] for u in HELD); ok = h > pct(ch, .95) and P < 0.05 / n
    res[c] = ('HELD-OUT-UNTESTABLE' if ok else 'FAIL') if hos == 0 else ('PASS' if ok and ho >= 1 else 'FAIL')
    print(f"{c}\t{v}\t{sum(occ[c].values())}\t{h}\t{len(R[c])}\t{sum(ch)/len(ch):.2f}\t{pct(ch,.95)}\t{max(ch)}\t{P:.4f}\t{ho}/{hos}\t{res[c]}")
if '--write' in sys.argv and any(g == 'PASS' for g in res.values()):
    rows = list(csv.DictReader(open(f'{T}/key_f23.tsv'), delimiter='\t')); fields = list(rows[0].keys())
    for c, g in res.items():
        if g != 'PASS': continue
        r = next((r for r in rows if r['code'] == c), None)
        if r is None: r = {k: '' for k in fields}; r['code'] = c; rows.append(r); old = 'absent'
        else: old = f"{r['value']}({r['grade']})"
        r['value'] = leads[c]; r['grade'] = 'C'; r['source'] = 'R10-COL26B per-code control (siblings/anchor_split_r10.py)'
        r['note'] = f"was {old}; anchor-span H vs control B, Bonferroni 0.05/{n}, held-out c62+c63 >= 1"
    rows.sort(key=lambda r: int(r['code']))
    with open(f'{T}/key_f23.tsv', 'w') as f:
        f.write('\t'.join(fields) + '\n')
        for r in rows: f.write('\t'.join(r[k] for k in fields) + '\n')
    print('key_f23.tsv changed for:', [c for c, g in res.items() if g == 'PASS'])
