# PREREG-HEID1621I (written before any crop is fetched or any tile re-read; 15 Oct 2026, 23:2x UTC by date -u)

Job: .claude/briefs/runs/2026-10-15-acct4-depth-steps-2.md, JOB HEID-1621I. service.archief.nl <= 6 requests; 0 vision calls (no reader
subagent); the re-read is this worker's own eye on windows cut from the native line crops. No decode, no key, no reading: nothing here
assigns a value to any unit.

## Material
- Crops: the native block regions whose sha1s are already on file in images/manifest.json -- 375 "900,780,1780,1420" (heid_6021g),
  379 "730,1640,1960,1420" (heid_6021), 423 "760,2000,1900,720" (heid_6021g) -- fetched once with the METS (4 requests), each region
  sha1 checked against the manifest before use (a mismatch is reported and the crops are not used), then `tools/iiif_lines.py --image
  <region> --out <dir> --prefix h375|h379|h423 --debug` with the same parameters as HEID-1621/HEID-1621G, crop sha1s checked against
  manifest where recorded. Departure from the brief stated here, before the fetch: the brief says "scans at 1200 px"; the 1200 px scans
  are 4.3x below native, too small for a secretary-hand letter re-read, and their crops are not the ones the reads were made on. The
  native regions are the reads' own source and their sha1s are on file, so they are fetched instead (4 requests <= 6).
- Tiles: the 22 split positions of heid1621h/focus.tsv / tiles_letters.tsv, candidate pairs as listed there.

## Re-read and settle rule (tools/lookalike_pass.py reconcile's fixed 2-of-3 rule, plus one stricter clause)
- Within-witness tiles (w375_*, w379_*, w423_*): the eye names the sign at the window from the tile's candidate set (or NONE / X_NEW),
  conf H (unambiguous), M (probable) or L/SPLIT. A firm (H/M) label equal to reader A or B settles the tile (tool rule).
- Cross-witness tiles (x375_379_N, A = 375's reconciled letter, B = 379's): two physical glyphs. The eye reads the 375 glyph and the 379
  glyph separately; the tile settles only when BOTH are read at H and to the same label and that label is A or B. Two firm but
  different readings mean the duplicate itself differs (or the hand varies): the tile stays UNSETTLED and is reported as a witness
  difference, not a reader error.
- Stated limitation: the third reader is not blind to the candidate set (the windows prompt's own design: candidates, never passC) and
  is the worker who runs the gate. A PASS below is therefore "agreement after a non-blind third read", not accuracy (CLAUDE.md Usage 6).
- Unsettled tiles go to heid1621i/focus.tsv for the owner's sign sorter (never blocking).

## Control re-run (gate fixed here: 0.90)
375-vs-379 per-unit agreement on the post-pass units (heid1621g alignment, 45 aligned units, the same difflib rule as PREREG-HEID1621G;
letters case kept). Settled cross tiles change both sides to the settled label; settled within-witness tiles change that witness's
reconciled letter only if the reconciled letter was the losing label.
- PASS (>= 0.90, i.e. at least 41/45): the trailing letters are licensed at **S-as-transcribed** (the sign is named as transcribed; no
  value read) at every position where (a) the two blind readers agreed or the tile settled 2-of-3 and (b) for the 13 Aug block the two
  witnesses agree after the pass; every other position stays M. 423's letters (no second witness) get S only under (a).
- FAIL (< 41/45): every letter stays M; the spec keeps the letter field declared unreliable.

## Stop rule
Cap USD 4 or 80% of the 60-minute box (box 23:13-00:13 UTC; no new unit after 00:01 UTC), whichever first.
