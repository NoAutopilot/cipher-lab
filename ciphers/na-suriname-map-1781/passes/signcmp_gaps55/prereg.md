# GAPS55-na-suriname-map-1781 (account-4), 3 Oct 2026 -- pre-registration (pushed before the vision call)

Second attempt at GAPS49's question (passes/signcmp_gaps49/prereg.md): on the Nieuw Secreet Alphabet key sheet
(NA 1.05.03 inv. 86 scan 0003), which row's y carries the two dots -- M, N, both or neither -- on each page? GAPS49 was a
non-test because its dots control (A-row [x-dots], tile e) read "unclear 0.4". This run changes the control only:
- dots control: two of 2077's own [u-dots] tokens (L15:0 and L08:3; GAPS45 read dots 17/17 on this class), cut as
  single-sign tiles (crops below), upscaled 2x;
- the left-page M and N tiles (GAPS49 a, b) upscaled 2x (Lanczos); everything else as GAPS49 (same crop files c, d, f, g).
Crops of the two new tiles (pasted commands):
  python3 tools/iiif_lines.py --image ciphers/na-suriname-map-1781/images/2077_legend_native.jpg --region 45,1538,70,85 --out ciphers/na-suriname-map-1781/images/crops_gaps55 --prefix g55_u1 --centres 42 --lines-per-crop 1 --max-width 1200
  python3 tools/iiif_lines.py --image ciphers/na-suriname-map-1781/images/2077_legend_native.jpg --region 495,822,65,88 --out ciphers/na-suriname-map-1781/images/crops_gaps55 --prefix g55_u2 --centres 44 --lines-per-crop 1 --max-width 1200
Tiles built by build_tiles.py, shuffled T1-T8 (seed 20261058), mapping in blind_key.json (not shown to the reader).
Reader: one blind Opus 5.5 vision call, brief.md (shapes only; no letters, rows, values, documents or hypothesis).
Note: the 2077 tiles come from a different sheet (map legend) than the key-sheet tiles; the reader is told the tiles come
from 18th-century handwritten sheets, not which.

Gate (scored first): BOTH dots-control tiles (u1, u2) reported dots (count >= 1) at conf >= 0.6; AND both no-mark controls
(f, g) reported none (stroke_from_line_above counts as none). Fail -> "non-test (mark-reading gate failed)", nothing
changes, and since this is the second attempt with the same instrument (blind tile mark call), the M/N row-mark call is
logged [retired] for this instrument (rule 3 third-attempt clause applied at the second failure, per the prompt), and the
next step names new material.

Outcomes (a page's M or N tile counts as dotted only at dots with confidence >= 0.6):
  A  N dotted, M not, on both pages -> key stands; [u-dots] = n stays H. No value change.
  B  M dotted, N not, on both pages -> M/N row assignment swapped: [u-dots] -> m at H (17 tokens) via
     key_period_codes_nieuw.tsv, decode_key --check, GAPS23 gate re-run unchanged, AUDIT item 4 propagation note.
  C  both M and N dotted on a page AND the reader groups that page's M and N tiles as the same sign -> the sheet does not
     separate M from N for this sign: [u-dots] -> two-valued n|m at M (17 tokens), applied as in B.
  D  anything else (incl. pages disagree, both dotted but grouped different) -> no value change; logged per page.
Grouping of u1/u2 with key-sheet tiles is reported, non-gating. Context (16/17 want m) is not used to choose an outcome.
Rule 10: report only.
