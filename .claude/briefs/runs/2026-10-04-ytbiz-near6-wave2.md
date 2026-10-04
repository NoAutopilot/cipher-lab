# LANE-NEAR6 wave 2 (4 Oct 2026, written 10:5x UTC by LANE-NEAR6, account 2 / ytbiz, session_019jKS1wURJVECZN9M5sEAPj)

Common rules: as wave 1 (`.claude/briefs/runs/2026-10-04-ytbiz-near6-wave1.md` first line, which points at the near4 wave-1 common
section); Vivonne jobs also follow wave 1's "Shared by both piece jobs" section (isolation, folder size < 30 MB, units, grading, done line).
Intake gate for fr16104-vivonne-spain-1572 rc=0 (pasted in wave 1). Two Vivonne jobs run at once in the same folder: pull --rebase before
every shared-file edit and keep both sides.

## N6-VIV63B -- fr.16105 ink 63: the remaining cipher pages ff.192r-194r (Opus; cap USD 12; box 120 min)
Continue N6-VIV63 exactly (NOTES "N6-VIV63", PREREG-N6VIV63.md, its tx/viv63_* scripts and crop settings): crops, 2 blind Sonnet passes +
1 reconciliation per page, decode with key.tsv. Before decoding the new pages push an addendum `PREREG-N6VIV63B.md`: the same b2 gate (4-gram
vs letter-order-shuffle p99) on (i) the new pages alone and (ii) the whole piece, with the same two positive controls; AND, as a registered
specificity check this time (N6-VIV63 ran it only post hoc: 5/50 wrong keys passed b2), 200 wrong keys (key.tsv values permuted across codes)
scored through b2 on the whole piece -- report the share that pass and the real key's margin against that distribution's p95/p99. State
the pass rule for the specificity check before running it (e.g. real margin > wrong-key margin p99). Regenerate reading_piece63 with --check.
NOTES "N6-VIV63B", gaps refresh, ROOM done line; if gates pass, "piece 63 ready for audit 1 (all pages)".

## N6-VIV53B -- ink 53: f.171v, the last cipher page (Opus; cap USD 6; box 75 min)
Continue N6-VIV53 (NOTES "N6-VIV53", its scripts/crops): f.171v (~18 cipher lines) crops, 2 blind passes + 1 reconciliation, interlinear
words read at native resolution BEFORE decoding and frozen. The registered gloss gate on ff.170r-171r FAILED (0.577 < 0.60): that result
stands and is not re-run or re-thresholded. Push `PREREG-N6VIV53B.md` before decoding f.171v: (a) the N5-VIV54 gloss check on f.171v's own
new glosses only (if >= 3), same floor; (b) N6-VIV63's b2 statistic (PREREG-N6VIV63.md) with its two positive controls, on f.171v alone and on
the whole piece 53, disclosing that ff.170r-171r's decode was already seen when b2 was chosen; (c) the same 200-wrong-key specificity check as
N6-VIV63B, rule stated in advance. Regenerate reading_piece53 with --check. NOTES "N6-VIV53B", gaps refresh, ROOM done line (audit-ready
only if a gate passes, naming which).

## N6-HEL81 -- hellen-frederick-1752: contact sheet of Add MS 32276 key records R4381-R4408 for R1049 (1756) and the 1763 letters (Opus; cap USD 5; box 60 min)
NOTES N6-HEL76 Verdict: "cheapest next: open the post-1756 Add MS 32276 key records R4381-R4408 (contact sheet first)". Run
`python3 tools/intake_gate_check.py hellen-frederick-1752` and paste it. DECODE listing is login-free (tools/decode_list.py): record each
record's title, date, folio, page count and thumbnail; view thumbnails only (no full-size fetch unless one record is a filled numeric table
whose header, date or range fits R1049 (7 Sept 1756, codes up to ~2626) or the 1763 letters -- then at most one DECODE login and that
record's pages to scratch, never committed). Output: `key_search/R4381-R4408.tsv` (record, folio, date, holder/header, code range, filled
y/n, fits R1049/1763/none, why). No transcription in this job: name the best candidate and its cost as the next step. NOTES "N6-HEL81",
gaps refresh + gaps_check OK line. Report what was found and where it was not found.

## N6-VIV63C -- fr.16105 ink 63: the last cipher pages ff.193v-194r (Opus; cap USD 5; box 60 min) -- added 11:2x UTC
Continue N6-VIV63B exactly (its NOTES section, PREREG-N6VIV63B.md and scripts). Push `PREREG-N6VIV63C.md` before decoding: the same b2 gate on
the new pages alone and the whole piece, the same two controls (subsampled to the new pages' letter count for the alone test, as N6-VIV53B
did), the same 200-wrong-key specificity rule. Regenerate reading_piece63 with --check. NOTES "N6-VIV63C", gaps refresh, ROOM done line
("piece 63 ready for audit 1 (all pages)" if gates pass) -- the account-3 audit of piece 63 is waiting on this, so keep to the box.
