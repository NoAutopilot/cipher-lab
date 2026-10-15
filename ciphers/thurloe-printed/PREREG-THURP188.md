# PREREG-THURP188 -- P4 (Stamford, Calais, 13 March 1655), Birch III p.188 lines 53-61

Written 15 Oct 2026 (13:29 UTC by date -u), worker THUR-P188, **before any scoring** of the hypotheses below.
Brief: `.claude/briefs/runs/2026-10-15-acct4-depth-steps.md`, JOB THUR-P188.

## Material
- Block under test: printed p.188 lines 53-61, 144 numerals (lines 50-61 carry 198; lines 50-52, 54 numerals, read coherently
  already and are an in-page reference, not part of the 144).
- Transcription: `P4/image_transcription.tsv` (worker I, 24 Sept 2026), re-read blind this pass by two Sonnet readers on line
  crops cut with `tools/iiif_lines.py` (`P4/p188/readA.tsv`, `readB.tsv`); reconciliation by this worker against the crops.
  The two blind reads and the committed transcription already agree on every numeral of lines 50-61 (198/198); the only
  differences are long-s spellings (thoufand/thouland, affured/assured) and two printed commas ("40," "18,"). This was
  checked before this file was written (it is a transcription fact, not a hypothesis score).
- Key: `pool_1654/key_stamford.tsv` as committed (P4's key, rebuilt from P5+P6 and P7), **no edit**. Multi-letter values
  (67 england, 81 which, 85 have, 158 designs, 130 general rising ...) decode to their full meaning.

## Statistic (fixed here)
`read share` = fraction of the block's 144 numerals that read as ordinary text: decode each numeral run (maximal sequence of
numerals not interrupted by a clear word; a clear word ends a run and is not decoded) with the key; concatenate the run's
letters; segment greedily by longest word from a word list; a numeral **reads** when every one of its letters falls inside a
segmented word of **3 or more letters** (or a multi-letter key value that is itself a word). A numeral whose value is not in the
key never reads. Word list: `tools/judge_plaintext.py`'s NgramModel word set (words seen >= 2 times) built from
`tools/data/en16_repo/` **minus** `thurloe-printed__reading_P4.txt` (circular) -- 16 decoded Thurloe-printed letters,
17th-century English official correspondence, era and register matched. No `specs/` judge spec exists for P4 (the brief's
"P4 spec"); the judge's own NgramModel is used directly with that corpus, and the 4-gram score of the best variant is reported
beside the share for information only (not gated).

## References (computed with the same statistic)
- SIB: the siblings' own share -- P5+P6 and P7 numerals (`pool_1654/tokens.tsv`, runs rebuilt from prev_word), same key.
- P4-50-52: lines 50-52 of the same page (54 numerals).

## Nulls (200 each, seed 1)
- N-line: shuffle the order of lines 53-61 (each line moves with its clear words), statistic recomputed.
- N-bound: within each run, concatenate the digits and re-cut them at random into the same number of groups (each 1-3 digits),
  statistic recomputed.

## Hypotheses, in order
(a) **Tokenisation**: the djvu/print split or joined digit groups. Test: the reconciled image read vs the committed
    transcription. Because they agree on every group, (a) for *our* tokenisation is settled by the comparison itself (no
    variant to score). Exploratory only, not gated: the count of adjacent pairs whose join is a key value and of numerals that
    split into two key values.
(b) **Compositor line transposition**: each of the 9 adjacent-line swaps touching the block ((52,53) ... (60,61)); report each
    share; the best is gated against N-line p95.
(c) **'am.' are set signs for a key value**: the 7 'am'/'am.' tokens in lines 54-61 are replaced together by one key value v
    (each of the 59 values in turn; the 'am' then joins the runs either side); best v gated against N-bound p95 **and** against
    the same 59-value search run on 200 line-shuffled texts (max-of-59 null). Also logged: how often 'am' stands inside a
    numeral run in the siblings' print (AUDIT says never).

## Gate (per hypothesis)
PASS = the variant's read share > the relevant null's p95 **and** >= SIB - 0.10 (at or near the siblings' own share).
Baseline (the block as printed, no hypothesis) is reported with the same two nulls. Any PASS -> report the block's reading
graded per token with the one hypothesis that did it; otherwise log all three as tested with numbers. No key edit either way.

## Amendment 1 (15 Oct 2026, written after the first scoring run; declared, not hidden)
The first run (`P4/p188/results_run1.tsv`) failed its own sanity reference. The en16_repo word list has only **180 words**
of 3+ letters, because those readings are mostly brace-joined runs ("{peopleareengaged}"), so even the siblings read at
**0.112** and P4 lines 50-52, which read coherently, at 0.37. A statistic that cannot read the siblings is a non-test, and run 1
is logged as one. The hypothesis numbers from run 1 had been printed when this amendment was written. The change is driven
by the reference failing, not by any target number. Changes:
1. Word list: words seen >= 2 times with 3+ letters in `tools/data/en18/` (6 files) plus `LANG_CORPORA["en"]` (Holmes,
   Moby-Dick). These are general English, not P4 or its siblings, so the word list is not circular.
2. A key value of 3+ letters that is a code word ("generalrising", "thelordprotector", "england") reads as one word.
3. The SIB run reconstruction is unchanged. If SIB is still below 0.6 under the new list, the statistic is declared unable to
   discriminate at this length and register, and all three hypotheses are logged "untestable by this statistic". No third
   word list is tried.
Everything else (nulls, gate, hypotheses) is unchanged.
