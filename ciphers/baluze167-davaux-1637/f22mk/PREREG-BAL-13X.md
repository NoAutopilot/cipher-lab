# PREREG BAL-13X (account 4, LANE DEFAULT-A4-1035-15), 15 Oct 2026 10:5x UTC by date -u -- pushed before any score or fetch

Prior work: `tools/prior_work.py baluze167-davaux-1637 --item-spec 'Baluze 169 13: cross-run control; 169 c298 c302 plain 65 strokes' --step-type key
--offline` exit 4: the one LEAD is this job's own ROOM claim (1-own, 0.0 h); generic UNCHECKED rows only otherwise.

## Part 1: cross-run control for 13: = Mr (no new reads; data = the four committed pairs files, unchanged)
Why: BAL-169C's within-run shuffle has no power here (each 13: run is 2 tokens, so a within-run permutation gives 4/4 about 1 in 16 per run; 2/200
tied). Rule-3 "can the control differ by construction" check, written before scoring: the statistic is k = number of glossed 13: tokens whose placed
unit is Mr. A cross-run shuffle permutes every placed unit among every placed token of all four files (glossed_pairs.tsv, _r, _169, _169c; '-'
units excluded), so a 13: token can receive any unit in the pool; k under the null depends on how many Mr units the pool holds and can be 0..4. The
manipulation (which unit sits on a 13: token) is the same axis as the statistic. It can fail differently from the target.
Scorer: f22mk/score_13x.py (new, reads the same four files as score_marks_169c.py).
1. Target: k_real for 13: = Mr. Null A: global cross-run shuffle, 10,000 seeds. Null B: shuffle stratified by pairs file (units move only among tokens
   of the same file, i.e. the same office batch), 10,000 seeds. Report mean, p99, max, count >= real for each.
2. Calibration controls, same statistic and same nulls, run in the same script before the target is printed:
   (a) positive: 13' = co (H in key.tsv; 9 glossed); (b) power at the target's n: 13' = co subsampled to 4 occurrences, 1,000 random subsets, each
   scored against Null A with 1,000 seeds; pass rate = share of subsets whose real count beats every null draw at p < 0.01 (count >= real / seeds
   < 0.01); (c) wrong value: 13: = co (must give k_real 0 and not pass).
   Gate on the controls: (a) passes, (b) pass rate >= 0.95, (c) does not pass. If any fails, stop: Part 1 is a non-test, logged so, 13: stays M.
3. Call rule for 13: (unchanged from score_marks.py except the null): S if k >= 3, k/n >= 3/4, and the share of Null A draws >= k_real is < 0.01 AND
   the share of Null B draws >= k_real is < 0.01; else M.
4. Then `tools/decode_key.py ciphers/baluze167-davaux-1637 --try 13:=Mr` at every occurrence (13: occurs once in the ciphertext files, f.22r L03 pos 13;
   key.tsv already holds 13: Mr H, so --try's statistic VALUE minus current value is 0 by construction: reported as such, a non-test of the value,
   not a negative). The S, if reached, rests on Part 1 alone; the f.22r token is regraded M -> S only if Part 1 passes AND the f.22r 13:'s own mark
   (two dots) was settled by BAL-F22R/BAL169-F22B (already S per NOTES); nothing else in key.tsv changes (13: is already H there).
5. Limits stated now: one reader per file, not blind (each reader knew key.tsv); the null tests chance association of gloss units with signs, not
   reader bias. A pass licenses "13: reads Mr in the 4 glossed same-office occurrences beyond chance placement", not more.

## Part 2: the two unsettled 65 strokes (c298 L12 "le Masserati", c302 L01 "diray"; Baluze 169 btv1b9001488b)
6. openapi.bnf.fr IIIF, ROOM take/release, one at a time >= 3.3 s, <= 4 requests: per canvas one `full/1000,` locator (if needed) and one region at
   `max`. Scratchpad only, never git; regen line in images/manifest.json style in NOTES.
7. Mark rule fixed now: plain = no stroke in cipher ink above or touching the top of the 5 at native scale; acute = a separate rising stroke in cipher
   ink (same ink tone as the numerals, not the gloss) above the 6 or 5. A stroke I cannot assign stays 65? and is not scored.
8. A settled plain 65 under a gloss is added to f22mk/glossed_pairs_169c.tsv (as a new row, the 65? row kept with a note) and scored by
   score_marks_169c.py unchanged (call rule there; plain 65 tested against ra). Under 3 glossed plain 65: M, reported as a count. f.22r L04 pos 0 stays
   M unless that rule gives S.

## Part 3 (only if >= 30% of cap left): c276 R16 "d'une" E shape, one request (Baluze 167 btv1b9001489r), epsilon vs Ebar, by eye at max; logged, no
grade change by itself.
