# TXE4-1 VIV-HAND results: the Saint-Gouard alphabet as words, as the key drawing, or as the drawing plus machine-cut strokes

Account 3, Fable 5.1 worker (session_01GcMxkniJHMYkrLFu9JrsMf), Sonnet (claude-sonnet-5) readers; 12 Oct 2026, 01:18-01:5x UTC by
`date -u`. Binding: benchmark-tx/PREREG-txeng4-1.md (pushed f3845355b at 01:29 UTC, before any read or score; addendum c69699828
before any sheet). Brief: .claude/briefs/runs/2026-10-11-acct3-txe4-1.md (93b7bb321). **Dev only** (vivonne1573-f102r-dev2, the
13 TXE3-6 test lines, 417 scored as measured / 216 flagged-excluded); no eval unit opened, no LOOKS.tsv row owed. Truth opened only
by tools/tx_bench.py (one scoring call per pass, two paired calls, three context calls on the committed Opus passes; by script,
never by eye). Hosts: 0 requests. Nothing published, nobody contacted. Cost: see the lane ledger (the parent's get_session).

## Verdict in one line
**H and Hx: declared non-test** ('f.102v tiles not separable, or not verifiably placed, at pen units': the purity gate failed on
two of its three parts). **W vs D: not distinguishable from pass spread** on both masks: the word list read 6.5 edits better
than the drawn sheet as measured and 7.5 better flagged-excluded, against a within-arm spread of 15 and 13.

## What was run (4 of the 8 registered passes; the registered order D, H, W, Hx with H and Hx removed)
| pass | alphabet form | err_true as measured (417; Wilson 95%) | unit-cost edits (S / D / I) | err_true flagged-excluded (216; Wilson 95%) | edits (S / D / I) | strict as measured / flagged-excl. |
|---|---|---|---|---|---|---|
| D1 | drawn key sheet (sheet_tomokiyo_v1.png) | 0.269 (112/417) 0.228-0.313 | 112 (94 / 9 / 9) | 0.102 (22/216) 0.068-0.149 | 22 (10 / 3 / 9) | 0.122 / 0.102 |
| D2 | drawn key sheet | 0.305 (127/417) 0.262-0.350 | 127 (94 / 14 / 19) | 0.162 (35/216) 0.119-0.217 | 35 (11 / 5 / 19) | 0.168 / 0.162 |
| W1 | words (sheet_SIGNS_dv1.md) | 0.283 (118/417) 0.240-0.326 (standard SER 0.281, 117) | 117 (103 / 10 / 4) | 0.111 (24/216) 0.072-0.155 (standard SER 0.106, 23) | 23 (16 / 3 / 4) | 0.117 / 0.106 |
| W2 | words | 0.261 (109/417) 0.222-0.306 | 109 (96 / 9 / 4) | 0.088 (19/216) 0.057-0.133 | 19 (12 / 3 / 4) | 0.144 / 0.088 |
| H, Hx | drawing + machine-cut tiles (plain / deranged) | not run (gate failed) | -- | not run | -- | -- |

The line bootstraps (1,000 resamples) are in scores/<pass>.txt. "Unit-cost edits" is tx_bench's standard SER numerator (the figure
TXE3-8 and SHEET-VIV report); where the 0.75-indel err_true numerator differs (W1: 118 vs 117, 24 vs 23) both are given and the
verdict is the same under either.

## Endpoint and gate, applied word for word (PREREG 'Declared readings by passes done': 4 passes, H and Hx non-test, so "W and D
reported against each other with the same spread rule")
| arm | passes | mean edits as measured | within-arm spread | mean edits flagged-excluded | within-arm spread |
|---|---|---|---|---|---|
| D (drawing) | 112, 127 | **119.5** | 15 | 22, 35 -> **28.5** | 13 |
| W (words) | 117, 109 | **113.0** | 8 | 23, 19 -> **21.0** | 4 |
| maximum within-arm spread | | | **15** | | **13** |

- G-DEFAULT needs mean(W) >= 1.25 x mean(H) as measured AND mean(W) > mean(H) flagged-excluded AND the gap above the maximum
  within-arm spread: **not applicable, H did not run**. Against D in H's place (the only pictured arm that ran): mean(W) / mean(D)
  = 113.0 / 119.5 = **0.95** as measured (the words read slightly *better*), mean(W) < mean(D) flagged-excluded (21.0 vs 28.5), and
  both gaps (6.5, 7.5) are **under** the maximum within-arm spread (15, 13). **'Not distinguishable from pass spread'** on both masks.
- G-HAND (D vs H, Hx vs H): **not applicable, H and Hx did not run** (non-test).

Beside the gate (paired per-line calls, W against D as the base, same round):
| round, mask | unit-cost edits | lines improved / worsened / tied (W vs D), sign test | position McNemar W vs D | paired line bootstrap of the SER difference, 95% |
|---|---|---|---|---|
| 1, as measured | D 112 -> W 117 / 417 | 3 / 6 / 4, p 0.5078 | fixed 9 / broken 17, p 0.1686 | -0.020..0.039 |
| 1, flagged excluded | D 22 -> W 23 / 216 | 5 / 5 / 3, p 1.0000 | fixed 7 / broken 11, p 0.4807 | -0.050..0.052 |
| 2, as measured | D 127 -> W 109 / 417 | 7 / 4 / 2, p 0.5488 | fixed 21 / broken 18, p 0.7493 | -0.112..0.007 |
| 2, flagged excluded | D 35 -> W 19 / 216 | 4 / 2 / 7, p 0.6875 | fixed 11 / broken 10, p 1.0000 | -0.189..0.005 |

Per-arm reader agreement (reconcile_passes --method nw, rec_D/ and rec_W/): D1 vs D2 584 / 670 aligned columns = **87.2%**; W1 vs
W2 545 / 656 = **83.1%**. Edits on tokens with hand tiles against tokens without: not computed, no reader saw a hand tile.
Context (never a baseline arm): the committed Opus SHEET-VIV passes rescored on the same 13 lines read 101 / 104 / 106 edits as
measured (A / B / Z) and 13 / 16 / 18 flagged-excluded (scores/context_pass*_sv.txt) -- the Sonnet drawn-sheet passes here read
about 10-20 edits worse than Opus on the same sheet. Cross-session: TXE4-8's arm N (the same configuration as D) had no committed
pass at the time of writing (benchmark-tx/txeng4/8/reads/ holds O1 and R1 only), so nothing is quoted beside D.

## The tile pipeline (read-free; PREREG addendum has every number; maps/, tokens.tsv, sheets/)
The hand joins its signs: pen-unit segmentation of the 74 f.102v crops gave 1,661 boxes against 1,819 pass-A tokens, and the
registered count tolerance (10%) passed only 5 of 37 lines. On those, the width-only seed round gave 159 tokens; the round-2 kNN
(leave-itself-out, trained on those 159) and the label-aware re-map gave 95 one-to-one tokens; the steered join check (R4a,
join_check --steered) **FAILed** on L34 (B1), and **PASSed** on the four remaining lines after the one allowed drop (n 106, share
at 0 0.236 against a permuted-label p95 of 0.105; share at +-1 0.160 under the 0.226 bound). Tiles kept (1:1 in both rounds at an
agree position, code in the 40): **24 tiles on 13 of the 40 tokens, 7 tokens with two or more**. Purity gate: (i) 1:1 share 92 / 197
= 0.467 (needs 0.80) FAIL; (ii) 7 of 40 (needs 25) FAIL; (iii) PASS. The H and Hx sheets in sheets/ were built after the gate
with the patched tool, for the record only (README there); no reader saw them.

Tools (both as patches with offline tests, R7: TXE4-0 touched tools/box_token_align.py at 00:59 and a ROOM push touched
tools/glyph_atlas.py at 00:37, both inside the hour): `box_token_align.patch` (--keep-pos, --tokens-out, --count-tol;
test_box_token_align_patch.py: a planted merged box, a disagreement position and an over-counted line all excluded, 14 tokens
kept) and `glyph_atlas.patch` (--from-tokens, --canonical-boxes/--canonical-dir, --shuffle-rows; test_glyph_atlas_patch.py: the
canonical cut equals the box, --from-tokens is byte-identical to --from-truth, the derangement has no fixed row and is seed-stable).
A parent can apply either to the shared tool with `patch -p1 < benchmark-tx/txeng4/1/<tool>.patch` and move the test into
tools/tests/.

## Blindness and access (access_log.tsv, access_log.summary, usage.txt)
Four Sonnet subagents, one per pass, fresh contexts, each confined to its scratch directory (task.txt, the arm's sheet copy, the 26
crops): 119 of 123 tool calls inside the allowlist; the 4 'OUTSIDE' rows are W1 and W2 each writing a 25-line helper script
(gen.py / gen_w2.py, inline rows, no file read) in its own directory and running it to write read.tsv -- a write in its own
directory, not a read of anything else. One call per pass held all 26 crops (no 7/6 split was needed). Token usage per pass
(usage.txt, output tokens a lower bound): input 0.56-0.93 M (cache reads included), 5-8 API calls each.

## Three sentences for the owner
1. On the 13 known-answer lines of the Saint-Gouard hand, a Sonnet reader given its alphabet as words read about as well as one
   given the drawn key sheet: 113 against 119.5 unit-cost edits of 417 as measured, 21 against 28.5 of 216 flagged-excluded, with the
   words slightly ahead and the gap smaller than the two drawn-sheet passes' own spread (15 and 13) -- no form reads this hand best.
2. The sheet cut automatically from the clerk's own strokes could not be built to the registered standard: this clerk joins his
   signs, only 4 of 37 lines of the sibling page gave verifiably placed tiles, and 24 tiles on 13 of the 40 signs reached the sheet
   (the gate asked for 25 signs with two tiles each) -- whether his strokes help is untested, not negative.
3. The automatically cut sheet should not be the default for the Saint-Gouard letters on this evidence, and the three published
   readings do not earn a pictured re-read from it: a Sonnet re-read of ink 53's weakest lines would cost about USD 12, and the only
   number that ever favoured a picture on this hand is the Opus SHEET-VIV run (58 vs 86 flagged-excluded, line sign test p 0.26).

## Next step (not run)
Neither gate passed, so neither of the brief's named next steps opens. What would move it: (a) tiles at sign units rather than pen
units, since the joins are what starved the gate -- rerun tiles.py with TXE3-6's `--split-wide 1.5 --split-piece 0.85` on the
same f.102v passes and re-apply the registered purity gate, read-free, about USD 4; if the gate then passes, the H and Hx arms
as registered (4 Sonnet passes, about USD 3 plus the Fable floor); (b) the W-vs-D question itself needs two more passes per arm
(about USD 2.5) before a 6.5-edit gap could clear a spread of 15. A sign-unit control on no.87 read no better than random cuts
(TXE3-6), so (a) is a tile-supply fix, not a reading claim.
