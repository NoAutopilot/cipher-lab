#!/usr/bin/env python3
"""Decode ciphertext.txt with WE028 (tools/data/uscodes-1800/WE028.tsv) and grade each token; rule 7.
usage: python3 ciphers/erving-monroe-1806/decode.py [--check]   (--check exits 1 if reading.txt is stale)
Grades: H = both blind passes agree and the value is read straight from WE028, a key source (Tomokiyo's transcription of
the period table, graded H in tools/data/uscodes-1800/README.md; the same key is attested on this Erving-Monroe channel by
the period interlinear of Erving to Monroe, 5 Feb 1806, 12 values agreeing) -- regraded from S by KHF-1, 7 Oct 2026; M = a group one pass marked doubtful or
read at a crop edge; I = a group neither pass read (braced in ciphertext.txt)."""
import sys, csv
from pathlib import Path
here = Path(__file__).resolve().parent
root = here.parents[1]
key = {}
for r in csv.DictReader(open(root / 'tools/data/uscodes-1800/WE028.tsv'), delimiter='\t', quoting=csv.QUOTE_NONE):
    key[r['value']] = r['plaintext']
DOUBT = {('L02', 2), ('L03', 6), ('L05', 6), ('L04', 2)}  # (line, index) a pass marked '?'; L04 idx 2 = crop-edge 146
out = []
for ln in open(here / 'ciphertext.txt'):
    if ln.startswith('#') or not ln.strip():
        continue
    lid, groups = ln.rstrip('\n').split('\t')
    toks = []
    for i, g in enumerate(groups.split()):
        inferred = g.startswith('{')
        v = g.strip('{}')
        grade = 'I' if inferred else ('M' if (lid, i) in DOUBT else 'H')
        toks.append(f"{v}={key.get(v, '?')}/{grade}")
    out.append(f"{lid}\t" + ' '.join(toks))
words = ' | '.join(''.join(t.split('=')[1].split('/')[0] for t in l.split('\t')[1].split()) for l in out)
text = '\n'.join(out) + '\n# joined: ' + words + '\n'
grades = [t.rsplit('/', 1)[1] for l in out for t in l.split('\t')[1].split()]
text += '# grades: ' + ' '.join(f"{g}={grades.count(g)}" for g in 'HCSMI') + f" of {len(grades)}\n"
letters = words.replace(' | ', '\n') + '\n'  # code-only letter stream, the judge's input
files = {here / 'reading.txt': text, here / 'reading_letters.txt': letters}
if '--check' in sys.argv:
    stale = [f.name for f, t in files.items() if not f.exists() or f.read_text() != t]
    if stale:
        print('STALE:', ' '.join(stale)); sys.exit(1)
    print('reading.txt, reading_letters.txt current'); sys.exit(0)
for f, t in files.items(): f.write_text(t)
print(text, end='')
