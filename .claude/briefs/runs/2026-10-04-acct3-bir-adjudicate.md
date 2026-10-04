# BIR-ADJ (account 3 worker) -- 4 Oct 2026 07:3x UTC (account-3 orchestrator)

Target ciphers/nevers-birago-fr3251-1572. Read harvest/ownersort/RESULTS.md (incl. the orchestrator re-score) first.
Question: on the tiles where the owner's sort disagrees with two agreeing blind machine readers (109 tiles, three_reader.tsv
where A == B != owner_family and status moved), who is right? The language score cannot settle it (every base text fails the
judge). Instrument: a value-blind image adjudication.
1. Pre-register (push before any read): for each such tile, cut a crop of the tile plus 2 neighbours each side (tools/iiif_lines.py
   from the Gallica arks in recut.tsv), and three reference strips: 6 confident members of the machine pile, 6 of the owner pile
   (if the owner pile is new, its other members). Shuffle which strip is shown first. No sign values, no letters, no pile names.
2. Known-answer control first: 30 tiles where owner and both machines agree, presented the same way with one true and one wrong
   reference pile (the wrong one = the nearest look-alike pile). The adjudicator must pick the true pile at >= 80% or the job stops
   ("non-test at this instrument").
3. Two blind Sonnet passes per tile (crop + strips, one call per batch of 10 tiles), then an Opus reconcile on splits only.
4. Report per leaf: owner right / machines right / both plausible / neither, with counts; grade each tile's verdict; list tiles
   where the owner is right as candidate corrections (M, never S without a second instrument). Then re-run
   `ownersort.py --new-piles-unknown` variant with only the owner-right corrections applied, and report the gate.
Cap 10 (rate-limit measure), box 90 min, price per pass (21 batches x 2 passes + control 3 batches x 2 + reconcile). ROOM claim/done,
NOTES.md section "BIR-ADJ (4 Oct 2026)". Report found / not found; no novelty claims.
