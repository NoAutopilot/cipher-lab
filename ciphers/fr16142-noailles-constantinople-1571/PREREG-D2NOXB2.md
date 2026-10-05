# PREREG-D2NOXB2 (D2-NOXB2, LANE DEFAULT-account-1-20261005-2217, written 5 Oct 2026 23:2x UTC by date -u, before any crop was viewed)

Job: blind read of the c262 margin/interlinear French gloss, with a control made only of lines that commit 4ef591e8c (DEF1-NOXG)
did not change. Replaces DEF1-NOXB's control (L02/L03/L05/L07), three of whose four lines 4ef591e8c had rewritten, so that
control compared the read against DEF1-NOXG's own new text, not an independent answer.

Reader: this session (Opus). Before finishing the read it has not opened Charriere, gloss.tsv (beyond its header line and a
script printing only the line-id column of 4ef591e8c's changed rows), read-DEF1NOXB.tsv or any reading file, NOTES.md after
line 15, AUDIT.md, or the text of 4ef591e8c's diff.

- Which lines changed (from `git show 4ef591e8c -- gloss.tsv`, line-id column only): L01-L06 and L08. Unchanged: L07, L09-L13.
- Crops: images/c262gl_L01.jpg ... c262gl_L10.jpg (the FT-D crops whose ids gloss.tsv uses), read in one pass, left to right.
- Control lines: L07, L09, L10 (unchanged by 4ef591e8c, same margin hand). Known answer = their gloss.tsv text, opened only
  after the read is written to read-D2NOXB2.tsv.
- Target lines: L01-L06, L08.
- Normalisation (rule 3, PX-BRODEC), applied to both sides by scripts/d2noxb2_score.py: lower case, accents dropped, punctuation
  dropped, u/v and i/j merged, y->i, a closed list of abbreviations expanded (q->que, nre->nostre, vre->vostre, sr->seigneur,
  mt->mont, md->monseigneur, ms->messieurs, sa->sa, sm->sa majeste, m.te/mte->majeste, &/et->et).
- Agreement = difflib SequenceMatcher matched tokens / known-answer tokens, pooled over the three control lines; "[?]" is a miss.
- Gate: pooled control agreement >= 0.80. Below it, the target-line comparison licenses nothing and is reported as such.
- Then, for L01-L06 and L08: the same agreement figure against the current gloss.tsv (DEF1-NOXG's text) and, where present,
  word-by-word agree/differ against DEF1-NOXG's leaf readings in NOTES.md. No edit to gloss.tsv.
