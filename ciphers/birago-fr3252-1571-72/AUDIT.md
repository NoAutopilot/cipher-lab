# AUDIT: fr.3252 f.47r hash relabels of CEPPO-WITNESS-PAIRS (VERIFY-CEPPO-WP, 3 Oct 2026)

Verifier: worker VERIFY-CEPPO-WP (account 2, LANE-A2PUSH, for the account-3 orchestrator), a separate session from the
solver CEPPO-WITNESS-PAIRS (1942dc4d, PREREG e1760f2e). Brief `.claude/briefs/runs/2026-10-03-acct3-verify-ceppo-wp.md`.
Clock read 01:39 UTC at start. Disk only: 0 network requests, 0 subagents. No novelty class is assigned or changed here.
f.87 (fr.3251) is audited in `../ceppo-nevers-fr3251-1570s/AUDIT.md`, last section.

**Claim under audit.** Six f.47r hash tiles that the two blind readers labelled S88 (t) against S75/S60, and that the third
reader (NEVBIR-47C) left UNSETTLED, are upright-stem hashes: L03.6, L04.32, L08.38, L10.10, L10.35, L12.29. The witness
rule R-hash (upright = S24 o, slanted = S88 t) makes them S24 (o). Proposed sequence `harvest/witness_pairs/f47_passE.tsv`.

## 1. The witness rule, second eye
`harvest/witness_pairs/w36v_x1000_y120.jpg` (fr.3252 f.36v top, 2.5x) read by this verifier's own eye. On line 2, the
slanted-stem hash carries a gloss **t** and the upright hash next to it carries **o**. On line 3, another upright hash
carries **o**. That is 3 of the solver's 6 hash tallies, reproduced independently. Grade M (one more eye; no period key).
The gloss over the barred 8 in this crop was not legible enough for this verifier to confirm R-8 here.

## 2. The six tiles, by eye
Composites cut from `images/f47/recut/` (2x, autocontrast; not committed):
| tile | context (passE) | stem | slanted hash nearby for contrast |
|---|---|---|---|
| L03.6 | S49 [x] S47 | upright | - |
| L04.32 | S23 [x] S57 | upright (at the strip edge, bars partly cut) | - |
| L08.38 | S84 [x] S89 | upright | L08.35 slanted |
| L10.10 | S57 [x] S35 | upright | L10.4, L10.6 slanted |
| L10.35 | S74 [x] S49 | upright | L10.42 slanted |
| L12.29 | S74 [x] S23 | upright | L12.37 slanted |
All six are upright, and the slanted form on the same lines is plainly different. Rule (i) is met for all six.

## 3. Re-derivation (rule 7)
`decode_control.py harvest/witness_pairs/f47_passE.tsv --extra X_THETA2=r --out ...` reproduces
`f47_reading_passE_s1/s2/s3.txt` byte for byte. (This folder has no decode.json; decode_control.py is the f.47 decoder.)

## 4. Controls at fresh seeds (the solver used 1-3)
- Key control at the two-reader error 0.33 (200 shuffles, 20 windows): seeds 4/5/6 give z **4.56 / 4.87 / 5.31**, rank
  **1/201** in each, power **20/20** (z median 7.61-7.95). The real key's score is -1.5133 (passD -1.5267).
- In-family flip control (the same 6 S88 -> S24 flips at random S88 positions, base = passE with the six put back to S88,
  1000 draws): seed 7 **0/1000**, seed 8 **0/1000** (p 0.001). The specific tiles the rule picks beat random hash flips.
  This is the control the solver could not run on f.47 (base passD has '?' there); it is the strongest number here.
- Judge (solver's run, not changed by this audit): `FAIL language: score=-1.524, null_p99=-1.788, real_p05=-0.906,
  real_median=-0.826, mode=both, N=782` (passD -1.543). Gate (iii) "judge not worse" is met.

## 5. Ruling
**Accepted: all 6 as S (o).** Endorsed S on f.47r: **0 -> 6 of 771**. Grades on the endorsed sequence `f47_passE.tsv`:
S 6, M 751, U 13. H 0, C 0. Cryptanalytic result with a published key; not a reading of the letter (judge FAIL). The
committed passD files are left as the record; `harvest/witness_pairs/f47_passE.tsv` is the endorsed sequence.

Not endorsed by this audit: R-8 and R-6 on f.47r (28/28, 39/39). Those agree with the third reader, but their shuffle
control is non-discriminating by construction (the solver says so), and S74 = m rests on elimination. Nothing was
relabelled there, so there is nothing to endorse.

## For the orchestrator (VERIFY-CEPPO-WP, f.47r)
- Verdict: **6 accepted**, endorsed S 0 -> 6. PROGRESS.tsv "Birago 1571 fr.3252 f.47" set from this section. status.json is yours.
- Still open: S74 = m by elimination (a legible gloss over a blob-6 on f.36r/f.37r would settle R-6), and S76/S91 has no rule.
