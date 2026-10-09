#!/usr/bin/env python3
"""AUD2-LEDGER-23 (9 Oct 2026): second-audit search for E302 (Sheldon to Eckert, Fort Monroe, 27 May 1864) in IA djvu texts given as argv
(fetched once to scratch, not committed): OR I/36 pt 3 `warofrebellion363unit`, Plum 1882 `militarytelegraph01plumrich`, `...02plumrich`.
(a) letters-only phrase grep; (b) every 'Sheldon' window in each volume, with 'Gloucester'/'Mattapony'/'White House'/'poles'/'wire' flags.
A miss is a search result (rule 10)."""
import re, sys, os
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = ['base of supplies', 'chestnut poles', 'not rotted down', 'very little wire', 'Gloucester Point, thence by a direct road',
      'from West Point to White House', 'pretty secure', 'raiders', 'old line was all destroyed', 'whole line of the Chickahominy',
      'office at Gloucester', 'asked O\'Brien', 'cross to West Point', 'Glo\'ster']
FL = ['gloucester', 'gloster', 'mattapony', 'white house', 'poles', 'wire', 'west point', 'yorktown', 'chickahominy']
for p in sys.argv[1:]:
    t = open(p, errors='ignore').read(); v = os.path.basename(p)[:-4]
    idx = [i for i, c in enumerate(t) if c.isalpha()]; n = ''.join(t[i].lower() for i in idx)
    print('==', v, len(t))
    for ph in PH:
        ms = [idx[m.start()] for m in re.finditer(norm(ph), n)]
        print('  phrase', repr(ph), len(ms))
        for o in ms[:6]:
            print('     ', ' '.join(t[max(0, o - 200):o + 250].split()))
    for m in re.finditer(r'Sheldon', t):
        w = ' '.join(t[max(0, m.start() - 300):m.start() + 500].split()); f = [x for x in FL if x in w.lower()]
        if f:
            print('  SHELDON', m.start(), f, '|', w[:800])
