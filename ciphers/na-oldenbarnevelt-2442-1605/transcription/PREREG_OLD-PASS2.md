# PREREG OLD-PASS2 (3 Oct 2026, written and pushed before any blind pass was read)

Job: second full blind pass over the block B and C1 line crops (`images/crops_BC1/`, 22 B + 28 C1 crops, cut with
`tools/iiif_lines.py`, commands in NOTES.md section 11). Committed transcription = the B/C1 rows of `ciphertext.tsv`
(A2-OLD's passD).

1. Blind pass: three subagent calls (B lines 1-6; B lines 7-11; C1 lines 1-7), crops only, no key, no reading, no prior
   transcription. Sign convention given to the reader (notation, not a reading): letters as Latin cursive letters;
   digit-like signs as digits; the G-shaped ligature as `l7`; a superscript small a as `^a`. Output: one token per row,
   line, position, token, confidence high/medium/low.
2. Normalisation of BOTH sides before the diff (rule 3, PX-BRODEC lesson): lowercase; drop `, . ; : - |` and spaces;
   `V.Sa`, `vsa`, `2s^a`, `25^a`, `2s a`, `25a` -> one symbol `@`; `5` in final position of a token -> `s`; `6` -> `b`
   (A2-OLD's settled conventions, applied to both sides alike); every other `^a` -> `a`.
3. Figure: per-sign disagreement = (substitutions + insertions + deletions in a per-line Levenshtein alignment of the
   normalised sign strings) / signs in the committed line, summed over B and C1 and reported per block. This is
   AGREEMENT between two readers, not accuracy (TRANSCRIPTION.md). `tools/reconcile_passes.py --split-chars` is run on
   the same two normalised files for the disagreements list.
4. Settling: every disagreement is settled by eye against its crop. Committed sign kept if the crop supports it; changed
   if the crop clearly supports the blind sign; otherwise the token's confidence becomes `uncertain` (grade M). No
   sign is changed because the change decodes to a better word.
5. Decode re-run with `scripts/apply_key.py ... --check` after any change; reading change -> AUDIT.md propagation note
   and SECOND-OPINIONS-QUEUE.tsv row SO-OLDEN-2442-BC1 (rule 10 propagation).
