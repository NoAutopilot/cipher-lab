#!/usr/bin/env python3
"""GAPS-fr4715-vieuville-pool-10 (2 Oct 2026): which glossed pool leaf (no.21 f.44, no.35 f.58, no.39 f.62) is
attested on disk carrying the most of no.44's unglossed word-codes. Reads only files already in the repository:
witness/f67r_wordcodes_context.tsv (no.44's slots, f60r_gloss '-' = unglossed) and Tomokiyo's hidden group dumps
in sources/cryptiana/web/nevers.htm (cp932). A leaf with no dump on disk scores 0 as 'no transcription', not as
'code absent'. Marks: Tomokiyo writes ' (dot) and ~ (bar); no.44's own mark is printed beside each hit."""
import csv, re, sys, os
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(os.path.dirname(HERE))
slots = [r for r in csv.DictReader((l for l in open(os.path.join(HERE, 'witness/f67r_wordcodes_context.tsv'))
                                    if not l.startswith('#')), delimiter='\t') if r['f60r_gloss'].strip() == '-']
want = {}
for r in slots:
    want.setdefault(r['group'].lstrip('.'), []).append(r['mark'])
t = open(os.path.join(ROOT, 'sources/cryptiana/web/nevers.htm'), 'rb').read().decode('cp932', 'replace')
leaves = {'no.21 f.44': 'no.21 (f.44) Letter of Jerome', 'no.35 f.58': 'no.35 (f.58) Montholon',
          'no.39 f.62': 'no.39 (f.62) Montholon'}
print('no.44 unglossed codes (occurrences, mark on no.44):', {k: v for k, v in want.items()})
best = None
for leaf, anchor in leaves.items():
    i = t.find(anchor)
    nxt = t.find('<P>no.', i + len(anchor))
    seg = t[i:nxt]
    m = re.search(r'<!--(.*?)-->', seg, re.S)
    dump = m.group(1) if m and re.search(r"\d+['~]", m.group(1)) else ''
    toks = re.findall(r"(?<![\d'])(\d+)(['~]+)", dump)
    hits = {}
    for code, mark in toks:
        if code in want:
            hits.setdefault(code, []).append(mark)
    occ = sum(len(want[c]) for c in hits)
    print(f"{leaf}: dump on disk={'yes' if dump else 'no'} ({len(toks)} marked groups); codes hit {sorted(hits)} "
          f"-> {len(hits)} of {len(want)} codes, {occ} of {sum(map(len, want.values()))} no.44 occurrences; marks {hits}")
    if best is None or occ > best[1]:
        best = (leaf, occ)
print('choose:', best[0])
