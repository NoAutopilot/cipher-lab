#!/usr/bin/env python3
"""H286 (runner 10 session_0148wt8Aokh6aZEdJsXzYiZX, 29 Sept 2026): score the blind positional read of f.61 L04 (h286_reply.tsv). Pre-stated: 'H283's lead
stands' iff the line's last item (segment 4, largest x) is a word read as 'les' (case and accents ignored); the sign items join read_call_U's two L04
signs (LOOPBAR, OTHER) in order iff their count is 2. x as the reader gives it (H264 found a reader may give display px; the join uses order only).
Writes f61_positions_L04.tsv and f61positions_L04_result.txt.  [--check]"""
import csv, os, sys, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__))
def norm(s): return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower().strip()
def main():
    rows = [l.rstrip("\n").split("\t") for l in open(f"{HERE}/h286_reply.tsv") if l[0] == "L"]
    items = [r for r in rows if not (r[3] == "sign" and ("dot" in r[4].lower() or "punctuation" in r[4].lower()))]
    last = max(items, key=lambda r: (int(r[1]), int(r[2]))); last_word = norm(last[4]).split(" ")[0] if last[3] == "word" else "(a sign)"
    signs = [r for r in items if r[3] == "sign"]; U = [r for r in csv.DictReader(open(f"{HERE}/read_call_U.tsv"), delimiter="\t") if r["line"] == "L04"]
    rep = [f"L04: items {len(items)} (words {len(items) - len(signs)}, signs {len(signs)}); last item: segment {last[1]} x {last[2]} {last[3]} '{last[4]}'",
           f"clear words in order: {' | '.join(r[4] for r in items if r[3] == 'word')}",
           "read-out: " + ("H283's lead stands (last word 'les')" if last_word == "les" else f"H283's lead does not stand (last item '{last_word}')")]
    out = ["line\tpos\tclass\tsegment\tx\tprev\tnext\tdesc"]
    if len(signs) == len(U):
        rep.append(f"signs joined to read_call_U {len(U)}/{len(U)}")
        for p, r in enumerate(signs):
            k = items.index(r); prev = "edge" if k == 0 else items[k - 1][3]; nxt = "edge" if k == len(items) - 1 else items[k + 1][3]
            out.append(f"L04\t{p + 1}\t{U[p]['sign']}\t{r[1]}\t{r[2]}\t{prev}\t{nxt}\t{r[4]}")
    else: rep.append(f"signs {len(signs)} vs read_call_U {len(U)}: not joined")
    open(f"{HERE}/f61_positions_L04.tsv", "w").write("\n".join(out) + "\n"); txt = "\n".join(rep) + "\n"; p = f"{HERE}/f61positions_L04_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
