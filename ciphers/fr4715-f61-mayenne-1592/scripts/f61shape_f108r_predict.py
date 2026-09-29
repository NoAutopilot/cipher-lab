#!/usr/bin/env python3
"""H249 (runner 9 session_012NTadgrCBftz3oRtgw5jFu, 29 Sept 2026), script-only: H120's pre-registered prediction of f.108r L04-L06 (H108 draft; the 4-gram
beam, scripts/f61hash4_108r.resolve, fr16, width 400) re-run with the cells set BY SHAPE at each position instead of by pass code, committed before any
person's read of the rows' period gloss (ASKS 88):
 4-family (H216's blind bowl answers, family/h216_bowl_positions.tsv): bowl -> c/p, no bowl -> a/n, 'n' -> the code's H120 cell;
 HASH4 (H212's blind forms, family/h212_items.tsv + passes/h212_sort.tsv, matched to the draft by segment and x): 4-head A -> d/q (period d/q on three
 leaves), looped B -> i/x (H119/H120's HASH4 map; no period value for the looped form, H227/H241 -- flagged); every other class as H120.
 Output scripts/f61shape_f108r_prediction.txt, one row per draft position: class, shape, pair, beam letter; the tail lists the positions where this
 prediction's pair differs from H120's.  [--check]"""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); F = os.path.abspath(f"{HERE}/../family"); sys.path.insert(0, HERE)
import f61hash4_108r as H
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def main():
    C = dict(H.J.cells(), HASH4="i/x"); L = H.J.lines("f108r_L04_L06_h108")
    bowl = {(r["line"], int(r["position"])): r["bowl"] for r in rd(f"{F}/h216_bowl_positions.tsv")}
    grp = {f"T{int(r['tile'].split()[-1]):02d}": r["group"].strip() for r in rd(f"{F}/passes/h212_sort.tsv")}
    hform = {(r["line"], r["segment"], int(r["x_px"])): grp[r["item"]] for r in rd(f"{F}/h212_items.tsv") if r["leaf"] == "108r"}
    draft = {(r["line"], int(r["position"])): r for r in rd(f"{HERE}/f61recon108r_draft.tsv")}
    out = ["# H249 prediction (29 Sept 2026): f.108r L04-L06, H108 draft positions, beam letter with cells set by blind shape (see docstring); '.' = outside the map",
           "line\tposition\tclass\tshape\tpair\tbeam"]; diff = []
    for line, seq in L.items():
        pairs = {}
        for k, c in enumerate(seq):
            pos = k + 1; sh = "-"; cell = C.get(c)
            if c in ("4TRI", "C43", "4STEM", "4PI") and (line, pos) in bowl and bowl[(line, pos)] in ("yes", "no"):
                sh = "bowl" if bowl[(line, pos)] == "yes" else "no-bowl"; cell = "c/p" if sh == "bowl" else "a/n"
                if c == "4PI": sh, cell = "4PI(" + sh + ")", C.get(c)   # 4PI on f.108r is the 4-head hash (H239): keep d/q
            if c == "HASH4":
                d = draft.get((line, pos)); f = hform.get((line, d["segment"], int(d["x_px"]))) if d else None
                if f: sh = "4-head" if f == "A" else "looped"; cell = "d/q" if f == "A" else "i/x"
            if cell: pairs[k] = (cell, sh)
            if cell != C.get(c): diff.append(f"{line} {pos} {c} ({sh}): H120 {C.get(c)} -> {cell}")
        idx = sorted(pairs); prs = [tuple(H.jp.fold(x) for x in pairs[k][0].split("/")) for k in idx]
        s, _, _ = H.resolve(prs); m = dict(zip(idx, s))
        for k, c in enumerate(seq): out.append(f"{line}\t{k + 1}\t{c}\t{pairs.get(k, ('', '-'))[1]}\t{pairs.get(k, ('', ''))[0]}\t{m.get(k, '.')}")
    out.append("# pairs changed from H120: " + ("; ".join(diff) if diff else "none"))
    txt = "\n".join(out) + "\n"; p = f"{HERE}/f61shape_f108r_prediction.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(out[-1])
if __name__ == "__main__": main()
