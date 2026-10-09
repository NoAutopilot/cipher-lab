# TXE2-COST (PREREG benchmark-tx/PREREG-txeng2-3.md X8): cost at equal error on dint-f128-print

LANE TX-ENGINEER-2, account 4, worker TXE2-COST (Opus), 9 Oct 2026 17:1x-17:2x UTC by date -u. Measurement only, no gate.

## Protocol (as run)
- Item dint-f128-print (dev; 85 scored positions, 4 lines, 183 reference signs). Truth file untouched.
- Readers: Opus subagents, blind. Each saw the brief (`brief_arm_a.md` / `brief_arm_b.md` = `f128/pass_instructions.md`, its crop
  paragraph rewritten for the arm; same vocabulary and output format as pass A/B) plus its image files, copied to a scratch directory
  so no repository path was in view. They were told to read no other file.
- Arm a: one call per LINE (4 calls). The 8 native crops rendered at 2x by `tools/tx_prep.py lines --setting sr2 --segments 4
  --max-w 1500 --overlap 150` (`regen_crops.sh`; 32 PNG of 1313x332, not committed, ~16 MB), the 8 pieces of that line per call.
- Arm b: one call for the whole page: the 8 native crops (2400 px wide) in one call, as pass A/B.
- Reads are committed verbatim in `reads/` (c25f572c5, dab120089). They were converted to the tx_bench format by `convert.py` (PREREG-dint128's rule:
  non-CLEAR rows' signs per line, '-' dropped; a `NEW:<desc>` whose description has a parenthesis with spaces in it stays as one sign,
  a parse fix committed before scoring). Scored after the commit with `tools/tx_bench.py --item dint-f128-print --label-map
  benchmark-tx/dint128_label_map.tsv --paired outputs/dint-f128-print/passB.tsv` (`score.txt`).

## Error (85 scored positions, label-mapped)
| arm | err_true | 95% CI | wrong / del / ins | paired vs pass B (fixed / broken, p) |
|---|---|---|---|---|
| a per-line, 2x (4 calls) | 0.318 (27/85) | 0.228-0.423 | 17 / 1 / 9 | 3 / 10, p 0.092 |
| b per-page, native (1 call) | 0.235 (20/85) | 0.158-0.336 | 16 / 0 / 4 | 5 / 10, p 0.302 |
| pass A (Sonnet, 3 Oct, reference) | 0.247 (21/85) | 0.168-0.348 | 12 / 2 / 7 | 1 / 4, p 0.375 |
| pass B (Sonnet, 3 Oct, base) | 0.188 (16/85) | 0.119-0.284 | 11 / 0 / 5 | -- |

The two arms are not at equal error. The per-line 2x arm is the worse of the two: it has 9 insertions, against 4 for the page arm.
That is consistent with the 4-way segmenting, which creates 6 more overlap seams per line for the reader to de-duplicate, and with
reading the z-tailed m as Z (m<-Z x3). The CIs overlap, and neither arm differs from pass B at p < 0.05. One reader per arm means N=1
per arm: reader variance is not separated from arm effect. Arm a's L04 reader wrote `÷` for the instructions' `-:-`. It is kept as
written; it falls on an excluded position and does not change the score. No read-time tuning was done.

## Cost proxy: subagent-reported tokens (from each subagent transcript's per-turn `usage`, `usage_raw.txt`)
| arm | API turns | input tokens (uncached + cache write + cache read) | of which cache write (incl. images) | output tokens | per 100 reference signs: input / output |
|---|---|---|---|---|---|
| a (4 calls) | 20 | 2,005,851 (40 + 287,833 + 1,717,978) | 287,833 | 13,450 | 1,096k / 7.4k |
| b (1 call) | 6 | 608,122 (12 + 77,146 + 530,964) | 77,146 | 10,233 | 332k / 5.6k |

The harness's per-agent `subagent_tokens` figures were: a 105,240 + 115,411 + 108,197 + 112,192 = 441,040; b 115,711.
Arm a costs about 3.3x arm b in input tokens, 3.7x in cache writes and 1.3x in output tokens, and it reads at higher error (0.318 vs 0.235).
Per 100 signs at the arm's own error, arm b dominates: it is cheaper and more accurate. Most of each call's input is the subagent's own
fixed context, re-read on every turn (cache read). A per-line split pays that fixed context once per call, so its cost grows with the
call count, not the sign count.

Beside TRANSCRIPTION.md target 8's first figures: HARVEST-D2 was about USD 6.6 per 100 signs (Fable, job-level, including decode).
A2-DIN was about USD 2.7 per 100 signs (f.128r itself, two Sonnet passes + reconcile, job-level). Those are dollar figures and these
are token counts. The orchestrator's get_session reading for this worker gives the dollar side; this file does not convert tokens to
dollars at a guessed rate.

## Verdict
Measurement, no gate (S5). On this item, one per-page native call beats four per-line 2x calls on both axes: 0.235 vs 0.318 err_true,
at about 30% of the input tokens. The 2x segmentation's extra seams cost insertions. Suggestion (not run, CLAUDE.md Usage 7): if
scale is to be retested, render at 2x with no extra segmenting (the two s1/s2 halves only) in one per-page call, which separates scale
from the seam count.
