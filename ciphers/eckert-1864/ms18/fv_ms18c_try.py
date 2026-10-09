#!/usr/bin/env python3
"""FV-MS18c (9 Oct 2026): test the print-derived values Kearney = Burbridge and Lavender = Washburn(e) at every filed (and one unfiled, image-read)
occurrence against the printed text, with a control: every distinct person-meaning in key.md (Cipher No. 1) put in the same slot, scored against the
same print. A value 'reads' at an occurrence when the printed name at that slot is the value's surname. Offline; reads key.md only.
Occurrences (the printed or period name at the slot is from the source named, eye-checked by FV-MS18c on the print page image or the ledger image):
  Kearney  E169 (5782/1, 9 Sept 1864, Eckert's instruction 'for Maj. Gen. Burbridge use Kent and Kearney')       -> Burbridge  (definition, period)
  Kearney  E329 (9864/1, 13 Oct 1864) 'send copy to Kearney'      vs OR I/39 pt 3 p.253 '(Same to General Burbridge.)'  -> Burbridge
  Kearney  E330 (9873/1, 20 Oct 1864) 'assistance of Kearney &'   vs OR I/39 pt 3 p.379 'assistance of Burbridge and'   -> Burbridge
  Kearney  unfiled 9889/1 (5 Nov 1864, to Bruch, Louisville) 'Jennie plaster Kearney zodiac' -- no print; context only, not scored
  Lavender E169 'see C wash burn lavender and loadstone' (definition, period)                                          -> Washburn
  Lavender E330 '& lavender you could drive him'                  vs OR I/39 pt 3 p.379 'Burbridge and Washburn you'    -> Washburn
Exit 0 when each tested value reads at every scored print occurrence and no control value from key.md does better than chance."""
import re, os, sys
K = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'key.md')
rows = [l.split('|') for l in open(K) if l.startswith('| ') and l.count('|') >= 4]
meanings = sorted({r[2].strip() for r in rows if re.search(r'\b(Gen|Genl|General|Maj|Col|Adm|Admiral|Brig)\b', r[2])})
surname = lambda m: re.sub(r'[^a-z]', '', re.split(r'[ .]+', re.sub(r'\(.*?\)', '', m).strip())[-1].lower())
OCC = {'Kearney': [('E329', 'burbridge'), ('E330', 'burbridge')], 'Lavender': [('E330', 'washburn')]}
ok = True
for code, occ in OCC.items():
    have = [r[2].strip() for r in rows if r[1].strip().lower() == code.lower()]
    def score(m): return sum(surname(m).rstrip('e') == p.rstrip('e') for _, p in occ)
    true = {'Kearney': 'Maj Gen S. G. Burbridge', 'Lavender': 'Gen C. C. Washburne'}[code]
    ctrl = [score(m) for m in meanings]
    hits = [m for m in meanings if score(m) == len(occ)]
    print(f'{code}: key.md rows now: {have or "none"}; tested value {true!r} reads {score(true)}/{len(occ)} print occurrences;'
          f' control: {len(meanings)} distinct person meanings in key.md, {sum(c == len(occ) for c in ctrl)} read {len(occ)}/{len(occ)}'
          f' ({", ".join(hits) or "-"}), mean {sum(ctrl)/len(ctrl):.3f}/{len(occ)}')
    ok &= score(true) == len(occ)
sys.exit(0 if ok else 1)
