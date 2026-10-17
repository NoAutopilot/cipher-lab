# Research director, wave 8 (17 Oct 2026, 07:4x UTC by date -u): Aitzema, the 1617-18 run at reading size

Common tail: .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a dollar
figure for yourself, `tools/experiment_log.py --check`). The job ends its NOTES section with the six research-director questions in one
line each. Report what was found and where it was not found; no novelty class (rule 10).

## JOB AITZEMA-RUN1618 (account 4; Sonnet 5; cap USD 4; box 40 minutes; hosts: service.archief.nl only (the scan list is already in ciphers/aitzema-sg6025-1618/images/manifest.json and scans.tsv -- the item page's drupal-settings JSON, re-fetched once only if the uuids are missing), one at a time, >= 1.5 s apart, <= 62 requests; Price: vision calls: 9 x USD 0.3 = 2.7)

ciphers/aitzema-sg6025-1618, NOTES "## AITZEMA-SHEET (17 Oct 2026)": a stride-10 sample at thumbnail size found 0 cipher blocks in 59
of 589 scans, with the caveat that the cipher letters are a 1617-1618 minority that a stride can miss and that 168-256 px thumbnails
cannot show a cipher block reliably. The lias runs 1617-1625; the deciphered letters (res. 1789 Dec 1617, 1923 Jan 1618, 2305 Feb 1618)
sit in its first year. Question: at reading size and stride 1, does the 1617-18 run carry cipher, and where is the 17 Feb 1618 Lubeck
original (the known-plaintext pair)?
1. From scans.tsv / manifest.json take orders 1-60 (and the two unsure scans 131, 221). Fetch each through the IIIF image route at about
   800 px wide (`.../full/800,/0/default.jpg` on the iiif.url the item page gives per scan; if that size is refused, the default route
   and a local resize), <= 62 requests. Fetch once, keep images/ under 30 MB (store the 800 px files, no native).
2. Eight contact sheets of 8 scans at 800 px (2 x 4) for orders 1-60 plus one sheet with 131 and 221 at native crops (that is the vision
   line, 9 calls): per scan, cipher block yes/no/unsure (numeral or symbol groups), any date or docket legible (write it), any
   decipherment beside cipher. Extend scans.tsv.
3. Report: the cipher-bearing orders found, the first legible dates (does the run start in 1617?), whether the 17 Feb 1618 Lubeck letter
   is among them, and the next step with its price: found with the pair -> AITZEMA-ALIGN (tools/interlinear_align.py on the pair, N-floor
   lesson HEID-1623CAL, matched control; a period decipherment reading another letter is key application); cipher found without the
   pair -> which orders to read next; nothing found in 1-60 -> say so, and whether the lias is chronological at all (dates seen).
   No transcription, no decode. "## AITZEMA-RUN1618 (17 Oct 2026)" in NOTES.md.
Report: cipher-bearing orders / 62, dates seen, the Lubeck pair found or not, next step and price, five lines.
