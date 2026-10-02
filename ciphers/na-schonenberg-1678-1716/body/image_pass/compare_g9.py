#!/usr/bin/env python3
"""GAPS9 2 Oct 2026: the third image pass (L01, L02, L04 = batch 1; L06, L08, L09 = batch 2; L11, L13 = batch 3). Reads the two blind passes
(g9_passA_b*.tsv, g9_passB_b*.tsv) and g9_settled.tsv (the reconciliation), reports pass-to-pass agreement, and compares the
predictions for the key's M-graded positions with the settled image letter, against a control that shuffles the predicted
letters across the same positions (20 seeds, rule 3). Two prediction sources: KEY (the M value key.tsv/exceptions.tsv
give the position, reading_tokens.tsv as committed before GAPS9 = key_before_GAPS9 snapshot) and SENSE (body/sense_inferences.tsv
where it names a letter, else the key value). Letters compared under the hand's own equivalences b=v, i=y=j, c=z.
Usage: python3 compare_g9.py [--seeds 20]"""
import csv, random, sys, os
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(os.path.dirname(H))
EQ = {'v': 'b', 'y': 'i', 'j': 'i', 'z': 'c'}
def norm(s):
    s = s.lower().strip(); s = '-' if s in ('null', '_', '-', '') else s  # NULL = no letter (one notation, rule 3)
    return ''.join(EQ.get(ch, ch) for ch in s)
seeds = int(sys.argv[sys.argv.index('--seeds') + 1]) if '--seeds' in sys.argv else 20
LINES = ['L01', 'L02', 'L04', 'L06', 'L08', 'L09', 'L11', 'L13']
def load(pat):
    d = {}
    for b in (1, 2, 3):
        p = os.path.join(H, pat % b)
        if os.path.exists(p):
            for r in csv.DictReader(open(p, encoding='utf-8'), delimiter='\t'): d[(r['line'], r['pos'])] = r
    return d
A, B = load('g9_passA_b%d.tsv'), load('g9_passB_b%d.tsv')
common = [k for k in A if k in B and k[0] in LINES]
same = sum(norm(A[k]['gloss']) == norm(B[k]['gloss']) for k in common)
print('pass agreement (gloss letter, normalised): %d of %d common positions' % (same, len(common)))
for L in LINES:
    ks = [k for k in common if k[0] == L]
    print('  %s: %d of %d' % (L, sum(norm(A[k]['gloss']) == norm(B[k]['gloss']) for k in ks), len(ks)))
before = {(r['line'], r['pos']): r for r in csv.DictReader(open(os.path.join(H, 'reading_tokens_before_GAPS9.tsv'), encoding='utf-8'), delimiter='\t')}
sense = {(r['line'], r['pos']): r['sense_letter'] for r in csv.DictReader(open(os.path.join(T, 'body', 'sense_inferences.tsv'), encoding='utf-8'), delimiter='\t')}
settled = {(r['line'], r['pos']): r['letter'] for r in csv.DictReader(open(os.path.join(H, 'g9_settled.tsv'), encoding='utf-8'), delimiter='\t')}
mpos = [k for k, r in sorted(before.items()) if k[0] in LINES and r['grade'] == 'M' and settled.get(k, '?') not in ('?', '')]
for lab, predf in (('KEY', lambda k: before[k]['value']),
                   ('SENSE', lambda k: sense[k] if sense.get(k, '') not in ('', '(none)', '(unread)') else before[k]['value'])):
    rows = [(k, predf(k), settled[k]) for k in mpos]
    def score(ps): return sum(norm(p) == norm(s) for (_, _, s), p in zip(rows, ps))
    real = score([p for _, p, _ in rows]); ctrl = []
    for sd in range(1, seeds + 1):
        ps = [p for _, p, _ in rows]; random.Random(sd).shuffle(ps); ctrl.append(score(ps))
    print('%s predictions vs settled image letter at the M positions: REAL %d/%d; shuffled predictions (%d seeds): mean %.2f, max %d, at or above real %d' % (
        lab, real, len(rows), seeds, sum(ctrl) / len(ctrl), max(ctrl), sum(x >= real for x in ctrl)))
    print('  control values:', ctrl)
    for k, p, s in rows:
        if norm(p) != norm(s): print('  DIFFER %s pos%s code %s pred=%s read=%s' % (k[0], k[1], before[k]['sign'], p, s))
