"""A2-COL7: pooled canvas 30 + canvas 32 test of key_f23.tsv against each leaf's own interlinear gloss.
Pre-registered 3 Oct 2026, committed BEFORE the canvas 32 passes were read or reconciled.
Canvas 32 (folio 27v-28r, the continuation of canvas 30's 8 May 1646 letter): numerals and gloss per line from
siblings/c32_reconciled.tsv (columns: line, tokens, gloss; tokens space-separated, '?' or bracketed = unsettled and
skipped; gloss brackets dropped by norm()). Canvas 30 exactly as siblings/c30_test.py (ciphertext.tsv + c30_gloss_reconciled.tsv).
Statistic (unchanged from c30_test.py): per numeral line, the ordered greedy walk -- a code scores if its key_f23 value
occurs in that line's gloss (letters only, lowercase, v->u, j->i) at or after the end of the previous match.
Primary set C-grade codes; secondary C+M. Pooled over all lines of both canvases.
GATE (A2-COL6's harder control): the LENGTH-MATCHED f23-window control -- each line's gloss replaced by a random window
of the same length cut from the f.23 main-text gloss bank (interlinear/f23w_pairs.tsv), 5000 draws; codes and order
fixed, so only the French each run meets changes and the score can differ from the real one. Pass = pooled C hits above
that control's p95 (P(ctrl>=real) < 0.05). Also reported, not gating: shuffled-gloss (glosses permuted over all pooled
lines, 10000 permutations) and the canvas-32-only numbers. A pass extends attestation only: no code enters key_f23.tsv
or key.tsv from this script.
Usage: python3 siblings/c32_test.py"""
import csv, random, re, os
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
def norm(s): return re.sub(r'[^a-z]', '', re.sub(r'\[[^\]]*\]', '', s.lower())).replace('v', 'u').replace('j', 'i')
key = {r['code']: (norm(r['value']), r['grade']) for r in csv.DictReader(open(f'{T}/key_f23.tsv'), delimiter='\t')}
runs, gl = {}, {}
for r in csv.DictReader(open(f'{T}/ciphertext.tsv'), delimiter='\t'):
    if r['canvas'] == '30': runs.setdefault(('30', int(r['line'])), []).append(r['token'])
for r in csv.DictReader(open(f'{H}/c30_gloss_reconciled.tsv'), delimiter='\t'): gl[('30', int(r['line']))] = norm(r['gloss'])
for r in csv.DictReader(open(f'{H}/c32_reconciled.tsv'), delimiter='\t'):
    k = ('32', r['line']); runs[k] = [t for t in r['tokens'].split() if t.isdigit()]; gl[k] = norm(r['gloss'])
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
rng = random.Random(20261003 + 32)
print('canvas\tline\tset\treal\tn\thits')
for name, grades in (('C', {'C'}), ('all', {'C', 'M'})):
    for L in lines:
        if L[0] != '32': continue
        h, k, hits = walk(runs[L], gl[L], grades)
        print(f"{L[0]}\t{L[1]}\t{name}\t{h}\t{k}\t{' '.join(f'{c}={key[c][0]}' for c in hits)}")
print('\nscope\tset\treal\tn\tctrl\tmean\tp95\tmax\tP(ctrl>=real)\tgate')
for scope in ('pooled30+32', 'canvas32'):
    ls = [L for L in lines if scope == 'pooled30+32' or L[0] == '32']
    for name, grades in (('C', {'C'}), ('all', {'C', 'M'})):
        h = sum(walk(runs[L], gl[L], grades)[0] for L in ls); n = sum(walk(runs[L], gl[L], grades)[1] for L in ls)
        win = []
        for _ in range(5000):
            s = 0
            for L in ls:
                st = rng.randrange(0, len(bank) - len(gl[L])); s += walk(runs[L], bank[st:st + len(gl[L])], grades)[0]
            win.append(s)
        perm = []
        for _ in range(10000):
            g = [gl[L] for L in ls]; rng.shuffle(g)
            perm.append(sum(walk(runs[L], g[i], grades)[0] for i, L in enumerate(ls)))
        for cn, c in (('f23-window', win), ('shuffled-gloss', perm)):
            P = sum(x >= h for x in c) / len(c)
            gate = ('PASS' if P < 0.05 else 'FAIL') if (scope, name, cn) == ('pooled30+32', 'C', 'f23-window') else '-'
            print(f"{scope}\t{name}\t{h}\t{n}\t{cn}\t{sum(c)/len(c):.2f}\t{pct(c,.95)}\t{max(c)}\t{P:.4f}\t{gate}")
