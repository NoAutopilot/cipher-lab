# PREREG-OBREDDP (10 Oct 2026, 07:0x UTC by date -u, account 2) -- written and pushed before any score below is computed

Texts: no. 92 tokens as `obred187/overlap.py v92()` extracts them (121 Arabic groups; XLII and the clear sums excluded), split into
runs at every clear word (XLII counts as a clear separator); 187 tokens as `ciphertext_187.tsv` (59 groups), split into runs at the two
clear insertions. Script `obred187/structure.py` (`--check`), output `obred187/structure.json`. Seed 92, 10000 draws per control.

G1 (shared order). Statistic B = number of distinct ordered adjacent pairs (a,b) of code values that occur inside a run in BOTH texts.
Control: permute each text's token sequence independently (run lengths kept, values reassigned to positions at random); this changes
which pairs are adjacent, so B can differ from the target (rule 3: order-dependent statistic, order-shuffling control).
Pass: p = (1 + #{B_ctrl >= B_obs}) / 10001 < 0.01. Pass reads "the two texts share ordered value sequences above chance: consistent
with words or syllable strings spelled the same way in one table", grade M, never a reading. Fail reads "no shared order above chance
at N=180" (not a design exclusion). Trigram count reported alongside, not gated.

G2 (names stand alone). Statistic H = share of no. 92 tokens with value >= 600 that stand as a run of length 1. Control: permute
no. 92's 121 values over its positions with the run structure kept. Pass: p < 0.01. Pass reads "the 600-751 band is used as
single-token name/title codes in no. 92 (nomenclator name band)", grade M. 187 is not gated (its runs are 42 and 17 long).

Everything else in structure.json (run lengths, contexts, value range by run length, crib positions) is descriptive, not a gate.
