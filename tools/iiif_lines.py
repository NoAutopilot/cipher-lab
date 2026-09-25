#!/usr/bin/env python3
"""Fetch a manuscript region once at native resolution and cut it into line crops a transcriber can read.

  python3 tools/iiif_lines.py (URL | --ark ARK --canvas N | --image FILE) --out ciphers/<target>/images
          [--region x,y,w,h] [--columns x0:x1] [--prefix f69] [--distance PX] [--prominence N] [--ink 170]
          [--smooth 1] [--lines-per-crop 1] [--max-width 2400] [--overlap 150] [--top-margin PX] [--debug] [--dry-run]
  URL: an IIIF image URL (any form: service base, info.json, or a full .../region/size/rotation/quality.jpg).
  Needs numpy and Pillow (pip install numpy pillow); no scipy.

Lesson answered (LEDGER.md 23-24 Sept 2026): the Opus f.30 worker on fr2980-gramont ran to its cap cutting line crops
by hand, and three workers wrote three crop scripts (dupuy452-carpi-1520/images/crop.py, fr2980-gramont/crop.py,
dupuy468-anhalt/images/crop.py). This is the dupuy452 method once, with its parameters exposed.

Steps:
  1. Fetch {base}/{x,y,w,h}/full/0/native.jpg (Gallica; 'default' elsewhere) once into OUT/src_<id>_<region>.jpg; a
     later run reads the file. One request, descriptive User-Agent; HTTP 403/429 or an altcha/challenge page stops the
     run with a message (log it in NOTES.md and ROOM.md), no retry loop.
  2. Row ink-density profile over --columns (pixels darker than --ink, summed per row, optionally smoothed).
  3. Line centres = local maxima at least --distance px apart with prominence >= --prominence (defaults: distance
     0.7 x the pitch found by autocorrelation, prominence 15% of the profile maximum). Band edges are the midpoints
     between centres, so a cut falls in whitespace; the first and last bands get half a pitch of margin.
  4. Each band (--lines-per-crop lines) is cut at native resolution into segments no wider than --max-width (default
     2400, under the 2500 px reading limit) with --overlap px shared between neighbours: OUT/<prefix>_L01_s1.jpg ...
  5. OUT/manifest.json gains one entry per crop under the key "iiif_lines" (source URL, source file, box in native
     page coordinates, crop path, date); entries for the same crop path are replaced, other keys are left alone.
  6. If OUT is over 30 MB afterwards, the reference copies this script fetched (src_*.jpg) are downscaled to 1600 px
     wide, renamed *_ref1600.jpg and marked so in the manifest (a later run refetches the native region); crops are never downscaled.
  --debug writes OUT/<prefix>_lines_debug.jpg: the region at 1600 px wide with centres (red) and band edges (blue).
  --dry-run prints the detected lines and writes nothing but the cached source.

Test: python3 tools/tests/test_iiif_lines.py (offline: a synthetic page with a known line count and pitch, and the
committed native image of fr.20140 f.36r, whose box 1300,1770,3400,210 holds one cipher line).
"""
import argparse, json, os, re, sys, time, urllib.error, urllib.request

import numpy as np
from PIL import Image, ImageDraw

Image.MAX_IMAGE_PIXELS = None
UA = 'cipher-lab research script (contact via repository)'
LIMIT = 30 * 1024 * 1024


def iiif_base(url):
    """Strip an IIIF image URL down to its service base."""
    url = re.sub(r'/info\.json$', '', url)
    m = re.match(r'(.*?)/(full|square|pct:[^/]+|\d+,\d+,\d+,\d+)/([^/]+)/(!?\d+(?:\.\d+)?)/(\w+)\.(jpg|png|tif|webp)$', url)
    return m.group(1) if m else url.rstrip('/')


def fetch_region(base, region, out):
    quality = 'native' if 'gallica.bnf.fr' in base else 'default'
    url = f"{base}/{region or 'full'}/full/0/{quality}.jpg"
    ident = re.sub(r'[^A-Za-z0-9]+', '_', base.split('/iiif/')[-1]).strip('_')[-60:]
    path = os.path.join(out, f"src_{ident}_{(region or 'full').replace(',', '_')}.jpg")
    if os.path.exists(path):
        return path, url, 'cached'
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    try:
        body = urllib.request.urlopen(req, timeout=300).read()
    except urllib.error.HTTPError as e:
        sys.exit(f'{url}: HTTP {e.code}; stop (no retry loop). Log it in NOTES.md and ROOM.md.')
    except urllib.error.URLError as e:
        sys.exit(f'{url}: {e.reason}; unreachable from here.')
    if body[:3] != b'\xff\xd8\xff' or b'altcha' in body[:4000].lower():
        sys.exit(f'{url}: not a JPEG (challenge or error page); stop, do not retry. Log it in NOTES.md and ROOM.md.')
    os.makedirs(out, exist_ok=True)
    open(path, 'wb').write(body)
    time.sleep(1.5)
    return path, url, 'fetched'


def profile(gray, x0, x1, ink, smooth):
    p = (gray[:, x0:x1] < ink).sum(axis=1).astype(float)
    if smooth > 1:
        p = np.convolve(p, np.ones(smooth) / smooth, 'same')
    return p


def pitch_of(p, lo=20):
    """Line pitch = first autocorrelation maximum after lag lo."""
    q = p - p.mean()
    ac = np.correlate(q, q, 'full')[len(q) - 1:]
    if len(ac) <= lo + 2:
        return None
    for i in range(lo + 1, len(ac) - 1):
        if ac[i] > 0 and ac[i] >= ac[i - 1] and ac[i] >= ac[i + 1]:
            return int(i)
    return None


def find_peaks(y, distance, prominence):
    """scipy.signal.find_peaks(distance=, prominence=) re-done in numpy: local maxima, the higher kept when two lie
    closer than distance, then prominence = height above the higher of the two bases."""
    n = len(y)
    cand = [i for i in range(1, n - 1) if y[i] > y[i - 1] and y[i] >= y[i + 1]]
    kept = []
    for i in sorted(cand, key=lambda i: (-y[i], i)):
        if all(abs(i - k) >= distance for k in kept):
            kept.append(i)
    out = []
    for p in sorted(kept):
        l = p
        lmin = y[p]
        while l > 0 and y[l - 1] <= y[p]:
            l -= 1; lmin = min(lmin, y[l])
        r = p
        rmin = y[p]
        while r < n - 1 and y[r + 1] <= y[p]:
            r += 1; rmin = min(rmin, y[r])
        if y[p] - max(lmin, rmin) >= prominence:
            out.append(int(p))
    return out


def detect(gray, x0, x1, ink=170, smooth=1, distance=None, prominence=None):
    p = profile(gray, x0, x1, ink, smooth)
    pitch = pitch_of(p) or 100
    distance = distance or max(10, int(0.7 * pitch))
    prominence = prominence if prominence is not None else 0.15 * p.max()
    centres = find_peaks(p, distance, prominence)
    return centres, dict(pitch_autocorr=pitch, distance=distance, prominence=round(float(prominence), 1))


def bands(centres, height, lines_per_crop):
    if not centres:
        return []
    pitch = int(np.median(np.diff(centres))) if len(centres) > 1 else 100
    b = [max(0, centres[0] - pitch // 2)] + [(a + c) // 2 for a, c in zip(centres, centres[1:])] + \
        [min(height, centres[-1] + pitch // 2)]
    return [(b[i], b[min(i + lines_per_crop, len(centres))], min(lines_per_crop, len(centres) - i))
            for i in range(0, len(centres), lines_per_crop)]


def segments(x0, x1, max_width, overlap):
    w = x1 - x0
    if w <= max_width:
        return [(x0, x1)]
    n = int(np.ceil((w - overlap) / (max_width - overlap)))
    step = (w - max_width) / (n - 1)
    return [(x0 + int(round(i * step)), x0 + int(round(i * step)) + max_width) for i in range(n)]


def folder_size(d):
    return sum(os.path.getsize(os.path.join(r, f)) for r, _, fs in os.walk(d) for f in fs)


def update_manifest(out, entries, downscaled=()):
    path = os.path.join(out, 'manifest.json')
    man = json.load(open(path, encoding='utf-8')) if os.path.exists(path) else {}
    if isinstance(man, list):
        man = {'entries': man}
    cur = [e for e in man.get('iiif_lines', []) if e['crop'] not in {x['crop'] for x in entries}]
    man['iiif_lines'] = cur + entries
    for e in man['iiif_lines']:
        if e.get('source_file') in downscaled:
            e['source_file'] = e['source_file'][:-4] + '_ref1600.jpg'
            e['source_file_downscaled'] = True
    json.dump(man, open(path, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    return path


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('url', nargs='?'); ap.add_argument('--ark'); ap.add_argument('--canvas', type=int)
    ap.add_argument('--image', help='a local image instead of fetching (the region is then cut from it)')
    ap.add_argument('--out', required=True, help='images folder of the target')
    ap.add_argument('--region', help='x,y,w,h in native pixels (default: full)')
    ap.add_argument('--columns', help='x0:x1 within the region for the ink profile and the crops (default: all)')
    ap.add_argument('--prefix'); ap.add_argument('--distance', type=int); ap.add_argument('--prominence', type=float)
    ap.add_argument('--ink', type=int, default=170); ap.add_argument('--smooth', type=int, default=1)
    ap.add_argument('--lines-per-crop', type=int, default=1)
    ap.add_argument('--max-width', type=int, default=2400); ap.add_argument('--overlap', type=int, default=150)
    ap.add_argument('--top-margin', type=int, default=0,
                     help='extra px included above each band\'s top edge (e.g. to capture an interlinear gloss '
                          'sitting just above the line); the bottom edge is unchanged, clamped to 0')
    ap.add_argument('--quality', type=int, default=85, help='JPEG quality of the crops')
    ap.add_argument('--debug', action='store_true'); ap.add_argument('--dry-run', action='store_true')
    a = ap.parse_args(argv)
    if a.max_width >= 2500:
        ap.error('--max-width must stay under 2500 px')
    os.makedirs(a.out, exist_ok=True)
    rx, ry = 0, 0
    if a.region:
        rx, ry, rw, rh = map(int, a.region.split(','))
    if a.image:
        src, url, how = a.image, '', 'local'
        im = Image.open(src).convert('L')
        if a.region:
            im = im.crop((rx, ry, rx + rw, ry + rh))
    else:
        base = f'https://gallica.bnf.fr/iiif/ark:/12148/{a.ark}/f{a.canvas}' if a.ark else iiif_base(a.url or '')
        if not base:
            ap.error('give an IIIF URL, --ark with --canvas, or --image')
        src, url, how = fetch_region(base, a.region, a.out)
        im = Image.open(src).convert('L')
    prefix = a.prefix or (f'f{a.canvas}' if a.canvas else os.path.splitext(os.path.basename(src))[0])
    gray = np.asarray(im)
    x0, x1 = (map(int, a.columns.split(':')) if a.columns else (0, im.width))
    centres, params = detect(gray, x0, x1, a.ink, a.smooth, a.distance, a.prominence)
    bb = bands(centres, im.height, a.lines_per_crop)
    if a.top_margin:
        bb = [(max(0, top - a.top_margin), bot, nl) for top, bot, nl in bb]
    segs = segments(x0, x1, a.max_width, a.overlap)
    print(f'{src} ({how}): region {im.width}x{im.height}, {len(centres)} lines, {len(bb)} bands x {len(segs)} segments; '
          f"pitch {params['pitch_autocorr']} distance {params['distance']} prominence {params['prominence']}")
    print('  centres (region y): ' + ' '.join(map(str, centres)))
    if a.dry_run:
        return dict(centres=centres, bands=bb, segments=segs, params=params)
    rgb = Image.open(src)
    if a.image and a.region:
        rgb = rgb.crop((rx, ry, rx + rw, ry + rh))
    entries = []
    date = time.strftime('%d %b %Y', time.gmtime())
    for bi, (top, bot, nl) in enumerate(bb, 1):
        for si, (sx0, sx1) in enumerate(segs, 1):
            name = f'{prefix}_L{bi:02d}' + (f'_s{si}' if len(segs) > 1 else '') + '.jpg'
            rgb.crop((sx0, top, sx1, bot)).convert('RGB').save(os.path.join(a.out, name), quality=a.quality)
            entries.append(dict(crop=name, source_url=url, source_file=os.path.basename(src),
                                box=[rx + sx0, ry + top, rx + sx1, ry + bot], lines_in_crop=nl, band=bi, segment=si,
                                method='tools/iiif_lines.py row ink profile', params=params, date=date))
    if a.debug:
        scale = min(1.0, 1600 / im.width)
        dbg = rgb.convert('RGB').resize((int(im.width * scale), int(im.height * scale)))
        d = ImageDraw.Draw(dbg)
        for c in centres:
            d.line([(0, c * scale), (dbg.width, c * scale)], fill=(255, 0, 0), width=1)
        for top, bot, _ in bb:
            for y in (top, bot):
                d.line([(0, y * scale), (dbg.width, y * scale)], fill=(0, 0, 255), width=1)
        dbg.save(os.path.join(a.out, f'{prefix}_lines_debug.jpg'), quality=70)
    shrunk = []
    if folder_size(a.out) > LIMIT:
        for f in sorted(os.listdir(a.out)):
            if f.startswith('src_') and f.endswith('.jpg'):
                p = os.path.join(a.out, f)
                r = Image.open(p)
                if r.width > 1600 and not f.endswith('_ref1600.jpg'):
                    ref = f[:-4] + '_ref1600.jpg'      # renamed, so a later run refetches the native region
                    r.convert('RGB').resize((1600, int(r.height * 1600 / r.width))).save(os.path.join(a.out, ref),
                                                                                          quality=75)
                    os.remove(p)
                    shrunk.append(f)
        if shrunk:
            print(f'  folder over 30 MB: reference copies downscaled to 1600 px: {", ".join(shrunk)} (crops untouched)')
        if folder_size(a.out) > LIMIT:
            print('  WARNING: folder still over 30 MB; keep the manifest and a sample, note where the rest re-fetches')
    mp = update_manifest(a.out, entries, set(shrunk))
    print(f'  wrote {len(entries)} crops and {mp}')
    return dict(centres=centres, bands=bb, segments=segs, params=params, entries=entries)


if __name__ == '__main__':
    main()
