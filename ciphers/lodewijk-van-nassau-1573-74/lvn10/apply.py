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
# --round b (R13-LVN10B, 6 Oct 2026, lvn10/PREREG_B.md): passes A5/B5, aligned_b.tsv -> apply_log_b.tsv, tag lvn10b.
# After a round-b apply, round b is the canonical rebuild of ciphertext_4610.tsv (round a's gate failed, it changed nothing).
RB = '--round' in sys.argv and sys.argv[sys.argv.index('--round') + 1] == 'b'
PA, PB, ALN, LOG, TAG = ('A5', 'B5', 'aligned_b.tsv', 'apply_log_b.tsv', 'lvn10b') if RB else ('A4', 'B4', 'aligned.tsv', 'apply_log.tsv', 'lvn10')
# --round c (R14-LVN10C, 6 Oct 2026, lvn10/PREREG_C.md): per-token crop reads A6/B6, aligned_c.tsv -> apply_log_c.tsv, tag lvn10c.
if '--round' in sys.argv and sys.argv[sys.argv.index('--round') + 1] == 'c': PA, PB, ALN, LOG, TAG = 'A6', 'B6', 'aligned_c.tsv', 'apply_log_c.tsv', 'lvn10c'
# --round d (R14-LVN10D, 6 Oct 2026, lvn10/PREREG_D.md): repaired per-token crops, reads A7/B7, aligned_d.tsv -> apply_log_d.tsv, tag lvn10d.
if '--round' in sys.argv and sys.argv[sys.argv.index('--round') + 1] == 'd': PA, PB, ALN, LOG, TAG = 'A7', 'B7', 'aligned_d.tsv', 'apply_log_d.tsv', 'lvn10d'
pre = rd(os.path.join(H, 'ciphertext_4610_pre.tsv'))
# R15-LVNAPP (6 Oct 2026): the 10 control values R14-LVNEYE and R15-LVNCTL both found wrong on the 300-dpi image
# (lvn10/corrections_lvnctl.tsv, grades S/M per R15-LVNCTL), applied in every round after any settle. The control
# gates above still score the uncorrected aligned_*.tsv control column; this does not re-score any round as a licence.
post = {(r['line'], r['pre_pos']): r for r in rd(os.path.join(H, 'corrections_lvnctl.tsv'))}
al = {(r['line'], r['position']): r for r in rd(os.path.join(H, ALN))}
ctl = {PA: [0, 0], PB: [0, 0]}
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
        A, B = a[PA], a[PB]
        clean = A == B and '?' not in A and '~' not in A and A != '-'
        if conf != 'H':
            if clean:
                act = 'settled' if A != sign else 'confirmed'
                alt = f'was {sign} {conf}' + (f'; {alt}' if alt else '')
                sign, conf, why = A, 'H', f'image300 {TAG} ({PA}={PB}={A}; pre pos {r["position"]})'
            else:
                act = 'stays'
                alt = (alt + '; ' if alt else '') + f'{TAG} {PA}:{A} {PB}:{B}'
        if '/' in sign:
            if clean and A == sign:
                parts = sign.split('/')
                for j, p in enumerate(parts):
                    pos += 1
                    out.append([r['line'], str(pos), p, conf, '', f'split {TAG} from pre pos {r["position"]} ({sign}), part {j + 1}/{len(parts)}; image300 {PA}={PB}'])
                log.append([r['line'], r['position'], r['sign'], r['confidence'], A, B, (act + '+' if act else '') + 'split'])
                continue
            act = act or 'slash-kept'
            if TAG not in alt: alt = (alt + '; ' if alt else '') + f'{TAG} {PA}:{A} {PB}:{B}'
        log.append([r['line'], r['position'], r['sign'] if act not in ('settled', 'confirmed') else r['sign'], r['confidence'], A, B, act or 'none'])
    c = post.get((r['line'], r['position']))
    if c:
        assert sign == c['old'], (r['line'], r['position'], sign, c['old'])
        alt = f'was {sign} {conf}' + (f'; {alt}' if alt else '')
        sign, conf, why = c['new'], c['confidence'], c['note'] + f' (pre pos {r["position"]})'
        log.append([r['line'], r['position'], c['old'], r['confidence'], '', '', 'lvnctl-corrected'])
    pos += 1
    out.append([r['line'], str(pos), sign, conf, alt, why])
def tsv(rows, head):
    s = io.StringIO(); s.write('\t'.join(head) + '\n')
    for x in rows: s.write('\t'.join(x) + '\n')
    return s.getvalue()
outs = {os.path.join(T, 'ciphertext_4610.tsv'): tsv(out, cols),
        os.path.join(H, LOG): tsv(log, ['line', 'pre_pos', 'pre_sign', 'pre_conf', PA, PB, 'action'])}
print('control %s %d/%d, %s %d/%d, gate %s' % (PA, *ctl[PA], PB, *ctl[PB], 'PASS' if gate else 'FAIL'))
stale = False
for p, s in outs.items():
    if '--check' in sys.argv:
        if not os.path.exists(p) or open(p).read() != s: print('STALE:', p); stale = True
    else: open(p, 'w').write(s)
from collections import Counter
print(Counter(x[-1] for x in log))
sys.exit(1 if stale else 0)
