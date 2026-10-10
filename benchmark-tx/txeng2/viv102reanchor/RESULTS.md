# DV1d: f.102r re-anchored, dev2 truth built, DV1b's passes re-scored once, insertions located (TXE2-VIV102-REANCHOR, 10 Oct 2026)

PREREG: benchmark-tx/PREREG-txeng2-16.md section DV1d. Brief row: .claude/briefs/runs/2026-10-10-account4-txe2-round16.md
TXE2-VIV102-REANCHOR. Worker: account 4, Opus 5.5, for LANE TX-ENGINEER-2 incarnation 3. Clock (date -u): 00:13-00:3x UTC
10 Oct 2026 (box to 01:28). Dev; scripts only; 0 network requests; 0 subagents / model calls.

**Openings of eval truth: 0.** Nothing of f.103r was opened (no c106 crop, nothing under outputs/vivonne1573-f103r-confirm2/
or txeng2/s2score/; vivonne1573-f103r-confirm2.truth.tsv not read). The dev2 truth was read only by scripts (the build, one
tx_bench run, decomp.py, overlap_audit.py). No existing *.truth.tsv was edited: `build_vivonne_f102r.py --check` (no --start)
still reads ok at sha256 04bb775f... (the withdrawn dev item, untouched). Disclosure, as in viv102base: tx_bench's own
"top confusions" lines print truth values beside read labels; they are in tx_bench_dev2.txt as the tool wrote them (default
--top), and were therefore seen in this worker's transcript. No other truth value or decode was printed.

## (1) Anchor scan, registered gate (scan.py; reuses viv102anchor/j0scan.py's share() unchanged)

f.102r collapsed stretch (1,759 signs) aligned by the builder's DP (tools/stream_align.band_dp, band 400) to a 2,700-letter
window of tx/dec_norm.txt at offset s = 0..2000 step 50 (41 offsets); published key vs 200 value-shuffled keys (seed 20261009).

- Real share by offset: 0.638 (s=0) rising to a plateau 0.681-0.694 over s = 300-700, then 0.666-0.630 to s=1050, a drop to
  0.541 at s=1100 and 0.515-0.553 thereafter (the registered j0 1265 lies in the low region). Full table: scan.json / scan.out.
- **s\* = 550**, real share **0.6940**.
- At s\*: 200 shuffled keys mean 0.4276, p95 0.4953, max 0.5184, rank 1/201, margin vs max **0.1756**.
- Selection-fair null (each shuffled key's best share over the same 41 offsets): mean 0.4466, p95 0.5134, max 0.5454, rank 1/201,
  **margin 0.1486 >= 0.03: ANCHORED.**
- Runtime 7 min (4 processes).

## (2) Build: vivonne1573-f102r-dev2 (build_vivonne_f102r.py --start 550)

`--start S` added: the f.102r stretch alone is aligned (same DP, band 400) to dec_norm[S : S+2700]; key forcing, exclusions,
flag rule and control unchanged; without --start the build is byte-identical to DV1 (checked). The f.102v+f.103r stretch keeps
j0's alignment (it is not part of this item).

- Positions 1,848; **scored 1,234**, excluded 614 (unaligned 253, letter-off-key 114, align-uncertain 91, key-M y 71 / S 15 /
  b 7 / A 2, off-key 61). (Old dev: 1,008 scored; align-uncertain 347 -> 91.)
- Flags at build time: align-conflict 248, clerk-split 424, any 555, **unflagged 679** (old dev 403); align-conflict among
  clerk-agreed scored 131/810.
- Build control (the builder's own, window = aligned span +/- 200): published key **0.721** vs 200 shuffled keys mean 0.427,
  p95 0.491, max 0.516, rank 1/201, **margin 0.205** (old dev 0.552 vs 0.549, margin 0.003; confirm2 0.605 vs 0.557).
- **Meet with f.102v**: f.102r's last aligned dec_norm letter (start 550) 2850; f.102v's first aligned letter under j0's
  alignment 4287: a **gap of 1,436 letters** of dec_norm covered by neither segment. Reading (inference, not tested): either
  the clerk text holds ~1,400 letters for which f.102r's re-anchored path runs short (the DP's window was 2,700 letters, the path
  used ~2,300), or j0's single straight diagonal also places f.102v's opening late; the f.103r stretch is independently
  end-anchored and DV1c found it clean. Not acted on here (f.102v is no benchmark item).
- Truth benchmark-tx/vivonne1573-f102r-dev2.truth.tsv, **sha256 007a8be9a280ff441f0da22eec66276fd36c808fe9a7ab57990e3ddaccb11714**;
  `--start 550 --check` ok. BENCHMARK-TX.tsv row `vivonne1573-f102r-dev2` (split dev, control and anchor numbers in notes),
  inserted after the dev row; the dev row left as it was.

## (3) One tx_bench run on DV1b's existing passes (no re-read)

`python3 tools/tx_bench.py outputs/vivonne1573-f102r-dev/{passZ,passA,passB}_dv1.tsv --bench BENCHMARK-TX.tsv --item
vivonne1573-f102r-dev2 --exclude-flagged --paired outputs/vivonne1573-f102r-dev2/committed.tsv` (tx_bench_dev2.txt). F48
decomposition by decomp.py (tx_bench.position_errors and score_item on the flag-dropped truth; pos_err + ins = numerator: ok
for all three).

| pass | as measured | flagged-excluded | position errors / unflagged | insertions / signs read | paired vs committed (fixed / broken, p) |
|---|---|---|---|---|---|
| passZ_dv1 (pipeline) | 0.276 (340/1234) | **0.124 (84/679)** | 43/679 = 0.063 | 41/1827 = 0.022 | 7 / 72, p 0.0000 |
| passA_dv1 | 0.287 (354/1234) | 0.143 (97/679) | 65/679 = 0.096 | 32/1813 = 0.018 | 13 / 101, p 0.0000 |
| passB_dv1 | 0.259 (319/1234) | 0.096 (65/679) | 31/679 = 0.046 | 34/1811 = 0.019 | 7 / 58, p 0.0000 |

committed.tsv against dev2: 234 wrong of 1,234 as measured (the paired base); it is the reconciled reference from which the
flags are built, so its flagged-excluded figure is 0 by construction (home advantage) and the paired lines measure distance
from the reference, not a gain. DV1b's 0.199 (80/403) was against the withdrawn dev truth and is superseded, not corrected
(Amendment 9 (11)); against dev2 the pipeline reads 0.124, and the single pass B again beats it (0.096).

## (4) Where passZ_dv1's 41 insertions sit (read-free; overlap_audit.py on dev2, decomp.py)

overlap_audit (crops symlinked under the scratchpad with the c105_ prefix dropped so the line ids match the truth; boxes and
pixel match 250 native px on all lines, ncc 0.997-0.999): indels 70 (41 ins + 29 del) -- inside 5, seam 3, outside 62,
in-or-seam 0.114 vs chance 0.128.

| line | ins | s1 | s2 | in overlap | at seam | outside | plain-word line |
|---|---|---|---|---|---|---|---|
| L01 | 1 | 1 | 0 | 1 | 0 | 0 | yes |
| L03 | 1 | 1 | 0 | 0 | 0 | 1 | |
| L05 | 1 | 0 | 1 | 0 | 1 | 0 | |
| L06 | 2 | 2 | 0 | 0 | 0 | 2 | |
| L07 | 1 | 1 | 0 | 0 | 0 | 1 | |
| L09 | 1 | 0 | 1 | 0 | 0 | 1 | |
| L10 | 2 | 2 | 0 | 0 | 0 | 2 | |
| L13 | 1 | 0 | 1 | 0 | 0 | 1 | |
| L17 | 5 | 1 | 4 | 0 | 0 | 5 | |
| L18 | 1 | 1 | 0 | 1 | 0 | 0 | |
| L22 | 1 | 1 | 0 | 0 | 0 | 1 | |
| L24 | 1 | 1 | 0 | 0 | 0 | 1 | |
| L26 | 3 | 0 | 3 | 0 | 0 | 3 | |
| L27 | 2 | 0 | 2 | 0 | 0 | 2 | |
| L28 | 1 | 0 | 1 | 0 | 0 | 1 | |
| L30 | 3 | 2 | 1 | 0 | 0 | 3 | |
| L33 | 2 | 2 | 0 | 0 | 0 | 2 | |
| L34 | 3 | 0 | 3 | 0 | 0 | 3 | yes |
| L35 | 1 | 0 | 1 | 0 | 0 | 1 | |
| L37 | 8 | 6 | 2 | 0 | 2 | 6 | yes |
| **total 41** | | **21** | **20** | 2 | 3 | 36 | 12 on 3 lines |

Classed once each: plain-word lines 12 (L37 alone 8), seam/overlap on other lines 2, elsewhere 27; 20 of 36 lines carry one.
**Reading: elsewhere dominates (27/41, spread over 17 lines, s1/s2 balanced); the plain-word lines are over-represented (3 of
36 lines, 12 of 41 insertions, L37 8) and the seam is not (5/41 in-or-seam vs 0.128 chance).** By the PREREG's mapping this
points first to a detector (TX-RED pass 10 strategy 2) with the [PLAIN:...] rule a secondary remedy for L37/L34; no crop
rule. Nothing built from it (this round).

## Commits and files

Commit **26f016500** (26f0165008ca7b3ba61eb28ffb83bd39e8790289): build option, dev2 truth + sha256, outputs, BENCHMARK-TX row,
scan, decomposition, tx_bench and overlap_audit outputs. This RESULTS.md: the following commit (named in the ROOM done line).

| file | sha256 |
|---|---|
| benchmark-tx/build_vivonne_f102r.py (with --start) | 49f01caf40ca55fd35113c3104a2169a973a479fd3b1202f984a67eaeaed0a75 |
| BENCHMARK-TX.tsv (at 26f016500) | ec49ae75b9a10a8e3654faf2bf62fd8c0db481e57dea4797bcd18c45b9afabe9 |
| benchmark-tx/vivonne1573-f102r-dev2.truth.tsv | 007a8be9a280ff441f0da22eec66276fd36c808fe9a7ab57990e3ddaccb11714 |
| outputs/vivonne1573-f102r-dev2/committed.tsv | 47604e4cba994cca05d99fe07d8d421e335092fa7b2d100bc75dde98a0abe2db |
| outputs/vivonne1573-f102r-dev2/passA.tsv | f02463fb3963a6aa0331413ff203273ff42425238f7d1b6b3b691ef7f8b86e77 |
| outputs/vivonne1573-f102r-dev2/passB.tsv | 8e16cc3c9aedebf78d494b53c0d7ecc41e44dd4f04a1ff598d89867caa635a34 |
| txeng2/viv102reanchor/scan.py | 08d91a99a270e40a6559dac3b36da1cb1a71b8bbb367965aa99e4817cb6ea91d |
| txeng2/viv102reanchor/scan.json | fcc8f9781950c82bd380909ddc7ca448f31c5f32ecce9db5ff0177826107f0dc |
| txeng2/viv102reanchor/decomp.py | 791903b026f9c66c37f18af33b6fc881d8ff2aa15cb696889742fd58cd97875d |
| txeng2/viv102reanchor/decomp.out | 8182524333148876cc2716da73b8a2e63d3ad39ef4e402a95751b35ecb9a51e3 |
| txeng2/viv102reanchor/tx_bench_dev2.txt | 8794b390ec93a74ec3e3d5aef89cce8f8b6f4b812882b0805873262224b68fb0 |
| txeng2/viv102reanchor/overlap_audit_passZ.json | a56d4b23fb1b4f4285bdec5fbdaf898c43e96213179c0fc6bbc70dd1fa90fca4 |
| inputs: txeng2/viv102anchor/j0scan.py (unchanged) | 4476e2fb5f1be4efe3b46be75c4f70783fa1291e7947a253af546475957acd5f |
| inputs: outputs/vivonne1573-f102r-dev/passZ_dv1.tsv | e5081ff031a69a7b1bcbd02995c58d81a7618030b33f9c45b39c9fed0762c4a0 |
| inputs: outputs/vivonne1573-f102r-dev/passA_dv1.tsv | 4e5f7a1024c310cade7d07987fa11bfade0e330a78e9f2bf7f94324729be6103 |
| inputs: outputs/vivonne1573-f102r-dev/passB_dv1.tsv | 0654504d5de3b8b04825899c571155b35eb410a4b8da5943b5b7b9aceccd8e69 |
| withdrawn dev truth (untouched; --check ok) | 04bb775fab2ceb74a9093508ecefdea56d0104f7e0a5104f409580dd33f19527 |

## Deviations and counts
- The 41-offset scan window is W = 2,700 letters (j0scan's), as the brief's "same DP" reuse implies; the build's truth alignment
  uses the same window at s\*. The build control's window is the aligned span +/- 200 clipped to that 2,700-letter window.
- overlap_audit needed matching line ids: a scratchpad manifest and symlinks (c105_f102r_* -> f102r_*), no image changed.
- Network 0; model calls 0; token counts: this session's own; the dollar cost is the lane's get_session reading.

Openings of eval truth: 0

Verdict: measured: ANCHORED at s* = 550 (real 0.694; margin 0.176 vs the 200 shuffled keys at s*, 0.149 vs the selection-fair
null max 0.545, gate 0.03); dev2 truth sha256 007a8be9 (1,234 scored, 679 unflagged, build control margin 0.205); DV1b's passes
against dev2: passZ_dv1 0.124 flagged-excluded (43/679 = 0.063 position + 41/1827 = 0.022 insertions), 0.276 as measured;
passA 0.143, passB 0.096; f.102r/f.102v meet leaves a 1,436-letter dec_norm gap; insertions mostly elsewhere (27/41), plain-word
lines over-represented (12/41 on 3 lines), seam at chance (5/41).
