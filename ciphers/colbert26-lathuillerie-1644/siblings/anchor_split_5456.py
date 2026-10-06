"""R7A-COL26 (account 1, LANE-RUN7-account-1, 6 Oct 2026): re-run of A2-COL16's anchor_split.py with canvas 54, 55 and 56 added as
cleared units (each passed its own pre-registered length-matched key_f23 C test, A2-COL17: 18/29 vs p95 15, 39/59 vs p95 32, 21/29
vs p95 16). Pre-registered: this copy is committed and pushed BEFORE its first run (rule 3). Changes from anchor_split.py, and only these:
(1) units c54, c55, c56 read from siblings/c5456_reconciled.tsv (line prefix 54/55/56; 55a12's unsettled '3?' group is dropped by the
digit-only token rule, as before; 55a05 kept as gloss, A2-COL17's attribution call made before its own scoring); (2) candidates are
written to key_f23_anchor_5456.tsv (source label R7A-COL26), never over key_f23_anchor.tsv. Statistic S, S_exact, spans, eligibility,
control B (2000 draws, same seed), gate (PASS iff S > p95 and P < 0.05) and merge rule are unchanged. key_f23.tsv and key.tsv untouched.
Usage: python3 siblings/anchor_split_5456.py [--write]

A2-COL16's registration, unchanged:
A2-COL16: anchor-split pairing of the units that cleared their own length-matched key_f23 C test, against control B.
Pre-registered 3 Oct 2026, committed and pushed BEFORE it was first run (rule 3).
Units (each cleared its own control; canvas 30 and 51 never included): f23 (interlinear/f23w_pairs.tsv, word pairs grouped by
their P-line, sign ids mapped back through interlinear/sign_ids.tsv), c32, c33, c3536, c3940, c47, c48, c49, c50 (siblings/*_reconciled.tsv).
Tokens: digit-only groups (split/unsettled readings such as '24/29' are dropped, as in every earlier test). Gloss: letters only,
lowercase, v->u, j->i, bracketed editorial text removed (same norm as c5051_test.py).
Anchors: the ordered greedy walk of key_f23 C codes over the line's gloss (c5051_test.py's walk); each C code that scores is an anchor
with a gloss interval. C codes that do not score are dropped (neither anchor nor candidate).
Spans: INTERIOR only -- between two consecutive anchors in the same line; span codes are the non-C codes (key_f23 M, or absent from
key_f23) between them in code order, span text is the gloss between the two anchor intervals. Line-edge spans are not used.
Eligible span: 1 <= k <= 3 span codes and 1 <= L <= 12 letters of span text.
Statistic S (primary): for each non-anchor code c and letter n-gram g (1 <= |g| <= 4), U(c,g) = number of distinct units with an
eligible span that contains c and whose text contains g; score(c) = max(0, max_g U(c,g) - 1); S = sum over codes of score(c).
Only cross-unit agreement scores; repeats inside one unit do not.
Secondary (reported, not gating): S_exact -- k = 1 spans only, score(c) = max over texts t of (units whose k=1 span for c reads t) - 1.
Control B: same anchors, same spans, same code sets; span TEXTS permuted at random among eligible spans of equal length L, pooled over
all units, 2000 draws. The statistic depends on which text meets which code, so the control can differ from the real value; the
number of spans in a length class of one (which cannot move) is printed.
GATE: PASS iff S_real > p95(control B) and P(ctrl >= real) < 0.05.
Merge rule (rule 3, per unit): only units that cleared their own control are read at all, so any attestation counted here is on a
cleared unit; a candidate is written to key_f23_anchor.tsv only if the gate passes: grade C where >= 2 cleared units agree on its best
n-gram (unique best, longest of the ties at max U), else M. Nothing is written to key_f23.tsv or key.tsv by this script.
Usage: python3 siblings/anchor_split.py [--write]"""
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
                ('c5456', {'54', '55', '56'})):
    for r in csv.DictReader(open(f'{H}/{fn}_reconciled.tsv'), delimiter='\t'):
        L = r['line']; p = L[:2] if L[:2].isdigit() else L[0]
        if p not in pre: continue
        unit = f'c{p}' if fn in ('c4749', 'c5051', 'c5456') else fn
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
if '--write' in sys.argv and passed:
    with open(f'{T}/key_f23_anchor_5456.tsv', 'w') as f:
        f.write('code\tvalue\tgrade\tsource\tnote\n')
        for c, g, m, uniq, kv, us in cand:
            f.write(f"{c}\t{g}\t{'C' if uniq and m >= 2 else 'M'}\tR7A-COL26 anchor-split pairing, 12 cleared units\tunits={m} ({','.join(us)}); key_f23 {kv}\n")
    print('wrote key_f23_anchor_5456.tsv')
