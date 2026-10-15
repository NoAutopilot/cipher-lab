#!/usr/bin/env python3
"""LVN-4611 (15 Oct 2026): score the blind per-token read of WVO 4611 per unit (lvn4611/reads_<unit>.tsv, Sonnet calls) against
lvn4611/key_<unit>.tsv under lvn4611/PREREG-LVN-4611.md -- per-unit control gate >= 8/10 exact; then a target settles when the read
equals A150 or B150 exactly (no '?'), H only when the value is a key_full.tsv code (else M kept). Targets not placed (not in reads;
the placement note's rows) stay M with action 'not-read'. Writes lvn4611/settle_<unit>.tsv, which ../settle.py applies last for 4611
(only when the unit's gate passed: a FAIL unit gets no settled/confirmed rows). Units p1, p3 (LVN-4611/LVN-PIN) and p2a, p2b (LVN-4611P2,
addendum LVN-4611P2: same rule, rows placed on deskewed physical lines). --check: exit 1 if any settle file is stale (rule 7)."""
import csv, io, os, sys
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
rd = lambda p: list(csv.DictReader(open(p), delimiter='\t'))
codes = {r['code'] for r in rd(os.path.join(T, 'key_full.tsv'))}
stale = False
for unit in ('p1', 'p3', 'p2a', 'p2b'):
    rp = os.path.join(H, 'reads_%s.tsv' % unit)
    if not os.path.exists(rp): continue
    key = rd(os.path.join(H, 'key_%s.tsv' % unit)); rs = {r['tid']: r['read'] for r in rd(rp)}
    ctl = [rs.get(k['tid']) == k['sign'] for k in key if k['role'] == 'control']
    gate = sum(ctl) >= 8
    print('%s control %d/%d, gate %s' % (unit, sum(ctl), len(ctl), 'PASS' if gate else 'FAIL'))
    rows = []
    for k in sorted((k for k in key if k['role'] == 'target'), key=lambda k: (k['line'], int(k['position']))):
        rd_ = rs.get(k['tid'], '-'); ok = gate and k['tid'] in rs and '?' not in rd_ and rd_ in (k['A150'], k['B150'])
        conf = ('H' if rd_ in codes else 'M') if ok else 'M'
        act = ('settled' if rd_ != k['sign'] else 'confirmed') if ok and conf == 'H' else ('read-confirmed-not-key-code' if ok else ('stays' if k['tid'] in rs else 'not-read'))
        rows.append([k['line'], k['position'], k['sign'], rd_ if ok else k['sign'], conf, act,
                     f"lvn4611 per-token 300-dpi read {rd_} (A150 {k['A150']}, B150 {k['B150']}; {k['tid']}; {unit} control {sum(ctl)}/10)"])
    s = io.StringIO(); s.write('line\tpre_pos\told\tnew\tconfidence\taction\tnote\n')
    for r in rows: s.write('\t'.join(r) + '\n')
    p = os.path.join(H, 'settle_%s.tsv' % unit)
    if '--check' in sys.argv:
        if not os.path.exists(p) or open(p).read() != s.getvalue(): print('STALE', p); stale = True
    else:
        open(p, 'w').write(s.getvalue())
        from collections import Counter; print(Counter(r[5] for r in rows))
if '--check' in sys.argv: print('STALE' if stale else 'up to date')
sys.exit(1 if stale else 0)
