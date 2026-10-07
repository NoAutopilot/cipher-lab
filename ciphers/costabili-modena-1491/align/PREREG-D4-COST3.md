# PREREG D4-COST3, 7 Oct 2026 (written and pushed before any reader call on the cipher crops and before any score)

Target: R1167 P2 page lines 22-29 (cipher; never read or scored by any job) against the clear copy P6 lines 1-5 (the copy's last page;
the copy of P2's earlier lines is on P5 and is not used). Crops (run before this file was written):
`python3 tools/iiif_lines.py --image IMG_R1167_I5858_P2.png --region 420,2640,1860,720 --out c2 --prefix c2 --ink 90 --prominence 30 --debug`
(9 lines: c2_L01 = page line 21, c2_L02..L09 = page lines 22-29) and
`--image IMG_R1167_I5862_P6.png --region 240,780,2000,560 --out k6 --prefix k6 --ink 90 --prominence 30 --debug` (k6_L01..L05 = copy lines 1-5).
Images: one DECODE browser login 14:46 UTC, R1167 P2/P6, sha1 = images_manifest.tsv, scratch only.
This worker looked at c2_L01-L09 at line-crop scale (no transcription written) to place the anchors: c2_L01's last groups stand where the copy's
P6 L1 opens ("li furono donate"), the clear words "ma como ho dicto de s." on c2_L08 stand where the copy has "ora como ho dicto de sopra" (P6 L4),
and c2_L09 ends where the copy's L5 has "succedessono ad" (the cipher letter continues on P3).

## Clear copy, P6 lines 1-5 as read by this worker (sigla shown as written; ? = uncertain word, kept as read)
L1 li furono donate a dixe serendo? ch ha Referito ch se sua m.ta ne mandasse multo ge
L2 piaceriano: et cussi geli mando: ch cussi passano le cose d sua m.ta lequale pobe?
L3 qua se procede cu in ogni cosa diffusamente da li modi de los?, pareria essere ch
L4 succedessono ad uotum et ad io priaria, ora como ho dicto de sopra alcuno buono sigale
L5 nō li appare: et quando dio volesse ch le succedessono ad uotum nō se crede ch

## Expansion table (PREREG-D4-COST2's, unchanged, plus three sigla met on P6 L1-5; fixed here before any score)
PREREG-D4-COST2's table (del, de la, non, per, personalmente, perche, che, questa/quella, maesta, u/v) applies unchanged. Added from P6's own usage:
| siglum as written | expanded | evidence |
|---|---|---|
| d (with stroke) before "sua" | de | "de" written out L3 ("de los"), L4 ("de sopra") |
| cu (with stroke) | cum | the standard siglum; "cum" written out P5 L9 (PREREG-D4-COST2) |
| et (ampersand-like) | et | "Et" written out P5 L5 |
"sigale" is kept as written (no siglum). Any further siglum met in a span and not in this table drops that span before scoring.

## x-marker rule (registered here, before any read; D4-COST2's named fix)
A `{CODE}` token written immediately after an `x` (same line, next token) is part of the x and is removed with it; it is not counted as a
`{CODE}` marker. (No span below is cut at x or {CODE}, so this rule only governs removal.)

## Spans (sign stream = the pass's groups for c2_L01..L09 in order; `{CLEAR}` and `{CODE}` are markers, removed from the sign string; x removed)
- w1: from the first token of c2_L02 to the first `{CLEAR}` on c2_L08 (exclusive), clear =
  "a dixe serendo che ha referito che se sua maesta ne mandasse multo ge piaceriano et cussi geli mando che cussi passano le cose de sua maesta lequale pobe qua se procede cum in ogni cosa diffusamente da li modi de los pareria essere che succedessono ad uotum et ad io priaria"
- w2: from after the last `{CLEAR}` on c2_L08 to the end of c2_L09, clear =
  "alcuno buono sigale non li appare et quando dio volesse che le succedessono ad"
A pass with no `{CLEAR}` on c2_L08 loses both spans. A `{CLEAR}` token inside w1 (other than on L08) is removed as a marker.

## Statistic, control, gate: D4-COST's, unchanged
`align/d4cost3_score.py` imports `nw`, `stat`, `load_key` from `align/d4cost_score.py` unchanged: NW, +2 C value == letter, -1 differs,
0 non-C sign, gap -1; real = share of C-valued sign tokens aligned to their own letter; null = the clear span's letters shuffled within the span,
20 seeds; gate per pass: pooled real >= null p95 + 0.20 and >= 4 C-valued tokens per span on average. Key: align/key_n9cos2.tsv C values.

## New values (D4-COST conditions a-d and the q rule, unchanged)
(a) both passes clear the gate, (b) the sign aligns to a letter >= 3 times in each pass, (c) same modal letter in both passes with share >= 0.6
in each, (d) the modal letter occurs for that sign in both spans w1 and w2. TT (s?) and Z (t?) tested; q goes to C only if q itself meets (a)-(d).
If any value passes: align/key_d4cost3.tsv = key_n9cos2.tsv + new C rows (occurrences cited), and R1166 P4 is re-scored:
`python3 align/r8cost_score.py align/r8cost_reads/passA.tsv align/r8cost_reads/passB.tsv --key align/key_d4cost3.tsv`; the number is reported
against 0.80, gate not moved. If (a) fails: rule 3 third-attempt clause, the alignment instrument for these signs is logged [retired] at this
transcription quality.
Readers: two blind Sonnet calls over the 9 line crops (A top-down, B bottom-up), labels.tsv + RUN3-COSK2 dash convention, no value, no copy, no key.
Units: 2 Sonnet reader calls + scoring; cap 3.5.

## Amendment 1 (7 Oct 2026, written after pass A's hand-back note, before any score and before this worker opened either read)
Pass A's hand-back said its c2_L09 crop is "essentially empty". Re-checking the crop centres printed by `tools/iiif_lines.py` (6 97 190 276 372
467 566 634 706) against the debug overlay: the crops are c2_L01 = page line 21, c2_L02..c2_L08 = page lines 22-28, and c2_L09 = blank margin.
The PREREG above mislabeled them by one from c2_L03 on: "ma como ho dicto de s." is on **c2_L07**, and the last cipher line (page 28) is c2_L08.
**Registered run (as written above): non-test** -- the spans are cut at a {CLEAR} on c2_L08, which carries none, so both spans drop in both passes
by the rule (the scorer is run unchanged and its output reported).
**Amended run:** the same spans with the line index corrected: w1 = first token of c2_L02 to the first {CLEAR} on c2_L07 (exclusive); w2 = after
the last {CLEAR} on c2_L07 to the end of c2_L08 (c2_L09 ignored). Clear text, statistic, gate, x-marker rule and conditions (a)-(d) unchanged.
Because this amendment follows a reader's hand-back note, a value that passes (a)-(d) in the amended run is reported as **C-eligible pending
the lane orchestrator's ruling**, and is not written to key.tsv by this worker; the R1166 P4 re-score is still run on a scratch key and reported.
Scorer: `align/d4cost3_score.py --l7` selects the amended indices.
