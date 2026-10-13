#!/usr/bin/env python3
"""Re-derive the line crops under images/crops/ from openapi.bnf.fr (BAL167-SHRINK, 13 Oct 2026).

  python3 ciphers/baluze167-davaux-1637/regen_images.py --out DIR [--offline] [--check] [--only SRC_SUBSTR] [--overlays]

images/crops/manifest.json records, per crop, the source region (source_url, or for the --image runs only source_file,
named src_ark_12148_<ark>_f<canvas>_<x>_<y>_<w>_<h>.jpg) and the crop box. This script
  1. fetches each source region from openapi.bnf.fr (IIIF Image v3, {base}/{x,y,w,h}/max/0/default.jpg), one request at a
     time, >= 3 s apart, descriptive User-Agent, stop on any non-200 or non-JPEG (no retry loop); --offline reads the
     committed src_*.jpg in images/crops/ instead and fetches nothing;
  2. cuts every crop by its box (offset by the region origin when source_url is set; box is source-relative when it is
     empty) and saves it at JPEG quality 85, as tools/iiif_lines.py does;
  3. --check compares the sha1 of each regenerated crop with the committed one and exits 1 on any mismatch.
  --overlays also re-runs tools/iiif_lines.py --image <src> --debug for each prefix with the flags NOTES.md recorded, writing
  the *_lines_debug.jpg overlays (deleted by BAL167-SHRINK when no file cited them) into OUT/overlays; not byte-tested.

Tests run 13 Oct 2026: --offline --check 141/141 crops byte-identical (all crops whose src is committed); one
openapi.bnf.fr request (btv1b9001503k f510 2800,4330,880,200) returned a file sha1-identical to the committed src, and the
crop cut from it (b168f247end_L01.jpg) is sha1-identical. images/b170gloss/ is not covered: its natives were re-saved as
grayscale q80 by BAL-CROP (see images/b170gloss/manifest.json for the URLs), so a re-fetch matches in pixels, not bytes.
"""
import argparse, hashlib, io, json, os, re, subprocess, sys, time, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
CROPS = os.path.join(HERE, 'images', 'crops')
UA = 'cipher-lab research script (contact via repository)'
SRC_RE = re.compile(r'^src_ark_12148_(\w+?)_f(\d+)_(\d+)_(\d+)_(\d+)_(\d+)\.jpg$')
# Flags recorded in NOTES.md for each iiif_lines.py run (the overlay is the run's --debug output).
OVERLAY_FLAGS = {
    'b168f166': ['--top-margin', '60'],
    'b170f229r': ['--max-width', '2490', '--top-margin', '70'],
    'b170f229v': ['--max-width', '2490', '--top-margin', '70', '--centres',
                  '287,418,542,709,832,996,1142,1346,1575,1691,1887,2063,2197,2371,2558'],
}


def openapi_url(source_file):
    m = SRC_RE.match(source_file)
    if not m:
        sys.exit(f'cannot parse source file name {source_file}')
    ark, canvas, x, y, w, h = m.groups()
    return f'https://openapi.bnf.fr/iiif/image/v3/ark:/12148/{ark}/f{canvas}/{x},{y},{w},{h}/max/0/default.jpg', int(x), int(y)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--out', required=True)
    ap.add_argument('--offline', action='store_true', help='cut from the committed src_*.jpg; no network')
    ap.add_argument('--check', action='store_true', help='sha1-compare each regenerated crop with the committed file')
    ap.add_argument('--only', default='', help='only sources whose file name contains this string')
    ap.add_argument('--overlays', action='store_true', help='also re-run iiif_lines.py --debug for the overlays')
    a = ap.parse_args()
    from PIL import Image
    os.makedirs(a.out, exist_ok=True)
    entries = json.load(open(os.path.join(CROPS, 'manifest.json')))['iiif_lines']
    by_src = {}
    for e in entries:
        if a.only in e['source_file']:
            by_src.setdefault(e['source_file'], []).append(e)
    n_req = n_ok = n_bad = n_skip = 0
    prefixes = {}
    for sf, es in sorted(by_src.items()):
        url, rx, ry = openapi_url(sf)
        if a.offline:
            path = os.path.join(CROPS, sf)
            if not os.path.exists(path):
                print(f'skip {sf}: not committed (run without --offline to fetch it)')
                n_skip += len(es)
                continue
        else:
            path = os.path.join(a.out, sf)
            if not os.path.exists(path):
                if n_req:
                    time.sleep(3)
                n_req += 1
                body = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA}), timeout=300).read()
                if body[:3] != b'\xff\xd8\xff':
                    sys.exit(f'{url}: not a JPEG; stop, no retry. Log it in NOTES.md and ROOM.md.')
                open(path, 'wb').write(body)
        src = Image.open(path)
        for e in es:
            ox, oy = (rx, ry) if e['source_url'] else (0, 0)
            x0, y0, x1, y1 = e['box']
            buf = io.BytesIO()
            src.crop((x0 - ox, y0 - oy, x1 - ox, y1 - oy)).convert('RGB').save(buf, 'JPEG', quality=85)
            open(os.path.join(a.out, e['crop']), 'wb').write(buf.getvalue())
            prefixes.setdefault(re.sub(r'_L\d+.*$', '', e['crop']), path)
            committed = os.path.join(CROPS, e['crop'])
            if a.check and os.path.exists(committed):
                same = hashlib.sha1(buf.getvalue()).hexdigest() == hashlib.sha1(open(committed, 'rb').read()).hexdigest()
                n_ok += same
                n_bad += not same
                if not same:
                    print(f'MISMATCH {e["crop"]}')
    if a.overlays:
        od = os.path.join(a.out, 'overlays')
        for p, path in sorted(prefixes.items()):
            cmd = [sys.executable, os.path.join(HERE, '..', '..', 'tools', 'iiif_lines.py'), '--image', path, '--prefix', p,
                   '--out', od, '--debug'] + OVERLAY_FLAGS.get(p, [])
            subprocess.run(cmd, check=False, stdout=subprocess.DEVNULL)
    print(f'sources {len(by_src)}, openapi.bnf.fr requests {n_req}, crops skipped {n_skip}'
          + (f', check: {n_ok} identical, {n_bad} mismatched' if a.check else ''))
    sys.exit(1 if n_bad else 0)


if __name__ == '__main__':
    main()
