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
Observed: band L11-L25 (494 keyed): control passes (w1 run 55 vs p95 27, lm -1.413 vs -2.284; range run 47-55, lm -1.529 to -1.342; 13.0% noise 17/20); target run 43 vs p95 35, lm -1.571 vs -2.126, beats null but below range minimum on both -> GATE FAIL. Joint L01-L25 (850): control w1 FAILS (a shuffled key reaches run 79; 2 windows) -> non-test; target run 43 vs p95 35, lm -1.583 vs -2.162. S bar on joint = max(53, 42) = 53; longest run 43 -> S 0, M 850, U 47. Judge FAIL -1.571 (band), -1.583 (joint).
Decision: change -- stop adding lines under this S bar; reduce f.133 transcription error (third pass on the 125 reconciled positions) and re-score; a length-independent S test needs its own PREREG.
Lesson: the S bar's shuffled-key maximum grows with N (38 at 356 keyed, 53 at 850) about as fast as the true-key run, and at N=850 the f.138 control has only 2 windows and window 1 fails; on this design more lines do not buy an S clause -- lower error does. The band's lm sat above its 13%-noise control median while missing the clean range, so the range clause reads transcription error, not key.
