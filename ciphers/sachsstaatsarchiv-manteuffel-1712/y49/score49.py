#!/usr/bin/env python3
"""MANT-Y49 scorer (PREREG-MANTY49.md): aligns each blind pass (y49/passA.tsv, passB.tsv) to the settled tokens of each
strip, reads the digit at every known slot's 4/9 position, and computes balanced accuracy vs the gloss-fixed label
with a permuted-label control (10,000 draws, seed 1712). Writes y49/reads.tsv and y49/score.txt; --check: exit 1 if stale."""
import csv, io, os, random, sys, contextlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
with contextlib.redirect_stdout(io.StringIO()):
    import census49 as C
strips = {r['label']: r for r in csv.DictReader(open(os.path.join(HERE, 'sheets', 'strips.tsv')), delimiter='\t')}
known = list(csv.DictReader(open(os.path.join(HERE, 'known.tsv')), delimiter='\t'))
def load(p):
    d = {}
    for l in open(os.path.join(HERE, p)):
        if '\t' in l and not l.startswith('NOTES'):
            a, b = l.rstrip('\n').split('\t', 1); d[a] = b.split()
    return d
def eq49(a, b):
    return len(a) == len(b) and all(x == y or (x in '49' and y in '49') for x, y in zip(a, b))
def align(S, R):
    n, m = len(S), len(R); D = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1): D[i][0] = i
    for j in range(m + 1): D[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            c = 0 if eq49(S[i-1], R[j-1]) else 1
            D[i][j] = min(D[i-1][j-1] + c, D[i-1][j] + 1, D[i][j-1] + 1)
    i, j, a = n, m, {}
    while i and j:
        c = 0 if eq49(S[i-1], R[j-1]) else 1
        if D[i][j] == D[i-1][j-1] + c: a[i-1] = R[j-1]; i, j = i - 1, j - 1
        elif D[i][j] == D[i-1][j] + 1: i -= 1
        else: j -= 1
    return a
crop2lab = {(r['leaf'], os.path.basename(r['source'])[:-4]): lab for lab, r in strips.items()}
passes = {p: load('pass%s.tsv' % p) for p in 'AB' if os.path.exists(os.path.join(HERE, 'pass%s.tsv' % p))}
reads = []
for k in known:
    lf, tid, crop, code = k['leaf'], k['tokid'], k['crop'], k['settled']
    lab = crop2lab[(lf, crop)]
    toks = [t for t in C.tl[lf] if t['crop'] == crop]
    S = [t['settled'] for t in toks]; i = [t['tokid'] for t in toks].index(tid)
    pos = [q for q, ch in enumerate(code) if ch in '49'][0]
    row = [lf, tid, lab, code, k['known']]
    for p in 'AB':
        if p not in passes: row += ['', '']; continue
        g = align(S, passes[p].get(lab, [])).get(i)
        dig = (g[pos] if g[pos] in '49' else 'other') if g and len(g) == len(code) else 'missing'
        row += [g or '', dig]
    reads.append(row)
def BA(labs, rd):
    out = []
    for c in '49':
        idx = [q for q, l in enumerate(labs) if l == c]
        out.append(sum(rd[q] == c for q in idx) / len(idx) if idx else 0.0)
    return (out[0] + out[1]) / 2, out
lines = []
labs = [r[4] for r in reads]
for p, col in (('A', 6), ('B', 8)):
    if p not in passes: continue
    rd = [r[col] for r in reads]
    ba, (r4, r9) = BA(labs, rd)
    rng = random.Random(1712); null = []
    for _ in range(10000):
        sh = labs[:]; rng.shuffle(sh); null.append(BA(sh, rd)[0])
    null.sort(); p99 = null[int(0.99 * len(null)) - 1]; mean = sum(null) / len(null)
    verdict = 'PASS' if ba > p99 and ba >= 0.80 else 'FAIL'
    lines.append('pass %s: N=%d BA %.3f (recall4 %.3f n=%d, recall9 %.3f n=%d) vs permuted mean %.3f p99 %.3f -> %s; reads 4/9/other/missing %d/%d/%d/%d'
                 % (p, len(rd), ba, r4, labs.count('4'), r9, labs.count('9'), mean, p99, verdict,
                    rd.count('4'), rd.count('9'), rd.count('other'), rd.count('missing')))
    for sub, name in ((lambda r: r[3] not in ('198', '191', '292'), 'excl. name codes 198/191/292'),
                      (lambda r: r[3][[q for q, ch in enumerate(r[3]) if ch in '49'][0]] != r[4], 'settled digit != label (y-candidates)')):
        rr = [r for r in reads if sub(r)]
        if rr:
            b, (a4, a9) = BA([r[4] for r in rr], [r[col] for r in rr])
            lines.append('   %s: N=%d BA %.3f recall4 %.3f recall9 %.3f; reads %s' % (name, len(rr), b, a4, a9,
                         ' '.join('%s:%s>%s' % (r[1], r[4], r[col]) for r in rr) if len(rr) <= 12 else ''))
    per = {}
    for r in reads: per.setdefault(r[0], []).append(r[col] == r[4])
    lines.append('   per leaf: ' + ' '.join('%s %d/%d' % (l, sum(v), len(v)) for l, v in sorted(per.items())))
if len(passes) == 2:
    both = [r for r in reads if r[6] == r[8] == r[4]]
    lines.append('both passes = label: %d/%d; passes agree on 4/9 digit: %d/%d' % (len(both), len(reads),
                 sum(r[6] == r[8] and r[6] in '49' for r in reads), len(reads)))
    gate = all('-> PASS' in l for l in lines if l.startswith('pass '))
    lines.append('GATE (both passes BA > p99 and >= 0.80): %s' % ('PASS' if gate else 'FAIL'))
H = 'leaf\ttokid\tlabel\tsettled\tknown\tA_group\tA_digit\tB_group\tB_digit\n'
out = {'reads.tsv': H + ''.join('\t'.join(r) + '\n' for r in reads), 'score.txt': '\n'.join(lines) + '\n'}
stale = False
for fn, txt in out.items():
    p = os.path.join(HERE, fn)
    if '--check' in sys.argv:
        if not os.path.exists(p) or open(p).read() != txt: print('STALE', fn); stale = True
    else: open(p, 'w').write(txt)
print(out['score.txt']); sys.exit(1 if stale else 0)
