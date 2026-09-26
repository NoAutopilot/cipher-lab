#!/usr/bin/env python3
"""AX2-4612S3: known-answer control for tools/key_repair.py's --objective paired (default,
--no-null-below 121, --min-occ 3), 3 seeds. Same design as AX2-4612S/AX2-4612S2 (identical seeds,
identical eligible-code pool, identical perturbation shape) so the numbers are directly comparable:
pick k=8 codes total (used >=5 times in ax4612tr/ciphertext_5811_cut833.tsv under key_full.tsv,
whose current key_full value is a plain single letter) and perturb all 8 -- 6 of them (3 pairs) get
their letter values swapped pairwise, and 2 of them (the H-S shape: a code that might really stand
for a syllable) get a French bigram value that is not their true letter -- then run
tools/key_repair.py's repair() from this perturbed key on the same 5811 cut and compare the repaired
key to the untouched key_full: recovery (does a code's repaired value match its true key_full
letter?) is reported for all 8 together (the brief's own gate denominator) AND for the 2
bigram-hidden codes alone (reported separately); false changes are counted on the other, untouched
codes."""
import os
import random
import sys

R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(R, "tools"))
import key_repair as kr  # noqa: E402
import decode_key as dk  # noqa: E402
import french16_ngram as fr  # noqa: E402

TARGET = os.path.join(os.path.dirname(__file__), "..", "ax4612tr", "ciphertext_5811_cut833.tsv")
KEY = os.path.join(os.path.dirname(__file__), "..", "key_full.tsv")
NO_NULL_BELOW = 121
MIN_OCC = 3

recs = kr.load_ciphertext(TARGET, "=", ["[blank]", "[blot]", "[spot]"])
template = kr.build_template(recs)
key_full = dk.load_key(KEY)
counts = __import__("collections").Counter(data for kind, data in template if kind == "sign")

eligible = sorted(c for c, n in counts.items() if n >= 5 and c in key_full
                   and len(key_full[c]["value"]) == 1 and key_full[c]["value"].isalpha())
print(f"{len(eligible)} codes used >=5 times with a single-letter key_full value")

model = fr.load()
mu = kr.compute_mu(model)
scorer = kr.make_scorer(model, "excess", mu)
print(f"mu (fr16 order-5 model's mean log2 p/char on its own held-out text): {mu:.4f}")
corpus_words = list(fr.corpus_words())
bigrams = kr.corpus_ngrams(corpus_words, 2, 60)
trigrams = kr.corpus_ngrams(corpus_words, 3, 20)
cand_values = kr.candidate_values(kr.ALPHA26, bigrams, trigrams)

results = []
for seed in range(3):
    rng = random.Random(46120 + seed)
    chosen = rng.sample(eligible, 8)
    bigram_codes, swap_codes = chosen[:2], chosen[2:8]
    perturbed = {c: dict(row) for c, row in key_full.items()}
    pairs = [(swap_codes[i], swap_codes[i + 1]) for i in range(0, 6, 2)]
    for a, b in pairs:
        perturbed[a]["value"], perturbed[b]["value"] = key_full[b]["value"], key_full[a]["value"]
    for c in bigram_codes:
        true_letter = key_full[c]["value"]
        pick = next(g for g in bigrams if g != true_letter)
        perturbed[c]["value"] = pick

    values, changes, rounds_run = kr.repair(template, perturbed, scorer, margin=3.0, rounds=4,
                                             cand_values=cand_values, no_null_below=NO_NULL_BELOW,
                                             min_occ=MIN_OCC, pair_model=model, pair_mu=mu)

    recovered_all = sum(1 for c in chosen if values[c] == key_full[c]["value"])
    recovered_bigram = sum(1 for c in bigram_codes if values[c] == key_full[c]["value"])
    altered_set = set(chosen)
    false_changes = [c for c in key_full if c not in altered_set and values[c] != key_full[c]["value"]]

    print(f"seed {seed}: swap_codes={swap_codes} (pairs {pairs}) bigram_codes={bigram_codes}")
    print(f"  recovered {recovered_all}/8 altered codes to their true key_full letter "
          f"({recovered_all / 8:.3f}); of those, {recovered_bigram}/2 were the bigram-hidden codes")
    print(f"  false changes on the other {len(key_full) - 8} untouched codes: {len(false_changes)} "
          f"({', '.join(false_changes[:20])}{' ...' if len(false_changes) > 20 else ''})")
    results.append(dict(seed=seed, recovered_all=recovered_all, recovered_bigram=recovered_bigram,
                         false_changes=len(false_changes)))

mean_recovery = sum(r["recovered_all"] for r in results) / (3 * 8)
mean_bigram_recovery = sum(r["recovered_bigram"] for r in results) / (3 * 2)
max_false = max(r["false_changes"] for r in results)
print()
print(f"GATE: mean recovery {mean_recovery:.3f} (>= 0.75 needed)? {mean_recovery >= 0.75}. "
      f"bigram-only mean recovery {mean_bigram_recovery:.3f} (reported, not gated separately). "
      f"max false changes across seeds {max_false} (<= 2 needed)? {max_false <= 2}.")
