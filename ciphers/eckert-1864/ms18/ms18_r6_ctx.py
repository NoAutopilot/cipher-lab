#!/usr/bin/env python3
"""MS18-R6: context of a phrase in a scratch OR djvu text. Usage: ms18_r6_ctx.py FILE 'phrase' [width]. Words are matched across any non-letter gap."""
import re, sys
f, ph = sys.argv[1], sys.argv[2]; w = int(sys.argv[3]) if len(sys.argv) > 3 else 900
t = open(f, errors='ignore').read()
pat = r'[^a-z0-9]+'.join(re.escape(x) for x in re.findall(r'[a-z0-9]+', ph.lower()))
for m in re.finditer(pat, t, flags=re.I):
    pg = t.count('\f', 0, m.start())
    print(f'--- {f.split("/")[-1]} offset {m.start()} formfeeds-before {pg}\n' + t[max(0, m.start()-w//2): m.end()+w//2].replace('\n\n', '\n'))
