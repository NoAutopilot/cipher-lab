#!/usr/bin/env python3
"""THUR-356 (11 Oct 2026): THUR-BAMF2's scan_codes.py method widened to codes 350-360 (alphabetical neighbours of 356)
and 94, over Birch vols 4-7 djvu texts. Each hit gets the nearest preceding letter heading; a hit inside a Bamfylde
letter also prints the line above (where Birch sets the letter-spaced decipherment) so a printed gloss can be read.
python3 scan_356.py v4.txt v5.txt v6.txt v7.txt > scan_356_hits.tsv  (texts: collectionofstat04/05/07thur,
bim_..._1742_6; sha1 in b146/manifest.tsv / sources/ia-fulltext/thurloe-gz). Every 350-360 hit is printed; 94 only in
Bamfylde letters."""
import re, sys
HEAD = re.compile(r'^\W{0,3}(A\s+)?(letter|paper|col[.,]|colonel|mr\.|the\s|to\s|an?\s|from\s)', re.I)
codes = {str(c) for c in range(350, 361)} | {'94'}
print('vol\tline\tcode\theading_line\theading\tbamfylde\tline_above\tcontext')
for path in sys.argv[1:]:
    vol = path.split('/')[-1][1]
    L = open(path, encoding='utf-8', errors='replace').read().splitlines()
    head, hl = '', 0
    for i, l in enumerate(L, 1):
        s = l.strip()
        if len(s) < 90 and HEAD.match(s) and re.search(r'(intelligence|thurloe|to\s+\w|bam)', s, re.I):
            head, hl = s, i
        # a code is a bare number inside a run of numbers: at least two other 1-4 digit numbers on the line
        toks = re.findall(r'(?<![\d.,])\d+(?![\d])', l)
        if len(toks) < 3:
            continue
        for t in toks:
            if t in codes:
                bam = 'yes' if re.search(r'bam', head, re.I) else 'no'
                if t == '94' and bam == 'no':
                    continue
                above = L[i - 2].strip() if i > 1 else ''
                print(f'{vol}\t{i}\t{t}\t{hl}\t{head[:60]}\t{bam}\t{above[:100]}\t{s[:120]}')
