"""A2-COL10: key_f23.tsv C codes on canvas 33 (folio 29, La Haye, 6e [?] 1648) against the leaf's own interlinear gloss.
Pre-registered 3 Oct 2026, committed BEFORE the canvas 33 image was cropped or either blind pass was read.
Input: siblings/c33_reconciled.tsv (columns: line, tokens, gloss, note; tokens space-separated, '?' or non-digit =
unsettled and skipped; bracketed gloss words dropped by norm()), the same format as c32_reconciled.tsv.
Statistic (unchanged from c30_test.py / c32_test.py): per numeral line, the ordered greedy walk -- a code scores if its
key_f23 value occurs in that line's gloss (letters only, lowercase, v->u, j->i) at or after the end of the previous match.
Primary set C-grade codes; secondary C+M. Summed over all canvas 33 lines; canvas 33 is scored ALONE (one unit, per rule
3's per-unit clause), not pooled with canvas 30/32.
GATE: the LENGTH-MATCHED f23-window control -- each line's gloss replaced by a random window of the same length cut from
the f.23 main-text gloss bank (interlinear/f23w_pairs.tsv), 5000 draws; codes and order fixed, so only the French each
run meets changes and the score can differ from the real one. Pass = canvas 33 C hits with P(ctrl>=real) < 0.05.
Also reported, not gating: shuffled-gloss (glosses permuted over the canvas 33 lines, 10000 permutations).
Power note, written before scoring: if canvas 33 has fewer than 15 C-valued occurrences, the result is reported as
'too short to test' whatever P is (A2-COL6: 23 occurrences on canvas 30 gave no decision).
A pass extends attestation only: no code enters key_f23.tsv or key.tsv from this script.
Usage: python3 siblings/c33_test.py"""
import csv, random, re, os
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
def norm(s): return re.sub(r'[^a-z]', '', re.sub(r'\[[^\]]*\]', '', s.lower())).replace('v', 'u').replace('j', 'i')
key = {r['code']: (norm(r['value']), r['grade']) for r in csv.DictReader(open(f'{T}/key_f23.tsv'), delimiter='\t')}
runs, gl = {}, {}
for r in csv.DictReader(open(f'{H}/c33_reconciled.tsv'), delimiter='\t'):
    k = r['line']; runs[k] = [t for t in r['tokens'].split() if t.isdigit()]; gl[k] = norm(r['gloss'])
lines = sorted(k for k in gl if gl[k])
bank = norm(''.join(r['plain_raw'] for r in csv.DictReader(open(f'{T}/interlinear/f23w_pairs.tsv'), delimiter='\t')))
def walk(codes, gloss, grades):
    p = 0; hit = n = 0; hits = []
    for c in codes:
        if c not in key or key[c][1] not in grades: continue
        n += 1; i = gloss.find(key[c][0], p)
        if i >= 0: hit += 1; p = i + len(key[c][0]); hits.append(c)
    return hit, n, hits
def pct(xs, q): xs = sorted(xs); return xs[min(len(xs) - 1, int(q * len(xs)))]
rng = random.Random(20261003 + 33)
print('line\tset\treal\tn\thits')
for name, grades in (('C', {'C'}), ('all', {'C', 'M'})):
    for L in lines:
        h, k, hits = walk(runs[L], gl[L], grades)
        print(f"{L}\t{name}\t{h}\t{k}\t{' '.join(f'{c}={key[c][0]}' for c in hits)}")
print('\nscope\tset\treal\tn\tctrl\tmean\tp95\tmax\tP(ctrl>=real)\tgate')
for name, grades in (('C', {'C'}), ('all', {'C', 'M'})):
    h = sum(walk(runs[L], gl[L], grades)[0] for L in lines); n = sum(walk(runs[L], gl[L], grades)[1] for L in lines)
    win = []
    for _ in range(5000):
        s = 0
        for L in lines:
            st = rng.randrange(0, len(bank) - len(gl[L])); s += walk(runs[L], bank[st:st + len(gl[L])], grades)[0]
        win.append(s)
    perm = []
    for _ in range(10000):
        g = [gl[L] for L in lines]; rng.shuffle(g)
        perm.append(sum(walk(runs[L], g[i], grades)[0] for i, L in enumerate(lines)))
    for cn, c in (('f23-window', win), ('shuffled-gloss', perm)):
        P = sum(x >= h for x in c) / len(c)
        gate = '-'
        if (name, cn) == ('C', 'f23-window'): gate = 'TOO-SHORT' if n < 15 else ('PASS' if P < 0.05 else 'FAIL')
        print(f"canvas33\t{name}\t{h}\t{n}\tcn={cn}\t{sum(c)/len(c):.2f}\t{pct(c,.95)}\t{max(c)}\t{P:.4f}\t{gate}".replace('cn=', ''))
