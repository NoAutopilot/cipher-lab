#!/usr/bin/env python3
"""694/08 frame 0490 gutter run, gate (a) with the leaf's own clear rendering as one span (MANT-GUT, 9 Oct 2026; PREREG-MANTGUT.md).
Alignment = f0490_08/gloss_gate_L.py's, copied unchanged (letters(), align()). Digits: blind passes passA_L.tsv / passB_L.tsv, crop c0490G01,
'?' stripped (deciding); ciphertext_L.tsv reconciled (reported only). Rendering: render_R1.txt / render_R2.txt, blind Sonnet passes used as
written. Control: key values permuted over codes, 1000 draws, seed 491. Gate per row: S > p99 and S >= 0.5 x keyed; gate PASS = all 4 rows.
Run from the repository root: python3 ciphers/sachsstaatsarchiv-manteuffel-1712/f0490_08/gutter_gate.py [--check]"""
import csv, os, random, sys, unicodedata
D = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(D)
key = {}
for r in csv.DictReader(open(f'{T}/key.tsv'), delimiter='\t'):
    if r['value'].strip(): key[r['code']] = r['value']
def letters(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.replace('roy', 'roi')
    return ''.join(c for c in s if c.isalpha())
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
def digits(fn):
    return [r['token'].replace('?', '') for r in csv.DictReader(open(f'{D}/{fn}'), delimiter='\t') if r['crop'] == 'c0490G01']
def recon():
    return [r[3] for r in csv.reader(open(f'{D}/ciphertext_L.tsv'), delimiter='\t') if len(r) > 3 and r[1] == 'c0490G01']
def cls(c, k):
    if c not in k: return 'unkeyed'
    return 'letter' if all(len(letters(v)) <= 1 for v in k[c].split('|')) else 'multi'
CL = ('letter', 'multi', 'unkeyed')
def score(codes, g, k):
    a, path = align(codes, g, k)
    per = {c: 0 for c in CL}; pos = []
    for i, (c, op, s) in enumerate(path):
        if op == 'match': per[cls(c, key)] += 1; pos.append(i)
    return a, per, path, pos
rend = {n: open(f'{D}/render_{n}.txt').read().replace('\n', ' ').strip() for n in ('R1', 'R2')}
digs = {'passA': digits('passA_L.tsv'), 'passB': digits('passB_L.tsv'), 'recon': recon()}
codes0 = list(key); vals0 = [key[c] for c in codes0]
out = [f'key: key.tsv ({len(key)} valued codes); renderings: R1 {rend["R1"]!r}; R2 {rend["R2"]!r}']
matched = {}
verdicts = []
for dn in ('passA', 'passB', 'recon'):
    for rn in ('R1', 'R2'):
        cs = digs[dn]; g = rend[rn]
        nkeyed = sum(c in key for c in cs); ncls = {x: sum(cls(c, key) == x for c in cs) for x in CL}
        real, per, path, pos = score(cs, g, key)
        rng = random.Random(491); vals = list(vals0); ctl = []; cper = {x: [] for x in CL}
        for _ in range(1000):
            rng.shuffle(vals); kk = dict(zip(codes0, vals)); a, p, _, _ = score(cs, g, kk); ctl.append(a)
            for x in CL: cper[x].append(p[x])
        ctl.sort(); p95, p99 = ctl[949], ctl[989]
        dec = dn != 'recon'
        v = 'too short' if nkeyed < 10 else ('PASS' if real > p99 and real >= 0.5 * nkeyed else 'FAIL')
        if dec: verdicts.append(v)
        out += [f'== {dn} x {rn} ({"deciding" if dec else "reported only"}): tokens {len(cs)}, keyed {nkeyed}',
                f'S = {real}/{nkeyed}; control mean {sum(ctl)/1000:.2f}, p95 {p95}, p99 {p99}, max {ctl[-1]}; control >= real {sum(c >= real for c in ctl)}/1000; {v}',
                '  per class (real matched/tokens | control mean, p99): ' + '; '.join(
                    f'{x} {per[x]}/{ncls[x]} | {sum(cper[x])/1000:.2f}, {sorted(cper[x])[989]}' for x in CL),
                '  path: ' + ' '.join(f'{c}:{op}:{s}' for c, op, s in path)]
        if dec:
            for i, (c, op, s) in enumerate(path):
                matched.setdefault(i, []).append((c, op == 'match'))
gate = 'PASS' if verdicts and all(v == 'PASS' for v in verdicts) else 'FAIL'
out += ['', f'GATE (a), all four deciding rows PASS: {gate} ({", ".join(verdicts)})']
allm = [i for i, v in matched.items() if len(v) == 4 and all(m for _, m in v) and len({c for c, _ in v}) == 1]
out.append(f'positions matched on all four deciding rows (same code): {len(allm)} -> ' + ' '.join(f'{i+1}:{matched[i][0][0]}' for i in allm))
cnt = {}
for i in allm: cnt[matched[i][0][0]] = cnt.get(matched[i][0][0], 0) + 1
gradem = {r['code']: r['grade'] for r in csv.DictReader(open(f'{T}/key.tsv'), delimiter='\t')}
out.append('key M codes matched at >= 2 positions on all four rows: ' + (', '.join(f'{c}({key[c]}) x{n}' for c, n in cnt.items() if n >= 2 and gradem.get(c) == 'M') or 'none'))
txt = '\n'.join(out) + '\n'; OUTF = f'{D}/gutter_gate.out'
if '--check' in sys.argv:
    good = os.path.exists(OUTF) and open(OUTF).read() == txt; print('gutter_gate.out up to date' if good else 'STALE'); sys.exit(0 if good else 1)
open(OUTF, 'w').write(txt); print(txt, end='')
