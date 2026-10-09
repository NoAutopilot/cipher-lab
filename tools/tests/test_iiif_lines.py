#!/usr/bin/env python3
"""Offline test for tools/iiif_lines.py (no network; writes only to a temporary folder).
1. Synthetic page, 12 lines of blob 'writing' at a 110 px pitch on 5000 px width: 12 lines found, centres within
   10 px of truth, every crop under 2500 px wide, manifest entries carry page-coordinate boxes.
2. fr.20140 f.36r native image (ciphers/fr20140-danzay-1557/images/native_f71.jpg): box 1300,1770,3400,210, the one
   cipher line the reconciler transcribed, gives 1 line; box 1000,1600,3900,1400 gives the 8 full lines visible in
   that region (checked by eye on the --debug overlay, 24 Sept 2026).
3. --groups (4) and --follow-slope (5, MONT-RECROP: a sloping line a fixed-y cut loses and a sloped cut keeps).
6. Size cap: with the cap lowered, the fetched reference copy is downscaled and renamed, the crops are not.
7. Size cap must not touch a src_* copy already tracked by git (RUN3-ESSHR, 4 Oct 2026).
8. TXE-B (9 Oct 2026): two lines whose descenders cross the midpoint. Midpoint bands cut them (--check-boxes > 0%);
   --band-extent keeps every box inside its band (0% cut, 0% admitted, box and ink rules, with and without
   --mask-neighbours); --overlap-note states the configured overlap (150 px, 5 signs of 30 px); the mask leaves no
   ghost rim of a removed neighbour stroke.
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

    # 3b. --centres (GAPS4-nevers-birago, 2 Oct 2026): eye-given centres skip detection; the bands follow them exactly
    #     (midpoints between the given centres), and detection is not run, so a profile the autocorrelation would
    #     misread cannot change the cut.
    r = run('--image', page, '--out', os.path.join(tmp, 'c'), '--prefix', 'c', '--region', '0,0,5000,400', '--centres', '80,190,300', '--dry-run')
    check(r['centres'] == [80, 190, 300] and r['params'].get('centres_given') == [80, 190, 300]
          and [b[:2] for b in r['bands']] == [(25, 135), (135, 245), (245, 355)],
          f"--centres: bands {[b[:2] for b in r['bands']]} follow the given centres, detection skipped")
    # 3c. --bottom-margin (NEVBIR-3252-B, 2 Oct 2026): pads each band's bottom edge only, clamped to the region height
    r = run('--image', page, '--out', os.path.join(tmp, 'c'), '--prefix', 'c', '--region', '0,0,5000,400', '--centres', '80,190,300',
            '--bottom-margin', '30', '--dry-run')
    check([b[:2] for b in r['bands']] == [(25, 165), (135, 275), (245, 385)],
          f"--bottom-margin: bands {[b[:2] for b in r['bands']]} padded below by 30")

    # 4. --groups (MONT-CAL, 27 Sept 2026): wide inter-group spacing splits into its 10 groups; uniform spacing (the
    #    fr.4715 f.81r shape) must NOT be reported as groups -- at the same gap it stays one piece.
    for label, gap_between, want in (('spaced', 60, 10), ('uniform', 12, 1)):
        im = Image.new('RGB', (1800, 200), (235, 225, 200)); d = ImageDraw.Draw(im)
        x = 40
        for gidx in range(10):
            for k in range(2):                       # two 'digits' per group, 12 px apart inside a group
                d.rectangle([x, 80, x + 24, 120], fill=(40, 30, 20)); x += 24 + 12
            x += gap_between - 12
        for yy in (20, 180):                         # faint lines above/below so line detection finds three bands
            d.rectangle([40, yy - 10, 1700, yy + 10], fill=(40, 30, 20))
        pg = os.path.join(tmp, f'grp_{label}.jpg'); im.save(pg, quality=95)
        r = run('--image', pg, '--out', os.path.join(tmp, 'g_' + label), '--prefix', 'g', '--groups', '30',
                '--group-lines', '2', '--max-width', '2000', '--distance', '50')
        n = len([e for e in r['entries'] if e.get('group')])
        check(n == want, f"--groups 30 on {label} spacing: {n} pieces (want {want})")

    # 5. --follow-slope (MONT-RECROP, 27 Sept 2026): seven lines at a 52 px pitch sloping 60 px down over 3000 px (the
    #    f.81r shape). A fixed-y cut of band 3 is more than half a pitch off its own line in the last segment (the
    #    strip's central row is the neighbour); the sloped cut follows the line the band shows at its left end.
    im = Image.new('RGB', (3000, 520), (235, 225, 200)); d = ImageDraw.Draw(im)
    slope, starts = 0.02, [60 + 52 * i for i in range(7)]
    for y0 in starts:
        for x in range(100, 2900, 40):
            y = y0 + slope * x
            d.rectangle([x, y - 10, x + 24, y + 10], fill=(40, 30, 20))
    pg = os.path.join(tmp, 'slope.jpg'); im.save(pg, quality=95)
    def centre_ink(path):                            # share of dark pixels in the strip's middle third
        g = Image.open(path).convert('L'); w, h = g.size
        px = [g.getpixel((x, y)) for x in range(0, w, 2) for y in range(h // 3, 2 * h // 3)]
        return sum(v < 120 for v in px) / len(px)
    rf = run('--image', pg, '--out', os.path.join(tmp, 'sf'), '--prefix', 'f', '--max-width', '900', '--distance', '40',
             '--only-lines', '3')
    rs = run('--image', pg, '--out', os.path.join(tmp, 'ss'), '--prefix', 's', '--max-width', '900', '--distance', '40',
             '--only-lines', '3', '--follow-slope', '300', '--slope-local')
    top, bot, _ = rf['bands'][2]
    y0 = min(starts, key=lambda s0: abs(s0 + slope * 250 - (top + bot) / 2))   # the line band 3 shows at its left end
    last = len(rf['segments']); sx0, sx1 = rf['segments'][-1]
    true_y = y0 + slope * (sx0 + sx1) / 2
    fixed_off = abs((top + bot) / 2 - true_y)
    sx = [e for e in rs['entries'] if e['segment'] == last][0]
    fit = sx['slope_fit']                            # the (local) fit this strip was cut on
    slope_off = abs(fit['a'] + fit['b'] * (sx0 + sx1) / 2 - true_y)
    check(fixed_off > 26, f'fixed-y cut is {fixed_off:.0f} px off the line in its last segment (> half the 52 px pitch)')
    check(slope_off <= 8 and abs(fit['b'] - slope) < 0.005,
          f"--follow-slope fit b={fit['b']} follows the same line: {slope_off:.1f} px off in the last segment")
    check(centre_ink(os.path.join(tmp, 'ss', sx['crop'])) > 0.2, 'sloped last-segment strip has the line in its middle third')
    check(len(rs['entries']) == last and all(e.get('slope_fit') for e in rs['entries']),
          '--only-lines 3 writes one line; entries carry slope_fit')
    r0 = run('--image', pg, '--out', os.path.join(tmp, 'sd'), '--prefix', 'd', '--max-width', '900', '--distance', '40')
    check(all('slope_fit' not in e for e in r0['entries']) and r0['entries'][0]['box'] == [0, r0['bands'][0][0], 900,
          r0['bands'][0][1]], 'default (no --follow-slope) unchanged: fixed boxes, no slope_fit')

    # 8. TXE-B: --band-extent, --check-boxes, --overlap-note
    W8 = 3 * 1250 - 2 * 150                         # three segments whose real overlap equals the configured 150 px
    im = Image.new('RGB', (W8, 320), (235, 225, 200)); d = ImageDraw.Draw(im)
    rows8 = []
    for ln, cy in (('1', 100), ('2', 220)):
        k = 0
        for x in range(120, W8 - 150, 60):
            k += 1
            bot = cy + (85 if ln == '1' and k % 3 == 0 else 20)   # every third sign of line 1 has a long descender
            d.ellipse([x, cy - 20, x + 29, cy + 20], fill=(40, 30, 20))   # widest at cy: the slope tracker peaks there
            if bot > cy + 20:
                d.rectangle([x + 10, cy + 15, x + 19, bot], fill=(40, 30, 20))
            rows8.append(('syn8_%s_%03d' % (ln, k), 'syn8', ln, str(k), str(x), str(cy - 20), '30', str(bot - cy + 21)))
    pg8 = os.path.join(tmp, 'desc.jpg'); im.save(pg8, quality=95)
    st = os.path.join(tmp, 'signs.tsv')
    with open(st, 'w') as f:
        f.write('sid\tpage\tline\tpos\tx\ty\tw\th\n' + ''.join('\t'.join(r) + '\n' for r in rows8))
    base8 = ['--image', pg8, '--prefix', 'syn8', '--centres', '100,220', '--max-width', '1250', '--overlap', '150',
             '--check-boxes', st]
    r_old = run(*base8, '--out', os.path.join(tmp, 'b0'), '--dry-run')
    cut_old = r_old['check']['total']['cut'] / r_old['check']['total']['boxes']
    check(cut_old > 0.1, f'midpoint bands cut the synthetic descenders ({cut_old:.1%} of boxes)')
    for extra in ([], ['--mask-neighbours']):
        r_new = run(*base8, '--out', os.path.join(tmp, 'b1'), '--band-extent', '0.1', *extra, '--overlap-note')
        t = r_new['check']['total']
        check(t['cut'] == 0 and t['admitted'] == 0 and r_new['check']['rule'] == 'ink',
              f"--band-extent 0.1 {' '.join(extra)}: ink rule cut {t['cut']}, admitted {t['admitted']} of {t['boxes']}")
        top, bot, _ = r_new['bands'][0]
        check(all(int(r[5]) >= top and int(r[5]) + int(r[7]) <= bot for r in rows8 if r[2] == '1'),
              f'every line-1 box inside its band {top}-{bot}')
        check(all(e.get('band_extent', {}).get('frac') == 0.1 for e in r_new['entries']), 'manifest records band_extent')
    note = open(os.path.join(tmp, 'b1', 'crops_note.md')).read()
    run(*base8, '--out', os.path.join(tmp, 'b3'), '--overlap-note', '--note-scale', '2', '--dry-run')
    note2 = open(os.path.join(tmp, 'b3', 'crops_note.md')).read()
    check('at 2x, so 300 px in each image' in note2, '--note-scale 2 states the overlap in the reader images (300 px)')
    check('overlap by 150 native px' in note and 'about 5 signs' in note and 'is ONE sign' in note,
          '--overlap-note states the configured 150 px overlap, about 5 signs')
    bc = open(os.path.join(tmp, 'b1', 'band_check.tsv')).read().splitlines()
    check(bc[0].startswith('prefix\tband') and bc[-1].split('\t')[1] == 'all', 'band_check.tsv has a total row')
    # the mask removes line 2's ink from band 1's crop without a ghost rim: no pixel there darker than mid-grey
    m1 = [e for e in r_new['entries'] if e['band'] == 1 and e['segment'] == 1][0]
    g = Image.open(os.path.join(tmp, 'b1', m1['crop'])).convert('L')
    lo = [g.getpixel((x, y)) for x in range(0, g.width, 3) for y in range(g.height - 12, g.height)]
    check(min(lo) > 150, f'masked band-1 crop: no neighbour ink or rim in its bottom rows (darkest {min(lo)})')
    # the box rule (sloped bands) agrees on this page
    r_sl = run(*base8, '--out', os.path.join(tmp, 'b2'), '--band-extent', '0.1', '--follow-slope', '300', '--dry-run')
    check(r_sl['check']['rule'] == 'box' and r_sl['check']['total']['cut'] == 0,
          f"--follow-slope: box rule, cut {r_sl['check']['total']['cut']}")

    out = os.path.join(tmp, 'cap'); os.makedirs(out)
    shutil.copy(page, os.path.join(out, 'src_test_full.jpg'))
    il.LIMIT = 1000
    r = run('--image', os.path.join(out, 'src_test_full.jpg'), '--out', out, '--prefix', 'cap')
    files = os.listdir(out)
    check('src_test_full_ref1600.jpg' in files and 'src_test_full.jpg' not in files, 'reference copy downscaled and renamed')
    check(Image.open(os.path.join(out, 'cap_L01_s1.jpg')).width == 2400, 'crops kept at native resolution')
    # 7. RUN3-ESSHR (4 Oct 2026): a src_* copy committed to git is never downscaled or removed by the guard.
    gout = os.path.join(tmp, 'git'); os.makedirs(gout)
    shutil.copy(page, os.path.join(gout, 'src_test_full.jpg'))
    import subprocess
    subprocess.run(['git', 'init', '-q'], cwd=gout, check=True)
    subprocess.run(['git', 'add', 'src_test_full.jpg'], cwd=gout, check=True)
    r = run('--image', os.path.join(gout, 'src_test_full.jpg'), '--out', gout, '--prefix', 'g')
    files = os.listdir(gout)
    check('src_test_full.jpg' in files and 'src_test_full_ref1600.jpg' not in files
          and Image.open(os.path.join(gout, 'src_test_full.jpg')).width == W, 'tracked src_* left untouched by the 30 MB guard')
    man = json.load(open(os.path.join(gout, 'manifest.json')))
    check(all(not e.get('source_file_downscaled') for e in man['iiif_lines']), 'manifest does not mark the tracked copy downscaled')
finally:
    shutil.rmtree(tmp)
print('iiif_lines:', 'all tests pass' if not fails else f'{fails} failures')
sys.exit(1 if fails else 0)
