"""NEAR3-C1TX-c187L (4 Oct 2026): apply the reconciler's settlements (read from the crops) to
tx/c187L_rec/ciphertext_draft.tsv and write tx/c187L_rec.tsv (wide 'row<TAB>codes', as tx/c185R_rec.tsv) and
tx/c187L_rec_long.tsv (line pos sign conf note). Conventions: NEW:5hook = s (the 's z' pair of c185R), NEW:v-bar = vdash,
NEW:triangle = tri (c185R labels already in key.tsv); '0' -> 'o' as in ciphertext.tsv; arc-hooked 2 = '2' (labels_v2).
Grades: agreed sign keeps the draft confidence; a settled split is H when seen clearly on the crop, else M."""
import csv, sys
D = {  # (line, col): (sign or '' to drop, conf, why)
 ('L02',31):('s','H','5hook=s'), ('L04',5):('y','M','eye'), ('L04',9):('d','H','eye'),
 ('L04',21):('PLAIN:?ugte','M','clear word'), ('L05',10):('o','H','0=o'), ('L05',18):('vdash','H','eye'),
 ('L05',23):('','H','no o on crop'), ('L06',7):('s','H','5hook=s'), ('L06',15):('K','M','eye'),
 ('L06',24):('sd','M','eye, unsure'), ('L07',1):('L','H','eye'), ('L07',14):('c','M','raised'),
 ('L07',15):('2','M','eye'), ('L08',1):('PLAIN:Cet','M','clear'), ('L08',3):('PLAIN:Dandre?','M','clear'),
 ('L08',4):('','M','clear word merged'), ('L08',5):('PLAIN:fermeu?','M','clear'), ('L09',14):('th','H','eye'),
 ('L09',26):('','H','no + on crop'), ('L10',19):('2','H','arc-2'), ('L10',23):('2','H','arc-2'),
 ('L11',1):('s','H','5hook=s'), ('L11',21):('sd','M','not viewed closely, A'), ('L11',23):('rot','M','not viewed closely, A'),
 ('L12',11):('e','H','eye'), ('L12',21):('','H','6r one sign'), ('L12',22):('6r','H','6r one sign'),
 ('L13',7):('o','H','0=o'), ('L13',15):('sd','M','eye'), ('L13',27):('dia','M','eye'), ('L14',16):('e','M','c/e: e in every viewed case but L07'),
 ('L15',11):('2','M','arc-2'), ('L15',13):('+','M','not viewed, A'), ('L15',28):('a','M','not viewed, A'),
 ('L16',7):('','H','p drawn with crossbar, one sign'), ('L16',18):('','H','p drawn with crossbar'), ('L16',24):('+','M','cross over ls'),
 ('L16',28):('s','H','5hook=s'), ('L16',30):('','H','6r one sign'), ('L16',31):('6r','H','6r one sign'),
 ('L17',11):('q','M','not viewed, A'), ('L18',8):('s','H','5hook=s'), ('L19',5):('vdash','H','v-bar=vdash'),
 ('L19',19):('2','H','arc-2'), ('L19',20):('e','H','eye'), ('L19',27):('th','H','eye'), ('L20',10):('2','M','arc-2'),
 ('L20',13):('l','M','eye (L26 same)'), ('L21',11):('vdash','H','eye'), ('L21',21):('e','H','eye'), ('L21',22):('qb','H','eye'),
 ('L21',27):('e','H','eye'), ('L22',7):('o','H','0=o'), ('L22',24):('s','H','5hook=s'), ('L23',5):('2','M','arc before 2'),
 ('L23',10):('6','M','6y shape, not the 6z of 6r'), ('L23',11):('7','M','eye'), ('L23',12):('th','M','eye'),
 ('L23',25):('f','M','looped f'), ('L23',28):('','H','6r one sign'), ('L23',29):('6r','H','6r one sign'),
 ('L24',9):('NEW1','M','open arc, see NOTES'), ('L24',11):('th','M','A only'), ('L24',16):('e','H','eye'),
 ('L24',21):('vdash','H','eye'), ('L25',10):('2','H','arc-2'), ('L25',18):('iii','M','eye'), ('L26',13):('l','H','eye'),
 ('L27',15):('w','H','eye'),
}
NORM = {'NEW:5hook':'s','NEW:v-bar':'vdash','NEW:triangle':'tri','0':'o','sqc?':'sqc'}
rows = list(csv.DictReader(open('tx/c187L_rec/ciphertext_draft.tsv'), delimiter='\t'))
out = {}; used = set()
for r in rows:
    k = (r['line'], int(r['position']))
    if k in D:
        s, c, why = D[k]; used.add(k)
    else:
        if r['why'] not in ('agree', 'agree-flagged'):
            sys.exit('unsettled %s %s' % k)
        s, c, why = r['sign'].rstrip('?'), r['confidence'], r['why']
    s = NORM.get(s, s)
    if s:
        out.setdefault(r['line'], []).append((s, c, why))
missing = set(D) - used
if missing: sys.exit('decisions not used: %s' % sorted(missing))
with open('tx/c187L_rec.tsv', 'w') as f:
    f.write('row\tcodes\n')
    for L in sorted(out): f.write('%s\t%s\n' % (L, ' '.join(s for s, _, _ in out[L])))
with open('tx/c187L_rec_long.tsv', 'w') as f:
    f.write('line\tpos\tsign\tconf\tnote\n')
    for L in sorted(out):
        for i, (s, c, why) in enumerate(out[L], 1): f.write('c187L_%s\t%d\t%s\t%s\t%s\n' % (L, i, s, c, why))
n = sum(len(v) for v in out.values()); nc = sum(1 for v in out.values() for s, _, _ in v if not s.startswith('PLAIN:'))
print('lines', len(out), 'tokens', n, 'cipher signs', nc, 'settled', len(D))
