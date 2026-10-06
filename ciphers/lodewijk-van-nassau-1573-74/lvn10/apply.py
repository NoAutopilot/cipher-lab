#!/usr/bin/env python3
"""R12-LVN10 (6 Oct 2026): rebuild ciphertext_4610.tsv from lvn10/ciphertext_4610_pre.tsv (the file as it stood
before this job) and lvn10/aligned.tsv (blind 300-dpi passes A4/B4, lvn10/score.py), under lvn10/PREREG.md:
control gate (each pass >= 0.90 on agreed H rows) first; a non-H row is settled to H when A4 == B4 (exact, no '?'
edge mark, no '~' alignment mark); a slash group is split into its codes when A4 == B4 and the agreed token is the
row's sign (after any settle). Positions are renumbered within a line when a split adds rows; every changed row's
`why` names the original position. Writes lvn10/apply_log.tsv. --check: exit 1 if either output is stale (rule 7).
Note: ../settle.py also writes ciphertext_4610.tsv (R20 lineage); do not run it for 4610 after this job
(after R12-LVN16 and this job run `settle.py --letters 4611,4612` only), or it will undo these settles."""
import csv, io, os, sys
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
def rd(p): return list(csv.DictReader(open(p), delimiter='\t'))
pre = rd(os.path.join(H, 'ciphertext_4610_pre.tsv'))
al = {(r['line'], r['position']): r for r in rd(os.path.join(H, 'aligned.tsv'))}
ctl = {'A4': [0, 0], 'B4': [0, 0]}
for r in al.values():
    if r['role'] == 'control':
        for k in ctl: ctl[k][1] += 1; ctl[k][0] += r[k] == r['sign']
gate = all(c / n >= 0.90 for c, n in ctl.values())
cols = ['line', 'position', 'sign', 'confidence', 'alt', 'why']
out, log = [], []
lastline, pos = None, 0
for r in pre:
    if r['line'] != lastline: lastline, pos = r['line'], 0
    a = al.get((r['line'], r['position']))
    sign, conf, alt, why = r['sign'], r['confidence'], r['alt'], r['why']
    act = ''
    if a and a['role'] == 'target' and gate:
        A, B = a['A4'], a['B4']
        clean = A == B and '?' not in A and '~' not in A and A != '-'
        if conf != 'H':
            if clean:
                act = 'settled' if A != sign else 'confirmed'
                alt = f'was {sign} {conf}' + (f'; {alt}' if alt else '')
                sign, conf, why = A, 'H', f'image300 lvn10 (A4=B4={A}; pre pos {r["position"]})'
            else:
                act = 'stays'
                alt = (alt + '; ' if alt else '') + f'lvn10 A4:{A} B4:{B}'
        if '/' in sign:
            if clean and A == sign:
                parts = sign.split('/')
                for j, p in enumerate(parts):
                    pos += 1
                    out.append([r['line'], str(pos), p, conf, '', f'split lvn10 from pre pos {r["position"]} ({sign}), part {j + 1}/{len(parts)}; image300 A4=B4'])
                log.append([r['line'], r['position'], r['sign'], r['confidence'], A, B, (act + '+' if act else '') + 'split'])
                continue
            act = act or 'slash-kept'
            if 'lvn10' not in alt: alt = (alt + '; ' if alt else '') + f'lvn10 A4:{A} B4:{B}'
        log.append([r['line'], r['position'], r['sign'] if act not in ('settled', 'confirmed') else r['sign'], r['confidence'], A, B, act or 'none'])
    pos += 1
    out.append([r['line'], str(pos), sign, conf, alt, why])
def tsv(rows, head):
    s = io.StringIO(); s.write('\t'.join(head) + '\n')
    for x in rows: s.write('\t'.join(x) + '\n')
    return s.getvalue()
outs = {os.path.join(T, 'ciphertext_4610.tsv'): tsv(out, cols),
        os.path.join(H, 'apply_log.tsv'): tsv(log, ['line', 'pre_pos', 'pre_sign', 'pre_conf', 'A4', 'B4', 'action'])}
print('control A4 %d/%d, B4 %d/%d, gate %s' % (*ctl['A4'], *ctl['B4'], 'PASS' if gate else 'FAIL'))
stale = False
for p, s in outs.items():
    if '--check' in sys.argv:
        if not os.path.exists(p) or open(p).read() != s: print('STALE:', p); stale = True
    else: open(p, 'w').write(s)
from collections import Counter
print(Counter(x[-1] for x in log))
sys.exit(1 if stale else 0)
