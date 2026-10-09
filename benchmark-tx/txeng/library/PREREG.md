# PREREG TXE-S: cross-target exemplar library, two-reader-agree compare (9 Oct 2026, 08:32 UTC by date -u; LANE TX-ENGINEER, account 4, Opus 5.5; pushed BEFORE any sheet is read)

Brief `.claude/briefs/runs/2026-10-09-account4-txe-s.md` (ideas O7 + O8 of research/TX-IDEAS-2026-10-09.md = owner's items 7 and 8).
Binds with benchmark-tx/PREREG-txeng-2.md (units, blindness, Amendment: single-instrument gate p < 0.01).

## Library (owner's items 7 + 8)
`tools/tx_compare.py library --out benchmark-tx/txeng/library/lib`: for each of the 51 codes of the 1572 key
(harvest/sign_id_map_1572.json), up to 4 tiles:
1. the printed key cell, cut from sources/cryptiana/web/img/NeversBirago.png at the cell box recorded by
   harvest/cut_sign_sheet.py (the source of sign_sheet_blind_1572.png; Tomokiyo's reconstruction, credited);
2. up to 3 secure tiles from atlas/secure_tokens.tsv (the 636 S-grade tiles behind atlas/sheet_truth/, 11 leaves, none of
   them no.87: f178r/f178v/f179r excluded by page), chosen by farthest-point sampling on glyph_atlas.py's classify features
   (HOG-PCA + log size, `pick_spread(spread=True, trim=0.2)`: medoid first, then the tile farthest from those picked,
   the 20% farthest from the mean dropped first when a code has 5+ tiles, so a mis-aligned tile is not the "spread" pick).
Other family targets with H/C tiles: searched 9 Oct 2026 (ciphers/*/atlas, secure_tokens.tsv, key_1572 references:
birago-fr3252-1571-72, ceppo-nevers, guazzo-nevers and others carry no box-level H/C tile set); none added. Per-code counts
are printed by the tool and pasted into RESULTS.md.

## Unit, show rule, layout
- Unit dev_tune (f178v L01-12), baseline L = benchmark-tx/txeng/units/labels_dev_tune.tsv.
- Show rule UNCHANGED from TXE-A (atlas held-out top-1 != L; top-1 share < 0.6; L merged conf M/L), same topk file
  (benchmark-tx/txeng/compare/topk_no87_allheld.tsv), same box_pos.tsv and conf files. **This is the third compare run at this
  show rule (TXE-A, its M1b re-resolutions, now TXE-S): a FAIL retires the compare family under rule 3's third-attempt
  clause.**
- Candidates = L sign + atlas held-out top-3 (deduplicated), numbered, seeded order (seed `txe-s`). Row = the sign in
  context | up to 4 library tiles per candidate. Sheets of at most 24 rows. Layout deviation declared now: each sheet is
  saved as two image files (rows 1-12 `sheet_NN_a.png`, rows 13-24 `sheet_NN_b.png`, row numbers continuous) so that 16
  tiles per row stay legible; both halves go to the same reader call (one sheet per call).
- TXE-A's dev show count was 165 positions (= 7 sheets of 24). The cap holds about 5 sheets x 2 readers, so **only the first
  5 sheets (the first 120 shown positions in line order) are read**; the remaining shown positions keep L. Stated here
  before any read; the gate is reachable on 120 positions.

## Readers
Two independent Opus 5.5 subagents (`model: opus`), R1 and R2, each read every one of the 5 sheets (10 calls), same task
text as TXE-A (paths changed only; reads to reads_r1/ and reads_r2/). Neither sees the other's reads, a truth file, a decode
or the key TSV of the sheet. Raw reads are committed and pushed before any resolve or score.

## Resolve (new rule) and gate
- `tools/tx_compare.py resolve --unit dev_tune --agree reads_r1 reads_r2`: a position changes from L only when both readers
  pick the same candidate and it is not L's sign; any disagreement, none, ? or missing keeps L.
  Output benchmark-tx/outputs/birago1572-no87/passG2_library_dev_tune.tsv.
- Gate: `tools/tx_bench.py passG2_library_dev_tune.tsv --bench BENCHMARK-TX.tsv --item birago1572-no87 --paired
  benchmark-tx/txeng/units/labels_dev_tune.tsv`: fixed > broken AND sign test p < 0.01. Met -> eval_heldout once (two
  readers, the one eval look). Not met -> FAIL, no eval; compare family retired.
- Information only (not gating): each single reader resolved by the TXE-A rule (a pick overrides L); the two readers'
  agreement rate on shown rows; after commit, whether the joint pick differs from L more often where L is wrong
  (a read-free sorter signal).
