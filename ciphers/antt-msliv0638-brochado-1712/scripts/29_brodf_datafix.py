"""BRO-DF (9 Oct 2026, LANE FAMILY-A2l): image-backed corrections to the appendix transcription.

Reads each affected entry's token list from ciphertext_appendix.tsv, checks it equals the list as it
stood before this pass (so a second run is a no-op and a drifted file is refused), and writes the list
read from the leaf image (crops in images/crops_brodf/). Unchanged tokens keep their grade; inserted or
changed tokens are graded M (one eye, this pass). cipher_line in plaintext_appendix.tsv gets the same
edits, so _anchors.json (scripts 01-02) and ciphertext_appendix.tsv agree again.

  m0286 Carta 74: line 4 of 6 (e.g.t.p.y.5.d.4.x.19.5.15.m.f.26.20, "velhacos de consul") was missing
    from the master file and replaced by a duplicate of line 5 in cipher_line; line 2 lacks the 7 after
    'a' and the raised final 12 ("Monteleao por tirar").
  m0289 Carta 92: line 6 of 7 (c.h.11.15.26.5.25.x.7.c.g.m.p.d.14.y.5.17, "hum pouco de vinho na")
    missing from the master file; its 'z' is the hand's 7 (context 'de').
  m0281 Carta 15: idx10 'z±' is the hand's 7 (AX2-BRO5); 'por.z.19.b.' is plain 'por' + codes 7.19.b
    (absent from the master file); line 6 opens with the g± glyph, not 7, and its two crossed-t signs
    were transcribed 4 ("expresso pelo qual": both read l by context).
  m0290 Passage 2a idx81-82: 'g.9' is the doubled-loop 'ff' then the looped g-shaped sign (the 'bare 9');
    two blind Sonnet looks (BRO-DF) read idx82 as g / the same sign as a transcribed g, and idx81 as a long
    f-like stroke ('indisposicoes': ff=s, g=i).
  m0291 Carta 96: 'f.f' is one doubled-loop sign 'ff' (D4-BROC G2, D4V-BROC).
"""
import csv, sys
from difflib import SequenceMatcher

ROOT = '/home/user/cipher-lab/ciphers/antt-msliv0638-brochado-1712'

def toks(s):
    return s.split('.')

FIX = {
    ('m0286', 'Carta 74'): (
        toks('7.f.6.24.12.d.4±.26.19.15.y.12.a.23.h.d.m.a.20.19.17.18.55.15.12.3.g.12.y.22.15.5.17.f.8.g.18.18.23.24.4.a.7.f.a.y.12.7.18.17.12.24.f.15.15.4.3.y.5.d.h.25.5.23.f.a.7.20.10.17.m.15'),
        toks('7.f.6.24.12.d.4±.26.19.15.y.12.a.23.h.d.m.a.7.20.19.17.18.55.15.12.3.g.12.y.12.22.15.5.17.f.8.g.18.18.23.24.4.a.7.f.e.g.t.p.y.5.d.4.x.19.5.15.m.f.26.20.a.y.12.7.18.17.12.24.f.15.15.4.3.y.5.d.h.25.5.23.f.a.7.20.10.17.m.15')),
    ('m0289', 'Carta 92'): (
        toks('19.4.3.7.26.3.20.10.y.5.15.24.f.3.17.x.7.5.20.23.12.y.x.25.16.12.17.m.5.7.4.19.y±.26.18.x.24.f.a.19.4.x.22.y.f.g.17.14.3.23.m.x.d.7.h.5.y.y±.17.x.15.56±.x.25.5.21.a.g.4.f.7.10.c.18.h.22.20.11.y.18.2.7.55.12.17.26.15.8.f.4.19.f.5.15.18.16.21.19.5.23'),
        toks('19.4.3.7.26.3.20.10.y.5.15.24.f.3.17.x.7.5.20.23.12.y.x.25.16.12.17.m.5.7.4.19.y±.26.18.x.24.f.a.19.4.x.22.y.f.g.17.14.3.23.m.x.d.7.h.5.y.y±.17.x.15.56±.x.25.5.21.a.g.4.f.7.10.c.18.h.22.20.11.y.18.2.7.55.12.17.26.15.8.f.4.19.f.5.15.18.16.c.h.11.15.26.5.25.x.7.c.g.m.p.d.14.y.5.17.21.19.5.23')),
    ('m0281', 'Carta 15'): (
        toks('2.y.g±.18.15.c.a.13.c.z±.y.g±.y.8.m.10.y.18.m.2.15.c.7.y.6.7.15.b±.15.7.y.7.4±.7.7.8.6.15.7.10.e.18.y.5.y.7.a.y.5.15.18.b.7.8.18.z.m.a.15.4.y.18.y.m.2.y.c.y.7.7.4.15.6.7.4.15.13.c.y.4.7.c.6.15.28.y'),
        toks('2.y.g±.18.15.c.a.13.c.7.y.g±.y.8.m.10.y.18.m.2.15.c.7.y.6.7.15.b±.15.7.y.7.4±.7.7.8.6.15.7.10.e.18.y.5.y.7.a.y.5.15.18.b.7.8.18.z.m.a.15.4.y.18.y.m.2.y.c.y.7.19.b.g±.7.4.15.6.7.t.15.13.c.y.t.7.c.6.15.28.y')),
    ('m0290', 'Passage 2a'): (
        toks('13.26.19.5.c.7.20.h.y.25.c.d.f.24.26.11.2.55.15.x.7.12.8.y.18.19.4.3.17.12.14.24.f.7.a.19.h.11.d.16.15.12.y.2.25.4.26.m.x.2.15.c.2.25.19.8.14.g.f.a.7.12.22.25.14.19.c.26.m.x.d.y.f.8.14.2.22.4.55.15.g.9.5.d.7.f.x.17.10.8.24.23.4.26.22.15.20.2.m.5.8.y.f.x.d.4.h.g.m.22.4.a.12.25.4'),
        toks('13.26.19.5.c.7.20.h.y.25.c.d.f.24.26.11.2.55.15.x.7.12.8.y.18.19.4.3.17.12.14.24.f.7.a.19.h.11.d.16.15.12.y.2.25.4.26.m.x.2.15.c.2.25.19.8.14.g.f.a.7.12.22.25.14.19.c.26.m.x.d.y.f.8.14.2.22.4.55.15.ff.g.5.d.7.f.x.17.10.8.24.23.4.26.22.15.20.2.m.5.8.y.f.x.d.4.h.g.m.22.4.a.12.25.4')),
    ('m0291', 'Carta 96'): (
        toks('5.12.2.12.15.e.15.4.3.25.5.15.18.13.26.2.16.8.5.15.15.2.8.y.21.25.20.2.c.y.15.3.2.f.f.15.c.12.7.8.12.25'),
        toks('5.12.2.12.15.e.15.4.3.25.5.15.18.13.26.2.16.8.5.15.15.2.8.y.21.25.20.2.c.y.15.3.2.ff.15.c.12.7.8.12.25')),
}

LINE_FIX = {
    ('m0286', 'Carta 74'): [('d.m.a.20.19.17.18.55.15.12.3.g.12.y.', 'd.m.a.7.20.19.17.18.55.15.12.3.g.12.y.12.'),
                            ('a.y.12.7±.18.17.12.24.f.15.15.4.3.y.5.d.', 'e.g.t.p.y.5.d.4.x.19.5.15.m.f.26.20.')],
    ('m0289', 'Carta 92'): [('x.z.c.g', 'x.7.c.g')],
    ('m0281', 'Carta 15'): [('13.c.z±.y', '13.c.7.y'),
                            ('por.z.19.b. 7.7.4.15.6.7.4.15.13.c.y.4.7.c', 'por 7.19.b. g±.7.4.15.6.7.t.15.13.c.y.t.7.c')],
    ('m0290', 'Passage 2a'): [('55.15.g.9.5.d', '55.15.ff.g.5.d')],
    ('m0291', 'Carta 96'): [('2.f.f.15', '2.ff.15')],
}

ct_path = f'{ROOT}/ciphertext_appendix.tsv'
with open(ct_path, newline='', encoding='utf-8') as f:
    rd = csv.DictReader(f, delimiter='\t')
    fields = rd.fieldnames
    rows = list(rd)

out, changed = [], 0
i = 0
while i < len(rows):
    key = (rows[i]['leaf'], rows[i]['entry_label'])
    j = i
    while j < len(rows) and (rows[j]['leaf'], rows[j]['entry_label']) == key:
        j += 1
    block = rows[i:j]
    if key in FIX:
        old, new = FIX[key]
        cur = [r['token'] for r in block]
        if cur == new:
            out.extend(block)
        elif cur == old:
            sm = SequenceMatcher(a=old, b=new, autojunk=False)
            kept = {}
            for a0, b0, n in sm.get_matching_blocks():
                for k in range(n):
                    kept[b0 + k] = block[a0 + k]
            for p, t in enumerate(new):
                r = dict(kept[p]) if p in kept else {'leaf': key[0], 'entry_label': key[1], 'token_type': 'num' if t.rstrip('±').isdigit() else 'ltr', 'grade': 'M'}
                r['position'] = str(p + 1)
                r['token'] = t
                out.append(r)
            changed += 1
            print(f'{key}: {len(old)} -> {len(new)} tokens')
        else:
            sys.exit(f'{key}: token list matches neither the pre-fix nor the fixed list; refusing')
    else:
        out.extend(block)
    i = j

# a changed sign that SequenceMatcher pairs with an unchanged neighbour of the same name keeps that
# neighbour's grade; these positions were re-read this pass and are M (one eye + two blind looks)
FORCE_M = {('m0290', 'Passage 2a'): {'82'}}
for r in out:
    if r['position'] in FORCE_M.get((r['leaf'], r['entry_label']), ()):
        r['grade'] = 'M'
    if r['token_type'] == 'alpha':
        r['token_type'] = 'ltr'

with open(ct_path, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=fields, delimiter='\t', lineterminator='\n')
    w.writeheader()
    w.writerows(out)

pt_path = f'{ROOT}/plaintext_appendix.tsv'
with open(pt_path, newline='', encoding='utf-8') as f:
    rd = csv.DictReader(f, delimiter='\t')
    pfields = rd.fieldnames
    prows = list(rd)
for r in prows:
    key = (r['leaf'], r['entry_label'])
    for a, b in LINE_FIX.get(key, []):
        if a in r['cipher_line']:
            r['cipher_line'] = r['cipher_line'].replace(a, b, 1)
        elif b not in r['cipher_line']:
            sys.exit(f'{key}: cipher_line has neither {a!r} nor {b!r}')
with open(pt_path, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=pfields, delimiter='\t', lineterminator='\n')
    w.writeheader()
    w.writerows(prows)
print(f'{changed} entries changed in ciphertext_appendix.tsv')
