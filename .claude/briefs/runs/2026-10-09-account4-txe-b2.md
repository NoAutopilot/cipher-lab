# TXE-B2: replicate the crop-geometry read (LANE TX-ENGINEER, idea M2 replication; account 4, Opus 5.5; cap 5, box 60 min)

Read `.claude/briefs/runs/2026-10-09-account4-txe-COMMON.md` first, then `benchmark-tx/txeng/geo/RESULTS.md` (TXE-B's result:
one Opus read on the re-cut geo unit, err 0.136 -> 0.089, vs pass A fixed 12 / broken 4, p 0.077 -- a near-miss under the
p < 0.01 gate; the L03 tail was read, 5 of 8 right) and `benchmark-tx/PREREG-txeng-2.md` (units, blindness, Amendment).
Why this job exists: a 12/4 count on one read is the strongest signal of the campaign so far and too small to clear the
gate alone; a second, independent read on the SAME crops either reproduces it (pooled 24/8 clears p < 0.01) or shows the
first was luck. Nothing about the crops or the brief changes.

## Pre-registration (write `benchmark-tx/txeng/geo/PREREG-B2.md` and push it BEFORE the read)
- Crops: exactly the files TXE-B read (its RESULTS.md names the directory under benchmark-tx/txeng/geo/ and the manifest);
  verify their sha1s against the manifest, change nothing.
- Reader: ONE blind Opus 5.5 subagent call over the same 18 crops with the same text TXE-B used (its RESULTS.md quotes the
  task text and the generated crops_note.md); the only difference is a fresh subagent. Raw read to
  `benchmark-tx/txeng/geo/passH2_raw.tsv`; commit and push before scoring; normalise as TXE-B did ->
  `benchmark-tx/outputs/birago1572-no87/passH2_geo.tsv`.
- Gate (fixed now): (1) the replication alone, `tools/tx_bench.py passH2_geo.tsv --bench BENCHMARK-TX.tsv --item
  birago1572-no87 --paired benchmark-tx/txeng/units/passA_geo.tsv`: fixed > broken; (2) pooled over H and H2 (sum of fixed,
  sum of broken, two-sided exact sign test), p < 0.01; (3) the two reads' per-position agreement on the geo unit (share of
  scored positions where H == H2) reported beside pass A/B's agreement on the same lines. Adopt only if (1) holds and (2)
  clears. Also report both vs labels_geo.tsv.
- This is a read of the geo unit (f178r + f178v L05/L10/L22), not of eval_heldout: no eval_heldout look is spent.

## Report
`benchmark-tx/txeng/geo/RESULTS-B2.md`: the three gate lines, the tail positions (L03 24-34) read right/wrong in H and H2,
`tools/tx_taxonomy.py` on H2 vs A and L (after commit), reader task text, 1 call. One Results-log row in
research/TX-IDEAS-2026-10-09.md (id M2-rep; rebase before editing); update the M2 row's status to the pooled verdict. No
tool change; no shelf change unless the pooled gate passes (then `iiif_lines.py --band-extent` -> controlled-only on no.87
geo unit with the numbers). Cap 5; stop at 80% of cap or box. Report in a short paragraph (first line: H2 fixed/broken, pooled
fixed/broken/p) and stop.
