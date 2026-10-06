#!/usr/bin/env python3
"""Print the numeral groups of ciphertext.txt (RGP 108 no. 92 as printed) in reading order, one per line.
Page headers, the item number, dates and the archival citation are excluded. R9-OBRED4, 6 Oct 2026."""
import re, pathlib
t = (pathlib.Path(__file__).resolve().parent.parent / 'ciphertext.txt').read_text()
body = t[t.index('=== p.110 ==='):t.index('A.R.A., Holland 2613')]
body = re.sub(r'=== p\.\d+ ===', '', body)
body = body.replace('92. [P. VAN BREDERODE AAN OLDENBARNEVELT], 21 februari 1605.', '')
body = body.replace('desen 21en february 1605', '')
for tok in re.findall(r'\b(XLII|\d+(?:\.\d+)?)\b', body):
    print(tok)
