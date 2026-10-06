# PREREG R12-OLDCORP (6 Oct 2026, LANE-RUN12-account-2) -- written and pushed before the corpus is built or any score is run

Step (d') of NOTES.md section 12: an era-matched judge corpus `tools/data/es1600` of 1598-1621 Spanish state letters, one
register and one printing kind (the 19th-century CODOIN, *Coleccion de documentos ineditos para la historia de Espana*,
1842-95, archive.org `coleccindedocuNNmadruoft` scans, `_djvu.txt`).

Volume selection (fixed now, applied by script to all 108 madruoft volumes): count four-digit years 1500-1700 in the OCR;
a volume is a candidate when >= 40% of those year mentions fall in 1598-1621. Within a candidate volume, text is kept
from a line naming a year in 1598-1621 up to the next line naming a year in 1500-1700 outside that window (so letters and
documents dated in the window are kept, the rest dropped). Then tools/data/es18/build.py's clean() unchanged (no long-s
repair; reference vocabulary es17c7 + es17a), footnote lines (starting "(1)" etc.), running heads and lines with
>= 2 Latin/Italian/French function words dropped. Each file capped at 650k folded letters; a file with < 100k folded
letters kept is dropped. At least 5 files, else the job reports "too few" and builds nothing. Hold-out: any line naming
Senisteros/Seniste*/Cisneros/"Juan de la Pena" removed (grep logged).

Fold check: tools/data/es18/holdout_check.py --lang es1600 --N 634, 200 windows per fold; blended rate and per-fold
spread reported. Reliability rule (unchanged from PREREG_OLD-ES17A): fewer than ~5 files, or max fold > 2x min fold and
> 20 pct, is "unknown reliability" and its PASS/FAIL is reported as such.

Scoring (only after the fold check, corpus frozen): scripts/es17a_rejudge.py --langs es1600 es17a -- the committed B/C1
reading (N=634), the whole reading.txt (N=1226), and the six shuffled-target decodes of PREREG_OLD-ES17A (seeds 1-3,
committed key and blind solver key). Gate: the judge's own (score > real_p05 and word cover >= 0.5). Voiding rule
(ARM-C1): any shuffled decode PASS voids es1600 as a gate for this family at this N. No reading or key is changed.

## Amendment, 6 Oct 2026 ~11:55 UTC -- after the year-share survey, BEFORE any corpus file was built or any score run

The share rule alone admitted 12 volumes, five of them not 1598-1621 letters (title pages read): 48 (Gonzalez de Najera's
*Desengano y reparo de la guerra de Chile*, a treatise), 60 (a Felipe III-IV chronicle), 81, 100, 106 (15th-century and
medieval chronicles, admitted by a few stray years). Since the brief is "state letters 1598-1621", the selection adds a
second, content criterion: the volume's own title/first heading names letters or state papers of 1598-1621. Kept, 7 files:
42 (letters of the Almirante de Aragon, Flanders 1596-1602), 43 (documents of the Archduke Albert 1598-1621, mostly
letters), 44-47 (Osuna's Naples/Sicily correspondence, 1610s), 96 (letters of Pedro de Toledo, marques de Villafranca,
to Felipe III, 1616-18). Five volumes (36, 61, 68, 82, 91) answered HTTP 500 on their djvu text and are unread
(logged). All other rules unchanged.
