#!/usr/bin/env python3
"""694/08 frame 0490 (MANT-0490, 9 Oct 2026): copy of f0089_08/gloss_gate.py (statistic unchanged), right page only; deciding row excludes the R01-line span (r01line=y), a second row includes it (reported),
seed 490, as fixed in f0490_08/PREREG-MANT0490.md before scoring. --print scores print_spans.tsv (Acta Borussica BO I p.212) -> gate_print.out. Gloss text is the blind pass's, letters only ('?' dropped). gloss_spans.tsv: span_id, line, gloss,
codes (space-separated tokens from ciphertext.tsv, in order). Alignment: a code whose key value (any '|' alternative, letters only)
equals the next gloss letters scores 1; a code may consume 1-3 gloss letters unmatched (0) or none (-0.25); a gloss letter may be
skipped (-0.25). S = matched codes summed over spans. Control: values permuted over codes, 1000 draws, seed 8.
python3 f0490_08/gloss_gate.py [--print] [--key FILE] [--check]   (--check exits 1 if gate.out is stale)"""
import csv, os, random, sys, unicodedata
D = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(D)
KEY = sys.argv[sys.argv.index('--key') + 1] if '--key' in sys.argv else f'{T}/key.tsv'
def letters(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.replace('roy', 'roi')
    return ''.join(c for c in s if c.isalpha())
key = {}
for r in csv.DictReader(open(KEY), delimiter='\t'):
    if r['value'].strip(): key[r['code']] = r['value']
spans = [r for r in csv.DictReader(open(f'{D}/' + ('print_spans.tsv' if '--print' in sys.argv else 'gloss_spans.tsv')), delimiter='\t')]
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
def S(k, sp):
    return sum(align(r['codes'].split(), r['gloss'], k)[0] for r in sp)
codes = list(key); vals0 = [key[c] for c in codes]
out = [f'key: {os.path.relpath(KEY, T)}; spans {len(spans)}']
for name, sp in (('R deciding (right page, R01 line excluded)', [r for r in spans if r['page'] == 'R' and r.get('r01line', 'n') != 'y']), ('R incl. R01 line (reported only)', [r for r in spans if r['page'] == 'R'])):
    real = S(key, sp)
    ntok = sum(len(r['codes'].split()) for r in sp); nkeyed = sum(c in key for r in sp for c in r['codes'].split())
    vals = list(vals0); rng = random.Random(490); ctl = []
    for _ in range(1000):
        rng.shuffle(vals); ctl.append(S(dict(zip(codes, vals)), sp))
    ctl.sort(); p95, p99 = ctl[949], ctl[989]
    if nkeyed < 10: verdict = 'too short (< 10 keyed code tokens): neither PASS nor FAIL'
    else: verdict = 'PASS' if (real > p99 and real >= 0.5 * nkeyed) else 'FAIL'
    out += [f'== {name}: spans {len(sp)}; code tokens {ntok}; keyed {nkeyed}',
            f'S = {real}/{nkeyed} keyed ({real/max(nkeyed,1):.3f}); control (1000 permutations, seed 490): mean {sum(ctl)/len(ctl):.2f}, p95 {p95}, p99 {p99}, max {ctl[-1]}; control >= real {sum(c >= real for c in ctl)}/1000',
            f'GATE (S > p99 and S >= 0.5 x keyed): {verdict}']
out += ['', 'per span (code:op:gloss-letters):']
per = {}
for r in spans:
    a, path = align(r['codes'].split(), r['gloss'], key)
    out.append(f"{r['span_id']}\t{r['page']}\t{r['gloss']}\t{a}/{len(r['codes'].split())}\t" + ' '.join(f'{c}:{op}:{s}' for c, op, s in path))
    for c, op, s in path: per.setdefault(c, []).append((op, s))
out += ['', 'distinct codes: ' + str(len(per)) + '; matched on every instance: ' + str(sum(all(o == 'match' for o, _ in v) for v in per.values())),
        'unkeyed codes and their slots: ' + '; '.join(f'{c}=' + ','.join(s or '0' for _, s in v) for c, v in sorted(per.items(), key=lambda x: int(x[0]) if x[0].isdigit() else 9999) if c not in key),
        'keyed codes with a non-match slot: ' + '; '.join(f'{c}({key[c]})=' + ','.join(f'{o}:{s}' for o, s in v if o != 'match') for c, v in sorted(per.items(), key=lambda x: int(x[0]) if x[0].isdigit() else 9999) if c in key and any(o != 'match' for o, _ in v))]
txt = '\n'.join(out) + '\n'
OUTF = f'{D}/' + ('gate_print.out' if '--print' in sys.argv else 'gate.out')
dst = OUTF if '--key' not in sys.argv else None
if '--check' in sys.argv:
    good = open(OUTF).read() == txt; print('gate.out up to date' if good else 'STALE'); sys.exit(0 if good else 1)
if dst: open(dst, 'w').write(txt)
print(txt, end='')
