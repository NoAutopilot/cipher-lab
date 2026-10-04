"""NEAR3-C1TX-c188L (4 Oct 2026): apply the reconciler's settlements to tx/c188L_rec/ciphertext_draft.tsv
(reconcile_passes.py with tx/c188L_signmap.tsv) and write tx/c188L_rec.tsv (wide 'row<TAB>codes', as tx/c185R_rec.tsv)
and tx/c188L_rec_long.tsv (line pos sign conf note). Run from the target folder.

Settled from slope-following crops (3 segments per line, each cut on that line's own ink-profile track; the committed
images/c188L_L*_s1/s2 crops of the first cut were level and lost the right half of most lines -- see the report).
Conventions:
- A:tz / B:z on the barred z with a small raised loop on top (35 splits, every one A=tz B=z): settled 'z', grade M,
  the label the earlier leaves give this shape (c185R z 48 / tz 6; c187L z 48 / tz 1). Sorter question, not settled.
- iii vs iib: per occurrence by stroke count (3 strokes + bar = iii, 2 strokes + bar = iib); unviewed ones keep A, M.
- the raised epsilon-like hook before q (A f, B e/7): 'e' (labels_v2 epsilon; c187L's c/e convention), M where unclear.
- 's z' pair: s (5-hook) as c186L/c187L.  phi vs q (bowl with the stem through it): phi, M.
- NEW_c188L_1 = closed D-loop under a long arched over-bar (L01 x2, L19). NEW_c188L_2 = small caret ^ (L01, L17).
  NEW_c188L_3 = large open C enclosing a barred z (L05, L09, L11, L24; read eloop or tz or 'eloop z' by the passes;
  L09 and L11 share the run '7 7 a sqc 3 7 NEW_c188L_3 y 4 q th').
- L15/L16 line ends: both passes gave L16's end ('e wb S th w + a y th') to L15 and dropped L15's end; corrected
  from the crops (grade M, one reader: this worker)."""
import csv, sys
D = {  # (line, col): (sign or '' to drop, conf, why)
 ('L01',5):('NEW_c188L_1','M','arched-bar D'), ('L01',6):('e','M','raised hook, f/e'), ('L01',15):('2','M','arc-2 vs 7'),
 ('L01',19):('NEW_c188L_1','M','arched-bar D'), ('L01',22):('NEW_c188L_2','H','caret before a'),
 ('L02',2):('','H','y drawn a+y; no a'), ('L02',13):('iii','H','3 strokes'), ('L02',14):('e','H','raised epsilon'),
 ('L02',18):('phi','M','stem through bowl'),
 ('L03',12):('','M','K one sign'), ('L03',13):('qb','H','bar on descender'), ('L03',20):('eloop','H','eye'),
 ('L04',4):('tz','M','bar top, 3-body'), ('L04',8):('e','M','raised hook, f/e'), ('L04',10):('p','H','p with crossbar'),
 ('L04',29):('3','H','eye'),
 ('L05',2):('','H','no sign'), ('L05',3):('d','H','eye'), ('L05',4):('z','H','eye'), ('L05',12):('NEW_c188L_3','M','C enclosing z'),
 ('L05',15):('','H','no a'), ('L05',23):('dia','H','cross with blob'), ('L05',25):('','H','y drawn a+y'), ('L05',29):('phi','H','eye'),
 ('L06',4):('s','H','s z pair'), ('L06',5):('z','H','s z pair'), ('L06',9):('p','H','p with crossbar'), ('L06',13):('','H','no + on crop'),
 ('L07',20):('K','M','e-looped K, see L17'),
 ('L08',7):('z','M','eye'), ('L08',10):('th','M','no vertical stroke'), ('L08',13):('eloop','M','eye'), ('L08',16):('z','M','eye'),
 ('L08',21):('','H','p crossbar, not qb'), ('L08',22):('p','H','p with crossbar'), ('L08',23):('rot','M','8-loop sign'),
 ('L09',6):('th','M','no vertical stroke'), ('L09',13):('eloop','H','eye'), ('L09',20):('NEW_c188L_3','M','C enclosing z'),
 ('L09',21):('','H','z inside the C'), ('L09',26):('e','H','raised epsilon'),
 ('L10',5):('iii','M','not viewed, A'),
 ('L11',23):('NEW_c188L_3','M','C enclosing z'), ('L11',24):('','H','z inside the C'),
 ('L12',4):('iib','H','2 strokes'), ('L12',6):('6','M','6 then 7'), ('L12',14):('iib','H','2 strokes'),
 ('L12',19):('phi','M','stem through bowl'), ('L12',22):('iib','H','2 strokes'),
 ('L13',7):('+','M','t 8 3 as three signs'), ('L13',8):('8','M','eye'), ('L13',9):('3','M','eye'), ('L13',20):('s','H','s z pair'),
 ('L14',1):('2','M','arc-2 vs 7'), ('L14',7):('q','M','long descender'), ('L14',23):('phi','M','stem through bowl'),
 ('L15',9):('iii','H','3 strokes'),
 ('L16',7):('','H','one q, barred'), ('L16',9):('iii','H','3 strokes'), ('L16',18):('phi','M','stem through bowl'),
 ('L17',14):('NEW_c188L_2','H','caret'), ('L17',19):('K','M','K-e, see L03'), ('L17',24):('9','M','short tail'),
 ('L17',26):('','M','e-looped K one sign, see L07'), ('L17',27):('K','M','e-looped K'), ('L17',28):('iii','H','3 strokes'),
 ('L17',29):('f','M','plain f, not rc'),
 ('L18',1):('e','M','raised hook, f/7'),
 ('L19',10):('NEW_c188L_1','M','arched-bar D'), ('L19',14):('iib','H','2 strokes'),
 ('L20',23):('','H','no o on crop'), ('L20',26):('','H','descender of L19 ls'),
 ('L21',23):('s','H','s z pair'),
 ('L22',1):('qb','M','not viewed, A'), ('L22',19):('iii','H','3 strokes'),
 ('L23',17):('','H','no + on crop'), ('L23',23):('d','H','barred d'), ('L23',24):('sd','M','dotted i over blob'),
 ('L23',28):('iii','H','3 strokes'),
 ('L24',6):('NEW_c188L_3','M','C enclosing z'), ('L24',15):('s','H','s z pair'),
 ('L25',1):('vdash','H','v with long bar'), ('L25',25):('tri','H','filled triangle'),
 ('L27',1):('s','H','s z pair'), ('L27',4):('8','H','eye'), ('L27',14):('sd','M','dotted i'),
}
TAIL = {  # line: (keep positions up to and including, replacement tail) -- line-end reassignment, see docstring
 'L15': (17, ['iii', '7', '7', 'th', 'K', 'w', '+', 'S', '9']),
 'L16': (18, ['e', 'wb', 'S', 'th', 'w', '+', 'a', 'y', 'th']),
}
NORM = {'sqc?': 'sqc'}
rows = list(csv.DictReader(open('tx/c188L_rec/ciphertext_draft.tsv'), delimiter='\t'))
out = {}; used = set()
for r in rows:
    L, pos = r['line'], int(r['position'])
    if L in TAIL and pos > TAIL[L][0]:
        continue
    k = (L, pos)
    if k in D:
        s, c, why = D[k]; used.add(k)
    elif r['why'] == 'differ' and r['sign'] == 'tz' and r['alt'] == 'B:z':
        s, c, why = 'z', 'M', 'tz/z convention'
    elif r['why'] == 'gap' and L in ('L04', 'L18') and r['alt'] == 'A:-':
        s, c, why = r['sign'].rstrip('?'), 'M', 'B only (A cut short by the level crop); checked on slope crop'
    else:
        if r['why'] not in ('agree', 'agree-flagged'):
            sys.exit('unsettled %s %s' % k)
        s, c, why = r['sign'].rstrip('?'), r['confidence'], r['why']
    s = NORM.get(s, s)
    if s:
        out.setdefault(L, []).append((s, c, why))
for L, (_, tail) in TAIL.items():
    out[L] += [(s, 'M', 'line end from slope crop') for s in tail]
missing = set(D) - used
if missing: sys.exit('decisions not used: %s' % sorted(missing))
with open('tx/c188L_rec.tsv', 'w') as f:
    f.write('row\tcodes\n')
    for L in sorted(out): f.write('%s\t%s\n' % (L, ' '.join(s for s, _, _ in out[L])))
with open('tx/c188L_rec_long.tsv', 'w') as f:
    f.write('line\tpos\tsign\tconf\tnote\n')
    for L in sorted(out):
        for i, (s, c, why) in enumerate(out[L], 1): f.write('c188L_%s\t%d\t%s\t%s\t%s\n' % (L, i, s, c, why))
n = sum(len(v) for v in out.values()); nc = sum(1 for v in out.values() for s, _, _ in v if not s.startswith('PLAIN:'))
conf = {}
for v in out.values():
    for _, c, _ in v: conf[c] = conf.get(c, 0) + 1
print('lines', len(out), 'tokens', n, 'cipher signs', nc, 'settled', len(D), 'conf', conf)
