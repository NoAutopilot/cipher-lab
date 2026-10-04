# PREREG-GAPS210 (STALE4 for account 4, account 1 worker, 4 Oct 2026, clock read 01:5x UTC, pushed before any vision read)

Target: naf14913-rousseau-venice-1743. Job GAPS210 (Verdict of FT4ad/GAPS204: "a 300 px sweep of the NAF 14913 leaves not yet
swept (outside ff.205v-289v) for further cipher passages (numeral groups) carrying 338, 534 or 722"). No transcription, no statistic.

Scope this session: canvases fetched at 300 px wide (Gallica IIIF `full/300,/0/native.jpg`), from f.205r backwards towards f.1r
(canvases 423 down to 15), as many as the request budget and box allow; ff.290r-392v (canvases 595-800) are not in this session's
budget and are named as the next step. Thumbnails stay out of git (folder at 32 MB); the fetch log (canvas, label, URL, bytes, sha1)
and the flag TSV are committed.

Sheets: 6 x 3 tiles of 300 px width per sheet (<= 1800 x ~1300 px), each tile labelled only with a random tile id. Every sheet carries
four controls at random positions, not identified to the reader:
- POS-A f.205v (canvas 424): the f.206 cipher passage (62 numeral groups, the f.206 key's own page) -- strong positive.
- POS-B f.266r (canvas 545, existing thumbnail): ~15 lines of numeral groups inside a clear letter -- medium positive.
- POS-C f.252r (canvas 517, existing thumbnail): 15 numeral groups with interlinear gloss -- weak positive (sensitivity probe).
- NEG f.206r (canvas 425): Rousseau's clear decipherment slip -- must not be flagged.
Reader: at most 2 blind Opus subagent calls, each given only sheet paths, asked per tile: numeral-group cipher present (yes / maybe /
no) and rough extent. Mask (tile id -> canvas) written only after both reads are saved.

Gate (per sheet): POS-A and POS-B both flagged yes/maybe. A sheet that misses either is a non-test for its sweep tiles (their "no"
is not a negative; listed as unswept). POS-C recall and NEG false-flag rate are reported across sheets (sensitivity to short passages;
a NEG flag on a sheet makes that sheet's sweep flags "unconfirmed").
Outcomes:
- O1 one or more sweep tiles flagged yes/maybe on passing sheets: listed with canvas and folio label in `align/gaps210_flags.tsv`,
  grade M (thumbnail flag), next step a native-resolution look at each flagged leaf (not this job).
- O2 no sweep tile flagged on any passing sheet: "no numeral-group block visible at 300 px" for those folios -- conditional on POS-C
  recall (if POS-C is missed on most sheets, short passages of ~15 groups are below this instrument's resolution and are not excluded).
- O3 sheets failing the gate: listed; their folios count as not swept.
