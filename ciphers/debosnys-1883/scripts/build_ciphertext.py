#!/usr/bin/env python3
"""Render signs.tsv + clusters.tsv + marks.tsv into a reading-order ciphertext.txt of sign
codes (S00-S89, one machine-clustered atlas across all 4 pages/cryptograms). Single
machine-segmented pass -- draft, not hand-verified. Marks (small superscript strokes) are
appended to their base sign as +Mxx."""
import csv
from collections import defaultdict

def load_marks_by_sign():
    m = defaultdict(list)
    with open('glyphs/clusters.tsv') as f:
        r = csv.DictReader(f, delimiter='\t')
        mark_cluster = {}
        for row in r:
            if row['kind'] == 'mark':
                mark_cluster[row['id']] = row['cluster']
    with open('glyphs/marks.tsv') as f:
        r = csv.DictReader(f, delimiter='\t')
        for row in r:
            mid = row['mid']
            sid = row['sid']
            code = mark_cluster.get(mid)
            if code is not None:
                m[sid].append(f"M{int(code):02d}")
    return m

def load_sign_codes():
    codes = {}
    with open('glyphs/clusters.tsv') as f:
        r = csv.DictReader(f, delimiter='\t')
        for row in r:
            if row['kind'] == 'sign':
                codes[row['id']] = f"S{int(row['cluster']):02d}"
    return codes

def main():
    marks_by_sign = load_marks_by_sign()
    codes = load_sign_codes()
    rows = []
    with open('glyphs/signs.tsv') as f:
        r = csv.DictReader(f, delimiter='\t')
        for row in r:
            rows.append(row)
    by_page_line = defaultdict(list)
    for row in rows:
        by_page_line[(row['page'], int(row['line']))].append(row)

    page_names = {'c1': 'Cryptogram 1', 'c2a': 'Cryptogram 2 (page a)',
                  'c2b': 'Cryptogram 2 (page b)', 'c3': 'Cryptogram 3'}
    out = []
    out.append("# debosnys-1883 ciphertext -- sign codes as segmented, SINGLE MACHINE PASS, DRAFT")
    out.append("# not hand-verified; codes are tools/glyph_atlas.py cluster ids (S00-S89 over an")
    out.append("# intentionally over-split k=90 clustering across all 4 fetched page images);")
    out.append("# +Mxx after a code is an attached mark (accent/dot/tilde) above that sign.")
    out.append("# Cryptogram 4 (pages 4a/4b) was not fetched this pass (4-request host cap).")
    out.append("")
    for page in ['c1', 'c2a', 'c2b', 'c3']:
        out.append(f"=== {page_names[page]} ===")
        lines_present = sorted({ln for (p, ln) in by_page_line if p == page})
        for ln in lines_present:
            toks = sorted(by_page_line[(page, ln)], key=lambda r: int(r['pos']))
            rendered = []
            for t in toks:
                sid = t['sid']
                code = codes.get(sid, '??')
                mk = marks_by_sign.get(sid, [])
                rendered.append(code + (''.join('+' + x for x in mk) if mk else ''))
            out.append(' '.join(rendered))
        out.append("")
    with open('ciphertext.txt', 'w') as f:
        f.write('\n'.join(out))
    print('wrote ciphertext.txt,', len(rows), 'sign tokens')

if __name__ == '__main__':
    main()
