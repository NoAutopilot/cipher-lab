# H63 pre-registration (29 Sept 2026, DEBOSNYS-RUNNER-3b; pushed before any crop is cut or read)

Row: CAMPAIGN.md H63 -- a FRESH known-answer page for the H61 folds.
Page: swarm/R2/R2-2/t_low.py's control() recipe unchanged (12 lines x 8 targets + 2 neighbours each side, boxes that
passes A and B agreed on and that are not reference-sheet exemplars, ids drawn from the disputed boxes' class mix,
rendered from the public PNGs' native pixels, 4x Lanczos crops), with two changes: seed 20260930 (R2-2 used 20260929),
and every source box used on R2-2's page (swarm/R2/R2-2/control/truth.tsv, source_box) excluded from targets and
neighbours. Script: scripts/h63_page.py. Truth stays outside the readers' file list.
Readers: two fresh value-blind readers, R2-2's reader_prompt.txt unchanged except the file paths; both on
claude-opus-5-5 (the brief's model rule: Fable while Fable answers, else Opus 5.5; account 3's Fable limit is rejected
until 3 Oct 08:00 UTC -- substitution recorded; R2-2 used Sonnet + Opus). Each reader = 4 subagent calls of 3 lines,
one line decided before the next (R2-2's split).
Scoring, fixed now: R2-2's folds (PCT-SLASH->PCT, X-DOT->X, X-CURL->X) + RULE.md marks, and on top the six H61 folds
exactly as in h61/PREREG.md (EIGHT+VENUS+THREE, C-BAR-X+ARCH-DASH, CIRC-O+BLOB, O-SLASH+PHI, II-DASH+CC-DASH,
S-CURL+DOUBLE-LOOP; fold before marks). Two-reader error = (unsettled + agreed-but-wrong) / 96; single-reader errors;
reported unfolded, R2-2-folded and coarse-folded.
Kill: coarse-folded two-reader error >= 5 pct -> the six folds do not give a low-noise text on the public pixels.
A pass licenses the coarse-folded c1+c2 text as a lower-noise INPUT (every later use reported folded and unfolded,
polyphony caveat), not a reading.
