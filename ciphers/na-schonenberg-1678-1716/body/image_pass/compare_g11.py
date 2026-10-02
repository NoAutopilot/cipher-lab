#!/usr/bin/env python3
"""GAPS11 2 Oct 2026: native-resolution blind pair on the 18 body M positions. Reports group and gloss agreement of the two blind
passes (g11_passA.tsv, g11_passB.tsv) and compares the committed (pre-GAPS11) values at the positions where both passes agree on the
gloss letter with that letter, against a control that shuffles the predicted letters across the same positions (rule 3; letters
under the hand's equivalences b=v, i=y=j, c=z; 'none' = NULL). Usage: python3 compare_g11.py [--seeds 20]"""
import csv, random, re, sys, os
H = os.path.dirname(os.path.abspath(__file__))
EQ = {'v': 'b', 'y': 'i', 'j': 'i', 'z': 'c'}
def norm(s):
    s = s.lower().strip().split(' ')[0].rstrip('.')
    s = '-' if s in ('none', 'null', '-', '') else s
    return ''.join(EQ.get(ch, ch) for ch in s)
seeds = int(sys.argv[sys.argv.index('--seeds') + 1]) if '--seeds' in sys.argv else 20
def load(p):
    lines, stars, sec = {}, {}, 0
    for row in open(os.path.join(H, p), encoding='utf-8').read().strip().split('\n'):
        if not row.strip(): continue
        f = row.split('\t')
        if f[0] == 'line': sec += 1; continue
        if sec == 1: lines[f[0]] = re.sub(r'\[[^\]]*\]', '[SYM]', f[1]).split(' ')  # a bracketed symbol counts as one group, named freely
        else: stars[(f[0], f[1])] = f
    return lines, stars
(LA, SA), (LB, SB) = load('g11_passA.tsv'), load('g11_passB.tsv')
tot = agree = 0
for L in LA:
    a, b = LA[L], LB[L]; tot += max(len(a), len(b)); agree += sum(x == y for x, y in zip(a, b))
print('whole-row group agreement (exact string; any bracketed symbol = [SYM]): %d of %d' % (agree, tot))
before = {(r['line'], r['pos']): r for r in csv.DictReader(open(os.path.join(H, 'reading_tokens_before_GAPS11.tsv'), encoding='utf-8'), delimiter='\t')}
rows = []
for k in sorted(SA):
    ga, gb = norm(SA[k][4]), norm(SB[k][4])
    if ga.isdigit(): continue  # L01 pos6: the gloss row carries the group number, not a letter
    print('  %s pos%s committed %s=%s  A %s  B %s  %s' % (k[0], k[1], before[k]['sign'], before[k]['value'], SA[k][4], SB[k][4], 'AGREE' if ga == gb else 'split'))
    if ga == gb: rows.append((k, before[k]['value'], ga))
def score(ps): return sum(norm(p) == s for (_, _, s), p in zip(rows, ps))
real = score([p for _, p, _ in rows]); ctrl = []
for sd in range(1, seeds + 1):
    ps = [p for _, p, _ in rows]; random.Random(sd).shuffle(ps); ctrl.append(score(ps))
print('gloss letter agreed by both passes: %d of %d starred letter positions' % (len(rows), len([k for k in SA if not norm(SA[k][4]).isdigit()])))
print('KEY M predictions vs agreed gloss letter: REAL %d/%d; shuffled predictions (%d seeds): mean %.2f, max %d, at or above real %d' % (
    real, len(rows), seeds, sum(ctrl) / len(ctrl), max(ctrl), sum(x >= real for x in ctrl)))
print('  control values:', ctrl)
for k, p, s in rows:
    if norm(p) != s: print('  DIFFER %s pos%s code %s pred=%s read=%s' % (k[0], k[1], before[k]['sign'], p, s))
