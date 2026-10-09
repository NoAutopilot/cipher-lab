# TXE-S: the cross-target symbol library in a two-reader-agree compare layout (LANE TX-ENGINEER, ideas O7 + O8 = owner's items 7 and 8; account 4, Opus 5.5; cap 10, box 100 min)

Read `.claude/briefs/runs/2026-10-09-account4-txe-COMMON.md` first, then `benchmark-tx/PREREG-txeng-2.md` (units, blindness,
Amendment: gate p < 0.01), `benchmark-tx/txeng/compare/RESULTS.md` (TXE-A: a compare layout with family-atlas exemplars made
the reader swap right line reads for look-alikes, fixed 4 / broken 16; its M1b variants failed too) and research/
TX-IDEAS-2026-10-09.md rows O7, O8, M1. Why this job exists: the owner's items 7 and 8 still carry no tested verdict. Item 7
is a LIBRARY: clean exemplars of every sign from every target in the key family, from the printed 1572 key itself
(`ciphers/nevers-birago-fr3251-1572/harvest/sign_sheet_blind_1572.png` cells and `key_1572_sheet.tsv`), and from the
sibling leaves' secure tiles (item 8: `atlas/sheet_truth/`, 636 S-grade tiles on 11 non-no.87 leaves; plus any other
target in the family with H/C tiles). The changed protocol, fixed now so this is not TXE-A again: a shown position's line
read is overridden ONLY when two independent compare readers pick the same candidate and it differs from L; a single
pick never overrides (TXE-A's failure mode).

## Pre-registration (write `benchmark-tx/txeng/library/PREREG.md` and push it BEFORE any read)
- Library: `tools/tx_compare.py build` gains `--library DIR` (a folder of per-code exemplar tiles assembled by a new
  subcommand `library`: for each of the 51 codes, up to 4 tiles = the printed sheet cell, then the 3 sheet_truth tiles
  with the highest classify-feature distance from each other, from non-no.87 leaves only; any other family target with
  H/C tiles is added by path and credited). Print the per-code tile counts.
- Unit: dev_tune (f178v L01-12). Show rule: UNCHANGED from TXE-A (atlas top-1 != L; share < 0.6; L conf M/L) -- this
  is the third compare run at this show rule, so a FAIL retires the compare family under rule 3 (say so in PREREG).
  Rows: sign in context | up to 4 library tiles per candidate; candidates = L sign + atlas held-out top-3; numbered,
  seeded order; sheets of at most 24 rows.
- Readers: TWO independent Opus 5.5 subagents read every sheet (same task text as TXE-A's); raw reads committed.
- Resolve (new rule): a position changes from L only when both readers pick the same candidate and it is not L's sign;
  `tools/tx_compare.py resolve --agree reads_r1 reads_r2` (add the option, with a test). Also report the single-reader
  resolution for each reader (the TXE-A rule) as information.
- Gate: `passG2_library_dev_tune.tsv --paired benchmark-tx/txeng/units/labels_dev_tune.tsv`: fixed > broken, p < 0.01.
  Met -> eval_heldout once (two readers, the eval look). Not met -> FAIL, no eval; the compare family is retired.
  Secondary: the agreement rate of the two compare readers on shown rows, and whether their joint pick differs from L
  more often where L is wrong (read-free after commit: a sorter signal).

## Report
`benchmark-tx/txeng/library/RESULTS.md` (gate line, per-code library counts, single-reader lines, agreement table,
`tools/tx_taxonomy.py` on G2 vs L after commit, task texts, calls); shelf and SYSTEM rows for the new options; Results-log
rows in research/TX-IDEAS-2026-10-09.md (ids O7, O8; rebase before editing) and the status cells of rows O7 and O8.
Vision calls: about 7 sheets x 2 readers = 14 on dev at about 1.5 (cap 10 holds ~5 sheets x 2: if the show rule yields
more than 5 sheets, read the first 5 sheets' positions only and say so in PREREG -- 120 positions is enough for the gate
to be reachable). Stop before a call that crosses 80% of cap or box. Report in a short paragraph (first line: dev
fixed/broken/p under the two-reader rule, then each single reader's) and stop.
