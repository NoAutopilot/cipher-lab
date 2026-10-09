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
     wide, renamed *_ref1600.jpg and marked so in the manifest (a later run refetches the native region); crops are never downscaled,
     and a src_*.jpg already committed to git is never touched (RUN3-ESSHR, 4 Oct 2026).
  --centres y1,y2,... gives the line centres (region y px) by eye and skips step 3, for a short block whose profile the
     autocorrelation misreads (check the --debug overlay first; GAPS4-nevers-birago, 2 Oct 2026).
  --debug writes OUT/<prefix>_lines_debug.jpg: the region at 1600 px wide with centres (red) and band edges (blue);
     with --follow-slope/--deskew also each segment's cut strip (green, mask margin included).
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
  --deskew [WIN] (SLANT-CROP, 5 Oct 2026): the --follow-slope fit, but the region is ROTATED about the line's centre so the
     line is level before the cut (marks keep their shape; a shear distorts it). Armstrong 1808 owner count page: 5 of 27
     axis-aligned boxes clipped an end mark and several took in numerals from the next line.
  --mask-neighbours [--mask-margin PX] [--mask-keep 0.5]: cut each crop PX taller above and below (default 0.4 x pitch)
     and white out (paper colour) each 8-connected ink component (pixels darker than --ink) with less than KEEP of its
     pixels inside the line band. Neighbour-line ink and bleed go; a mark of this line that reaches past the band edge is
     kept whole instead of clipped. Pixels are only removed, never added; the manifest records removed/kept counts.
     The removed components' 2 px rim goes too (TXE-B, 9 Oct 2026: their anti-aliased edges, lighter than --ink, had
     stayed as ghost outlines a reader could take for signs), and the fill is the local paper shade (mean of the
     non-ink pixels within 20 px), not one flat colour that left white silhouettes on shaded paper; ink of a kept
     component is never whitened.
  --band-extent [FRAC] (TXE-B, 9 Oct 2026; research/TX-TAXONOMY-2026-10-09.md class 2; do NOT use on a leaf with tight
     interlinear gloss rows: on fr.3623 f.23r the profile minimum sat out at the gloss rows, so the bands grew to hold the
     whole gloss line and --mask-neighbours kept it -- TXE2-RECUT, 9 Oct 2026; use midpoint bands there): after the centres are found,
     each band edge is moved from the midpoint between two centres to the row-profile minimum between them when that
     lies farther out, then grown FRAC x pitch further (default 0.1, never past the neighbouring centre), so this line's
     descenders and ascenders stay inside. Bands of neighbours then overlap; give --mask-neighbours with it so a grown
     band carries no neighbour-line ink. The manifest entry records band_extent (frac, band rows, height). Lesson:
     Birago no.87 (fr.3251 f.178v) fixed midpoint bands cut 14% of the hand's boxes top or bottom, error 9.5% on those
     against 5.2% inside, half the d/s confusions on cut descenders. Default 0.1 from the read-free gate on f178v (ink
     rule, with --mask-neighbours): FRAC 0.1 cut 0.6% / admitted 1.3%; 0.35 (the PREREG's first guess) admitted 34%.
  --check-boxes signs.tsv [--check-page NAME] [--check-only]: read-free band report against an atlas box file (columns
     sid, page, line, x, y, w, h; boxes in the coordinates of the source image the region is cut from, i.e. canvas
     minus the fetched region origin, as tools/tx_taxonomy.py load_geometry uses them; with --image and --region the
     region origin is subtracted). Each atlas line goes to the band whose centre is nearest its boxes. A box is CUT
     when its top or bottom lies outside its own band (with --mask-neighbours: outside the crop's rows, or less than
     --mask-keep of its height inside the band, so the mask would white it out); a box is ADMITTED to another band
     when at least --mask-keep of its height lies inside that band (box height stands in for the component's ink
     share). That box rule is a proxy; for fixed (unsloped) bands the report uses the INK rule instead: each band's
     crop (band +/- mask margin) is simulated on the page pixels, with the very component mask --mask-neighbours
     applies, and a box is CUT when under 90% of its ink pixels (darker than --ink) survive in its own band's crop,
     ADMITTED to another band when at least --mask-keep of its ink survives there (a detached descender stroke the
     mask would erase counts as cut here, which the box rule cannot see). Sloped bands (--follow-slope/--deskew) get the
     box rule, evaluated at the box's centre x on the fit the crop was cut on (whole-line, or with --slope-local the
     segment's local fit); the TSV's band_extent column names the rule.
     Printed and written to OUT/band_check.tsv (one row per band and a total). It never reads a transcription or a
     truth file; it is a dev gate for band parameters. --check-only (or --dry-run) writes no crops.
  --overlap-note: OUT/crops_note.md gets one line per prefix stating the real segment overlap in native px and in
     signs (median box width of the page from --check-boxes, else the median ink-run width of the band cores), to be
     pasted into a pass brief, never typed by hand (the Birago 1572 brief said "about 100 px at 2x" while the boxes
     overlapped 425 native px, 5-6 signs, and a reader de-duplicated by sequence and deleted 10 signs). --note-scale K
     states the pixels at the scale the reader sees (K=2 for crops upscaled 2x).
  --views N|LIST [--views-of CROP ...] (TX-VIEWS, 4 Oct 2026; research/TRANSCRIPTION-PRACTICE-2026-10-04.md #1, #10, #14):
     write altered views of every crop for multi-view voting, OUT/views/<view>/<crop name>, one manifest entry each under
     "iiif_lines_views". N takes the first N of the default order pad,s125,warp,s080,contrast; LIST names them. pad = the
     content shifted inside a background-coloured margin (left 8%, top 20%, right 2%, bottom 5% of the crop); s080 / s125 =
     LANCZOS rescale 0.8 / 1.25 (capped under 2500 px wide); warp = a small smooth elastic warp (random displacement on a
     coarse grid, about one control point per 90 px, amplitude 2.5 px, bilinearly upsampled; seeded from the crop name, so a
     re-run is byte-identical); contrast = a 1st-99th percentile luminance stretch. The pixels are the same information in
     every view: these are presentations for independent blind reads whose errors are less correlated, never enhancement
     claims. --views-of takes existing crop files (no fetch, no line detection) -- the usual way to add views to crops a
     target already has. Vote the reads with tools/reconcile_passes.py --vote [--err-truth].

Test: python3 tools/tests/test_iiif_lines.py (views: tools/tests/test_iiif_views.py) (offline: a synthetic page with a known line count and pitch, and the
committed native image of fr.20140 f.36r, whose box 1300,1770,3400,210 holds one cipher line).
"""
import argparse, json, os, re, subprocess, sys, time, urllib.error, urllib.request, zlib

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


def extent_bands(gray, x0, x1, centres, height, lines_per_crop, frac, ink=170):
    """--band-extent: band edges at the row-profile minimum between two centres when it lies farther out than the
    midpoint, plus frac x pitch, clamped to the neighbouring centre (and to the region). Returns bands like bands()."""
    if not centres:
        return []
    pitch = int(np.median(np.diff(centres))) if len(centres) > 1 else 100
    sm = max(1, pitch // 10)
    p = profile(gray, x0, x1, ink, sm)
    grow = int(round(frac * pitch))
    tops, bots = [], []
    for i, c in enumerate(centres):
        if i == 0:
            tops.append(max(0, c - pitch // 2 - grow))
        else:
            a, b = centres[i - 1], c
            mid = (a + b) // 2
            lo, hi = a + max(1, (b - a) // 4), b - max(1, (b - a) // 4)
            mn = lo + int(np.argmin(p[lo:hi])) if hi > lo else mid
            tops.append(max(a, min(mid, mn) - grow))
        if i == len(centres) - 1:
            bots.append(min(height, c + pitch // 2 + grow))
        else:
            a, b = c, centres[i + 1]
            mid = (a + b) // 2
            lo, hi = a + max(1, (b - a) // 4), b - max(1, (b - a) // 4)
            mn = lo + int(np.argmin(p[lo:hi])) if hi > lo else mid
            bots.append(min(b, max(mid, mn) + grow))
    out = []
    for i in range(0, len(centres), lines_per_crop):
        j = min(i + lines_per_crop, len(centres)) - 1
        out.append((tops[i], bots[j], j - i + 1))
    return out


def read_boxes(path, page, dx=0, dy=0):
    """Atlas boxes of one page: [(line, x, y, w, h)] with the region origin (dx, dy) subtracted."""
    import csv
    rows = []
    with open(path, newline='') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            if r.get('page') == page:
                rows.append((r['line'], int(float(r['x'])) - dx, int(float(r['y'])) - dy, int(float(r['w'])),
                             int(float(r['h']))))
    return rows


def band_geoms(bb, centres, lines_per_crop, fits, mm, segs=None):
    """Per band: functions of x giving (centre, band top, band bottom, crop top, crop bottom) in region rows. A sloped
    band with --slope-local uses, at x, the local fit of the segment whose middle is nearest x (the fit that crop was
    cut on)."""
    g = []
    for bi, (top, bot, nl) in enumerate(bb, 1):
        if fits and bi in fits:
            f = fits[bi]
            h = f['half_height']

            def fn(x, f=f, h=h):
                a_, b_ = f['a'], f['b']
                if f.get('local') and segs:
                    sx0, sx1 = min(segs, key=lambda s_: abs((s_[0] + s_[1]) / 2 - x))
                    a_, b_ = local_fit(f['peaks'], sx0, sx1, f['win'], a_, b_)
                y = a_ + b_ * x
                return y, y - h, y + h, y - h - mm, y + h + mm
            g.append(fn)
        else:
            c = centres[(bi - 1) * lines_per_crop:(bi - 1) * lines_per_crop + nl]
            cy = sum(c) / len(c)
            g.append(lambda x, cy=cy, t=top, b=bot: (cy, t, b, t - mm, b + mm))
    return g


def check_boxes(boxes, geoms, keep=0.5, masked=False):
    """Read-free band report: per band, own boxes cut and other-line boxes admitted (see --check-boxes in the doc).
    Returns (rows, total, line_to_band)."""
    by_line = {}
    for b in boxes:
        by_line.setdefault(b[0], []).append(b)
    l2b = {}
    for ln, bs in by_line.items():
        d = [np.median([abs(y + h / 2 - g(x + w / 2)[0]) for _, x, y, w, h in bs]) for g in geoms]
        l2b[ln] = int(np.argmin(d)) + 1 if d else None

    def inside(y, h, t, b):
        return max(0.0, min(y + h, b) - max(y, t)) / max(1, h)
    rows = {bi: dict(band=bi, lines=[], boxes=0, cut=0, admitted=0) for bi in range(1, len(geoms) + 1)}
    for ln, bi in l2b.items():
        rows[bi]['lines'].append(ln)
    n = cut = adm = 0
    for ln, x, y, w, h in boxes:
        own = l2b[ln]
        cx = x + w / 2
        _, t, b, vt, vb = geoms[own - 1](cx)
        if masked:
            c = inside(y, h, t, b) < keep or y < vt or y + h > vb
        else:
            c = y < t or y + h > b
        rows[own]['boxes'] += 1; n += 1
        if c:
            rows[own]['cut'] += 1; cut += 1
        hit = False
        for bi, g in enumerate(geoms, 1):
            if bi == own:
                continue
            _, t2, b2, _, _ = g(cx)
            if inside(y, h, t2, b2) >= keep:
                rows[bi]['admitted'] += 1; hit = True
        adm += hit
    total = dict(band='all', lines=sorted(l2b, key=lambda v: int(v) if str(v).isdigit() else 0), boxes=n, cut=cut,
                 admitted=adm)
    return [rows[k] for k in sorted(rows)], total, l2b


def check_ink(gray, boxes, bb, centres, lines_per_crop, x0, x1, ink, mm, keep, masked, l2b, cut_below=0.9, mrows=None):
    """Ink rule for fixed (unsloped) bands: simulate each band's crop on the page pixels -- rows band +/- mm, and with
    masked the same component mask as mask_neighbours() -- and count, per box, the share of its ink pixels (darker than
    ink, whole page) that survive in a band's crop. Own band: CUT when under cut_below survive. Other band: ADMITTED
    when at least keep survive. Returns (rows, total) like check_boxes()."""
    H = gray.shape[0]
    pm = gray < ink
    tot = [max(1, int(pm[max(0, y):max(0, y + h), max(0, x):max(0, x + w)].sum())) for _, x, y, w, h in boxes]
    rows = {bi: dict(band=bi, lines=[], boxes=0, cut=0, admitted=0) for bi in range(1, len(bb) + 1)}
    for ln, bi in l2b.items():
        rows[bi]['lines'].append(ln)
    surv = {}
    for bi, (top, bot, nl) in enumerate(bb, 1):
        ct, cb = max(0, top - mm), min(H, bot + mm)
        m = pm[ct:cb, x0:x1].copy()
        if masked:
            lab, n = label_components(m)
            if n:
                total = np.bincount(lab.ravel(), minlength=n + 1)
                mt, mb = mrows[bi - 1] if mrows else (top, bot)
                ins = np.bincount(lab[max(0, mt - ct):max(0, mb - ct)].ravel(), minlength=n + 1)
                drop = np.where((total > 0) & (ins < keep * total))[0]
                drop = drop[drop > 0]
                m[np.isin(lab, drop)] = False
        for k, (_, x, y, w, h) in enumerate(boxes):
            ya, yb = max(ct, y), min(cb, y + h)
            if yb <= ya:
                continue
            xa, xb = max(x0, x), min(x1, x + w)
            surv[(k, bi)] = int(m[ya - ct:yb - ct, xa - x0:xb - x0].sum()) / tot[k]
    n = cut = adm = 0
    for k, (ln, x, y, w, h) in enumerate(boxes):
        own = l2b[ln]
        rows[own]['boxes'] += 1; n += 1
        if surv.get((k, own), 0) < cut_below:
            rows[own]['cut'] += 1; cut += 1
        hit = False
        for bi in range(1, len(bb) + 1):
            if bi != own and surv.get((k, bi), 0) >= keep:
                rows[bi]['admitted'] += 1; hit = True
        adm += hit
    total = dict(band='all', lines=sorted(l2b, key=lambda v: int(v) if str(v).isdigit() else 0), boxes=n, cut=cut,
                 admitted=adm)
    return [rows[k] for k in sorted(rows)], total


def ink_run_width(gray, bb, x0, x1, ink, core=0.55):
    """Median width of ink runs along the core rows of every band (the sign-width fallback for --overlap-note)."""
    ws = []
    for top, bot, _ in bb:
        h = bot - top
        c0, c1 = top + int(h * (1 - core) / 2), bot - int(h * (1 - core) / 2)
        col = (gray[c0:c1, x0:x1] < ink).any(axis=0).astype(np.int8)
        d = np.diff(np.concatenate(([0], col, [0])))
        st, en = np.where(d == 1)[0], np.where(d == -1)[0]
        ws += [int(e - s_) for s_, e in zip(st, en) if e - s_ >= 3]
    return float(np.median(ws)) if ws else None


def overlap_sentence(segs, sign_w, src_w, scale=1.0):
    """One sentence for a pass brief: the actual overlap of neighbouring segments in native px and in signs."""
    if len(segs) < 2:
        return 'each line is one crop (no segments, no overlap).', 0
    ov = [segs[i][1] - segs[i + 1][0] for i in range(len(segs) - 1)]
    o = int(np.median(ov))
    k = o / sign_w if sign_w else None
    ks = f'about {k:.0f} signs (median sign width {sign_w:.0f} px, {src_w})' if k else 'sign width unknown'
    sc = f'{scale:g}x' if scale != 1 else 'native resolution'
    oi = int(round(o * scale))
    return (f'segments of a line overlap by {o} native px (the images you read are at {sc}, so {oi} px in each image), '
            f'{ks}; a sign at the right edge of s1 and the left edge of s2 is ONE sign: the last {oi} px of s1 and the '
            f'first {oi} px of s2 show the same ink, read it once.'), o


def write_note(out, prefix, sentence):
    p = os.path.join(out, 'crops_note.md')
    lines = []
    if os.path.exists(p):
        lines = [l for l in open(p).read().splitlines() if l.strip() and not l.startswith(f'- {prefix}: ')
                 and not l.startswith('# ')]
    lines.append(f'- {prefix}: {sentence}')
    with open(p, 'w') as f:
        f.write('# Crops note (written by tools/iiif_lines.py --overlap-note; paste after the pass brief)\n\n'
                + '\n'.join(lines) + '\n')
    return p


def write_band_check(out, prefix, rows, total, extent, masked):
    p = os.path.join(out, 'band_check.tsv')
    keep = []
    if os.path.exists(p):
        keep = [l for l in open(p).read().splitlines()[1:] if l and not l.startswith(prefix + '\t')]
    with open(p, 'w') as f:
        f.write('prefix\tband\tlines\tboxes\tcut\tcut_share\tadmitted\tadmitted_share\tband_extent\tmasked\n')
        for l in keep:
            f.write(l + '\n')
        for r in rows + [total]:
            nb = max(1, r['boxes'])
            f.write(f"{prefix}\t{r['band']}\t{','.join(map(str, r['lines']))}\t{r['boxes']}\t{r['cut']}\t"
                    f"{r['cut'] / nb:.3f}\t{r['admitted']}\t{r['admitted'] / nb:.3f}\t{extent}\t{int(masked)}\n")
    return p


def segments(x0, x1, max_width, overlap):
    w = x1 - x0
    if w <= max_width:
        return [(x0, x1)]
    n = int(np.ceil((w - overlap) / (max_width - overlap)))
    step = (w - max_width) / (n - 1)
    return [(x0 + int(round(i * step)), x0 + int(round(i * step)) + max_width) for i in range(n)]


def shift_segments(x0, x1, max_width, overlap, frac):
    """--shift-segments FRAC (TXE-N, 9 Oct 2026): the segment cut points (the middles of the overlaps of segments())
    moved right by FRAC x the segment step, the segments rebuilt around them with the same overlap, a shorter edge
    segment added where needed. FRAC 0 gives segments() back; 0.5 puts every new cut at the middle of an old segment,
    so a sign at an old segment edge is central in a new one."""
    base = segments(x0, x1, max_width, overlap)
    if len(base) < 2:
        return base
    step = base[1][0] - base[0][0]
    ov = base[0][1] - base[1][0]
    cut0 = (base[0][1] + base[1][0]) / 2 - step + (frac % 1.0) * step
    cuts, c = [], cut0
    while c < x1:
        if c > x0 + ov / 2 and c < x1 - ov / 2:
            cuts.append(c)
        c += step
    edges = [x0] + cuts + [x1]
    out = []
    for i in range(len(edges) - 1):
        a = x0 if i == 0 else int(round(edges[i] - ov / 2))
        b = x1 if i == len(edges) - 2 else int(round(edges[i + 1] + ov / 2))
        out.append((a, b))
    return out


def shift_bands(bb, frac, pitch, height):
    """--shift-bands FRAC (TXE-N): every band moved down by FRAC x pitch (clamped to the region). Returns (shifted
    bands, mask rows): with --mask-neighbours a shifted crop keeps the components of its own line and of the next one
    whole (mask rows = own band top .. next band bottom), so the marked line is never masked away at the band edge."""
    s = int(round(frac * pitch))
    out, mrows = [], []
    for i, (top, bot, nl) in enumerate(bb):
        out.append((min(height, top + s), min(height, bot + s), nl))
        nb = bb[i + 1][1] if i + 1 < len(bb) else min(height, bot + s)
        mrows.append((top, max(nb, min(height, bot + s))))
    return out, mrows


def mark_crop(crop, y, pad=40):
    """A white left margin of pad px with a red triangle pointing at row y: the line the reader transcribes (TXE-N)."""
    c = crop.convert('RGB')
    out = Image.new('RGB', (c.width + pad, c.height), (255, 255, 255))
    out.paste(c, (pad, 0))
    d = ImageDraw.Draw(out)
    h = max(6, pad // 3)
    d.polygon([(4, y - h), (pad - 6, y), (4, y + h)], fill=(220, 0, 0))
    return out


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


def deskewed_strip(img, sx0, sx1, a, b, half):
    """--deskew: rotate the region about the line's centre point (x mid-segment, y = a + b*x) by atan(b), so the
    fitted line is horizontal, then cut columns sx0..sx1 and rows centre +/- half. A rotation, not a shear: marks keep
    their own shape and slant, which a sheared strip distorts in proportion to the slope."""
    cx = (sx0 + sx1) / 2
    cy = a + b * cx
    fill = 255 if img.mode == 'L' else (255, 255, 255)
    pad = int(abs(b) * (sx1 - sx0) / 2) + half + 4
    y0, y1 = int(cy) - pad, int(cy) + pad
    win = img.crop((sx0 - pad, y0, sx1 + pad, y1))      # PIL pads out-of-image areas with black; fill below
    if win.mode != 'L':
        win = win.convert('RGB')
    inside = Image.new('L', win.size, 0)
    ImageDraw.Draw(inside).rectangle([max(0, -(sx0 - pad)), max(0, -y0), min(win.width, img.width - (sx0 - pad)) - 1,
                                      min(win.height, img.height - y0) - 1], fill=255)
    bg = Image.new(win.mode, win.size, fill)
    win = Image.composite(win, bg, inside)
    deg = float(np.degrees(np.arctan(b)))
    rot = win.rotate(deg, center=(cx - (sx0 - pad), cy - y0), resample=Image.BICUBIC, fillcolor=fill)
    top = int(round(cy - y0)) - half
    return rot.crop((pad, top, pad + (sx1 - sx0), top + 2 * half)), deg


def label_components(mask):
    """8-connected components of a boolean array, by run-length union-find (numpy, no scipy). Returns (labels, n):
    int32 array the shape of mask, 0 = background, 1..n = components."""
    h, w = mask.shape
    runs = []                                            # (row, x0, x1 exclusive)
    row_runs = []
    for y in range(h):
        r = mask[y]
        if not r.any():
            row_runs.append([]); continue
        d = np.diff(np.concatenate(([0], r.view(np.int8), [0])))
        st, en = np.where(d == 1)[0], np.where(d == -1)[0]
        ids = []
        for s_, e_ in zip(st, en):
            ids.append(len(runs)); runs.append((y, int(s_), int(e_)))
        row_runs.append(ids)
    parent = list(range(len(runs)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]; i = parent[i]
        return i
    for y in range(1, h):
        prev, cur = row_runs[y - 1], row_runs[y]
        i = j = 0
        while i < len(prev) and j < len(cur):
            _, ps, pe = runs[prev[i]]; _, cs, ce = runs[cur[j]]
            if ps <= ce and pe >= cs:                    # overlap incl. diagonal touch (8-connectivity)
                ra, rb = find(prev[i]), find(cur[j])
                if ra != rb:
                    parent[ra] = rb
            if pe < ce:
                i += 1
            else:
                j += 1
    lab = np.zeros((h, w), np.int32)
    ids = {}
    for k, (y, s_, e_) in enumerate(runs):
        root = find(k)
        lab[y, s_:e_] = ids.setdefault(root, len(ids) + 1)
    return lab, len(ids)


def _dilate(m, r):
    """Boolean dilation by r px (square), numpy shifts only."""
    out = m.copy()
    h, w = m.shape
    for dy in range(-r, r + 1):
        for dx in range(-r, r + 1):
            if dy or dx:
                out[max(0, dy):h + min(0, dy), max(0, dx):w + min(0, dx)] |= \
                    m[max(0, -dy):h + min(0, -dy), max(0, -dx):w + min(0, -dx)]
    return out


def _box_sum(a, r):
    """Sum over a (2r+1)^2 window, edges clipped (cumulative sums, numpy only)."""
    c = np.pad(a, ((r + 1, r), (r + 1, r))).cumsum(0).cumsum(1)
    return c[2 * r + 1:, 2 * r + 1:] - c[:-2 * r - 1, 2 * r + 1:] - c[2 * r + 1:, :-2 * r - 1] + c[:-2 * r - 1, :-2 * r - 1]


def local_paper(arr, ink_mask, r=20):
    """Per-pixel paper colour: the mean of the non-ink pixels within r px (normalised box filter), so a whited-out
    stroke takes the shade of the paper around it instead of one flat colour that leaves a silhouette."""
    ok = (~ink_mask).astype(float)
    n = _box_sum(ok, r)
    out = np.empty(arr.shape, float)
    flat = np.median(arr[~ink_mask], axis=0) if (~ink_mask).any() else np.array([255.0, 255.0, 255.0])
    for ch in range(arr.shape[2]):
        sm = _box_sum(arr[..., ch] * ok, r)
        out[..., ch] = np.where(n > 0, sm / np.maximum(n, 1), flat[ch])
    return out


def mask_neighbours(crop, band_top, band_bot, ink, keep=0.5, halo=2):
    """--mask-neighbours: white out (paper colour) every ink component of the crop whose share of pixels inside rows
    band_top..band_bot is below KEEP -- ink belonging to the line above or below that the crop's margin took in.
    A component mostly inside the band is kept whole, including the parts that reach into the margin (a tall mark of
    this line is not clipped). Returns (crop, components removed, components kept)."""
    rgb = crop.convert('RGB')
    arr = np.asarray(rgb).copy()
    gray = np.asarray(rgb.convert('L'))
    m = gray < ink
    lab, n = label_components(m)
    if not n:
        return rgb, 0, 0
    total = np.bincount(lab.ravel(), minlength=n + 1)
    inside = np.bincount(lab[max(0, band_top):max(0, band_bot)].ravel(), minlength=n + 1)
    drop = np.where((total > 0) & (inside < keep * total))[0]
    drop = drop[drop > 0]
    if len(drop):
        gone = np.isin(lab, drop)
        if halo:      # the anti-aliased rim of a removed stroke is lighter than --ink and would stay as a ghost outline
            gone = _dilate(gone, halo) & ~(m & ~gone)     # (TXE-B, 9 Oct 2026); kept components' ink is never touched
        paper = local_paper(arr.astype(float), _dilate(m, halo) if halo else m)
        arr[gone] = np.clip(paper[gone], 0, 255).astype(np.uint8)
    return Image.fromarray(arr), int(len(drop)), int(n - len(drop))


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


def git_tracked(path):
    """True when PATH is committed in a git checkout. The 30 MB guard never downscales a tracked src_* copy: doing so
    deleted committed native references in a worktree (RUN3-ES41, 4 Oct 2026) and left the manifest naming *_ref1600
    files that were later restored to their native names; shrink a committed folder the AX2-SHRINK way instead."""
    try:
        return subprocess.run(['git', 'ls-files', '--error-unmatch', os.path.basename(path)], cwd=os.path.dirname(os.path.abspath(path)),
                              stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0
    except OSError:
        return False


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

VIEW_ORDER = ('pad', 's125', 'warp', 's080', 'contrast')


def _background(arr):
    edge = np.concatenate([arr[0].reshape(-1, arr.shape[-1]), arr[-1].reshape(-1, arr.shape[-1]),
                           arr[:, 0].reshape(-1, arr.shape[-1]), arr[:, -1].reshape(-1, arr.shape[-1])])
    return tuple(int(v) for v in np.median(edge, axis=0))


def _bilinear(arr, yy, xx):
    h, w = arr.shape[:2]
    xx = np.clip(xx, 0, w - 1.001); yy = np.clip(yy, 0, h - 1.001)
    x0 = np.floor(xx).astype(int); y0 = np.floor(yy).astype(int)
    fx = (xx - x0)[..., None]; fy = (yy - y0)[..., None]
    a = arr.astype(np.float32)
    top = a[y0, x0] * (1 - fx) + a[y0, x0 + 1] * fx
    bot = a[y0 + 1, x0] * (1 - fx) + a[y0 + 1, x0 + 1] * fx
    return np.clip(top * (1 - fy) + bot * fy + 0.5, 0, 255).astype(np.uint8)


def make_view(img, view, seed=0):
    """One altered view of a crop (PIL RGB in, PIL RGB out); see --views in the module docstring."""
    img = img.convert('RGB')
    w, h = img.size
    if view == 'pad':
        l, t, r, b = int(0.08 * w), int(0.20 * h), int(0.02 * w), int(0.05 * h)
        out = Image.new('RGB', (w + l + r, h + t + b), _background(np.asarray(img)))
        out.paste(img, (l, t))
        return out
    if view in ('s080', 's125'):
        f = 0.8 if view == 's080' else 1.25
        nw_ = min(int(round(w * f)), 2499)
        f = nw_ / w
        return img.resize((nw_, max(1, int(round(h * f)))), Image.LANCZOS)
    if view == 'warp':
        rng = np.random.default_rng(seed)
        gx, gy = max(2, w // 90 + 1), max(2, h // 90 + 1)
        fields = []
        for _ in range(2):
            g = rng.normal(0, 2.5, (gy, gx)).astype(np.float32)
            fields.append(np.asarray(Image.fromarray(g, mode='F').resize((w, h), Image.BILINEAR)))
        yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
        return Image.fromarray(_bilinear(np.asarray(img), yy + fields[1], xx + fields[0]))
    if view == 'contrast':
        a = np.asarray(img).astype(np.float32)
        lum = a.mean(axis=2)
        lo, hi = np.percentile(lum, 1), np.percentile(lum, 99)
        if hi - lo < 1:
            return img.copy()
        return Image.fromarray(np.clip((a - lo) * 255.0 / (hi - lo), 0, 255).astype(np.uint8))
    raise ValueError(f'unknown view {view!r} (known: {", ".join(VIEW_ORDER)})')


def parse_views(spec):
    if spec is None:
        return []
    if spec.isdigit():
        n = int(spec)
        if not 1 <= n <= len(VIEW_ORDER):
            raise ValueError(f'--views N must be 1..{len(VIEW_ORDER)}')
        return list(VIEW_ORDER[:n])
    vs = [v.strip() for v in spec.split(',') if v.strip()]
    for v in vs:
        if v not in VIEW_ORDER:
            raise ValueError(f'unknown view {v!r} (known: {", ".join(VIEW_ORDER)})')
    return vs


def write_views(crop_paths, views, out, quality=85):
    """Write OUT/views/<view>/<name> for every crop and view; returns manifest entries."""
    entries, date = [], time.strftime('%d %b %Y', time.gmtime())
    for p in crop_paths:
        name = os.path.basename(p)
        im = Image.open(p)
        for v in views:
            d = os.path.join(out, 'views', v)
            os.makedirs(d, exist_ok=True)
            vi = make_view(im, v, seed=zlib.crc32(name.encode()))
            vi.save(os.path.join(d, name), quality=quality)
            entries.append(dict(crop=f'views/{v}/{name}', view=v, from_crop=os.path.relpath(p, out), size=list(vi.size),
                                method=f'tools/iiif_lines.py --views {v}', date=date))
    return entries


def update_views_manifest(out, entries):
    path = os.path.join(out, 'manifest.json')
    man = json.load(open(path, encoding='utf-8')) if os.path.exists(path) else {}
    if isinstance(man, list):
        man = {'entries': man}
    cur = [e for e in man.get('iiif_lines_views', []) if e['crop'] not in {x['crop'] for x in entries}]
    man['iiif_lines_views'] = cur + entries
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
    ap.add_argument('--deskew', type=int, nargs='?', const=200, metavar='WIN',
                    help='track each line through WIN-px windows (default 200), fit its slope and ROTATE the region so '
                         'the line is level before cutting (SLANT-CROP, 5 Oct 2026); exclusive with --follow-slope')
    ap.add_argument('--mask-neighbours', action='store_true',
                    help='cut each crop --mask-margin px taller above and below and white out every ink component that '
                         'lies mostly (share inside < --mask-keep) outside the line band: neighbour-line ink goes, '
                         'this line\'s tall marks stay whole (SLANT-CROP, 5 Oct 2026)')
    ap.add_argument('--mask-margin', type=int, help='with --mask-neighbours: extra px above and below (default 0.4 x pitch)')
    ap.add_argument('--mask-keep', type=float, default=0.5, help='with --mask-neighbours: share of a component that must '
                                                                  'lie inside the band for it to be kept (default 0.5)')
    ap.add_argument('--band-extent', type=float, nargs='?', const=0.1, metavar='FRAC',
                    help='grow each band edge from the midpoint to the row-profile minimum plus FRAC x pitch (default '
                         '0.1; 0.35 admitted 34%% of other-line boxes on f178v) so descenders stay inside; use with '
                         '--mask-neighbours (TXE-B, 9 Oct 2026)')
    ap.add_argument('--check-boxes', metavar='SIGNS_TSV',
                    help='read-free report: share of atlas boxes cut by their own band and admitted to another band; '
                         'written to OUT/band_check.tsv (TXE-B)')
    ap.add_argument('--check-page', help='with --check-boxes: the page name in the box file (default: --prefix)')
    ap.add_argument('--check-only', action='store_true', help='with --check-boxes: report only, write no crops')
    ap.add_argument('--overlap-note', action='store_true',
                    help='write the real segment overlap (native px and signs) to OUT/crops_note.md for the pass brief')
    ap.add_argument('--note-scale', type=float, default=1.0,
                    help='with --overlap-note: the scale the reader sees the crops at (2 when they are upscaled 2x, as '
                         'harvest/make_2x.py does), so the note gives pixels in the reader\'s images')
    ap.add_argument('--shift-bands', type=float, metavar='FRAC',
                    help='move every band down by FRAC x pitch (0.5: bands centred on the gaps), keep the own line and '
                         'the next one whole under --mask-neighbours, and mark the own line with a red triangle in a '
                         'white left margin: a second crop set where each sign sits at a band edge instead of the '
                         'centre (TXE-N, M20, 9 Oct 2026)')
    ap.add_argument('--shift-segments', type=float, metavar='FRAC',
                    help='move every segment cut point right by FRAC x the segment step (0.5: new cuts at the middles '
                         'of the old segments), adding a shorter edge segment (TXE-N)')
    ap.add_argument('--only-lines', help='comma list of band numbers to write crops for (default: all)')
    ap.add_argument('--centres', help='comma list of line centres (region y px) given by eye, skipping detection: for a '
                                      'short block whose ink profile the autocorrelation misreads (GAPS4-nevers-birago, 2 Oct 2026: '
                                      'three tall cipher lines under a prose tail read as pitch 100 and five lines)')
    ap.add_argument('--views', help='N or a comma list of pad,s125,warp,s080,contrast: also write altered views of '
                                    'every crop to OUT/views/<view>/ for multi-view voting (TX-VIEWS)')
    ap.add_argument('--views-of', nargs='+', metavar='CROP',
                    help='with --views: make views of these existing crop files only (no fetch, no line detection)')
    a = ap.parse_args(argv)
    try:
        views = parse_views(a.views)
    except ValueError as e:
        ap.error(str(e))
    if a.views_of:
        if not views:
            ap.error('--views-of needs --views')
        os.makedirs(a.out, exist_ok=True)
        ve = write_views(a.views_of, views, a.out, a.quality)
        mp = update_views_manifest(a.out, ve)
        print(f'  wrote {len(ve)} views ({",".join(views)}) of {len(a.views_of)} crops under {a.out}/views and {mp}')
        return dict(views=ve)
    if a.deskew and a.follow_slope:
        ap.error('--deskew and --follow-slope are alternatives (rotate vs shear); give one')
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
    if a.band_extent is not None:
        bb = extent_bands(gray, x0, x1, centres, im.height, a.lines_per_crop, a.band_extent, a.ink)
    else:
        bb = bands(centres, im.height, a.lines_per_crop)
    if a.top_margin:
        bb = [(max(0, top - a.top_margin), bot, nl) for top, bot, nl in bb]
    if a.bottom_margin:
        bb = [(top, min(im.height, bot + a.bottom_margin), nl) for top, bot, nl in bb]
    mrows = None
    if a.shift_bands:
        if a.deskew or a.follow_slope:
            ap.error('--shift-bands is for fixed bands (not --deskew / --follow-slope)')
        pitch0 = int(np.median(np.diff(centres))) if len(centres) > 1 else 100
        bb, mrows = shift_bands(bb, a.shift_bands, pitch0, im.height)
    segs = (shift_segments(x0, x1, a.max_width, a.overlap, a.shift_segments) if a.shift_segments
            else segments(x0, x1, a.max_width, a.overlap))
    print(f'{src} ({how}): region {im.width}x{im.height}, {len(centres)} lines, {len(bb)} bands x {len(segs)} segments; '
          f"pitch {params['pitch_autocorr']} distance {params['distance']} prominence {params['prominence']}")
    print('  centres (region y): ' + ' '.join(map(str, centres)))
    pitch = int(np.median(np.diff(centres))) if len(centres) > 1 else 100
    only = {int(x) for x in a.only_lines.split(',')} if a.only_lines else None
    slope_win = a.follow_slope or a.deskew
    mm = (a.mask_margin if a.mask_margin is not None else int(0.4 * pitch)) if a.mask_neighbours else 0
    fits = {}
    if slope_win:
        for bi, (top, bot, nl) in enumerate(bb, 1):
            if only and bi not in only and not a.check_boxes:
                continue
            c = centres[(bi - 1) * a.lines_per_crop:(bi - 1) * a.lines_per_crop + nl]
            fa, fb, pts = track_line(gray, sum(c) / len(c), pitch, x0, x1, slope_win, a.ink)
            half = (bot - top) // 2 + a.slope_margin
            if a.band_extent is not None:      # a grown band is asymmetric about its centre; the strip is symmetric
                cc = sum(c) / len(c)           # about the fit, so it takes the larger reach of the two
                half = int(np.ceil(max(cc - top, bot - cc))) + a.slope_margin

            fits[bi] = dict(a=round(fa, 2), b=round(fb, 5), peaks_kept=len(pts), half_height=half, win=slope_win,
                            peaks=pts, local=a.slope_local)
            print(f'  band L{bi:02d}: slope fit y = {fa:.1f} + {fb:.5f}*x ({len(pts)} window peaks kept); '
                  f'drift over the region {fb * (x1 - x0):+.0f} px (pitch {pitch})')
    check = None
    sign_w, src_w = None, ''
    if a.check_boxes:
        page = a.check_page or prefix
        boxes = read_boxes(a.check_boxes, page, rx if a.image and a.region else 0, ry if a.image and a.region else 0)
        if not boxes:
            ap.error(f'--check-boxes: no boxes for page {page!r} in {a.check_boxes}')
        rows, total, l2b = check_boxes(boxes, band_geoms(bb, centres, a.lines_per_crop, fits, mm, segs), a.mask_keep,
                                       a.mask_neighbours)
        ext = a.band_extent if a.band_extent is not None else 'off'
        mtxt = 'on (margin ' + str(mm) + ')' if a.mask_neighbours else 'off'
        nb = max(1, total['boxes'])
        box_line = (f"box rule: cut {total['cut']} ({total['cut'] / nb:.1%}), admitted to another band "
                    f"{total['admitted']} ({total['admitted'] / nb:.1%})")
        rule = 'box'
        if not slope_win:
            rows, total = check_ink(gray, boxes, bb, centres, a.lines_per_crop, x0, x1, a.ink, mm, a.mask_keep,
                                    a.mask_neighbours, l2b, mrows=mrows)
            rule = 'ink'
        bc = write_band_check(a.out, prefix, rows, total, f'{ext};rule={rule}', a.mask_neighbours)
        print(f"  check-boxes {page}: {total['boxes']} boxes, {rule} rule: cut {total['cut']} "
              f"({total['cut'] / nb:.1%}), admitted to another band {total['admitted']} "
              f"({total['admitted'] / nb:.1%}); band-extent {ext}, mask {mtxt} -> {bc}")
        if rule == 'ink':
            print(f'    (proxy {box_line})')
        for r in rows:
            if r['cut'] or r['admitted']:
                print(f"    L{r['band']:02d} (atlas line {','.join(map(str, r['lines']))}): {r['boxes']} boxes, cut "
                      f"{r['cut']}, admitted {r['admitted']}")
        check = dict(rows=rows, total=total, line_to_band=l2b, file=bc, rule=rule)
        sign_w, src_w = float(np.median([b[3] for b in boxes])), 'from the atlas boxes'
    if a.overlap_note:
        if sign_w is None:
            sign_w, src_w = ink_run_width(gray, bb, x0, x1, a.ink), 'ink-run median'
        sent, ov = overlap_sentence(segs, sign_w, src_w, a.note_scale)
        if a.shift_bands:
            mp_ = int(round(40 * a.note_scale))
            sent += (f' Each crop shows parts of two lines: transcribe ONLY the line marked by the red triangle in the '
                     f'white left margin ({mp_} px wide in each image), along its full length; the other line is read '
                     f'from its own crop. The overlap above is measured after that margin.')
        np_ = write_note(a.out, prefix, sent)
        print(f'  overlap note -> {np_}: {sent}')
    if a.dry_run or a.check_only:
        return dict(centres=centres, bands=bb, segments=segs, params=params, check=check, fits=fits)
    rgb = Image.open(src)
    if a.image and a.region:
        rgb = rgb.crop((rx, ry, rx + rw, ry + rh))
    entries = []
    date = time.strftime('%d %b %Y', time.gmtime())
    rgbc = rgb.convert('RGB') if slope_win else None
    for bi, (top, bot, nl) in enumerate(bb, 1):
        if only and bi not in only:
            continue
        for si, (sx0, sx1) in enumerate(segs, 1):
            name = f'{prefix}_L{bi:02d}' + (f'_s{si}' if len(segs) > 1 else '') + '.jpg'
            extra = {}
            if slope_win:
                f = dict(fits[bi])
                if a.slope_local:
                    la, lb = local_fit(f['peaks'], sx0, sx1, slope_win, f['a'], f['b'])
                    f.update(a=round(la, 2), b=round(lb, 5))
                hh = f['half_height'] + mm
                if a.deskew:
                    crop, deg = deskewed_strip(rgbc, sx0, sx1, f['a'], f['b'], hh)
                    extra['deskew_deg'] = round(deg, 3)
                    method = f'tools/iiif_lines.py row ink profile, --deskew {a.deskew} (rotated)'
                else:
                    crop = sheared_strip(rgbc, sx0, sx1, f['a'], f['b'], hh)
                    method = f'tools/iiif_lines.py row ink profile, --follow-slope {a.follow_slope} (sheared strip)'
                ytop0, ytop1 = f['a'] + f['b'] * sx0 - hh, f['a'] + f['b'] * sx1 - hh
                box = [rx + sx0, ry + int(min(ytop0, ytop1)), rx + sx1, ry + int(max(ytop0, ytop1)) + 2 * hh]
                band_rows = (mm, mm + 2 * f['half_height'])
            else:
                ct, cb = max(0, top - mm), min(im.height, bot + mm)
                crop, box = rgb.crop((sx0, ct, sx1, cb)), [rx + sx0, ry + ct, rx + sx1, ry + cb]
                method = 'tools/iiif_lines.py row ink profile'
                band_rows = (top - ct, bot - ct)
            if a.mask_neighbours and mrows and not slope_win:
                band_rows = (mrows[bi - 1][0] - ct, mrows[bi - 1][1] - ct)
            if a.mask_neighbours:
                crop, ndrop, nkeep = mask_neighbours(crop, band_rows[0], band_rows[1], a.ink, a.mask_keep)
                extra['mask'] = dict(margin=mm, keep=a.mask_keep, band_rows=list(band_rows), removed=ndrop, kept=nkeep)
                method += f', --mask-neighbours (margin {mm})'
            if a.shift_bands:
                c = centres[(bi - 1) * a.lines_per_crop:(bi - 1) * a.lines_per_crop + nl]
                my = int(round(sum(c) / len(c))) - ct
                crop = mark_crop(crop, my)
                extra['marked'] = dict(line_centre_row=my, margin_px=40, shift_bands=a.shift_bands,
                                       note='crop x = source x - box[0] + 40 (white margin with the marker)')
            if a.shift_segments:
                extra['shift_segments'] = a.shift_segments
            crop.convert('RGB').save(os.path.join(a.out, name), quality=a.quality)
            e = dict(crop=name, source_url=url, source_file=os.path.basename(src), box=box, lines_in_crop=nl, band=bi,
                     segment=si, method=method, params=params, date=date)
            if slope_win:
                e['slope_fit'] = {k: v for k, v in f.items() if k != 'peaks'}
            if a.band_extent is not None:
                e['band_extent'] = dict(frac=a.band_extent, band_rows=[top, bot], height=bot - top)
            e.update(extra)
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
        for bi, f in fits.items():        # sloped cuts: the strip each segment was cut on, in green (TXE-B)
            for sx0, sx1 in segs:
                fa, fb = (local_fit(f['peaks'], sx0, sx1, f['win'], f['a'], f['b']) if f.get('local')
                          else (f['a'], f['b']))
                for off in (-f['half_height'] - mm, f['half_height'] + mm):
                    d.line([(sx0 * scale, (fa + fb * sx0 + off) * scale), (sx1 * scale, (fa + fb * sx1 + off) * scale)],
                           fill=(0, 170, 0), width=1)
        dbg.save(os.path.join(a.out, f'{prefix}_lines_debug.jpg'), quality=70)
    shrunk = []
    if folder_size(a.out) > LIMIT:
        for f in sorted(os.listdir(a.out)):
            if f.startswith('src_') and f.endswith('.jpg'):
                p = os.path.join(a.out, f)
                r = Image.open(p)
                if r.width > 1600 and not f.endswith('_ref1600.jpg') and not git_tracked(p):
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
    if views:
        ve = write_views([os.path.join(a.out, e['crop']) for e in entries], views, a.out, a.quality)
        update_views_manifest(a.out, ve)
        print(f'  wrote {len(ve)} views ({",".join(views)}) under {a.out}/views')
    return dict(centres=centres, bands=bb, segments=segs, params=params, entries=entries, fits=fits, check=check)


if __name__ == '__main__':
    main()
