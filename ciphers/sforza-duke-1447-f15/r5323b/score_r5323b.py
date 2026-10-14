#!/usr/bin/env python3
"""SFZ-R5323B scorer (../PREREG-SFZ-R5323B.md). Reader files: pass{A,B}_{G1,G2}_b{1,2}.tsv, rows sheet<TAB>letter<TAB>labels.
A pass's column = union of its G1 and G2 calls. S = C pairs listed in both passes. Strict exact labels ('^' stripped);
'a/b?' tokens counted only in the loose sensitivity line.  usage: score_r5323b.py [DIR]"""
import glob, os, random, sys

PAIRS = [("O", "a"), ("Y", "o"), ("N8", "d"), ("N2", "h"), ("N11", "r"), ("ce", "r"), ("cu", "n")]


def load(d, p, loose):
    cols = {}
    for path in sorted(glob.glob(os.path.join(d, f"pass{p}_G*_b*.tsv"))):
        for line in open(path, encoding="utf-8"):
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 2 or not parts[0].startswith("sheet_"):
                continue
            sheet, letter, labs = parts[0], parts[1].strip().lower(), (parts[2] if len(parts) > 2 else "")
            s = cols.setdefault(sheet, {}).setdefault(letter, set())
            for t in labs.split():
                t = t.rstrip("^")
                if "/" in t and t.endswith("?"):
                    if loose:
                        s.update(x.rstrip("^") for x in t[:-1].split("/"))
                    continue
                s.add(t)
    return cols


def score(c):
    return sum(1 for lab, let in PAIRS if lab in c.get(let, set()))


def hits(c):
    return [f"{lab}={let}" for lab, let in PAIRS if lab in c.get(let, set())]


def main(d):
    smap = {l.split("\t")[0]: l.split("\t")[1] for l in open(os.path.join(d, "sheet_map.tsv")).read().split("\n")[1:] if l}
    target = [k for k, v in smap.items() if v == "R5323"][0]
    for loose in (False, True):
        tag = "loose" if loose else "strict"
        A, B = load(d, "A", loose), load(d, "B", loose)
        agreed = {sh: {k: A[sh][k] & B[sh].get(k, set()) for k in A.get(sh, {})} for sh in smap if sh in A and sh in B}
        res = {}
        for sh in sorted(smap):
            ag = agreed.get(sh, {})
            res[sh] = score(ag)
            print(f"[{tag}] {sh} {smap[sh]}: S_A={score(A.get(sh, {}))} S_B={score(B.get(sh, {}))} "
                  f"S_agreed={res[sh]} {hits(ag)}{'  <- target' if sh == target else ''}")
        s = res[target]
        mx = max(v for k, v in res.items() if k != target)
        ag = agreed.get(target, {})
        letters = sorted(ag)
        rng = random.Random(5323)
        ge = 0
        for _ in range(10000):
            perm = letters[:]
            rng.shuffle(perm)
            ge += score({perm[i]: ag[letters[i]] for i in range(len(letters))}) >= s
        p = ge / 10000
        ok = s >= 4 and s > mx and p <= 0.01
        print(f"[{tag}] R5323 S_agreed={s}  max control={mx}  shuffled p={p:.4f}  GATE {'PASS' if ok else 'FAIL'}"
              f"{' (sensitivity only)' if loose else ''}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__)))
