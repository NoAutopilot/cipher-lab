#!/usr/bin/env python3
"""AX2-4612S (b): known-answer control for tools/key_repair.py, 3 seeds. Per the job brief's own
fallback design ('if [re-enciphering] is too awkward, instead SWAP...'): pick 10 codes used >=5 times
in ax4612tr/ciphertext_5811_cut833.tsv under key_full.tsv, whose current key_full value is a plain
single letter; swap the letter values of 8 of them in 4 pairs; replace the other 2 codes' values with
a French bigram that is not their true letter ('hiding' them as syllable codes). Run
tools/key_repair.py's repair() from this perturbed key on the same 5811 cut, and compare the repaired
key to the untouched key_full: recovery (of the 8 swapped codes) and false changes (on the other,
untouched codes -- the 2 hidden-bigram codes are reported separately, not counted either way, since
the brief's gate names only the 8 swapped codes)."""
import os
import random
import sys

R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(R, "tools"))
import key_repair as kr  # noqa: E402
import decode_key as dk  # noqa: E402

TARGET = os.path.join(os.path.dirname(__file__), "..", "ax4612tr", "ciphertext_5811_cut833.tsv")
KEY = os.path.join(os.path.dirname(__file__), "..", "key_full.tsv")

recs = kr.load_ciphertext(TARGET, "=", ["[blank]", "[blot]", "[spot]"])
template = kr.build_template(recs)
key_full = dk.load_key(KEY)
counts = __import__("collections").Counter(data for kind, data in template if kind == "sign")

eligible = sorted(c for c, n in counts.items() if n >= 5 and c in key_full
                   and len(key_full[c]["value"]) == 1 and key_full[c]["value"].isalpha())
print(f"{len(eligible)} codes used >=5 times with a single-letter key_full value")

import french16_ngram as fr  # noqa: E402
model = fr.load()
corpus_words = list(fr.corpus_words())
bigrams = kr.corpus_ngrams(corpus_words, 2, 60)
trigrams = kr.corpus_ngrams(corpus_words, 3, 20)
cand_values = kr.candidate_values(kr.ALPHA26, bigrams, trigrams)

results = []
for seed in range(3):
    rng = random.Random(46120 + seed)
    chosen = rng.sample(eligible, 10)
    swap_codes, hide_codes = chosen[:8], chosen[8:]
    perturbed = {c: dict(row) for c, row in key_full.items()}
    pairs = [(swap_codes[i], swap_codes[i + 1]) for i in range(0, 8, 2)]
    for a, b in pairs:
        perturbed[a]["value"], perturbed[b]["value"] = key_full[b]["value"], key_full[a]["value"]
    for c in hide_codes:
        true_letter = key_full[c]["value"]
        pick = next(g for g in bigrams if g != true_letter)
        perturbed[c]["value"] = pick

    values, changes, rounds_run = kr.repair(template, perturbed, model, margin=3.0, rounds=4,
                                             cand_values=cand_values)

    recovered = sum(1 for c in swap_codes if values[c] == key_full[c]["value"])
    hidden_recovered = sum(1 for c in hide_codes if values[c] == key_full[c]["value"])
    perturbed_set = set(swap_codes) | set(hide_codes)
    false_changes = [c for c in key_full if c not in perturbed_set and values[c] != key_full[c]["value"]]

    print(f"seed {seed}: swap_codes={swap_codes} hide_codes={hide_codes}")
    print(f"  recovered {recovered}/8 swapped codes to their true key_full letter "
          f"({recovered / 8:.3f}); {hidden_recovered}/2 hidden-bigram codes also reverted to their "
          f"true letter (not gated)")
    print(f"  false changes on the other {len(key_full) - 10} untouched codes: {len(false_changes)} "
          f"({', '.join(false_changes[:20])}{' ...' if len(false_changes) > 20 else ''})")
    results.append(dict(seed=seed, recovered=recovered, hidden_recovered=hidden_recovered,
                         false_changes=len(false_changes)))

mean_recovery = sum(r["recovered"] for r in results) / (3 * 8)
max_false = max(r["false_changes"] for r in results)
print()
print(f"GATE: mean recovery {mean_recovery:.3f} (>= 0.75 needed)? {mean_recovery >= 0.75}. "
      f"max false changes across seeds {max_false} (<= 2 needed)? {max_false <= 2}.")
