#!/usr/bin/env python3
"""AX-5797 (26 Sept 2026) control for the 5797-under-key.tsv positive-control runs.

Per CLAUDE.md rule 3 / the AX-5797 brief step 3: a run "reads" only if its decode is
German-consistent with Groen's own frame AND 20 shuffled copies of key.tsv do not
reproduce the same word at the same position anywhere near as often. This checks the
two positive-control runs on p6 (spot4's "zeuget" spelling and the neighbouring "abso-"
fragment) -- the six missing-subject spot runs are not included here because every one
of their codes is simply absent from key.tsv (U-graded, "not in table"), so a shuffle of
key.tsv's *existing* codes cannot make them legible either way; that is reported as a
gap in key.tsv's coverage, not tested by a shuffle.

Shuffle model: permute the VALUE column among codes in the 1-120 homophonic block only
(preserves the block's letter multiset; excludes the >=121 NULL/nomenclature rows, which
are a different subsystem). Same permutation applied consistently within one shuffle.
20 shuffles, seeded 1..20.

Usage: python3 control_5797.py
"""
import csv
import random

KEY_PATH = "key.tsv"
RUNS = {
    "p6_spot4_zeuget": {"codes": ["58", "85", "38", "95", "82", "35"], "target": "zeuget"},
    "p6_control_abso": {"codes": ["62", "66", "26", "6"], "target": "abso"},
    "p7_spot6_mit": {"codes": ["117", "103", "33"], "target": "mit"},
    "p5_control_election": {"codes": ["82", "112", "83", "72", "32", "102", "10", "2"], "target": "election"},
}


def load_key(path):
    rows = []
    with open(path) as f:
        r = csv.DictReader(f, delimiter="\t")
        for row in r:
            rows.append(row)
    return rows


def decode(codes, value_by_code):
    out = []
    for c in codes:
        v = value_by_code.get(c)
        if v is None or v == "NULL" or v == "?":
            out.append("_")
        else:
            out.append(v)
    return "".join(out)


def main():
    rows = load_key(KEY_PATH)
    block = [row for row in rows if row["code"].isdigit() and 1 <= int(row["code"]) <= 120]
    other = [row for row in rows if not (row["code"].isdigit() and 1 <= int(row["code"]) <= 120)]

    real_value_by_code = {row["code"]: row["value"] for row in rows}
    print("REAL KEY:")
    for name, spec in RUNS.items():
        decoded = decode(spec["codes"], real_value_by_code)
        hit = decoded == spec["target"]
        print(f"  {name}: {spec['codes']} -> '{decoded}' (target '{spec['target']}') {'HIT' if hit else 'no'}")

    print("\n20 SHUFFLED KEYS (homophonic block 1-120 only, values permuted):")
    hits = {name: 0 for name in RUNS}
    for seed in range(1, 21):
        rng = random.Random(seed)
        values = [row["value"] for row in block]
        shuffled_values = values[:]
        rng.shuffle(shuffled_values)
        shuf_value_by_code = {row["code"]: sv for row, sv in zip(block, shuffled_values)}
        for row in other:
            shuf_value_by_code[row["code"]] = row["value"]
        line = []
        for name, spec in RUNS.items():
            decoded = decode(spec["codes"], shuf_value_by_code)
            hit = decoded == spec["target"]
            if hit:
                hits[name] += 1
            line.append(f"{name}='{decoded}'{'*HIT*' if hit else ''}")
        print(f"  seed {seed}: " + " ".join(line))

    print("\nSummary (hits out of 20 shuffles):")
    for name, spec in RUNS.items():
        print(f"  {name} (target '{spec['target']}'): {hits[name]}/20")


if __name__ == "__main__":
    main()
