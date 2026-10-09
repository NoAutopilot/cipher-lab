# PREREG-NEAR-POLL -- neighbour-conditioned phrase-level LM search, catokwacopa unread lines (9 Oct 2026, worker NEAR-POLL)

Committed and pushed before any control, known-answer or target statistic below is computed. Script:
`ciphers/catokwacopa-1875/catokjoint.py` (our own; imports `catoklm.py` and `catok23.py` unmodified). Output `catokjoint.json`.

## Why this and not the brief's literal step
The brief (`.claude/briefs/runs/2026-10-09-account4-orch-jobs.md`, NEAR-POLL) names "the phrase-level LM search on the unread lines
9/12/23/26/29". That search already ran on 6 Oct 2026 (R13-CATOKLM, PREREG-CATOKLM.md 328958aff, catoklm.json): CONTROL BELOW GATE on
lines 9/12/26/29 (R_c 0.00-0.05 vs 0.50), line 23 not completed; the NEAR.md row was last touched before it and did not record it.
Re-running it unchanged is the same instrument (rule 3, third-attempt clause). R13's own named next instrument is run instead:
the same search with each line conditioned on its neighbours' published readings (the ads are one running text).

## Instrument (only change from PREREG-CATOKLM: the two edge bigrams)
Score of a reading w1..wn = catoklm score (word bigram + Bourdeau's positional prior - 2.3 per omitted letter), except that w1 is
scored log P(w1 | left) instead of the unigram, and log P(right | wn) is added, where left/right are the last word of the previous
line's published reading and the first word of the next line's. A context word is used only if it is in the LM vocabulary V; a
published misspelling is normalised to its V word (LECSURES/LECSURS -> lectures). Names not in V (HERTFORD, CONINGTON) and number
lines give no context. Same V (18,943), LM, beam 80, top 20, uniqueness margin 3.0 nats, omission budget.

Lines scored (those with at least one context word in V; 12 has only number neighbours and 23 (48 letters) did not finish its
control in R13's 54 min, so neither is run -- both stay "untestable by this instrument at this N", not attempted):
- 9  (mistrl / otenpu): left `lectures` (line 8 I ATTENDED CONINGTON LECSURES); right none (line 10 HERTFORD not in V)
- 26 (mistrl / oatvpu): left `lectures` (line 25 I ATTENDED JOWETT LECSURS); right `dying` (line 27 DYING)
- 29 (ereflodbr / rileohmae): left `declaration` (line 28 DECLARATION); right none (last cipher line)

## Matched control (run first, per line)
As PREREG-CATOKLM (20 held-out period phrases, seed 1875 + line, |A|, |B|, L matched, prior-shaped split, 3-12 omissions), plus:
the planted window's own held-out neighbours are its context, on the same sides as the target line (left only for 9 and 29; left
and right for 26), and the window is redrawn unless each such neighbour is in V. Statistics as PREREG-CATOKLM.

## Gate (unchanged)
A line's target is scored only if its control has R_c >= 0.50 and W_c <= 0.10. Below gate: "CONTROL BELOW GATE: untestable by
this instrument at this N", target not scored, not a negative. Thresholds not tuned after any result.

## Known-answer control (reported, not a gate)
The brief names CONINGTON/SHIRLEY (PREREG-CATOK23): those names are not in V, so this instrument cannot produce them; their
CATOK23 numbers are carried over as the reference (line 8: power 0.86, null false-unique 0.04; line 24: power 0.84, null 0.02).
Instead the instrument is run on the forced non-name lines with their published neighbours as context: 7 REPEATED (right `i`),
27 DYING (right `declaration`), 28 DECLARATION (left `dying`). Reported: published reading top1 (y/n), unique (y/n), margin.
A known-answer hit says the instrument can recover a forced line; it does not license scoring a line whose control is below gate.

## Caveat registered in advance
One or two edge bigrams add little information to a 12-18-letter line; the expected effect on R_c is small. This test exists to
close R13's named instrument, not because a pass is expected.
