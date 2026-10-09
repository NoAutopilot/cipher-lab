#!/usr/bin/env python3
"""694/08 frame 0317, dispatch of 17 Sept 1712 (MANT-0317, 9 Oct 2026; copied unchanged from f0309_08/gloss_gate.py, MANT-0309, which is f0314_08's, MANT-XTR). Row (a) statistic copied unchanged from
f0474_08/gloss_gate.py; row (n) as MANT-XTR; seed 317, as fixed in f0317_08/PREREG-MANT0317.md before scoring.
Spans: f0317_08/spans_G{1,2}.tsv (written by build_spans.py from ciphertext.tsv + gloss{1,2}.tsv):
span_id, leaf, run, gloss, codes. Gloss text is the blind pass's, letters only ('?' dropped).
Row (a): runs with >= 2 codes, 0474 alignment (a code whose key value equals the next gloss letters scores 1; a code may consume 1-3 gloss
letters unmatched or none (-0.25); a gloss letter may be skipped (-0.25)). Row (n): runs with 1 code; gloss words (articles dropped) each a
prefix of a distinct value word, in order, the first on the first. Row (a-all): every span with row (a)'s statistic (continuity only).
Control: key values permuted over codes, 1000 draws, seed 317. Gate: S > p99 and S >= 0.5 x keyed; < 10 keyed = too short.
python3 f0317_08/gloss_gate.py [--key FILE] [--check]   (--check exits 1 if gate.out is stale)"""
import csv, os, random, sys, unicodedata, re
D = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(D)
KEY = sys.argv[sys.argv.index('--key') + 1] if '--key' in sys.argv else f'{T}/key.tsv'
def letters(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.replace('roy', 'roi')
    return ''.join(c for c in s if c.isalpha())
key = {}
for r in csv.DictReader(open(KEY), delimiter='\t'):
    if r['value'].strip(): key[r['code']] = r['value']
def align(codes, gloss, k):
    g = letters(gloss); n, m = len(codes), len(g); NEG = -1e9
    best = [[NEG] * (m + 1) for _ in range(n + 1)]; back = [[None] * (m + 1) for _ in range(n + 1)]
    best[0][0] = 0
    for i in range(n + 1):
        for j in range(m + 1):
            b = best[i][j]
            if b == NEG: continue
            if j < m and b - 0.25 > best[i][j + 1]: best[i][j + 1] = b - 0.25; back[i][j + 1] = (i, j, 'skip', '')
            if i == n: continue
            alts = [letters(v) for v in k.get(codes[i], '').split('|') if letters(v)] if codes[i] in k else []
            for v in alts:
                if g[j:j + len(v)] == v and b + 1 > best[i + 1][j + len(v)]:
                    best[i + 1][j + len(v)] = b + 1; back[i + 1][j + len(v)] = (i, j, 'match', v)
            for L in (1, 2, 3):
                if j + L <= m and b > best[i + 1][j + L]: best[i + 1][j + L] = b; back[i + 1][j + L] = (i, j, 'miss', g[j:j + L])
            if b - 0.25 > best[i + 1][j]: best[i + 1][j] = b - 0.25; back[i + 1][j] = (i, j, 'null', '')
    path = []; i, j = n, m
    while (i, j) != (0, 0):
        pi, pj, op, s = back[i][j]
        if op != 'skip': path.append((codes[pi], op, s))
        i, j = pi, pj
    path.reverse()
    return sum(1 for _, op, _ in path if op == 'match'), path
ART = {'le', 'la', 'les', 'l'}
def words(s):
    return [w for w in (letters(x) for x in re.split(r"[\s.:;,'’]+", s)) if w and w not in ART]
def name_match(code, gloss, k):
    gw = words(gloss)
    if not gw or code not in k: return 0
    for alt in k[code].split('|'):
        vw = words(alt)
        if not vw or not vw[0].startswith(gw[0]): continue
        j = 1; ok = True
        for w in gw[1:]:
            while j < len(vw) and not vw[j].startswith(w): j += 1
            if j == len(vw): ok = False; break
            j += 1
        if ok: return 1
    return 0
def S(k, sp, row):
    if row == 'n': return sum(name_match(r['codes'].split()[0], r['gloss'], k) for r in sp)
    return sum(align(r['codes'].split(), r['gloss'], k)[0] for r in sp)
codes = list(key); vals0 = [key[c] for c in codes]
out = [f'key: {os.path.relpath(KEY, T)}']
for gp in ('G1', 'G2'):
    spans = []
    for leaf in ('0317',):
        spans += [r for r in csv.DictReader(open(f'{T}/f{leaf}_08/spans_{gp}.tsv'), delimiter='\t')]
    out += ['', f'######## gloss pass {gp} ({"deciding" if gp == "G1" else "reported beside G1"}); spans {len(spans)}']
    for row, rname in (('a', 'row (a) letter runs (>= 2 codes)'), ('n', 'row (n) name runs (1 code)'), ('all', 'row (a-all) every span, 0474 statistic (continuity, not deciding)')):
        rsp = [r for r in spans if (row == 'all') or (row == 'a' and len(r['codes'].split()) >= 2) or (row == 'n' and len(r['codes'].split()) == 1)]
        for lname, sp in (('0317', rsp),):
            real = S(key, sp, 'n' if row == 'n' else 'a')
            ntok = sum(len(r['codes'].split()) for r in sp); nkeyed = sum(c in key for r in sp for c in r['codes'].split())
            vals = list(vals0); rng = random.Random(317); ctl = []
            for _ in range(1000):
                rng.shuffle(vals); ctl.append(S(dict(zip(codes, vals)), sp, 'n' if row == 'n' else 'a'))
            ctl.sort(); p95, p99 = ctl[949], ctl[989]
            if nkeyed < 10: verdict = 'too short (< 10 keyed code tokens): neither PASS nor FAIL'
            else: verdict = 'PASS' if (real > p99 and real >= 0.5 * nkeyed) else 'FAIL'
            out += [f'== {gp} {rname}, {lname}: spans {len(sp)}; code tokens {ntok}; keyed {nkeyed}',
                    f'S = {real}/{nkeyed} keyed ({real/max(nkeyed,1):.3f}); control (1000 permutations, seed 317): mean {sum(ctl)/len(ctl):.2f}, p95 {p95}, p99 {p99}, max {ctl[-1]}; control >= real {sum(c >= real for c in ctl)}/1000',
                    f'GATE (S > p99 and S >= 0.5 x keyed): {verdict}']
    out += ['', f'per span {gp} (code:op:gloss-letters; name rows: match 1/0):']
    for r in spans:
        cs = r['codes'].split()
        if len(cs) == 1:
            out.append(f"{r['span_id']}\t{r['leaf']}\t{r['gloss']}\t{name_match(cs[0], r['gloss'], key)}/1\t{cs[0]}={key.get(cs[0], '(unkeyed)')}")
        else:
            a, path = align(cs, r['gloss'], key)
            out.append(f"{r['span_id']}\t{r['leaf']}\t{r['gloss']}\t{a}/{len(cs)}\t" + ' '.join(f'{c}:{op}:{s}' for c, op, s in path))
txt = '\n'.join(out) + '\n'
OUTF = f'{D}/gate.out'
if '--check' in sys.argv:
    good = open(OUTF).read() == txt; print('gate.out up to date' if good else 'STALE'); sys.exit(0 if good else 1)
if '--key' not in sys.argv: open(OUTF, 'w').write(txt)
print(txt, end='')
