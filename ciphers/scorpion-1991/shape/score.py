#!/usr/bin/env python3
"""Score spec test 3 (scorpion-1991): S1 sign types with an identical-feature-code counterpart in the
Zodiac Z408/Z340 glyph set vs the Unicode Geometric Shapes control (shape_prereg.md). Writes shape/result.tsv;
with --check exits non-zero if the committed result.tsv is stale (rule 7)."""
import csv, os, sys
H = os.path.dirname(os.path.abspath(__file__))
rd = lambda f: list(csv.DictReader(open(os.path.join(H, f)), delimiter='\t'))
sc = rd('scorpion_codes.tsv'); zo = rd('zodiac_codes.tsv'); co = rd('control_unicode_geometric.tsv')
assert len(sc) == 53 and len(zo) == 70 and len(co) == 70
zc = {}
for r in zo: zc.setdefault(r['code'], []).append(r['glyph'])
cc = {}
for r in co: cc.setdefault(r['code'], []).append(r['codepoint'])
base = lambda c: c.split('/')[0] if '/' in c else None
rows = [('sign', 'code', 'tier', 'zodiac', 'control', 'zodiac_near', 'control_near')]
for r in sc:
    c = r['code']; tier = 'letter' if c.startswith('L:') else 'primary'
    zn = '' if c in zc else ','.join(g for k, v in zc.items() if base(c) and base(k) == base(c) for g in v)
    cn = '' if c in cc else ','.join(g for k, v in cc.items() if base(c) and base(k) == base(c) for g in v)
    rows.append((r['sign'], c, tier, ','.join(zc.get(c, [])), ','.join(cc.get(c, [])), zn, cn))
out = '\n'.join('\t'.join(x) for x in rows) + '\n'
prim = [x for x in rows[1:] if x[2] == 'primary']; let = [x for x in rows[1:] if x[2] == 'letter']
zp = sum(1 for x in prim if x[3]); cp = sum(1 for x in prim if x[4])
geo = [x for x in prim if not x[1].startswith(('RL:', 'ROT:'))]
zg = sum(1 for x in geo if x[3]); cg = sum(1 for x in geo if x[4])
rl = [x for x in prim if x[1].startswith(('RL:', 'ROT:'))]
only_z = [x[0] for x in prim if x[3] and not x[4]]
zl = sum(1 for x in let if x[3])
summ = (f"primary (non-letter) S1 types {len(prim)}: zodiac {zp}, control {cp}\n"
        f"  of which shape/stroke codes {len(geo)}: zodiac {zg}, control {cg}; mirrored/rotated letters {len(rl)}: zodiac {sum(1 for x in rl if x[3])}, control 0 by construction\n"
        f"  matched in zodiac only: {' '.join(only_z)}\n"
        f"letter S1 types {len(let)}: zodiac {zl} (plain A-Z baseline {len(let)})\n"
        f"decision (prereg: zodiac-control >= 5 AND >=1 zodiac-only match): "
        f"{'SUPPORT' if zp - cp >= 5 and only_z else 'NO SUPPORT'} (difference {zp - cp})\n")
p = os.path.join(H, 'result.tsv')
if '--check' in sys.argv:
    ok = os.path.exists(p) and open(p).read() == out
    print(summ, 'check:', 'OK' if ok else 'STALE'); sys.exit(0 if ok else 1)
open(p, 'w').write(out); print(summ, end='')
