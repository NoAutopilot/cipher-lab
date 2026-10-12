# PREREG-PISA-MERGE (12 Oct 2026, written 18:2x UTC by date -u, pushed in its own commit before any score)

Job: PISA-MERGE, brief .claude/briefs/runs/2026-10-12-ytbiz-default-1810-jobs.md (LANE DEFAULT-A2-1810, account 2). Disk only, CPU only.
Amendment to pisa_rs244/PREREG-PISA-RS244.md, which named these merges as untested. A transcription question (delete tokens a double read
put in tx86), never a key edit: key86.tsv unchanged in every outcome. Base = the committed tx86/ciphertext_f244r.tsv (post-RS244 bytes);
positions = 1-based counting '/', as tx86 and pisa_244/locate.tsv; the script asserts the label at every position before deleting.

## Geometry (decided before any score)
One look by this worker at pisa_merge/overlap_L06_L08.png (the committed images/f244r_L06/L08 s1 and s2 crops, aligned at the strip
offset 1360, ruler in strip px): L06 shows one "q o p(crossed) d" group after the slash, then "h s t o d lambda"; L08 shows one
"a lambda" pair after "y tau varpi v", then "q y". L05 p29-p30: PISA-244's eye record (one sign at strip x 1635). No subagent call.

## Merge groups (each applied ALONE to the base and gated alone)
- G-M5: L05 p30 (T57) deleted; p29 (T35, the cell PISA-244's reader settled) kept. n_del 1. Descriptive alternative, never committed:
  p29 deleted, p30 T57 kept.
- G-OV6: L06 p27-p30 (T14 T30 T45 T18) deleted: a second read of p22-p26 in the s1/s2 overlap. n_del 4; kept partners p23 p24 p26.
- G-OV8: L08 p25-p26 (T26 T37) deleted: a second read of p23-p24. n_del 2; kept partners p23 p24.
- G-X (crossed-p doubles): L02 p11, L04 p44, L06 p25 (?[tcross]) deleted; T19 kept. DECLARED A NON-TEST BY THIS INSTRUMENT (rule 3):
  load_tokens drops every ?[...] token, so the score, both nulls and the alignment are identical before and after by construction.
  Computed only to show the identity; never committed by this job whatever the numbers; logged "untestable by this instrument".

## Scoring (unchanged instruments, imported, as PISA-RS244)
pis1key.run_files (seed 20261004, key-shuffle 1000 + order 1000) and clear_of; key86.tsv; copy kp86/colbert_p49_50.txt, err 0.284;
pis1key.ctrl86 at that err (5 seeds); una2_pisa.per_token (band_dp) for the alignment. Script pisa_merge/merge.py -> pisa_merge/result.json,
per_token.tsv, tx/.

## GATE per group (G-M5, G-OV6, G-OV8)
- G1: merged score > base score AND above both key-shuffle p99 and order p99.
- G2: positive control >= 4/5 (a miss makes the run a non-test for every group).
- G3 (alignment vs the Colbert copy, the RS244 G3 adapted to a deletion): (a) of the deleted tokens, fewer than half (ceil(n_del/2) not
  reached; for n_del 1: none) decode to letters band_dp places on identical copy letters in the base; AND (b) the kept partners' identical
  count after the merge >= their identical count in the base.
- G4 (subset null, gating here): the same-size deletion elsewhere on the page -- for G-M5 one T-token, for G-OV6 / G-OV8 a contiguous run
  of 4 / 2 T-tokens inside one line ('/' skipped, ?[...] never counted) -- every candidate if <= 200, else 200 sampled (seed 20261012),
  the group's own deletion excluded; PASS needs share of draws scoring >= ours <= 0.05.
PASS = G1 and G2 and G3 and G4.

## Descriptive
Per-token copy letters before/after; the G-M5 alternative; the combined score of all PASS groups; judge_plaintext before/after if
anything is committed.

## Commit rule
Only PASS groups are committed. The base bytes are kept byte-identical as tx86/ciphertext_f244r_preMERGE.tsv; pisa_rs244/apply_rs244.py
then derives/checks that file; pisa_merge/apply_merge.py [--check] derives tx86/ciphertext_f244r.tsv from it. Reading regenerated with
tools/decode_key.py (--check exit 0); grades by kp86e/t31_grades.py --page f244r (before/after). FAILs logged as FAIL, candidates kept in
pisa_merge/tx/ only. A changed count goes to a verifier as a one-line next step (no AUDIT.md edit).
