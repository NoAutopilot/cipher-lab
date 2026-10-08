#!/usr/bin/env python3
"""FAM-SUR729 crib score, per PREREG-FAM-SUR729.md. Exits 1 if score.out is stale (--check)."""
import csv, random, sys, os
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.join(H, '..', '..')
def lines(fn):
    d = {}
    for r in open(os.path.join(T, fn)):
        if r.startswith('#') or r.startswith('line\t'): continue
        p = r.rstrip('\n').split('\t')
        if len(p) < 3 or p[2].startswith('w:'): continue
        d.setdefault(p[0], []).append(p[2])
    return d
F = {f: lines(f) for f in ['ciphertext_2046_legend.tsv', 'ciphertext_2077_legend.tsv', 'ciphertext_2039_legend.tsv',
                           'ciphertext_2039_remarque.tsv', 'ciphertext_2061_battery.tsv', 'ciphertext.tsv']}
def S(c, seqs):
    best = 0
    for s in seqs:
        for i in range(len(s) - len(c) + 1):
            best = max(best, sum(a == b for a, b in zip(c, s[i:i + len(c)])))
    return best
cribs = [r for r in csv.reader((l for l in open(os.path.join(H, 'crib_0729.tsv')) if not l.startswith('#')), delimiter='\t')]
TGT = {'purm': ('ciphertext_2046_legend.tsv', ['2046_title1', '2046_title2']),
       'zeel': ('ciphertext_2077_legend.tsv', ['2077_L01', '2077_L02', '2077_L03'])}
out = []
for cid, gloss, occ, signs, plain in cribs:
    for variant, c in (('as_read', signs.split()), ('0->o', ['o' if x == '0' else x for x in signs.split()])):
        if variant == '0->o' and '0' not in signs.split(): continue
        tf, tl = TGT[cid[:4]]
        tgt = [F[tf][l] for l in tl]
        st = S(c, tgt)
        other = [s for f, d in F.items() for l, s in d.items() if not (f == tf and l in tl)]
        so = S(c, other)
        rng = random.Random(729); null = []
        for _ in range(1000):
            p = c[:]; rng.shuffle(p); null.append(S(p, tgt))
        null.sort(); p99 = null[989]
        g1 = st >= 0.5 * len(c); g2 = st > so; g3 = st > p99
        out.append(f"{cid}\t{variant}\tS_target={st}/{len(c)}\tS_other_max={so}\tshuffle_p99={p99}\tg1={g1}\tg2={g2}\tg3={g3}\t"
                   f"{'HIT' if g1 and g2 and g3 else 'MISS'}")
txt = '\n'.join(out) + '\n'
fn = os.path.join(H, 'score.out')
if '--check' in sys.argv:
    sys.exit(0 if open(fn).read() == txt else 1)
open(fn, 'w').write(txt); print(txt, end='')
