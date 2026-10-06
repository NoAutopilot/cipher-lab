# PREREG R7-OLDA (6 Oct 2026, written and pushed before any blind pass was read)

Job: R7-OLDA (LANE LANE-RUN7-account-2), step (a') of the folder's Verdict after OLD-ES17A: crop-and-read pass on blocks
A (leaf 001, folio 54) and C2 (leaf 006, folio 56). Crops: `images/crops_AC2/` (A: 11 lines x 3 segments; C2: 8 lines x 3
segments plus `C2_L09_s1.jpg`, cut by hand for the trailing word under line 8), commands in NOTES.md section 13.

1. Two blind passes, Sonnet subagents, crops only (no key, no reading, no prior transcription, no full-page image), one
   block (leaf) per call: pass A reads the lines in order, pass B reads them in reverse line order. Notation given (not a
   reading), same as PREREG_OLD-PASS2 item 1: Latin cursive letters as letters; digit-like signs as digits; the G-shaped
   ligature as `l7`; a superscript small a as `^a`. Every word on the line is transcribed, plain or cipher. Output: block,
   line, position, token, confidence high/medium/low.
2. Normalisation of both passes alike: PREREG_OLD-PASS2 item 2 (lowercase; drop punctuation and spaces; V.Sa forms -> `@`;
   final `5` -> `s`; `6` -> `b`; other `^a` -> `a`), via `transcription/diff_pass2.py`'s `norm_tok`.
3. Figure (gate): per-sign disagreement between pass A and pass B = sum over lines of the Levenshtein distance between the
   two normalised line strings / sum over lines of the mean of the two line lengths; reported per block and for A+C2.
   Agreement between two readers, not accuracy (TRANSCRIPTION.md).
4. Rule (brief, CLAUDE.md Usage 6): if A+C2 disagreement > 10.0%, the job stops after reconciliation: the reconciled
   draft is committed under `transcription/` only, the committed `ciphertext.tsv` A/C2 rows and the reading are NOT
   replaced, and the split is logged for the owner's sign sorter (no third machine pass). If <= 10.0%, the reconciled
   text replaces the A and C2 rows of `ciphertext.tsv` (old rows kept as `transcription/ciphertext_AC2_pre_R7OLDA.tsv`,
   A/C2 overrides retired the same way A2-OLD retired B/C1's), decoded with the existing route
   (`scripts/apply_key.py ... --check`), graded, judged with es17a (unknown reliability per OLD-ES17A's fold result).
5. Reconciliation: `tools/reconcile_passes.py` on the two passes; one reconciliation unit settles each listed position
   by eye on its crop: a sign the crop supports is kept, otherwise the token is marked `uncertain` (grade M). No sign is
   chosen because it decodes to a better word.
6. Not gating, reported only: reconciled A/C2 vs the committed A/C2 rows, whole-block normalised Levenshtein (the
   committed rows carry no line numbers and omit plain words, so this is a rough figure).
