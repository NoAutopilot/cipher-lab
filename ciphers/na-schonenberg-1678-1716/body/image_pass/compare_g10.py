#!/usr/bin/env python3
"""GAPS10 2 Oct 2026: blind GROUP re-read of the transcription-confidence-M body positions (ciphertext.tsv conf M, L01-L14).
Readers saw the line crops, the group count and the starred positions only -- not the expected groups, the key, the gloss
column or sense_inferences.tsv. Reads g10_passA_b*.tsv / g10_passB_b*.tsv, aligns each pass's group sequence to the
committed transcription (ciphertext_before_GAPS10.tsv) with difflib (equal-length replace blocks map one to one), and
classes each starred position: CONFIRM (both passes read the committed group), CHANGE (both passes agree on another group),
SPLIT (anything else). g10_settled.tsv (the reconciliation) may override a CHANGE/SPLIT with a settled group.
Rule-3 controls, 20 seeds: (1) GROUP: the committed group vs the settled blind group at the starred positions, the committed
groups shuffled across the same positions; (2) KEY / SENSE: the committed M value (reading_tokens_before_GAPS10.tsv) and the
sense letter (body/sense_inferences.tsv, else the key value) vs the key value of the settled group, predictions shuffled.
Usage: python3 compare_g10.py [--seeds 20]"""
import csv, random, sys, os, difflib
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(os.path.dirname(H))
seeds = int(sys.argv[sys.argv.index('--seeds') + 1]) if '--seeds' in sys.argv else 20
EQ = {'v': 'b', 'y': 'i', 'j': 'i', 'z': 'c'}
def nl(s):
    s = (s or '').lower().strip(); s = '-' if s in ('null', '_', '-', '', '(none)') else s
    return ''.join(EQ.get(ch, ch) for ch in s)
def ng(g): return (g or '').strip().replace(' ', '').lower()
def rd(p): return list(csv.DictReader(open(p, encoding='utf-8'), delimiter='\t'))
cur = rd(os.path.join(H, 'ciphertext_before_GAPS10.tsv'))
lines = {}
for r in cur:
    if r['line'] <= 'L14': lines.setdefault(r['line'], []).append(r)
starred = [(r['line'], r['pos']) for r in cur if r['line'] <= 'L14' and r['conf'] == 'M']
def load(tag):
    out = {}
    for b in (1, 2, 3):
        p = os.path.join(H, 'g10_pass%s_b%d.tsv' % (tag, b))
        if not os.path.exists(p): continue
        by = {}
        for r in rd(p): by.setdefault(r['line'], []).append(r)
        for L, rs in by.items():
            rs.sort(key=lambda r: int(r['pos'])); seen = [ng(r['group_seen']) for r in rs]
            ref = [ng(r['group']) for r in lines[L]]
            for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ref, seen, autojunk=False).get_opcodes():
                if op == 'equal' or (op == 'replace' and i2 - i1 == j2 - j1):
                    for k in range(i2 - i1): out[(L, str(i1 + k))] = rs[j1 + k]
    return out
A, B = load('A'), load('B')
settled_p = os.path.join(H, 'g10_settled.tsv')
settled = {(r['line'], r['pos']): r for r in rd(settled_p)} if os.path.exists(settled_p) else {}
curg = {(r['line'], r['pos']): ng(r['group']) for r in cur}
common = [k for k in curg if k in A and k in B and k[0] <= 'L14']
print('pass agreement (group, all aligned positions): %d of %d' % (sum(ng(A[k]['group_seen']) == ng(B[k]['group_seen']) for k in common), len(common)))
cls = {}; fin = {}
for k in starred:
    a = ng(A[k]['group_seen']) if k in A else None; b = ng(B[k]['group_seen']) if k in B else None
    c = 'CONFIRM' if a == b == curg[k] else 'CHANGE' if (a is not None and a == b) else 'SPLIT'
    if k in settled:
        c2 = settled[k]['class']; g = ng(settled[k]['group']) or (curg[k] if c2 == 'CONFIRM' else None)
        if g == 'delete' or c2 == 'SPLIT': g = None
    else: c2 = c; g = a if c in ('CONFIRM', 'CHANGE') else None
    cls[k] = c2; fin[k] = g
    print('%s pos%-2s cur=%-9s A=%-9s B=%-9s %s%s' % (k[0], k[1], curg[k], a, b, c, (' -> settled %s %s' % (c2, g)) if k in settled else ''))
from collections import Counter
print('starred positions: %d; classes (blind) %s; after reconciliation %s' % (len(starred), dict(Counter(
    'CONFIRM' if (k in A and k in B and ng(A[k]['group_seen']) == ng(B[k]['group_seen']) == curg[k]) else
    'CHANGE' if (k in A and k in B and ng(A[k]['group_seen']) == ng(B[k]['group_seen'])) else 'SPLIT' for k in starred)), dict(Counter(cls.values()))))
key = {r['code']: r['value'] for r in rd(os.path.join(H, 'key_before_GAPS10.tsv'))}
ex = {(r['line'], r['pos']): r['value'] for r in rd(os.path.join(H, 'exceptions_before_GAPS10.tsv'))}
before = {(r['line'], r['pos']): r for r in rd(os.path.join(H, 'reading_tokens_before_GAPS10.tsv'))}
sense = {(r['line'], r['pos']): r['sense_letter'] for r in rd(os.path.join(T, 'body', 'sense_inferences.tsv'))}
rkey = {ng(c): v for c, v in key.items()}
def ctl(rows, eq):
    real = sum(eq(p, s) for _, p, s in rows); ps = [p for _, p, _ in rows]; out = []
    for sd in range(1, seeds + 1):
        q = ps[:]; random.Random(sd).shuffle(q); out.append(sum(eq(p, s) for (_, _, s), p in zip(rows, q)))
    return real, out
ok = [k for k in starred if fin.get(k)]
rows = [(k, curg[k], fin[k]) for k in ok]
real, c = ctl(rows, lambda p, s: p == s)
print('GROUP committed vs settled blind group: REAL %d/%d; shuffled (%d seeds) mean %.2f max %d, at or above real %d' % (real, len(rows), seeds, sum(c) / len(c), max(c), sum(x >= real for x in c)))
okv = [k for k in ok if fin[k] in rkey and k not in ex]
for lab, pf in (('KEY', lambda k: before[k]['value']), ('SENSE', lambda k: sense[k] if sense.get(k, '') not in ('', '(none)', '(unread)') else before[k]['value'])):
    rows = [(k, pf(k), rkey[fin[k]]) for k in okv]
    real, c = ctl(rows, lambda p, s: nl(p) == nl(s))
    print('%s prediction vs key value of the settled blind group (non-exception, keyed): REAL %d/%d; shuffled mean %.2f max %d, at or above real %d' % (lab, real, len(rows), sum(c) / len(c), max(c), sum(x >= real for x in c)))
    for k, p, s in rows:
        if nl(p) != nl(s): print('  DIFFER %s pos%s pred=%s settled-group value=%s' % (k[0], k[1], p, s))
