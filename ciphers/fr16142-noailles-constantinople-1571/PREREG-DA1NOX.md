# PREREG-DA1NOX (DA1-NOX, LANE DEFAULT-account-1-20261007-1440, written 7 Oct 2026 14:5x UTC by date -u, before any pass ran)

Part 1 -- c262 margin gloss L01-L13, two blind word-level passes + one blind reconciliation (the instrument D2-NOXB2's Remaining gaps
named after two whole-line blind eyes missed their control; rule 3 repeat clause bars a third whole-line read).

- Crops: images/c262gw/c262gw_Lnn_gkk.jpg, 75 ink pieces (one to about four words each) cut from the native canvas 262 by
  `tools/iiif_lines.py --groups 18` on the same region, centres and slope fit as DEF1-NOXG / R7A-NOX262 (command in
  images/c262gw/manifest.json). Pieces are handed in line and piece order; a piece holding no word is read as "(none)".
- Readers: two independent Opus subagents (pass A, pass B), each given only the crops and the instructions in this file (16th-c.
  French secretary hand, a margin decipherment of a diplomatic letter; transcribe as written, expand no abbreviation except by
  writing the full word in [] after it, mark an unreadable word [?]). Neither sees gloss.tsv, Charriere, NOTES.md, read-*.tsv or each
  other. Reconciliation: a third Opus subagent given both passes' text and the crops of the pieces where they differ, the same
  blindness; it picks or re-reads each disputed word from the crop. This worker has seen gloss.tsv and does not edit any pass.
- Files: witness/da1nox_gloss_passA.tsv, _passB.tsv, _recon.tsv (line<TAB>read), pushed before scoring.
- Score: scripts/da1nox_gloss_score.py = d2noxb2_score.py's PX-BRODEC normalisation and difflib agreement, with one registered change:
  an apostrophe is dropped without splitting the word (j'ay = jay; D2-NOXB2's own sensitivity found its split cost a control word).
- Control lines: L07, L10, L11, L12 -- the lines neither print-aware correction round changed (DEF1-NOXG changed L01-L06, L08;
  R7A-NOX262 changed L09, L13). Known answer = gloss.tsv. Headroom: the two whole-line blind reads scored 0.667 and 0.714, not near
  ceiling.
- Gate (primary): the reconciled read's pooled control agreement >= 0.80. Passes A and B are scored and reported the same way
  (secondary, not the gate). Below the gate the target comparison licenses nothing and is reported as such.
- Targets: L01-L06, L08, L09, L13. If the gate passes: per disputed gloss word (L01 promener, L03 lantienne, L06 farce, L06 jouera,
  L09 treuve, L13 quon, plus any other word the reconciled read gives differently), "supported" when the reconciled read gives the
  gloss.tsv word, "disputed" when it gives another word. No edit to gloss.tsv in this job; disputed words are listed in NOTES.md.

Part 2 -- c510 L05-L14: follow PREREG-D07NOXREAD.md and scripts/noxread510.py unchanged. Order: tools/lookalike_pass.py on the named
split glyphs first; witness/c510_recon.tsv is scored only as that PREREG's own stop rule allows (if its reader-split stop still
applies after the look-alike pass, no decode statistic is computed). Nothing in Part 2 is decided by this file.
