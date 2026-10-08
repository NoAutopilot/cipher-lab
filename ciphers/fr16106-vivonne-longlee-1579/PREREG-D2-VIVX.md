# PREREG D2-VIVX: D4-VIVV's crosswalk fixes applied, then re-score (8 Oct 2026, written and pushed before any re-score)

Change (crosswalk only; key/crosswalk.tsv; the transcription tx/passA.tsv, tx/passB.tsv is not relabelled):
1. Pair row '1+o' = x.g1 (table x = '10'): label '1' immediately followed by a single 'o' reads x. The existing 'o o' -> d
   pair keeps precedence ('1 o o' stays n + d). Counted before scoring: 1 occurrence in pass A (L01), 0 in pass B.
2. '8' gains cc.g1 (m|par|cc); 3. 'H' gains b.g2 (t|g|b); 4. 'z' gains ff.g1 (Ze ligature), becoming multi (e|ff).
   Values are appended after the existing ones, so every first-listed value -- the one the letter stream uses -- is unchanged.
   Consequence stated in advance: fixes 2-4 cannot change the gating score; only fix 1 (one token) and the null's label set
   (one more single-letter label, '1+o') can. Expected: a near-identical score; this is not a new knob.
Gate, statistic, nulls and control: those of PREREG_vivmous.md (nw_score vs copy f.105r, 1000 value permutations seed 1, PASS iff
real > null p99; 5-seed matched control at e=0.576, NON-TEST if < 3/5) and PREREG_vivv.md (text-specific PASS iff real > wrong-text
(fr16 Catherine de Medicis) p99 and > token-order-shuffle p99, control seed 0 clears its own wrong-text max), unchanged.
Compared against: pass A 0.4537 vs p99 0.3998; wrong-text p99 0.448, order-shuffle p99 0.431 (vivmous_result_cw1.json,
vivv_contam_result_cw1.json). Rule 3 third-attempt clause: if the text-specific margin does not widen with every number moving
together, this is the second attempt of this instrument on this transcription; logged in HYPOTHESES.md and the Escalation, no
further tuning.
