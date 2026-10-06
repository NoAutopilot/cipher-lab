#!/usr/bin/env python3
"""R7A-HEL53 (6 Oct 2026): split DECODE's own R1953 transcription document (DOC_R1953_D3616_3616.txt, transcriber
'KL', 26 Jan 2020; not committed, re-fetch with tools/decode_browser_login.js 1953 OUT --guess-fullsize) into
per-line tokens and check they are the same 846 tokens, in the same order, as ciphertext_R1953.txt.
Usage: python3 doc_tokens.py DOC.txt > doc_tokens.tsv   (columns: pos image line doc_raw ct_raw)"""
import re, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
doc = open(sys.argv[1], encoding='utf-8', errors='replace').read()
img = None; ln = 0; toks = []
for line in doc.splitlines():
    m = re.match(r'#IMAGE NAME: (\d+)\.png\s*$', line)
    if m: img = m.group(1); ln = 0; continue
    if line.startswith('#') or img is None: continue
    line = re.sub(r'<[^>]*>', '', line)
    if not re.search(r'\d', line) or line.strip() == '1752.': continue
    ln += 1
    for g in re.split(r'[.,]', line):
        if re.search(r'\d', g): toks.append((img, ln, g.strip()))
ct = open(os.path.join(HERE, '..', 'ciphertext_R1953.txt')).read().split()
norm = lambda s: re.sub(r'[^0-9?]', '', s)
print('pos\timage\tline\tdoc_raw\tct_raw')
diff = 0
for i, (t, c) in enumerate(zip(toks, ct)):
    if norm(t[2]) != norm(c): diff += 1
    print(f'{i}\t{t[0]}\tL{t[1]:02d}\t{t[2]}\t{c}')
print(f'# doc tokens {len(toks)}, ciphertext tokens {len(ct)}, digit mismatches {diff}', file=sys.stderr)
