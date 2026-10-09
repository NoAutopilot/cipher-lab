#!/usr/bin/env python3
"""Offline test for tools/cvd_check.py (MQS-SHEETS unit 1). Expected numbers are the 9 Oct 2026 pass's own
computation. Run: python3 tools/tests/test_cvd_check.py"""
import os, random, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import cvd_check as c

fails = 0
def t(ok, msg):
    global fails
    fails += not ok
    print('PASS' if ok else 'FAIL', msg)
def near(a, b, tol): return abs(a - b) <= tol

# must catch: legacy sorter ok vs bad
r = c.check(['#2f6b3a', '#b3261e'], '#f3f1ec')
t(r['code'] == 1 and near(r['worst']['deutan'][0], 11.3, 0.5) and near(r['worst']['protan'][0], 8.7, 0.5),
  'legacy ok/bad FAILS (deutan %.1f protan %.1f)' % (r['worst']['deutan'][0], r['worst']['protan'][0]))
# must catch: first proposed set
r = c.check(['#0072B2', '#E69F00', '#F0E442', '#CC79A7'], '#ffffff')
oy = c.de2000(c.rgb_to_lab(c.simulate('#E69F00', 'deutan')), c.rgb_to_lab(c.simulate('#F0E442', 'deutan')))
t(r['code'] == 1 and near(oy, 11.6, 0.5) and near(c.contrast('#E69F00', '#ffffff'), 2.25, 0.02),
  'first proposed set FAILS (orange/yellow deutan %.1f; #E69F00 contrast %.2f)' % (oy, c.contrast('#E69F00', '#ffffff')))
# must catch: light ink on yellow tint
r = c.check(['#000000'], '#ffffff', pairs=[('#F0E442', '#ece6dc')])
t(r['code'] == 1 and near(c.contrast('#ece6dc', '#F0E442'), 1.07, 0.02), 'light ink on yellow tint FAILS (%.2f)' % c.contrast('#ece6dc', '#F0E442'))
# must not block: the three palettes
for name, want in (('sorter_light', 20.7), ('sheets_light', 22.7), ('dark', 25.5)):
    r = c.check_palette(name)
    t(r['code'] == 0 and near(r['min_de'], want, 0.5) and all(m is not None and m > 0 for m in r['margin'].values()),
      '%s passes (worst %.1f, margins %s)' % (name, r['min_de'], {k: round(v, 1) for k, v in r['margin'].items()}))
# tint/text pairs of the palettes carry dark ink
t(near(c.contrast('#24211c', '#F0E442'), 12.13, 0.05) and near(c.contrast('#24211c', '#56B4E9'), 6.95, 0.05)
  and near(c.contrast('#1b1916', '#F0E442'), 13.26, 0.05) and near(c.contrast('#1b1916', '#56B4E9'), 7.60, 0.05),
  'dark ink on tints: 12.13 / 6.95 (sorter), 13.26 / 7.60 (dark)')
# synthetic palette worst ~19.5 -> exit 2, not 1
base = '#0072B2'
found = None
for k in range(1000):  # blend the blue toward grey #767676 until the worst vision sits in [19, 20)
    f = k / 1000.0
    rgb = [x * (1 - f) + y * f for x, y in zip(c.parse_hex(base), c.parse_hex('#767676'))]
    other = c.to_hex(rgb)
    d = min(c.de2000(c.rgb_to_lab(c.simulate(base, v)), c.rgb_to_lab(c.simulate(other, v))) for v in c.VISIONS)
    if 19.0 <= d < 20.0:
        found = (other, d); break
r = c.check([base, found[0]], '#ffffff') if found else None
t(found is not None and r['code'] == 2, 'synthetic palette at worst %.1f returns exit 2 (WARN), not 1' % (found[1] if found else -1))
# CLI exit codes
t(c.main(['--palette', 'sheets_light']) == 0 and c.main(['--marks', '#2f6b3a,#b3261e', '--bg', '#f3f1ec']) == 1, 'CLI exit codes 0 / 1')
# de2000 vs published Sharma/Wu/Dalal pairs (skimage not required)
t(near(c.de2000((50, 2.6772, -79.7751), (50, 0, -82.7485)), 2.0425, 1e-3)
  and near(c.de2000((50, 2.5, 0), (50, 0, -2.5)), 4.3065, 1e-3), 'de2000 matches Sharma et al. 2005 test pairs')
try:
    from skimage.color import deltaE_ciede2000, rgb2lab
    import numpy as np
    rnd = random.Random(1); worst = 0
    for _ in range(20):
        a = '#%06x' % rnd.randrange(1 << 24); b = '#%06x' % rnd.randrange(1 << 24)
        ref = float(deltaE_ciede2000(rgb2lab(np.array([[c.parse_hex(a)]])), rgb2lab(np.array([[c.parse_hex(b)]])))[0, 0])
        worst = max(worst, abs(ref - c.de2000(c.rgb_to_lab(a), c.rgb_to_lab(b))))
    t(worst < 0.01, 'de2000 agrees with skimage on 20 random pairs (max diff %.4f)' % worst)
except ImportError:
    print('SKIP skimage not installed')
# --audit (MQS-CVD-AUDIT): must catch a cv2 BGR red vs green overlay; must not flag Okabe-Ito or neutrals
found = c.extract('import cv2\ncv2.rectangle(d, a, b, (0, 0, 255), 1)\ncv2.line(d, a, b, (0, 160, 0), 1)\n')
_, fl = c.audit_colours(found)
t(set(found) == {'#ff0000', '#00a000'} and any(k == 'CVD-COLLAPSE' for _, _, k, _ in fl)
  and any(k == 'RED-GREEN' for _, _, k, _ in fl), 'audit catches cv2 BGR red vs green')
_, fl = c.audit_colours(['#E69F00', '#56B4E9', '#009E73', '#F0E442', '#0072B2', '#D55E00', '#CC79A7'])
t(not any(k == 'CVD-COLLAPSE' for _, _, k, _ in fl), 'audit does not collapse-flag Okabe-Ito')
chrom, fl = c.audit_colours(['#ffffff', '#24211c', '#f3f1ec'])
t(chrom == [] and fl == [], 'audit skips neutrals')
t(set(c.extract('a{color:#fff;background:#0072B2} &#123; x#123abc')) == {'#ffffff', '#0072b2'}, 'audit hex extraction')
sys.exit(1 if fails else 0)
