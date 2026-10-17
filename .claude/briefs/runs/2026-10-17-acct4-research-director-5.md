# Research director, wave 4 (17 Oct 2026, 03:2x UTC by date -u): the flagship's crossword test; the Haga leaf

Common tail: .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a dollar
figure for yourself, PREREG with a `## Decision` block pushed before any scored run, `tools/experiment_log.py --check`). Each job ends its
NOTES section with the six research-director questions in one line each. Report what was found and where it was not found; no novelty
class (rule 10).

## JOB VIV-KCELLS2 (account 4; Opus 5.5; cap USD 3; box 30 minutes; disk only, no network, no readers, no images; Price: vision calls: 0 x USD 0 = 0)

Flagship ciphers/fr16104-vivonne-spain-1572. Read NOTES "### VIV-KCELLS target step (17 Oct 2026)" and tx/kcells/target_result.json: the
clerk's p sits under reader label c (share 0.62, purity 0.75) and m under label 2 (0.61, 0.69), both unkeyed; ERR-SIM's cap_diag says p+m
coded lifts the zero-error ceiling 54 -> 143 against AD 94.6. Question: on the real ink 63 reading, do c=p and 2=m as trial cells move
the all-H run, and past the bar? Every run takes seconds (tx/err_sim/err_sim.py; tools/decode_key.py --try; the viv63 decode scripts).
1. PREREG first (`PREREG-VIV-KCELLS2.md`, Decision below, pushed before any run). No key.tsv edit in this job; trial cells live in a
   scratch key under tx/kcells2/.
2. Target: decode ink 63 (reading_piece63.tsv's tokens, the committed decode route) with c=p and 2=m at grade S-trial; report the
   longest all-H run (trial cells counting as H), V_strict, and the fr16 b2 score, before and after. Also inks 53 and 54.
3. Control, run first: the same two labels assigned random letters (value-shuffled, 20 draws, letters drawn from the alphabet minus the
   true pair); the real pair must beat the shuffle p99 on the all-H run AND on b2. Also the mirror: c=m, 2=p (the swapped pair) as a
   second null.
4. Crossover: rerun `tx/err_sim/err_sim.py` with the extended key (p, m as codes at ink 63's frequencies) across the ERR-SIM sweep
   (0.05 / 0.10 / 0.14 / 0.19 / 0.23, 5 seeds) and report the largest error level at which 3 of 5 seeds still show a run >= 94.6.
5. Packet: write tx/kcells2/packet.tsv (page, line, pos, label, clerk letter, crop path if a line crop exists under images/) for every
   p-position tile under label c, every m-position tile under label 2, and an equal number of c-label and 2-label tiles at other clerk
   letters (e, q, u) -- the material for a tile split by a reader or the owner's eye; no crops are cut in this job.
6. Decision (pre-registered): (a) real > p99 on both statistics and a run >= 94.6: a D2 candidate clause exists -- write it out with
   its liberties counted, name the verifier step (DV-VIV1), no key edit; (b) real > p99 but < 94.6: the cells are real and the readers
   cap the clause -- report the crossover vs the measured 0.14 and name the split (tile reader on packet.tsv, priced per tile, or the
   owner's sort); (c) real <= p99: the labels are too impure to use as cells; the split comes first.
7. "## VIV-KCELLS2 (17 Oct 2026)" in NOTES.md; RESEARCH.md s.5/6b updated; HYPOTHESES.md row via tools/experiment_log.py.
Report: before/after runs, shuffle p99, crossover, decision, five lines.

## JOB HAGA-LEAF (account 4; Sonnet 5; cap USD 4; box 30 minutes; hosts: www.nationaalarchief.nl and service.archief.nl only, one at a time, >= 1.5 s apart, <= 40 requests; Price: vision calls: 12 x USD 0.3 = 3.6)

ciphers/haga-sg6896-1622 (verdict open, intake gate exit 0, 17 Oct 2026; NOTES "## Next test" step 1). Find the 30 April 1622 duplicate
of Cornelis Haga's letter in NA 1.01.02 inv. 6896 (575 scans, IIIF via service.archief.nl; the item page's drupal-settings JSON gives the
scan list; ciphers/oldenbarnevelt-brederode-1605/screen_tools/na_fetch.py is the pattern; images/manifest.json records every fetch).
1. From CHECK-HAGA's two contact sheets (NOTES "## Material step": orders 120-318 sampled) narrow the April-June 1622 run; the lias is
   roughly chronological.
2. Fetch at most 12 single scans at native resolution, choosing dorsal/address leaves where a filing docket ("Haga ... April 1622",
   "duplicaat") is legible; read each docket (that is the vision line); stop at the first scan that is the 30 April duplicate or its
   docket, then fetch its text leaves (within the 12).
3. Record: scan numbers, the docket text as read, whether cipher groups are visible and roughly how many lines, whether any
   decipherment sits beside them; manifest.json; keep images/ under 30 MB. No transcription, no decode.
4. NOTES "## HAGA-LEAF (17 Oct 2026)" with the result or the narrowed range if not found; name the next step (HAGA-KEYAPP: Bourdeau's
   R2118 alphabet and nomenclator against the cipher spans with a shuffled-key control, label key application) and its price.
Report: found or not, scan numbers, cipher lines, next step, five lines.
