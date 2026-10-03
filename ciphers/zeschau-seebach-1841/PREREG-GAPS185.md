# Pre-registration: GAPS185 crib test (written 3 Oct 2026 18:08 UTC, before any statistic was computed)

Question: is R5006 (6 Apr 1842, 692 digits, GAPS175/179) enciphered with the same two-digit syllabary as R5005
(Bourdeau's 3,969-digit transcription), so that Bourdeau's 7 published gloss values (11=la, 70=pre, 82=m, 34=i,
29=er, 40=e, 46=que; grade I in his own NOTES, credited) can be applied to it as pins?

Inputs: `transcription/r5006p1_ciphertext.txt` + `r5006p2_ciphertext.txt`, concatenated in page/line order;
R5005 from `sources/cyphersolver/2026-10-03/zeschau1841/ct_R5005.txt`, paired per line with Bourdeau's
`offsets.json` phases (a phase-1 line drops its first digit; a trailing odd digit is dropped).

Parsing of R5006: the concatenated 692-digit stream, phase 0 (346 pairs) and phase 1 (345 pairs). For each
statistic the phase is chosen by one fixed rule: the phase with the higher pair index of coincidence. The same
rule is applied inside every control draw.

Statistics (all one-sided, "greater"):
- T1 (same-key profile): cosine similarity of R5006's 100-cell pair-count vector to R5005's.
- T2 (pin coverage): share of R5006 pairs that are one of the 7 pins.
- T3 (pin profile): Spearman correlation between the 7 pins' counts in R5006 and in R5005 is too small (7 points)
  to gate on; reported only, no verdict.

Matched control (rule 3): 2,000 shuffled-digit versions of the R5006 stream (same 692 digits, same digit
frequencies, order destroyed), each parsed and phase-selected the same way. Shuffling digits changes the pair
counts, so T1 and T2 can differ between target and control (a pair-level shuffle could not: it is identical by
construction for both statistics and is NOT used). Empirical p = (1 + #draws >= target) / (1 + 2000).

Positive control (power at the target's N, ARM3-ADJ lesson): 200 random contiguous 692-digit windows of R5005
(window re-paired with the same phase rule), each scored for T1 against the REST of R5005 (window removed), and
each compared with its own 200-draw shuffled-digit null. Power = share of windows whose p < 0.01. If power < 0.8
the test cannot license a negative at N=692 ("untestable at this N").

Gate: T1 p < 0.01 -> "R5006 shares R5005's pair profile beyond its digit frequencies: consistent with the same
syllabary" (supports applying the pins; it does NOT read any token). T1 p >= 0.01 with power >= 0.8 -> control-
backed "no evidence of the same key at the pair level". T2 is reported with its p but only supports T1.

Grades (rule 4): the pins stay grade I (Bourdeau's rubbed-gloss values). A pass licenses at most M for a pin
token applied in R5006; no S grade for anything, no reading, no plaintext. Script: `crib_test.py` (seeded,
`--check` regenerates `crib_test.json` and fails if stale).
