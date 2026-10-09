# PREREG-LINCOUNT (LIN-COUNT, 9 Oct 2026, written 11:3x UTC by date -u, pushed before any row label exists)

Question: the two disputed dictionary counts of the Linhares key (Vieyra, New Pocket Dictionary, London 1809, Part I):
283219 "cagar" = p.83 col 2 rank 19 (leaf 95 col 2) and 3241315 "justa" = p.241 col 3 rank 15 (leaf 255 col 3).
Instrument: the A1B-LIN-ROWS instrument (blind per-row labelling of tools/iiif_lines.py row crops by Sonnet subagents),
on NEW material: the IA leaves at their full served size, 1897 x 2152 (`images/book_hires/leafNNNN.jpg`, 2x the 949 px
derivative every earlier count used; LIN-VIEYRA, 9 Oct 2026). Rule 3: three instruments failed on the 949 px scan; this
one runs on the targets only if it passes the calibration below, fresh, at 1897 px.

## Calibration set (fixed now)
The 7 columns of A1B-LIN-ROWS (key ranks from hocr/calibration.tsv, agreed groups), leaves fetched at 1897 px:
236/1 Guerra r2 | 236/3 Habil r1 | 146/1 D r1 | 276/2 Memoria r3 | 261/2 Lhe r6 | 265/2 Lugar r17 | 255/2 Junto r20.

## Crops
Column boxes are set on the full-res image from the vertical ink profile (column rules located by script; box starts
just right of the rule, never inside the text margin; script and boxes committed), checked on the `--debug` overlay before
any label; one crop per text row with `tools/iiif_lines.py --image <leaf> --region <box> --lines-per-crop 1 --debug`
(commands and overlays pasted in NOTES). Row strips are stacked, numbered R01.., into one sheet per column, from the top of
the column down to (key rank + 4) FLUSH-looking rows at most for calibration (about 30 rows for the targets). Crops and
sheets are committed (images/rows_hires/).

## Labels (blind)
Each sheet goes to a Sonnet subagent told nothing about the key, the target words or ranks. One column per call, two
independent blind passes (A, B) per column. Per row one label: FLUSH (starts at the column's left text margin; give the
first word), INDENT (starts at the hanging indent), DROPCAP (a large section initial / letter heading), OTHER (blank,
running head, rule, fragment, two lines merged -- named). Labels are never overridden or settled by the worker.

## Count and match rule (fixed now)
- rank = ordinal of FLUSH rows from the top of the column. DROPCAP rows and running heads are not counted (a section
  initial is not a headword). Each bold FLUSH line counts: a repeated word (e.g. "Guérra" twice) is its own rank.
- A calibration column is scored at the key's rank: **hit** iff the FLUSH row at ordinal = key rank has a first word whose
  normalised form (accents, long s, case, punctuation/apostrophe removed) begins with the expected headword
  (so "D'." matches "D", "Guérra" matches "Guerra"). Otherwise, if the expected headword's matching FLUSH row nearest the
  key rank sits at ordinal k, **MISS (k - rank)**; if no FLUSH row matches, or an OTHER "fragment"/"merged" row lies
  above the key rank, **undecided**.
- Scored per blind pass (V-BRANDT rule), never on a reconciled set.

## Gate (fixed now)
PASS iff, in EACH of passes A and B separately: exact hits >= 6 of 7, AND at most one non-hit column, AND that column (if
any) is a MISS of +-1 or undecided -- not a MISS of 2 or more. Either pass failing = FAIL.
FAIL -> the target sheets are never sent to any model; the per-row labelling instrument is logged [retired] at 1897 px
too (rule 3), next = a person's count (ASKS row draft text in NOTES, not filed).

## What settles each gap (read only if the gate passes)
Targets labelled the same way (two blind passes each). For each, the word at FLUSH rank 19 (95/2) and rank 15 (255/3):
- both passes give the same word at the rank -> that is the count. 95/2: "Cagar..." at rank 19 resolves the
  column-count objection (LX-QAFIX's 18) for 28[3]219; the token stays **M** (grade rests on the caret digit's shape,
  which this does not see). Another word, or fewer than 19 FLUSH rows, in both passes -> 283219 goes to unresolved (U)
  at the column-count level. 255/3: "Justa" or "Jus" at rank 15 is the reading, graded **H** if it agrees with at least
  one earlier independent count (LX-DEC: Justa; LX-DEC's subagent and LX-QAFIX: Jus); also reported: whether
  "Junto, prepos." heads col 3 as its own FLUSH row.
- the passes disagree at the rank, or the rank row is OTHER/unreadable -> that gap stays as it is (M), said so.
Never argue a grade up beyond what the count shows. A moved token is propagated (decode_key.py --check, AUDIT.md,
SECOND-OPINIONS-QUEUE.tsv rows); a rule-7 re-derivation is named as the next step, not run here.

## Units and cost
18 Sonnet subagent calls planned (7 calibration columns x 2 + 2 targets x 2), each one small sheet of row strips;
the orchestrator reads cost by get_session. Stop before starting a unit that crosses 80% of cap 4.5 or box 12:53 UTC
(80% line 12:35 UTC).
