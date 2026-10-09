#!/usr/bin/env python3
"""Held-out control for cvd_check.py --audit (MQS-CVD-AUDIT, 9 Oct 2026); gates in PREREG-MQS-CVD-AUDIT.md.
Writes synthetic HTML / RGB-tuple / cv2-BGR files to a temp dir, audits them, prints recall, false flags, rotated null."""
import itertools, os, sys, tempfile
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import cvd_check as c

POS = [('#F8766D', '#00BA38'), ('#F8766D', '#7CAE00'), ('#377eb8', '#984ea3'), ('#d95f02', '#1b9e77'),
       ('#fc8d62', '#66c2a5'), ('#C0504D', '#9BBB59'), ('#4F81BD', '#8064A2'), ('#dc3912', '#109618'),
       ('#3366cc', '#990099'), ('#dc3545', '#28a745')]
TOL = ['#4477AA', '#EE6677', '#228833', '#CCBB44', '#66CCEE', '#AA3377']
IBM = ['#648FFF', '#785EF0', '#DC267F', '#FE6100', '#FFB000']
NEG = list(itertools.combinations(TOL, 2)) + list(itertools.combinations(IBM, 2)) + [
    ('#0077BB', '#EE7733'), ('#33BBEE', '#CC3311'), ('#009988', '#EE3377'), ('#0077BB', '#CC3311'),
    ('#33BBEE', '#EE7733'), ('#009988', '#CC3311')]
NEUTRAL = ['#ffffff', '#000000', '#f3f1ec', '#24211c']


def rot(h):  # RGB -> GBR
    h = h.lstrip('#'); return '#' + h[2:4] + h[4:6] + h[0:2]


def tup(h):
    r, g, b = (int(h.lstrip('#')[i:i + 2], 16) for i in (0, 2, 4)); return r, g, b


def write(d, name, pair):
    cols = list(pair) + NEUTRAL
    files = {
        name + '.html': '\n'.join('<span style="color:%s">x</span>' % x for x in cols),
        name + '_rgb.py': 'from PIL import ImageDraw\n' + '\n'.join('d.rectangle(box, outline=(%d, %d, %d))' % tup(x) for x in cols),
        name + '_bgr.py': 'import cv2\n' + '\n'.join('cv2.rectangle(img, p, q, (%d, %d, %d), 2)' % tup(x)[::-1] for x in cols),
    }
    paths = []
    for fn, txt in files.items():
        p = os.path.join(d, fn); open(p, 'w').write(txt); paths.append(p)
    return paths


def run(pairs, d, tag, rotate=False):
    flagged, extract_ok = 0, 0
    for i, pr in enumerate(pairs):
        pr = tuple(rot(x) for x in pr) if rotate else pr
        want = {x.lower() for x in pr}
        hits = []
        for p in write(d, '%s%d' % (tag, i), pr):
            found = c.extract(open(p).read())
            extract_ok += want <= set(found)
            _, fl = c.audit_colours(found)
            hits.append(any(k == 'CVD-COLLAPSE' and {a, b} == want for a, b, k, _ in fl))
        flagged += all(hits)
    return flagged, extract_ok


if __name__ == '__main__':
    with tempfile.TemporaryDirectory() as d:
        fp, ep = run(POS, d, 'pos')
        fn, en = run(NEG, d, 'neg')
        fr, _ = run(POS, d, 'rot', rotate=True)
    rec, null = fp / len(POS), fr / len(POS)
    print('extraction %d/%d' % (ep + en, 3 * (len(POS) + len(NEG))))
    print('recall %d/%d = %.2f (gate >= 0.70)' % (fp, len(POS), rec))
    print('false flags %d/%d (gate <= 3)' % (fn, len(NEG)))
    print('rotated null recall %d/%d = %.2f (gate <= %.2f)' % (fr, len(POS), null, rec - 0.30))
    ok = rec >= 0.70 and fn <= 3 and null <= rec - 0.30 and ep + en == 3 * (len(POS) + len(NEG))
    print('CONTROL', 'PASS' if ok else 'FAIL')
    sys.exit(0 if ok else 1)
