# BIR-ADJ pre-registration (4 Oct 2026, account-3 worker; pushed before any image read)

Question: on the 109 tiles where the owner's sort (4 Oct) overrode two agreeing blind machine readers
(`../three_reader.tsv`: status moved, A == B != owner_family), does the tile's image match the machine pile or the owner pile?

Instrument (value-blind, `build_adj.py`, seed 20261004, deterministic): one composite PNG per item: the tile on its line strip
with two neighbours each side and a red box on the tile; then "Strip 1" and "Strip 2", up to 6 reference tiles each, which strip
comes first drawn at random per item. No sign names, values, pile names or reader names on any image or in the prompt.
- Machine strip: tiles where A == B == owner == the machine pile and the owner kept them there; if short, filled from tiles
  where A == B == the machine pile. Never the tile itself or its two neighbours each side.
- Owner strip: if the owner pile is a sheet pile, its all-three-agree kept tiles, filled from its other owner members; if it is
  an owner-made new pile (T60-c, X_NEW-l, ...) or an X_ pile, its other owner members.
- Images: the page strips already on disk (`sorter/pages`, `birago-fr3252-1571-72/sorter/pages`), the same public Gallica regions
  (fr.3251 ark btv1b9060248g canvases 146/171/172; fr.3252 ark btv1b9060232m canvas 118) the owner sorted, so no refetch
  (deviation from the brief's tools/iiif_lines.py recut: same source pixels, the sorter's own tile boxes). Tile boxes are approximate
  (sorter/README.md) -- the adjudicator sees the context to compensate.
- `key.tsv` (this commit) maps item -> tile, piles and which strip is which. `items.tsv` is what the passes see (ids only).
- t014 has an empty owner strip (owner pile has no other member): untestable at this instrument, not shown.

Answer per item: 1, 2, both (both plausible), neither; confidence high/med/low.

Step 1, known-answer control (30 tiles, c001-c030): all three readers agree and the owner kept the tile; strips = the true pile and
the nearest look-alike pile (the sheet pile most often confused with it by any reader pair in three_reader.tsv, >= 6 confident
tiles), at most 4 tiles per pile, disputed-pair piles first. Two blind Sonnet passes, 10 items per call. Gate: each pass picks the
true strip on >= 24/30 (80%), answers 'both'/'neither' counting as misses. If either pass is below 24/30 the job stops:
"non-test at this instrument", no target item is read.

Step 2, targets (108 items t001-t109 minus t014): two blind Sonnet passes, 10 items per call; Opus reconcile (a subagent shown only
the same images, blind) on items where the two passes differ. Verdict mapping: machine strip -> machines right; owner strip -> owner
right; both -> both plausible; neither -> neither. Grade of each verdict: 'agreed' (both passes, at least one high confidence),
'agreed-low', 'reconciled'. Owner-right tiles are candidate corrections at M only (never S: one instrument).

Step 3: re-run `ownersort.py --new-piles-unknown --only-sids adj/owner_right.tsv` (moves outside the list = no change; output to
`v3_adj/`) and report the gate as is (PASS/FAIL per leaf, rank in 201), whatever it says.
