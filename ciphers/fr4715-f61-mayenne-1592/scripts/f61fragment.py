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
# H51 (28 Sept 2026, runner session_01J8hunWPcE7QYcpCx59CUHV): H26's blind sort (scripts/f61qo.py, read_call_QO.tsv, 38/38,
# P < 0.0005) put L10 positions 6 and 11 -- the two-loops-side-by-side form audit 1 questioned -- in the b/o group, so their
# cell is SBS b/o (grade S with that control), not PHI e/r; the H16 judge's letter for them is withdrawn (it chose within
# e/r), the letters within every pair stay M. The pre-H51 file is in git history (commit 310c85e5 and earlier).
import f61qo2
SBS_POS = {pos for (line, pos), g in f61qo2.G.items() if line == "L10" and g == "G2"}
def signs(path):
    return [r["sign"] for r in csv.DictReader(open(f"{HERE}/{path}"), delimiter="\t") if r["line"] == "L10"]
def main():
    a, b = signs("passU1_classes.tsv"), signs("passU2_classes.tsv")
    assert a == b, ("the two blind passes differ on L10", a, b)
    verdict = next(r for r in csv.DictReader(open(f"{HERE}/f61judge_unmarked_verdict.tsv"), delimiter="\t") if r["label"] == "SET-13")
    resolved = verdict["reading"].split("|")[-1].strip()
    rows = []; k = 0
    for i, c in enumerate(a, 1):
        if c in CELLS and i in SBS_POS:
            k += 1   # the judge resolved this position under e/r; that letter is withdrawn
            rows.append((i, "SBS", "b/o", "", "S/M", "cell S (H26 blind sort: side-by-side pair = b/o 6/6, 38/38 overall, P < 0.0005), letter within the pair unresolved M (the H16 judge saw e/r here; withdrawn H51)"))
        elif c in CELLS:
            pair = CELLS[c]; letter = resolved[k]; k += 1
            assert letter in pair.split("/"), (c, pair, letter)
            rows.append((i, c, pair, letter, "S/M", "cell S (controlled map), letter within the pair M (judge)"))
        else:
            rows.append((i, c, "-", "", "S", "null (dash share > 0.5 on the known lines)"))
    assert k == len(resolved)
    seq = " ".join(f"[{r[2]}]" for r in rows if r[2] != "-")
    txt = ("# f.61r L10, after the clear words 'pas paresseux si' (both passes), run ends the line. 27 Sept 2026, campaign H16-H17; revised 28 Sept 2026, H51 (positions 6 and 11 = SBS b/o after H26).\n"
           "# 8 letter signs, cells S, letters within pairs M (two unresolved); 5 nulls. Pair sequence: " + seq + " -- the H16 judge's string '" + resolved + "' is withdrawn (it read positions 6 and 11 under e/r); no reading is claimed.\n"
           "pos\tclass\tcell\tletter\tgrade\tnote\n" + "".join("\t".join(map(str, r)) + "\n" for r in rows))
    res = f"{HERE}/fragment_L10.tsv"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt
        print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    main()
