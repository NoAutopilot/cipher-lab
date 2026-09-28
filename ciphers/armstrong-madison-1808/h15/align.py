#!/usr/bin/env python3
"""H15: reconcile the two mark transcriptions of the 20 Feb 1808 letter -- ciphertext_ms.txt ('*' per mark, ARM-TR/TR2
+ H5/H17, 35 runs, 218 marks; a '^' tick on a numeral is a mark on that group, not a run) and codex-2026-09-27b/glyphs.tsv
(Tomokiyo-labelled shape tokens, 26 passages with '|' sub-runs, 257 tokens) -- run by run, keyed on the numeric context
each passage records. Writes h15/runs.tsv (one row per ms run: line, left, right, ms_count, 27b tokens, 27b count,
grade) and h15/glyphs_reconciled.tsv (the 27b passages with a 'grade' column and, in the wave-merged variant
h15/glyphs_wavemerged.tsv, consecutive wave-type tokens 20/22/23 collapsed to one token -- ARM-S1's reading of the
same strokes as one compound filler class, line B step B28). Grade H = the two sources count the same marks in the
run; M = they differ (Tomokiyo's segmentation splits what the ms count reads as one stroke, or the reverse)."""
import csv, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)
lines = [l.rstrip('\n') for l in open(os.path.join(T, 'ciphertext_ms.txt'), encoding='utf-8') if not l.startswith('#')]
runs = []  # (ms_line, left, count, right)
for li, l in enumerate(lines, 1):
    toks = l.split(); i = 0
    while i < len(toks):
        if toks[i].startswith('*'):
            j = i; n = 0
            while j < len(toks) and toks[j].startswith('*'):
                n += len(toks[j]); j += 1
            runs.append([li, toks[i-1] if i > 0 else '<bol>', n, toks[j] if j < len(toks) else '<eol>']); i = j
        else:
            i += 1
pas = list(csv.DictReader(open(os.path.join(T, 'codex-2026-09-27b/glyphs.tsv')), delimiter='\t'))
# passage -> the ms runs it spans, fixed by hand from the numeric contexts (ms line, left token) -- the automatic
# context walk stopped one run short wherever a passage runs across a line break, so the table is explicit.
SPANS = {'p1a': [(2, '1480')], 'p1b': [(3, '240')], 'p1c': [(4, '98')], 'p1d': [], 'p1e': [(7, '45'), (8, '<bol>'), (8, '13')],
         'p1f': [(10, '<bol>'), (11, '<bol>')], 'p1g': [(15, '<bol>')], 'p1h': [(15, '17')], 'p2a': [(16, '1801'), (17, '<bol>'), (18, '<bol>')],
         'p2b': [(18, '421')], 'p2c': [(19, '18')], 'p2d': [(21, '<bol>')], 'p2e': [(21, '1158'), (22, '<bol>')], 'p2f': [(25, '<bol>')],
         'p2g': [(25, '481')], 'p2h': [(26, '17')], 'p2i': [(28, '1540')], 'p3a': [(32, '760')], 'p3b': [(32, '1')], 'p3c': [(34, '365')],
         'p3d': [(35, '740'), (35, '3'), (36, '<bol>')], 'p3e': [(37, '<bol>')], 'p3f': [(38, '5')], 'p3g': [(39, '1764'), (40, '<bol>')],
         'p3h': [(43, '141'), (44, '<bol>')]}
key = {(r[0], r[1]): i for i, r in enumerate(runs)}
assign = {p['passage']: [key[k] for k in SPANS[p['passage']]] for p in pas}
inv = {}
WAVES = {'20', '22', '23'}
def merge_waves(toks):
    out = []
    for t in toks:
        if t in WAVES and out and out[-1] in WAVES: continue
        out.append(t)
    return out
rows = []; total_ms = total_27 = total_merged = 0; agree = 0
inv = {}
for p in pas:
    span = assign[p['passage']]
    toks = [x for x in p['symbols'].replace('|', ' ').split()]
    n27 = len(toks); nms = sum(runs[i][2] for i in span); nmg = len(merge_waves(toks))
    grade = 'H' if n27 == nms else 'M'
    if n27 == nms: agree += 1
    total_ms += nms; total_27 += n27; total_merged += nmg
    rows.append([p['passage'], ';'.join(str(runs[i][0]) for i in span), p['left_numeric_context'], p['right_numeric_context'], nms, n27, nmg, grade, ' '.join(toks)])
    for i in span: inv[i] = p['passage']
with open(os.path.join(HERE, 'runs.tsv'), 'w') as f:
    f.write('passage\tms_lines\tleft\tright\tms_count\ttok27b\twave_merged\tgrade\tsymbols\n')
    for r in rows: f.write('\t'.join(map(str, r)) + '\n')
    for i, r in enumerate(runs):
        if i not in inv: f.write(f"(no 27b passage)\t{r[0]}\t{r[1]}\t{r[3]}\t{r[2]}\t0\t0\tM\t\n")
for name, fn in (('glyphs_reconciled.tsv', lambda t: t), ('glyphs_wavemerged.tsv', merge_waves)):
    with open(os.path.join(HERE, name), 'w') as f:
        f.write('passage\tleft_numeric_context\tright_numeric_context\tsymbols\tconfidence\tgrade\n')
        for p, r in zip(pas, rows):
            parts = [' '.join(fn(x.split())) for x in p['symbols'].split('|')]
            f.write('\t'.join([p['passage'], p['left_numeric_context'], p['right_numeric_context'], ' | '.join(parts), p['confidence'], r[7]]) + '\n')
unassigned = [runs[i] for i in range(len(runs)) if i not in inv]
print(f"passages {len(pas)}, ms runs {len(runs)} (ms marks {sum(r[2] for r in runs)}), runs matched to a passage {len(inv)}, unmatched ms runs {unassigned}")
print(f"counts over matched runs: ms {total_ms}, 27b {total_27}, 27b wave-merged {total_merged}; passages with equal counts {agree}/{len(pas)}")
print("per passage (ms / 27b / merged):", ', '.join(f"{r[0]} {r[4]}/{r[5]}/{r[6]}" for r in rows))
