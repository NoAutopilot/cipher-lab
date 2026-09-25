#!/usr/bin/env python3
"""Diff meye/blind_pass.tsv against ciphertext.tsv (the settled two-pass reading) and
exceptions.tsv (the five M-graded 14-vs-19 corrections), for LANE R7 R7-MEYE's blind
re-transcription of espagnol142-mercy-1648 lines r06, r14, r16, r17, v04, v07.

Writes meye/compare.tsv. Reads only files in the target folder; no network.
"""
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINES = ["r06", "r14", "r16", "r17", "v04", "v07"]

EXCEPTION_POSITIONS = {
    ("r06", 14): "14",
    ("r14", 7): "14",
    ("r16", 3): "14",
    ("r16", 6): "14",
    ("r17", 5): "14",
}


def load_blind(path):
    rows = {}
    with open(path, newline="") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            key = (row["line"], int(row["position"]))
            rows[key] = row
    return rows


def load_ciphertext(path):
    rows = {}
    with open(path, newline="") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            if row["line"] in LINES:
                key = (row["line"], int(row["position"]))
                rows[key] = row
    return rows


def strip_dot(sign):
    return sign.rstrip(".").rstrip(":").strip()


def main():
    blind = load_blind(ROOT / "meye" / "blind_pass.tsv")
    settled = load_ciphertext(ROOT / "ciphertext.tsv")

    out_rows = []
    agree = disagree = unreadable = 0
    for line in LINES:
        blind_positions = sorted(p for (l, p) in blind if l == line)
        settled_positions = sorted(p for (l, p) in settled if l == line)
        count_note = ""
        if len(blind_positions) != len(settled_positions):
            count_note = (
                f"COUNT MISMATCH: blind={len(blind_positions)} "
                f"settled={len(settled_positions)}; aligned by raw position from line start, "
                "not by plain-word anchor (none present, all-numeral lines)"
            )
        for pos in blind_positions:
            b = blind[(line, pos)]
            s = settled.get((line, pos))
            b_sign = strip_dot(b["sign"])
            s_sign = strip_dot(s["sign"]) if s else None
            if s is None:
                status = "unreadable"
                unreadable += 1
            elif b_sign == "1?" or b["confidence"] == "L":
                status = "unreadable"
                unreadable += 1
            elif b_sign == s_sign:
                status = "agree"
                agree += 1
            else:
                status = "disagree"
                disagree += 1
            out_rows.append(
                [line, pos, b["sign"], b["confidence"], s_sign if s else "", status, count_note]
            )
            count_note = ""

    with open(ROOT / "meye" / "compare.tsv", "w", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(["line", "position", "blind_sign", "blind_conf", "settled_sign", "status", "note"])
        w.writerows(out_rows)

    total = agree + disagree + unreadable
    print(f"overall: {agree}/{total} agree, {disagree}/{total} disagree, {unreadable}/{total} unreadable")

    print("\nfive exceptions.tsv 14-vs-19 positions:")
    for (line, pos), settled_value in EXCEPTION_POSITIONS.items():
        b = blind.get((line, pos))
        b_sign = strip_dot(b["sign"]) if b else "?"
        agrees_with_exception = b_sign == settled_value
        print(f"  {line} pos {pos}: blind read {b_sign!r} (conf {b['confidence']}), "
              f"exceptions.tsv says {settled_value!r} -> "
              f"{'AGREE' if agrees_with_exception else 'DISAGREE'}")


if __name__ == "__main__":
    main()
