#!/usr/bin/env python3
"""ciphertext.tsv (one reconciled line per row) -> ciphertext_tokens.tsv (one sign per row) for tools/decode_key.py.
Struck runs ([struck...]) are dropped; other bracketed signs are kept as nomenclator tokens (unkeyed). NV01-READ, 3 Oct 2026."""
import re
rows = ['line\tpos\tsign\tconf']
for ln in open('ciphertext.tsv'):
    if ln.startswith('#') or ln.startswith('line\t') or not ln.strip(): continue
    line, digits = ln.rstrip('\n').split('\t')[:2]
    toks = [t for t in re.findall(r'\[[^\]]*\]|\S+', digits) if not t.startswith('[struck') and t != '[blot]']
    for i, t in enumerate(toks, 1):
        rows.append(f"{line}\t{i}\t{t.strip('[]')}\t{'M' if t.startswith('[') else 'H'}")
open('ciphertext_tokens.tsv', 'w').write('\n'.join(rows) + '\n')
