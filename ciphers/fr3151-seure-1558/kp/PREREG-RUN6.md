# RUN6-SEURE pre-registration (5 Oct 2026, ~05:10 UTC by date -u; committed before any reconciliation call)

Worker RUN6-SEURE (LANE-RUN6, account 1), brief `.claude/briefs/runs/2026-10-05-acct1-run6-wave2.md`.
Question: can a reconciliation pass of readers A (`f81R_cipher_read.tsv`) and B (`f81R_cipher_readB.tsv`) bring the f81R
two-reader error below the N8-SEU control's power line (~0.24, control 2/3 at e=0.242), so `nom_test.py` can be re-run unchanged?

## Unit count and cap (Usage 6)
Per-line A/B err (err2.py method, N8-SEU mapping): all 20 lines disagree (0.26-0.72; pooled 0.484). Full reconciliation =
20 Sonnet line calls x 0.35 + 1 unit = ~USD 7.4 > cap 3.5. So this job is a PILOT: 2 lines x 2 independent reconcilers
= 4 Sonnet calls + 1 reconciliation unit = ~USD 1.75 (+ orchestration), under the 80% line (2.8).

## Lines (rule fixed before any call)
The first two lines in order whose A/B err is within +-0.10 of the pooled 0.484 (representative, not easiest): L04 (0.538),
L06 (0.480). Crops: images/kp/f81R_L04_s1/s2.jpg, f81R_L06_s1/s2.jpg (existing, 2400 px wide; no network).

## Method
Each reconciler (Sonnet subagent, blind to the other reconciler) sees the line's two half-crops, reader A's and reader B's
sequences (B translated to A's labels through err2.json's mapping where one exists) and returns one sequence in A's label
vocabulary (new shapes as n1, n2 ...), with per-sign source A / B / both / neither.
Measure: err_R = err2.py method (edit distance / max length, identity labels) between R1 and R2 on L04+L06 pooled.

## Gate
- err_R < 0.24 -> pilot PASS: the reconciliation instrument is worth the full 20-line pass (~USD 7.4 one reconciler/line + a
  second reconciler on a sample); nom_test.py is still NOT re-run in this job (it needs all 20 lines; a 2-line read cannot feed it).
- err_R >= 0.24 -> pilot FAIL: logged as the measured err; reconciliation by Sonnet with A/B in view does not reach the power
  line at this capture; next step names the owner's sign sorter on f81R tiles (TRANSCRIPTION.md), not a third machine pass.
Caveat registered now: R1 and R2 both see A and B, so their agreement is biased UP (shared anchoring); a PASS is necessary,
not sufficient, and agreement is not accuracy (TRANSCRIPTION.md). Also reported: share of signs each R takes from "neither".
