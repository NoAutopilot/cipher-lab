#!/usr/bin/env python3
"""GAPS30-riksarkivet-r4282-1628 (3 Oct 2026): does the letter table of DECODE key record 4263 (Chifferklaver II:100,
cover "1650- Sternberg ...", heading "... und ...s Ziffern"; all reading M) fit R4282 on the signs the two share?
The table (IMG_R4263_I25581_P, read by eye at 200 dpi, grade M) gives each plain letter one 2-digit number and one
graphic sign, and a reverse number list whose single digits are 4 -> g, 6 -> o, 8 -> d (2 and 3 struck through).
STRICT: the three key signs whose shape matches an R4282 sign class without doubt (key m = open square = R4282 B;
key o = epsilon-like E = R4282 E; key c = x = R4282 x) plus R4282's digits 4 and 8, which the key's own number list
gives as single-digit homophones.  WIDE: STRICT plus four ambiguous pairings (R4282 L=lambda vs the key's h, an
inverted V; R4282 T=Delta vs the key's i, an inverted Delta; R4282 D, looped d, vs the key's x, a looped delta;
R4282 u vs the key's l, a U).  Same statistic and controls as key4327_overlap.py / key4275_overlap.py (rule 3):
mean la18 Latin unigram log-probability of the letters the key gives R4282's tokens of those signs, vs (a) the same
values permuted among the signs and (b) distinct random Latin letters, 2000 draws each.  --check re-derives and
compares with the committed key4263_overlap.json."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from key4275_overlap import test
from key4327_overlap import HERE
STRICT = {'B': 'm', 'E': 'o', 'x': 'c', '4': 'g', '8': 'd'}
WIDE = dict(STRICT, L='h', T='i', D='x', u='l')

def run():
    return {'strict': test(STRICT, 4263), 'wide': test(WIDE, 42631)}

if __name__ == '__main__':
    out = run(); j = HERE / 'key4263_overlap.json'
    if '--check' in sys.argv:
        ok = json.loads(j.read_text()) == out; print('OK' if ok else 'STALE'); sys.exit(0 if ok else 1)
    j.write_text(json.dumps(out, indent=1) + '\n'); print(json.dumps(out, indent=1))
