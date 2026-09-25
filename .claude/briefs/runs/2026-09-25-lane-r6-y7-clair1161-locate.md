LANE R6 Y7 -- clair1161-avis-flandre-1688: locate the cipher leaves (Sonnet, cap $5, box 45 minutes). Common: 2026-09-25-lane-r6-common.md.
Intake gate (live, 25 Sept 16:18 UTC): "clair1161-avis-flandre-1688: open (line 1) -- edition/page or full-text-search citation found within 6 lines" (exit 0).
You are this lane's Gallica fetcher. Read NOTES.md: ark btv1b90010063, 342 canvases all labelled "NP", finding aid cc137837/cd0e35310 gives
"folio 106 et suiv."; images/f106_full.png on disk turned out to be an engraved portrait (Y3, 25 Sept), so the canvas guess was wrong. Job:
(1) read the ink foliation on low-resolution probes (IIIF /full/300,/0/, one at a time, >= 2 s apart) and fit canvas = a*folio + b with
tools/gallica_folio.py --anchor pairs as LANE R6 Y5 did on Espagnol 142 (it pinned f.22 in 41 requests from the ink numbers); bisect toward
f.106; <= 70 requests. (2) Pinned: native-resolution leaves of the "Avis de Flandre, chiffrés" to images/ with manifest.json (under 30 MB),
describe cipher extent, system, any gloss or plain heading, sender/date clues. Replace or relabel f106_full.png in the manifest so no one is
misled again. Not pinned: canvas_sweep.tsv of every canvas read. NOTES.md section "## Y7: leaf located (25 Sept 2026, LANE R6)".
Hosts: gallica.bnf.fr only. ROOM done: "for LANE R6: clair1161 canvas <n>, <extent>, gloss <yes/no>".
