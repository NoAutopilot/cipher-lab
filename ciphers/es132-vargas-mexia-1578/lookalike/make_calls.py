#!/usr/bin/env python3
"""ES132-LOOK: split lookalike_pass.py packet tiles (run with --hide-passc) into half-page re-read calls, each with only that half's
line crops. Restricts f.51v to L11-L25 (the brief) and drops f.52r L22 (the clear dating line). The tool's own prompt text is kept;
only the crop list is narrowed, the (absent) candidate sheet is replaced by the pass prompt's notation legend, and tiles are listed.
Writes lookalike/<page>/look_<page>_sel_tiles.tsv (the tiles reconcile gets) and lookalike/calls/<call>_prompt.md."""
import csv, os
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
CALLS = {'f51v_a': ('f51v', range(11, 19)), 'f51v_b': ('f51v', range(19, 26)),
         'f52r_a': ('f52r', range(1, 12)), 'f52r_b': ('f52r', range(12, 22))}
LEGEND = """Notation of the candidate labels (the transcription's own, shape names only):
  the number as written; a vowel sign written right after it: '+' small cross, '.' dot, 'ρ' looped e/p-like tail, 'σ' hook like a
  small 6 that is not clearly a digit, '⊣' u-like hook; a mark ABOVE the number: @n circumflex/hat ^, @s straight bar, @l short
  slanted acute stroke, @m wavy tilde, @r small v- or r-shaped hooked mark, @2 two dots; '_' underline; {y} or y the letter y;
  '/' slash; '-' or an empty candidate never appears: if the sign is not there at all (one reader saw a token that is not on the
  page), answer X_NEW with note 'absent'; if two tokens are written together as one group (or one group split), say so in note."""
HEAD = """# Look-alike re-read, {call} (value-blind; ES132-LOOK, 9 Oct 2026, from tools/lookalike_pass.py packet --hide-passc)

You are re-reading {n} sign tiles of a 16th-century symbol-cipher transcription (numerals with small marks). Two earlier readers
disagreed on some of them, or gave a label that is often confused with another. You see only the line crops (s1 = left half,
s2 = right half of the same line; the halves overlap a little: do not count a token twice). You are never told what any sign
means; do not guess letters or words; do not try to decipher.

Line crops (read every one of these images with the Read tool before answering): {crops}

{legend}

For each tile below, find the token at that line and position ('pos' counts tokens from the left of the line; it may be off by one
or two, so use the 'before'/'after' neighbouring labels to find it) and pick the candidate whose shape it is. Candidates are in
alphabetical order. Labels shown anywhere here are earlier readers' and may be wrong: judge the shape in the image, never copy a label.
Answer one TSV row per tile, header: passage<TAB>pos<TAB>label<TAB>conf<TAB>second<TAB>note
  label  one of the tile's candidates, X_NEW if none fits, or SPLIT:a|b if you cannot choose between two
  conf   H (clear), M (probable), L (guess); second = your runner-up or empty; note = the shape feature you used.
Write the TSV (header + exactly {n} rows, same order) to {out} and reply only "done N rows".

Tiles (passage, pos, candidates, before | after):
{tiles}
"""
os.makedirs(HERE / 'lookalike/calls', exist_ok=True)
sel = {}
for call, (page, rng) in CALLS.items():
    T = list(csv.DictReader(open(HERE / f'lookalike/{page}/look_{page}_tiles.tsv'), delimiter='\t'))
    lines = ['L%02d' % i for i in rng]
    t = [r for r in T if r['passage'] in lines]
    sel.setdefault(page, (list(T[0]), []))[1].extend(t)
    crops = ', '.join(str(HERE / f'images/{page}_{ln}_s{s}.jpg') for ln in lines for s in (1, 2))
    rows = '\n'.join(f"{r['passage']}\t{r['pos']}\t{','.join(sorted(r['candidates'].split(',')))}\t{r['before']} | {r['after']}" for r in t)
    out = HERE / f'lookalike/calls/{call}_reread.tsv'
    (HERE / f'lookalike/calls/{call}_prompt.md').write_text(HEAD.format(call=call, n=len(t), crops=crops, legend=LEGEND, out=out, tiles=rows))
    print(call, len(t), 'tiles', len(lines), 'lines')
for page, (fields, rows) in sel.items():
    with open(HERE / f'lookalike/{page}/look_{page}_sel_tiles.tsv', 'w', newline='') as f:
        w = csv.DictWriter(f, fields, delimiter='\t', lineterminator='\n'); w.writeheader(); w.writerows(rows)
