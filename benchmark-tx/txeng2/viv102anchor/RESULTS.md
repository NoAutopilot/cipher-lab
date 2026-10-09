# DV1c: anchor checks on the f.102r stretch of the Vivonne stream (TXE2-VIV102-ANCHOR, 9 Oct 2026)

PREREG: benchmark-tx/PREREG-txeng2-15.md section DV1c. Brief row: .claude/briefs/runs/2026-10-09-account4-txe2-round15.md
TXE2-VIV102-ANCHOR. Worker: account 4, Opus 5.5, for LANE TX-ENGINEER-2 incarnation 3. Clock (date -u): 23:33-23:5x UTC 9 Oct 2026 (box to 00:18).
Read-free, scripts only. Nothing was built or edited: the frozen builders were imported, not changed (`--check` on
build_vivonne_f102r.py still reads `ok`, truth sha256 04bb775f...). Only counts, shares and per-line status tallies were printed;
no truth value, plain letter or decode of f.102r or f.103r was printed by these scripts.

Scripts (this folder): `anchor.py ctrl` (check ii/iv control, the builder's own `share()` and seed copied verbatim),
`anchor.py lines` (checks iii/iv, status column only, from the builders' in-memory rows), `j0scan.py` and `j0confirm.py`
(supplementary, POST HOC, not gating). Raw outputs: ctrl_*.json, lines.json, j0scan.json/.out, j0confirm.json/.out.

## Inputs (commit, sha256 first 16)

| file | commit | sha256 |
|---|---|---|
| benchmark-tx/build_vivonne_f102r.py | 1bd44f900 | 3ddc0c31c333a873 |
| benchmark-tx/build_vivonne_confirm2.py | 1bd44f900 | df585f0e74ead75a |
| ciphers/fr16104-vivonne-spain-1572/tx/vivk_result.json (j0 = 1265) | 1bd44f900 | e2447da60add9953 |
| ciphers/fr16104-vivonne-spain-1572/tx/dec_norm.txt | 1bd44f900 | 2d6384b1d24d5654 |
| ciphers/fr16104-vivonne-spain-1572/tx/f102r_rec.tsv | 1bd44f900 | 2cbc1f6551f0f439 |
| ciphers/fr16104-vivonne-spain-1572/tx/f102v_rec.tsv | 1bd44f900 | a3198acaf500ede6 |
| ciphers/fr16104-vivonne-spain-1572/tx/f103r_rec.tsv | 1bd44f900 | 4deb88c03997d652 |
| ciphers/fr16104-vivonne-spain-1572/key.tsv | 1bd44f900 | 7e3e758f6c6751ff |
| ciphers/fr16104-vivonne-spain-1572/key_tomokiyo.tsv | 1bd44f900 | 7dcbefed896039e9 |
| tools/stream_align.py | 1bd44f900 | d970a9f78e9ad68e |
| benchmark-tx/vivonne1573-f102r-dev.truth.tsv (not opened; .sha256 file read) | -- | 04bb775fab2ceb74 |
| benchmark-tx/vivonne1573-f103r-confirm2.truth.tsv (not opened; .sha256 file read) | -- | 5d228b454ef556fa |

HEAD at read: 6e882e553.

## (i) Anchor j0 and the f.102r bounds, by shape counts

- j0 = 1265 in dec_norm letters (N5-VIVK, anchor score 0.463), i.e. line ~24 of 26 on clerk f.105v ("92% of the way down").
  The builder's i0..i1 = stream index 0..1759 (f.102r L01 to the first token of f.102v L01; 36 lines, L14 a DUP band absent;
  1,848 raw / 1,759 collapsed signs, 0 [PLAIN] insert letters). Under the full-stream DP f.102r spans letters 400..3019 after j0.
- The DP (tools/stream_align.band_dp, band 400, free start) follows a straight diagonal from j0 to the end of dec_norm, so the
  whole stream is held to one density: 8,289 letters / 5,469 collapsed signs = 1.52 letters per sign; f.102r's own stretch
  1.49, f.102v+f.103r 1.42. The end is anchored independently (N5-VIVK: f.103r's last lines = f.108v's closing paragraph).
- Clerk opening on disk: c107_f104r_L01..L04 (s1/s2), 4 line bands only (2400 x 195-239 px) -- the head of f.104r; no shape
  count on them can reach the f.102r opening, because the clerk pages between (f.104r rest, f.104v, f.105r) are neither cropped
  nor transcribed, and the cipher pages before f.102r (f.100 lower half, f.100v, f.101r, f.101v; ~126 lines by N4-VIV's eye
  estimate) are not counted. Clerk density from the transcribed pages: 1,240-1,513 letters and 22-29 lines per page
  (ff.105v-108v, 9,670 merged letters).
- Shape estimate (inference, not measured): with ~126 cipher lines x ~49 collapsed signs before f.102r and 3 clerk pages x ~1,380
  letters + j0 before it, the letter-per-sign density before f.102r would be ~0.9 against 1.52 inside the stream; the two cannot
  both hold under a uniform density. The shape count therefore does NOT confirm j0; it cannot locate the true opening either,
  because both of its "before" counts are eye estimates of unread pages. Result (i): **not confirmed** (inconsistent density;
  unmeasured pages), and see the supplementary scan below, which measures where f.102r aligns.

## (ii) Control under shifted bounds, 200 shuffles each (seed 20261009; builder's share() verbatim)

| bounds | n (collapsed) | real | shuffled mean | p95 | max | rank /201 | margin vs max | seg. unaligned |
|---|---|---|---|---|---|---|---|---|
| base f.102r (registered) | 1759 | 0.5517 | 0.4380 | 0.5039 | 0.5490 | 1 | **0.0027** | 0.150 |
| start +1 line | 1705 | 0.5492 | 0.4383 | 0.5011 | 0.5540 | 2 | -0.0048 | 0.148 |
| end -1 line (= both -1: the stream starts at f.102r L01) | 1719 | 0.5538 | 0.4372 | 0.5043 | 0.5494 | 1 | 0.0044 | 0.154 |
| end +1 line | 1807 | 0.5784 | 0.4393 | 0.5048 | 0.5491 | 1 | **0.0293** | 0.167 |
| both +1 line | 1753 | 0.5766 | 0.4392 | 0.5039 | 0.5540 | 1 | 0.0227 | 0.165 |
| f.102r + f.102v one segment | 3524 | 0.5554 | 0.4486 | 0.5090 | 0.5422 | 1 | 0.0132 | 0.132 |

The base row reproduces the build's control exactly (0.552 vs max 0.549). Best bounds choice: end +1 line, margin 0.0293 --
under the 0.03 gate. Moving the end one line into f.102v helps (+0.027); moving the start does not; merging f.102v dilutes.

## (iii) Exclusions by line, f.102r (from the builder's status column)

Totals: 1,848 raw positions; scored 1,008; excluded:unaligned 200; excluded:align-uncertain 347; other exclusions 293.
Unaligned is spread thin: longest run of consecutive unaligned positions 5 (one line); 0 lines with >= 50% unaligned; longest
run of lines with >= 25% unaligned 1; longest run of lines with >= 50% (unaligned + align-uncertain) 1. **No unaligned run longer
than 3 lines.** Align-uncertain is concentrated, not uniform: L01 27/55, L03 21/52, L09-L12 19/50, 15/47, 16/49, 23/53, L17 21/52,
L36-L37 15/51, 16/41 -- the opening lines and an L09-L12 block carry 142 of the 347.
Per-line counts (n, scored, unaligned, align-uncertain, other): lines.json.

## (iv) f.103r as the clean control (script only; no position opened)

| bounds | n | real | mean | p95 | max | margin vs max |
|---|---|---|---|---|---|---|
| base f.103r (registered, confirm2) | 1945 | 0.6049 | 0.4264 | 0.4980 | 0.5573 | **0.0476** |
| start +1 line | 1892 | 0.6125 | 0.4275 | 0.4976 | 0.5480 | 0.0645 |
| start -1 line (f.102v last line) | 1997 | 0.6006 | 0.4263 | 0.4980 | 0.5571 | 0.0436 |

f.103r exclusions: 2,033 raw; scored 1,068; unaligned 226; align-uncertain 310; other 429. Longest unaligned position run 4
(one line); 0 lines >= 50% unaligned; longest >= 50% excluded line run 3 (L10-L12). The f.103r control stays >= 0.04 under all
three bounds: **clean**.

## Supplementary, POST HOC, not gating: where does f.102r align best?

j0scan.py aligns the f.102r collapsed stretch (same DP, band 400) to a 2,700-letter window of dec_norm starting at offset s,
s = 0..5000 step 250, published key vs 50 shuffled keys. Margin (real - shuffled max): s=0 0.141, 250 0.153, **500 0.171**,
750 0.162, 1000 0.143, **1250 0.035** (the registered j0), 1500 0.031, 1750 0.039, 2000 0.022, then 0.02-0.065 to s=5000.
Real share peaks at 0.688 (s=500) against 0.548 at s=1250; the shuffled max never exceeds 0.521 at any offset.
j0confirm.py (200 shuffles; null = each shuffled key's BEST share over all 21 offsets, a selection-fair null): at s=500 real 0.6878 vs shuffled mean 0.4270, p95 0.4939, max 0.5239, margin
0.1639; at s=1250 (j0) real 0.5484 vs max 0.5412, margin 0.0072 (the build's near-null, reproduced); best-offset null: real best
0.6878 (s=500) vs the shuffled keys' own best-over-21-offsets mean 0.4466, p95 0.5092, max 0.5412 -- margin **0.1466**, rank 1 of 201.

Reading of the scan (interpretation): the f.102r cipher matches the clerk text from roughly dec_norm 500-1000 onward (about lines
9-19 of f.105v) far better than from j0 = 1265, i.e. the registered anchor sits several hundred letters late for f.102r, and the
DP's single straight diagonal from j0 to the anchored end cannot absorb it inside band 400 at the start of the stream. That
explains the near-null f.102r control while f.103r (near the independently anchored end) is clean.

## Gate (declared in the PREREG)

ANCHORED iff some bounds choice gives control margin >= 0.03 AND no line-level unaligned run > 3 lines AND f.103r >= 0.04.
- best bounds margin 0.0293 (end +1 line) < 0.03: **fails**;
- longest unaligned run 1 line (<= 3): passes;
- f.103r control 0.0476 (0.0436-0.0645 across bounds) >= 0.04: passes.

## Proposal (not done here; a rebuild is a later PREREG)

Re-anchor f.102r rather than move its bounds: register a j0 for the f.102r stretch from a scan like j0scan.py (or a two-anchor
DP: start anchor from the scan, end anchor from f.108v), re-run the build's control at 200 shuffles, and keep the f.103r confirm2
truth unchanged unless its own control moves. The dev-pool entry stays withdrawn until then.

## Deviations and counts

- At 23:3x UTC this worker printed the whole of tx/vivk_result.json to its own transcript while looking for j0, including
  the committed fields decA_held/decB_held (N5-VIVK's Arm A/B decodes of the held-out stretch, which covers f.103r). No truth
  file was opened and nothing from those fields was used, copied or committed; declared here because the brief says never
  print a decode.
- Requests: 0 network. Model calls: 0 subagents. Token counts: this session's own; the dollar cost is the lane's get_session reading.

Openings of eval truth: 0

Verdict: measured: UNANCHORED -- no bounds choice reaches the 0.03 control margin on f.102r (base 0.0027, best 0.0293 at end +1
line; f.102r+f.102v 0.0132), unaligned positions are spread thin (no run over 1 line), and the f.103r control stays clean (0.0476);
a post-hoc offset scan puts f.102r's best alignment several hundred letters before j0 (margin 0.164 at dec_norm 500 vs 0.007 at
1250, 200 shuffles; 0.147 against a best-over-offsets null), so DV1 stays labelled ink only and a re-anchor is a later PREREG.
