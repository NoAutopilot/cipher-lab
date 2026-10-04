# BIR-KEYFIT pre-registration (4 Oct 2026, written ~07:47 UTC (commit 23dca7e5) before any fit, control or score is run)

Brief `.claude/briefs/runs/2026-10-04-acct3-bir-keyfit.md`. Script `keyfit.py` beside this file (disk only, 0 requests, 0 vision calls).

## Transcription (target)
Base = the committed token files ownersort.py reads (f117 apply, f168 apply, f144r open), with these changes only:
1. the 98 owner-right moves in `../ownersort/adj/owner_right.tsv` (tile -> position by ownersort.py's BIR-OWNER rule, imported, not copied):
   the position's sign becomes the owner pile name (a `-b/-c..` pile is its own sign, not its family);
2. the 4 review answers (`adj/owner_review_2026-10-04.tsv`): q1 T60-c stays its own sign; q2 every X_NEW-l tile becomes T19;
   q3 f168_V02_29 -> T81-d; q4 f144r_L06_01 and f117_L01_20 -> T42-b. No other owner move is applied.

## Fixed and free values
Fixed: every sign whose `keys/key_1572_clerk.tsv` row is grade C with relation `agrees` keeps the sheet value
(`harvest/key_1572_sheet.tsv`; T42 = m is the sheet value and clerk C, fixed). Every position not carrying a free sign keeps its base value.
Free: the signs touched by the corrections (destination pile of each applied move, and its source sign), minus the fixed set, minus the
off-sheet bags (X_NEW, X_EQ, X_S, X_K, X_A, ?) which are shape bags, not signs. A free sign's value is chosen from the sheet's letter
values (single letters only; word codes are never freed). All positions carrying a free sign take its fitted value.

## Fit
Objective = sum over fit leaves of (judge 4-gram mean log10 per letter of the leaf text, leaf's own spec model: f117 fr, f168/f144r it16dip)
x (base text length). Coordinate ascent from the baseline values (family/sheet value; '?' start for off-sheet new piles), signs in sorted
order, up to 6 rounds or no change. Directions: FWD fit f117+f144r, hold out f168; REV fit f168, hold out f117+f144r.
Baseline B1 = the same corrected transcription with the free signs at their baseline values (sheet value of the family; '?' for an
off-sheet family). Held-out gain = objective(held-out leaves, fitted) - objective(held-out leaves, B1). Also reported vs B0 (the committed base).

## Nulls (per direction, 100 draws each, seed 20261004)
- shuffled-label: the free-sign labels permuted at random over all positions carrying a free sign (fit and held-out leaves), refit, held-out gain.
- shuffled-value: the real fit's free-sign values permuted among the free signs (derangement not required), held-out gain, no refit.
PASS for a direction: held-out gain > 0 and > the p95 of both nulls.

## Known-answer control first (gate)
no.87 (ciphertext f178r+f178v+f179r tokens, the committed reading_*_tokens values as base). Blank 10 letter signs drawn (seeded) among
C-agreeing letter signs with >= 3 occurrences in the window; run the identical fit (start '?'/value of nothing: start = most frequent
sheet letter 'e') on a window of no.87 letters matched to the FWD fit size (f117+f144r letter count), it16dip model. Recovery = fitted
value equals the clerk C value. Three draws (seeds 1, 2, 3; window start drawn with the same seed). Also reported at full no.87 length.
Gate: mean recovery at matched length >= 8 of 10. If not met: stop, log "untested-by-this-tool" for the refit; no target fit is run.

## Reporting and application
Per free sign: baseline value, fitted value FWD and REV, fit-side and held-out occurrence counts, held-out gain of that sign alone
(only that sign changed from B1 on the held-out leaves). Grade M for every proposed change unless a second instrument agrees (the clerk
alignment, for signs occurring in no.87); the two directions agreeing is one instrument twice, not two. Nothing enters key.tsv or any
exceptions file in this job unless the direction PASSes AND the sign's own held-out gain is > 0, and then only with a ROOM line;
by default this job writes results only (keyfit/), no key change.
