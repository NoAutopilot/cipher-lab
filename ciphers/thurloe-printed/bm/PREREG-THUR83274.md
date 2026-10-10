# PREREG-THUR83274 -- written 10 Oct 2026, 18:1x UTC by date -u, before the control score is computed
Job THUR-83274 (LANE FAMILY-A2s, account 2). Target: l.83274 (Birch 1742 vol 6 p.698) row 9 after the clear word "the" (14 groups) and row 10
(numeral groups only), the two rows with no printed gloss. Disclosure: the decode of these groups under bm/key_period_f117.tsv was looked up by
hand (value -> letter) before this file and before the control ran, so the text was seen first; the gate below is therefore a check on the
statistic, not a blind one.
- Statistic: mean log10 4-gram score (decode_44535.py's score(), same smoothing) of the letter stream, segments split at clear words/rows.
- Control: sheet letter values (codes 1-101) permuted over the sheet's letter codes, 200 draws, seeds 0..199; gate real > shuffle p95.
- Corpus (disk only): tools/data/en16_repo/*.txt (1650s Thurloe readings, no '#' lines); bm/ vol-6 OCR corpus of decode_44535.py is not on disk.
- Power check: the same statistic on every 28-letter window of l.83274's glossed rows 1-8 decoded under the sheet, each against its own 200 shuffles;
  the control "discriminates" at this length if >= 0.8 of windows exceed their own p95.
