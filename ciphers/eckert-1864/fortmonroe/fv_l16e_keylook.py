#!/usr/bin/env python3
"""FV-L16e: look up every word of an entry's ciphertext block in key.md (Cipher No. 1 table rows '| Word | Meaning | grade | where |');
prints word -> meaning for exact and stem (-s, -er, -ing, -ed) matches, so plain/code collisions can be judged by eye. Usage: fv_l16e_keylook.py E447 [E...]"""
import re, sys
K = {}
for l in open('key.md'):
    m = re.match(r'\|\s*([A-Za-z][A-Za-z \'.-]*?)\s*\|\s*([^|]+?)\s*\|\s*([HCSMI])\s*\|\s*([^|]*)\|', l)
    if m: K.setdefault(m.group(1).lower(), []).append((m.group(2), m.group(4).strip()))
t = open('ciphertext.txt').read()
for e in sys.argv[1:]:
    b = re.search(r'^### ' + e + r'\b[^\n]*\n(.*?)(?=^note:|^### )', t, re.S | re.M).group(1)
    print('==', e)
    for w in re.findall(r"[A-Za-z']+", b):
        lw = w.lower(); hit = K.get(lw)
        how = 'exact'
        if not hit:
            for suf in ('s', 'er', 'ing', 'ed', 'es'):
                if lw.endswith(suf) and K.get(lw[:-len(suf)]): hit = K[lw[:-len(suf)]]; how = '-' + suf; break
        if hit: print(f'  {w:14s} {how:6s} ' + ' ; '.join(f'{a} ({b})' for a, b in hit[:3]))
