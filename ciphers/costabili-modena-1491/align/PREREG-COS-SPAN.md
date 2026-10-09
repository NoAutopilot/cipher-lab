# PREREG COS-SPAN, 9 Oct 2026 (written and pushed before any score of this job; addendum to PREREG-N9-COS2.md step 2)

Worker COS-SPAN (account 4, Opus) for LANE DEFAULT-account-4-20261009-1340, job J8. Material: the R1163 P2 cipher slip vs R1163 P1 clear
slip, and the R1165 P5 postscript slip L05-L10 vs R1165 P4 clear slip, as in N9-COS2 step 2.

What changes from N9-COS2 (the one instrument change, the Verdict's named next step): span granularity. N9-COS2 paired all cipher signs
between two consecutive clear-word anchors with all clear-slip letters between the same anchors, so spans ran over several lines and the
0.8-1.25 ratio filter left 2 (A) and 4 (B) pairs. Here, inside each anchor span, the reader's own cipher groups ('|' boundaries; a clear
word and a line end are also boundaries) are paired with the clear-slip words by a monotone DP **on lengths only** (no sign value, no key):
chunks of k groups to l words, 1 <= k, l <= 3, k + l <= 4, cost |signs - letters| / letters + 0.1 (k + l - 2), an unpaired group or word
cost 1.0. Each chunk is one pair. Script: `align/cosspan_pairs.py` (anchor rule imported unchanged from `align/n9cos2_slip_pairs.py`).
Sigla: the clear-slip words are normalised before pairing with the registered table in `cosspan_pairs.py` (SIGLA: p per, ch/chr che, pch
perche, no/nõ non, mta maesta, z et, vra vostra, dl del, dla dela, lra littera, pnte presente), the PX-BRODEC rule of CLAUDE.md rule 3 and
PREREG-D4-COST2's table; any other abbreviation stays as read (its pair usually fails the ratio filter).

Unchanged from PREREG-N8-COS / N9-COS2: `align/run_align.py` (ratio filter 0.8-1.25, `tools/interlinear_align.py align --code-prefix @
--keep-fs`, share of aligned tokens agreeing with the sign's majority value), gloss-shuffle control 20 seeds, gate per pass real >= shuffle
p95 + 0.20 AND real >= 0.430, pooled over both slips per pass; fewer than 4 pairs past the filter in a pass = non-test; C only if both passes
clear the gate and both passes' alignment keys give a sign the same value with >= 2 agreeing occurrences each in >= 2 distinct pairs; a
value already C in `align/key_n9cos2.tsv` is reported, not re-graded; a sign held M for a stated shape reason (q, TT) stays M whatever this
run shows (N8-COS, R9-COST, D4-COST3: the label covers several shapes). Reconciliation by this worker licenses M at most.

Step 1 (0 reader calls): the committed N9-COS2 blind reads `align/n9cos2_reads/r116{3,5}_pass{A,B}.txt` re-paired by the rule above ->
`align/cosspan/pairs_pass{A,B}.tsv`, then `python3 align/run_align.py align/cosspan align/cosspan/pairs_passA.tsv align/cosspan/pairs_passB.tsv`.
Step 2 (fresh short boxes + 2 blind Sonnet passes, one DECODE login) runs only if the step 1 pair count leaves the instrument room
(>= 4 pairs past the filter in both passes) and the orchestrator's cost reading leaves >= USD 2 of the 3.5 cap; otherwise it is the named
next step, with the box rule: one crop per run of cipher between two consecutive breaks (a clear word or a line end), cut with
`tools/iiif_lines.py --image <page> --region <box>` per run. No step 1 number is re-tuned after it is read (rule 3).
Output: any value meeting the C rule goes into `align/key_cosspan.tsv` (key_n9cos2.tsv columns + source); key_n9cos2.tsv is not edited.
