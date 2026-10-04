# LANE-NEAR4 wave 2 (4 Oct 2026, written 04:3x UTC by LANE-NEAR4, account 2 / ytbiz, session_01LRQBWNfFKjoMQfG9LHoUuz)

Common rules: the "Common to every job below" section of `.claude/briefs/runs/2026-10-04-ytbiz-near4-wave1.md` (claim, cap/box, rule 10,
TRANSCRIPTION.md crops, PREREG before statistic, gaps refresh, end-of-job push and done line for LANE-NEAR4). Intake gates pasted there
04:13 UTC for paget, es132, hellen; fr16104-vivonne-spain-1572 pasted 04:3x UTC: "partial (line 1) -- edition/page or full-text-search citation found within 6 lines", exit 0.

## N4-PAG213 -- clairambault1225-paget-1714: code 213 "ma" vs "Mariage" (Opus; cap USD 2; box 30 min)
N4-PAG65 (ROOM 04:20, commit e74d7ba7) left one seen-not-settled conflict: 213 ma (C) reads against "Mariage" (Gibbs ri). Same method as
N4-PAG65 (align/settle7.py, extended by option, same S/M rule), per-token ruling, key.tsv/exceptions.tsv, `decode_key.py --check` exit 0.
Also the NOTES Remaining gaps' code-level M rows: if any other code shows the same C-vs-gloss conflict in settle7's report, list it (do not
settle more than 213 plus at most two such codes). Say in the done line whether tokens changed (the lane then briefs one rule-7 re-derivation).

## N4-HEL6 -- hellen-frederick-1752: pre-registered diagnosis of R4372's bigram-only signal on R1953 (Opus; cap USD 6; box 60 min)
NOTES.md "Remaining gaps" (N4-HEL5) cheapest next. Read NEAR3-HEL4 (R4372 LR100 test: uni FAIL, bigram signal) and READ2-HEL/HEL2.
Pre-register (`key_r4372/PREREG_diag.md`, pushed before computing): which bigram pairs carry the signal (per-pair contribution vs the shuffle
distribution), and a per-code check: for each R1953 token in codes 1-800 adjacent to an R4369-decoded (H/S) neighbour, does the R4372 value
form a plausible French bigram/trigram with the neighbour, scored against (i) R4372 values shuffled among codes 1-800 (200 draws) and
(ii) a size-matched French table from another key on disk. Gate stated before running. Outcome: either R4372 carries partial real values
(name which codes, grade at most M) or the bigram signal is an artefact of a named mechanism. No key adoption; NOTES section "N4-HEL6", gaps.

## N4-ES132B -- es132-vargas-mexia-1578: f.90r + f.91r under test 2 (Opus; cap USD 6; box 60 min)
Same as N4-ES132 (wave 1; its NOTES section and PREREG_test2 amendment 1): the f.89 letter's f.90r then f.91r, crop commands pasted, two
blind passes + reconciliation per page, gate (a) where a printed overlap exists (pre-registered overlap clause) else (b), err_2reader,
grades, a few phrases by eye, `test2.py --check`. Check cabinet_noir_map.tsv first. Stop before a page that would cross 80% of cap.

## N4-VIV -- fr16104-vivonne-spain-1572: date of the f.157-159 letter, then the fr.16105 bisection (Opus; cap USD 3; box 45 min)
NOTES.md Remaining gaps (3 Oct): the two "sans le dechiffrement" letters (fr.16104 8 Sept 1572, fr.16105 4 June 1573); candidate f.157-159
found, date unconfirmed. (1) Read the date of the f.157-159 letter at a native crop (`tools/gallica_folio.py` for the canvas, `tools/iiif_lines.py
--region` one crop, one vision call). (2) If it is not 8 Sept 1572, or for fr.16105 4 June 1573: bisect the volume by canvas (gallica_folio.py
labels, a few 1200 px thumbnails per step, <= 30 Gallica requests, >= 2 s apart) to the leaf with that date; record canvas, folio, whether cipher
without interlinear gloss. No transcription this job. NOTES section "N4-VIV", gaps refresh.
