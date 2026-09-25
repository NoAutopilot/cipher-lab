#!/usr/bin/env python3
"""Shuffle the sign stream of a cipher_codes.tsv to destroy sequence while keeping the multiset
(and, with --within-lines, the line-level profile) intact -- LANE R7 MSHUF's control for whether an
anneal gap over the matched control (rule 3) comes from real plaintext sequence or only from the
target's skewed symbol profile.

Full shuffle: every sign across the whole stream is permuted together (line/position kept as
scaffolding only; the profile per line is destroyed along with word order).

--within-lines: signs are permuted only inside each line's own rows, so each line keeps its own
sign multiset (its length and symbol mix) but the order within it is destroyed. Across-line order
is untouched either way since homophonic_anneal.py reads the sign stream in row order regardless
of the `line` column.

Usage:
  python3 shuffle_control.py cipher_codes.tsv --seed 1 --out shuffled_s1.tsv
  python3 shuffle_control.py cipher_codes.tsv --seed 1 --within-lines --out lineshuf_s1.tsv

Test: python3 shuffle_control.py --self-test
"""
import argparse
import csv
import random
import sys


def load_rows(path):
    with open(path, newline="") as f:
        r = csv.DictReader(f, delimiter="\t")
        rows = list(r)
        fieldnames = r.fieldnames
    return rows, fieldnames


def shuffle_full(rows, seed):
    signs = [row["sign"] for row in rows]
    random.Random(seed).shuffle(signs)
    out = []
    for row, sign in zip(rows, signs):
        new = dict(row)
        new["sign"] = sign
        out.append(new)
    return out


def shuffle_within_lines(rows, seed):
    rng = random.Random(seed)
    out = [dict(row) for row in rows]
    by_line = {}
    for i, row in enumerate(rows):
        by_line.setdefault(row.get("line", ""), []).append(i)
    for line, idxs in by_line.items():
        signs = [rows[i]["sign"] for i in idxs]
        rng.shuffle(signs)
        for i, sign in zip(idxs, signs):
            out[i]["sign"] = sign
    return out


def write_rows(rows, fieldnames, path):
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t")
        w.writeheader()
        w.writerows(rows)


def self_test():
    import tempfile, os

    rows = [
        {"line": "a", "position": "1", "sign": "5"},
        {"line": "a", "position": "2", "sign": "7"},
        {"line": "b", "position": "1", "sign": "9"},
        {"line": "b", "position": "2", "sign": "9"},
        {"line": "b", "position": "3", "sign": "3"},
    ]
    fieldnames = ["line", "position", "sign"]
    with tempfile.TemporaryDirectory() as d:
        src = os.path.join(d, "in.tsv")
        write_rows(rows, fieldnames, src)
        r2, fn2 = load_rows(src)
        assert fn2 == fieldnames

        full = shuffle_full(r2, seed=1)
        assert sorted(x["sign"] for x in full) == sorted(x["sign"] for x in rows)

        wl = shuffle_within_lines(r2, seed=1)
        assert sorted(x["sign"] for x in wl if x["line"] == "a") == sorted(
            x["sign"] for x in rows if x["line"] == "a"
        )
        assert sorted(x["sign"] for x in wl if x["line"] == "b") == sorted(
            x["sign"] for x in rows if x["line"] == "b"
        )
    print("self-test OK")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cipher", nargs="?")
    ap.add_argument("--seed", type=int)
    ap.add_argument("--within-lines", action="store_true", help="shuffle only inside each line, keeping line-level profile")
    ap.add_argument("--out")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        self_test()
        return

    if not args.cipher or args.seed is None or not args.out:
        ap.error("cipher, --seed and --out are required unless --self-test")

    rows, fieldnames = load_rows(args.cipher)
    if args.within_lines:
        out = shuffle_within_lines(rows, args.seed)
    else:
        out = shuffle_full(rows, args.seed)
    write_rows(out, fieldnames, args.out)
    print(f"wrote {args.out}: {len(out)} rows, seed {args.seed}, {'within-lines' if args.within_lines else 'full'} shuffle")


if __name__ == "__main__":
    sys.exit(main())
