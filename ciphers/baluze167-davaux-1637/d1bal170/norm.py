#!/usr/bin/env python3
"""D1-BAL170: drop {clear words} from a wide pass TSV (line<TAB>tokens) so reconcile_passes.py aligns cipher tokens only.
Usage: python3 d1bal170/norm.py passes/passA_b170f228r.tsv d1bal170/normA_b170f228r.tsv"""
import re, sys
src, dst = sys.argv[1], sys.argv[2]
out = []
for i, ln in enumerate(open(src, encoding='utf-8').read().splitlines()):
    if not ln.strip():
        continue
    if i == 0 and ln.startswith('line'):
        out.append(ln); continue
    lid, _, toks = ln.partition('\t')
    toks = re.sub(r'\{[^}]*\}', ' ', toks)
    toks = re.sub(r'\(([^)]*)\)', lambda m: '(' + '_'.join(m.group(1).split()) + ')', toks)
    out.append(lid + '\t' + ' '.join(toks.split()))
open(dst, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
