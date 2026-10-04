#!/usr/bin/env python3
"""VIV54-A1 (verifier, 4 Oct 2026): position-null control for PREREG-N5VIV54 gate (a).

The PREREG's shuffled-KEY null changes letter frequencies as well as positions, so it cannot tell "the decode matches
the gloss at that spot" from "the true key yields French-frequency letters anywhere". This control keeps the TRUE key
and moves each gloss's window to a random other line and offset of the same token width (rule 3: the control must be
able to vary on the axis under test, here position). Also reports window lengths.

    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv54_audit_posnull.py
"""
import math, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(HERE))), 'tools'))
import viv54_decode as vd  # noqa: E402
from viv54_test import lcs, fold  # noqa: E402

k = {c: v for c, (v, g) in vd.key().items()}
lines = []
for page in ('f173r', 'f173v'):
    for line, seq in sorted(vd.page_tokens(page).items()):
        lines.append((page, line, [c for c, _ in seq]))
bykey = {(p, l): s for p, l, s in lines}
gl = [ln.rstrip('\n').split('\t') for ln in open(os.path.join(HERE, 'glosses54.tsv'), encoding='utf-8')][1:]
gl = [g for g in gl if g[6] == 'yes']
dec = lambda seq: fold(''.join(k.get(c, '') for c in seq))
real, widths = [], []
for p, l, x0, x1, _, g, *_ in gl:
    seq = bykey[(p, l)]; n = len(seq)
    a, b = max(0, math.floor((float(x0) - 0.08) * n)), min(n, math.ceil((float(x1) + 0.08) * n))
    w = dec(seq[a:b]); widths.append(b - a)
    real.append(lcs(fold(g), w) / len(g))
    print(f"{p} {l} gloss={g!r} len_g={len(g)} window_tokens={b-a} window_letters={len(w)} score={real[-1]:.3f} window={w}")
S = sum(real) / len(real)
rng = random.Random(20261004)
null = []
for _ in range(1000):
    sc = []
    for (p, l, x0, x1, _, g, *_), wd in zip(gl, widths):
        while True:
            pp, ll, seq = rng.choice(lines)
            if (pp, ll) != (p, l) and len(seq) >= wd:
                break
        a = rng.randint(0, len(seq) - wd)
        sc.append(lcs(fold(g), dec(seq[a:a + wd])) / len(g))
    null.append(sum(sc) / len(sc))
null.sort()
p95 = null[949]; med = null[499]
pval = sum(1 for x in null if x >= S) / len(null)
print(f"S_a(real)={S:.3f}  position-null (true key, other line/offset, 1000 draws): median={med:.3f} p95={p95:.3f} max={null[-1]:.3f} p={pval:.3f}")
