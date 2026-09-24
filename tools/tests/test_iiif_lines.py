#!/usr/bin/env python3
"""Offline test for tools/iiif_lines.py (no network; writes only to a temporary folder).
1. Synthetic page, 12 lines of blob 'writing' at a 110 px pitch on 5000 px width: 12 lines found, centres within
   10 px of truth, every crop under 2500 px wide, manifest entries carry page-coordinate boxes.
2. fr.20140 f.36r native image (ciphers/fr20140-danzay-1557/images/native_f71.jpg): box 1300,1770,3400,210, the one
   cipher line the reconciler transcribed, gives 1 line; box 1000,1600,3900,1400 gives the 8 full lines visible in
   that region (checked by eye on the --debug overlay, 24 Sept 2026).
3. Size cap: with the cap lowered, the fetched reference copy is downscaled and renamed, the crops are not.
Run: python3 tools/tests/test_iiif_lines.py"""
import contextlib, io, json, os, random, shutil, sys, tempfile
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

tmp = tempfile.mkdtemp()
try:
    random.seed(1)
    W, H, pitch, n = 5000, 1500, 110, 12
    im = Image.new('RGB', (W, H), (235, 225, 200)); d = ImageDraw.Draw(im)
    truth = [80 + pitch * i for i in range(n)]
    for y in truth:
        x = 150
        while x < W - 300:
            w = random.randint(20, 60); d.ellipse([x, y - 18, x + w, y + 18], fill=(40, 30, 20)); x += w + random.randint(15, 40)
    page = os.path.join(tmp, 'page.jpg'); im.save(page, quality=90)
    out = os.path.join(tmp, 'syn')
    r = run('--image', page, '--out', out, '--prefix', 'syn', '--region', '0,0,5000,1500')
    check(len(r['centres']) == n and all(abs(c - t) <= 10 for c, t in zip(r['centres'], truth)),
          f"synthetic: {len(r['centres'])} of {n} lines, centres within 10 px")
    widths = [Image.open(os.path.join(out, e['crop'])).width for e in r['entries']]
    check(max(widths) < 2500 and len(r['segments']) == 3, f'crops under 2500 px wide ({max(widths)}), 3 segments')
    man = json.load(open(os.path.join(out, 'manifest.json')))
    check(len(man['iiif_lines']) == n * 3 and man['iiif_lines'][0]['box'][1] >= 0, 'manifest has one entry per crop')

    f71 = os.path.join(ROOT, 'ciphers', 'fr20140-danzay-1557', 'images', 'native_f71.jpg')
    r = run('--image', f71, '--out', os.path.join(tmp, 'a'), '--region', '1300,1770,3400,210', '--dry-run')
    check(len(r['centres']) == 1, 'fr.20140 f.36r cipher line box: 1 line')
    r = run('--image', f71, '--out', os.path.join(tmp, 'b'), '--region', '1000,1600,3900,1400', '--dry-run')
    check(len(r['centres']) == 8, f"fr.20140 f.36r upper block: {len(r['centres'])} lines (8 by eye)")

    out = os.path.join(tmp, 'cap'); os.makedirs(out)
    shutil.copy(page, os.path.join(out, 'src_test_full.jpg'))
    il.LIMIT = 1000
    r = run('--image', os.path.join(out, 'src_test_full.jpg'), '--out', out, '--prefix', 'cap')
    files = os.listdir(out)
    check('src_test_full_ref1600.jpg' in files and 'src_test_full.jpg' not in files, 'reference copy downscaled and renamed')
    check(Image.open(os.path.join(out, 'cap_L01_s1.jpg')).width == 2400, 'crops kept at native resolution')
finally:
    shutil.rmtree(tmp)
print('iiif_lines:', 'all tests pass' if not fails else f'{fails} failures')
sys.exit(1 if fails else 0)
