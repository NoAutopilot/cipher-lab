# Shadow boxes in the L74 box check (10 Oct 2026, account-3 parent)

Owner, 10 Oct 2026 about 18:1x UTC, after Birago: "Biggest observation is that the super dark blocks on the page are shadows
but are thought to be signs." Checked against his own answers (geometry and grey levels only; no value read):
`python3 benchmark-tx/txeng2/oracle1/answers/shadow/features.py` writes `features.tsv` (per box: touches the crop's left or
right edge, mean grey / page median, share of near-black pixels, spread, size) and prints the table below.

| hand | owner's answer | n | at crop edge | mean grey (min-med-max) | near-black share |
|---|---|---|---|---|---|
| Birago no.87 | trashed | 11 | 0 | 0.08-0.14-0.19 | 0.82-0.87-0.90 |
| Birago no.87 | kept | 22 | 0 | 0.69-0.77-0.86 | 0.05-0.13-0.19 |
| Birago no.87 | not asked | 310 | 0 | 0.55-0.77-0.86 | 0.05-0.11-0.33 |
| La Luzerne p.1 | trashed | 25 | 23 | 0.83-0.85-0.97 | 0 |
| La Luzerne p.1 | kept | 57 | 0 | 0.92-0.95-0.98 | 0-0-0.01 |
| La Luzerne p.1 | not asked | 363 | 6 | 0.82-0.95-0.98 | 0-0-0.03 |

All 11 Birago trashes are the last box of their line (the dark band at the page edge). Candidate rule, fitted on these 36
trashed / 79 kept answers, so NOT validated (Vivonne's answers, still to come, are the held-out check):
**A** near-black share >= 0.6 or mean grey <= 0.4, or **B** touching the crop's left/right edge and mean grey <= 0.90.
On the answers: catches 33 of 36 trashed (Birago 11/11, Luzerne 22/25; the 3 misses are not edge shadows), flags 0 of 79 kept.
On boxes the owner was not asked about it flags 6 Luzerne (p1_L03_b042-b043, p1_L04_b041-b044) and 8 Vivonne edge boxes, 3 of
which were already in Vivonne's step 2. The other 6 Luzerne and 5 Vivonne were added to those pages' step 2 (account-3 pages,
v5, question "Possible shadow ... A sign, or Trash?") so the owner sees them; nothing was trashed by rule.

Suggestion for LANE TX-ENGINEER-2 (not done here, the box builder is the lane's): after Vivonne's answers land, score rule
A/B held-out on them; if it holds, add it to the segmenter as a declared "shadow" filter that routes such boxes to the owner's
step 2 (never drops them silently), with this table as its known-answer test.

## Outcome, 11 Oct 2026 00:0x UTC (account-3 parent)
Table above is the first read; `features.tsv` is now regenerated from the second Luzerne read (31 trashed).
- **Luzerne, in-sample:** the owner trashed all 6 rule-flagged boxes he was then asked about. This is agreement on boxes the
  rule was fitted next to (same page, same edge band), not a validation. On all Luzerne answers the rule catches 28 of 31
  trashed and flags 0 of 57 kept.
- **Vivonne, held-out:** the rule flags 8 boxes (all by B, crop edge; none by A). The owner's answers: 0 trashed, 2 kept as
  signs (f102r_L03_b047 after a re-cut, f102r_L12_b057), 6 bad cut. By his own Vivonne convention a bad cut means he could not
  see around the box or it did not show the whole sign (answers/vivonne/README.md), so those 6 are undecided, not trashes.
  On the 2 decided boxes the rule is wrong both times, and he trashed nothing on the whole Vivonne page.
- **Why B does not transfer:** B's grey cap (mean <= 0.90 of the page median) separates Luzerne's pale edge strips from its
  signs (signs 0.92-0.98) but not on Vivonne, where ordinary signs sit at 0.42-0.92 (median 0.76). On Vivonne B reduces to
  "touches the crop edge". A has nothing to fire on there (near-black share at most 0.51).
- **Verdict:** rule A/B is NOT validated; held-out it is 0 of 2 on decided answers with 6 undecided. Do not add it to the
  segmenter as a filter. If the lane still wants an edge cue, it routes boxes to step 2 as a question (as done here), never
  trashes them, and a per-hand grey threshold would need its own held-out page. The 6 Vivonne bad cuts get a second look with the
  whole-page view (account-3 second-look build, in progress).
