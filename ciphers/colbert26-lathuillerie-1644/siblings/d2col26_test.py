"""D2-COL26 (8 Oct 2026): value-independent test of 20 i, 30 s, 67 leur, 81 me/il, 85 na/luy, 96 que on glossed two-digit sibling
units outside every R10-COL26B value-choice unit (c30, c33, c51, c62). Registered in PREREG-D2-COL26.md before it was run.
Statistic: anchor-bracketed ordered walk at line grain; controls L (length-matched f.23 windows) and S (shuffled gloss within unit).
Usage: python3 siblings/d2col26_test.py"""
import csv, os, re, random
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
def norm(s): return re.sub(r'[^a-z]', '', re.sub(r'\[[^\]]*\]', '', s.lower())).replace('v', 'u').replace('j', 'i')
key = {r['code']: (norm(r['value']), r['grade']) for r in csv.DictReader(open(f'{T}/key_f23.tsv'), delimiter='\t')}
ANC = {c: v for c, (v, g) in key.items() if g == 'C' and v}
TEST = [('20', 'i'), ('30', 's'), ('67', 'leur'), ('81', 'me'), ('81', 'il'), ('85', 'na'), ('85', 'luy'), ('96', 'que')]
assert not set(c for c, _ in TEST) & set(ANC)
ALPHA = 0.05 / 6; D = 10000
units = {}
runs = {}
for r in csv.DictReader(open(f'{T}/ciphertext.tsv'), delimiter='\t'):
    if r['canvas'] == '30': runs.setdefault(int(r['line']), []).append(r['token'])
units['c30'] = [(runs.get(int(r['line']), []), norm(r['gloss'])) for r in csv.DictReader(open(f'{H}/c30_gloss_reconciled.tsv'), delimiter='\t')]
def rec(fn, pref=''):
    return [([x for x in r['tokens'].split() if x != '|' and x.isdigit()], norm(r['gloss']))
            for r in csv.DictReader(open(f'{H}/{fn}'), delimiter='\t') if r['line'].startswith(pref)]
units['c33'] = rec('c33_reconciled.tsv'); units['c51'] = rec('c5051_reconciled.tsv', '51'); units['c62'] = rec('c6263_reconciled.tsv', '62')
for u in units: units[u] = [(c, g) for c, g in units[u] if c and g]
bank = norm(''.join(r['plain_raw'] for r in csv.DictReader(open(f'{T}/interlinear/f23w_pairs.tsv'), delimiter='\t')))
def anchors(codes, gloss):
    p = 0; m = {}
    for j, c in enumerate(codes):
        if c in ANC:
            i = gloss.find(ANC[c], p)
            if i >= 0: m[j] = (i, i + len(ANC[c])); p = i + len(ANC[c])
    return m
def score(codes, gloss, tests):
    m = anchors(codes, gloss); out = []
    for j, c in enumerate(codes):
        for k, (tc, v) in enumerate(tests):
            if c != tc: continue
            lo = max([m[a][1] for a in m if a < j], default=0); hi = min([m[a][0] for a in m if a > j], default=len(gloss))
            i = gloss.find(v, lo); out.append((k, i >= 0 and i + len(v) <= hi))
    return len(m), out
rng = random.Random(20261008)
def ctrlL(lines):
    return [(c, bank[s:s + len(g)]) for c, g in lines for s in [rng.randrange(0, len(bank) - len(g))]]
def ctrlS(lines):
    gs = [g for _, g in lines]; rng.shuffle(gs); return [(c, g) for (c, _), g in zip(lines, gs)]
def tally(lines):
    a = 0; hits = [0] * len(TEST); n = [0] * len(TEST)
    for c, g in lines:
        ah, o = score(c, g, TEST); a += ah
        for k, h in o: n[k] += 1; hits[k] += h
    return a, hits, n
def pctl(xs, q): xs = sorted(xs); return xs[min(len(xs) - 1, int(q * len(xs)))]
print('D2-COL26 bracketed-walk test; anchors', len(ANC), 'key_f23 C codes; units', {u: len(v) for u, v in units.items()})
real = {}; CL = {}; CS = {}
cleared = []
for u, lines in units.items():
    real[u] = tally(lines)
    CL[u] = [tally(ctrlL(lines)) for _ in range(D)]; CS[u] = [tally(ctrlS(lines)) for _ in range(D)]
    ca = [x[0] for x in CL[u]]; p95 = pctl(ca, 0.95); P = sum(x >= real[u][0] for x in ca) / D
    ok = real[u][0] > p95 and P < 0.05; cleared += [u] if ok else []
    print(f'instrument {u}: anchor hits {real[u][0]} vs L p95 {p95} max {max(ca)} P {P:.4f} -> {"CLEARS" if ok else "FAILS"}')
print('code\tvalue\tN\tH\tper_unit\tL_mean\tL_p95\tL_P\tL_Pmin\tS_mean\tS_p95\tS_P\tverdict')
for k, (c, v) in enumerate(TEST):
    N = sum(real[u][2][k] for u in cleared); Hh = sum(real[u][1][k] for u in cleared)
    per = ' '.join(f'{u}:{real[u][1][k]}/{real[u][2][k]}' for u in units if real[u][2][k])
    if N < 5: print(f'{c}\t{v}\t{N}\t{Hh}\t{per}\t-\t-\t-\t-\t-\t-\t-\tTOO-SHORT'); continue
    res = []
    for C in (CL, CS):
        dist = [sum(C[u][d][1][k] for u in cleared) for d in range(D)]
        res.append((sum(dist) / D, pctl(dist, 0.95), sum(x >= Hh for x in dist) / D, sum(x >= N for x in dist) / D))
    (lm, lp, lP, lPm), (sm, sp, sP, _) = res
    verdict = 'UNDERPOWERED' if lPm >= ALPHA else ('PASS' if Hh > lp and lP < ALPHA and Hh > sp and sP < ALPHA else 'FAIL')
    print(f'{c}\t{v}\t{N}\t{Hh}\t{per}\t{lm:.2f}\t{lp}\t{lP:.4f}\t{lPm:.4f}\t{sm:.2f}\t{sp}\t{sP:.4f}\t{verdict}')
