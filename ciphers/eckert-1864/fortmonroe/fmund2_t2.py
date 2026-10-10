#!/usr/bin/env python3
"""FM-UND2: 5658/0 telegram 2 under No. 1 and four meaning-shuffled copies (seeds 1,2,3,7) -> fmund2_t2.out. Run from fortmonroe/."""
import sys, random
from pathlib import Path
sys.path.insert(0, '..'); import decode
key = decode.load_key(Path('../key.md'))
def sh(seed):
    rows = [k for k, v in key.items() if v[2] == "word"]; m = [key[k] for k in rows]; random.Random(seed).shuffle(m); o = dict(key); o.update(zip(rows, m)); return o
for h, lines in decode.load_ciphertext(Path('fmund2_entries.txt')):
    if not h.startswith('T2'): continue
    text = decode.entry_text(lines)
    for n, k in [('no1', key)] + [(f'shuf{s}', sh(s)) for s in (1, 2, 3, 7)]:
        r, c = decode.decode_entry(text, k); print('==', n, c); print(r.replace('\n', ' '))
