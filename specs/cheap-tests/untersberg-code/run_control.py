#!/usr/bin/env python3
"""NEAR.md untersberg-code step 1: abbreviation-expander control, run FIRST (rule 3).

Usage: python3 specs/cheap-tests/untersberg-code/run_control.py
Run from the repo root. Writes control_results.json in this directory.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import expand_lib as L

SEED = 20260925
WINDOW_LEN = 71
N_WINDOWS = 5
GATE = 0.30


def run_one_set(words, letter_len_labels, digit_lens, label):
    windows = L.build_windows(words, n_windows=N_WINDOWS, window_len=WINDOW_LEN, seed=SEED)
    per_window = []
    for i, (start, wwords) in enumerate(windows):
        before, after = L.rest_of_corpus(words, start, WINDOW_LEN)
        model = L.build_bigram_model(before, after)
        tokens, true_words = L.make_synthetic_window(wwords, letter_len_labels, digit_lens, seed=SEED + i)
        result = L.beam_expand(tokens, true_words, model)
        per_window.append({
            "window_start": start,
            "n_tokens": len(tokens),
            "n_scored": result["scored"],
            "correct": result["correct"],
            "score": result["score"],
        })
        print(f"[{label}] window {i} (start={start}): {result['correct']}/{result['scored']} = {result['score']:.3f}")
    mean = sum(w["score"] for w in per_window) / len(per_window)
    return per_window, mean


def main():
    shape = L.target_shape()
    letter_len_labels = L.abbreviation_length_labels(shape["letter_lens"])
    digit_lens = shape["digit_lens"]
    print("target shape:", {"n_tokens": shape["n_tokens"], "n_letter": len(letter_len_labels), "n_digit": len(digit_lens)})

    words = L.load_corpus_words()

    print("\n=== Control: real de16 word order (bigram model from leave-window-out rest) ===")
    control_windows, control_mean = run_one_set(words, letter_len_labels, digit_lens, "control")

    print("\n=== Floor: shuffled word order (breaks bigram signal) ===")
    shuffled = list(words)
    import random
    random.Random(SEED).shuffle(shuffled)
    floor_windows, floor_mean = run_one_set(shuffled, letter_len_labels, digit_lens, "floor")

    out = {
        "seed": SEED,
        "window_len": WINDOW_LEN,
        "n_windows": N_WINDOWS,
        "gate": GATE,
        "target_shape": {
            "n_tokens": shape["n_tokens"],
            "n_letter_tokens": len(letter_len_labels),
            "n_digit_tokens": len(digit_lens),
            "digit_lens": digit_lens,
            "letter_len_histogram": {str(k): letter_len_labels.count(k) for k in sorted(set(letter_len_labels))},
        },
        "control": {"per_window": control_windows, "mean": control_mean},
        "floor": {"per_window": floor_windows, "mean": floor_mean},
        "gate_met": control_mean >= GATE,
    }
    with open(os.path.join(os.path.dirname(__file__), "control_results.json"), "w") as f:
        json.dump(out, f, indent=1)

    print(f"\nCONTROL MEAN: {control_mean:.3f} (gate {GATE})")
    print(f"FLOOR MEAN (shuffled word order): {floor_mean:.3f}")
    print("GATE MET" if out["gate_met"] else "CONTROL BELOW GATE")


if __name__ == "__main__":
    main()
