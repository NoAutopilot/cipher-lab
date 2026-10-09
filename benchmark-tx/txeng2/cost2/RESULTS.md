# TXE2-COST2 (PREREG benchmark-tx/PREREG-txeng2-4.md X8b): cost replication, 2 readers x 2 hands

LANE TX-ENGINEER-2, account 4, worker TXE2-COST2 (Opus 5.5), 9 Oct 2026 17:48-17:5x UTC by date -u. This is a measurement (S5) with
no gate. No eval item was looked at, no truth file was edited, and no hosts were contacted.
Nearest prior: X8 / TXE2-COST (`../cost/RESULTS.md`). There, one per-page native call (arm b) beat four per-line 2x calls (arm a)
on dint-f128-print (0.235 vs 0.318 err_true, at 0.30x the input tokens), with N=1 reader per arm.

## Protocol (as run)
- **Readers.** 11 Opus subagent calls, all launched at once, all blind. Each call saw its own scratch folder: a TASK.md (the
  wrapper plus the brief, committed beforehand as `prompts/*.md`), copies of its crops, and the sign sheet for Ceppo. No path
  into the repository was in view. Briefs, prompts and the crop script were committed before any read (86875978c). The 11 reads
  were committed verbatim in `reads/` (4051bc38b). The converted outputs (a275e3815) were committed before `tx_bench` scored them
  (`score.txt`).
- **dint-f128-print, second reader per arm.** This used X8's own briefs (`../cost/brief_arm_a.md`, `brief_arm_b.md`) unchanged:
  - Arm a2: 4 calls, one per line, on the 2x q1-q4 pieces re-rendered by `../cost/regen_crops.sh`'s command.
  - Arm b2: 1 call on the 8 native crops.
  - Both were converted with `../cost/convert.py` and scored with `--label-map benchmark-tx/dint128_label_map.tsv`.
- **ceppo-f87-S, both arms (the second hand).** The brief is `harvest/blind_pass_brief.md` plus the sign sheet, with TX-FABLE's
  per-line layout text.
  - Arm a (`brief87_arm_a.md`): 5 calls, one per line. The brief is unchanged apart from a title note. The crops are the item's
    standard `f87/lines2x` set: tracked and sheared, 2x, 3-4 gap-cut segments per line with no overlap. They were re-cut by
    `harvest/cut_folio_lines.py`.
  - Arm b (`brief87_arm_b.md`): 1 call. The crop sentence was rewritten to "native scale, two segments". The 10 crops come from
    `make_native87.py`: the same tracked, sheared bands at 1x, with 2 segments per line cut at the ink minimum nearest mid-line.
  - Ceppo runs were converted by `convert87.py` (`build_ceppo.write_out`'s rule, with prose-split runs joined per line; no reader
    split any line).
- **Token counts** come from each subagent transcript (`usage.py`, written to `usage_raw.txt`), deduplicated by API message id.
  Input counts are exact. Output counts are only a lower bound: the transcript logs partial streamed counts per content block,
  and the file-writing turn's final count is often missing. The harness's own `subagent_tokens` figure is given beside them.

## Disclosed deviations (found after the reads, before scoring)
1. **The ceppo arm b reader left the native-only condition.** It made its own 2x and 3x enlargements of the native crops
   (`c87_up/` in scratch) and read from them. That is why it took 17 API turns and 1.99M input tokens. Its error and cost are
   therefore for "native crops, reader upscales itself", not pure native. It is kept as written, not re-run (it was the only
   call).
2. **The dint arm a2 L04 reader did the same.** It wrote 7 temporary zooms and then deleted them (9 turns against 5 for the
   other lines).
3. **The dint arm b2 reader reported heavy s1/s2 overlap** ("each s2 repeats a large stretch of s1"). These are the same native
   crops X8's arm b used.

The briefs did not forbid tool-made zooms; they forbade only extra output files. A future arm that means "native" has to say "do
not resize".

## Error (err_true)
| item | arm | reader | err_true | 95% CI | wrong / del / ins | paired vs best single pass (fixed / broken, p) |
|---|---|---|---|---|---|---|
| dint-f128-print (85) | a per-line 2x | 1 (X8) | 0.318 (27) | 0.228-0.423 | 17 / 1 / 9 | vs pass B: 3 / 10, p 0.092 |
| | a per-line 2x | 2 | 0.388 (33) | 0.292-0.494 | 18 / 1 / 14 | vs pass B: 4 / 12, p 0.077 |
| | b per-page native | 1 (X8) | 0.235 (20) | 0.158-0.336 | 16 / 0 / 4 | vs pass B: 5 / 10, p 0.302 |
| | b per-page native | 2 | 0.318 (27) | 0.228-0.423 | 17 / 1 / 9 | vs pass B: 3 / 10, p 0.092 |
| | pass B (Sonnet, best single) | -- | 0.188 (16) | 0.119-0.284 | 11 / 0 / 5 | -- |
| ceppo-f87-S (139) | a per-line 2x | 1 | 0.166 (23) | 0.113-0.236 | 20 / 0 / 3 | vs pass A: 4 / 20, p 0.0015 |
| | b per-page native* | 1 | 0.122 (17) | 0.078-0.187 | 16 / 0 / 1 | vs pass A: 4 / 16, p 0.012 |
| | pass A (Sonnet, best single) | -- | 0.043 (6) | 0.020-0.091 | 3 / 1 / 2 | -- |
| | pass B (Sonnet) | -- | 0.130 (18) | 0.084-0.195 | 8 / 0 / 10 | vs pass A: 4 / 8, p 0.39 |

\* The arm b reader upscaled the crops itself (deviation 1).

Pooled per arm on dint (2 readers): a 60/170 = 0.353, b 47/170 = 0.276.

Direct arm b vs arm a, same reader index:
| item | reader | arm a wrong | arm b wrong | b fixes / b breaks | p |
|---|---|---|---|---|---|
| dint | 1 | 18 | 16 | 5 / 3 | 0.73 |
| dint | 2 | 19 | 18 | 6 / 5 | 1.0 |
| ceppo | 1 | 20 | 16 | 9 / 5 | 0.42 |

In all three pairs arm b has fewer errors than arm a. None of the differences is significant.

**Caveat on ceppo.** The ceppo-f87 truth was adjudicated from passes A and B; 29 of the splits sided with A (TX-FABLE). So "pass A
best" leans to A by construction, and both Opus arms lose to it decisively. Against pass B, which is less favoured by the truth's
construction, the Opus arms are at 0.166 and 0.122 vs 0.130.

Both Opus page-level readers on dint (0.235, 0.318) are worse than Sonnet pass B (0.188). Reader-to-reader spread within one arm
is as large as the arm effect: 0.235 vs 0.318 for b, 0.318 vs 0.388 for a.

## Cost proxy (subagent transcripts)
| item | arm | reader | calls | API turns | input tokens (all) | of which cache write | output (lower bound) | harness subagent_tokens | input per 100 ref signs |
|---|---|---|---|---|---|---|---|---|---|
| dint (183 ref) | a | 1 (X8) | 4 | 20 | 2,005,851 | 287,833 | 13,450 | 441,040 | 1,096k |
| | a | 2 | 4 | 24 | 2,501,132 | 458,949 | >= 3,450 | 461,331 | 1,367k |
| | b | 1 (X8) | 1 | 6 | 608,122 | 77,146 | 10,233 | 115,711 | 332k |
| | b | 2 | 1 | 7 | 723,405 | 116,047 | >= 313 | 116,678 | 395k |
| ceppo (204 ref) | a | 1 | 5 | 20 | 1,990,528 | 522,064 | >= 3,501 | 524,366 | 976k |
| | b* | 1 | 1 | 17 | 1,990,069 | 144,505 | >= 3,595 | 145,488 | 976k |

- **Input ratio, arm a / arm b.** dint reader 1 is 3.3x and reader 2 is 3.5x. On ceppo it is 1.00x, because the arm b reader's
  self-upscaling took it to 17 turns, each re-reading a growing context.
- **Cache writes**, which carry the images and fixed context once per call, still scale with the call count: ceppo a is 3.6x b,
  and dint a2 is 4.0x b2.
- **Harness subagent_tokens** follow the same pattern: per-line runs about 4-5x the per-page call on both items.

No conversion to dollars is made here. The orchestrator's get_session reading for this worker gives the dollar side.

## Verdict (measurement, no gate)
- **Error.** With N=2 readers on dint and a second hand on ceppo, the per-page call has fewer errors than the per-line 2x calls
  in all 3 same-reader pairs. Each difference is small (p 0.42-1.0), and it is the same size as the spread between two readers
  in one arm.
- **Cost.** The X8 finding replicates on dint: one page call costs 0.29-0.30x the input tokens of the per-line calls.
- **Cost on ceppo.** One reader's choice to upscale for itself erased the input-token saving there, though it did not erase the
  cache-write saving. The cost advantage of a page call holds only when the reader does not zoom on its own.
- **Against the best single Sonnet pass.** No Opus arm beats it on either item: dint pass B 0.188, ceppo pass A 0.043 (A-leaning
  truth).
- **S5 figure.** Prefer one page call. Expect about 0.3x the input tokens of per-line calls, not better accuracy than a good
  single pass. A reader that upscales for itself costs about as much as per-line calls.

Suggestion (not run, Usage 7): a native arm that forbids tool-made zooms, and a reader-variance arm (2 readers, same arm, same
crops) to put a size on the reader term separately.
