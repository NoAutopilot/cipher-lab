#!/usr/bin/env python3
"""ARM-S2 step 3: score each of the 7 systems from symbol_match.tsv against
the reconciled top-12 shapes' mark counts (INVENTORY_reconciled.tsv).

Two numbers per system, both mark-count-weighted (not a flat per-category
average, since one shape covers 75 marks and another covers 2):
  shape_score = weighted fraction of exact/partial shape counterparts
                (yes=1.0, partial=0.5, no=0.0), weighted by each shape's
                mark count, over the total mark count of the 12 shapes (189).
  freq_score  = weighted fraction of "consistent" among the shapes that got
                ANY letter/sign assignment (yes or partial with a real
                letter judgement), weighted by mark count -- shapes marked
                "n-a" (not a letter claim: punctuation, a diacritic, a
                ligature, page furniture) are excluded from this second
                score's denominator, since there is nothing to test.
No network. Usage: python3 score_summary.py"""
import csv
import os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))


def load_counts():
    counts = {}
    path = os.path.join(HERE, "..", "INVENTORY_reconciled.tsv")
    with open(path, newline="") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            counts[row["id"]] = float(row["count"])
    return counts


def main():
    counts = load_counts()
    total = sum(counts.values())
    systems = defaultdict(list)
    path = os.path.join(HERE, "symbol_match.tsv")
    with open(path, newline="") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            systems[row["system"]].append(row)

    verdict_w = {"yes": 1.0, "partial": 0.5, "no": 0.0}
    freq_w = {"consistent": 1.0, "inconsistent": 0.0}

    print(f"{'system':<16}{'shape_score':<14}{'freq_score':<14}{'n_yes':<7}{'n_partial':<11}{'n_no':<6}")
    results = {}
    for system, rows in systems.items():
        shape_num = 0.0
        freq_num = 0.0
        freq_den = 0.0
        n = {"yes": 0, "partial": 0, "no": 0}
        for r in rows:
            c = counts[r["shape"]]
            v = r["verdict"]
            n[v] += 1
            shape_num += c * verdict_w[v]
            fc = r["freq_consistent"]
            if fc in freq_w:
                freq_den += c
                freq_num += c * freq_w[fc]
        shape_score = shape_num / total
        freq_score = (freq_num / freq_den) if freq_den else float("nan")
        results[system] = (shape_score, freq_score)
        print(f"{system:<16}{shape_score:<14.3f}{freq_score:<14.3f}{n['yes']:<7}{n['partial']:<11}{n['no']:<6}")

    print()
    ranked = sorted(results.items(), key=lambda kv: -kv[1][0])
    print("Ranked by shape_score (highest first):")
    for system, (s, f) in ranked:
        print(f"  {system}: shape_score={s:.3f} freq_score={f:.3f}")

    taylor = results.get("Taylor1786")
    pitman = results.get("Pitman_CONTROL")
    candidates = {k: v for k, v in results.items() if k not in ("Taylor1786", "Pitman_CONTROL")}
    print()
    if taylor and pitman:
        best_candidate = max(candidates.items(), key=lambda kv: kv[1][0]) if candidates else None
        print(f"Taylor1786 (known negative): shape_score={taylor[0]:.3f}")
        print(f"Pitman_CONTROL:               shape_score={pitman[0]:.3f}")
        if best_candidate:
            print(f"Best untested candidate ({best_candidate[0]}): shape_score={best_candidate[1][0]:.3f}")
            if taylor[0] >= best_candidate[1][0]:
                print("VERDICT: Taylor scores AT OR ABOVE the best candidate -- this finer method still "
                      "has no resolving power to pick a system by shape_score alone; a candidate can only "
                      "be called identified if it clears Taylor by a real margin AND has a frequency-"
                      "consistent profile (rule 3).")
            else:
                print("Taylor scores below the best candidate -- shape_score alone has some resolving "
                      "power here; check freq_score and Pitman's position before calling anything identified.")
        if pitman[0] > min(v[0] for v in candidates.values()):
            print("NOTE: Pitman (control) does NOT score lowest of all systems tested -- check which "
                  "candidate(s) it beats.")


if __name__ == "__main__":
    main()
