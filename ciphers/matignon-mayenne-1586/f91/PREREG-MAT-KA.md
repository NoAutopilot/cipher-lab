# PREREG MAT-KA (15 Oct 2026, account-2 worker, LANE DEFAULT-A2-0810-15)

Written 09:2x UTC 15 Oct 2026 by `date -u`, before any score is computed. Disk only, no network, no vision call.
Prior work: `tools/prior_work.py matignon-mayenne-1586 --item-spec 'shelfmark=BnF fr.15572;folio=91-92;sender=Mayenne' --step-type key --offline`
exit 4: plaintext KNOWN (Tomokiyo l.640 = the period margin decipherment, used here as the known answer); the two LEAD rows are this lane's own
claims (the 05:16 lane orchestrator line and this job's 09:15 claim), not prior work on this step.

## Question
Do the unkeyed reader labels U, T, D2, BOX2 and + carry the values the MAT-F91/F91C/F91E alignments suggested (U=e, T=r, D2=a, BOX2=u, +=m),
judged by a held-out block of the f.91r-92r period gloss rather than by the retired `--try` window score (its power control failed, MAT-F91B)?

## Data (fixed, on disk)
Blocks A, B, D (`ciphertext_draft_f91.tsv`, `gloss_f91.tsv`), C, F (`..._f91c.tsv`), E (`..._f91e.tsv`). Cipher token = the reconciled sign
where confidence H, else `?` (unsettled). Signs that are integers >= 10 enter as word codes (`%`) as in `align_f91*.py`. Gloss = the
`normalised` column. Occurrence counts (H-confidence, pooled): U 111, T 29, D2 15, BOX2 11, + 4.

## Instrument (block-held-out gloss agreement)
1. **Per-block masked alignment.** Each block is aligned ON ITS OWN (one pair per run, so nothing is learned across blocks) with
   `tools/interlinear_align.py`'s `run_align` (imported, same settings as `align_f91e.py`: `--code-prefix @`, `--word-code-prefix %`,
   `--keep-fs`, `--max-chunk 12`, prior = key.tsv H single-letter rows). Every code token that is NOT an H single-letter key code (all
   unkeyed labels, `?`, keyed non-H codes) is renamed to a unique singleton (`@<label>#<block><pos>`), so its chunk comes only from the
   H-code anchoring around it, never from EM consistency with its own other occurrences. The aligned chunk (0 or 1 letter, folded v->u,
   j->i) at each position is that position's "gloss letter"; positions with an empty chunk are excluded (as in `score()` of align_f91e.py).
2. **Leave-one-block-out (LOBO).** For label L and held-out block b: fit = majority gloss letter of L's positions in the other five blocks
   (ties: alphabetically first letter); prediction for every L position in b = fit. Pooled LOBO accuracy = hits / scored positions over all
   blocks where L occurs and the fit blocks give a prediction.
3. **Null (label shuffle).** Pool = every position in the masked alignments with a non-`?`, non-word-code token and a non-empty chunk.
   Draw (seeds 1-200) the same number of positions per block as L has scored positions, from that block's pool, and compute the same LOBO
   accuracy. Report mean, p95 (the 190th of 200 sorted) and max. The statistic depends on which positions are chosen, so the control can
   differ from the target (rule 3, non-test clause checked).
4. **Power check (per label, known H code at the same occurrence count).** The power code is re-run with that code ALSO masked (removed
   from the prior and uniquified, i.e. treated exactly like an unkeyed label), then subsampled to the label's scored count n (seeds 1-20,
   uniform over its scored positions; if it has fewer than n, all of them, which is conservative), with its own 200-draw null at the
   same per-block counts. Power passes if the median over the 20 subsamples of (LOBO accuracy > null p95) is true, i.e. >= 11 of 20
   subsamples beat their p95, AND the LOBO fit equals the code's key value in >= 11 of 20. Power codes (same letter where one has >= n
   occurrences, else frequency-matched):
   - U (111) -> h = e (84, all; below n, conservative)
   - T (29) -> L = r (36, subsampled to 29)
   - D2 (15) -> e = r (18, subsampled to 15; X = a has only 8, reported as secondary, not gating)
   - BOX2 (11) -> s = u (30, subsampled to 11)
   - + (4) -> 4+ = m (15, subsampled to 4)
5. **Verdict per label.**
   - power FAILS -> `too-short` (not rejected), whatever its own accuracy;
   - power PASSES and L's LOBO accuracy > null p95 and the all-block majority letter equals the candidate value -> `candidate for key.tsv at
     grade S` with its numbers (no key.tsv edit in this job);
   - power PASSES and accuracy > p95 but the majority letter differs from the candidate -> reported as that other letter, `candidate S`
     at that value, flagged;
   - power PASSES and accuracy <= p95 -> `fails held-out gloss test` (control-backed negative for that value under this instrument).
6. Secondary, not gating: per-fold breakdown (each held-out block's hits/n and fit letter) for every label and power code; the
   unmasked-H sanity number (the masked alignment's R on H codes, which should stay near the MAT-F91* R).

## Outputs
`f91/mat_ka.py` (regenerates every number; `--check` exits non-zero if `f91/mat_ka_result.tsv` is stale), `f91/mat_ka_result.tsv`,
`f91/mat_ka_folds.tsv`, HYPOTHESES.md rows, NOTES.md section "MAT-KA", Verdict update, gaps_check.
