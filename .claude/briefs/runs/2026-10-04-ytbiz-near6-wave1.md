# LANE-NEAR6 wave 1 (4 Oct 2026, written 10:1x UTC by LANE-NEAR6, account 2 / ytbiz, session_019jKS1wURJVECZN9M5sEAPj)

Common rules: the "Common to every job below" section of `.claude/briefs/runs/2026-10-04-ytbiz-near4-wave1.md`, with
"LANE-NEAR4" read as "LANE-NEAR6" everywhere (claims, done line addressed "for LANE-NEAR6 (account 2)").
Intake gate: `python3 tools/intake_gate_check.py fr16104-vivonne-spain-1572` rc=0 at 10:11 UTC (pasted by LANE-NEAR6):
`fr16104-vivonne-spain-1572: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.

## Shared by both piece jobs (N6-VIV53, N6-VIV63) -- they run at the same time in the same folder
- Read NOTES.md sections "N5-VIVK", "N5-VIVTAB" and "N5-VIV54" first; follow N5-VIV54's method exactly (its brief:
  `.claude/briefs/runs/2026-10-04-ytbiz-near5-wave1.md` "N5-VIV54"). Reuse tx/SIGNS.md labels, tx/reconcile_vivk.py's label rules,
  tx/viv54_clean.py / viv54_decode.py / viv54_test.py as the pattern -- extend them with a `--piece` option or write
  `tx/viv<NN>_*.py` that imports the shared parts; never edit what regenerates reading_piece54.tsv (its `--check` must still pass).
- Isolation from the sister job: your crops go to `images/p<NN>/` (iiif_lines `--out ciphers/fr16104-vivonne-spain-1572/images/p<NN>`, its
  own manifest.json), your files are named `*<NN>*`, your NOTES section is appended at the end of NOTES.md after `git pull --rebase`
  immediately before the edit. Do not touch key.tsv: an M-code question or a label change goes in your section as a suggestion.
- Folder size: images/ is 24 MB already. Commit only the crops your NOTES cites (or none) and always the manifest + the exact crop
  commands so they regenerate; `du -sh ciphers/fr16104-vivonne-spain-1572` under 30 MB at your push (AX2-SHRINK pattern if needed).
- Step 0 premise first (Gachard I/II djvu text, La Ferriere Catherine IV, the neighbouring leaves for a "dechiffre"); if a decipherment or
  printed plaintext of your piece turns up, record it and stop.
- Units: each cipher page = 2 blind Sonnet passes + 1 reconciliation = 3 units at ~USD 1.3 (N5-VIV54 ran 2 pages for 7.93 all in, ~USD 4
  per page). State page count x rate in NOTES before the first subagent call; stop before a page that would cross 80% of cap or box and
  decode what is done.
- PREREG-N6VIV<NN>.md pushed before any decode. Gates: (a) where interlinear words exist, the N5-VIV54 gloss check (frozen gloss rows read
  at native resolution BEFORE decoding, 200 shuffled-key draws, pass = > null p95 AND >= 0.60); (b) where none exist (expected for 63), a
  statistic you pre-register whose POSITIVE CONTROL passes first: the N5-VIVK f.103r decode (tx/f103r_control_decode.txt) and the ink-54
  decode subsampled to your piece's token count, each against its own 200 shuffled-key decodes (e.g. French word-cover with a fixed
  lexicon, or the fr16 judge's 4-gram score used as a relative statistic vs the shuffled-key null, not against real_p05). If the positive
  control does not pass its own null, the statistic is not a gate: say so and report the target descriptively. Ceiling check per rule 3.
- Grade per token as N5-VIV54 (H = both readers agree or a label rule settled it AND the code is C in key.tsv; M = M code or unsettled split;
  U = code not in key.tsv); state that H is key-source grading, not legibility. Counts. `--check` reproducibility (rule 7).
- print_check on 5-10 decoded phrases (phrases_<NN>.txt). Report what was found and where it was not found; do not classify novelty.
- NOTES section, Remaining gaps / Escalation refresh (after a pull, merging the sister job's lines, keep both), gaps_check OK line.
  ROOM done line for LANE-NEAR6 (account 2) with gate numbers beside controls, err_2reader per page; if a gate passes add
  "fr16104-vivonne-spain-1572 piece <NN> ready for audit 1" in the same line. status.json / NEAR.md untouched (orchestrator).

## N6-VIV53 -- ink 53 (5 Sept 1572, Saint-Gouard to the duc d'Anjou, fr.16104 ff.170r-171v) (Opus; cap USD 15; box 150 min)
fr.16104 = ark btv1b9009609w, canvases 184-186 (piece_table.tsv row 53: f.170r 6 plain lines then cipher; ff.170v-171r on c185 not yet
viewed; f.171v ~22 cipher lines then closing; f.172r address leaf). View c185 at 1600 px first and count cipher pages (expect 3-4, ~100
lines). Look for interlinear words on every page (gate a if any).

## N6-VIV63 -- fr.16105 ink 63 (10 Oct 1573, to the King, ff.190r-194r) (Opus; cap USD 30; box 240 min)
fr.16105 = ark btv1b9009663p; canvas c shows f.(c-4)v left and f.(c-3)r right (N5-VIVK fit near f.100; the offset may change further on --
piece_table.tsv puts f.190r on c195 right, so confirm with tools/gallica_folio.py and the leaf numbers before cropping). Cipher from the
head of f.190r to ~line 20 of f.194r (c199 right per piece_table), ~8.5 pages, ~340 lines;
no interlinear gloss seen (gate b). 1573 is inside Tomokiyo's April 1572-Nov 1574 key span. If 8.5 pages x 3 units would cross 80% of the
cap, read the first pages that fit and decode those; name the rest in Remaining gaps with its cost.

## N6-KERV -- Kervyn de Lettenhove, Les Huguenots et les Gueux (1884) grep (Sonnet; cap USD 1.5; box 30 min)
NOTES "N5-VIV54" print_check found a Google Books hit for "saint gouard septembre 1572 chiffre" in this work, not opened. Find the volumes
on archive.org (advancedsearch, no login), fetch the djvu.txt once to scratch (not committed), grep "Gouard", "Saint-Gouard", "7 septembre",
"5 septembre", "10 octobre 1573", "chiffre", "dechiffr". Write a short NOTES section "N6-KERV" (identifier, hits with page/leaf context,
whether any passage prints or summarises inks 52, 53, 54 or 63 -- quote <= 2 lines each), and add the volume to sources.tsv if it bears on
a piece. Do not touch the piece jobs' files. Report what was found and where it was not found.

## N6-HEL76 -- hellen-frederick-1752: transcribe R4376 P3 (f.56, 1754, codes 1-500) and test it on R1049 (7 Sept 1756) (Opus + Sonnet subagents; cap USD 8; box 90 min)
NEAR5 handoff open item (no owner input). Read NOTES.md sections "NEAR3-HEL3" (R4376 facts: P1 docket 1754, P2 blank form, P3 filled French
table 1-500 with "zero" nulls, "la Haye", "pays bas", no holder), "NEAR3-HEL4" (the R4372 recipe this job copies), "N4-HEL6" and "N5-HEL7"
(statistic, OOV floor fix), and the LANE-NEAR5 gaps refresh (R4372 retired for R1049 by rule 3 -- do not use it as a candidate).
Intake gate rc=0 pasted by LANE-NEAR6 at 10:1x UTC is for Vivonne only: run `python3 tools/intake_gate_check.py hellen-frederick-1752` yourself
and paste it; nonzero = stop.
Method: exactly NEAR3-HEL4's steps 1-5 (its brief: `.claude/briefs/runs/2026-10-04-ytbiz-near3-wave2.md` "NEAR3-HEL4") with R4376 P3 in place
of R4372 P2/P3 and R1049 in place of R1953: PREREG (`key_r4376/PREREG.md`) pushed before any test, with the matched control drawn from R1049's
own 1-500 token count (subsample the positive control to that N, CLAUDE.md rule 3 last paragraph); one DECODE browser login, P3 full size into
the scratchpad (sha1 recorded), never committed; column crops via `tools/iiif_lines.py --image`, command pasted; 1 page x (2 blind Sonnet
passes + 1 reconciliation) = 3 units at ~USD 1.3; key_r4376/key.tsv + README conventions; run the tests; paste outputs. If the DECODE
full-size image is refused (role gate, see the CLAUDE.md host table), stop and log the blocker -- do not transcribe a thumbnail.
NOTES "N6-HEL76", HYPOTHESES.md row (target and control side by side), NEAR.md row Evidence/Last-touched if it bears, near_check, gaps
refresh + gaps_check OK line. Report what was found and where it was not found; do not classify novelty.
