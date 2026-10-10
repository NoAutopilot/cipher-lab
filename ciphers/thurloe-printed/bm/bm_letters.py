#!/usr/bin/env python3
"""THUR-BM: list Blank-Marshall letters in Birch 1742 vol 6 (bim_ djvu OCR) with a numeral count per window.

python3 bm_letters.py DJVU [--check]   writes/compares bm/bm_letters.tsv
python3 bm_letters.py DJVU --vol 7 [--check]   the vol 7 heading list (THUR-BM3, collectionofstat07thur) -> bm/bm_letters_v7.tsv
Window = heading line to the next line holding 'A letter', 'to secretary', 'to mr.' or 'Vol.' heading-like start, max 140 lines.
Numerals counted = tokens of 1-3 digits (OCR), excluding the year-like 4-digit tokens. Heuristic; a lead list, not a census.
"""
import re, sys, os
HEADS7 = [16036, 23009, 24824, 26900, 28173, 29618, 31075]  # THUR-BM3: grep 'Blank|Blanck' headings + the Bruges letter signed Margaret Smith
HEADS = [3370, 10287, 14147, 16481, 17948, 40460, 44522, 45614, 64300, 65442, 65853, 69171, 77380, 83274, 84125, 86815, 89869]
def main():
    djvu = sys.argv[1]; check = '--check' in sys.argv; v7 = '--vol' in sys.argv and sys.argv[sys.argv.index('--vol') + 1] == '7'
    heads, outname = (HEADS7, 'bm_letters_v7.tsv') if v7 else (HEADS, 'bm_letters.tsv')
    L = open(djvu, encoding='utf-8', errors='ignore').read().split('\n')
    rows = ['heading_line\theading\tdate_line\tnumerals_in_window\twindow_end']
    for h in heads:
        i = h - 1; end = min(len(L), i + 140)
        for j in range(i + 3, end):
            if re.search(r'^\s*(A letter|Secretary Thurloe|.*to ſecretary Thurloe|.*to secretary Thurloe)', re.sub(r'\s+', ' ', L[j]) if v7 else L[j]):
                end = j; break
        nums = sum(len(re.findall(r'(?<![\w.])\d{1,3}(?![\w])', L[k])) for k in range(i, end))
        date = next((L[k].strip() for k in range(i, min(i + 5, end)) if re.search(r'1[56]\d\d|Bruges|N\.\s*S', L[k]) and not (v7 and 'letter of' in L[k])), '')
        rows.append(f'{h}\t{(re.sub(r"\s+", " ", L[i]) if v7 else L[i]).strip()[:70]}\t{(re.sub(r"\s+", " ", date) if v7 else date)[:60]}\t{nums}\t{end+1}')
    out = '\n'.join(rows) + '\n'
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), outname)
    if check:
        sys.exit(0 if open(p).read() == out else 1)
    open(p, 'w').write(out); print(out)
main()
