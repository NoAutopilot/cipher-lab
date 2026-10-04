# N4-HEL6 pre-registration (4 Oct 2026, 04:4x UTC, written and pushed before any statistic below is computed)

Question: NEAR3-HEL4 found R4372 LR100 (codes 1-800) FAILs the unigram statistic on R1953 (p 0.375) while its order-sensitive
bigram statistic sits at the gate (bi order p 0.010 seed 1, 0.000 seed 2; bi value p 0.025) on 42 adjacent covered pairs.
Does R4372 carry some real values for the Hellen key's codes 1-800, or is the bigram signal an artefact of a nameable mechanism?
Inputs fixed now: `ciphertext_R1953.txt` (DECODE transcription, rule 2), `key_r4372/key_LR100.tsv` (the attribution that gave
the signal), `key_r4369/reading_R1953_tokens.tsv` (R4369 decode, grades), fr18 bigram/unigram model and `words()`/`pmi()` exactly
as `sibling_michell/test_sibling.py`. Script: `key_r4372/diag.py [--check]`, output `key_r4372/diag_output.txt`. Seed 1; seed 2 rerun.

## Part A -- which pairs carry the bigram signal (descriptive, plus a pre-registered artefact rule)
A1. List the 42 pairs (x, y) of adjacent R1953 tokens both covered by key_LR100 with words, with junction PMI, and each pair's
    excess = PMI - mu0, where mu0 = mean of the order-shuffle distribution of the statistic (200 shuffles, as NEAR3-HEL4).
A2. Leave-out curve: drop pairs in order of largest excess first; k* = the fewest pairs whose removal raises bi order p (200
    order shuffles recomputed on the remaining stream, the dropped pairs' tokens kept in the stream but the pairs excluded from
    the real statistic) above 0.0125.
A3. Mechanism tags, each pair tagged by script: (m1) the same code pair (x, y) occurs more than once in R1953 (a repeated phrase;
    an order shuffle destroys repeats whatever the key); (m2) a null ("zero") on either side; (m3) x == y; (m4) both junction
    words in the 30 most frequent fr18 words (a generic function-word collocation any French table yields, e.g. "de la").
    **Artefact rule (pre-registered):** the bigram signal is called an artefact of mechanism m if k* <= 3 AND every one of the
    first k* pairs carries tag m (or the m1 repeat of one pair accounts for them). Otherwise Part A names no mechanism and Part B
    decides.

## Part B -- per-code context check against R4369-decoded neighbours (the gated test; pairs disjoint from Part A's)
B1. Units: every R1953 token t with code 1-800 covered by key_LR100 (value with words, "zero" excluded) that has an adjacent
    token decoded by R4369 at grade H or S (left neighbour n_L and/or right neighbour n_R). Junction scores: PMI(last word of
    n_L, first word of v(t)) and PMI(last word of v(t), first word of n_R). These junctions never appear in Part A's statistic
    (Part A uses pairs with both sides in 1-800), so B is an independent test of the R4372 values.
B2. Statistic S_B = mean junction PMI over all units' junctions. Per-code score s_c = mean over that code's junctions.
B3. Controls (200 draws each), both able to differ from the target on S_B because they change the values at the scored positions:
    (i) R4372's own values permuted among its codes 1-800 (key_LR100, nulls kept in the pool so the junction set changes only
        through which value lands where; junctions re-derived per draw);
    (ii) a size-matched French table from another key on disk: R4370 key_LR100 (codes 1-800, a 1751 French table of the same
        printed form that READ2-HEL2 tested negative on R1953), its values sampled without replacement to the number of R4372
        codes (398) and assigned at random to R4372's codes, per draw. This tests whether R4372's *vocabulary mix* alone (its
        share of function words and syllables) explains any excess.
B4. Positive control (power at matched N, ARM3-ADJ lesson): R4369 LR100's own values on R1953 tokens 801+ whose neighbour is
    also R4369-decoded H/S: hold the 801+ token's value out, score its junctions with its neighbours exactly as B1/B2, subsample to
    the target's junction count J, test against 50 permutations of R4369 values; power = share of 200 subsamples with p <= 0.01.
    If power < 0.8 at J, Part B is a non-test (logged so), whatever the target reads.
B5. **Gate (pre-registered).** R4372 "carries partial real values" iff S_B exceeds the 99th percentile of control (i) AND of
    control (ii) (p <= 0.01 each, seed 1), the same at seed 2, AND power (B4) >= 0.8. Then the codes named as candidate values are
    those with s_c above their own per-code (i) null at p <= 0.05 (per-code null: s_c recomputed under the 200 draws of (i)) and
    at least 2 junctions; graded **M at most**, not adopted into any key, not merged (brief: no key adoption).
    If the gate fails with power >= 0.8: "R4372's values do not fit the R4369-decoded context beyond chance" (control-backed
    negative for R4372 as codes 1-800), and the bigram signal is reported as the Part A mechanism if the artefact rule fired, else
    as "unexplained, not supported by the context check".
    If B3 (i) passes but (ii) does not: the excess is a vocabulary-mix effect of R4372's table (named as such), not real values.
B6. Nothing here changes after the first look. Any further analysis is labelled "not pre-registered".
