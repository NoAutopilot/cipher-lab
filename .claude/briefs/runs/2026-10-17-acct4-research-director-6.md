# Research director, wave 5 (17 Oct 2026, 04:3x UTC by date -u): split the merged labels; the Haga leaf, second pass

Common tail: .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a dollar
figure for yourself, PREREG with a `## Decision` block pushed before any scored run, `tools/experiment_log.py --check`,
`tools/iiif_lines.py`-sized crops only, never a whole page to a vision call). Each job ends its NOTES section with the six
research-director questions in one line each. Report what was found and where it was not found; no novelty class (rule 10).

## JOB VIV-KSPLIT (account 4; Opus 5.5; cap USD 14; box 60 minutes; disk plus the Artifact tool for one published page, no other network, no Gallica; Price: vision calls: 8 x USD 1.3 = 10.4)

Flagship ciphers/fr16104-vivonne-spain-1572. Read NOTES "## VIV-KCELLS2 (17 Oct 2026)" and tx/kcells2/packet.tsv (214 rows: 94 c-label
tiles at clerk p, 73 2-label tiles at clerk m, 48 contrast tiles of the same labels at e/q/u; 95 rows carry an ink-40 line crop pair
under images/, the rest are ink 67/70 leaves with no crops -- use only rows with crops, never fetch). The readers merge the p sign into
label c and the m sign into label 2 (T1); the crossover says even perfect cells need < 0.05 reader error. Question: can the two labels be
split into their two shapes, by a model reader and by the owner's eye, and do the two agree?
1. PREREG first (`PREREG-VIV-KSPLIT.md`, Decision below). Frequency-matched null first (seconds, disk): re-run tx/kcells2/kcells2.py's
   real-vs-shuffle on ink 63 with the shuffle letters drawn to match p's and m's corpus frequency (fr16), 20 draws; report whether the
   worker's caveat (the mean log-prob null favours frequent letters) changes the VIV-KCELLS2 verdict. Report only; no key edit.
2. Tiles: for every packet row with a crop, cut the sign tile from the line crop (pos -> the token's box as the committed reader output
   locates it; `tx/sorter_step1/pool.py` is the pattern that cut 628 tiles for the step-1 sort), write tx/ksplit/tiles/<id>.png and
   tx/ksplit/tiles.tsv (id, page, line, pos, label, clerk_letter kept ONLY in a separate truth.tsv that the sorter never reads).
3. Owner's sort (blind, TRANSCRIPTION.md): build one sorter page with `tools/sign_sorter.py` from tiles.tsv, two trays per label
   ("label c: sort into the shapes you see", "label 2: likewise"), no values, no model guess, no clerk letter on the page;
   `tools/sorter_preflight.py` and `tools/cvd_check.py` must pass; publish with the Artifact tool (capabilities {"db": {}}, title
   "Vivonne 1573: split two signs"), and write one ASKS.md row for the owner with the link and the ten-minute instruction (desk; the
   step-1 sort stays optional). Register the page in tools/data/sorter_families.tsv as the step-1 page is.
4. Model read (the measured exception, strongest model): a blind 2-way read of the same tiles per label -- exemplar sheet: the two
   shapes seeded from the alignment's own certain tiles (3 highest-purity p-tiles and 3 e/q-tiles for label c; 3 m and 3 u for label 2),
   then batches of about 12 tiles per call, 8 calls at most (that is the vision line), each answering "shape A or shape B" per tile, no
   letters named. Score against truth.tsv; null: truth labels shuffled 200 times (no new calls). Gate: accuracy above the shuffle p99
   on both labels, and >= 0.80 on at least one. Write tx/ksplit/model_read.tsv and the per-label accuracy.
5. Decision (pre-registered): (a) model read passes on a label: the split works by machine -- name the key-cell re-read of ink 63 for
   that sign (KEYCELL-READ scoped to label c or 2, priced per page from this job's per-call rate) and hold the owner's sort as the
   cross-check; (b) model read fails on both: the owner's sort is the instrument; the parent scores it against truth.tsv when it lands;
   (c) the tiles are unusable (cut failures, under 30 per label): say so, no read.
6. "## VIV-KSPLIT (17 Oct 2026)" in NOTES.md; RESEARCH.md s.5/6 updated; HYPOTHESES.md row via tools/experiment_log.py. Images under
   30 MB. Report: null re-test verdict, tiles cut per label, model accuracy per label vs p99, the artifact link, decision, five lines.

## JOB HAGA-LEAF2 (account 4; Sonnet 5; cap USD 3; box 25 minutes; hosts: www.nationaalarchief.nl and service.archief.nl only, one at a time, >= 1.5 s apart, <= 15 requests; Price: vision calls: 7 x USD 0.3 = 2.1)

ciphers/haga-sg6896-1622, NOTES "## HAGA-LEAF (17 Oct 2026)": the 30 April 1622 duplicate is projected to scan orders 321-327 of
NA 1.01.02 inv. 6896 by the docket calendar (orders 320 and 328 anchored); the default-image route from the item page's
drupal-settings JSON is on file in images/manifest.json. Fetch orders 321-326 (and 327 only if needed) at native resolution, read each
docket and opening, and say which scan is the 16/30 April duplicate ("duplicaat", Haga, Constantinople) and whether its cipher groups
have a decipherment beside them; count the cipher lines. Manifest entries for every fetch; images under 30 MB; no transcription, no
decode. "## HAGA-LEAF2 (17 Oct 2026)" in NOTES.md with the result and the next step (HAGA-KEYAPP: Bourdeau's R2118 alphabet and
nomenclator on the cipher spans with a shuffled-key control, label key application, about USD 4) or, if still not found, the one
next cheap step. Report: scan number or not found, cipher lines, decipherment beside it or not, five lines.
