#!/usr/bin/env python3
"""H297 (runner 10 session_0148wt8Aokh6aZEdJsXzYiZX, 29 Sept 2026): score the blind positional read of sheet B's L05 (h297_reply.tsv). Rules fixed before
the call (PROMPTS H297): words before the first sign item; 'begins with clear text' iff >= 1 such word; 'runner's read stands' iff the last of them,
ignoring a bare 'a', is 'sont'; sign items joined to read_call_A's 18 L05 signs iff 18 (bare a as a word) or 19 (edge a as a sign -> pos 0, CA_edge).
Writes f61_positions_L05B.tsv and f61positions_L05B_result.txt.  [--check]"""
import csv, os, sys, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__))
def norm(s): return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower().strip()
def main():
    rows = [l.rstrip("\n").split("\t") for l in open(f"{HERE}/h297_reply.tsv") if l[0] == "L"]
    items = [r for r in rows if not (r[3] == "sign" and ("dot" in r[4].lower() or "punctuation" in r[4].lower()))]
    first = next((k for k, r in enumerate(items) if r[3] == "sign"), len(items))
    words = [norm(r[4]).split(" ")[0] for r in items[:first] if r[3] == "word"]; core = [w for w in words if w != "a"]
    A = [r for r in csv.DictReader(open(f"{HERE}/read_call_A.tsv"), delimiter="\t") if r["line"] == "L05"]
    signs = [k for k, r in enumerate(items) if r[3] == "sign"]
    rep = [f"words before the first sign: {' '.join(words) or '(none)'}",
           "read-out (a): " + ("the line begins with clear text before the run" if words else "the run opens the line"),
           "read-out (b): " + ("the runner's read stands (last word 'sont')" if core and core[-1] == "sont" else f"the runner's read does not stand (last word '{core[-1] if core else '(none)'}')"),
           f"signs {len(signs)} vs read_call_A {len(A)}"]
    out = ["line\tpos\tclass\tsegment\tx_reply\tprev\tnext\tdesc"]
    off = 1 if len(signs) == len(A) + 1 else (0 if len(signs) == len(A) else None)
    if off is None: rep.append("not joined (count)")
    else:
        rep.append("joined" + (" (edge a as pos 0, CA_edge)" if off else ""))
        for p, k in enumerate(signs):
            cls = "CA_edge" if (off and p == 0) else A[p - off]["symbol"] + ":" + A[p - off]["marks"][:30]
            prev = "edge" if k == 0 else items[k - 1][3]; nxt = "edge" if k == len(items) - 1 else items[k + 1][3]
            out.append(f"L05\t{p + 1 - off}\t{cls}\t{items[k][1]}\t{items[k][2]}\t{prev}\t{nxt}\t{items[k][4]}")
    open(f"{HERE}/f61_positions_L05B.tsv", "w").write("\n".join(out) + "\n"); txt = "\n".join(rep) + "\n"; p = f"{HERE}/f61positions_L05B_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
