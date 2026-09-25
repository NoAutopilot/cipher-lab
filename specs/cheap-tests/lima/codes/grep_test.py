#!/usr/bin/env python3
"""lima-1916 cheap test 1: commercial-code lookup.
Grep the 17 cipher words (both transcriptions of word 1) as whole words, case-folded,
against four telegraph codebooks' OCR text. Matched controls: 17 random real words
drawn from each book's own OCR vocabulary (method-sensitivity check), and 17 random
strings matching the target's length profile (chance-hit rate)."""
import json
import random
import re

OUTDIR = "specs/cheap-tests/lima/codes"

# Position 1 has two newspaper transcriptions; both are searched, either counts as a hit
# for that word. All other 16 words are single-spelling per specs/lima-1916.json.
TARGET_WORDS = [
    ("nvlvaft/nvkvaft", ["nvlvaft", "nvkvaft"]),
    ("aakat", ["aakat"]),
    ("txpxsck", ["txpxsck"]),
    ("upbk", ["upbk"]),
    ("txphn", ["txphn"]),
    ("ohay", ["ohay"]),
    ("ybtx", ["ybtx"]),
    ("cpt", ["cpt"]),
    ("mxhg", ["mxhg"]),
    ("wae", ["wae"]),
    ("sxfp", ["sxfp"]),
    ("zavfz", ["zavfz"]),
    ("ack", ["ack"]),
    ("txlk", ["txlk"]),
    ("wayx", ["wayx"]),
    ("za", ["za"]),
    ("thx", ["thx"]),
]
LENGTH_PROFILE = [len(v[0]) for v in TARGET_WORDS]  # first variant's length per word

BOOKS = ["abc_code", "western_union", "lieber", "bentley"]

WORD_RE = re.compile(r"[a-zA-Z]{2,8}")


def load_vocab(text):
    return WORD_RE.findall(text)


def whole_word_hit(word_lc, wordset_lc):
    return word_lc in wordset_lc


def random_string(length, rng):
    return "".join(rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(length))


def main():
    rng = random.Random(20260925)  # fixed seed, reproducible (rule 7)
    results = {}
    for book in BOOKS:
        path = f"{OUTDIR}/{book}.txt"
        with open(path, encoding="utf-8", errors="replace") as f:
            text = f.read()
        tokens = load_vocab(text)
        wordset_lc = set(t.lower() for t in tokens)

        # target hits
        target_hits = []
        for label, variants in TARGET_WORDS:
            hit = any(whole_word_hit(v.lower(), wordset_lc) for v in variants)
            target_hits.append((label, hit))
        target_hit_count = sum(1 for _, h in target_hits if h)

        # positive control: 17 random real words from this book's own vocabulary,
        # restricted to the same length range as the target words (2-8 chars) to
        # keep the sensitivity check comparable in scale to the target grep.
        candidates = sorted(set(t.lower() for t in tokens if 2 <= len(t) <= 8))
        rng_book = random.Random(20260925 + hash(book) % 1000)
        pos_sample = rng_book.sample(candidates, min(17, len(candidates)))
        pos_hits = [whole_word_hit(w, wordset_lc) for w in pos_sample]
        pos_hit_count = sum(pos_hits)

        # random-string control: 17 random strings, target's length profile
        rng_rand = random.Random(20260925 + hash(book) % 1000 + 1)
        rand_sample = [random_string(L, rng_rand) for L in LENGTH_PROFILE]
        rand_hits = [whole_word_hit(w, wordset_lc) for w in rand_sample]
        rand_hit_count = sum(rand_hits)

        results[book] = {
            "target_hits": target_hit_count,
            "target_total": len(TARGET_WORDS),
            "target_detail": target_hits,
            "positive_control_hits": pos_hit_count,
            "positive_control_total": len(pos_sample),
            "positive_control_sample": pos_sample,
            "random_string_hits": rand_hit_count,
            "random_string_total": len(rand_sample),
            "random_string_sample": rand_sample,
            "vocab_size": len(wordset_lc),
        }
        print(f"{book}: target {target_hit_count}/17, positive-control {pos_hit_count}/{len(pos_sample)}, "
              f"random-string {rand_hit_count}/17 (vocab {len(wordset_lc)})")

    with open(f"{OUTDIR}/results.json", "w") as f:
        json.dump(results, f, indent=1)


if __name__ == "__main__":
    main()
