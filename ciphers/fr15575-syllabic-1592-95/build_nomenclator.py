#!/usr/bin/env python3
"""SYL-NOM (13 Oct 2026): build key_no54_nomenclator.tsv from the two blind passes (nomen_passA.tsv, nomen_passB.tsv) and
the reconciler's eye settlements below (made on the native crops images/fr3995/nomen/ and the column views cut from
images/fr3995/src_image_v3_..._f188_250_1600_3650_4455.jpg). Grade H = both passes agree on entry and code (case, a
trailing '+' written in the code vs as a mark, and mark wording normalised) and the reconciler saw nothing against it;
M = settled by the reconciler from the image (pass split, or a shared misread), or letter identity unsure.
  python3 build_nomenclator.py [--check]   (--check: exit 1 if the committed TSV differs from a rebuild)
"""
import csv, sys, os
H = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(H, 'key_no54_nomenclator.tsv')
# (crop,row): (entry, code, marks, grade, note)
S = {
 ('nomc1_L01',2): ('aunque','zo','', 'M','first letter the 3-shaped z of this hand (as in zur, zim); B read 30'),
 ('nomc1_L01',3): ('alli','dis','', 'M','final s with a long tail; A dir'),
 ('nomc1_L01',6): ('agora','bu','plus2-above','M','two crosses above (A read two dots)'),
 ('nomc1_L01',7): ('assi','so','', 'M','first sign S or 5 (B 50); same S as in sor, size'),
 ('nomc1_L01',10): ('autoridad','Ja','', 'M','first letter the looped J/d of jam, jol (A da)'),
 ('nomc1_L01',12): ('alguna','dee','', 'M','second e with a flourish (B dec)'),
 ('nomc1_L02',3): ('[struck]','fes','struck', 'M','entry and code struck through; entry unread (A ahi/fo, B aui?/fes); the next row auisa=fes is the replacement'),
 ('nomc1_L02',5): ('bien','87','plus-after', 'M','87 followed by a cross'),
 ('nomc1_L02',7): ('beneficio','?h','blot-before', 'M','a blotted sign before h'),
 ('nomc1_L02',10): ('Carta','pa','', 'M','marks unsure (A dot above)'),
 ('nomc1_L02',11): ('Caso','pe','tick-above', 'M','small tick above p'),
 ('nomc1_L03',3): ('cio','17','plus-after,dot1-above', 'M','dot above 1, cross after 7'),
 ('nomc1_L03',5): ('come','se','', 'M','first sign s or 8 (B 8e)'),
 ('nomc1_L03',6): ('cuenta','gals','', 'M','final s with a flourish (A galg)'),
 ('nomc1_L03',7): ('causa','gui','', 'M','small "fal" written at the column edge after gui, possibly a second code; not taken as code'),
 ('nomc1_L03',9): ('carlos','gue','circumflex-above', 'M','entry carlos (A canalos)'),
 ('nomc1_L03',10): ('Comodita','ram','', 'M','faded entry'),
 ('nomc1_L04',1): ('dicho','hor ou lal','', 'M','"ou" underlined, the alternative "lal" stands at the head of column 2 (both passes missed it)'),
 ('nomc1_L04',4): ('despacho','zel','', 'M','entry despacho (passes despaus o / despaeso); z the 3-shaped z'),
 ('nomc1_L04',6): ('duque','pol','', 'M','o inked heavily; no mark'),
 ('nomc1_L05',5): ('diablo','22','flourish-after', 'M','A carried pul from duda above; 22 with a z-like tail'),
 ('nomc2_L01',5): ('fin','dam','', 'M','the dot is before the entry, not over the code'),
 ('nomc2_L01',8): ('fuerca','gim','', 'H','entry spelling only (fuerza/fuerca)'),
 ('nomc2_L01',9): ('franceses','fum','plus-after,circumflex-above', 'H','mark notation only'),
 ('nomc2_L02',2): ('generale','hom','plus-after', 'H','mark notation only; the dot is on the rule'),
 ('nomc2_L02',3): ('grande','Jam','', 'M','looped J/z letter (A zam, B jam)'),
 ('nomc2_L02',4): ('gayeras','hem','other:7-like mark above right', 'M',''),
 ('nomc2_L02',5): ('Size','705','', 'M','third digit 5 or s (B 70s)'),
 ('nomc2_L02',7): ('Sizo','nom','other:z barred', 'M','second "Sizo" with a barred z (A Sito)'),
 ('nomc2_L02',10): ('heresia','nams','', 'M','last sign s or 6 (A nam6)'),
 ('nomc2_L03',6): ('despues','Jol','', 'M','looped J letter as in Jam (A sol)'),
 ('nomc3_L01',4): ('Mismo','gi','dot1-above', 'M','"gi" written small above "der" at the end of the Mismo line; Mismo/Marques/Muestra share these two codes and one more der, so which entry has gi is unsure (A der, B ger)'),
 ('nomc3_L01',5): ('Marques','der','', 'M','Marques written small between Mismo and Muestra; its code not separately visible'),
 ('nomc3_L01',9): ('mucho','sur','', 'M','first sign s, 5 or b (B bur)'),
 ('nomc3_L02',5): ('necessitados','nir','plus-after,circumflex-above', 'H','mark notation only'),
 ('nomc3_L02',9): ('nuemo','pers','', 'H','entry spelling only'),
 ('nomc3_L02',10): ('nuestra','pirs','tick-above-left', 'M','r written like v (B pius)'),
 ('nomc3_L03',7): ('podra','24','other:f-like sign above,comma-after', 'M',''),
 ('nomc3_L03',8): ('personas','cos','tick-above', 'M','acute tick over s'),
 ('nomc3_L03',9): ('platicas','dis','', 'H','entry spelling only'),
 ('nomc3_L03',12): ('porque','fos','', 'M','f or long s (A sos); same letter as far, fem'),
 ('nomc3_L04',6): ('proposito','Jis','', 'M','looped J letter (A zis, B js)'),
 ('nomc4_L01',7): ('razon','pos','dot1-above', 'M','dot above o on the first razon'),
 ('nomc4_L01',9): ('razon','pos','', 'M','second razon; no dot seen'),
 ('nomc4_L01',10): ('religion','rus','', 'M','first letter a descending stroke (A us)'),
 ('nomc4_L02',2): ('S.mag.','so ou so','T-below(first),dot3-above(second)', 'M','first sign S, 5 or z in both codes (A zo ou 30, B zo ou zo); o raised on the first'),
 ('nomc4_L02',9): ('sennores','zus','plus-after,circumflex-above-right', 'M','the three dots below belong to 49 (S.S.d)'),
 ('nomc4_L03',1): ('tierra','63','dot3-before,T-below', 'M','B ??; A 02'),
 ('nomc4_L03',6): ('trauajo','65','T-below', 'M','second digit 5 (A 69); entry trauajo/tranalo'),
 ('nomc4_L03',8): ('trauajo','pul','flourish-after', 'M','second trauajo entry'),
 ('nomc4_L03',9): ('V.M.d','88','dot3-above', 'M','8s written as the looped 8 of 87e (A 8es)'),
 ('nomc4_L03',10): ('ue','0','plus-after', 'M','first sign 0 or a'),
 ('nomc4_L03',11): ('V.M.d','87e','dot3-above', 'H','entry spelling only'),
 ('nomc4_L03',12): ('voluntad','?6 et tim','T-below', 'M','first sign a looped symbol (A cf, B c6); second code tim (B tun)'),
 ('nomc4_L04',1): ('V.M.d','??','', 'M','a two-part looped symbol (A qf, B qp)'),
 ('nomc4_L04',3): ('vua','87e','', 'M','entry vua or via'),
 ('nomr_L01',1): ('Yglesia','gm','', 'H','entry spelling only'),
 ('nomr_L01',2): ('zia','706e','', 'M','z the 3-shaped z (B ?); third sign read 6 (both passes b): the 6 of this hand has a tall ascender, cf. 46e, s6'),
}
for r in range(1, 6):
    S.setdefault(('nomn_nulles', r), None)
NUL = {1: ('s', 'M', 'S or 5'), 2: ('8', 'H', ''), 3: ('9', 'H', ''), 4: ('0', 'H', ''), 5: ('25', 'M', '25 or 2s')}

def rows(p):
    d = {}
    for r in csv.DictReader(open(os.path.join(H, f'nomen_pass{p}.tsv')), delimiter='\t'):
        d[(r['crop'], int(r['row']))] = r
    return d
A, B = rows('A'), rows('B')
nc = lambda c: c.lower().replace(' ', '').rstrip('+')
out = []
for k in sorted(A):
    a, b = A[k], B[k]
    pa, pb = f"{a['entry']}={a['code']}[{a['marks']}]", f"{b['entry']}={b['code']}[{b['marks']}]"
    if k[0] == 'nomn_nulles':
        c, g, n = NUL[k[1]]
        out.append((f'{k[0]}:{k[1]}', 'NULLE', c, 'other:H-like mark above', g, pa, pb, 'reconciler' if g == 'M' else 'A=B+image', n)); continue
    if S.get(k):
        e, c, m, g, n = S[k]
        out.append((f'{k[0]}:{k[1]}', e, c, m, g, pa, pb, 'reconciler', n)); continue
    ok = a['entry'].lower() == b['entry'].lower() and nc(a['code']) == nc(b['code'])
    assert ok, k
    out.append((f'{k[0]}:{k[1]}', a['entry'], a['code'], a['marks'] if a['marks'] == b['marks'] else a['marks'] + ' | ' + b['marks'],
                'H' if a['marks'] == b['marks'] else 'M', pa, pb, 'A=B+image', '' if a['marks'] == b['marks'] else 'marks differ'))
hdr = ['# BnF fr.3995 no.54 nomenclator, f.96v-97r (Gallica/openapi ark btv1b525085665 canvas f188; native region 250,1600,3650,4455 + 3550,2450,1450,1500 + 5500,1800,1750,450). SYL-NOM, 13 Oct 2026.',
       '# Period key sheet (Tomokiyo: a partial reconstruction). Entry -> code as written. Grades: H both blind passes + reconciler agree; M settled by the reconciler or letter identity unsure. The French legend of marks (right of f.97r) is not transcribed.',
       'pos\tentry\tcode\tmarks\tconf\tpassA\tpassB\tsettled_by\tnote']
text = '\n'.join(hdr + ['\t'.join(r) for r in out]) + '\n'
if '--check' in sys.argv:
    sys.exit(0 if open(OUT).read() == text else 1)
open(OUT, 'w').write(text)
print(len(out), 'rows; H', sum(r[4] == 'H' for r in out), 'M', sum(r[4] == 'M' for r in out))
