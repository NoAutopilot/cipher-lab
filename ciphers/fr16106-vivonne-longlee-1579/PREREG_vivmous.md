# PREREG D4-VIVMOUS: Mousset 1912 published key applied to f.101v (6 Oct 2026, written before any decode was scored)

Key: key/mousset1912.tsv (Mousset pp.lviii-lix, published). Crosswalk: key/crosswalk.tsv (label -> table glyph, by shape, frozen
in this commit). No key edits after this commit; no fit.
Decode: tx/passA.tsv (gating) and tx/passB.tsv (reported), all 32 rows in order. 'o o' adjacent -> d. one-value labels -> letter;
multi -> first-listed value for the letter stream (alternatives kept in the reading); none -> dropped from the letter stream.
Word signs (quant, sur, fait, quel, par) expand to their letters in the stream.
Statistic: tools/stream_align.nw_score(decoded letters, copy letters) where copy = tx/plain_c110_f105r.txt folded as in test1.py,
window = copy[0 : len(decode)+20%] (f.101v is the first cipher page and f.105r the first copy page; test1 aligned them from the start).
Null (can vary on the statistic: the score depends on which letter each label gets): 1000 random permutations of the letter values
over the crosswalk's labels (same label set, same value multiset), seed 1.
Matched positive control: the copy's own letters enciphered with the crosswalk inverted (one random label per letter among labels
mapped to it; letters with no label kept as an unmapped symbol), then reader noise at e = 0.576 (half substitutions by label
frequency, a quarter deletions, a quarter insertions), length matched to pass A; 5 seeds; same statistic and null.
Verdict: PASS if real > null p99. If the control passes on fewer than 3/5 seeds at e=0.576 the target's result is NON-TEST
(no power at this reader error), whatever the target number. Also reported, not gated: share of decoded letters that align to an
identical copy letter, and the token grade counts (H = both readers agree on the label and match=one; M = otherwise mapped; I = none).
