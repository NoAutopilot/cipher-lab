# No.87 mini sign sorter: the owner's own piles (BIR87-SORTER, 4 Oct 2026)

Published 4 Oct 2026 12:4x UTC by the account-3 orchestrator: https://claude.ai/artifact/RLiTdKMG6BRhoja1yEQY5Y (private, capabilities {"db": {}}; board card bir-no87-sort). Purpose: BIR-KEYFIT's
named next step (`../../harvest/keyfit/RESULTS.md`, "Next"): put the no.87 tiles (f.178r, f.178v, f.179r) into the
owner's OWN piles from the 4 Oct sort (`../owner-sort-2026-10-04/settled_labels.tsv`, 105 piles over f.117/f.144r/f.168),
so the clerk-sheet alignment can give one C value per owner pile. No sign values appear on the page or in its inputs.
Gallica-derived crops already on disk only (atlas/pages.json); the build makes no network request.

## What is on the page (numbers from the 4 Oct build)

- **248 no.87 tiles**, families T45 (65), T37 (63), T60 (54), T19 (53), T89 (12), T24 (1). A family is on the page when
  the owner made a new pile carrying its name (T45 -> T45-b) -- 28 families qualify, together far over the ~250 cap, so
  families are taken by no.87 count, skipping any that would cross 250. `scope.tsv` lists every family and why it is on
  or off the page. Largest off the page: not split T83 49, T86 45, T53 35, T76 29, T90 28; split but over the cap T33 32,
  T85 29, T96 29, T25 25, T80 18, T18 18, T36 18, T42 16, T98 12, T65 12 (scope.tsv). Those tiles keep their atlas label.
- **28 piles**: every owner pile a tile of those six families ended in, named exactly as in settled_labels.tsv (T19,
  T19-b, T19-c, X_NEW-l, T86, T83, T97, ...). T37-c and T45-c are owner piles with no reference tile on the page (their
  only tiles did not map cleanly to an atlas box), so no no.87 tile is seeded there; the owner can still start a pile.
- **120 reference tiles** (green check, "sorted by you"): up to 6 of the owner's own tiles per pile, nearest the pile
  mean. They are locked (`tools/sign_sorter.py --refs`): no take-out, no move, no drag; tap shows them on their line.
  They are NOT in `apply_labels.tsv`, so the apply step never writes them.
- **"Check these first", 30 tiles**: the no.87 tiles whose two nearest owner piles are within 6% in distance (smallest
  margin first, margins 0.001-0.019 in this build); the caption names the two piles.

## How the inputs are made (`build_inputs.py`, docstring has the detail)

1. Owner tiles (line-strip tiles) are mapped to family-atlas boxes by shifting each strip tile's centre back into the
   Gallica region image the atlas segmented: 445 of 488 map one-to-one (`owner_map.tsv`; 9 unmatched, 34 on an atlas
   box shared by two strip tiles, both left out).
2. Seed: each no.87 tile goes to the owner pile nearest in `tools/glyph_atlas.py` feats() space (the space `classify`
   uses), pile distance = mean of the 3 nearest owner tiles in that pile; candidates are the piles reached from the
   tile's k1/k2/k3 families. 195 of 248 seeds keep the atlas label; 53 go to another owner pile (`seed.tsv`).
   The seed is a computer guess for the owner to correct, not a reading.

## Build (orchestrator)

    sh ciphers/nevers-birago-fr3251-1572/sorter/no87/build.sh <scratch>/birago-no87-sign-sorter.html

(re-runs build_inputs.py, then sign_sorter.py with --refs/--focus, greyscale JPEG tiles, half-scale context pages:
28 piles, 368 tiles, about 1.7 MB; rendered headless with no script errors, 4 Oct 2026.)

## Apply (after the owner says the sort is done)

Export the page's db (`ArtifactData list` piles / moves / newpiles / checked into DIR, as in
`../owner-sort-2026-10-04/README.md`), then from the repo root:

    N=ciphers/nevers-birago-fr3251-1572/sorter/no87
    python3 tools/sign_sorter_apply.py --labels $N/apply_labels.tsv --db DIR --out $N/settled_no87.tsv --summary $N/summary.json

`apply_labels.tsv` holds only the 248 no.87 tiles (sid = atlas box, sign = seeded owner pile), so reference tiles never
appear in `settled_no87.tsv`. A tile the owner never touched stays at its SEED pile with status `kept`: that is the
computer's guess, not an owner decision -- only `moved` rows, and `kept` rows listed in summary.json `confirmed_tiles`
(approved with the "?" badge or "Right pile: keep it"), are owner-labelled.

## Feeding tools/interlinear_align.py (the next job, not run here)

`../../atlas/no87_box_token.tsv` maps each atlas box (sid) to its transcription token (fol, line, pos) in
`../../harvest/ciphertext_f178r.tsv` / `_f178v.tsv` / `_f179r.tsv`. The alignment job:

1. copies those three files to a new folder and replaces `sign` with `new_sign` for every owner-labelled tile
   (moved, or kept and confirmed) of settled_no87.tsv, leaving every other token as transcribed;
2. runs `../../harvest/align87/build_pairs.py` on the copies (it reads `H/ciphertext_<fol>.tsv` today: a `--cipher-dir`
   option is the small change it needs) -- an owner pile name such as T45-b has no numeric code yet, so give each new
   owner pile its own code the way off-sheet tiles get 1000 + k there, and keep word-sign piles of T11/T15/T26/T29/T46/
   T78/T84/T89 at 6000 + nn;
3. runs `python3 tools/interlinear_align.py align pairs.tsv align.tsv key.tsv --floor 5000` against the clerk's sheet
   (`../../harvest/f179r_sheet/decipherment_sheet.tsv`) with its matched control (`build_pairs.py --shuffle-words`),
   as NEVBIR-87ALIGN did; a value per owner pile is grade C only where the pile clears that control (rule 3).

The owner's piles are a third reader, not ground truth (`../owner-sort-2026-10-04/README.md`); a split must still be
tested before any key value rides on it.
