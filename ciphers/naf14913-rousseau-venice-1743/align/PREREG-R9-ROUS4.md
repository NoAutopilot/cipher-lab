# PREREG R9-ROUS4 -- count-vector gate re-registered with a same-class planted known-answer (6 Oct 2026, account 2, LANE-RUN9-account-2)

Written and pushed before `align/r9rous4_plantgate.py` is run on anything. Disk only, no network. Supersedes the known-answer
clause of PREREG-R8-ROUS3 only; units, normalisation, statistic, controls (s) and (g), and the per-candidate PASS rule are unchanged
(same script logic, imported, 2000 draws per control).

## Why
R8-ROUS3's licence used the only eligible C whole-word values (de, et, se): short function words, 0/3 recovered, the wrong class to
show power for a long rare word. A pre-run listing of slip words with >= 5 letters and 4-8 tokens over the four slips (6 Oct 2026,
this job) returns only republique (2,1,2,2) and venise (1,1,1,1), the two candidates themselves, so no real same-class known answer
exists on disk. Hence a planted one.

## Planted known-answer (per candidate, its own class)
Class of a candidate with slip vector u: vectors with every pair count in 1..3 (all four pairs nonzero, as for both candidates) and
total within sum(u) +/- 1. For 605/republique: totals 6-8; for 739/venise: totals 3-5 (vectors with a 0 excluded, so effectively 4-5).
40 plants per class, vector drawn uniformly from the class with replacement, seed 9 (random.Random(9), plants for 605 drawn first).
Each plant: a synthetic word `zzplant` inserted v_p times at uniformly random positions in slip p's token list, and a synthetic code
`9999` written over v_p uniformly random groups of passage p, chosen among groups that are not 605, 739, 52 or any key.tsv C code
(passage lengths unchanged; the overwritten groups' own counts drop, which can create or break other codes' vector ties).
The full gate is then re-run on the planted data: MATCH, UNIQUE (against every code on the planted passages), p_s and p_g from fresh
2000-draw (s) and (g) redeals of the planted pools (draw seed 9 + plant index). A plant is RECOVERED under the R8-ROUS3 rule
(MATCH and UNIQUE and p_s <= 0.05 and p_g <= 0.05).
The control can fail differently from the target: recovery depends on the plant's own vector (low totals cannot reach p <= 0.05),
on uniqueness against the real codes after planting, and on the redealt pools; it is not a copy of the candidate's numbers.
It measures power on a true whole-word code of the class written by its code at every occurrence; it does not model a word
sometimes spelled out instead (that failure mode is MATCH-false, which the gate already reports as FAIL, not PASS).

## Licence and verdict
Licence for a candidate: recovered plants of its class >= 32/40 (0.80). PASS for a candidate = its own R8-ROUS3 numbers recomputed
here (MATCH, UNIQUE, p_s <= 0.05, p_g <= 0.05, original unplanted data, draws seed 8 as in R8-ROUS3) AND its class licence met.
Match but licence not met, or a p > 0.05: NON-INFORMATIVE. No match: FAIL. Both numbers (candidate p_s/p_g and class recovery
fraction) reported side by side.

## Consequence
PASS: the value enters key.tsv at grade C (period slip as known plaintext, count-level, control-backed; note "count-vector gate
R9-ROUS4, pending VERIFY"), reading regenerated, `tools/decode_key.py <folder> --check` exit 0, ROOM flag for a verifier (reading
changed after AUDIT.md). FAIL / NON-INFORMATIVE: no key entry; logged in NOTES.md. Key 501 is not touched in any case.
