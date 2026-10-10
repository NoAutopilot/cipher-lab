# PREREG-LINCAL (FAM-LINCAL, 10 Oct 2026, written 09:2x UTC by date -u, pushed before any held-out leaf is fetched or labelled)

Question: does the blind per-row labeller (LIN-COUNT's instrument: tools/iiif_lines.py row crops of a 1897 px Vieyra leaf,
stacked into numbered sheets, one column per Sonnet subagent call) give the key's rank on columns it has never seen, under
an "undecided" clause rewritten so that it no longer fires on rows that cannot change a count? Only on PASS are the two
target columns labelled: 83/2 (leaf 95 col 2, 283219 "cagar", rank 19) and 241/3 (leaf 255 col 3, 3241315 "justa", rank 15).
This is the second labeller attempt at 1897 px (LIN-COUNT, 9 Oct 2026, was the first). It is NOT a re-score of LIN-COUNT's
sheets or labels: none of LIN-COUNT's 7 columns is used, and their labels are not re-scored under the new clause here.

## Held-out calibration columns (fixed now; none used by LIN-COUNT)
The key's own worked examples on the period key sheet (m0003-m0004, ANTT PT/TT/CLNH/0086/11), each group's page/column/rank
read off the digits by the key's parse rule and each matched to its word by LX-BOOK on 25 Sept 2026 (BOOK.md, "The twelve
worked-example groups"; hocr/calibration.tsv rows `example`). The known rank comes from the period key sheet, not from any
count of ours:

| group | page | leaf (IA) | col | rank | headword |
|---|---|---|---|---|---|
| 3290219 | 290 | 306 | 2 | 19 | Parecer |
| 3234124 | 234 | 248 | 1 | 24 | Inevitavel |
| 3344325 | 344 | 362 | 3 | 25 | Rustico |
| 321118 | 211 | 225 | 1 | 8 | Franco |

Chosen for deep ranks (19-25, like the targets' 15 and 19) and for all three column positions. Leaves fetched once from
iiif.archive.org at the full served size 1897 px (same route as LIN-VIEYRA/LIN-COUNT, <= 6 requests, >= 3 s apart, IA
take/release), saved to images/book_hires/, logged in images/manifest.json.

## Crops (same instrument as LIN-COUNT, unchanged)
Column images by hocr/hires_columns.py; rows by `tools/iiif_lines.py --image <masked column> --region <box>
--lines-per-crop 1 --ink 110 --centres <grid> --debug`, grid by hocr/rows_grid_hires.py; sheets by hocr/rows_sheets_hires.py
(24 strips per sheet, native scale). Each column's sheet covers from the top of the column down to at least rank + 6 rows;
debug overlays checked by eye before any label is requested (a misplaced grid is fixed and re-cut before labelling, never
after). Commands pasted in NOTES "## LIN-CAL"; crops, overlays and sheets committed.

## Labels (blind, one pass per column)
One Sonnet subagent call per column (all of that column's sheets in the one call), told nothing about the key, the
headwords, the ranks or which columns are calibration and which are targets. Per row one label: FLUSH (line starts at the
column's left text margin; give its first word), INDENT (starts at the hanging indent; give the first word), DROPCAP (a large
section initial or centred letter heading), OTHER (blank, running head, page number, rule, cut fragment, two lines merged --
named in a note). Labels saved verbatim to hocr/lincal_labels/<leaf>_c<col>.tsv and never edited, overridden or settled by
the worker. One pass per column (budget: cap 4.5); the labeller is the same model on each sheet, so it is one instrument,
not independent readers.

## Count and match rule
- rank = ordinal of FLUSH rows from the top of the column. DROPCAP, INDENT and OTHER rows are not counted. Each FLUSH line
  counts, a repeated word included.
- **hit** iff the FLUSH row at ordinal = key rank has a first word whose normalised form (accents, long s, case and
  punctuation removed) begins with the expected headword, AND the column is not undecided (below).
- **MISS (k - rank)** if the expected headword's FLUSH row nearest the rank sits at ordinal k != rank.
- **undecided** if no FLUSH row matches the headword, OR (rewritten clause) any OTHER row lies strictly between the first
  FLUSH row of the column and the FLUSH row at the key rank.

### The rewritten "undecided" clause, and why it is not threshold-shopping
Old (PREREG-LINCOUNT): "undecided if ... an OTHER 'fragment'/'merged' row lies above the key rank", scored as the substring
fragment|merged|two anywhere in an OTHER row's free-text note, anywhere above the rank row. LIN-COUNT's three non-hits all
came from OTHER rows ABOVE THE FIRST FLUSH ROW (a running head cut by the strip edge, a blank band, the top of a drop cap):
rows that precede every headword and so cannot change any ordinal. The clause tested the labeller's choice of words in a
note, not the count.
New: position, not wording. An OTHER row can hide a headword (a merged or cut text line) only if it sits INSIDE the counted
span, i.e. after the first FLUSH row and before the rank row; any OTHER row there -- whatever its note says, blank or not --
makes the column undecided. OTHER rows above the first FLUSH row are ignored. This is at least as strict as the old clause
inside the span (every OTHER row there counts, not only those whose note says "fragment") and drops it only where it could
not bear on a count. It is fixed here before any held-out leaf is fetched, any held-out sheet cut or any held-out label
returned. LIN-COUNT's 14 label files are not re-scored under it (that would be a re-score, which this job is not).

## Gate (fixed now)
PASS iff all 4 held-out columns are exact **hits** (4/4). Any MISS or undecided = FAIL. (One pass per column, so no
non-hit allowance: the gate is stricter than LIN-COUNT's 6/7 per pass.) Scorer: hocr/lincal_score.py, written and committed
with this file before any label exists; `--calibrate` exits 0 PASS / 1 FAIL.

## On PASS (only then): targets
The two target sheets already committed by LIN-COUNT (images/rows_hires/sheets/sheet_0095_c2_*.jpg, sheet_0255_c3_*.jpg,
never sent to any model) are labelled by the same prompt, one call per column, and scored with `lincal_score.py --rank`:
- 95/2: FLUSH rank 19 begins "Cagar" -> the column-count objection (LX-QAFIX's 18) is answered by this instrument for
  28[3]219; the token stays **M** (its grade also rests on the caret digit). Another word at rank 19, or an undecided column
  -> no change, said so.
- 255/3: the FLUSH word at rank 15 ("Justa" or "Jus") and whether "Junto, prepos." heads col 3 as its own FLUSH row are
  reported; the token stays **M** whatever the word (grade M at most).
No token moves above M; the person's count of both columns is still owed (the ASKS draft in NOTES stays). If a target
label changes a token's word, decode_key.py --check, AUDIT.md and SECOND-OPINIONS-QUEUE.tsv are propagated and a rule-7
re-derivation is named as next step, not run here.

## On FAIL or non-test
Targets never sent to any model. Rule 3's third-attempt clause: this is the second labeller attempt at 1897 px; the result
is logged plainly in NOTES "## LIN-CAL" and HYPOTHESES.md is not touched (no hypothesis family); the next step stays a
person's count.

## Units and cost
4 held-out calls + (on PASS) 2 target calls, each one column's sheets, plus session floor. Stop before starting a unit that
crosses 80% of cap 4.5 or of the box (start 09:22 UTC, end 10:42 UTC, 80% line 10:26 UTC).
