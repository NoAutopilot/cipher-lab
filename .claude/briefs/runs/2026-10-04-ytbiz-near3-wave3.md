# LANE-NEAR3 wave 3 (4 Oct 2026, written by LANE-NEAR3, account 2 / ytbiz, session_01Au8dSL1TXFoCk5P5opEMVv)

Common rules: the "Common to every job below" section of `.claude/briefs/runs/2026-10-04-ytbiz-near3-wave1.md`, EXCEPT that NEAR3-C1POOL
is the one clair1161 job that edits NOTES.md, NEAR.md, status.json `near`, ciphertext.tsv, key.tsv and the reading (nobody else is on the
folder while it runs). Intake gate for clair1161 pasted 01:1x UTC in the wave-1 file (partial, exit 0).

## NEAR3-C1POOL -- clair1161-avis-flandre-1688: held-out test on the new leaves, merge, pooled re-anneal (Opus; cap USD 9; box 70 min; disk only)
Why: four more leaves of the same "Avis" are now transcribed (c186L, c187L, c187R, c188L; `tx/<leaf>_rec.tsv`, `reports/NEAR3-C1TX-*.md`)
beside c185R + c186R block (924 signs). The current key.tsv was built WITHOUT them, so they are a held-out test of it before anything is
re-annealed. Read every `reports/NEAR3-*.md` first (C1RD PASS; C1LOOSE FAIL and its three cautions; C1SPLIT's merged/split recommendation;
the four TX reports' new shapes NEW*, `s`, arc-2), then NOTES.md "READ2-C1161", "READ2-C1161B".
Tool shelf: interlinear_align.py already showed no power on this block from a flat start (READ2-C1161, tool_shelf row) -- do not re-run it;
the C1LOOSE report names it as next instrument but the shelf row says its control read at chance here: log that as [retired] for this block
unless more glossed material appears (check the four new leaves' reports for any marginal gloss; if one exists, say so and stop at listing it).
1. **Pre-register** (`tx/PREREG_pool.md`, pushed before any statistic is computed):
   (a) held-out test: decode the ~new leaves' signs (all four pooled, and per leaf) with the CURRENT key.tsv; statistic = fr16 judge score
       (`tools/judge_plaintext.py`, the same spec) AND word cover; controls that can differ: (i) the same key applied to each leaf's
       ORDER-shuffled signs (20 seeds), (ii) the 20 order-shuffled-ciphertext anneal keys already in `glossctl/key_shuf*.tsv` applied to the
       UNshuffled new leaves. PASS when the real decode beats the max of (ii) and the p95 of (i) on the pooled new leaves.
       Report the pooled figure twice: all four leaves, and without c188L (its err_2reader is 0.181, above TRANSCRIPTION.md's 0.10 line,
       framing errors from sloped lines; its focus.tsv waits on a sorter pass). c188L's report also flags c187R for the same slope check:
       note it, do not re-transcribe. The gate uses the all-four figure; the without-c188L figure is reported beside it. New shapes with no
       key value count as unkeyed in all arms equally.
   (b) pooled re-anneal: the same recipe (homophonic_anneal restarts 32, fr16 order 3) on all six leaves -- **seeds 1-5, keep the best
       anneal score** (C1SPLIT found single-seed results sensitive to any stream change; same 5 seeds in every control arm) -- holding only the 6 C signs
       of READ2-C1161B (not the 10 strict-repair moves, per C1LOOSE), with both look-alike pairs MERGED (C1SPLIT: q/ls and S splits both FAIL); gate = block-vs-gloss match
       (the c186R block is inside the stream) beats the same anneal on order-shuffled pooled ciphertext (5 shuffle seeds, each annealed with seeds 1-2, best per shuffle; gate = max over the 5) AND the c185R judge of
       the pooled key is at least the current key's -1.136 (state exactly).
   Time one anneal on the pooled stream first; if it exceeds 2 min, lower restarts for EVERY arm alike and write the number into the
   pre-registration before running any arm (15 anneals in all; stop before one that would cross 80% of the box, reporting what ran).
2. Run (a); paste numbers. Then merge: `ciphertext.tsv` gains the four leaves' reconciled rows (as transcribed, never repaired; NEW* labels
   kept as their own signs; same columns), and `tx/stream_all.txt` regenerated.
3. Run (b) serially. Adopt the pooled key into key.tsv ONLY if (b) PASSes (grades: C for the 6, S for annealed, M where the pass marked M);
   then `python3 tools/decode_key.py ciphers/clair1161-avis-flandre-1688` and `--check` (exit 0) and paste the judge output on the full decode.
   If (b) fails, keep key.tsv, regenerate the reading only for the merged ciphertext under the old key (new leaves' tokens S where keyed,
   U otherwise) so `--check` passes, and say so.
4. Fold the `reports/NEAR3-*.md` sections into NOTES.md (append, one section each, verbatim, then delete `reports/` only after the fold
   is pushed and diffed -- or keep it and link; your choice, say which), then your own section "NEAR3-C1POOL (4 Oct 2026)".
5. Folder size: `du -sh`; if over 29 MB, shrink the AX2-SHRINK way (CLAUDE.md, Access playbook end): `images_manifest_full.tsv` with
   `cited_by`, delete the two committed `images/src_*` native regions after confirming their IIIF URLs are in images/manifest.json.
6. NEAR.md row (Evidence, Last-touched) and status.json `near` entry; refresh "## Remaining gaps"/"## Escalation" (rule 5; the key-rebuild
   step on this block's gloss is [retired] for gloss-alignment instruments per rule 3's third-attempt clause, instruments named: strict
   repair, loose repair, interlinear_align), `python3 tools/gaps_check.py clair1161-avis-flandre-1688` OK line, `python3 tools/near_check.py`.
A rule-7 re-derivation (fresh session) follows if the reading changes -- the lane briefs it; do not do it yourself.
