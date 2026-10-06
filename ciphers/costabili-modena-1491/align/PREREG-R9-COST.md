# PREREG R9-COST, 6 Oct 2026 (written and pushed before any q crop is cut or read, and before any split outcome is computed)

Target: the label `q` on R1166 P1, P2 (N8-COS group crops, passes as relabelled by N9-COS2: n9cos2_pass{A,B}_W.tsv) and P4 (R8-COST
segment crops, r8cost_reads/pass{A,B}.tsv). Images re-fetched scratch-only by one DECODE browser login; sha1 checked against images_manifest.tsv.
No new full transcription: only the crops (same boxes: n8cos_boxes.tsv with n9cos2_boxes_fix.tsv; r8cost_boxes.tsv) in which either earlier
pass read at least one `q` are re-read, and only for the q-labelled signs.

Split criterion (fixed here): readers see a crop and are told only how many q-like signs (bowl with a descender) earlier reads found in its
cipher line. For each q-like sign, left to right, they answer two features: F1 bowl CLOSED or OPEN (a visible gap in the bowl), F2 descender
STRAIGHT or TURNED (hooks/curls at its foot). Primary split: q1 = F1 closed, q2 = F1 open. F2 is recorded and reported only; it is not used to
re-split if the primary split fails (no knob change after outcomes).
Readers: two blind Sonnet calls per page (pass A crops in page order, pass B reverse), P1, P2, P4 -> 6 calls; no value, gloss text or key given.
Mapping: the k-th q answer in a crop goes to the k-th `q` in each earlier pass's read of that crop only if the reader's count equals that
pass's q count in the crop; otherwise those q tokens stay `q` (unsplit). A token becomes q1/q2 only when BOTH split passes give the same F1
answer for it; a split disagreement leaves it `q`.
Statistic, filter, control, gate (unchanged from PREREG-N8-COS / N9-COS2): `align/run_align.py` on the relabelled P1+P2 passes;
gloss-shuffle control, 20 seeds (it re-pairs glosses with groups and so can move the agreement statistic); per pass real >= shuffle p95 + 0.20
AND real >= 0.430. C rule per shape: both passes clear the gate and both passes' alignment keys give q1 (resp. q2) the same value with >= 2
agreeing occurrences each; otherwise M.
P4 decode gate (PREREG-N8-COS / R8-COST, unchanged): C coverage >= 0.80, computed by r8cost_score.py on the P4 passes with q split as above and
the key_n9cos2.tsv C values plus any q1/q2 C from this job. Coverage is reported per page (P1+P2 by the same agreed-AND-C rule on the group
crops, P4 by r8cost_score.py), beside the shuffle-control numbers.

Stated before any read (arithmetic on the committed R8-COST score, not an outcome): P4 has 188 aligned positions, 135 covered; q has 15 agreed
tokens. Even if every one of them became C, coverage would be 150/188 = 0.798 < 0.80, so **the P4 gate cannot pass from the q split alone**;
it also needs TT (9 agreed tokens) or a re-read of the 21 split positions. This job is still run for the key (q1/q2 at C on P1/P2) and to log
the number; a P4 FAIL is logged, not re-tuned (rule 3 third-attempt clause).
Grades: no reading is written unless the gate passes. Reconciliation by this worker licenses M at most.
