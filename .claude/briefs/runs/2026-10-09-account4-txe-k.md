# TXE-K: Fable as the adjudicator of reader splits (LANE TX-ENGINEER, idea M19; account 4, Opus 5.5 worker, Fable reader; cap 8, box 90 min)

Read `.claude/briefs/runs/2026-10-09-account4-txe-COMMON.md` first, then `benchmark-tx/PREREG-txeng-2.md` (units, blindness,
Amendment: gate p < 0.01) and research/TX-IDEAS-2026-10-09.md row M19 and its Results log (what has failed so far and why:
exemplars beside the sign pull the reader off right reads; thin-only selections are too small; the lattice never clears
its floor). Why this job exists: TX-FABLE (4 Oct) showed Fable is a worse plain line reader than Sonnet; the lane brief says
Fable is tried again only under a changed protocol, and TX-FABLE itself named "Fable as the reconciler or adjudicator" as
the untested instrument. Today the A/B disagreements of a page are settled by a third value-blind Sonnet reader from the
crops with the agreed neighbours as landmarks (nevers-birago NOTES "Blind passes": 10 to A, 6 to B, 1 neither on L11-23).
This job gives the same adjudication task to a Fable subagent and scores it against the known answer.

## Pre-registration (write `benchmark-tx/txeng/adjud/PREREG.md` and push it BEFORE any read)
- Unit: dev_tune (f178v L01-12). Items: every position where passes A and B disagree or either is M/L on those lines --
  take them from `harvest/f178v/passC_agreement.tsv` (status != agree, or merged_conf M/L) and `passC_disagreements.tsv`;
  the committed adjudication (what passC chose) is the Sonnet-adjudicator baseline on exactly these positions.
  Print the count (expect roughly 40-70).
- Packet: for each item, the line crop segment that holds it (the existing harvest crops, native) with the position marked
  by its neighbours ("the sign between the 4th and 6th of this segment", never a value), the two candidate cells named
  (A's T## and B's T##, order seeded random), the 51-cell `sign_sheet_blind_1572.png`; question "which of the two, a
  third cell T##, or ?". Sheets/packets of at most 20 items per call. Reader: a Fable subagent (`model: fable`), value-blind;
  then the SAME packets to one Opus 5.5 subagent as the second arm (so the comparison is adjudicator vs adjudicator, not
  Fable vs the committed read alone). Raw reads committed before scoring.
- Resolve: L with each adjudicator's choices applied at the item positions ->
  `benchmark-tx/outputs/birago1572-no87/passS_adj_fable_dev_tune.tsv`, `passS_adj_opus_dev_tune.tsv`.
- Gate (fixed now): for each arm, `tools/tx_bench.py ... --paired benchmark-tx/txeng/units/labels_dev_tune.tsv`, fixed >
  broken, p < 0.01 (L already carries the Sonnet adjudication plus relabels, so this is the hard baseline); also vs
  passC's choices on the item positions alone (accuracy of each adjudicator on the items, with the Sonnet adjudicator's
  accuracy from passC on the same items). Met for an arm -> eval_heldout once for that arm (the eval look). Not met ->
  FAIL, no eval. If both arms fail, the register's verdict is "adjudication by a stronger model does not beat the Sonnet
  third reader on this hand"; if Opus passes and Fable does not (or the reverse), say so.

## Report
`benchmark-tx/txeng/adjud/RESULTS.md`: item count, per-arm accuracy on the items vs the Sonnet adjudicator, the paired
lines, `tools/tx_taxonomy.py` on each arm vs L (after commit), reader task text, calls and Fable token use. Tool: the
packet builder goes into `tools/lookalike_pass.py` as a subcommand (`adjudicate-packet`) or, if that file's shape does not
fit, a `tools/tx_adjudicate.py` with --help and an offline test; shelf and SYSTEM rows (grade from the result). One
Results-log row per arm in research/TX-IDEAS-2026-10-09.md (ids M19-fable, M19-opus; rebase before editing). Vision calls:
about 3 Fable (2.5 each) + 3 Opus (1.5 each) on dev, the same again on eval only if a gate is met; cap 8; stop before a
call that crosses 80% of cap or box. Report in a short paragraph (first line: per-arm fixed/broken/p and item accuracy) and
stop.
