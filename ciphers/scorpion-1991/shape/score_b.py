#!/usr/bin/env python3
"""Score R13-SCORP2C (PREREG-R13-SCORP2C.md): blind second coder B's S1 and Zodiac codes against coder A's
(A2P4-SCORP2) and the Unicode-geometric control. Reads shape/coder_b_s1.tsv (position, code) and
shape/coder_b_zodiac.tsv (glyph, code). Writes shape/result_b.tsv; --check exits non-zero when stale (rule 7)."""
import csv, os, sys
from collections import Counter
H = os.path.dirname(os.path.abspath(__file__)); D = os.path.dirname(H)
rd = lambda f: list(csv.DictReader(open(os.path.join(H, f)), delimiter='\t'))
a_s1 = {r['sign']: r['code'].strip() for r in rd('scorpion_codes.tsv')}
a_zo = {r['glyph']: r['code'].strip() for r in rd('zodiac_codes.tsv')}
ctl = {r['code'].strip() for r in rd('control_unicode_geometric.tsv')}
b_pos = {r['position']: r['code'].strip() for r in rd('coder_b_s1.tsv')}
b_zo = {r['glyph']: r['code'].strip() for r in rd('coder_b_zodiac.tsv')}
rows = [l.split() for l in open(os.path.join(D, 'ciphertext.txt')) if l.strip() and not l.startswith('#')][:7]
pos = [(f'r{i+1}c{j+1}', t) for i, r in enumerate(rows) for j, t in enumerate(r)]
assert len(pos) == 70 and len(b_pos) == 70 and len(b_zo) == 70 and len(a_s1) == 53
bytype = {}
for p, t in pos: bytype.setdefault(t, []).append(b_pos[p])
b_type = {t: Counter(v).most_common()[0][0] if Counter(v).most_common()[0][1] > 1 or len(v) == 1 else v[0]
          for t, v in bytype.items()}
for t, v in bytype.items():  # modal, tie -> earliest position
    c = Counter(v); top = max(c.values()); b_type[t] = next(x for x in v if c[x] == top)
nl = lambda c: not c.startswith('L:')
def dist(s1codes, zset):
    d = {c for c in s1codes if nl(c)}
    z = {c for c in d if c in zset}; k = {c for c in d if c in ctl}
    return d, z, k
fam = lambda c: c.split('/')[0] if '/' in c else c.split(':')[0] + ':' + (c.split(':')[1] if c.startswith('ST:') else '')
def kappa(x, y):
    n = len(x); po = sum(a == b for a, b in zip(x, y)) / n
    cx, cy = Counter(x), Counter(y); pe = sum(cx[k] * cy[k] for k in cx) / n / n
    return po, (po - pe) / (1 - pe) if pe < 1 else 1.0
out = [('item', 'coder_a', 'coder_b', 'in_zodiac_A', 'in_zodiac_B', 'in_control')]
for t in a_s1: out.append((f'S1:{t}', a_s1[t], b_type[t], str(b_type[t] in set(a_zo.values())),
                           str(b_type[t] in set(b_zo.values())), str(b_type[t] in ctl)))
for g in a_zo: out.append((f'Z:{g}', a_zo[g], b_zo[g], '', '', str(b_zo[g] in ctl)))
d, zA, kA = dist(b_type.values(), set(a_zo.values()))
_, zB, kB = dist(b_type.values(), set(b_zo.values()))
dA, zAA, kAA = dist(a_s1.values(), set(a_zo.values()))
onlyA = sorted(zA - ctl)
xa = [a_s1[t] for _, t in pos]; xb = [b_pos[p] for p, _ in pos]
s1po, s1k = kappa(xa, xb); s1fpo, s1fk = kappa([fam(c) for c in xa], [fam(c) for c in xb])
zg = list(a_zo); zpo, zk = kappa([a_zo[g] for g in zg], [b_zo[g] for g in zg])
zfpo, zfk = kappa([fam(a_zo[g]) for g in zg], [fam(b_zo[g]) for g in zg])
prim = [t for t in a_s1 if nl(b_type[t])]
summ = (f"PRIMARY cross-coder (B S1 vs A Zodiac): B distinct non-letter S1 codes {len(d)}: zodiac {len(zA)}, control {len(kA)}; "
        f"zodiac-only {' '.join(onlyA) or '-'}\n"
        f"decision (prereg: diff >= 5 AND >=1 zodiac-only): {'SUPPORT' if len(zA) - len(kA) >= 5 and onlyA else 'NO SUPPORT'} "
        f"(difference {len(zA) - len(kA)})\n"
        f"secondary (a) B both sides: zodiac {len(zB)}, control {len(kB)} (difference {len(zB) - len(kB)})\n"
        f"secondary (b) B per-type non-letter {len(prim)}: zodiac(A) {sum(b_type[t] in set(a_zo.values()) for t in prim)}, "
        f"zodiac(B) {sum(b_type[t] in set(b_zo.values()) for t in prim)}, control {sum(b_type[t] in ctl for t in prim)}\n"
        f"reference A both sides distinct: {len(dA)} codes, zodiac {len(zAA)}, control {len(kAA)}\n"
        f"agreement S1 70 positions: exact {s1po:.3f} kappa {s1k:.3f}; family {s1fpo:.3f} kappa {s1fk:.3f}\n"
        f"agreement Zodiac 70 glyphs: exact {zpo:.3f} kappa {zk:.3f}; family {zfpo:.3f} kappa {zfk:.3f}\n")
txt = '\n'.join('\t'.join(r) for r in out) + '\n'
p = os.path.join(H, 'result_b.tsv')
if '--check' in sys.argv:
    ok = os.path.exists(p) and open(p).read() == txt
    print(summ, 'check:', 'OK' if ok else 'STALE'); sys.exit(0 if ok else 1)
open(p, 'w').write(txt); print(summ, end='')
