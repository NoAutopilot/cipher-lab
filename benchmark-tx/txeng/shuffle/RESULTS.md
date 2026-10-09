# TXE-L / M7 results: read the signs out of order (9 Oct 2026, 08:05 UTC by date -u)

PREREG: `benchmark-tx/txeng/shuffle/PREREG.md` (64f3c27d, pushed 08:02 UTC before any read). Ordered reads committed
cabcebd0, shuffled reads 45ff5459, both before any score. Lines f178v L08, L06, L11, L01 (the 4 dev_tune lines with the
most A/B disagreements; brief's 4-sheet cap), 115 tiles, 29 a sheet, 4 sheets per arm, 8 Opus 5.5 calls.

**Verdict: non-test at this N (registered clause), no detected effect.** Shuffled vs ordered fixed 5 / broken 2, p 0.453;
7 discordant positions, so p < 0.01 was unreachable (the smallest two-sided p at 7 is 0.0156). The two arms read 112 of 119
positions identically, and 8 of the shuffled arm's 10 errors are the same wrong sign as the ordered arm's: the errors sit in
the glyph, not in the order. Neither arm beats L, so no eval look was taken (looks so far 0).

## Gate lines (tools/tx_bench.py, --bench BENCHMARK-TX.tsv --item birago1572-no87)
```
PRIMARY  passT_shuffled_dev.tsv vs passT_ordered_dev.tsv: 115 common scored signs; base wrong 13, output wrong 10; fixed 5, broken 2; sign test p = 0.4531
ordered  err_true 0.139 (16/115) 95% 0.087-0.214 | wrong 10 deleted 3 inserted 3 | excluded 4
shuffled err_true 0.113 (13/115) 95% 0.067-0.184 | wrong 7 deleted 3 inserted 3 | excluded 4
ordered  vs labels_dev_tune (L): base wrong 5, output wrong 13; fixed 2, broken 10; p = 0.0386
ordered  vs passA_dev_tune:      base wrong 8, output wrong 13; fixed 3, broken 8;  p = 0.2266
shuffled vs labels_dev_tune (L): base wrong 5, output wrong 10; fixed 2, broken 7;  p = 0.1797
shuffled vs passA_dev_tune:      base wrong 8, output wrong 10; fixed 5, broken 7;  p = 0.7744
```
(tx_bench prints the split as "[eval]" for this item; these are dev_tune lines, not eval_heldout.)
Fallbacks to L's sign (`*/fallback.tsv`): ordered 4 '?' + 2 X_NEW, shuffled 4 '?' + 2 X_NEW, plus 4 unmapped (L11 pos 9, 10,
17, 18; op 1:2) in both arms.

## Agreed-wrong class (benchmark-tx/taxonomy/no87_positions.tsv, opened after both arms were committed)
34 positions in no.87 where A and B read the same wrong sign; 4 fall in these lines.

| position | truth | A = B = L read | ordered | shuffled |
|---|---|---|---|---|
| f178v L06.18 | d (T18/T63) | T98 | T18 right | T18 right |
| f178v L06.27 | u (T33/T49) | T76 | T15 wrong | T15 wrong |
| f178v L11.5 | e (T45/T66/T86) | T76 | T76 wrong | T76 wrong |
| f178v L11.17 | r (T83/T97) | T80 | (unmapped, L's sign) | (unmapped, L's sign) |

Each arm fixes 1 of the 3 read agreed-wrong positions, the same one. Removing the order changes none of them.

## Taxonomy (tools/tx_taxonomy.py, passes A, L, Tord, Tshuf on the 4 lines; `taxonomy.md`, `taxonomy_positions.tsv`)
Wrong-or-deleted of 115: A 8, L 5, Tord 13, Tshuf 10. Error correlation: Tshuf repeats 8/10 of Tord's errors with the same
wrong sign; Tord repeats 3/13 of L's and Tshuf 3/10. The tile arms' extra errors versus L are l <- T64/T65 (x2 each in both
arms) and three '?' tiles in L06: a single tile without its line loses what the line read had, whatever the order. Fatigue axis flat.

## Reader task text (each call; NN = 01-04, ARM = ordered | shuffled)
> You are reading cipher signs. Open ONLY these two images with the Read tool and no other file:
> - reference sheet: .../ciphers/nevers-birago-fr3251-1572/harvest/sign_sheet_blind_1572.png (cells labelled T##)
> - tile sheet: .../benchmark-tx/txeng/shuffle/ARM/sheet_NN.png (numbered tiles #n, one handwritten sign each)
> For each numbered tile, give the reference-sheet cell T## that matches, or X_NEW if the sign is on no cell, or ? if you
> cannot tell. conf = H, M or L. Write a TSV with header `tile	sign_id	conf` (one row per tile, tile as the bare number) to
> .../benchmark-tx/txeng/shuffle/ARM/reads_NN.tsv using the Write tool. Do not open, list or search any other file. Reply only "done N rows".

Calls: 8 Opus 5.5 (about 97k subagent tokens each, 13-25 s each). Tool: `tools/tx_compare.py tiles` / `tiles-resolve`
(offline test `tools/tests/test_tx_compare_tiles.py`).

## Caveats and follow-up
- The ordered arm is tiles in line order, not a line read: it carries the sequence of signs but not the line image, so it
  isolates "order" only, not all of a line's context. The larger gap is tile vs line read (both arms lose to L).
- Follow-up (one line, not run): the full 12-line subsample (about 340 tiles, 12 sheets per arm) would be needed for p < 0.01
  to be reachable if the 5:2 direction held; at 97% arm agreement a real effect, if there is one, is small.
