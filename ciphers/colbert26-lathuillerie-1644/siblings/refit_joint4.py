#!/usr/bin/env python3
"""A2-COL12, 3 Oct 2026: pre-registered joint key revision folding the four units that each cleared their own
length-matched control -- f.23 (interlinear/f23w_pairs.tsv, 116 word pairs, P36 still held out), canvas 32
(siblings/c32w_pairs.tsv, A2-COL9 word-level where licensed), canvas 33 (siblings/c33_reconciled.tsv, 9 line pairs) and
canvas 35-36 (siblings/c3536_reconciled.tsv, 20 line pairs). Canvas 30 (tied/failed its own control, A2-COL6) is NOT an
input. Committed and pushed BEFORE the first run. Fit, statistic and controls are A2-COL9's refit_c32w.py unchanged:
tools/interlinear_align.py align, codes 100+code, --floor 100 --keep-fs; '?' and 'a/b' groups dropped; [bracketed] gloss
dropped. Statistic: tokens with status 'agrees', total and on the sibling units (c32+c33+c3536).
Control A: glosses dealt in a derangement within each unit, 50 seeds. Control B: f.23 real, every sibling gloss replaced by
a same-letter-length window of the f.23 gloss bank, 50 seeds. Both change the French each run meets, so both can differ
from the real fit. Gates: G1 real total > A p95; G2 real sibling agrees > B p95. Both must PASS before any key change.
Key rule (rule 3 per-unit merge clause; every input unit cleared its own control): joint grade C when n >= 2 over the four
units and >= 2/3 take the majority chunk; 'attest' column records agreeing/total per unit.
Key-change rule (applied only if G1 and G2 PASS): a code ENTERS key_f23.tsv at grade C only if (i) it is not already C
there, (ii) joint grade C, and (iii) its majority chunk is attested (agreeing occurrence) on >= 2 distinct units. An
existing C code is never re-valued from this fit (a conflict is reported, not resolved by majority -- rule 4).
12 = c re-test (pre-registered, independent of the DP fit): the ordered greedy walk of c32_test.py/c33_test.py/c3536_test.py
(full key_f23 C set) on every sibling line (c32_reconciled.tsv rows, c33, c3536); statistic = occurrences of code 12 that
score; control = the same length-matched f23-window (5000 draws). Rule: 12 is downgraded C -> M (data-conflict note) if its
real off-f.23 hits <= the control mean; otherwise it stays C. The same per-code table is printed for every C code, not gating.
Outputs: siblings/refit_joint4_out.txt, siblings/key_refit_joint4.tsv, siblings/refit_align_joint4.tsv.
Usage: python3 siblings/refit_joint4.py"""
import csv, random, re, subprocess, sys, tempfile, os
from collections import Counter, defaultdict
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
TOOL = os.path.join(T, '../../tools/interlinear_align.py')
FLAGS = ['--floor', '100', '--keep-fs']
SEED, N = 20261003 + 4, 50
UNITS = ('f23', 'c32', 'c33', 'c3536'); SIB = UNITS[1:]

def norm(s): return re.sub(r'[^a-z ]', '', re.sub(r'\[[^\]]*\]', '', s.lower())).replace('v', 'u').replace('j', 'i')
def raw(codes): return ' '.join(str(100 + int(c)) for c in codes if re.fullmatch(r'\d\d', c))

pairs = []
for r in csv.DictReader(open(f'{T}/interlinear/f23w_pairs.tsv'), delimiter='\t'): pairs.append(('f23', r))
for i, r in enumerate(csv.DictReader(open(f'{H}/c32w_pairs.tsv'), delimiter='\t')):
    g = ' '.join(norm(r['gloss']).split()); c = raw(r['codes'].split())
    if g and c: pairs.append(('c32', dict(plain_line=g, plain_raw=g, cipher_line='C32%sw%02d' % (r['row'], i), cipher_raw=c)))
for u, fn in (('c33', 'c33_reconciled.tsv'), ('c3536', 'c3536_reconciled.tsv')):
    for r in csv.DictReader(open(f'{H}/{fn}'), delimiter='\t'):
        g = ' '.join(norm(r['gloss']).split()); c = raw(r['tokens'].split())
        if g and c: pairs.append((u, dict(plain_line=g, plain_raw=g, cipher_line='%s_%s' % (u.upper(), r['line']), cipher_raw=c)))
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
    ag = Counter(unit_of[r['cipher_line']] for r in rows if r['status'] == 'agrees')
    return (sum(ag.values()), sum(ag[u] for u in SIB), ag['c32'], ag['c33'], ag['c3536']), rows

def pct(xs, q): xs = sorted(xs); return xs[min(len(xs) - 1, int(q * len(xs)))]
real, rows = run([p for u, p in pairs], keep=f'{H}/refit_align_joint4.tsv')
rng = random.Random(SEED); ctlA = []; ctlB = []
for _ in range(N):
    sh = []
    for unit in UNITS:
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
out = open(f'{H}/refit_joint4_out.txt', 'w')
def say(s): print(s); out.write(s + '\n')
say('pairs\t' + '\t'.join('%s %d' % (x, sum(u == x for u, _ in pairs)) for x in UNITS) + '\ttokens %d' % len(rows))
say('stat\treal\tctrl\tmean\tp95\tmax\tP(ctrl>=real)\tgate')
gates = {}
for k, name in enumerate(('agrees_total', 'agrees_sibling', 'agrees_c32', 'agrees_c33', 'agrees_c3536')):
    for cn, c in (('A-derange-within-unit', ctlA), ('B-f23-window', ctlB)):
        v = [x[k] for x in c]; g = '-'
        if (k, cn[0]) == (0, 'A'): g = gates['G1'] = 'PASS' if real[0] > pct(v, .95) else 'FAIL'
        if (k, cn[0]) == (1, 'B'): g = gates['G2'] = 'PASS' if real[1] > pct(v, .95) else 'FAIL'
        say(f'{name}\t{real[k]}\t{cn}\t{sum(v)/N:.1f}\t{pct(v,.95)}\t{max(v)}\t{sum(x>=real[k] for x in v)/N:.2f}\t{g}')
say('gates\t' + ' '.join(f'{k} {v}' for k, v in gates.items()))
# joint key with per-unit attestation
kf = {r['code']: r for r in csv.DictReader(open(f'{T}/key_f23.tsv'), delimiter='\t')}
occ = defaultdict(list)
for r in rows:
    if r['kind'] == 'num': occ[int(r['value']) - 100].append((unit_of[r['cipher_line']], r['plain_chunk'] or ''))
enter = []
with open(f'{H}/key_refit_joint4.tsv', 'w') as f:
    f.write('code\tvalue\tgrade\tkey_f23\tunits_agreeing\tattest\tothers\n')
    for code in sorted(occ):
        allc = Counter(ch for u, ch in occ[code] if ch)
        if not allc: continue
        val = allc.most_common(1)[0][0]; n = len(occ[code]); agree = sum(ch == val for u, ch in occ[code])
        grade = 'C' if n >= 2 and agree * 3 >= 2 * n else 'M'
        ua = sorted({u for u, ch in occ[code] if ch == val})
        att = ' '.join('%s:%d/%d' % (u, sum(ch == val for uu, ch in occ[code] if uu == u), sum(uu == u for uu, _ in occ[code]))
                       for u in UNITS if any(uu == u for uu, _ in occ[code]))
        k0 = kf.get('%02d' % code) or kf.get(str(code)); k0s = '%s/%s' % (k0['value'], k0['grade']) if k0 else '-'
        if grade == 'C' and len(ua) >= 2 and not (k0 and k0['grade'] == 'C'): enter.append((code, val, att, k0s))
        f.write(f'{code}\t{val}\t{grade}\t{k0s}\t{",".join(ua)}\t{att}\t{dict(allc - Counter({val: allc[val]}))}\n')
ok = gates['G1'] == 'PASS' and gates['G2'] == 'PASS'
say('key-change candidates (joint C, >=2 units agreeing, not already C in key_f23): %d' % len(enter))
for e in enter: say('  %02d\t%s\t%s\tkey_f23 %s\t%s' % (e[0], e[1], e[2], e[3], 'ENTERS' if ok else 'blocked by gates'))
# 12 = c re-test, ordered greedy walk, length-matched control
def nw(s): return re.sub(r'[^a-z]', '', re.sub(r'\[[^\]]*\]', '', s.lower())).replace('v', 'u').replace('j', 'i')
key = {c: (nw(r['value']), r['grade']) for c, r in kf.items()}
lines = []
for fn, col in (('c32_reconciled.tsv', 'tokens'), ('c33_reconciled.tsv', 'tokens'), ('c3536_reconciled.tsv', 'tokens')):
    for r in csv.DictReader(open(f'{H}/{fn}'), delimiter='\t'):
        g = nw(r['gloss'])
        if g: lines.append(([t for t in r[col].split() if t.isdigit()], g))
wbank = nw(''.join(r['plain_raw'] for r in csv.DictReader(open(f'{T}/interlinear/f23w_pairs.tsv'), delimiter='\t')))
def walk(codes, gloss):
    p = 0; hit = Counter(); n = Counter()
    for c in codes:
        if c not in key or key[c][1] != 'C': continue
        n[c] += 1; i = gloss.find(key[c][0], p)
        if i >= 0: hit[c] += 1; p = i + len(key[c][0])
    return hit, n
rh, rn = Counter(), Counter()
for cs, g in lines:
    h, n = walk(cs, g); rh += h; rn += n
r2 = random.Random(SEED + 12); sims = defaultdict(list)
for _ in range(5000):
    s = Counter()
    for cs, g in lines:
        st = r2.randrange(0, len(wbank) - len(g)); s += walk(cs, wbank[st:st + len(g)])[0]
    for c in rn: sims[c].append(s[c])
say('\nper-code ordered walk off f.23 (c32+c33+c3536 lines, full key_f23 C set), length-matched f23-window 5000 draws')
say('code\tvalue\treal\tn\tctrl_mean\tp95\tP(ctrl>=real)\tdecision')
for c in sorted(rn, key=int):
    v = sims[c]; m = sum(v) / len(v); P = sum(x >= rh[c] for x in v) / len(v)
    dec = '-'
    if c == '12': dec = ('DOWNGRADE C->M (conflict)' if rh[c] <= m else 'stays C')
    say(f'{c}\t{key[c][0]}\t{rh[c]}\t{rn[c]}\t{m:.2f}\t{pct(v,.95)}\t{P:.4f}\t{dec}')
