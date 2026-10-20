# PREREG MONL-KING3 (20 Oct 2026, addendum to PREREG-MONL-KING2.md; written and pushed before any c258 L11-L25 crop is cut or read)

Question: with f.133 (Gallica c258) L11-L25 added, does any decoded run under key.tsv (Tomokiyo's Cipher 1 table, unchanged) clear the
registered S bar, and does the L11-L25 band read as French under the key the way L01-L10 did?
Instrument: unchanged. Same script (king2/king2_score.py, no edits), same statistics (run = longest fr16 lexicon run in letters; lm = fr
4-gram mean log10 per letter), same null (20 value-shuffled keys, seed 133, p95), same positive control (f.138r-v windows at the scored
file's own keyed N; window 1 must beat its null on both), same noise bracket (r = this band's measured pass A/B disagreement), same gate
(control window 1 passes AND target beats null on both AND target >= range minimum on both).
Scored files: (a) band L11-L25 alone, king3/c258_L11-L25.tsv, `king2_score.py --target ../king3/c258_L11-L25.tsv --noise r --out
../king3/results_band.json`; (b) L01-L25 jointly, ciphertext_c258.tsv extended (L01-L10 rows unchanged), `--target ../ciphertext_c258.tsv
--out ../king3/results_joint.json`. Each is gated on its own.
S bar (unchanged, king2/king2_grade.py, no edits): a keyed token is S only inside a lexicon run longer than BOTH the longest run any of the
20 shuffled keys yields on the same tokens AND 42 letters; computed on the joint L01-L25 file; M otherwise; U unkeyed. A gate FAIL on the
joint file means no grades beyond M for the new lines.
Transcription: tools/iiif_lines.py crops of c258 L11-L25 from the native page (overlay checked), pass A and pass B blind with the
king2 prompt template (one call per 5 lines per pass, 6 calls), tools/reconcile_passes.py, one reconciliation call on the split positions.
Stop after L11-L25.

## Decision
Belief: f.133 is Cipher 1 under the published key (MONL-KING2 gate PASS on L01-L10); more lines give a run the chance to clear the S bar.
Would change it: the joint L01-L25 file failing the gate (run or lm at or below shuffled-key p95, or below the f.138 range minimum) with the
control passing; or the L11-L25 band alone failing while its noise-bracketed control still beats its null in >= 50% of draws.
Observed: <pending>
Decision: <pending>
Lesson: <pending>
