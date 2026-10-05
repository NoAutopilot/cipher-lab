# PREREG-DEF1NOXB (DEF1-NOXB, written 5 Oct 2026 21:07 UTC by date -u, before any crop was viewed)

Job: blind second read of the interlinear French gloss on images/c262gx_L01.jpg ... c262gx_L08.jpg (canvas 262).
Reader: this session (Opus), which has not opened Charrière, gloss.tsv, any reading file, NOTES.md after line 1000,
AUDIT.md or DEF1-NOXG's commit before finishing the read.

- Unit: one word of the interlinear gloss, read left to right, unclear words marked [?].
- Control lines: L02, L03, L05, L07 (unchanged by DEF1-NOXG); known answer = their gloss.tsv text, opened only after
  the read is written to disk (read-DEF1NOXB.tsv, committed in the same push).
- Normalisation (rule 3, PX-BRODEC): lower case, punctuation dropped, u/v and i/j merged, y->i, abbreviations expanded
  where the expansion is unambiguous (e.g. "q" -> "que", "nre" -> "nostre"), accents dropped.
- Agreement = word-level alignment (difflib SequenceMatcher on normalised token lists): matched tokens / tokens in the
  known answer, pooled over the four control lines. [?] counts as a miss.
- Gate: pooled control agreement >= 0.80. If below, the L01/L04/L06/L08 comparison licenses nothing and is reported as such.
- Test lines L01, L04, L06, L08 are then compared word by word with DEF1-NOXG's leaf readings (its NOTES.md table): agree / differ.
