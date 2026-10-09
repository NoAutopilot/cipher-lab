# TXE2-BASE-GUN: stopped at step (1), before any read -- the B3 relabel conflicts with the image on 4 of 6 exemplars

LANE TX-ENGINEER-2 (account 4), Opus worker; PREREG benchmark-tx/PREREG-txeng2-10.md B3; brief
.claude/briefs/runs/2026-10-09-account4-txe2-round10.md row TXE2-BASE-GUN; 9 Oct 2026 22:13-22:2x UTC by date -u.

No sheet_v2, no reader brief, no pass, no reconcile, no adjudication, no score. No p.2 row, truth, decode, old pass or
passZ_pipeline.tsv opened. Nothing in benchmark-tx/txpool/ was changed.

Openings of eval truth: 0

## Why stopped
The sheet is value-blind: `blind_pass_brief_p2.md` tells readers to use `calibration.tsv` "only to learn which shape each
label names. It is not a key and says nothing about meaning." B3 relabels the 6 exemplars to the *letter* the p.1 print
gives through the key (d6 -> c x2, Ib -> s, 34 -> e, xb -> a, ps -> f). A sheet label has to be a shape label, so "-> c"
can only mean a shape whose key value is c (key.tsv: c = `a`, `xr`; s = `]`, `L`, `aaa`; e = `f`, `r`, `g`, `85`, `ss`;
a = `01`, `ii`, `x`, `x+`; f = `p`, `x+x`). Read literally, `c` is itself a shape label whose key value is n.
I enlarged each exemplar from the committed sheet crops (2-3x, scratch only) and compared it with the shape definitions in
the reader brief:

| tile | label now | print -> key-consistent labels | what the image shows | relabel that fits both image and key |
|---|---|---|---|---|
| p1cal_L03.16 | d6 | c -> a / xr | a clear d6 (bowl at the bottom, stem curving over to the right) | none: the shape is d6 |
| p1cal_L06.14 | d6 | c -> a / xr | a clear d6, same shape as L03.16 | none: the shape is d6 |
| p1cal_L05.14 | Ib | s -> ] / L / aaa | a clear Ib (I with cross-bars), same shape as L03.10 (aligned o) | none: the shape is Ib |
| p1cal_L06.17 | 34 | e -> f / r / g / 85 / ss | a clear "34" (an interlinear "a" is written above it) | none: the shape is 34 |
| p1cal_L08.15 | xb | a -> x | a plain x, no bar above (compare the x_ at L03.17) | **x** (shape and key agree) |
| p1cal_L09.14 | ps | f -> p | a p with a loop and no s joined (compare the ps at L08.19) | **p** (shape and key agree) |

So 2 of the 6 are shape mislabels by the earlier reader, and the relabel to x and p fits both the image and the key. In the
other 4 the shape label is right, and the disagreement is between the key and the print alignment (a key gap or homophone
d6 = c / Ib = s; an alignment or encipherment question at 34 = e). This matches GS1's own note that d6 = c and Ib = s are
the label-level patterns the build already flagged as `align-conflict` on p.2. Following B3 as written would put the
names of other shapes on 4 tiles. That would teach readers wrong shapes on p.2's d6/Ib/34 signs (the treatment would add
errors, not fix them), and to use any eval opening on it would waste it.

Rule applied: the brief's step order (sheet fix committed before any read) and "a worker never extends its own brief".
Choosing a different treatment from the pre-registered one (the 2-relabel sheet) would mean changing a pre-registered
treatment after the fact, and that call belongs to the lane (Amendment 9), not to this worker.

## Options for the lane (one line each)
- (a) Amend B3 to the 2 image-consistent relabels (xb -> x at L08.15, ps -> p at L09.14) and leave d6/Ib/34 as drawn. Re-brief
  the same job at the same cap; the reads, reconcile, adjudication and one score are unchanged.
- (b) As (a), and also mark the 4 key-vs-print tiles in the sheet as "shape correct, value disputed". Readers never see
  values, so this changes nothing a reader sees; it only matters to the record (GS1's cross.tsv).
- (c) Drop B3 this round. Leave the gunther baseline at its current figure, and file the d6/Ib/34 conflicts as a key
  question for the gunther target (ciphers/gunther-van-schwarzburg-1561), not a transcription one.

## Inputs read (sha256)
| file | sha256 |
|---|---|
| benchmark-tx/txpool/gunther8246-p2/sheet/calibration.tsv | 01abf56bebd3c7809b16ed3a0b8e021392b283eee188623cb5bf552590cd54b9 |
| sheet/p1cal_L03.jpg | d64426219e3849417dd585869cdd4f02cf736f36ae565739e5c38670ccb5e00a |
| sheet/p1cal_L05.jpg | 6ca8ff01c06dcb1cd00c1cdb672b6865df415a73e40a8b213f68d134c37e9b0f |
| sheet/p1cal_L06.jpg | edc5fe2d30675759e97cd1eed357209b91e10ac09fc4745d8049d9559c934b41 |
| sheet/p1cal_L08.jpg | 0d2db00197f13ad92b33b33aa1679c1431dcac22fecc679b54670b12d9d44d54 |
| sheet/p1cal_L09.jpg | f79ab57f98cb9997249756158c998cdc71cfd10225300c6826403fc8337c5437 |

Also read: benchmark-tx/txeng2/gunsheet/RESULTS.md and cross.tsv; benchmark-tx/txpool/gunther8246-p2/blind_pass_brief_p2.md;
ciphers/gunther-van-schwarzburg-1561/key.tsv (p.1 is outside the scored p.2).
Calls: 0 subagents, 0 host requests. Cost: the orchestrator's get_session reading.
