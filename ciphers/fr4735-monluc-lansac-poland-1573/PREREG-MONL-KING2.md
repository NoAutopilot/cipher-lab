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
(appended after the run)
