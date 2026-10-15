# PREREG ELEC-REC (worker ELEC-REC, LANE DEFAULT-A1-1426-15, account 1, 15 Oct 2026, 15:2x UTC by date -u)

Written and pushed before any fetch of the rectos. Job: search BnF fr.5761 rectos ff.161r-164r (openapi.bnf.fr IIIF v3, ark
btv1b52510561g, canvases c325, c327, c329, c331, `full/1000,/0/default.jpg`, 4 requests; <= 1 further native region for one candidate) for
further occurrences of the f.51r lower-block ("A monsr de la Vernade devers monsr de Treves") signs. One look per canvas by this worker
(Opus, own eye; NOT blind: it has seen the key and ELEC-VERSO/R2/R3). Images and crops in the session scratchpad only, never git.

## The key block (images/canvas105_folio51r.jpg, 1500-px frame x 0-1500 y 1250-2050, read by this worker before any recto)
Palatin (Lfo: L/f stroke, cross-bar, small detached circle above right); Treves (Hbar: R/f-like sign, bar, descending hook, superscript mark);
Brandebourg (Phi: closed loop crossed by a stroke, vertical descender); Saxe (Z-like stroke joined to a loop/h, small circle above);
Colongne (6/G-like bowl with a small o inside or beside); Magence (asterisk/X with a small circle above); Le Roy de France (S-loop crossed
by a long vertical); Le Roy catholicque (oXo: horizontal stroke, circle at each end, diagonal X); Le legat Sainte-Marie in Portico (looped
8/&-like sign); Le legat qui est en Allemaigne (vertical stroke with two cross-bars, dagger-like). Nulles: Pi, L-bracket, small p-loop, Q,
R with tailed circle.

## What counts as an occurrence (registered)
A mark counts only if ALL hold:
(a) it stands in a word slot of the running text of a letter (not margin, foliation, heading flourish, paraph or signature flourish);
(b) it is not a letter form or a standard scribal abbreviation: par/per/pro p-forms, the 7-like par mark (ELEC-KLU), 9-like con/us,
    tironian et, superscript abbreviation strokes, the "monsr"/"led." contractions;
(c) it scores 5/5 on ELEC-POOL's five-feature rule (stroke count, closed loops, crossings, orientation, detached marks) against one
    f.51r lower-block name row.
Nulles are NOT searched: Pi, L, Q, R are letter-like and cannot be told from letters at 1000 px.
Procedure order: on each canvas, first list every mark that meets (a) and (b) with its five features and its context words, BEFORE
comparing to any key row; then score the list against the block.

## Decoy rule (how this pass avoids ELEC-R3's failure)
ELEC-R3's decoy fired because a reader shown a key panel and asked to assign each target sign assigned a decoy to the nearest panel row
(forced choice). Here (1) the search is open: candidates are listed before any key comparison (no target set to force); (2) every
candidate that scores 5/5 on an f.51r row is also scored against the f.53r key rows (images/canvas109_folio53r.jpg, a different block,
the decoy panel); a candidate that also scores 5/5 on any f.53r row is logged "conflict, not counted"; (3) context: the clear words around
the slot must admit the row's name (a prince-elector, the king, a legate); a slot whose context contradicts the row is logged, not counted.
A counted occurrence is graded M (one non-blind reader); a third independent oXo is reported, not keyed. No key.tsv edit; no fourth reader
on the f.51r images.

## Report
Per canvas: candidates listed (count, features, context), each with its f.51r and f.53r scores and counted / conflict / context-fail.
A canvas with zero candidates under (a)+(b) is a search result at 1000 px ("no name sign seen"), not a census at native resolution.
