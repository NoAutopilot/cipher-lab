#!/usr/bin/env python3
"""BRO-123 (9 Oct 2026): reconciled body run m0253-m0254 = blind pass A + the reconciler's settlements from the crops
(images/crops_m0253_b123, crops_m0254_b123). Writes body123_ciphertext.tsv. `--check` exits 1 if the file is stale.
Settlements (bro123/disagreements.tsv, uncertain.tsv; reconciler read the crops, 9 Oct 2026):"""
import csv, sys
from pathlib import Path
H = Path(__file__).resolve().parent.parent
# (line, pos in pass A) -> list of replacement (token, conf, note); [] deletes
EDITS = {
 ('m0253_L01-1', '1'): [('Z', 'M', 'decorated paragraph initial (Z/barred shape), kept as its own unkeyed token')],
 ('m0253_L01-1', '2'): [('f', 'M', 'long stroke after the initial; A y, B none; reconciler: long-s f')],
 ('m0253_L05-1', '4'): [('x', 'H', 'A x? B 7; crop shows x.z')],
 ('m0253_L05-4', '1'): [],
 ('m0253_L05-4', '2'): [],
 ('m0253_L06-1', '1'): [('8', 'M', 'line start 8.18 split across crops L05/L06 (both passes); full leaf reads 8.18.24'),
                        ('18', 'M', 'see previous')],
 ('m0253_L06-3', '1'): [('Z', 'M', 'decorated paragraph initial')],
 ('m0253_L06-3', '13'): [('g', 'M', 'A g, B q')],
 ('m0253_L07-1', '24'): [('552', 'M', 'A 52, B 552?; no dot visible between 55 and 2')],
 ('m0253_L07-3', '5'): [('w:e', 'M', 'clear word')],
 ('m0253_L07-3', '6'): [('w:const', 'M', 'clear word as written (A consta, B const + a)'), ('a', 'M', 'B: separate a after const')],
 ('m0253_L08-1', '7'): [('55', 'M', 'A 55, B 11: same glyph as the agreed 55s on L01; 55 and 11 are both p in key.tsv')],
 ('m0253_L08-3', '15'): [('55', 'M', 'A 55, B 11 (as above)')],
 ('m0253_L10-2', '9'): [('12', 'M', 'A 52, B 12; both r in key.tsv')],
 ('m0253_L11-2', '13'): [('w:he', 'H', 'clear: he para entender')],
 ('m0254_L01-3', '1'): [('Z', 'M', 'decorated paragraph initial')],
 ('m0254_L02-3', '3'): [('x', 'H', 'A 7, B x; crop shows x')],
 ('m0254_L02-3', '14'): [('x', 'M', 'struck-through sign (bold x over a sign); A 7, B x?')],
 ('m0254_L03-2', '12'): [('ff', 'M', 'A ff, B f; doubled loop')],
}
def build():
    rows = []
    with open(H / 'bro123' / 'passA.tsv') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            k = (r['line'], r['pos'])
            if k in EDITS:
                for t, c, n in EDITS[k]:
                    rows.append((r['line'], t, c, n))
            else:
                t = r['token'].rstrip('?').replace('^', '')
                if t in ('o', '0'):
                    t = '0'
                rows.append((r['line'], t, r['conf'] if not r['token'].endswith('?') else 'M', 'mark ^ dropped' if '^' in r['token'] else ''))
    out = ['line\tpos\ttoken\tconf\tnote']
    last, p = None, 0
    for line, t, c, n in rows:
        p = p + 1 if line == last else 1
        last = line
        out.append(f'{line}\t{p}\t{t}\t{c}\t{n}')
    return '\n'.join(out) + '\n'
txt = build()
o = H / 'body123_ciphertext.tsv'
if '--check' in sys.argv:
    ok = o.exists() and o.read_text() == txt
    print('body123_ciphertext.tsv', 'OK' if ok else 'STALE'); sys.exit(0 if ok else 1)
o.write_text(txt); print('wrote', o, txt.count('\n') - 1, 'tokens')
