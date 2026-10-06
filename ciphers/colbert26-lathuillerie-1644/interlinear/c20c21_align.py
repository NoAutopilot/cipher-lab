#!/usr/bin/env python3
"""A4-COLALN, 6 Oct 2026: interlinear_align on the canvas 20-21 reconciled gloss pairs (A4-RFCOL), with a deranged-gloss
control per unit (rule 3 per-unit clause). PRE-REGISTERED before any run (rule, flags, gate, seeds fixed here).

Pairs: c20c21_reconciled.tsv, one pair per row. Signs mapped to numeric ids via sign_ids.tsv (f.24's map); signs not in it get
ids from 160 up in order of first appearance (written to c20c21_sign_ids.tsv). Unglossed tails named in the row's notes
("<tokens> unglossed", a suffix of cipher_tokens) are cut before alignment; "[?]" and punctuation are stripped from the gloss.
Flags as f24_control.py: --floor 100 --keep-fs --max-chunk 6 --word-prior, prior c20c21_seed.tsv = key_f24's two codes that
read in place on these canvases (A4-RFCOL known-answer: 83 de 6/6, 31 que 4/4). 25 (par vs m, rule 4 conflict) is not seeded.
Statistic: tokens with status 'agrees' (chunk = the code's majority reading over >=2 occurrences), all and unseeded.
Control: within one unit (c20 rows or c21 rows), the gloss lines dealt out in a derangement (no row keeps its own gloss),
same flags, 200 seeds, SEED 20261006. Gate per unit: real agrees_all > control p95 AND real agrees_unseeded > control p95.
Joint c20+c21 fit is run and reported but is a diagnostic; a code enters key_period.tsv at C only if every occurrence it
'agrees' on lies in a unit that cleared its own gate and it agrees on >=2 occurrences; otherwise M (lead)."""
import csv, random, re, subprocess, sys, tempfile, os
SEED, N = 20261006, 200
HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(HERE, '../../../tools/interlinear_align.py')
SEEDF = os.path.join(HERE, 'c20c21_seed.tsv')
FLAGS = ['--floor', '100', '--keep-fs', '--max-chunk', '6', '--prior', SEEDF, '--word-prior']

ids = {r['sign']: r['id'] for r in csv.DictReader(open(os.path.join(HERE, 'sign_ids.tsv')), delimiter='\t')}
nxt = 160
rows = list(csv.DictReader(open(os.path.join(HERE, 'c20c21_reconciled.tsv')), delimiter='\t'))
pairs = {'c20': [], 'c21': []}
for r in rows:
    toks = r['cipher_tokens'].split()
    m = re.search(r"([^;:]*?)\s+unglossed", r['notes'])
    if m:
        tail = m.group(1).split()
        # keep only the longest suffix of tail that is a suffix of toks
        while tail and toks[-len(tail):] != tail: tail = tail[1:]
        if tail: toks = toks[:-len(tail)]
    for t in toks:
        if t not in ids: ids[t] = str(nxt); nxt += 1
    plain = re.sub(r"\[\?\]", " ", r['gloss_text'])
    plain = re.sub(r"[^A-Za-z' ]", " ", plain); plain = re.sub(r"\s+", " ", plain).strip()
    pairs[r['unit'][:3]].append({'plain_line': plain, 'plain_raw': plain, 'cipher_line': r['unit'],
                                 'cipher_raw': ' '.join(ids[t] for t in toks)})
with open(os.path.join(HERE, 'c20c21_sign_ids.tsv'), 'w') as f:
    f.write('sign\tid\n'); [f.write('%s\t%s\n' % kv) for kv in ids.items()]
with open(SEEDF, 'w') as f:
    f.write('code\tmeaning\tsign\tbasis\n%s\tde\t83\tkey_f24 C, A4-RFCOL 6/6\n%s\tque\t31\tkey_f24 C, A4-RFCOL 4/4\n' % (ids['83'], ids['31']))
seeded = {ids['83'], ids['31']}
inv = {v: k for k, v in ids.items()}

def run(ps, keep=None):
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, 'p.tsv')
        with open(p, 'w') as f:
            w = csv.DictWriter(f, fieldnames=list(ps[0].keys()), delimiter='\t', lineterminator='\n'); w.writeheader(); w.writerows(ps)
        subprocess.run([sys.executable, TOOL, 'align', p, d + '/a.tsv', d + '/k.tsv'] + FLAGS, check=True, capture_output=True)
        al = list(csv.DictReader(open(d + '/a.tsv'), delimiter='\t')); key = list(csv.DictReader(open(d + '/k.tsv'), delimiter='\t'))
        if keep:
            for src, dst in ((d + '/a.tsv', keep + '_align.tsv'), (d + '/k.tsv', keep + '_key_raw.tsv'), (p, keep + '_pairs.tsv')):
                open(dst, 'w').write(open(src).read())
    tot = sum(r['status'] == 'agrees' for r in al)
    return tot, sum(r['status'] == 'agrees' and r['value'] not in seeded for r in al), al

def control(ps, rng):
    out = []
    for _ in range(N):
        while True:
            perm = list(range(len(ps))); rng.shuffle(perm)
            if all(i != j for i, j in enumerate(perm)): break
        out.append(run([dict(p, plain_line=ps[j]['plain_line'], plain_raw=ps[j]['plain_raw']) for p, j in zip(ps, perm)])[:2])
    return out

rng = random.Random(SEED); res = {}
for u in ('c20', 'c21'):
    real = run(pairs[u], keep=os.path.join(HERE, u + 'u'))
    ctl = control(pairs[u], rng); ok = True
    for k, name in ((0, 'agrees_all'), (1, 'agrees_unseeded')):
        v = sorted(c[k] for c in ctl); p95 = v[int(0.95 * N) - 1]; ok &= real[k] > p95
        print('%s\t%s\treal %d\tcontrol mean %.1f p95 %d max %d\tP(ctl>=real) %.3f' % (u, name, real[k], sum(v) / N, p95, v[-1], sum(x >= real[k] for x in v) / N))
    print('%s\tGATE %s' % (u, 'PASS' if ok else 'FAIL')); res[u] = (ok, real[2])
j = run(pairs['c20'] + pairs['c21'], keep=os.path.join(HERE, 'c20c21'))
print('joint\tagrees_all %d agrees_unseeded %d (diagnostic, not gated)' % j[:2])
# per-code summary over the per-unit fits, with which unit each agreeing occurrence sits in
from collections import defaultdict
occ = defaultdict(list)
for u in ('c20', 'c21'):
    for r in res[u][1]:
        occ[r['value']].append((u, r['plain_chunk'], r['status']))
with open(os.path.join(HERE, 'c20c21_codes.tsv'), 'w') as f:
    f.write('sign\tid\tn\tagree\tunits_agree\tmajority\tchunks\tgrade_rule\n')
    for v, L in sorted(occ.items(), key=lambda kv: -len(kv[1])):
        ag = [x for x in L if x[2] == 'agrees']
        maj = ag[0][1] if ag else ''
        units = sorted({x[0] for x in ag})
        grade = 'C' if len(ag) >= 2 and all(res[x][0] for x in units) else 'M'
        f.write('%s\t%s\t%d\t%d\t%s\t%s\t%s\t%s\n' % (inv.get(v, v), v, len(L), len(ag), ','.join(units), maj, ','.join(x[1] for x in L), grade))
