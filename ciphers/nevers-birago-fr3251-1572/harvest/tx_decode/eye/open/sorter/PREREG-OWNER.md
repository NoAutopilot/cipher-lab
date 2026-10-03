# PREREG-OWNER (BIR-OWNER, account-3 worker, 3 Oct 2026 18:40 UTC) -- written and pushed before any score

Input: `owner-2026-10-03/` (the owner's PARTIAL sorter save; "doesn't mean they're right"). Applied with
`tools/sign_sorter_apply.py --labels owner-2026-10-03/labels.tsv --db owner-2026-10-03` (the tool already reads flat per-doc JSON
via `d.get('data', d)` and a missing checked/ folder; no tool change needed) -> `owner_settled.tsv`.
Status counts before scoring (from the tool's summary, not a score): kept 346, moved 68, taken-out 58, bad-cut 11, aside 5; T60 pile verdict "same".

Tile -> position: where a line has as many tiles as positions, tile i = position i; otherwise sorter tiles are aligned to the transcription positions by sequence alignment of the sorter's own labels to
the transcription signs (difflib), equal-length replace blocks mapped in order; f117 L09 lacks the tile for position 21 and f168 R03 lacks
position 19 (both verified by alignment before this file was written).

Base readings (a): f.117r and f.168 = `eye/apply/decode_apply.json` tokens (BIR-APPLY); f.144r = `eye/open/decode_open144.json` tokens (BIR-OPEN-144).

Owner pick at a position = a tile with status `moved`. Its value: the key value of the destination sign if the destination is a sheet sign
in `harvest/key_1572_sheet.tsv`; U (no value, '?') if the destination is an auto-named new pile (`-b`, `-c` ...) or an off-sheet label,
since nothing here can say the key covers that shape. taken-out / aside / bad-cut / kept = no change (unsettled or untouched; "not moved"
is never read as confirmed). A pick is a *change* only if its value differs from the base value at that position.

Grade rule: S where the owner's destination sign equals the sign read at the same position by at least one blind instrument --
A1-BIR-VERIFY two-option (`verify/vpositions.tsv` + `vanswers_<leaf>.tsv`), BIR-OPEN open-choice (`open/opositions.tsv` + `oanswers_<part>.tsv`),
BIR-OPEN-144 (`open/opositions_f144r.tsv` + `oanswers_f144r.tsv`); decoy-arm reads count, since they are blind reads of that position.
Owner-only changes M. Moves into new piles U. A1-BIR-EYE agreement is reported but does not grade.

Comparison (score = `tools/judge_plaintext.py` NgramModel mean log10 4-gram/letter, the same model and control windows as the CLI; spec
`specs/birago-fr3252-f117.json` (fr) for f.117r, `specs/nevers-birago-fr3251-1572.json` (it16dip) for f.168 and f.144r; letters only from the
tokens' values, '?' dropped, bracketed word values kept as letters):
  (a) base; (b) base + every owner change (values as above; S and M both applied, U removes the letter);
  (b-S) secondary, only the S-graded changes + the U removals;
  (c) control, 200 draws (seed 20261003): the same number of value changes as (b) at random positions of the same leaf, each given a random
      sign from that position's lattice top-k candidate list other than its base sign (`open/olat_<leaf>_topk.tsv`, the in-family look-alikes),
      plus the same number of U removals at further random positions. Positions with no alternative candidate are not drawn.
Gate, per leaf and on the pooled sum of (score x letters): the owner's picks "help" only if (b) > (a) AND (b) > p95 of (c).
Note: the top-k candidates carry LM weight, so the control is, if anything, biased upward (conservative for the owner).
Nothing is applied to committed readings unless (b) passes on that leaf.
