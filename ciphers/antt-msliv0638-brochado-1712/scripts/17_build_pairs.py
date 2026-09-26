import json

"""AX2-BRO4 (26 Sept 2026): builds tools/interlinear_align.py's PAIRS.tsv from the appendix's own
already-reconciled anchors (_anchors.json, AX-BRO3's exact anchor-finding, never re-touched here).
One row per appendix entry: plain_raw is the WHOLE deciffrada gloss (not a per-run truncated span --
letting the DP see the full sentence is exactly what the flexible chunk-length alignment needs to
absorb the appendix's own abbreviation-driven length drift, CLAUDE.md rule 3's PX-BRODEC lesson);
cipher_raw flattens each entry's merged (PLAIN word / CODE run) segments into individual
whitespace-separated tokens, each CODE token prefixed '@' (tools/interlinear_align.py's
--code-prefix) so the aligner can tell a codebook symbol from a literal clear word without relying on
digitish() (Brochado's codebook mixes digit codes with single-letter alpha codes, x/y/z/a/b.../m).
A code's own uncertain-glyph marker ('9±' vs '9') is stripped to its base identity here, matching
16_thin_attest.py's code_val() convention (key_by_code strips '±' the same way) -- otherwise '9' and
'9±' would wrongly count as two different codes to the aligner.

Output: align/pairs.tsv (plain_line, plain_raw, cipher_line, cipher_raw), one row per of the 38
appendix entries, no network, no image access.
"""

ROOT = '/home/user/cipher-lab/ciphers/antt-msliv0638-brochado-1712'

anchors = json.load(open(f'{ROOT}/scripts/_anchors.json'))

rows = []
for key, merged, decif, anchor_pos, ok in anchors:
    leaf, entry_label = key
    label = f'{leaf}/{entry_label}'
    toks = []
    for t, v in merged:
        if t == 'PLAIN':
            toks.append(v)
        else:
            for tok in v:
                toks.append('@' + tok.rstrip('±'))
    rows.append((label, decif, label, ' '.join(toks)))

import csv
with open(f'{ROOT}/align/pairs.tsv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f, delimiter='\t', lineterminator='\n')
    w.writerow(['plain_line', 'plain_raw', 'cipher_line', 'cipher_raw'])
    w.writerows(rows)

print(f'{len(rows)} pairs written to align/pairs.tsv')
n_code = sum(1 for _, _, _, cr in rows for t in cr.split() if t.startswith('@'))
n_plain = sum(1 for _, _, _, cr in rows for t in cr.split() if not t.startswith('@'))
print(f'code tokens: {n_code}, plain-word tokens: {n_plain}')
