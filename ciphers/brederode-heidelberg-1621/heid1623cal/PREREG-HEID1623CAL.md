# PREREG-HEID1623CAL (written before any calibration run; 16 Oct 2026, 02:2x UTC by date -u)

Job: .claude/briefs/runs/2026-10-15-acct4-depth-steps-2.md, JOB HEID-1623CAL (account 2; cap USD 2.5; box 40 minutes, 02:16-02:56 UTC).
Disk only, no network, no readers, no images. No reading, no key. Question: at what N can `tools/interlinear_align.py` pass its own
shuffle gate on a KNOWN-TRUE gloss with the 1623 block's grammar? Answers whether reading scan 181 (pooled N about 85) is worth its 6 units.

## Tool, exactly as HEID-1623A ran it
`python3 tools/interlinear_align.py align PAIRS OUT_ALIGN OUT_KEY --code-prefix @ --code-chunk 6 --wildcard '?' --keep-fs --shuffle 200
--seed 1623 --shuffle-out FILE.json` (heid1623a/regen_heid1623a.sh line 13, plus --shuffle-out to read the numbers).
**Gate per seed (HEID-1623A PREREG rule 2): PASS = CONSISTENT real > shuffle p95 AND real >= 3.**

## Synthetic pairs (heid1623cal/calib.py; seeds 1-20 at each N = 64, 85, 120, 200; 80 runs)
- Pair sizes: resampled with replacement from the real 1623 pairs' token counts (7, 6, 7, 32, 11; pairs_1623.tsv) until the total
  reaches N; the last pair is trimmed so the total is exactly N (a remainder under 2 is added to the previous pair).
- Clear spans: Dutch words; each word's length drawn from the 171 note's own word-length distribution (heid1623a/note_6022_171.tsv,
  words only, '?' and punctuation dropped), the word itself drawn by frequency from tools/data/nl16 (1569-1589 Dutch prose, the
  nearest era-matched Dutch corpus on disk; nl18 is 1770-1799) among words of that length. Words are added until the span has
  2.0 letters per cipher token (the real pairs: 126 letters / 63 tokens).
- Cipher, design A (PRIMARY, gating) = HEID-1623A poscontrol.py's design: each span's letters cut at t-1 random points into t chunks
  (t = the pair's token count), one code per distinct chunk, one table per seed; codes drawn from the real alphabet (numbers 1-99 and
  the block's letters a b c d e f g h m p r s x y z H), a letter code with probability 0.26 (the real block: 16 of 63 tokens are
  letters, 47 numerals) while letters last; numbers 100-199 added only if the pool runs out (logged).
- Cipher, design B (DESCRIPTIVE, not gating): the same spans cut deterministically (each word into 2-letter chunks from the left, a
  1-letter remainder its own chunk), one code per chunk: a fixed syllable-like table where recurring chunks recur, as a real
  nomenclator would. Its token count follows the span, so its N is reported as realised.

## Reported
Per N: seeds passing / 20 for design A (and B); mean real CONSISTENT and mean p95. Smallest N at which design A passes in >= 18/20
seeds (>= 90%); if none of the four, "untested-by-this-tool below N = 200 at least".
**Verdict line:** "read scan 181 for a pooled alignment: yes" only if design A passes >= 18/20 at N = 85; otherwise "no", with the next
instrument named. Design B never licenses a yes on its own (it is easier than the real cut is known to be) but is reported.
