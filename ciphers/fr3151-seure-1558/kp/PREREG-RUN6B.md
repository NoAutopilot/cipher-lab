# RUN6-SEURE2 pre-registration (5 Oct 2026, written 05:2x UTC by date -u; committed before any reconciler call)

Worker RUN6-SEURE2 (LANE-RUN6, account 1, Opus 5.5; reconcilers Sonnet), brief `.claude/briefs/runs/2026-10-05-acct1-run6-wave3.md`.
Follows RUN6-SEURE (`PREREG-RUN6.md`, pilot L04/L06 err_R 0.080 PASS). Same per-line protocol, extended to the other 18 lines.

## Units and stop rule (Usage 6)
18 lines (L01-03, L05, L07-20) x 2 independent Sonnet reconcilers + 1 scoring unit. List rate 37 x 0.35 = ~USD 13 > cap 9, so the
brief's rule: price from the first 4 lines (8 calls, using the subagent usage figures the Agent tool returns) and never start a line
that would cross 80% of cap (USD 7.2) or of box (72 min, i.e. 06:33 UTC). Order: lines in number order, R1 and R2 of a line run together.

## Method (unchanged from the pilot)
Per line, inputs in `kp/run6b_inputs.tsv` (A = `f81R_cipher_read.tsv`; B = `f81R_cipher_readB.tsv` translated to A's labels through
the inverse of `err2.json`'s mapping). Each reconciler (blind to the other) sees the line's two half-crops
(`images/kp/f81R_Lnn_s1.jpg`, `_s2.jpg`, 2400 px wide, no network), A and B, and returns one sequence in A's label vocabulary (new shapes
n1, n2 ...) with per-sign source A / B / AB / N. Prompt text: `kp/run6b_prompt.txt`. Output: `kp/run6b_recon.tsv` (same columns as
`run6_recon.tsv`); the pilot's L04/L06 rows are carried in unchanged.

## Measures
- err_R = edit distance / max length (identity labels, `run6_err.py` method), pooled over every line with both R1 and R2. Registered
  caveat (as the pilot): both reconcilers see A and B, so err_R is agreement biased DOWN by shared anchoring, not accuracy; it is a
  lower bound on the reconciled read's true error.
- Also reported: source shares (A/B/AB/N), and A/B err on the same lines for comparison.

## nom_test (only if all 20 lines have R1 and R2)
`kp/nom_test.py` unchanged, the N8-SEU settings: `python3 kp/nom_test.py kp/P.txt kp/f81R_recon_R1.tsv kp/f81R_recon_R2.tsv
kp/result_run6b.json --err 0,E2,E,0.242 --ctl-seeds 3 --ctl-draws 20 --draws 200` with E = measured err_R (3 dp), E2 = E/2.
0.242 is added (the only setting change) as the anchoring bracket: err_R is a lower bound, and the prior control crossed from 2/3
(0.242) to 0/3 (0.484).
- Control power (rule 3, 0%-null arm): the target result is a TEST only if the control passes >= 2/3 keys at E AND >= 2/3 at 0.242
  (the measured err_R cannot be trusted as the true error, so the bracket must reach the last level where the control still reads).
  If it passes at E but not 0.242: "non-test above the agreement figure" -- a miss is not a negative.
- The 10%-null arm failed 0/3 at every error including 0 in N8-SEU; any target miss is therefore conditional on no null signs.
- Target gate (N8-SEU, unchanged): a reader PASSes iff S* > p95 AND > max of BOTH shuffled and rotated nulls (200 draws each);
  H-span-under-nomenclator licensed iff R1 or R2 passes. PASS -> draft key fragment at C (letters only where P is read H, M
  otherwise), VERIFIER WANTED. FAIL with control power -> negative conditional on the H-span, the reconciled reads and no nulls;
  not a design-family negative.
- Not all 20 lines reconciled -> nom_test NOT run; remaining line count and cost reported.
