# PREREG -- R10-ROELL12, 6 Oct 2026 (written and pushed before any overlap was computed)

Question: is DECODE R1469/R1470 ("9 Feb 1809", catalogued NA 1.02.20 inv. 804) in the same code as DECODE R2131
(Van Dedem to Van de Spiegel, Pera 9 Feb 1793, NA 3.01.26 inv. 212, one 50-group cipher paragraph)? A shared code would back
R10-ROELL11's inference that R1469 is Van Dedem's 9 Feb 1793 despatch.

Inputs (all transcriptions, rule 2; no image read): `decode_transcription/R1469_groups.txt`, `R1470_groups.txt` (Bourdeau's parse of
DECODE/SofPe); `r2131/R2131_cipher.txt` and the 1788-89 Van Dedem family texts `r2131/R1947_cipher.txt`, `R2053_cipher.txt`,
`R2121_cipher.txt`, `R2122_cipher.txt` (Bourdeau's transcriptions, dbourdeau/cyphersolver targets/dedem1788/tx, MIT/CC BY 4.0, copied
unchanged 6 Oct 2026). Comment lines (#) and '?' dropped; groups = digit runs.

Query set Q: R2131's distinct groups minus the frame/indicator groups 701, 801, 301, 401, 501, 601, 2504, 2604, 2704 (Bourdeau's
named nulls/indicators).
Statistic S(P) = |Q intersect distinct(P)| for a reference pool P.
- Target: P = ROELL = R1469 + R1470.
- Positive control: P = FAM = R1947 + R2053 + R2121 + R2122 (DECODE links R2131 to these as one codebook; Bourdeau found 52% of
  R2131's groups in them).
Nulls (each 10,000 draws, seed 20261006), applied to both pools:
- N1 jitter (the gate): each q in Q replaced by q + d, d uniform in [-50, 50] minus {0}, clipped to 2..3839, distinct set re-drawn
  on collision -- keeps R2131's magnitude profile, varies the values, so S can differ from the target's.
- N2 uniform: |Q| distinct values uniform in 2..3839 (reported, not gated).
Gate (both pools judged against their own N1):
- Positive control must give S(FAM) > N1 p99. If not: non-test at N=|Q| ("R2131 too short to detect a shared code by overlap").
- If the control passes: S(ROELL) > its N1 p99 -> "shared code backed (S)"; S(ROELL) <= N1 p95 -> "R2131's code not detectably
  shared by R1469/R1470 at this N, control-backed"; between p95 and p99 -> "undecided".
Descriptive only (no gate): positions of the frame/opener groups (701, 801, 301-601, 2504/2604/2704) in R1469 and R1470.
Not run, stated now: a crib decode of R1469 against the inv. 804 clear copy (scans 150R-152R) -- no key for the 1788-93 family exists
in this folder, a sibling, or Bourdeau's targets/dedem1788 (his aligners found no consistent values).
Script: `r2131/overlap_test.py` (writes `r2131/overlap_result.tsv`).
