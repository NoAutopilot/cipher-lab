# PREREG ELEC-3897 (worker ELEC-3897, LANE DEFAULT-A1-1426-15, account 1, 15 Oct 2026, 15:5x UTC by date -u)

Written and pushed before any fetch. Job: BnF fr.3897 (ark btv1b90096539, openapi.bnf.fr IIIF v3) items 36-38, 62, 64-65, 73 searched
for second witnesses of (A) the nr. 357 name signs (elecpair/name_signs_fr3897.tsv: W, dd, barI, 4, II, Zheavy, flag; hash3 and loop
logged too) and (B) the fr.5761 f.51r lower-block signs (elecrec/PREREG-ELEC-REC.md "The key block": Lfo, Hbar, Phi, Saxe Z-loop,
Colongne 6/G, Magence asterisk, Roy de France S-loop, oXo, legat 8/&, legat dagger). One non-blind reader (this worker, Opus, own eye).
Images in the session scratchpad only, never git.

## Requests (<= 6)
1 manifest (tools/gallica_folio.py; labels are all "NP", so it gives the item list from the Description, not folios). <= 5 canvas views.
Placement from anchors on file: items 36-65 = ff.72-127 (KEYHUNT-2026-10-07.tsv row "Brandenburg election papers"); c128 = f.103r,
c142 = f.116r, c150 = f.123r (ELEC-357; canvas = opening, verso left, recto right, offset 25-27); item 73 = f.146. Planned: two openings
at the start of the run (items 36-38, ~f.72-74), two near its end (items 62, 64-65, ~f.125-127), one at f.146 (item 73); each view is
adjusted from what the previous one shows (folio read on the recto).
Scale: `full/2000,/0/default.jpg` per opening, i.e. ~1000 px per page, the per-page scale the brief's "1000 px" and ELEC-REC used on
fr.5761's single-page canvases (fr.3897 canvases are two-page openings). No native region unless a candidate needs one (counts in the 6).

## What counts as an occurrence (registered; ELEC-REC's rule, extended to set A)
A mark counts only if ALL hold:
(a) it stands in a word slot of the running text (not margin, foliation, heading flourish, paraph, signature flourish, endorsement);
(b) it is not a letter form or a standard scribal abbreviation (p-forms, the 7-like par mark, the light cursive par-Z of f.116v, 9-like
    con/us, tironian et, superscript strokes, "monsr"/"led." contractions, the "que" sign);
(c) it scores 5/5 on ELEC-POOL's five-feature rule (stroke count, closed loops, crossings, orientation, detached marks) against one row of
    set A (by ELEC-PAIR's shape description) or set B (by the on-disk f.51r image, images/canvas105_folio51r.jpg).
Procedure: per canvas, first list every mark meeting (a)+(b) with its features and context words, BEFORE any comparison; then score.

## Decoy rule
(1) Open search, no forced choice. (2) A set-B 5/5 candidate is re-scored against the f.53r rows (images/canvas109_folio53r.jpg); 5/5
there too = "conflict, not counted". A set-A candidate that scores 5/5 on two set-A rows = conflict. (3) Context: the clear words around
the slot must admit the row's name (a king, an elector, a legate); otherwise "context-fail, not counted".
A counted occurrence is M (one non-blind reader); a second witness raises no grade here; no key.tsv or elecpair edit.

## Report
Per item: located (canvas, folio) or not; name signs present or not (names written in letters noted); every candidate with its scores and
verdict. A page with no candidate is a search result at ~1000 px per page, not a native-resolution census.
