#!/usr/bin/env python3
"""bMAT1F: diff pass A f.78v lines A-F (page lines 6-11) against Bourdeau's f78_cipher.txt lines 6-10 by NW alignment of
every page-line half against every Bourdeau line, to locate his line joins. Writes align1f/diff_f78v.tsv."""
import os, difflib
h = os.path.dirname(os.path.abspath(__file__))
bd = [l.split() for l in open(os.path.join(h, '..', 'align1e', 'f78_cipher.txt')) if l.strip()]
pa = [l.rstrip('\n').split('\t') for l in open(os.path.join(h, 'passA_f78v.tsv'))][1:]
out = ['page_line\thalf\tn_tokens\tbest_bourdeau_line\tshared_block_tokens']
for lid, toks, *_ in pa:
    t = toks.split(); m = len(t) // 2
    for half, seg in (('left', t[:m]), ('right', t[m:])):
        best = max(range(len(bd)), key=lambda i: sum(b.size for b in difflib.SequenceMatcher(None, seg, bd[i], autojunk=False).get_matching_blocks()))
        s = sum(b.size for b in difflib.SequenceMatcher(None, seg, bd[best], autojunk=False).get_matching_blocks())
        out.append('%s\t%s\t%d\t%d\t%d' % (lid, half, len(seg), best + 1, s))
open(os.path.join(h, 'diff_f78v.tsv'), 'w').write('\n'.join(out) + '\n'); print('\n'.join(out))
