# D2-B117KAPC pre-registration (5 Oct 2026, 18:5x UTC by date -u, account-1 worker for LANE-D2PUSH)

Written and pushed before any score below is computed. Brief `.claude/briefs/runs/2026-10-05-acct1-d2-b117kapc.md`.

## Measured error of the same pipeline (step 1, disk only, no new vision)

Known-answer leaf pair of the same hand and key sheet: nevers-birago-fr3251-1572 no.87 f.178r + f.179r, truth = the clerk's
clear sheet (canvas 182). Pipeline = two value-blind passes + look-alike third reader (`tools/lookalike_pass.py`) + 2-of-3,
i.e. exactly what produced `la/recon_f117_3r.tsv`. Re-scored this session from the files on disk:

    python3 lookalike_known/score_known.py lookalike_known/f178r_passD.tsv --span f178r  -> 97 signs, right 74, wrong 16, empty 7, true_error 0.178
    python3 lookalike_known/score_known.py lookalike_known/f179r_passD.tsv --span f179r  -> 89 signs, right 78, wrong 6, empty 5, true_error 0.071

(run from ciphers/nevers-birago-fr3251-1572/harvest; identical to LOOKALIKE-TOOL, 2 Oct 2026).

- E1 (measured, pooled wrong / scored) = 22/174 = **0.126**
- E2 (bracket, wrong + empty over all signs; also >= the worse leaf's 0.178) = 34/186 = **0.183**
- Reference: two-reader 0.25 (the NEVBIR-117C figure, re-run unchanged).

## Test (fixed before scoring)

`python3 ../../../ceppo-nevers-fr3251-1570s/harvest/decode_control.py la/recon_f117_3r.tsv --map map_printed.json --corpus fr
--err E --seed S` (200 shuffles, 20 windows, defaults), run from harvest/f117. Map: printed (the primary key of NEVBIR-117C).
Seeds 1-5 at E1 (real-key rank of the target and power per seed); seed 1 at E2 and at 0.25. No change to decoder, map, corpus
or sequence; no re-tuning after scores.

Rule-3 can-differ check: the power control's statistic (real-key rank among 200 value-shuffled keys) is computed on synthetic
windows enciphered with the same key and error, and on the target; either can rank 1 or not independently, so the control
can fail differently from the target.

## Gate and verdict

Licensed iff power >= 16/20 at E1 on seed 1 **and** at E2 (bracket, rule 3), **and** the target's real key ranks 1/201 on
>= 3 of seeds 1-5. Then step 3 (M -> S for tokens where two blind instruments agree, regrade, decode --check, depth_check).
If power < 16/20 at E1 or E2: non-test at this length (untested-by-this-tool, rule 3), both numbers logged, no regrade.
If power clears but rank 1 on < 3 seeds: neither licence nor negative; numbers reported.
