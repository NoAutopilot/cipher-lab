#!/usr/bin/env python3
"""VIV-CLS step 1 (PREREG-VIVCLS.md): pen-unit tiles for f.102r, f.103r and f.201r in ONE glyph_atlas directory.
TXE3-6's seg.py (benchmark-tx/txeng3/6/seg.py) generalised to three leaves: tools/glyph_atlas.py segment, default mode,
one page per line crop, --median-h pool; boxes mapped to line coordinates by the crop's manifest x0, the s1/s2 overlap
deduped at its midpoint, ordered by centre x; marks are not tokens. No truth is read.

  python3 ciphers/fr16104-vivonne-spain-1572/tx/vivcls/seg.py
Writes tx/vivcls/atlas/{signs.tsv,bitmaps.npz,...} and tx/vivcls/map_signs.tsv (sid, page=<leaf>, line=<n>, x=<line x>, w).
"""
import csv, json, os, subprocess, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__))
FOLD = os.path.abspath(os.path.join(HERE, '..', '..'))
REPO = os.path.abspath(os.path.join(FOLD, '..', '..'))
IMG = os.path.join(FOLD, 'images')
LEAVES = {'f102r': (os.path.join(IMG, 'manifest.json'), IMG),
          'f103r': (os.path.join(IMG, 'manifest.json'), IMG),
          'f201r': (os.path.join(IMG, 'p67/cut/manifest.json'), os.path.join(IMG, 'p67/cut'))}


def crops():
    out = {}
    for leaf, (man, d) in LEAVES.items():
        for e in json.load(open(man))['iiif_lines']:
            c = e['crop']
            if f'_{leaf}_L' not in c:
                continue
            ln = c.split('_')[2]
            seg = int(c.split('_s')[1].split('.')[0])
            out[(leaf, ln, seg)] = dict(path=os.path.join(d, c), x0=e['box'][0], x1=e['box'][2], page=f'{leaf}_{ln}_s{seg}')
    return out


def main():
    cr = crops()
    out = os.path.join(HERE, 'atlas')
    os.makedirs(out, exist_ok=True)
    pages = []
    for k, e in sorted(cr.items()):
        pages += ['--page', f"{e['page']}={e['path']}"]
    cmd = [sys.executable, os.path.join(REPO, 'tools/glyph_atlas.py'), 'segment', '--out', out, '--median-h', 'pool'] + pages
    log = subprocess.run(cmd, capture_output=True, text=True)
    if log.returncode:
        sys.exit(log.stdout + log.stderr)
    open(os.path.join(out, 'segment.log'), 'w').write(log.stdout[-4000:])
    rows = list(csv.DictReader(open(os.path.join(out, 'signs.tsv')), delimiter='\t'))
    byline = collections.defaultdict(list)
    for r in rows:
        leaf, ln, s = r['page'].split('_')
        seg = int(s[1:])
        e = cr[(leaf, ln, seg)]
        xc = e['x0'] + int(r['x']) + int(r['w']) / 2
        byline[(leaf, ln)].append(dict(r, seg=seg, xl=e['x0'] + int(r['x']), xc=xc))
    n = collections.Counter()
    with open(os.path.join(HERE, 'map_signs.tsv'), 'w') as f:
        f.write('sid\tpage\tline\tx\tw\tcrop_page\n')
        for (leaf, ln) in sorted(byline):
            segs = sorted({s for (l0, l2, s) in cr if (l0, l2) == (leaf, ln)})
            keep = []
            for b in byline[(leaf, ln)]:
                sg = b['seg']
                lo = -1e9 if sg == segs[0] else (cr[(leaf, ln, sg)]['x0'] + cr[(leaf, ln, sg - 1)]['x1']) / 2
                hi = 1e9 if sg == segs[-1] else (cr[(leaf, ln, sg + 1)]['x0'] + cr[(leaf, ln, sg)]['x1']) / 2
                if lo <= b['xc'] < hi:
                    keep.append(b)
            keep.sort(key=lambda b: b['xc'])
            for b in keep:
                f.write(f"{b['sid']}\t{leaf}\t{int(ln[1:])}\t{b['xl']}\t{b['w']}\t{b['page']}\n")
            n[leaf] += len(keep)
    print('tiles kept per leaf (pen units, overlap deduped):', dict(n), '; atlas rows', len(rows))


if __name__ == '__main__':
    main()
