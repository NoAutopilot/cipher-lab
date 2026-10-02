#!/usr/bin/env python3
"""GAPS2-matignon-mayenne-1586 (2 Oct 2026, account-4): test a single-letter value for an unkeyed label
as a hypothesis, per leaf, with the spec's fr16 judge (tools/judge_plaintext.py), against a control that
CAN vary on the same axis (rule 3): the same label set to every other single letter of the key's alphabet
in turn, same positions, same N. The proposed value's rank among the 20 letters, and its margin over the
best other letter, are the result; a value that ranks first by less than the spread of the others is noise.

Hypotheses (from Daniel Bourdeau's HEAD NOTES.md glyph table, dbourdeau/cyphersolver targets/matignon1586,
snapshot sources/cyphersolver/2026-10-02/matignon1586/NOTES.md, CC BY 4.0): "⊐ (box) ... = u / v" and
"ꝉ (crossed t) = u / v". His HEAD key.json (same snapshot) keeps BOX as '+' (unidentified) and has no row
for our label T, so these are his table's values, not his key's: grade M at most. Whether our ASCII label T
is his ꝉ is not established (T= is m/mm in both keys); BOX is his own label.

Letters per line are built exactly as judge_leaves.py / reading_letters.txt build them (first alternative of
an M value, word codes expanded, U/'*'/'+' dropped), from reading_tokens.tsv, with the hypothesis label
overridden. Output: openings/hypothesis_judge.tsv (one row per hypothesis x leaf x letter) and a summary.

Usage (from the repository root): python3 ciphers/matignon-mayenne-1586/hypothesis_judge.py [--check]
"""
import argparse, csv, json, sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from judge_plaintext import NgramModel, fold, read_corpus  # noqa: E402

SPEC = ROOT / "specs" / "matignon-mayenne-1586.json"
LETTERS = list("abcdefghilmnopqrstuy")
HYPOTHESES = {"BOX": "u", "T": "u"}  # label -> Bourdeau's table value (u/v folded to u)


def tokens():
    per = defaultdict(lambda: defaultdict(list))  # leaf -> line -> [(sign, value)]
    with open(HERE / "reading_tokens.tsv", encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            per[r["line"].split("-")[0]][r["line"]].append((r["sign"], r["value"]))
    return per


def letters_for(lines, label=None, value=None):
    out = []
    for toks in lines.values():
        for sign, v in toks:
            if label is not None and sign == label:
                out.append(value); continue
            if v in ("?", "*", "+", ""):
                continue
            out.append(v.split("|")[0])
    return fold("".join(out))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=str(HERE / "openings"))
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    spec = json.loads(SPEC.read_text(encoding="utf-8"))
    model = NgramModel([read_corpus(ROOT / p) for p in spec["judge"]["corpora"]])
    per = tokens()
    rows, summary = [], []
    for label, proposed in HYPOTHESES.items():
        counts = {leaf: sum(1 for ls in lines.values() for s, _ in ls if s == label) for leaf, lines in per.items()}
        targets = [leaf for leaf, n in counts.items() if n >= 5] + ["ALL"]
        for leaf in targets:
            if leaf == "ALL":
                base = lambda lab=None, val=None: "".join(letters_for(l, lab, val) for l in per.values())
                n_label = sum(counts.values())
            else:
                base = lambda lab=None, val=None, L=per[leaf]: letters_for(L, lab, val)
                n_label = counts[leaf]
            b = base(); base_score = model.score(b)
            scores = {}
            for x in LETTERS:
                s = base(label, x)
                scores[x] = model.score(s)
                rows.append({"label": label, "leaf": leaf, "n_label": n_label, "N": len(s), "letter": x,
                             "score": round(scores[x], 4), "proposed": x == proposed})
            ranked = sorted(scores, key=scores.get, reverse=True)
            others = [scores[x] for x in LETTERS if x != proposed]
            summary.append({"label": label, "leaf": leaf, "n_label": n_label, "N_base": len(b),
                            "base_score_dropped": round(base_score, 4), "proposed": proposed,
                            "proposed_score": round(scores[proposed], 4),
                            "rank_of_proposed": ranked.index(proposed) + 1, "best_letter": ranked[0],
                            "best_score": round(scores[ranked[0]], 4),
                            "second_letter": ranked[1], "second_score": round(scores[ranked[1]], 4),
                            "others_max": round(max(others), 4), "others_mean": round(sum(others) / len(others), 4),
                            "others_min": round(min(others), 4),
                            "margin_over_best_other": round(scores[proposed] - max(others), 4),
                            "top5": " ".join(f"{x}:{scores[x]:.3f}" for x in ranked[:5])})
    out = Path(a.out); out.mkdir(exist_ok=True)
    tsv, summ = out / "hypothesis_judge.tsv", out / "hypothesis_judge_summary.tsv"
    new_rows = [{k: str(v) for k, v in r.items()} for r in rows]
    new_summ = [{k: str(v) for k, v in r.items()} for r in summary]
    if a.check:
        old = list(csv.DictReader(open(tsv, encoding="utf-8"), delimiter="\t")) if tsv.exists() else None
        olds = list(csv.DictReader(open(summ, encoding="utf-8"), delimiter="\t")) if summ.exists() else None
        if old != new_rows or olds != new_summ:
            print("STALE: hypothesis_judge*.tsv differ from a fresh run", file=sys.stderr); sys.exit(1)
        print("hypothesis_judge.tsv and summary are current"); return
    for path, data in ((tsv, new_rows), (summ, new_summ)):
        with open(path, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(data[0].keys()), delimiter="\t"); w.writeheader(); w.writerows(data)
    for r in summary:
        print("\t".join(f"{k}={v}" for k, v in r.items() if k not in ("top5",)), "|", r["top5"])


if __name__ == "__main__":
    main()
