# PREREG-MQS-CTTS-EXPORT (written 9 Oct 2026, 06:5x UTC by date -u, by MQS-CTTS-EXPORT, before any control below was run)

Research row: research/MARY-STUART-TALK-2026-10-09.tsv M35 ("CTTS interoperability: our transcriptions open in the authors'
own tool"; gap: our sorter output cannot be opened in CTTS). CTTS = CrypTool Transcriber and Solver (G. Lasry, CrypTool
project, Apache-2.0).

Feature: `tools/sign_sorter_apply.py` gains
- `--icons DIR`: one exemplar PNG per settled sign (the crop of the first `kept`/confirmed tile of that sign, else the first
  tile carrying it), plus `DIR/icons.tsv` (sign, file, sid, n_tiles);
- `--ctts-out DIR`: the settled transcription written as a CTTS-loadable project (one record per box: page, x, y, w, h, sign),
  with the sign inventory pointing at the `--icons` files; and a reader (`read_ctts`) that parses that output back.
  The exact CTTS file layout is taken from the CTTS repository's own save/load code if the lane allows one read of
  github.com/CrypToolProject/CTTS; otherwise `--ctts-out` is not built and only `--icons` ships (stated before the run).
- Unsettled tiles (aside, bad-cut, taken-out) and not-letter tiles are exported with their status, never with a sign the
  person did not give (they are not silently dropped and not silently labelled).

## Known answer (synthetic, offline, no network: `tools/tests/test_sign_sorter_ctts.py`)

Per seed (20 seeds, 1..20): 3 synthetic page images (numpy/PIL), 300 boxes at known positions, 40 sign labels drawn from a
Zipf-like distribution, and a simulated sorter db (piles/moves/newpiles) giving every status `apply()` can produce (kept,
moved, merged, not-letter, aside, bad-cut, taken-out). Truth = `apply()`'s own rows joined to signs.tsv boxes.

Statistics, per seed:
- **S1 round-trip agreement** = share of the 300 boxes for which `read_ctts(--ctts-out)` returns exactly the truth
  (sid, page, x, y, w, h, sign or status).
- **S2 icon fidelity** = share of settled signs whose icon PNG is pixel-identical to the crop of its chosen exemplar box
  from the page image.

Nulls (each can differ from the known answer on its statistic):
- **label-permuted**: the same export with sign labels shuffled across boxes before writing. S1 compares each box's label
  to its own truth label, so a shuffle lowers it; expected about the sum of squared label shares (Zipf over 40 signs: about
  0.10-0.20), never near 1.
- **box-convention**: the same export with the box written as (x1, y1, x2, y2) where (x, y, w, h) is read back. S1 compares
  the coordinates, so this changes it; expected 0.0 (every box with w or h > 0 differs).
- **icon-offset** (for S2): icons cropped 3 px right of the exemplar box. Pixel identity compares the crop, so the shift
  changes it; expected near 0 on ink glyphs.

Gate (fixed now): S1 = 1.000 and S2 = 1.000 on 20/20 seeds, AND each null below 0.5 on 20/20 seeds.
Ceiling check: not applicable in the usual sense -- this is a lossless-format test, the known answer is expected at 1.000;
headroom is shown by the nulls, which must sit far below it.

What this does NOT measure (stated before the run): whether CTTS itself opens the file. That needs CTTS (16 GB RAM,
2560x1600 screen, the owner's desktop only). Our reader is written from CTTS's own format code, not from CTTS running, so
a pass is a plumbing control. Shelf grade at most `weak` for `--ctts-out` until a person opens one export in CTTS and
reports the box and sign counts; `--icons` can be `controlled-only` on S2 alone.

## Result

(appended after the run; the text above is unchanged once pushed)
