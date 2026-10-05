#!/usr/bin/env python3
"""D2-B117KAPC step 3: which f.117r M tokens become S under the BIR-APPLY rule (two independent blind instruments agree),
now that the printed key is licensed at the measured post-look-alike error (la/PREREG-KAPC.md).

Rule, fixed before counting:
 1. base M token (conf M in ciphertext_f117_top1.tsv, no exception row): S iff the aligned tile of la/recon_f117_3r.tsv is firm
    (note 'lookalike 2-of-3' or 'lookalike confirms') and carries the same sign as top1.
 2. exception row 'BIR-OPEN single instrument only (open blind read X->Y ...)': S iff the aligned 3r tile is firm and carries Y.
 3. exception row 'A1 vs BIR-OPEN conflict': stays M (owner sorter).
Alignment per line: positional when the two lines have equal length, else difflib on the sign strings (unmatched -> stays M).
Writes la/kapc/m_to_s.tsv. Usage (from harvest/f117): python3 la/kapc/m_to_s.py
"""
import csv, re, difflib, collections
NB = '../../../nevers-birago-fr3251-1572/harvest/tx_decode/eye/'
top = [r for r in csv.DictReader(open(NB + 'verify/ciphertext_f117_top1.tsv'), delimiter='\t')]
exc = {(r['line'], int(r['pos'])): r for r in csv.DictReader(open(NB + 'apply/exceptions_apply_f117.tsv'), delimiter='\t')}
G = {(r['line'], int(r['pos'])): r['grade'] for r in csv.DictReader(open(NB + 'apply/reading_f117_apply_tokens.tsv'), delimiter='\t')}
r3 = [r for r in csv.DictReader(open('la/recon_f117_3r.tsv'), delimiter='\t')]
T = collections.defaultdict(list); R = collections.defaultdict(list)
for r in top: T[r['line'].replace('f117_', '')].append(r)
for r in r3: R[r['passage']].append(r)
out = []
for ln in sorted(T):
    a, b = T[ln], R.get(ln, [])
    amap = {}
    if len(a) == len(b):
        amap = {i: i for i in range(len(a))}
    else:
        sm = difflib.SequenceMatcher(None, [x['sign'] for x in a], [x['sign_id'] for x in b], autojunk=False)
        for blk in sm.get_matching_blocks():
            for k in range(blk.size): amap[blk.a + k] = blk.b + k
    for i, t in enumerate(a):
        pos = int(t['pos']); e = exc.get((ln, pos))
        if G.get((ln, pos)) != 'M': continue  # only tokens graded M in the committed apply reading
        kind = None; want = t['sign']
        if e is not None:
            if e['grade'] != 'M': continue
            if 'conflict' in e['reason']: kind = 'conflict'
            else:
                kind = 'single'; m = re.search(r'->(\w+)', e['reason']); want = m.group(1)
        elif t['conf'] == 'M': kind = 'base'
        else: continue
        j = amap.get(i); s3 = b[j] if j is not None else None
        firm = s3 is not None and s3['note'] in ('lookalike 2-of-3', 'lookalike confirms')
        new = 'S' if kind != 'conflict' and firm and s3['sign_id'] == want else 'M'
        out.append((ln, pos, t['sign'], want, kind, s3['sign_id'] if s3 else '-', s3['note'] if s3 else 'unaligned', new,
                    'equal-length' if len(a) == len(b) else 'difflib'))
with open('la/kapc/m_to_s.tsv', 'w') as f:
    f.write('line\tpos\ttop1_sign\tsign_required\tkind\tsign_3r\tnote_3r\tnew_grade\talign\n')
    for o in out: f.write('\t'.join(map(str, o)) + '\n')
c = collections.Counter((o[4], o[7]) for o in out)
print('M tokens considered', len(out), dict(c))
