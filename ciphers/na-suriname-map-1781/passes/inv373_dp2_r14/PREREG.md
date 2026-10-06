# PREREG addendum R14-SURDP2 (6 Oct 2026, ~16:0x UTC by date -u; committed and pushed BEFORE dp2_run.py is written or run)
Addendum to ../inv373_0746_dp_r14/PREREG.md (R14-SURDP, 1a3b32a91). Same instrument, unchanged: dp_align.py's functions (table,
csigns, gletters, dp, score, A, derange) are loaded from that file as written and called by a short driver, dp2_run.py; the only
additions are (a) tokens starting "[plain" are dropped before alignment (0758 L01 opens with plain words; R14-SUR758's score.py
rule), (b) a line subset, (c) per-run output files. Same tokenising, equivalences, DP (+1 / 0 / gap -0.5, band +-6, tie order),
statistic A, C1 (gloss lines deranged among the run's own lines, 1,000 draws), C2 (within-line permutation, descriptive), gate
SAME SYSTEM (DP) iff A >= 0.50 AND A > C1 p99, else "not shown". Inputs unchanged; no vision, no transcription change, no key edit.
Table T: R14-SURDP did NOT pool 0746 (it wrote dp_sign_table.tsv, DP-derived, not a sign_table.tsv), so T stays pooled
sign_table.tsv letters_seen from the scans named per run, leave-own-scan-out; [y-fam] -> {m, n}.
Runs (each reported with both numbers; each its own gate):
  R1 0758, all 11 pairs (L01-L06, L11-L15) of ../inv373_0758_r14/ (passA_sonnet_blind.tsv, gloss_reconciled.tsv); T = 0693+0702+0730;
     seed 758. (0758's own sign_table.tsv, from 9 positions, is not pooled into any T.)
  R2 0730, the 7 word-unaligned lines L03 L05 L06 L07 L08 L09 L10 (every align_words.tsv row "skip-line"); T = 0693+0702; seed 730.
  R3 0702, the 32 word-unaligned lines L01 L06 L07 L08 L09 L12 L13 L14 L16 L17 L18 L19 L20 L22 R01 R02 R03 R04 R05 R06 R07 R09 R10
     R11 R12 R13 R14 R15 R17 R18 R19 R20; T = 0693+0730; seed 7020.
  Regression check first (must reproduce R14-SURDP's dp.out to 3 d.p., else stop and log a driver fault): 0702 all 42 pairs, T =
  0693+0730, seed 702 -> A 0.966, C1 p99 0.481.
Power floor: a run with fewer than 30 keyed aligned signs is a non-test (R14-SUR758's floor). R2's derangement space (7 lines) is
small but well above 100 distinct derangements (1,854).
Outputs, descriptive, no gate, never applied: per run dp2_<run>_pairs.tsv, dp2_<run>_sign_table.tsv, dp2_<run>_candidates.tsv
(codes whose top DP-aligned letter, >= 3 times, is outside that run's T) for a verifier. conflicts.tsv and key files not touched.
