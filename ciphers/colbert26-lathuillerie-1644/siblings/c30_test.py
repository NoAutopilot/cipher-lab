"""A2-COL6: does key_f23.tsv (built from f.23 only) read canvas 30 (folio 27, 8 May 1646) consistently with canvas 30's
own interlinear gloss? Statistic and gate fixed before the gloss passes were read (3 Oct 2026): per numeral line, walk the
codes in order; a code scores if its key_f23 value occurs in that line's gloss (letters only, lowercase, v->u, j->i) at or
after the end of the previous match (ordered greedy; the margin/kat.py walk). Primary set: C-grade codes; secondary: C+M.
Control 1 (the brief's): shuffle the gloss ASSIGNMENT -- the 11 reconciled glosses permuted over the 11 numeral lines,
10000 random permutations; codes and their order stay fixed, so only the gloss each run meets changes and the pooled score
can differ from the real one. Control 2: windows of equal length cut at random from the f.23 main-text gloss bank
(interlinear/f23w_pairs.tsv), 2000 per line, as in margin/kat.py. Gate: pooled C hits above control 1's p95 (P < 0.05).
Codes from ciphertext.tsv canvas 30 (two-pass, 97.3% agreement; positions 14/15 still ambiguous, kept as pass A).
Usage: python3 siblings/c30_test.py"""
import csv, random, re, os
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
def norm(s): return re.sub(r'[^a-z]', '', re.sub(r'\[[^\]]*\]', '', s.lower())).replace('v', 'u').replace('j', 'i')
key = {r['code']: (norm(r['value']), r['grade']) for r in csv.DictReader(open(f'{T}/key_f23.tsv'), delimiter='\t')}
runs = {}
for r in csv.DictReader(open(f'{T}/ciphertext.tsv'), delimiter='\t'):
    if r['canvas'] == '30': runs.setdefault(int(r['line']), []).append(r['token'])
gl = {int(r['line']): norm(r['gloss']) for r in csv.DictReader(open(f'{H}/c30_gloss_reconciled.tsv'), delimiter='\t')}
lines = sorted(gl)
bank = norm(''.join(r['plain_raw'] for r in csv.DictReader(open(f'{T}/interlinear/f23w_pairs.tsv'), delimiter='\t')))
def walk(codes, gloss, grades):
    p = 0; hit = n = 0; hits = []
    for c in codes:
        if c not in key or key[c][1] not in grades: continue
        n += 1; i = gloss.find(key[c][0], p)
        if i >= 0: hit += 1; p = i + len(key[c][0]); hits.append(c)
    return hit, n, hits
def pct(xs, q): xs = sorted(xs); return xs[min(len(xs) - 1, int(q * len(xs)))]
rng = random.Random(20261003)
print('line\tset\treal\tn\thits')
real = {}
for name, grades in (('C', {'C'}), ('all', {'C', 'M'})):
    tot = 0; n = 0
    for L in lines:
        h, k, hits = walk(runs[L], gl[L], grades); tot += h; n += k
        print(f"{L}\t{name}\t{h}\t{k}\t{' '.join(f'{c}={key[c][0]}' for c in hits)}")
    real[name] = (tot, n)
print('\nset\treal\tn\tctrl\tmean\tp95\tmax\tP(ctrl>=real)')
for name, grades in (('C', {'C'}), ('all', {'C', 'M'})):
    h, n = real[name]
    perm = []
    for _ in range(10000):
        g = [gl[L] for L in lines]; rng.shuffle(g)
        perm.append(sum(walk(runs[L], g[i], grades)[0] for i, L in enumerate(lines)))
    win = []
    for _ in range(2000):
        s = 0
        for L in lines:
            st = rng.randrange(0, len(bank) - len(gl[L])); s += walk(runs[L], bank[st:st + len(gl[L])], grades)[0]
        win.append(s)
    for cn, c in (('shuffled-gloss', perm), ('f23-window', win)):
        print(f"{name}\t{h}\t{n}\t{cn}\t{sum(c)/len(c):.2f}\t{pct(c,.95)}\t{max(c)}\t{sum(x>=h for x in c)/len(c):.4f}")
