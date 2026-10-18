# Research director, wave 12 (18 Oct 2026, 05:2x UTC by date -u): program A/C, key-image test for sp84-fuente-1662

Common tail: .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a dollar
figure for yourself, `tools/experiment_log.py --check`). The job ends its NOTES section with the six research-director questions in one
line each. Report what was found and where it was not found; no novelty class (rule 10).

## JOB FUENTE-KEY (account 4; Opus 5.5; cap USD 4; box 40 minutes; hosts: de-crypt.org (ONE browser login, records 523, 522, 517 only); Price: vision calls: 5 x USD 0.5 + 1 reconciliation = 3.0)

CHECK-FUENTE (ciphers/sp84-fuente-1662/NOTES.md) found 11 undeciphered Spanish intercepts in SP 84/165 (1662, undigitised) and, on DECODE,
three SP 106/6 Key records with Spanish vocabulary: 523 `TNA_SP106/6_CharlesII_(0163-0164)` (1672, 2 pages), 522 `(0160)` (1 page), 517
`(0123-0125)` (2 pages). Tomokiyo describes SP 106/6 no. 34 as a decoding table using 1-211 without diacritics, 1-210 with an overbar,
1-211 with a double bar, 1-211 with triple dots, 1-210 with m, 1-220 with a crossed circle, 1-240 with a grave, 1-239 with a double prime
and 1-234 with a %-like sign, single letters scattered inside the figures. Question: does any of the three records match that description?
A match makes the 11-image TNA copy order (SPRINT.md P12) a key-assisted recovery; no match leaves it a cryptanalysis candidate and the order
is not worth placing yet.
1. One login, three records: `NODE_PATH=$(npm root -g) node tools/decode_browser_login.js 523 <scratch> --guess-fullsize`, with the same
   context fetching 522 and 517 (see the script's --probe/--click options; craven-rupert-1648 NOTES and the A2-HDK note are worked
   examples). If full-size is refused, use the largest thumbnail served and say so. Never print the account name, and scrub it from any
   saved HTML. One login only; a second failure stops the job.
2. Shrink each page to under 2500 px on the long side (PIL) before any vision call; never send a full 12 MB scan. For each of the five
   pages record the layout (table or list, plain-to-code or code-to-plain), the number ranges and the marks seen (overbar, double bar,
   dots, m, crossed circle, grave, double prime, %-like), whether single letters sit among the figures, and whether the vocabulary is
   Spanish. Do not transcribe the whole key.
3. Write "## Key-image test (FUENTE-KEY, 18 Oct 2026)" in ciphers/sp84-fuente-1662/NOTES.md: per record, match / partial / no match to
   Tomokiyo's no. 34 with the features as evidence; images to ciphers/sp84-fuente-1662/images/ with images/manifest.json, under 30 MB
   (keep reduced JPEGs if needed and note the re-fetch route). Note the Restoration date range and the 1672 date of 523 against the 1662
   intercepts. Name the next step: the copy order (folios, images) if a match, else what would tie a key to these intercepts.
Report: login result, per-record verdict, the next step, five lines.
