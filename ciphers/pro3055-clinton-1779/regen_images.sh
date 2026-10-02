#!/usr/bin/env bash
# Re-derive every image of ciphers/pro3055-clinton-1779/images from its source URL (AX2-SHRINK pattern,
# GAPS7-pro3055-clinton-1779, 2 Oct 2026). Writes into OUTDIR (default: ./regen_out beside this script), never into
# images/. Needs python3 with Pillow and numpy, curl.
#
#   bash ciphers/pro3055-clinton-1779/regen_images.sh [OUTDIR] [--only h1649|armylist1778|armylist|hmc|stevens1888]
#
# What it does, per images_manifest_full.tsv:
#   1. fetches every manifest entry that has a URL and is not marked deleted (canadiana needs a browser User-Agent
#      plus a Referer of the viewer page; archive.org a descriptive User-Agent), one request at a time, 1.6 s apart;
#      the H-1649 frames come back at the size their URL names (full/max, 1600, 1400, 1520 px), which is the
#      pre-shrink file: img827-829_full.jpg were re-encoded at quality 70 on 2 Oct 2026 (GAPS7) at the same
#      dimensions, so the re-fetched originals are the byte-identical pre-shrink files (tested on img829, sha256
#      b87f13f9...3765), and the w760 reference copies come back at 1520 px;
#   2. re-cuts every recorded crop from the re-fetched original by its manifest box: p186_text_region.jpg
#      (greyscale, box 1956,527,4090,3772, q90), p186_bottom_region.jpg (its lower 915 px, q90), p186_lines/*
#      (manifest boxes, q85, tools/iiif_lines.py's default), p184_cols/ and p185_cols/ (passes/cut_cipher_cols.py,
#      run on OUTDIR through CLINTON_H1649_DIR), p123_lines/* (Image 1205 full/max, polarity-inverted as the
#      committed crops are, manifest boxes, q85), p102_lines/* (Image 1183, same way, not inverted); p382_cols/, p385_lines/, p386_lines/ (Images 1030,
#      1033, 1034, GAPS8: greyscale, q70, manifest boxes);
#      the byte-identical tests run 2 Oct 2026 (GAPS7): img829_full.jpg, p186_text_region.jpg,
#      p186_bottom_region.jpg, p186_text_region_L01.jpg and all 28 p184/p185 column crops;
#   3. the HMC and Stevens pages come from archive.org _jp2.zip members and are converted to JPEG here, so they
#      regenerate the page, not the committed bytes (their original conversion settings were not recorded).
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
OUT="${1:-$HERE/regen_out}"
ONLY="${3:-}"
[ "${2:-}" = "--only" ] || ONLY=""
mkdir -p "$OUT"
export HERE OUT ONLY
python3 - <<'PY'
import io, json, os, subprocess, time
from PIL import Image, ImageOps
HERE, OUT, ONLY = os.environ['HERE'], os.environ['OUT'], os.environ.get('ONLY', '')
IMG = os.path.join(HERE, 'images')
BROWSER = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36'
DESC = 'cipher-lab research script (contact via repository)'
last = [0.0]

def fetch(url, dest, referer=None):
    if os.path.exists(dest):
        return dest
    wait = 1.6 - (time.time() - last[0])
    if wait > 0:
        time.sleep(wait)
    cmd = ['curl', '-sS', '-L', '-o', dest, '-w', '%{http_code}', '-A', BROWSER if referer else DESC]
    if referer:
        cmd += ['-e', referer]
    code = subprocess.run(cmd + [url], capture_output=True, text=True).stdout.strip()
    last[0] = time.time()
    print(code, url, '->', dest)
    if code != '200':
        raise SystemExit(f'fetch failed {code}: {url}')
    return dest

def save(im, path, q):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    im.save(path, 'JPEG', quality=q)

def recut(manifest, src_im, outdir, q=85, mode=None):
    for e in json.load(open(manifest))['iiif_lines']:
        x0, y0, x1, y1 = e['box']
        im = src_im.convert(mode) if mode else src_im
        save(im.crop((x0, y0, x1, y1)).convert('RGB'), os.path.join(outdir, e['crop']), q)

def want(sec):
    return not ONLY or ONLY == sec

if want('h1649'):
    m = json.load(open(os.path.join(IMG, 'h1649', 'manifest.json')))
    d = os.path.join(OUT, 'h1649'); os.makedirs(d, exist_ok=True)
    viewer = 'https://heritage.canadiana.ca/view/oocihm.lac_reel_h1649/{}'
    for f in m['files']:
        if f.get('deleted') or not f.get('url'):
            continue
        fetch(f['url'], os.path.join(d, f['file']), viewer.format(f['image']))
    full = Image.open(os.path.join(d, 'img829_full.jpg'))
    save(full.crop((1956, 527, 4090, 3772)).convert('L'), os.path.join(d, 'p186_text_region.jpg'), 90)
    reg = Image.open(os.path.join(d, 'p186_text_region.jpg'))
    save(reg.crop((0, 3245 - 915, 2134, 3245)), os.path.join(d, 'p186_bottom_region.jpg'), 90)
    for e in json.load(open(os.path.join(IMG, 'h1649', 'p186_lines', 'manifest.json')))['iiif_lines']:
        src = Image.open(os.path.join(d, e['source_file']))
        x0, y0, x1, y1 = e['box']
        save(src.crop((x0, y0, x1, y1)).convert('RGB'), os.path.join(d, 'p186_lines', e['crop']), 85)
    env = dict(os.environ, CLINTON_H1649_DIR=d)
    subprocess.run(['python3', os.path.join(HERE, 'passes', 'cut_cipher_cols.py')], check=True, env=env)
    for img, iiif, sub, invert, *qq in [(1205, 'c0ft8dg56944', 'p123_lines', True)] + \
            [tuple(x) for x in m.get('native_for_crops', [])]:
        man = os.path.join(IMG, 'h1649', sub, 'manifest.json')
        if not os.path.exists(man):
            continue
        src = fetch(f'https://image-uab.canadiana.ca/iiif/2/69429%2F{iiif}/full/max/0/default.jpg',
                    os.path.join(d, f'img{img}_native.jpg'), viewer.format(img))
        im = Image.open(src).convert('L')
        if invert:
            im = ImageOps.invert(im)
        entries = [e for e in json.load(open(man))['iiif_lines'] if 'box' in e]
        for e in entries:
            x0, y0, x1, y1 = e['box']
            save(im.crop((x0, y0, x1, y1)).convert('RGB'), os.path.join(d, sub, e['crop']), qq[0] if qq else 85)

if want('armylist1778'):
    m = json.load(open(os.path.join(IMG, 'armylist1778', 'manifest.json')))
    d = os.path.join(OUT, 'armylist1778'); os.makedirs(d, exist_ok=True)
    src = fetch('https://archive.org/download/listofgeneralfie00grea/page/n12.jpg', os.path.join(d, 'n12_native.jpg'))
    recut(os.path.join(IMG, 'armylist1778', 'lines', 'manifest.json'), Image.open(src), os.path.join(d, 'lines'))

if want('armylist'):
    d = os.path.join(OUT, 'armylist'); os.makedirs(d, exist_ok=True)
    src = fetch('https://archive.org/download/listofgeneralfie00grea_0/page/n4.jpg', os.path.join(d, 'n4.jpg'))
    im = Image.open(src)
    save(im.resize((1600, round(im.height * 1600 / im.width)), Image.LANCZOS).convert('RGB'),
         os.path.join(d, 'n4_w1600.jpg'), 78)
    recut(os.path.join(IMG, 'armylist', 'lines', 'manifest.json'), im, os.path.join(d, 'lines'))

for sec, key in [('hmc', 'images'), ('stevens1888', 'images')]:
    if not want(sec):
        continue
    m = json.load(open(os.path.join(IMG, sec, 'manifest.json')))
    d = os.path.join(OUT, sec); os.makedirs(d, exist_ok=True)
    for e in m[key]:
        url = e.get('url')
        if not url:
            ident = m.get('identifier')
            url = (f'https://archive.org/download/{ident}/{ident}_jp2.zip/{ident}_jp2%2F{ident}_{e["leaf"]:04d}.jp2')
        jp2 = fetch(url, os.path.join(d, e['file'].replace('.jpg', '.jp2')))
        save(Image.open(jp2).convert('RGB'), os.path.join(d, e['file']), 85)
print('regenerated into', OUT)
PY
