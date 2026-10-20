# PREREG MONL-KING2 (20 Oct 2026, written and pushed before any f.133 line is fetched or read, and before the control is run)

Question: does f.133 (Gallica c258) L01-L10, transcribed in two blind passes and decoded with key.tsv (Tomokiyo's Monluc Cipher 1
table, unchanged), read as French under that key -- i.e. is the king's 28 Apr 1573 letter in Cipher 1?
Script: king2/king2_score.py (statistics, null, control and gate are defined in its docstring; nothing in it changes after this push
except bug fixes, which are logged in the Decision block).
Statistics: (1) run = longest run in letters of fr16 lexicon words >= 2 letters in the straight key decode (tools/segmenter.py);
(2) lm = judge_plaintext's mean log10 4-gram score per letter on the fr corpus (the spec's judge language). Also reported, not
gated: `tools/judge_plaintext.py specs/fr4735-monluc-lansac-poland-1573.json --file` on the target decode.
Null: the same tokens under 20 value-shuffled keys (key.tsv's plain column permuted over its ids), p95 per statistic.
Positive control (must pass first): the f.138r-v decode (ciphertext_c268.tsv + ciphertext_c269.tsv, sign column), cut into
non-overlapping windows of the target's keyed-token count N; window 1 (c268 from L01) must beat its own null on BOTH statistics.
Run first at N = c268 L01-L10's keyed count before any image is fetched; if window 1 fails there, stop: no requests, no reads
(the instrument cannot see this key at this length). Range = [min, max] over all windows under the true key.
Noise bracket (rule 3): the control is re-run with a share r of keyed tokens replaced at random, r = the target's measured pass A/B
disagreement; reported beside the target. A target FAIL is read as "not Cipher 1 / not readable" only if the noise-injected control
still beats its null in >= 50% of 20 draws; otherwise the FAIL is "untestable at this transcription error".
Gate: control window 1 passes AND the target beats its null on both statistics AND the target sits in range (each statistic >= the
range minimum). Pass -> per-token grades (S where the key reads in a clause above the authentication distance; M otherwise),
reading_c258.txt, decode_key.py --check, judge pasted. Fail -> no grades; name the likeliest cause (reading error, other key,
jargon/nulls) from the numbers.
Secondary, exploratory (not gated, cheap): the target decode placed against f.166 (clear_f166.tsv) and ff.140-141 (clear_f140.tsv)
with king_f166.py's exact-run statistic vs 200 word-shuffled copies (MONL-KING's lesson: the run clause separates, share does not).
Transcription: tools/iiif_lines.py crops of c258 L01-L10 (overlay checked), pass A and pass B blind (one subagent call per 5 lines
per pass), mechanical reconciliation (tools/reconcile_passes.py) + one reconciliation call on the split positions.

## Decision
(Block filled after the run; the PREREG pushed at d3ab538ae had only the heading. Belief and Would change restate the pre-run text above.
Script fixes after the push: none to king2_score.py; the --target path is read relative to king2/.)
Belief: f.133 (c258) is in Monluc Cipher 1 (the king's 28 Apr letter continues the f.132 cipher), so key.tsv should read it as French.
Would change it: the f.133 decode failing to beat its 20 shuffled keys (p95) on run AND lm, or falling below the f.138 window minimum, with
the f.138 control passing and the 16.1%-noise control still beating its null in >= 50% of draws.
Observed: control (f.138r-v, N=356 keyed, 5 windows) all pass; window 1 run 55 vs p95 27, lm -1.409 vs -2.276; range run 31-56, lm -1.630
to -1.292; noise 0.161: 19/20 beat null (run median 55, lm median -1.663). Target f.133 L01-L10 (377 tokens, 356 keyed): run 40 vs p95 31,
lm -1.605 vs p95 -2.213; in range on both -> GATE PASS. Grades: no lexicon run exceeds max(shuffled-key max 38, 42 letters) -> S 0, M 356,
U 21. Judge (spec): language FAIL -1.605 (null_p99 -1.839, real_p05 -0.894), words 0.711 ok. Exploratory placement (exact run vs 200
word-shuffled copies): control c268 L01-L10 vs f.140 16 vs max 12 (placed); f.133 vs f.166 6 vs max 9, vs ff.140-141 8 vs max 11 (neither).
Decision: continue -- f.133 is Cipher 1 under the published key and is not the text of f.166 or ff.140-141; read c258 L11-L40 (the page has
about 40 lines) so a run can clear the 42-letter clause, settling the K04|K12 and K39|K19 look-alikes first.
Lesson: on this design at N~356 the lm statistic separates key from shuffled key by ~0.6 per letter and survives 16% transcription noise,
while the lexicon-run statistic sits only ~2 letters above the shuffled-key max (40 vs 38); at 10 lines a gate PASS does not yet give an
S-grade clause -- size the next read for the clause, not the gate.
