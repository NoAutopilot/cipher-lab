# Research director, wave 7 (17 Oct 2026, 06:4x UTC by date -u): Aitzema, the first look at the lias

Common tail: .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a dollar
figure for yourself, `tools/experiment_log.py --check`). The job ends its NOTES section with the six research-director questions in one
line each. Report what was found and where it was not found; no novelty class (rule 10).

## JOB AITZEMA-SHEET (account 4; Sonnet 5; cap USD 4; box 40 minutes; hosts: www.nationaalarchief.nl (item page once) and service.archief.nl only, one at a time, >= 1.5 s apart, <= 60 requests; Price: vision calls: 8 x USD 0.3 = 2.4)

ciphers/aitzema-sg6025-1618 (verdict open, intake gate exit 0, CHECK-AITZEMA 17 Oct 2026): Foppe van Aitzema to the States General, NA
1.01.02 inv. 6025, 589 scans, digitised. Known: one confirmed known-plaintext pair (res. 2305: the 17 Feb 1618 Lubeck original in this
lias, read deciphered in session), two more deciphered letters named (res. 1789, 1923) without a pointer; the 1617 code's own location
unknown. Question: which scans carry cipher, how many, and does any carry a decipherment beside it? Lesson of HAGA-LEAF/LEAF2: no date
projection; look at the scans.
1. Scan list from the item page's drupal-settings JSON (order -> uuid -> service.archief.nl/api/file/v1/default/{uuid}, the route in
   ciphers/haga-sg6896-1622/images/manifest.json). Fetch every scan at a thumbnail size (about 700 px wide; <= 60 requests means a
   stride: every 10th scan, 59 fetches, or the viewer's own thumbnail tiles if a single request lists them -- say which).
2. Eight contact sheets of about 8 thumbnails each (that is the vision line): mark each thumbnail cipher-bearing or not (numeral or
   symbol groups), docket legible or not, and any interlinear or marginal decipherment. Write images/sheet_*.jpg (under 30 MB total),
   images/manifest.json, and scans.tsv (order, uuid, cipher yes/no/unsure, decipherment yes/no, note).
3. Report: the count of cipher-bearing scans at this stride, whether any has a decipherment beside it, the 17 Feb 1618 Lubeck original
   if it was in the sample, and the next step with its price (a full pass at stride 1 on the cipher-bearing runs; then the
   known-plaintext alignment of the Lubeck pair with tools/interlinear_align.py, HEID-1623CAL N-floor in mind; label key application
   if a period decipherment reads another letter). No transcription, no decode. "## AITZEMA-SHEET (17 Oct 2026)" in NOTES.md.
Report: cipher-bearing count / sampled, decipherments seen, the Lubeck pair found or not, next step and price, five lines.
