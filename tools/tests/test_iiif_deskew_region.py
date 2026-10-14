#!/usr/bin/env python3
"""Offline test for tools/iiif_lines.py --deskew-region (VIV-F191, 14 Oct 2026). No network.
Must catch: a page whose lines all share one tilt (b = -0.025, ~1.4 deg, 50 px drift over 2000 px at pitch 90 -- the
fr.16105 f.194r shape N6-VIV63C deskewed by hand): the fixed-y cut's right end leaves the line, the rotated flat cut keeps
every line's ink centred at BOTH ends of every band.
Must not block / change: (a) a level page fits |deg| <= 0.1 and gives the same line count as no option; (b) without the
option the crops and manifest carry no deskew_region; (c) a given DEG is applied as given; (d) the option refuses
--follow-slope, --deskew and --check-boxes.
Run: python3 tools/tests/test_iiif_deskew_region.py"""
import contextlib, io, json, os, shutil, sys, tempfile
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import iiif_lines as il
from PIL import Image, ImageDraw

fails = 0
def check(ok, what):
    global fails
    fails += not ok
    print('PASS' if ok else 'FAIL', what)

def run(*args):
    with contextlib.redirect_stdout(io.StringIO()):
        return il.main(list(args))

def page(path, slope, n=8, pitch=90, w=2000, top=150):
    rng = np.random.default_rng(7)
    im = Image.new('L', (w, top * 2 + pitch * n), 255)
    d = ImageDraw.Draw(im)
    for i in range(n):
        for x in range(40, w - 40, 22):
            y = top + i * pitch + slope * (x - w / 2)
            h = int(rng.integers(10, 18))
            d.ellipse([x, y - h, x + 12, y + h // 2], fill=0)
    im.save(path)

def centre_offset(crop_path, side):
    a = np.asarray(Image.open(crop_path).convert('L'))
    w = a.shape[1]
    part = a[:, :w // 6] if side == 'left' else a[:, -w // 6:]
    rows = np.where((part < 128).sum(axis=1) > 0)[0]
    if not len(rows):
        return 999
    ink = (part < 128).sum(axis=1).astype(float)
    cy = (ink * np.arange(len(ink))).sum() / ink.sum()
    return abs(cy - a.shape[0] / 2)

tmp = tempfile.mkdtemp()
try:
    tilted = os.path.join(tmp, 'tilt.png'); page(tilted, -0.025)
    level = os.path.join(tmp, 'level.png'); page(level, 0.0)

    # must catch: tilted page
    o1 = os.path.join(tmp, 'flat'); r1 = run('--image', tilted, '--out', o1, '--prefix', 'p', '--max-width', '1200',
                                           '--overlap', '100', '--distance', '50')
    o2 = os.path.join(tmp, 'rot'); r2 = run('--image', tilted, '--out', o2, '--prefix', 'p', '--max-width', '1200',
                                          '--overlap', '100', '--distance', '50', '--deskew-region')
    deg = r2['deskew_region']['deg']
    want = np.degrees(np.arctan(-0.025))
    check(abs(deg - want) <= 0.15, f'fitted angle {deg:+.2f} within 0.15 deg of the true {want:+.2f}')
    check(len(r2['centres']) == 8, f"rotated page: 8 lines found ({len(r2['centres'])})")
    worst_rot = max(centre_offset(os.path.join(o2, e['crop']), side) for e in r2['entries'] for side in ('left', 'right'))
    worst_flat = max(centre_offset(os.path.join(o1, e['crop']), side) for e in r1['entries'] for side in ('left', 'right'))
    check(worst_rot <= 8, f'rotated flat cut: every band end within 8 px of the crop middle (worst {worst_rot:.1f})')
    check(worst_flat > 15, f'unrotated fixed-y cut leaves the line at an end (worst {worst_flat:.1f} > 15)')
    m = json.load(open(os.path.join(o2, 'manifest.json')))['iiif_lines']
    check(all(e.get('deskew_region', {}).get('deg') == deg for e in m), 'every manifest entry records deskew_region.deg')
    check(all('--deskew-region' in e['method'] for e in m), 'method names --deskew-region')

    # must not block: level page
    o3 = os.path.join(tmp, 'lev'); r3 = run('--image', level, '--out', o3, '--prefix', 'p', '--max-width', '1200',
                                          '--overlap', '100', '--distance', '50', '--deskew-region')
    o4 = os.path.join(tmp, 'lev0'); r4 = run('--image', level, '--out', o4, '--prefix', 'p', '--max-width', '1200',
                                           '--overlap', '100', '--distance', '50')
    check(abs(r3['deskew_region']['deg']) <= 0.1, f"level page fits |deg| <= 0.1 ({r3['deskew_region']['deg']:+.2f})")
    check(len(r3['centres']) == len(r4['centres']) == 8, 'level page: same line count with and without the option')
    m4 = json.load(open(os.path.join(o4, 'manifest.json')))['iiif_lines']
    check(r4['deskew_region'] is None and not any('deskew_region' in e for e in m4), 'no option: no deskew_region anywhere')

    # given angle
    o5 = os.path.join(tmp, 'given'); r5 = run('--image', tilted, '--out', o5, '--prefix', 'p', '--max-width', '1200',
                                            '--overlap', '100', '--distance', '50', '--deskew-region', '-1.4')
    check(r5['deskew_region']['deg'] == -1.4 and r5['deskew_region']['how'] == 'given', 'a given DEG is applied as given')

    # refusals
    for extra in (['--follow-slope', '200'], ['--deskew'], ['--check-boxes', tilted]):
        try:
            with contextlib.redirect_stderr(io.StringIO()):
                run('--image', tilted, '--out', os.path.join(tmp, 'x'), '--deskew-region', *extra)
            check(False, f'refuses --deskew-region with {extra[0]}')
        except SystemExit:
            check(True, f'refuses --deskew-region with {extra[0]}')
finally:
    shutil.rmtree(tmp)
print('ALL PASS' if not fails else f'{fails} FAIL')
sys.exit(1 if fails else 0)
