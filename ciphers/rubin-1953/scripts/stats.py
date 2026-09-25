#!/usr/bin/env python3
"""N, distinct K and index of coincidence for the rubin-1953 letter-passage block, with matched
controls: an English sample of the same N (tools/data/pg1661_holmes.txt, several offsets) and a
uniform-random string over the same K (several seeds). No network fetch; controls run offline.

Usage: python3 ciphers/rubin-1953/scripts/stats.py
"""
import random
import re
import statistics
from collections import Counter

ROOT = "/home/user/cipher-lab"
CIPHERTEXT = f"{ROOT}/ciphers/rubin-1953/ciphertext.txt"
ENGLISH_CORPUS = f"{ROOT}/tools/data/pg1661_holmes.txt"

# Block A (letter/word passages) + Block D (closing lines), by line content, excluding
# comments, Block B's numeral line and Block C's 0/1/./x lines. [SYM1] is dropped (not a letter).
LETTER_LINES = [
    "digIs 'sawthn'g mathUlley-Dulles crancklavn' meteore iElli",
    "zheaopfvamn greA'Lltenmn",
    "kKiqtu albawmnabs dzhjellEiE matel ungdreabozvmie oie",
    "sprekln meIktrene fodroscolmn oier",
    "*driEk Conant astereantol Iyvondiolon",
    "desceth megleagna mAlzbourgnion grele",
    "newtdo sfoatzdexklagh 2pont ly asgestaltverbensdi",  # [SYM1] dropped, digit '2' also dropped below
    "Want: datum Tywood Janossey Ketelle",
    "R-QR6                              aliacaui PER",
]


def letters_only_upper(text):
    return re.sub(r"[^A-Za-z]", "", text).upper()


def ic(seq):
    n = len(seq)
    if n < 2:
        return None
    c = Counter(seq)
    return sum(v * (v - 1) for v in c.values()) / (n * (n - 1))


def main():
    body = "".join(LETTER_LINES)
    letters = letters_only_upper(body)
    n = len(letters)
    k = len(set(letters))
    target_ic = ic(letters)
    print(f"target: N={n} letters, distinct K={k}, IC={target_ic:.4f}")

    # English control: N-letter windows from a real English novel, several offsets.
    eng_text = letters_only_upper(open(ENGLISH_CORPUS, encoding="utf-8", errors="replace").read())
    rng = random.Random(1953)
    eng_ics = []
    for _ in range(10):
        start = rng.randrange(0, len(eng_text) - n)
        eng_ics.append(ic(eng_text[start:start + n]))
    print(
        f"english control (pg1661_holmes.txt, N={n}, 10 windows): "
        f"mean={statistics.mean(eng_ics):.4f} range={min(eng_ics):.4f}-{max(eng_ics):.4f}"
    )

    # Uniform random control: N-letter strings drawn uniformly from K symbols, several seeds.
    rand_ics = []
    for seed in range(5):
        rr = random.Random(seed)
        alphabet = [chr(ord("A") + i) for i in range(k)]
        s = "".join(rr.choice(alphabet) for _ in range(n))
        rand_ics.append(ic(s))
    print(
        f"uniform-random control (K={k}, N={n}, 5 seeds): "
        f"mean={statistics.mean(rand_ics):.4f} range={min(rand_ics):.4f}-{max(rand_ics):.4f} "
        f"(closed-form expectation 1/K={1/k:.4f})"
    )


if __name__ == "__main__":
    main()
