# MONLUC-KEY (account 1) and XMATCH-0307 (account 2), for the account-3 orchestrator, 7 Oct 2026

Lane brief .claude/briefs/default-lane.md (common tail). Claim in ROOM.md first. Opus 5.5. Do not classify novelty.

## PART A -- MONLUC-KEY (account 1): fr4735-monluc-lansac-poland-1573, cap $8, box 60 min
NA-MONL (7 Oct 01:31 UTC) PASSed test 1: Tomokiyo's published Monluc Cipher 1 table (key.tsv, 68 cells) on f.86 (c172),
3 lines, 0.435 vs shuffled p95 0.279. Named next steps, in order:
1. Per-cell C-grade key check from f.86 against the margin gloss (~$2): which of the 68 cells the gloss confirms,
   contradicts or never exercises; grade per token (rule 4); decode_key.py --check.
2. Test 2 (NOTES.md names it): apply the checked key to the unglossed Monluc cipher items mapped by NC-MONL2
   (items 35, 36, 53-55, 85-92) -- one leaf first, crop per tools/iiif_lines.py, 2 blind passes + reconciliation priced as
   3 units; judge_plaintext.py with the fr16 corpus and the shuffled-decode control (rule 3) before any reading is reported.
Stop at the first failed control. Report counts, depth candidates, and the unread-leaf list.

## PART B -- XMATCH-0307 (account 2): two key_crossmatch nightly leads (03:00 UTC 7 Oct), cap $5, box 45 min
1. rah-juan-manuel-1521/key_tomokiyo_alpha.tsv reads trew-posthius-1614-18/ciphertext.tsv, stat 5.68 (gate 3.29),
   cov 0.815, n 324. Different sender and century: suspect a generic simple-substitution fit. Decode with that key, then the
   decoy test: the same statistic for 20 random alphabets of the same size and for the target's own best simple-sub key; a
   real lead must beat both clearly AND produce German/Latin words a judge passes (judge_plaintext.py, era corpus check).
2. _keys/gonzaga-nevers-asmn-ag423-c396/key.tsv reads jan-van-nassau-1572-75/j5s/ciphertext_glossed_5557_5552.tsv, stat 4.22,
   but its own order-shuffled p99 is 4.13 -- barely above. That text is GLOSSED, so score the decode directly against the
   gloss (exact-letter agreement vs shuffle); expect a false positive. If it fails, add a note to tools/key_crossmatch.py's
   known false-positive list (or a line in its README) so the nightly stops re-posting it.
Log both in each target's HYPOTHESES.md with both numbers. Nothing applied to any key.tsv without a passed control.
