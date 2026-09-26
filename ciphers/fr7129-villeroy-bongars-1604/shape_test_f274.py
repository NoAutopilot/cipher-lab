#!/usr/bin/env python3
"""KEY-7129 shape test (CLAUDE.md rule 3): does key_f274.tsv (the f.274 alphabet-substitution grid, cipher
no.2 per Tomokiyo) decode ciphertext_candidate.txt (the candidate cipher block at f.268r) better than 20
class-shuffled versions of the same key? A shape test, not a reading -- no status change, no reading claim.

Usage: python3 ciphers/fr7129-villeroy-bongars-1604/shape_test_f274.py
"""
import importlib.util
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_tokens(path):
    tokens = []
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        tokens += line.split()
    return tokens


def coverage_and_stream(tokens, key):
    hits = 0
    letters = []
    for t in tokens:
        code = t.lstrip("^")  # overline marker is not part of the code itself
        row = key.get(code) or key.get(t)
        if row and row["value"] and row["value"] not in ("?",):
            hits += 1
            v = row["value"]
            if len(v) == 1 and v.isalpha():
                letters.append(v)
    return hits / len(tokens) if tokens else 0.0, "".join(letters)


def main():
    dk = load_module("dk", ROOT / "tools" / "decode_key.py")
    jp = load_module("jp", ROOT / "tools" / "judge_plaintext.py")

    key = dk.load_key(HERE / "keys" / "key_f274.tsv")
    tokens = load_tokens(HERE / "ciphertext_candidate.txt")

    cov, stream = coverage_and_stream(tokens, key)
    print(f"tokens: {len(tokens)}")
    print(f"coverage (tokens whose code is in key_f274.tsv, tier-agnostic): {cov:.3f}")
    print(f"decoded letter-stream length: {len(stream)}")
    print(f"decoded letter-stream (raw, unspaced -- NOT a reading, just the shape-test input): {stream}")

    fr = jp.NgramModel([jp.read_corpus(p) for p in jp.LANG_CORPORA["fr"]])
    real_score = fr.score(stream) if stream else float("nan")
    print(f"fr16 NgramModel score of the real decode: {real_score:.4f}")

    codes = list(key.keys())
    values = [key[c]["value"] for c in codes]
    rnd = random.Random(20260926)
    shuffled_scores = []
    shuffled_covs = []
    for draw in range(20):
        shuffled_values = values[:]
        rnd.shuffle(shuffled_values)
        shuf_key = {c: {"value": v} for c, v in zip(codes, shuffled_values)}
        c_cov, c_stream = coverage_and_stream(tokens, shuf_key)
        shuffled_covs.append(c_cov)
        shuffled_scores.append(fr.score(c_stream) if c_stream else float("nan"))

    valid = [s for s in shuffled_scores if s == s]  # drop NaN
    mean_shuf = sum(valid) / len(valid) if valid else float("nan")
    var_shuf = sum((s - mean_shuf) ** 2 for s in valid) / len(valid) if valid else float("nan")
    sd_shuf = var_shuf ** 0.5
    z = (real_score - mean_shuf) / sd_shuf if sd_shuf else float("nan")

    print(f"20 class-shuffled keys (rule 3 control): mean score {mean_shuf:.4f}, sd {sd_shuf:.4f}")
    print(f"z (real vs shuffled-key control): {z:.2f}")
    print(f"mean shuffled-key coverage: {sum(shuffled_covs)/len(shuffled_covs):.3f} (coverage is code-set-driven, near-identical to the real key's coverage by construction -- only the VALUES differ under shuffling, so coverage is not itself the discriminating statistic here, the fr16 score is)")


if __name__ == "__main__":
    main()
