#!/usr/bin/env python3
"""Blind transcription (one pass, LANE B3 worker bRAY, 25 Sept 2026) of
ciphers/rayburn-2004/images/Rayburn-Cryptogram.jpg into a type-id sequence, plus
cheap test 1's IC computation against a matched English control (same N) and a
matched uniform-random control (same K). Position/mark data lives in the TSV this
script writes; type ids group visually-identical symbols (same letter, same case)
and keep composite/ligature-looking marks (e.g. an 'A' with a small 'm' written
under it) as their own type rather than folding them into a plain letter.

Not a decode: cheap_tests_in_order[1]/[2] (diagram-layout test, substitution
judge) are explicitly out of scope for this worker (breadth.md: first test only).
"""
import random
import statistics

# (group, row_in_group, type_id, mark) -- mark: U=underlined, S=struck/crossed,
# O=overlined (mark above, not below -- distinct from U), D=double/ambiguous mark,
# '?'=mark not confidently classified.
TOKENS = [
    # --- main grid, inside/below the rounded-rectangle enclosure ---
    ("main", 1, "W", "U"), ("main", 1, "j", "U"), ("main", 1, "u", "O"),
    ("main", 1, "P", "U"), ("main", 1, "D", "U"),
    ("main", 2, "a", "U"), ("main", 2, "X", "U"), ("main", 2, "o", "U"),
    ("main", 2, "R", "U"), ("main", 2, "w", "S"), ("main", 2, "i", "U"),
    ("main", 2, "s", "U"),
    ("main", 3, "M", "U"), ("main", 3, "rn?", "S"), ("main", 3, "g", "U"),
    ("main", 4, "H", "U"), ("main", 4, "k", "S"), ("main", 4, "e", "U"),
    ("main", 4, "I-bold", "U"), ("main", 4, "B", "U"), ("main", 4, "f", "U"),
    ("main", 4, "e", "U"),
    ("main", 5, "X", "U"), ("main", 5, "L?", "U"), ("main", 5, "o", "U"),
    ("main", 5, "y/x?", "U"), ("main", 5, "u", "U"), ("main", 5, "I-bold2", "U"),
    ("main", 6, "w", "S"), ("main", 6, "A", "U"), ("main", 6, "z", "U"),
    ("main", 6, "Q", "U"), ("main", 6, "Y", "U"),
    ("main", 7, "b", "S"), ("main", 7, "U", "U"), ("main", 7, "kr?", "U"),
    ("main", 7, "cross/t?", "U"), ("main", 7, "P", "U"), ("main", 7, "s", "U"),
    ("main", 7, "q", "U"),
    ("main", 8, "Am?", "U"), ("main", 8, "c", "U"), ("main", 8, "Z", "U"),
    ("main", 8, "i", "U"), ("main", 8, "Y", "U"), ("main", 8, "Z", "U"),
    ("main", 8, "D", "U"),
    ("main", 9, "RH?", "U"), ("main", 9, "V", "U"), ("main", 9, "h", "U"),
    ("main", 10, "E", "U"), ("main", 10, "f", "U"), ("main", 10, "b", "U"),
    ("main", 10, "d", "U"), ("main", 10, "av?", "U"), ("main", 10, "a", "U"),
    ("main", 10, "r", "U"), ("main", 10, "O", "U"),
    # --- left margin (separate side sequence, own vertical rule) ---
    ("left-margin", 1, "p", "S"), ("left-margin", 2, "pct(%)", "?"),
    ("left-margin", 3, "K", "?"), ("left-margin", 4, "4/h7?", "?"),
    ("left-margin", 5, "p-loop?", "?"), ("left-margin", 6, "d-loop?", "?"),
    ("left-margin", 7, "Y-tail?", "?"), ("left-margin", 8, "K*", "S"),
    # --- right margin ---
    ("right-margin", 1, "X-cross?", "S"), ("right-margin", 2, "amp(&)", "?"),
    ("right-margin", 3, "hash(#)", "?"), ("right-margin", 4, "N?", "?"),
    ("right-margin", 5, "K", "?"), ("right-margin", 6, "H-hash?", "?"),
    ("right-margin", 7, "3", "?"), ("right-margin", 8, "dot-?", "?"),
]

def main():
    with open("ciphertext.tsv", "w") as f:
        f.write("idx\tgroup\trow\ttype_id\tmark\n")
        for idx, (g, r, t, m) in enumerate(TOKENS, 1):
            f.write(f"{idx}\t{g}\t{r}\t{t}\t{m}\n")

    N = len(TOKENS)
    types = [t for _, _, t, _ in TOKENS]
    K = len(set(types))
    counts = {}
    for t in types:
        counts[t] = counts.get(t, 0) + 1

    def ic(seq_counts, n):
        return sum(c * (c - 1) for c in seq_counts.values()) / (n * (n - 1))

    target_ic = ic(counts, N)

    # English control: same N, sampled from tools/data en corpus (letters only,
    # case-folded to match a 26-symbol alphabet the way a plain substitution
    # cipher's IC baseline is usually computed).
    en_paths = [
        "../../../tools/data/pg1661_holmes.txt",
        "../../../tools/data/pg2701_mobydick.txt",
    ]
    en_text = []
    for path in en_paths:
        with open(path, encoding="utf-8", errors="ignore") as fh:
            en_text.append(fh.read())
    en_text = "".join(en_text)
    letters = [c for c in en_text if c.isalpha()]

    random.seed(20260925)
    en_ics = []
    if len(letters) >= N:
        for _ in range(200):
            start = random.randrange(0, len(letters) - N)
            sample = letters[start:start + N]
            c = {}
            for ch in sample:
                c[ch] = c.get(ch, 0) + 1
            en_ics.append(ic(c, N))

    uniform_ics = []
    for _ in range(200):
        draws = [random.randrange(K) for _ in range(N)]
        c = {}
        for d in draws:
            c[d] = c.get(d, 0) + 1
        uniform_ics.append(ic(c, N))

    with open("test1_result.txt", "w") as f:
        f.write(f"N (tokens, main grid + both margins) = {N}\n")
        f.write(f"K (distinct type ids, case-sensitive, composites kept separate) = {K}\n")
        f.write(f"target IC = {target_ic:.4f}\n")
        if en_ics:
            f.write(
                f"English control IC (same N, {len(en_ics)} samples, tools/data en corpus, "
                f"26-letter alphabet): mean {statistics.mean(en_ics):.4f} "
                f"[{min(en_ics):.4f}, {max(en_ics):.4f}]\n"
            )
        else:
            f.write("English control IC: not run (no en corpus found under tools/data)\n")
        f.write(
            f"Uniform-random control IC (same N and K, {len(uniform_ics)} draws): "
            f"mean {statistics.mean(uniform_ics):.4f} "
            f"[{min(uniform_ics):.4f}, {max(uniform_ics):.4f}] "
            f"(expected ~1/K = {1/K:.4f})\n"
        )

    print(open("test1_result.txt").read())

if __name__ == "__main__":
    main()
