# Armstrong 1808 mark sorter (ARM-SORTER, 4 Oct 2026, account 3)

The owner settles the shorthand marks of Armstrong to Madison, Paris, 20 Feb 1808 (NARA M34 roll 14) by eye, the way
the Birago piles were settled. The numeral groups are manuscript-checked (ARM-TR/ARM-TR2) and are **not on the page**.

## What the sort is meant to settle

Two one-reader transcriptions of the marks disagree on the count by about 16%: `ciphertext_ms.txt` has 218 marks in
28 runs, `codex-2026-09-27b/glyphs.tsv` has 257 tokens in 28 fragments (NOTES.md "Campaign step H3", where the count
error decided whether the pair-design test had any power). `passages.tsv` maps every run on the page to the gap
between two numeral groups and gives both counts there; the totals reproduce 218 and 257 exactly. This cut has 263
tiles (deliberately over-split). The disagreement is concentrated in five gaps: 61 45 _ 48 1360 (ms 22, glyphs 32),
14 740 _ 67 780 (12 vs 20; ms reads a numeral 3 inside it), 18 1801 _ 78 1364 (20 vs 25), 28 14 _ 44 176 (35 vs 39),
101 421 _ 17 86 (5 vs 8). The owner's piles answer two things at once: **how many marks** each gap holds (merge
bad-cut halves, split doubled tiles, set aside specks) and **which marks are the same sign** (pile = sign).

## Files (inputs only; the page is built, not committed)

| file | what |
|---|---|
| `runs.tsv` | 37 mark runs: frame, box in the frame's native pixels, note. Located by eye on ruler overviews of the ARM-TR line bands (`images/crops_0030`, `crops_0031L`, `crops_0031R`, `crops_0033` manifests), page-1 left edge widened to x=120 and page-2 right edge to x=2010 (the H5/H17 crop-shear lessons) |
| `exclude.tsv` | 34 boxes inside a run removed by eye from the debug overlays: digits (13, 48, 47, 17, 67, 1360, 1210), specks, gutter-only and black-border boxes |
| `segment_marks.py` | runs.tsv + exclude.tsv -> `signs.tsv` (sid, page, x, y, w, h, run). Why not `glyph_atlas.py segment` is in its docstring (both modes tried: --cursive dropped/merged whole marks, the default mode cut dust) |
| `cluster_marks.py` | HOG + size, PCA(30), k-means k=26 (seed 20261004) -> `clusters.tsv`, `labels.tsv` (initial pile = cluster, named M01.. by size, value-blind), `focus.tsv` (30) |
| `passages.tsv` | run -> numeral gap, with the ms and glyphs counts there |
| `build.sh` | the build |

Frames: page 1 = 0030; pages 2-3 = **0031** (0032 is a second scan of the same spread; 0031 is the cleaner copy:
Laplacian variance 2800/2891 vs 2262/2624 on the left/right page regions); page 4 = 0033 left leaf, one mark (line 4
head). Page images come from `images/` on disk; no network.

Focus ("Check these first", 30): 11 named spots (flourish before 200 on p.1, the tick after 38, the '31?' at the end of
p.1 line 9, ms's numeral 3 on p.3 line 4, the mark before 58 that only glyphs counts, six boxes cut against the binding
edge); then, gap by gap, largest count disagreement first, the widest tile where glyphs counts more (two marks merged?),
the smallest where it counts fewer (a fragment?), both where the counts differ by 8+; then tiles nearest a pile boundary.

## Build (repo root, disk only)

```
bash ciphers/armstrong-madison-1808/sorter/build.sh OUTDIR
NODE_PATH=$(npm root -g) node tools/sign_sorter/browser_tests/test_qa.js OUTDIR/armstrong1808_marks_sorter.html
```

4 Oct 2026: 263 tiles, 26 piles, page 1.12 MB; test_qa.js 141 PASS, 0 FAIL (after the container's proxy-CA fix for
Chromium, CLAUDE.md access playbook item 2; without it the two "no page errors" checks fail on the Google Fonts load).
The orchestrator publishes it with capabilities `{"db": {}}`.

## Apply (after the owner's sort)

Export the page's db collections (piles, moves, newpiles, checked) to a directory DUMP, then:

```
python3 tools/sign_sorter_apply.py --labels ciphers/armstrong-madison-1808/sorter/labels.tsv --db DUMP \
  --out ciphers/armstrong-madison-1808/sorter/settled.tsv --summary ciphers/armstrong-madison-1808/sorter/settled.md
```

`settled.tsv` gives every tile its settled pile or status (kept/moved/merged, not-letter, aside, bad-cut). Then the
mark tokens of the transcription come from it like this:

1. Drop tiles marked not-letter, aside or bad-cut (a bad cut the owner marks means "not one mark": its run gets a
   review line, not a guess).
2. Within each run, order the remaining tiles by x (signs.tsv) and write each one's settled pile name: that is the
   run's mark sequence, and its length is the settled count.
3. Place each run at its gap with `passages.tsv` (runs listed in reading order; a gap spanning two lines is the
   runs joined in that order).
4. Write the result as a **new** file, `ciphertext_marks.txt` (numerals from `ciphertext_ms.txt`, each '*' run replaced
   by the settled pile sequence, grade M until a second reader or a control lifts it) with a script that regenerates it
   and `--check`s it (rule 7). `ciphertext.txt` and `ciphertext_ms.txt` are never overwritten. The settled count then
   replaces the 218-vs-257 band in any test that brackets transcription error (H3's pair-design control).

Not done here (out of brief): that regeneration script, and any reading of the marks.
