#!/usr/bin/env python3
"""F61 fragment (campaign steps H16-H17, 27 Sept 2026): the controlled 8-letter fragment on f.61r line L10, regenerated from
the two blind passes, the cell map and the judge's verdict (rule 7: exits non-zero when scripts/fragment_L10.tsv is stale).

Inputs: scripts/passU1_classes.tsv and passU2_classes.tsv (two independent blind Opus reads of images/f61sheetB_L10.jpg
with the shape atlas; identical on L10, H17), scripts/f61crib4_map.tsv with H4's dash-share null rule (the 9 cells of
scripts/f61judge.py CELLS), and scripts/f61judge_unmarked_verdict.tsv (the blind judge's resolution of each pair, H16).
Grades (CLAUDE.md rule 4): a letter sign's CELL is S (cryptanalytic, controls: H15b cell fit 42/55 vs permuted max 0.400;
judge rank 1 of 21 on known lines and 1 of 21 on this run); the choice WITHIN the pair is M (the judge's, unchecked);
a null is S (dash share > 0.5 on the known lines). Nothing here is H or C: this is a cryptanalytic result, a fragment
of one run after the clear words 'pas paresseux si', not a reading of the letter.

  python3 scripts/f61fragment.py [--check]   (from the target folder)
"""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from f61judge import CELLS
def signs(path):
    return [r["sign"] for r in csv.DictReader(open(f"{HERE}/{path}"), delimiter="\t") if r["line"] == "L10"]
def main():
    a, b = signs("passU1_classes.tsv"), signs("passU2_classes.tsv")
    assert a == b, ("the two blind passes differ on L10", a, b)
    verdict = next(r for r in csv.DictReader(open(f"{HERE}/f61judge_unmarked_verdict.tsv"), delimiter="\t") if r["label"] == "SET-13")
    resolved = verdict["reading"].split("|")[-1].strip()
    rows = []; k = 0
    for i, c in enumerate(a, 1):
        if c in CELLS:
            pair = CELLS[c]; letter = resolved[k]; k += 1
            assert letter in pair.split("/"), (c, pair, letter)
            rows.append((i, c, pair, letter, "S/M", "cell S (controlled map), letter within the pair M (judge)"))
        else:
            rows.append((i, c, "-", "", "S", "null (dash share > 0.5 on the known lines)"))
    assert k == len(resolved)
    txt = ("# f.61r L10, after the clear words 'pas paresseux si' (both passes), run ends the line. 27 Sept 2026, campaign H16-H17.\n"
           "# 8 letters, all S/M; 5 nulls. Resolved fragment: " + resolved + "\n"
           "pos\tclass\tcell\tletter\tgrade\tnote\n" + "".join("\t".join(map(str, r)) + "\n" for r in rows))
    res = f"{HERE}/fragment_L10.tsv"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt
        print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    main()
