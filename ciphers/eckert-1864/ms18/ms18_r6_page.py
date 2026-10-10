#!/usr/bin/env python3
"""MS18-R6: nearest running heads (lines with 'Chap.' or 'CHAP.') before and after a phrase in a scratch OR djvu text. Usage: ms18_r6_page.py FILE 'phrase'"""
import re, sys
f, ph = sys.argv[1], sys.argv[2]; t = open(f, errors='ignore').read()
pat = r'[^a-z0-9]+'.join(re.escape(x) for x in re.findall(r'[a-z0-9]+', ph.lower()))
m = re.search(pat, t, flags=re.I)
if not m: sys.exit('no match')
heads = [(h.start(), t[max(0, h.start()-70):h.end()+30].replace('\n', ' | ')) for h in re.finditer(r'Chap\.\s*[IVXL]+\]|CHAP\.\s*[IVXL]+\]|\[Chap', t)]
b = [h for h in heads if h[0] < m.start()][-1:]; a = [h for h in heads if h[0] > m.end()][:1]
print('before:', b); print('after:', a)
