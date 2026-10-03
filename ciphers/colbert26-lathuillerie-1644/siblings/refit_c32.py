#!/usr/bin/env python3
"""A2-COL8, 3 Oct 2026: re-fit key_f23 with tools/interlinear_align.py on the f.23 word pairs (interlinear/f23w_pairs.tsv,
116 pairs, P36 still held out) plus the canvas 32 glossed rows (siblings/c32_reconciled.tsv, 22 rows) and canvas 30's glossed
lines (siblings/c30_gloss_reconciled.tsv + ciphertext.tsv canvas 30, 11 lines). Statistic, controls, gates and key rule fixed
here and committed before the first run.
Flags as A2-COL2/3: codes renumbered 100+code, --floor 100 --keep-fs (tool default --max-chunk 14). Unsettled groups ('?')
dropped; gloss words in [brackets] dropped (same normalisation as c30_test.py / c32_test.py).
Statistic: tokens with status 'agrees' (chunk = the code's majority reading over >= 2 occurrences), total and on the
sibling rows only (canvas 30 + 32), and on canvas 32 alone.
Control A (shuffled gloss assignment within each unit): f.23 glosses dealt in a random derangement over the f.23 runs,
canvas 32 glosses over canvas 32 rows, canvas 30 over canvas 30; 50 seeds. Control B (length-matched window, as A2-COL7):
f.23 pairs kept real, every canvas 30/32 gloss replaced by a same-letter-length window cut at random from the f.23 gloss
bank; 50 seeds. Both move the French each cipher run meets, which is what 'agrees' depends on, so both can differ from the
real fit. Gates: G1 real total > control A p95; G2 real sibling agrees > control B p95. Both must pass before any key change.
Key rule (rule 3 per-unit merge clause): a code is C when, counting only occurrences on units that cleared their own
length-matched control (f.23, canvas 32), n >= 2 and >= 2/3 of them take the code's majority chunk; canvas 30 occurrences
are reported per code ('attest' column) but never count toward C. Output: siblings/refit_c32_out.txt, siblings/key_refit.tsv,
and the joint alignment siblings/refit_align.tsv.
Usage: python3 siblings/refit_c32.py"""
import csv, random, re, subprocess, sys, tempfile, os
from collections import Counter, defaultdict
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
TOOL = os.path.join(T, '../../tools/interlinear_align.py')
FLAGS = ['--floor', '100', '--keep-fs']
SEED, N = 20261003, 50

def norm(s): return re.sub(r'[^a-z ]', '', re.sub(r'\[[^\]]*\]', '', s.lower())).replace('v', 'u').replace('j', 'i')
def raw(codes): return ' '.join(str(100 + int(c)) for c in codes if re.fullmatch(r'\d\d', c))

pairs = []  # (unit, dict)
for r in csv.DictReader(open(f'{T}/interlinear/f23w_pairs.tsv'), delimiter='\t'):
    pairs.append(('f23', r))
for r in csv.DictReader(open(f'{H}/c32_reconciled.tsv'), delimiter='\t'):
    g = ' '.join(norm(r['gloss']).split()); c = raw(r['tokens'].split())
    if g and c: pairs.append(('c32', dict(plain_line=g, plain_raw=g, cipher_line='C32' + r['line'], cipher_raw=c)))
runs = defaultdict(list)
for r in csv.DictReader(open(f'{T}/ciphertext.tsv'), delimiter='\t'):
    if r['canvas'] == '30': runs[int(r['line'])].append(r['token'])
for r in csv.DictReader(open(f'{H}/c30_gloss_reconciled.tsv'), delimiter='\t'):
    g = ' '.join(norm(r['gloss']).split()); c = raw(runs[int(r['line'])])
    if g and c: pairs.append(('c30', dict(plain_line=g, plain_raw=g, cipher_line='C30L%02d' % int(r['line']), cipher_raw=c)))
unit_of = {p['cipher_line']: u for u, p in pairs}
bank = re.sub(r'[^a-z]', '', norm(''.join(p['plain_raw'] for u, p in pairs if u == 'f23')))

def run(prs, keep=None):
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, 'p.tsv')
        with open(p, 'w') as f:
            w = csv.DictWriter(f, fieldnames=['plain_line', 'plain_raw', 'cipher_line', 'cipher_raw'], delimiter='\t',
                               lineterminator='\n', extrasaction='ignore')
            w.writeheader(); w.writerows(prs)
        subprocess.run([sys.executable, TOOL, 'align', p, d + '/a.tsv', d + '/k.tsv'] + FLAGS, check=True, capture_output=True)
        rows = list(csv.DictReader(open(d + '/a.tsv'), delimiter='\t'))
        if keep: open(keep, 'w').write(open(d + '/a.tsv').read())
    tot = sum(r['status'] == 'agrees' for r in rows)
    sib = sum(r['status'] == 'agrees' and unit_of[r['cipher_line']] != 'f23' for r in rows)
    c32 = sum(r['status'] == 'agrees' and unit_of[r['cipher_line']] == 'c32' for r in rows)
    return (tot, sib, c32), rows

def pct(xs, q): xs = sorted(xs); return xs[min(len(xs) - 1, int(q * len(xs)))]
real, rows = run([p for u, p in pairs], keep=f'{H}/refit_align.tsv')
rng = random.Random(SEED); ctlA = []; ctlB = []
for _ in range(N):
    sh = []
    for unit in ('f23', 'c32', 'c30'):
        ps = [p for u, p in pairs if u == unit]
        while True:
            perm = list(range(len(ps))); rng.shuffle(perm)
            if all(i != j for i, j in enumerate(perm)): break
        sh += [dict(p, plain_line=ps[j]['plain_line'], plain_raw=ps[j]['plain_raw']) for p, j in zip(ps, perm)]
    ctlA.append(run(sh)[0])
for _ in range(N):
    sh = []
    for u, p in pairs:
        if u == 'f23': sh.append(p); continue
        L = len(p['plain_line'].replace(' ', '')); st = rng.randrange(0, len(bank) - L)
        sh.append(dict(p, plain_line=bank[st:st + L], plain_raw=bank[st:st + L]))
    ctlB.append(run(sh)[0])
out = open(f'{H}/refit_c32_out.txt', 'w')
def say(s): print(s); out.write(s + '\n')
say('pairs\tf23 %d\tc32 %d\tc30 %d\ttokens %d' % tuple([sum(u == x for u, _ in pairs) for x in ('f23', 'c32', 'c30')] + [len(rows)]))
say('stat\treal\tctrl\tmean\tp95\tmax\tP(ctrl>=real)\tgate')
gates = {}
for k, name in ((0, 'agrees_total'), (1, 'agrees_sibling'), (2, 'agrees_c32')):
    for cn, c in (('A-derange-within-unit', ctlA), ('B-f23-window', ctlB)):
        v = [x[k] for x in c]; g = '-'
        if (k, cn[0]) == (0, 'A'): g = gates['G1'] = 'PASS' if real[0] > pct(v, .95) else 'FAIL'
        if (k, cn[0]) == (1, 'B'): g = gates['G2'] = 'PASS' if real[1] > pct(v, .95) else 'FAIL'
        say(f'{name}\t{real[k]}\t{cn}\t{sum(v)/N:.1f}\t{pct(v,.95)}\t{max(v)}\t{sum(x>=real[k] for x in v)/N:.2f}\t{g}')
# key with per-unit attestation
occ = defaultdict(list)
for r in rows:
    if r['kind'] == 'num' and r['plain_chunk']: occ[int(r['value']) - 100].append((unit_of[r['cipher_line']], r['plain_chunk']))
    elif r['kind'] == 'num': occ[int(r['value']) - 100].append((unit_of[r['cipher_line']], ''))
with open(f'{H}/key_refit.tsv', 'w') as f:
    f.write('code\tvalue\tgrade\tsource\tnote\n')
    for code in sorted(occ):
        allc = Counter(ch for u, ch in occ[code] if ch)
        if not allc: continue
        val = allc.most_common(1)[0][0]
        cl = [ch for u, ch in occ[code] if u in ('f23', 'c32')]
        agree = sum(ch == val for ch in cl)
        grade = 'C' if len(cl) >= 2 and agree * 3 >= 2 * len(cl) else 'M'
        att = ' '.join('%s:%d/%d' % (u, sum(ch == val for uu, ch in occ[code] if uu == u), sum(uu == u for uu, _ in occ[code]))
                       for u in ('f23', 'c32', 'c30') if any(uu == u for uu, _ in occ[code]))
        f.write(f'{code}\t{val}\t{grade}\tjoint interlinear_align fit f.23 word pairs + canvas 32 + canvas 30 (A2-COL8); '
                f'C counts f.23 + canvas 32 only\tattest {att}; others={dict(allc - Counter({val: allc[val]}))}\n')
say('gates\t' + ' '.join(f'{k} {v}' for k, v in gates.items()))
