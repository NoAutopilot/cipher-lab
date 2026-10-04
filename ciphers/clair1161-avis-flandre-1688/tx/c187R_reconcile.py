"""NEAR3-C1TX-c187R (4 Oct 2026): apply the reconciler's settlements (read from the crops) to
tx/c187R_rec/ciphertext_draft.tsv and write tx/c187R_rec.tsv (wide 'row<TAB>codes', as tx/c185R_rec.tsv) and
tx/c187R_rec_long.tsv (line pos sign conf note). Same script shape as tx/c187L_reconcile.py. Conventions: '0' -> 'o' as in
ciphertext.tsv; crossed p = p (c187L); v-with-long-bar = vdash (c186L NEW1 / c187L); the small open square after wb = sqc;
the ornate crossed 'Rs' = K; the 'p8'-shaped crossed 8 = rot; the 'xe'/fish ligature (A: x e, B: K/rot) = NEW_c187R_2, one sign,
not forced; the flat bar with an ink blob (L04) = NEW_c187R_1; the L20 ink blot over one sign = NEW_c187R_blot (illegible).
Grades: agreed sign keeps the draft confidence; a settled split is H when seen clearly on the crop, else M."""
import csv, sys
D = {  # (line, col): (sign or '' to drop, conf, why)
 ('L01',3):('o','H','0=o'), ('L01',9):('p','H','crossed p'), ('L01',17):('o','H','0=o'),
 ('L02',11):('qb','H','eye'), ('L02',16):('','H','crossed p, one sign'),
 ('L03',14):('l','M','small looped l'), ('L03',28):('vdash','H','v-bar=vdash'),
 ('L04',1):('th','H','eye, A missed'), ('L04',8):('o','H','0=o'), ('L04',17):('iii','H','three strokes, barred'),
 ('L04',18):('K','M','ornate Rs'), ('L04',25):('NEW_c187R_1','M','flat bar with ink blob'),
 ('L05',11):('sqc','H','open square'), ('L05',23):('/','H','slash on crop'),
 ('L06',10):('rot','M','p8 shape'), ('L06',23):('sqc','H','open square'), ('L07',26):('tz','H','bar over 3-body'),
 ('L09',1):('','M','initial joined to word'), ('L09',2):('PLAIN:Juil','M','clear, large initial J'),
 ('L09',6):('ee','M','eye, unsure'), ('L09',13):('o','H','0=o'),
 ('L10',10):('th','M','theta with a dot above'), ('L11',9):('rot','M','p8 shape'), ('L11',28):('q','M','eye'),
 ('L12',1):('vdash','H','v-bar=vdash'), ('L12',9):('K','M','ornate Rs'), ('L12',11):('l','M','small looped l'),
 ('L12',20):('l','M','small looped l'), ('L13',1):('K','M','ornate Rs at line start'),
 ('L14',13):('sqc','H','open square'), ('L14',15):('p','H','eye'), ('L14',27):('K','M','ornate Rs'),
 ('L15',8):('sqc','M','open square, curved roof'), ('L15',28):('w','M','w with a dot'),
 ('L16',1):('l','M','small looped l'), ('L16',10):('e','M','small epsilon'),
 ('L17',5):('q','M','long descender'), ('L17',18):('PLAIN:toute','M','clear word'),
 ('L18',16):('K','M','ornate Rs'), ('L18',22):('eloop','M','same crossed loop as L12 eloop'), ('L18',28):('eloop','M','line-final loop'),
 ('L19',16):('','H','no + on crop'), ('L20',5):('NEW_c187R_blot','M','ink blot over one sign'), ('L20',6):('sqc','H','open square'),
 ('L20',26):('q','M','eye'), ('L21',15):('w','M','no bar seen'),
 ('L22',24):('NEW_c187R_2','M','xe ligature, one sign'), ('L22',25):('','M','part of the xe ligature'),
 ('L23',18):('sqc','H','open square'), ('L24',20):('eloop','M','large loop'), ('L24',24):('PLAIN:toute','M','clear word'),
 ('L25',8):('NEW_c187R_2','M','xe ligature, one sign'), ('L25',9):('','M','part of the xe ligature'),
 ('L26',6):('NEW_c187R_2','M','xe ligature, one sign'), ('L26',23):('z','H','barred z'),
 ('L26',26):('','M','clear word, see next'), ('L26',27):('PLAIN:monsr','M','clear abbreviation'),
}
NORM = {'0':'o'}
rows = list(csv.DictReader(open('tx/c187R_rec/ciphertext_draft.tsv'), delimiter='\t'))
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
with open('tx/c187R_rec.tsv', 'w') as f:
    f.write('row\tcodes\n')
    for L in sorted(out): f.write('%s\t%s\n' % (L, ' '.join(s for s, _, _ in out[L])))
with open('tx/c187R_rec_long.tsv', 'w') as f:
    f.write('line\tpos\tsign\tconf\tnote\n')
    for L in sorted(out):
        for i, (s, c, why) in enumerate(out[L], 1): f.write('c187R_%s\t%d\t%s\t%s\t%s\n' % (L, i, s, c, why))
n = sum(len(v) for v in out.values()); nc = sum(1 for v in out.values() for s, _, _ in v if not s.startswith('PLAIN:'))
print('lines', len(out), 'tokens', n, 'cipher signs', nc, 'settled', len(D))
