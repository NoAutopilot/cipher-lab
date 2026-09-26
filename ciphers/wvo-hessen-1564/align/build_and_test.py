#!/usr/bin/env python3
"""Build a reconciled reading of ciphers/wvo-hessen-1564 f.23 (the 1109 cipher enclosure) by
applying willem-van-hessen-1567/siblings/key_174_nomenclator.tsv, using the deterministic
shape classifier in classify.py, and test it against N shuffles of the key's VALUES
(CLAUDE.md rule 3: a matched control the same shuffle cannot fail differently from the target
would be a non-test -- here the shuffle changes which letter each code maps to, which the
statistic (4-gram German log-score) can and does respond to).

Primary transcription pass used: pass A (arbitrary but fixed choice, documented in NOTES.md;
full manual per-token reconciliation against pass B was not completed given the box).
"""
import sys, random, csv
sys.path.insert(0, "/home/user/cipher-lab/tools")
from importlib import import_module
jp = import_module("judge_plaintext")
from classify import classify, load

PASS_FILES = [
    "passA_L01-06.tsv",
    "passA_L07-12.tsv",
    "passA_L13-18.tsv",
]

KEY174 = "/home/user/cipher-lab/ciphers/willem-van-hessen-1567/siblings/key_174_nomenclator.tsv"

def load_key174_values():
    vals = {}
    grades = {}
    for r in csv.DictReader(open(KEY174), delimiter="\t"):
        if r.get("type") == "alphabet":
            vals[r["value"]] = r["value"]
            grades[r["value"]] = r["grade"]
    return vals, grades

def build_tokens():
    """Return list of (line, idx, kind, code_or_text) for all lines, kind in clear/cipher/null/unmatched."""
    out = []
    for fn in PASS_FILES:
        for line, idx, typ, val in load(fn):
            if typ == "clear":
                out.append((line, idx, "clear", val))
            else:
                code = classify(val)
                out.append((line, idx, "cipher", code))
    return out

def decode_string(tokens, value_map):
    """value_map: code -> plaintext letter. Returns the concatenated candidate string."""
    out = []
    for line, idx, kind, val in tokens:
        if kind == "clear":
            out.append(val)
        else:
            if val in ("NULL", "UNMATCHED"):
                continue
            out.append(value_map.get(val, ""))
    return " ".join(out)

def main():
    alphabet_vals, grades = load_key174_values()
    codes_used = sorted({c for _, _, k, c in build_tokens() if k == "cipher" and c not in ("NULL", "UNMATCHED")})
    print("codes used (from cipher tokens):", codes_used)
    real_map = {c: c for c in codes_used}  # key_174's own value IS the code name here (a-z)
    tokens = build_tokens()
    real_text = decode_string(tokens, real_map)
    print("REAL decode (clear text + key_174-decoded cipher runs):")
    print(real_text)
    print()

    corpus = jp.read_corpus("/home/user/cipher-lab/tools/data/de16/composed_enhg.txt")
    model = jp.NgramModel([corpus])
    real_score = model.score(real_text)
    real_cover = model.cover(real_text)
    print(f"REAL score={real_score:.4f} cover={real_cover:.4f} (n_letters={len(jp.fold(real_text))})")

    rnd = random.Random(20260926)
    shuffle_scores = []
    shuffle_covers = []
    for i in range(20):
        vals = codes_used[:]
        rnd.shuffle(vals)
        shuf_map = dict(zip(codes_used, vals))
        text = decode_string(tokens, shuf_map)
        s = model.score(text)
        c = model.cover(text)
        shuffle_scores.append(s)
        shuffle_covers.append(c)
    shuffle_scores.sort()
    shuffle_covers.sort()
    print(f"SHUFFLE (n=20) score: min={shuffle_scores[0]:.4f} max={shuffle_scores[-1]:.4f} mean={sum(shuffle_scores)/20:.4f}")
    print(f"SHUFFLE (n=20) cover: min={shuffle_covers[0]:.4f} max={shuffle_covers[-1]:.4f} mean={sum(shuffle_covers)/20:.4f}")
    print()
    print(f"Real beats shuffle max on score? {real_score > shuffle_scores[-1]}")
    print(f"Real beats shuffle max on cover? {real_cover > shuffle_covers[-1]}")

if __name__ == "__main__":
    main()
