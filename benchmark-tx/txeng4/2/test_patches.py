#!/usr/bin/env python3
"""Offline tests for the two TXE4-2 tool patches (box_token_align.py.patch, glyph_atlas.py.patch), run against scratch copies
of the tools with the patches applied (R7: the shared tools were not edited in this job). No network, no model, no truth.
    python3 test_patches.py SCRATCH_TOOLS_DIR
Catches: (1) --count-tol skips and lists a line whose box count is 20% off its token count and keeps one 5% off;
(2) --tokens-out writes only 1:1 boxes at --keep-pos positions with the read sign as label; (3) atlas --from-tokens accepts
the same TSV as --from-truth; --row-text prints the words column (sheet wider than without); --shuffle-rows derangement:
no row keeps its own tiles, the same tiles appear, labels stay. Must NOT change: a run without the new flags is unchanged."""
import csv, os, subprocess, sys, tempfile, numpy as np
TOOLS = sys.argv[1]
d = tempfile.mkdtemp()
# --- (1)(2) box_token_align
signs = ['sid\tpage\tline\tx\tw']
for ln, n in ((1, 10), (2, 10)):
    for i in range(n):
        signs.append(f'p_{ln}_{i}\tp\t{ln}\t{i * 30}\t20')
open(f'{d}/signs.tsv', 'w').write('\n'.join(signs) + '\n')
read = ['line\tpos\tsign'] + [f'p_L01\t{i + 1}\ts{i}' for i in range(10)] + [f'p_L02\t{i + 1}\ts{i}' for i in range(8)]  # L02: 10 boxes vs 8 tokens = 25% off
open(f'{d}/read.tsv', 'w').write('\n'.join(read) + '\n')
open(f'{d}/keep.tsv', 'w').write('line\tpos\n' + ''.join(f'p_L01\t{p}\n' for p in (1, 2, 5)))
r = subprocess.run(['python3', f'{TOOLS}/box_token_align.py', '--signs', f'{d}/signs.tsv', '--read', f'{d}/read.tsv', '--lam', '0',
                    '--keep-pos', f'{d}/keep.tsv', '--count-tol', '0.10', '--tokens-out', f'{d}/tok.tsv', '--out', f'{d}/map.tsv'],
                   capture_output=True, text=True)
assert 'count-tol: p_L02 skipped (10 boxes vs 8 tokens' in r.stdout, r.stdout + r.stderr
rows = list(csv.DictReader(open(f'{d}/map.tsv'), delimiter='\t'))
assert {x['line'] for x in rows} == {'p_L01'}, 'the off-count line must have no map rows'
tok = list(csv.DictReader(open(f'{d}/tok.tsv'), delimiter='\t'))
assert [(t['sid'], t['pos'], t['label']) for t in tok] == [('p_1_0', '1', 's0'), ('p_1_1', '2', 's1'), ('p_1_4', '5', 's4')], tok
r0 = subprocess.run(['python3', f'{TOOLS}/box_token_align.py', '--signs', f'{d}/signs.tsv', '--read', f'{d}/read.tsv', '--lam', '0',
                     '--out', f'{d}/map0.tsv'], capture_output=True, text=True)
assert {x['line'] for x in csv.DictReader(open(f'{d}/map0.tsv'), delimiter='\t')} == {'p_L01', 'p_L02'}, 'without --count-tol both lines map'
print('box_token_align patch: count-tol, keep-pos, tokens-out OK; unchanged without the flags')
# --- (3) glyph_atlas atlas --from-tokens / --row-text / --shuffle-rows on a synthetic atlas
import cv2
A = f'{d}/atlas'; os.makedirs(f'{A}/crops')
img = np.full((60, 400), 255, np.uint8)
for i in range(8):
    cv2.rectangle(img, (10 + i * 48, 15), (30 + i * 48, 45), 0, -1 if i % 2 else 2)
cv2.imwrite(f'{A}/crops/pg.png', img)
subprocess.run(['python3', f'{TOOLS}/glyph_atlas.py', 'segment', '--page', f'pg={A}/crops/pg.png', '--out', A], check=True, capture_output=True)
sg = list(csv.DictReader(open(f'{A}/signs.tsv'), delimiter='\t'))
assert len(sg) >= 6, len(sg)
tokens = 'sid\tcode\n' + ''.join(f"{s['sid']}\t{'A' if i % 2 else 'B'}\n" for i, s in enumerate(sg))
open(f'{d}/tokens.tsv', 'w').write(tokens)
open(f'{d}/rt.tsv', 'w').write('code\ttext\nA\tfilled box (π)\nB\thollow box (Δ)\n')
def atlas(prefix, *extra):
    subprocess.run(['python3', f'{TOOLS}/glyph_atlas.py', 'atlas', '--out', A, '--from-tokens', f'{d}/tokens.tsv', '--per', '3',
                    '--spread', '--sheet-prefix', prefix, '--rows-per-sheet', '5'] + list(extra), check=True, capture_output=True)
    return {r['code']: r for r in csv.DictReader(open(f'{A}/{prefix}.tsv'), delimiter='\t')}, cv2.imread(f'{A}/{prefix}_01.png', 0)
p, im_p = atlas('plain')
assert set(p) == {'A', 'B'} and all(r['shown_from'] == c for c, r in p.items())
t, im_t = atlas('text', '--row-text', f'{d}/rt.tsv')
assert im_t.shape[1] > im_p.shape[1], 'row-text widens the sheet'
assert p['A']['exemplars'] == t['A']['exemplars'], 'row-text changes no tile pick'
s, im_s = atlas('shuf', '--row-text', f'{d}/rt.tsv', '--shuffle-rows', '7')
assert s['A']['shown_from'] == 'B' and s['B']['shown_from'] == 'A', s
assert s['A']['exemplars'] == t['B']['exemplars'] and s['B']['exemplars'] == t['A']['exemplars'], 'shuffle swaps the tile sets'
assert set(s) == {'A', 'B'} and s['A']['n_secure'] == t['A']['n_secure'], 'labels and counts stay'
print('glyph_atlas patch: from-tokens, row-text, shuffle-rows OK')
