"""A2-COL14: key_f23.tsv C codes on canvas 47, 48 and 49 (folio 43-45, La Thuillerie to Servien, La Haye; canvas 47-48 is one letter
closing "A la Haye ce 20e Janvier 1648" (docket on canvas 47 "18 [?] Janvier 1648"); canvas 49 opens the next letter, which closes on
canvas 51 "le 23e Janvier 1648") against each leaf's own interlinear gloss.
Pre-registered 3 Oct 2026 (copy of c3940_test.py, statistic, control, gate and floor unchanged), committed BEFORE the canvas 47-49 images
were cropped or either blind pass was read.
Input: siblings/c4749_reconciled.tsv (columns: line, tokens, gloss, note; line ids '47L01', '48L01', '49L01' ... carry the canvas).
Statistic (unchanged): per numeral line, the ordered greedy walk -- a code scores if its key_f23 value occurs in that line's gloss
(letters only, lowercase, v->u, j->i) at or after the end of the previous match. Primary set C-grade codes; secondary C+M.
UNITS (brief: one result per canvas): canvas 47, canvas 48 and canvas 49 are each scored ALONE, each with its own gate, never pooled with
each other or with earlier units. Also reported, NOT gating: 'letter4748' (canvas 47+48 together, the one letter of 20 Jan 1648).
GATE per canvas: the LENGTH-MATCHED f23-window control -- each line's gloss replaced by a random window of the same length cut from
the f.23 main-text gloss bank (interlinear/f23w_pairs.tsv), 5000 draws; codes and order fixed, so only the French each
run meets changes and the score can differ from the real one. Pass = that canvas's C hits with P(ctrl>=real) < 0.05.
Also reported, not gating: shuffled-gloss (glosses permuted over that unit's lines, 10000 permutations).
Power floor, written before scoring: a unit with fewer than 15 C-valued occurrences is reported 'TOO-SHORT' whatever P is
(canvas 48 is expected to carry only ~5 groups, leaves.tsv).
A pass extends attestation only: no code enters key_f23.tsv or key.tsv from this script.
Usage: python3 siblings/c4749_test.py"""
import csv, random, re, os
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
def norm(s): return re.sub(r'[^a-z]', '', re.sub(r'\[[^\]]*\]', '', s.lower())).replace('v', 'u').replace('j', 'i')
key = {r['code']: (norm(r['value']), r['grade']) for r in csv.DictReader(open(f'{T}/key_f23.tsv'), delimiter='\t')}
runs, gl = {}, {}
for r in csv.DictReader(open(f'{H}/c4749_reconciled.tsv'), delimiter='\t'):
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
rng = random.Random(20261003 + 4749)
units = [('canvas47', ['47']), ('canvas48', ['48']), ('canvas49', ['49']), ('letter4748', ['47', '48'])]
print('line\tset\treal\tn\thits')
for name, grades in (('C', {'C'}), ('all', {'C', 'M'})):
    for L in lines:
        h, k, hits = walk(runs[L], gl[L], grades)
        print(f"{L}\t{name}\t{h}\t{k}\t{' '.join(f'{c}={key[c][0]}' for c in hits)}")
print('\nscope\tset\treal\tn\tctrl\tmean\tp95\tmax\tP(ctrl>=real)\tgate')
for uname, cans in units:
    ul = [L for L in lines if L[:2] in cans]
    if not ul: print(f"{uname}\t-\t-\t0\t-\t-\t-\t-\t-\tNO-LINES"); continue
    for name, grades in (('C', {'C'}), ('all', {'C', 'M'})):
        h = sum(walk(runs[L], gl[L], grades)[0] for L in ul); n = sum(walk(runs[L], gl[L], grades)[1] for L in ul)
        win = []
        for _ in range(5000):
            s = 0
            for L in ul:
                st = rng.randrange(0, len(bank) - len(gl[L])); s += walk(runs[L], bank[st:st + len(gl[L])], grades)[0]
            win.append(s)
        perm = []
        for _ in range(10000):
            g = [gl[L] for L in ul]; rng.shuffle(g)
            perm.append(sum(walk(runs[L], g[i], grades)[0] for i, L in enumerate(ul)))
        for cn, c in (('f23-window', win), ('shuffled-gloss', perm)):
            P = sum(x >= h for x in c) / len(c)
            gate = '-'
            if (name, cn) == ('C', 'f23-window') and uname != 'letter4748': gate = 'TOO-SHORT' if n < 15 else ('PASS' if P < 0.05 else 'FAIL')
            print(f"{uname}\t{name}\t{h}\t{n}\t{cn}\t{sum(c)/len(c):.2f}\t{pct(c,.95)}\t{max(c)}\t{P:.4f}\t{gate}")
# Also reported (not gating): every occurrence of code 12 (key_f23 12 = c, grade C) with its line's gloss.
print('\ncode12\tline\tgloss')
for L in lines:
    if '12' in runs[L]: print(f"12\t{L}\t{gl[L]}")
