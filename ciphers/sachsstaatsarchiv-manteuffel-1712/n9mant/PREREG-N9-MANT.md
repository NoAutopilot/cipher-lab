# PREREG-N9-MANT (5 Oct 2026, 05:4x UTC by date -u, N9-MANT for LANE-NEAR9, account 2) -- pushed before any search is run

Question: which transcribed leaves of the Loc. 694/08 pool carry duplicate copies of f.409 / f.410 cipher passages?

Query: the code-group streams of f.409r (ciphertext.tsv 0510a-e excerpts + the f.409r side of f0500_0502/witness_matched_runs_mant3.tsv
and f0501/witness_matched_runs_mant2.tsv), f.409v (ciphertext.tsv 694-08_0511_f409v_*) and f.410 (694-08_0511_f410*), each in reading
order, clear words dropped, '...' and unreadable groups as breaks (no n-gram spans a break). 'bir' is mapped to 612 (RUN4-MANT, I).

Pool (every leaf with code groups on disk): 0500, 0501, 0502 (reconciled glossed runs + witness tables), 0528 (f423_0528/reconciled.tsv),
0579 = f.467 (f467/passA.tsv code_groups), 0580 = f.468 (f468/passes.tsv), and, as an eye-excerpt screen only (grade M, not a transcription),
the codes_seen_eye_M excerpts of frame_rank_gaps189.tsv (0513 0531 0534 0540 0549 0558 0573 0576) and the code_range excerpts of
frame_classify_gaps207.tsv (0151 0241 0291 0391). The query leaves are also searched against each other (f.409v vs f.410) for internal repeats.

Statistic: shared code-group 4-grams and 6-grams (exact, contiguous within a run-segment) between a query leaf and a pool leaf. A
"duplicate" = >= 2 shared 6-grams in the same order on both sides. A run of shared n-grams is merged into a span (start, end, length).
Digit variants are NOT normalised (a 3/8 or 4/9 misread breaks an n-gram; reported as a conservative count).

Control (can differ: shuffling the group order destroys contiguous n-grams but keeps every code and its frequency): the same search with
each query stream's groups permuted (within the whole leaf), 200 draws, seed 9409; report mean and max 6-gram hits and 4-gram hits per
pool leaf. Expected ~0 6-grams. A pool leaf counts as a duplicate only if its real 6-gram count is >= 2, in order, and above the control max.

Known-positive check: 0500/0501/0502 are already known copies of f.409r/v (RUN4-MANT2/3); the search must find them. If it does not,
the instrument fails and no negative on the other leaves is reported.

Output: n9mant/hits.tsv (leaf, query leaf, span, length, glossed?), n9mant/control.tsv. Lift for RUN5-MANT gates: a hit span counts only if the
pool side carries a period gloss over it AND that glossed run is not already in the RUN3/RUN5 gate pairs (0501, 0500, 0502, 0528).
