#!/usr/bin/env python3
"""NEAR.md untersberg-code step 1, part 2: run the same expander on the target's
six lines. Only run after run_control.py reports GATE MET. Grades M/I only (rule 4):
no H/C/S is possible on an unsolved cipher with no known plaintext."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import expand_lib as L


def main():
    words = L.load_corpus_words()
    model = L.build_bigram_model(words, [])  # whole de16 corpus; target is not in it

    spec = json.load(open(L.SPEC_PATH, encoding="utf-8"))
    tokens = []
    for line in spec["ciphertext"]:
        for raw in line.split():
            raw = raw.strip(",")
            if raw:
                tokens.append(raw)

    result = L.beam_expand(tokens, {}, model)  # no true words known; scored/correct will be 0/0
    choices = result["choices"]

    out_tokens = []
    n_letter = 0
    n_expanded = 0
    for i, tok in enumerate(tokens):
        letters = L.token_letters(tok)
        if letters.isdigit():
            out_tokens.append(tok)
        else:
            n_letter += 1
            w = choices.get(i)
            if w:
                out_tokens.append(w)
                n_expanded += 1
            else:
                out_tokens.append(tok + "[?]")
    expansion = " ".join(out_tokens)

    print("TOP EXPANSION (grade M for every expanded token, I where no candidate was found):")
    print(expansion)
    print(f"\n{n_expanded}/{n_letter} letter-tokens received a beam-search word proposal ({n_letter - n_expanded} had no vocabulary match, grade I).")

    out_path = os.path.join(os.path.dirname(__file__), "target_expansion.txt")
    with open(out_path, "w") as f:
        f.write(expansion + "\n")
    print(f"\nwritten to {out_path}")


if __name__ == "__main__":
    main()
