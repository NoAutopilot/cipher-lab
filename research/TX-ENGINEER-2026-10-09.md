# TX-ENGINEER: results of the transcription-engineering campaign (LANE TX-ENGINEER, account 4, Fable; 9 Oct 2026)

Final, 9 Oct 2026 08:5x UTC by date -u (incarnation 2, session_01XMybhAz9WRCkE3vzvZdXLt; incarnation 1 session_015pFTECNKte4KHbEeDW5LwU
ran rounds 1-3). Brief
`.claude/briefs/runs/2026-10-09-account4-lane-tx-engineer.md` and its Amendments 1-2; pre-registrations
`benchmark-tx/PREREG-txeng-2.md`, `PREREG-txeng-3.md`; the ideas register `research/TX-IDEAS-2026-10-09.md`; the taxonomy
`research/TX-TAXONOMY-2026-10-09.md`; per-instrument results under `benchmark-tx/txeng/<instrument>/RESULTS.md`.

## For the owner, in plain words

We tried everything on the list, and a few more, against the known answer: 23 instruments in about two hours, each
pre-registered, each scored on the dev lines of Birago no.87 before any held-out look. Nothing beat today's reading at the
bar we set (p < 0.01 on the paired count). The one thing that moved was the crop: a line that slopes out of its band
(f.178r L03) is now read in full, which recovers 7 of the 8 signs the old crop cut off; on lines that do not slope the
new crops change nothing (9 fixed, 8 broken). So the held-out figure stays where it was, and TRANSCRIPTION.md's "Today"
column does not move.

What we learnt about why is the useful part. The errors that remain are not where the two readers disagree (only 1 of
the 14 dev errors sits on a split), not in the order the signs are read (8 of 10 shuffled-order errors are the same wrong
sign), not in the scale, the contrast or the crop (13 of 22 errors are identical across two crop sets; 4x reads, Sauvola,
CLAHE and stroke thickening leave them). They are glyphs that look like another cell to every reader, in every
presentation. Showing the reader exemplars beside the glyph made it worse (it swapped right reads for look-alikes, 4
fixed / 16 broken), and your symbol library did the same (clean printed cells and the hand's own secure tiles beside each
glyph, two readers who had to agree before a change: 0 fixed / 7 broken, the two readers agreeing 97.5% of the time because
the same exemplar pulled them both the same way); hints in the brief did not reach the pairs that matter; and the floor
audit found that of the 20 positions every reader gets wrong, 13 are doubtful on the truth side (alignment slips in the
clerk-sheet matching, a few clerk readings), so part of what we have been counting as reader error is the benchmark's own.
A second audit over all 803 positions found no further doubtful position, so the 13 are the whole of it. With those 13
excluded, today's best read is 0.029, not 0.045 (a verifier has to accept the flags first; they are proposed, not applied).

What you should do at the sorter: the doubt detector flags 6% of the held-out positions and 9 of the 15 wrong signs are in
them (a two-signal rule: the two readers disagreed, or the key-constrained lattice disagrees with the read); a four-signal
rule flags 18% and holds 11 of 15. That is 25 tiles on the held-out lines, about three sessions of ten. Those tiles are
the look-alike pairs (d/s, p/t, n/e, h/l) in this hand's ink; your decision propagates through the atlas clusters to every
letter of the family. Nothing else we tried moves them.

On the live letter f.117r the pipeline's two fresh passes split on 13% of signs (the folder's earlier pair split on 25%) and
the key reads 17 more tokens at S than the committed reading, but the language judge scores the new reading very slightly
worse, so under the folder's own rules no change is licensed and the committed reading stands. The confirm leaf (a
different hand, Spinelli c.1519, never tuned on) reads at 0.088 with the same pipeline; 8 of its 14
errors are two shapes that are not on that folder's sign sheet, which is the same lesson from the other side: the sheet
inventory, not the reader, is where the next gain is.

## Headline numbers

| what | figure | source |
|---|---|---|
| no.87 held-out (eval_heldout, 376 signs), today's best read L | 0.040 (15/376); whole no.87 0.045 (36/803) | TRANSCRIPTION.md; benchmark-tx/txeng/units |
| the same with the 13 truth-doubtful floor positions excluded (proposed, read-free) | 0.029 (23/790, 0.019-0.043) | TXE-T, benchmark-tx/taxonomy/FLOOR-AUDIT.md |
| eval_heldout looks spent on an instrument | 0 | PREREG-txeng-3 Decision |
| confirm item spinelli-c1519-confirm, one look, today's pipeline | 0.088 (17/193, 0.056-0.137); passes 0.104 / 0.083 | TXE-Q |
| live letter fr.3252 f.117r: tokens the key licenses at S | none licensed: S 207 vs committed 190 (+17 net) at err_2reader 0.134 (power ok), but the judge reads -1.234 vs the committed -1.224, so the committed reading stands | TXE-R, ciphers/birago-fr3252-1571-72/harvest/f117/RESULTS-TXE-R.md |

## The instrument table (dev = f178v L01-12, 343 signs; gate paired fixed > broken, p < 0.01)

| id | instrument | class | dev result | eval | verdict | cost |
|---|---|---|---|---|---|---|
| C | thin-stroke pair re-read (tx_pair_reread.py) | C3 x C1 | vs L 1/1 p 1.0, 28 selected | not run | FAIL (selection too small) | 4.36 |
| A | compare, don't recall (tx_compare.py) + 3 read-free variants | C1 | vs L 4/16 p 0.012 wrong way; H-only 2/12, top1 4/14 | not run | FAIL, retired at this show rule | 9.64 |
| E | confusion-matrix lattice (key_decode_lattice --confusion-matrix) | C1 | vs L 3/7; identical to the plain lattice | not run | FAIL read-free | 3.26 |
| G | Sauvola / CLAHE / stroke-width normalisation (tx_recovery.py) | C3 | proxy 7/10, 4/65, 3/3 | not run | FAIL read-free; 19-method literature note | 3.72 |
| B | crop geometry (iiif_lines --band-extent/--check-boxes/--overlap-note, follow-slope) | C2 | geo unit vs A 12/4 p 0.077 | geo only | near-miss | 7.46 |
| D | rendering sweep (tx_prep.py: tight, gamma, stretch, thicken, channels, sr2/sr4) | C3 | proxy sr4 9/1 p 0.02; colour a non-test (greyscale) | not run | FAIL proxy | 3.45 |
| F | per-cut quality gate (tx_tile_gate.py) | C2 | flags hold 6/14 at 19% | n/a | FAIL read-free | 2.99 |
| H | pair hints in the reader brief (tx_pair_hints.py) | C1 | vs A 11/3 p 0.057; vs L 3/4 | not run | FAIL (gain = the omega L has) | 5.77 |
| D2 | one read at 4x | C3 | vs A 9/8 p 1.0 | not run | FAIL | 7.49 |
| I | contrast sweep before cutting (tx_contrast_sweep.py) | C3 | flags hold 5/14 at 21% | n/a | FAIL read-free | 2.97 |
| B2 | geometry replication | C2 | H2 vs A 15/4; pooled 27/8 p 0.0019 (reads 95% identical) | geo only | PASS on the geo unit (the tail) | 3.68 |
| J | jitter-stability prior (glyph_atlas --jitter, lattice --stability) | C1 | vs L 1/4; stab holds 1/14 | n/a | FAIL read-free | 4.09 |
| K | Fable / Opus adjudicator of A/B splits (tx_adjudicate.py) | C1 | 0/1 each; Sonnet 35/36 items; 1 of 14 errors on a split | not run | FAIL + non-test for gain | 10.76 |
| L | shuffled-order tiles vs ordered (tx_compare tiles) | C1 | 5/2 p 0.45; both arms lose to L; 8/10 same wrong sign | not run | non-test; errors in the glyph | 7.36 |
| M | feature-first protocol (tx_features.py) | C1 | vs A 9/6; readers filled features backwards | not run | non-test | 4.70 |
| N | shifted second crop set (iiif_lines --shift-bands/--shift-segments, tx_shift_look.py) | C2 | shift vs A 13/7 p 0.26; S0 alone 9/8 p 1.0 | not run | FAIL; crop step does not clear a 2nd unit | 9.97 |
| O | doubt detector (tx_doubt.py, 9 read-free signals) | sorter | disagree+latt 6/14 at 10.5% | read-free 9/15 at 6.1%; n>=4 11/15 at 18% | gate FAIL; adopted as the sorter feed | 3.45 |
| P | glued digit groups, Dinteville (tx_split_groups.py) | Dint. | 1/11 at 4.2%; the extra signs are dots and marks | n/a | FAIL read-free; class re-labelled | 2.86 |
| M2 | feature-first retest, two calls, compliance gate | C1 | control 19/51 vs 0.70 | not run | non-test; M24 retired | 4.76 |
| T | floor audit, read-free | truth | 13 of 20 truth-doubtful; L 0.045 -> 0.029 | n/a | flags proposed for a verifier | 2.54 |
| Q | confirm item, one look | guard 2 | 0.088 (17/193) | one look | headline | 6.93 |
| R | live letter f.117r (guard 3) | live | err_2reader 0.134 (old 0.25); S 207 vs 190; judge -1.234 vs -1.224 | n/a | no licensed change | 8.35 |
| S | cross-target symbol library (printed 1572 cells + the hand's secure tiles) in the compare layout, two-reader-agree override (tx_compare.py library, resolve --agree; owner 7 + 8) | C1 | vs L 0/7 p 0.016 wrong way (0.041 -> 0.073); R1 1/7, R2 0/8; readers agree 117/120 | not run | FAIL; compare family retired (third run at the show rule) | 8.27 |
| T2 | skipped-letter truth audit over all 803 positions, read-free | truth | 114 sites, 306 positions within 2: 284 clean, 12 conflict-but-clean, 10 TXE-T flags; no new doubtful position | n/a | the 13 flags stand, proposal only (ASKS 157) | 2.44 |

Round 1 (the taxonomy, no reads) is in research/TX-TAXONOMY-2026-10-09.md; the three classes it named carried the mass as
predicted (C1 half of pass A's errors; C2 a third, of which the sloped tail was the fixable part; C3 half of the mapped
errors), and the non-findings held (no fatigue by call position, no overlap-zone excess, glued pairs not a class on this hand).

## What goes into the pipeline, and what does not

Adopted: `iiif_lines.py --follow-slope`/`--deskew` on any line the debug overlay shows sloping (a crop rule); the
manifest-generated overlap sentence (`--overlap-note`) in every pass brief; the doubt detector's two-signal and
four-signal lists as the sorter's focus.tsv for the Birago 1572 family. Not adopted: everything else above, each with its
numbers in the register. Retired for this hand: the compare family (three runs at the show rule), the feature-first
vocabulary, plain re-passes at scale or under rendering, the lattice as a fixer.

## Open, for the owner and the next lane

1. A verifier session on `benchmark-tx/taxonomy/truth_flags_proposed.tsv` (TXE-T; TXE-T2's 803-position sweep,
   `FLOOR-AUDIT-803.md`, added none): accept or reject each flag (ASKS 157, TX-TRUTH-VERIFY on account 1), then a `flag`
   column through `build_birago87.py` and `tx_bench.py --exclude-flagged`. Until then every benchmark figure on no.87
   carries up to 13 truth-side errors.
2. The sheet inventory: the confirm leaf's two off-sheet shapes and no.87's curled Ce / m-with-foot say the next gain on
   a new hand is a sheet that holds the hand's own forms -- the owner's sort, family-wide, before any machine pass
   (TRANSCRIPTION.md rules already say so; this campaign measured why).
3. Colour: O4 and the colour half of O5 are untestable on the greyscale sources on disk; one Gallica colour probe when it
   answers (M25).
4. Dinteville's third class is small marks (dots, primes), not glued groups (M26, low).

## Cost and looks

24 workers, 131.27 of cap 150 (rounds 1-3 under incarnation 1: 22 workers, 120.56; incarnation 2: TXE-S 8.27, TXE-T2 2.44);
lane orchestrator incarnation 1 58.26, incarnation 2 on its archived session. Eval_heldout looks spent: 0. Confirm-item looks: 1
(TXE-Q, 0.088). Tool fixed on the way out: `tools/reconcile_passes.py` now reads the `passage pos sign_id` long header TXE-R's
reader brief used and refuses a long-looking header under any other first column, instead of reading each position cell as the
sign (99.3% for a real 86.6%); test in `tools/tests/test_reconcile_passes.py`.
