# TXE-O: the doubt detector -- which read-free signals find the wrong signs, for the sorter (LANE TX-ENGINEER, ideas M22 + M14 + the sorter feed; account 4, Opus 5.5; cap 5, box 75 min; no vision call)

Read `.claude/briefs/runs/2026-10-09-account4-txe-COMMON.md` first, then `benchmark-tx/PREREG-txeng-2.md` (units, blindness,
Amendment) and research/TX-IDEAS-2026-10-09.md (rows M22, M14 and the Results log). Why this job exists: twelve instruments
have tried to FIX wrong signs and only the crop step moved; but several produced a read-free signal that FINDS them --
TXE-A's show rule (atlas top-1 != line read, or top-1 share < 0.6, or merged confidence M/L) held 11 of L's 14 dev errors;
the band-cut rule held 6 of 14 (TXE-F); the contrast flag 5 of 14 (TXE-I); jitter stability 1 of 14 (TXE-J). Round 3 feeds the
owner's sorter (`tools/sign_sorter.py`, focus.tsv, TRANSCRIPTION.md item 7: ask the person only the tiles whose answer moves the
reading most) with the positions still doubtful, and the owner's time is the scarce resource: a detector that puts the 14-15
wrong signs of a unit inside the smallest flagged set is worth more than any of the failed fixes. This job builds and
measures that detector, read-free, with two new signals (M22, M14) beside the ones on disk.

## Build `tools/tx_doubt.py` (--help; test tools/tests/test_tx_doubt.py; disk only; import the other tools' functions, never copy)
Signals per position of a unit (all truth-blind; the box<->position map label-blind via `tools/tx_compare.py map`):
1. `show` = TXE-A's show rule (atlas held-out top-1 != L sign; top-1 share < 0.6; merged conf M/L) -- reuse tx_compare's
   candidate logic and `benchmark-tx/txeng/compare/topk_no87_allheld.tsv`.
2. `disagree` = passes A and B differ at the position (harvest/f178v/passC_agreement.tsv status != agree).
3. `bandcut` = the box's top or bottom outside its crop band (tx_taxonomy band_edge == cut; tx_tile_gate's rule).
4. `thin` = erosion-share lowest tercile (tx_taxonomy.erosion_share).
5. `contrast` = tx_contrast_sweep's uncertain flag (its committed per-box table).
6. `stab` = glyph_atlas --jitter stability < 0.6 (TXE-J's committed table).
7. `freq` (M22): the sign's count on the page vs the expected count of its key value under the it16dip letter frequencies
   (key_1572_sheet.tsv values; expected = page sign total x P(letter) / homophones of that letter); flag the positions of
   any sign whose count exceeds expectation by > 2 sd (binomial), i.e. an over-read cell such as T76 'n'.
8. `latt` (M14): the lattice at lam 4 (TX-DECODE inputs, TXE-E's run_conf.py harness) chooses a sign other than L's.
9. `pair` = L's sign is in a taxonomy pair (the PREREG C list).
Output `benchmark-tx/txeng/doubt/<unit>_signals.tsv` (line, pos, one 0/1 column per signal, and `n_signals`). Commit it
BEFORE any truth is opened.

## Measure (opens truth through tx_bench.position_errors on labels_<unit>.tsv; after the commit)
On dev_tune: per signal, recall of L's 14 wrong positions and the share of positions flagged; then the best SMALL
combinations: for k = 1..3 signals (OR), the combination with the highest recall at <= 10%, <= 15% and <= 20% flagged, and
the recall of `n_signals >= 2`. Registered gate for the detector to feed the sorter: recall >= 0.7 of L's wrong positions
at <= 15% flagged on dev_tune, AND the same combination (chosen on dev, not re-chosen) reaches recall >= 0.6 on
eval_heldout read-free (no reader involved: not an eval look; say so). Report the full table either way, plus the same
for pass A's 24 errors (a single-pass detector is what a live letter has before reconciliation).
Also, for the owner: on eval_heldout, the list of positions the chosen combination flags, sized against the sorter's
10-20 tiles per session (TRANSCRIPTION.md item 7) -- how many sessions would clear the unit's flags.

## Report
`benchmark-tx/txeng/doubt/RESULTS.md`: the signal table, the combination table, the eval read-free table, the sorter
sizing, 0 vision calls. Shelf and SYSTEM rows (grade: controlled-only if the gate holds on both units, else weak with the
numbers); Results-log rows in research/TX-IDEAS-2026-10-09.md (ids M22, M14, DOUBT; rebase before editing). Offline test:
a synthetic unit of 20 positions with planted signals and planted wrong positions: the recall/flag-share table and the
best-combination search return the planted answer. Cap 5; stop at 80% of cap or box. Report in a short paragraph (first
line: the best combination with its dev recall at its flag share, and the eval read-free recall) and stop.
