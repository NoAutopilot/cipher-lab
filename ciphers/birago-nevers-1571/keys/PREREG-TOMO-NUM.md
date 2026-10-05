# TOMO-NUM pre-registration (5 Oct 2026, 13:27 UTC, before any score)

Target: pooled Nov 1571 numerical stream, fr.3251 f.119 + fr.3252 f.100r, 985 digits in 48 runs
(`../../birago-fr3252-1571-72/num/pooled_tokens.txt`, tokens joined per line). Two keys: `tomo_colbert398.tsv` (system A,
Tomokiyo's Colbert 398 table) and `tomo_nevers_no23.tsv` (system B, Nevers no.23, the variable-length system of his 2025/02 post).

Test 1 (both systems) -- segmentation fit. Beam parse of each digit run into the system's codes (A: two-digit codes + single 7;
B: single digits 1-9, the nine two-digit codes, null 0), with a stray option (skip one digit). Objective per digit =
(sum of it16 4-gram log10 P over decoded letters - 2.0 per stray - 0.5 per null/space) / digits. Beam 300.
  - Null: 20 shuffles of the target's own digits (whole pooled stream permuted, run lengths kept).
  - Matched control: 3 synthetic streams (it16dip Italian, 985 digits, 48 runs, 5% stray digits) enciphered with the SAME
    system (A: words split by 7; B: l and dot marks absent, as in the target's digit stream), and 20 shuffles of each.
  - Control gate: every control seed's objective above the max of its own 20 shuffles (3/3).
  - Target FITS if the control gate is met and the target's objective exceeds the max of its 20 shuffles; NO FIT
    (control-backed) if the gate is met and the target does not; NON-TEST if the gate fails.
  Also reported: stray fraction and mean LM per letter.
Test 2 (system A only; B's variable-length codes do not fit a pair cut) -- tools/key_crossmatch.py pair_stats + gate_verdict
on the two phase.py pair files (240 + 274 tokens), gate KEY-CROSSMATCH-CAL (stat 3.292), with the matched control of
num/tools/xmatch_control.py rebuilt for system A's key (3 seeds, em-phase). Reported as coverage, stat, verdict for both.
No reading is claimed either way.
