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
     Keep segments under this width and never re-stitch them back into one wider image, even to give a pass full
     line context: re-stitching measurably lowers blind-transcription agreement (clair349-este-guise-1556, 25 Sept
     2026: ZX-TR349C hand-stitched two --max-width 2400 segments into a single 3895 px line image and two Sonnet
     blind-pass pairs agreed only 39.3% and 42.0% pooled against a 60% gate; ZX-TR349D re-cut the same leaf as the
     tool's own two native segments, kept apart, boundary marked with a corner tick, and pooled agreement on the
     same 33 lines jumped to 70.7%). Pass segments separately and tell the worker where the tick-marked boundary is.
  5. OUT/manifest.json gains one entry per crop under the key "iiif_lines" (source URL, source file, box in native
     page coordinates, crop path, date); entries for the same crop path are replaced, other keys are left alone.
  6. If OUT is over 30 MB afterwards, the reference copies this script fetched (src_*.jpg) are downscaled to 1600 px
     wide, renamed *_ref1600.jpg and marked so in the manifest (a later run refetches the native region); crops are never downscaled.
  --centres y1,y2,... gives the line centres (region y px) by eye and skips step 3, for a short block whose profile the
     autocorrelation misreads (check the --debug overlay first; GAPS4-nevers-birago, 2 Oct 2026).
  --debug writes OUT/<prefix>_lines_debug.jpg: the region at 1600 px wide with centres (red) and band edges (blue).
  --dry-run prints the detected lines and writes nothing but the cached source.
  --groups GAP [--group-lines 3,8] [--group-ink 120] [--group-upscale 3]: split each band into ink pieces at runs of
     >= GAP blank columns in the band's core rows, one crop per piece (<prefix>_Lnn_gNN.jpg), and print the piece count
     with the blank-run width histogram; with --debug, <prefix>_Lnn_groups_debug.jpg boxes and numbers the pieces. A
     hand that spaces groups no wider than digits shows a unimodal histogram: then the pieces are not groups (fr.4715
     f.81r, MONT-CAL 27 Sept 2026) and the crops must not be handed to a reader as groups.
  --follow-slope WIN [--slope-local] [--only-lines 3,8] [--slope-margin PX]: lines that slope across the leaf leave a fixed-y band
     (fr.4715 f.81r, MONT-READ-DIGITS 27 Sept 2026: the named line ran out of the strip's bottom edge in segment 3 or 4
     and the later segments' central row was the neighbouring line). With this option each line is tracked through
     column windows WIN px wide (the row-profile peak nearest the previous window's, within a third of the pitch,
     starting at the band centre in the leftmost window with ink there, so the line followed is the one the fixed-y
     cut shows at the start of the line), a straight line y = a + b*x is fitted to the tracked peaks
     (outliers beyond a quarter pitch dropped, refitted), and every segment is cut as a sheared strip whose centre row
     follows that fit end to end (band height unchanged, plus --slope-margin px above and below). The fit (a, b, peaks
     kept) goes into each manifest entry. --slope-local refits each segment to the peaks within one window of it, for a
     line that curves (f.81r L03: flat for the first segment, then descending). Off by default: without it the cut is exactly as before.

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


def track_line(gray, centre, pitch, x0, x1, win, ink, smooth=5):
    """Follow one line across the region: per column window, the row-profile peak nearest the running estimate
    (within pitch/3), walked rightward from the leftmost inked window at the band centre; then a least-squares y = a + b*x with outliers beyond
    pitch/4 dropped and refitted. Returns (a, b, [(x, y), ...] kept)."""
    edges = list(range(x0, x1, win))
    wins = [(e, min(e + win, x1)) for e in edges if min(e + win, x1) - e >= win // 2]
    lo_h, hi_h = 0, gray.shape[0]
    prof = []
    for wx0, wx1 in wins:
        p = (gray[:, wx0:wx1] < ink).sum(axis=1).astype(float)
        if smooth > 1:
            p = np.convolve(p, np.ones(smooth) / smooth, 'same')
        prof.append(p)
    reach = max(3, pitch // 3)
    ys = [None] * len(wins)
    # start at the leftmost window with real ink near the band centre: the named line is the one the fixed-y cut
    # shows at the start of the line (MONT-RECROP: starting mid-region followed the neighbouring line on L13, L15)
    near = [prof[k][max(0, int(centre) - reach):int(centre) + reach + 1].max() for k in range(len(wins))]
    top = max(near) if near else 0
    mid = next((k for k, v in enumerate(near) if v >= 0.3 * top), len(wins) // 2)

    def pick(k, est):
        a_, b_ = max(lo_h, int(est) - reach), min(hi_h, int(est) + reach + 1)
        seg = prof[k][a_:b_]
        if seg.size == 0 or seg.max() <= 0:
            return None
        return a_ + int(np.argmax(seg))
    ys[mid] = pick(mid, centre)
    for rng in (range(mid + 1, len(wins)), range(mid - 1, -1, -1)):
        est = ys[mid] if ys[mid] is not None else centre
        for k in rng:
            y = pick(k, est)
            ys[k] = y
            if y is not None:
                est = y
    pts = [((w0 + w1) / 2, y) for (w0, w1), y in zip(wins, ys) if y is not None]
    if len(pts) < 2:
        return float(centre), 0.0, pts
    xs, yv = np.array([p[0] for p in pts]), np.array([p[1] for p in pts], float)
    b, a = np.polyfit(xs, yv, 1)
    keep = np.abs(yv - (a + b * xs)) <= max(2, pitch / 4)
    if keep.sum() >= 2 and not keep.all():
        b, a = np.polyfit(xs[keep], yv[keep], 1)
    return float(a), float(b), [(int(x), int(y)) for x, y, k in zip(xs, yv, keep) if k]


def local_fit(pts, sx0, sx1, win, a, b):
    """--slope-local: a line fitted only to the kept peaks within one window of the segment (a curving line); falls
    back to the whole-line fit (a, b) when fewer than two peaks lie there."""
    near = [(x, y) for x, y in pts if sx0 - win <= x <= sx1 + win]
    if len(near) < 2:
        return a, b
    bb, aa = np.polyfit([x for x, _ in near], [y for _, y in near], 1)
    return float(aa), float(bb)


def sheared_strip(img, sx0, sx1, a, b, half):
    """Cut columns sx0..sx1 as a strip whose centre row follows y = a + b*x (region coordinates)."""
    w, h = sx1 - sx0, 2 * half
    return img.transform((w, h), Image.AFFINE, (1, 0, sx0, b, 1, a + b * sx0 - half), resample=Image.BICUBIC,
                         fillcolor=255 if img.mode == 'L' else (255, 255, 255))


def group_pieces(gray, top, bot, x0, x1, ink, gap, core=0.55, minw=4):
    """Split one line band into ink pieces by the column profile of its core rows (the middle `core` share of the
    band, so neighbours' ascenders/descenders do not bridge gaps): a run of >= gap blank columns ends a piece."""
    h = bot - top
    c0, c1 = top + int(h * (1 - core) / 2), bot - int(h * (1 - core) / 2)
    p = (gray[c0:c1, x0:x1] < ink).sum(axis=0)
    xs = np.where(p > 0)[0]
    if not len(xs):
        return []
    out, s, last = [], xs[0], xs[0]
    for x in xs[1:]:
        if x - last - 1 >= gap:
            out.append((x0 + int(s), x0 + int(last) + 1)); s = x
        last = x
    out.append((x0 + int(s), x0 + int(last) + 1))
    return [o for o in out if o[1] - o[0] >= minw]


def gap_histogram(gray, top, bot, x0, x1, ink, core=0.55):
    """Widths of every blank-column run inside the band's core rows (the evidence for or against a --groups gap)."""
    h = bot - top
    p = (gray[top + int(h * (1 - core) / 2):bot - int(h * (1 - core) / 2), x0:x1] < ink).sum(axis=0)
    xs = np.where(p > 0)[0]
    g = np.diff(xs) - 1
    return g[g > 0]


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
    ap.add_argument('--bottom-margin', type=int, default=0,
                     help='extra px included below each band\'s bottom edge (descenders of tall signs; NEVBIR-3252-B, '
                          '2 Oct 2026, fr.3252 f.117r), clamped to the region height')
    ap.add_argument('--quality', type=int, default=85, help='JPEG quality of the crops')
    ap.add_argument('--debug', action='store_true'); ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--groups', type=int, metavar='GAP',
                    help='also split each band into ink pieces at >= GAP blank columns (core rows only) and write one '
                         'crop per piece, <prefix>_Lnn_gNN.jpg, upscaled --group-upscale and padded; prints the piece '
                         'count and the blank-run histogram per band so a reader can see whether spacing separates '
                         'groups at all (MONT-CAL, 27 Sept 2026: on fr.4715 f.81r it does not)')
    ap.add_argument('--group-ink', type=int, default=120); ap.add_argument('--group-upscale', type=int, default=3)
    ap.add_argument('--group-lines', help='comma list of band numbers for --groups (default: all)')
    ap.add_argument('--follow-slope', type=int, metavar='WIN',
                    help='track each line through WIN-px column windows, fit its slope, and cut every segment as a '
                         'sheared strip centred on the line end to end (MONT-RECROP, 27 Sept 2026); off by default')
    ap.add_argument('--slope-local', action='store_true',
                    help='with --follow-slope, fit each segment to the peaks within one window of it (a curving line)')
    ap.add_argument('--slope-margin', type=int, default=0, help='extra px above and below a --follow-slope strip')
    ap.add_argument('--only-lines', help='comma list of band numbers to write crops for (default: all)')
    ap.add_argument('--centres', help='comma list of line centres (region y px) given by eye, skipping detection: for a '
                                      'short block whose ink profile the autocorrelation misreads (GAPS4-nevers-birago, 2 Oct 2026: '
                                      'three tall cipher lines under a prose tail read as pitch 100 and five lines)')
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
    if a.centres:
        centres = sorted(int(v) for v in a.centres.split(','))
        params = dict(pitch_autocorr=0, distance=0, prominence=0.0, centres_given=centres)
    else:
        centres, params = detect(gray, x0, x1, a.ink, a.smooth, a.distance, a.prominence)
    bb = bands(centres, im.height, a.lines_per_crop)
    if a.top_margin:
        bb = [(max(0, top - a.top_margin), bot, nl) for top, bot, nl in bb]
    if a.bottom_margin:
        bb = [(top, min(im.height, bot + a.bottom_margin), nl) for top, bot, nl in bb]
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
    only = {int(x) for x in a.only_lines.split(',')} if a.only_lines else None
    pitch = int(np.median(np.diff(centres))) if len(centres) > 1 else 100
    fits = {}
    rgbc = rgb.convert('RGB') if a.follow_slope else None
    for bi, (top, bot, nl) in enumerate(bb, 1):
        if only and bi not in only:
            continue
        if a.follow_slope:
            c = centres[(bi - 1) * a.lines_per_crop:(bi - 1) * a.lines_per_crop + nl]
            fa, fb, pts = track_line(gray, sum(c) / len(c), pitch, x0, x1, a.follow_slope, a.ink)
            half = (bot - top) // 2 + a.slope_margin
            fits[bi] = dict(a=round(fa, 2), b=round(fb, 5), peaks_kept=len(pts), half_height=half, win=a.follow_slope,
                            peaks=pts, local=a.slope_local)
            print(f'  band L{bi:02d}: slope fit y = {fa:.1f} + {fb:.5f}*x ({len(pts)} window peaks kept); '
                  f'drift over the region {fb * (x1 - x0):+.0f} px (pitch {pitch})')
        for si, (sx0, sx1) in enumerate(segs, 1):
            name = f'{prefix}_L{bi:02d}' + (f'_s{si}' if len(segs) > 1 else '') + '.jpg'
            if a.follow_slope:
                f = dict(fits[bi])
                if a.slope_local:
                    la, lb = local_fit(f['peaks'], sx0, sx1, a.follow_slope, f['a'], f['b'])
                    f.update(a=round(la, 2), b=round(lb, 5))
                crop = sheared_strip(rgbc, sx0, sx1, f['a'], f['b'], f['half_height'])
                ytop0, ytop1 = f['a'] + f['b'] * sx0 - f['half_height'], f['a'] + f['b'] * sx1 - f['half_height']
                box = [rx + sx0, ry + int(min(ytop0, ytop1)), rx + sx1, ry + int(max(ytop0, ytop1)) + 2 * f['half_height']]
                method = f'tools/iiif_lines.py row ink profile, --follow-slope {a.follow_slope} (sheared strip)'
            else:
                crop, box = rgb.crop((sx0, top, sx1, bot)), [rx + sx0, ry + top, rx + sx1, ry + bot]
                method = 'tools/iiif_lines.py row ink profile'
            crop.convert('RGB').save(os.path.join(a.out, name), quality=a.quality)
            e = dict(crop=name, source_url=url, source_file=os.path.basename(src), box=box, lines_in_crop=nl, band=bi,
                     segment=si, method=method, params=params, date=date)
            if a.follow_slope:
                e['slope_fit'] = {k: v for k, v in f.items() if k != 'peaks'}
            entries.append(e)
    if a.groups:
        want = {int(x) for x in a.group_lines.split(',')} if a.group_lines else None
        for bi, (top, bot, nl) in enumerate(bb, 1):
            if want and bi not in want:
                continue
            pieces = group_pieces(gray, top, bot, x0, x1, a.group_ink, a.groups)
            hist = np.bincount(np.minimum(gap_histogram(gray, top, bot, x0, x1, a.group_ink), 40), minlength=41)[1:]
            print(f'  band L{bi:02d}: {len(pieces)} pieces at gap >= {a.groups}; blank-run widths 1..40: '
                  + ' '.join(map(str, hist)))
            for gi, (gx0, gx1) in enumerate(pieces, 1):
                name = f'{prefix}_L{bi:02d}_g{gi:02d}.jpg'
                pad = 6
                c = rgb.crop((max(0, gx0 - pad), top, gx1 + pad, bot)).convert('RGB')
                c = c.resize((c.width * a.group_upscale, c.height * a.group_upscale), Image.LANCZOS)
                c.save(os.path.join(a.out, name), quality=a.quality)
                entries.append(dict(crop=name, source_url=url, source_file=os.path.basename(src),
                                    box=[rx + gx0, ry + top, rx + gx1, ry + bot], band=bi, group=gi,
                                    method=f'tools/iiif_lines.py --groups {a.groups} column ink profile', date=date))
            if a.debug:
                dbg = rgb.crop((x0, top, x1, bot)).convert('RGB')
                dd = ImageDraw.Draw(dbg)
                for gi, (gx0, gx1) in enumerate(pieces, 1):
                    dd.rectangle([gx0 - x0, 1, gx1 - x0, dbg.height - 2], outline=(255, 0, 0), width=2)
                    dd.text((gx0 - x0 + 2, 1), str(gi), fill=(0, 0, 255))
                dbg.save(os.path.join(a.out, f'{prefix}_L{bi:02d}_groups_debug.jpg'), quality=70)
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
    return dict(centres=centres, bands=bb, segments=segs, params=params, entries=entries, fits=fits)


if __name__ == '__main__':
    main()
