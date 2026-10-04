# BIR-KEYFIT results (4 Oct 2026, 07:46-07:5x UTC, account-3 worker)

Prereg `PREREG.md` (commit 23dca7e5, before any run). Script `keyfit.py` (deterministic; ~10 s on 1 CPU). Disk only: 0 requests,
0 vision calls, 0 subagents. One post-prereg edit, no effect on numbers: the coordinate-ascent convergence test was rewritten for
clarity (the re-run printed identical numbers); the prereg's clock time was corrected from 07:55 to 07:47 (rule 6).

## Known-answer control (gate) -- FAIL, so no target fit was run
no.87 (f.178r+f.178v+f.179r committed tokens), 10 C-agreeing letter signs blanked per draw, identical 4-gram coordinate-ascent fit
(it16dip), recovery = fitted value equals the clerk C value (`control_no87.tsv`, `control_no87.json`):

| length | seed 1 | seed 2 | seed 3 | mean | gate (>= 8) |
|---|---|---|---|---|---|
| matched to the FWD fit side (357 letters, f117 + f144r) | 6 | 8 | 6 | 6.67 | **FAIL** |
| full no.87 (920 letters) | 8 | 10 | 7 | 8.33 | (reported only) |

By occurrence count in the window: n >= 10 recovered 14/15 (matched), 19/20 (full); n < 10 recovered 6/15 (matched), 6/10 (full).
Misses are the rare signs (T57 s->r, T92 s->r/t, T63 d->t, T54 m->t, T58 l->r, T13 l->d/n, T65 t->p, T76 n at 6-12 occurrences, T81 b->t).

## Verdict
Per prereg: CONTROL BELOW GATE -> the constrained LM refit is **untested-by-this-tool** at this length. Not refuted, not run.
Why it cannot be rescued by the full-length number: the target's free signs are the owner's new piles (1-11 tiles each across all
three leaves, fewer on any fit side) and a handful of M-grade sheet signs; at n < 10 the instrument recovers 40% of known values even
on no.87, whose base text reads, while every target base text already FAILs the judge (about -1.2 vs real_p05 -0.9). A value it
proposed for a target sign would be below the control's own reliability.
Nothing entered key.tsv or any exceptions file; no value change is proposed.
Next (a different instrument or new material, rule 3 third-attempt clause not yet reached): the clerk-sheet alignment itself on
owner-labelled no.87 -- re-label the no.87 tiles with the owner's sort (if the owner sorts no.87 too) and re-run
`tools/interlinear_align.py`; a C value per owner pile from period plain text needs no LM, and is the second instrument this
question lacks. Cost ~$2 after an owner pass on no.87 (waiting-on the owner's sorter, never blocking).
