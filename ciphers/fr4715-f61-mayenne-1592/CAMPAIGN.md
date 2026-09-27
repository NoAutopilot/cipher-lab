target: fr4715-f61-mayenne-1592
goal: a verified reading of BnF fr.4715 f.61 (Duke of Mayenne's polyphonic cipher, 1592-93) at N3 or better after two audits
started: 2026-09-27 20:33 UTC
daily_budget_usd: 40
spent_today_usd: 0
spent_day: 2026-09-27
closed:

## Attempts already made

- INTAKE-4715-F61 (27 Sept 2026, parent worker, Sonnet): Job 0 gate -- NOT found-solved (Tomokiyo's own `bnf4715.htm#no38`
  prints only a partial decode, self-labelled "Solution Incomplete": one phrase, "jalousie au beau-pere", plus a handful
  of isolated words over his own published image of the leaf; `mayenne.htm` prints no reading at all, only the
  reconstructed cipher table). Built this folder. Transcribed `keys/key_mayenne_1592.tsv` (25 rows, 21 AB / 2 M / 2 ?)
  from `mayenne.png` via two independent blind Sonnet subagent reads, disagreements settled from crops. Stopped: job
  finished on its own brief (a Layout intake, no cryptanalysis); named "calibrate the key against Tomokiyo's five
  known spans" as the next step, which F61-CAL then ran.
- F61-CAL (27 Sept 2026, parent worker, Opus): pre-registered gate -- token-level match between our decode of
  Tomokiyo's five marked spans (55 letters, `scripts/tomokiyo_spans.tsv`, grade H for this test) and 20 shuffled-key
  controls (seed 1), gate pooled match >= 0.85 and above the control max. One Opus vision call
  (`scripts/read_call_A.tsv`, 82 signs) matched f.61's own hand to `mayenne.png`'s 16 table drawings via
  `scripts/f61cal.py`. Result: 8/55 = 0.145 vs control mean 0.114, max 0.309 -- gate MISSED. Outcome (c): the
  drawing-to-hand matching is what fails (8 of 10 f.61 shape classes mislabelled against the 25-px table drawings,
  each consistently), while Tomokiyo's own letters sit in one table cell per f.61 shape class for 48/55 of the 55
  letters (`scripts/class_diag.tsv`) -- the key's value-pairing structure holds, its drawings don't transfer to this
  hand. One data conflict left open: the "V with bar" shape class takes both s and t, which the table splits across
  two columns (f/s and g/t). Logged untested-by-this-tool (image-to-drawing matching), not a key negative. Stopped:
  brief's box/cap met its own stopping point once the gate outcome was diagnosed; no second vision call made (see H2
  below for why that call was withheld and what would test it properly).

## Hypotheses

| id | rank | hypothesis | needs | est_usd | status | result |
|---|---|---|---|---|---|---|
| H1 | 1 | F61-CRIB: build a class-to-letter map straight from read_call_A.tsv's own shape-class notes (the 'marks' column, ignoring its S0x/table-drawing labels), fit on 4 of Tomokiyo's 5 known spans and scored on the withheld 5th by a script in the shape of scripts/f61cal.py (same DP, 20 shuffled class-maps, seed 1), repeated leave-one-span-out for all 5; passes if the pooled held-out match beats every shuffled-map max, the same gate shape F61-CAL used | nobody | 1 | open |  |
| H2 | 2 | Second independent blind Opus read of the same images/f61sheet_L0*.jpg sheets, describing raw sign shapes only (no key_inventory_sheet.png shown, no S0x label asked for), reconciled against read_call_A.tsv's marks column with tools/reconcile_passes.py; passes if the shape-class assignment agrees for at least 9 of the 10 non-null classes named in scripts/class_diag.tsv, which would show F61-CAL's single call was not reader noise before H1's map is trusted further | nobody | 2 | open |  |
| H3 | 3 | Search sources/cryptiana/web/ (already fetched) and cryptiana.web.fc2.com's own site index for a separate page on any of the fr.3982/3983 sibling letters mayenne.htm names (ff.97, 101, 106, 108v, 124, 211); a page carrying its own interlinear markup like BnFfr4715f61.png would more than double the 55-letter known-answer set H1 trains on | nobody | 1 | open |  |
| H4 | 4 | Once H1 passes: apply its class map to the leaf's unmarked runs (L02, L04, L08's tail, L10 -- about 20-25 signs, new crops cut by images/regen_f61r_sheets.sh) with one Opus read, scored against the same 20-shuffled-map control as H1; a pass yields a cryptanalytic fragment reading, graded S/M per rule 4, not yet a reading of the letter | nobody | 2 | open |  |
| H5 | 5 | Once H1 passes: two independent blind Opus passes on the full leaf (all 11 lines, images/regen_f61r_sheets.sh re-run over the whole 500,1880,3320,1420 region), reconciled with tools/reconcile_passes.py (a third priced pass per CLAUDE.md Usage item 6's own reconciliation-costing lesson), scored by an f61cal.py-style script against 20 shuffled-map controls, with the five known spans held out as an internal check; passes at the same >=0.85-and-above-control-max gate | nobody | 6 | open |  |
| H6 | 6 | Once H4 or H5 produces any transcription beyond the five known spans: run the 20-shuffled-map control from scripts/f61cal.py against the full decode, not only the five spans, before any word in the unmarked lines is reported as a reading, per rule 3's control-before-target order | nobody | 1 | open |  |
| H7 | 7 | Fetch archivesetmanuscrits.bnf.fr's own finding-aid/depouillement entry for fr.4715 no.38 (plain POST search form, works from the cloud per the access playbook table), or grep a shallow clone of dbourdeau/cyphersolver for the same cached ark:/12148/cc577658 notice POOL.md used for item 38's sibling row; either could add a sender/recipient/date this folder's NOTES.md currently lacks | nobody | 1 | open |  |
| H8 | 8 | Resolve the "61" vs "66" foliation flagged in images/manifest.json against archivesetmanuscrits.bnf.fr's own finding aid for this volume, or the Gallica manifest's own canvas-label sequence around canvas 137, so any future outward citation of this leaf uses the volume's own numbering | nobody | 1 | open |  |
| H9 | 9 | JSTOR scholarship search for Charles de Lorraine Duke of Mayenne's cipher correspondence 1592-93 (sender/recipient/date ANDed with a cipher keyword, plus a bare quoted-phrase row once any decoded fragment exists), per the verifier brief's two-family JSTOR method | doc a JSTOR-QUEUE.tsv row for this target, not yet filed | 0.5 | open |  |
| H10 | 10 | A BnF reproduction request for a higher-resolution native capture of f.61r beyond the current 900px sheets, held because F61-CAL's own outcome (c) found the manuscript already very legible at this width -- only worth raising if a later test shows resolution, not shape-to-drawing transfer, is the limiting factor | person the owner (a copy/reproduction request, access playbook item 4) | 0.5 | open |  |

## Log

2026-09-27 20:33 | session_0198Bo8Dhz8XHkanQxcnayCk | seed | 0 | CAMPAIGN.md written, 10 hypotheses.
