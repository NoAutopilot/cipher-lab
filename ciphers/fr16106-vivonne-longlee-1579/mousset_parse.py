#!/usr/bin/env python3
"""Mousset 1912 (IA dpchesdiplom00longuoft djvu text) -> mousset_letters.tsv, one row per printed source line (126 on 4 Oct 2026).
Usage: mousset_parse.py DJVU_TXT OUT.tsv.  Anchor = source line ('Bibl. nat. Fonds fr. 161xx, ff. N-M. -- Original autographe');
date = nearest preceding heading line '<year>. <day> <month>, <place>' (OCR, grade I); recipient = nearest preceding all-caps 'A ...' line;
cipher_original / official_decipherment flags from 'Or. chiffre' / 'dechiffr' in the source line. Printed pages: the djvu text carries no
reliable page numbers (the OCR'd table is column-scrambled), so printed_page is left blank: use djvu_line to locate the letter."""
import re, sys
src = [re.sub(r'\s+', ' ', x).strip() for x in open(sys.argv[1], encoding='utf-8', errors='replace')]
end = next(i for i, l in enumerate(src) if l.startswith('TABLE CHRONOLOGIQUE'))
mon = r'(janv|f[ée]vr|mars|avr|mai|juin|juill|ao[uû]t|sept|oct|nov|d[ée]c)'
head = re.compile(r'^(15[89]\d)[.,]\s+(.{1,12}?)\s*(' + mon + r'\S*)\s*,?\s*(\w[\w\-]*)?', re.I)
isrc = re.compile(r'^(Bibl|liibl|Bilil|Hibl|IliljL|liihl|I!il\)l|Archives|Bibliothèque|Mémoires|Arch)', re.I)
rows = []; date = recip = ''
for i in range(2000, end):
    l = src[i]
    m = head.match(l)
    if m: date = f'{m.group(1)}.{m.group(2)} {m.group(3)}'
    if re.match(r'^(A|AU|À) [A-ZÉ]', l) and l == l.upper() and len(l) < 45: recip = l
    if isrc.match(l) and re.search(r'[Ff]onds|Kouds|nat\.|Archiv|Ms', l) and len(l) < 220:
        fr = re.search(r'1[56]1\d\d|15109|1610i\)|ir,109|16109|16110', l)
        rows.append([date, recip, fr.group(0) if fr else '', l, str(i + 1)])
        date = ''
with open(sys.argv[2], 'w') as f:
    f.write('date_ocr\trecipient_ocr\tvolume_token\tsource_line_ocr\tdjvu_line\tcipher_original\tofficial_decipherment\tprinted_page\n')
    for r in rows:
        s = r[3]
        co = 'y' if re.search(r'chi|cliil|ciiitr|Or\.', s, re.I) and 'Original autogr' not in s else ''
        dd = 'y' if re.search(r'd[ée]c[hl]|dcchiffr|décl|official|officiel|oi+ciel', s, re.I) else ''
        f.write('\t'.join(r + [co, dd, '']) + '\n')
print(len(rows), 'source lines')
