# PREREG-D1411POOL -- pooled independent-numeral test of frozen T21r, p.4 + p.5 + p.6 (10 Oct 2026, account 2)

Brief D1411-POOL (LANE FAMILY-A2n, account 2). Written and pushed before any pooled score is computed; scorer `d1411pool/score_pool.py`
is pushed in the same commit.

**What this is.** A confirmatory power test of a fixed table, not a search. All three pages were read, masked and scored one by one
before this pooling (p.4 independent N=112: d1411p6/posthoc/p4_copy_mask.json; p.5 independent N=136: AM-D1411V d1411v/rescore_v.json;
p.6 independent N=60: d1411p6/score_p6.json), and each page's independent coverage sat at or under its own order-shuffle p99 or under the
gloss bar. The per-page results are known to the writer of this PREREG; so is the arithmetic consequence (length-weighted mean of the three
coverages is about 0.51, under the gloss bar). The test is registered anyway because the single pages have no power and the lane asked
for the pooled number; it cannot be tuned, since nothing below is a free choice.

**Material (fixed, no re-reads, no re-masking, no table changes).** Concatenated in page order p.4, p.5, p.6, each page's rows in its
committed numbers.tsv order, keeping only the independent rows under that page's committed copy mask:
- p.4: `d1411p4/numbers.tsv` minus the `score_p6.copy_mask` span set against p.1, p.1 gloss, p.2, p.3 (exactly
  `d1411p6/posthoc/p4_copy_mask.py`); expected N=112.
- p.5: `d1411p5/numbers.tsv` minus the AM-D1411V mask (p5L lines against p.2 only, `score_p6.reproduce_p5` rule); expected N=136.
- p.6: `d1411p6/numbers.tsv` minus `score_p6.copy_mask` against p.1-p.5; expected N=60.
Expected pooled N=308. If any page's independent N differs from the expected figure, the script stops (exit 2) and nothing is scored.

**Statistic and controls (copied unchanged, `d1411v/rescore_v.score`).** Word coverage (`judge_plaintext.NgramModel.cover`, de1600) of
the pooled decode under T21r (primary), T21r_h12 and T21r_h22 (reported, not gated); 200 order shuffles of the pooled number list,
seed 1411, p99; 23 shifted rules (reported); gloss bar = coverage of `gaps150/gloss_text.txt` under de1600 (0.6129, the bar AM-D1411V
names); gloss agreement on the pooled glossed pairs vs 10,000 value-shuffled tables (reported). The order shuffle can differ from the
target on this statistic: shuffling order breaks table-to-position fit (each page's runs showed real != shuffle mean).

**Gate (T21r only).** PASS iff pooled T21r coverage > pooled order-shuffle p99 AND >= 0.6129. Anything else is FAIL. N < 60 cannot occur.

**Outcomes.** PASS -> one ROOM line asking the lane for a verifier; no S grades written by this job. FAIL -> HYPOTHESES.md row as the third
independent-material miss for T21r (p.4 independent, p.6 independent, this pool; p.3 and p.5 independent below gloss), with a statement
on whether rule 3's third-attempt clause applies to "T21r on independent numerals" by word coverage. No token grade moves either way.
