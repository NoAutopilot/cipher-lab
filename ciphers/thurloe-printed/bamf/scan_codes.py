#!/usr/bin/env python3
"""THUR-BAMF2: find codes 937, 745, 356 (and 94 inside Bamfylde letters) in the Birch vols 4-6 djvu texts.
Each hit gets the nearest preceding letter heading (a line containing 'letter'/' to ' + a sender name, or 'Bam(p)fylde').
python3 scan_codes.py v4.txt v5.txt v6.txt  (djvu texts of collectionofstat04thur, collectionofstat05thur,
bim_..._1742_6; sha1 in b146/manifest.tsv / sources/ia-fulltext/thurloe-gz) -> TSV on stdout"""
import re, sys
HEAD = re.compile(r'^\W{0,3}(A\s+)?(letter|paper|col[.,]|colonel|mr\.|the\s|to\s|an?\s)', re.I)
codes = {'937', '745', '356', '94'}
print('vol\tline\tcode\theading_line\theading\tbamfylde\tcontext')
for path in sys.argv[1:]:
    vol = re.sub(r'\D', '', path.split('/')[-1])
    L = open(path, encoding='utf-8', errors='replace').read().splitlines()
    head, hl = '', 0
    for i, l in enumerate(L, 1):
        s = l.strip()
        if len(s) < 90 and HEAD.match(s) and re.search(r'(intelligence|thurloe|to\s+\w|bam)', s, re.I):
            head, hl = s, i
        toks = re.findall(r'(?<![\d.,])\d+(?![\d])', l)
        for t in toks:
            if t in codes:
                bam = 'yes' if re.search(r'bam', head, re.I) else 'no'
                if t == '94' and bam == 'no':
                    continue
                print(f'{vol}\t{i}\t{t}\t{hl}\t{head[:60]}\t{bam}\t{s[:120]}')
