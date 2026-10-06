#!/usr/bin/env python3
"""Turn Thorsten Rotering's 2015 partial transcription PDF (Cylob-Manuskript.pdf) into ciphertext.tsv.

Usage: rotering_to_tsv.py BBOX_HTML [--out ciphertext.tsv] [--check]
  BBOX_HTML is `pdftotext -bbox Cylob-Manuskript.pdf bb.html` of the PDF whose sha256 is
  0f9deae8ef6b313a2087cc3be944bfeea964afc80c334943a5d94bd351232082 (not committed: third-party file, licence unknown;
  fetch from the cloud.rotering-net.de share named in NOTES.md). --check exits 1 if the committed TSV differs.
Layout read from the word boxes: each PDF page after the table is one booklet page or spread ("Seite a/b"); words left
of the gutter (x < 297.6 pt) belong to page a, right of it to page b; a single page uses the whole width. Rows are
grouped by yMin; a row's column is the letter's x rank among that page's column x positions. A one-letter row at the
top of a page (before any picture or grid row) is the page's header sign (row 0, kind=header); "[Abbildung]" is a
picture panel Rotering did not transcribe (kind=picture, sign '-'); everything else is kind=grid.
"""
import re, sys, argparse, collections, hashlib

ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
ap.add_argument('bbox'); ap.add_argument('--out', default='ciphertext.tsv'); ap.add_argument('--check', action='store_true')
a = ap.parse_args()
pages = re.split(r'<page ', open(a.bbox, encoding='utf-8').read())[1:]
rows_out = []
for p in pages[1:]:
    ws = [(float(x0), float(y0), float(x1), t) for x0, y0, x1, y1, t in
          re.findall(r'xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)<', p)]
    title = ' '.join(t for x0, y0, x1, t in ws if y0 < 80)
    m = re.search(r'Seite (\d+)(?:/(\d+))?', title)
    left, right = int(m.group(1)), m.group(2) and int(m.group(2))
    body = [w for w in ws if w[1] >= 80]
    halves = {}
    for w in body:
        pg = right if (right and w[0] >= 297.6) else left
        halves.setdefault(pg, []).append(w)
    for pg in sorted(halves):
        ws_ = halves[pg]
        letters = [w for w in ws_ if w[3] != '[Abbildung]']
        xs = sorted({round(w[0]) for w in letters})
        # column grid: positions present in multi-letter rows define the columns
        byy = collections.OrderedDict()
        for w in sorted(ws_, key=lambda w: (w[1], w[0])):
            byy.setdefault(round(w[1]), []).append(w)
        multi = sorted({round(w[0]) for r in byy.values() if len(r) > 1 for w in r if w[3] != '[Abbildung]'})
        if not multi:  # pages 1 and 3: single letters only, they sit in the middle column of a 3-wide grid
            multi = None
        r_i, seen_other = 0, False
        for y, r in byy.items():
            if r[0][3] == '[Abbildung]':
                r_i += 1; seen_other = True
                rows_out.append((pg, r_i, 0, 'picture', '-')); continue
            if len(r) == 1 and not seen_other:
                rows_out.append((pg, 0, 2, 'header', r[0][3])); continue
            r_i += 1; seen_other = True
            for w in r:
                col = (multi.index(min(multi, key=lambda c: abs(c - w[0]))) + 1) if multi else 2
                rows_out.append((pg, r_i, col, 'grid' if len(r) > 1 or multi is None else 'trailer', w[3]))
hdr = ('# source: Thorsten Rotering, "Cylob-Manuskript" transcription PDF, 2 May 2015, 12 pp., sha256 0f9deae8...2082, '
       'cloud.rotering-net.de share (see NOTES.md); fetched 6 Oct 2026 (R12D-CYLOB) and converted by rotering_to_tsv.py\n'
       '# conventions: Rotering labels A-X; standard alphabet 16 signs; C D E G H I K L on p.20 only = his reading of simplified\n'
       '#   variants (his bracket: C~N D~Q E~O G~P H~S I~V K~T L~M); only dark-printed tiles are transcribed, faded/ghost tiles and\n'
       '#   picture panels are not; kind=header is the single sign above each page; picture rows are "-" placeholders;\n'
       '#   col counts from the left of that page\'s grid (3 wide; 6 wide on p.20); pp.2,4 blank. Rotering\'s, not ours: rule 2 says the scans decide.\n')
body = hdr + 'page\trow\tcol\tkind\tsign\n' + ''.join('\t'.join(map(str, r)) + '\n' for r in rows_out)
if a.check:
    cur = open(a.out, encoding='utf-8').read()
    print('OK' if cur == body else 'STALE: ' + a.out); sys.exit(0 if cur == body else 1)
open(a.out, 'w', encoding='utf-8').write(body)
print(f'wrote {a.out}: {len(rows_out)} rows')
