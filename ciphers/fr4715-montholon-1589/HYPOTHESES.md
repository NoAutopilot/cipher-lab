# fr4715-montholon-1589 -- hypothesis families (append-only)

CLAUDE.md rule 3: CONTROL and TARGET numbers side by side. Created by MONT-CAL, 27 Sept 2026.

## Transcription instrument: vision reading of group crops (MONT-CAL, 27 Sept 2026)

| Family | CONTROL | TARGET | Status | Reason |
|---|---|---|---|---|
| per-group crops by column ink profile, then a vision reader (recipes A Sonnet strip+crops, B Opus, C Sonnet crops only) | synthetic offline test: 10 spaced groups -> 10 pieces; uniform spacing -> 1 piece (tools/tests/test_iiif_lines.py item 4) | f.81r L03/L08/L13/L15: blank-run widths unimodal 1-14 px; gap 6 gives 62/62/52/52 pieces vs dump 63/57/62/64, but only about 12 of 21 L03 boxes are one group | **untested-by-this-tool** (not refuted) | this hand does not space groups apart, so group crops cannot be cut; no recipe call was run |
| key-constrained segmentation of a boundary-free digit stream (feasibility, no reading) | random valid 1/2-digit parse: letter 0.440 (dump stream) | dump stream: letter 0.990, dotted 1.000 (dots kept); our v2 digits: letter 0.499 vs 0.461 as segmented | **works on the known answer** | segmentation is recoverable from the key; the binding loss is digit accuracy, 0.677 in order vs a 0.502 digit-shuffle control |
