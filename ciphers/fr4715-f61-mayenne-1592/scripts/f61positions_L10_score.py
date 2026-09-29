#!/usr/bin/env python3
"""H264 (runner 10 session_0148wt8Aokh6aZEdJsXzYiZX, 29 Sept 2026): join the blind positional read of f.61 L10 (h264_reply.tsv, from the sheet B ruler
sheet) to fragment_L10.tsv's 13 signs (the run after the clear words 'pas paresseux si', to the end of the line). Rule, fixed before the call: take the
sign items after the LAST clear word in the reply (dot/punctuation items dropped, as f61positions_score.py); join in order only if their count is 13,
else report and do not join. Writes f61_positions_L10.tsv (line, pos, class, segment, x, prev, next, x_reply, desc) and f61positions_L10_result.txt.
Scale note, added after the reply (29 Sept 2026): the reader gave x in the half-size sheet's display pixels, not the ruler's labels -- its three a-shaped
signs sit at 720 / 490 / 920 where H63's sheet-B read of the same marks gave 1440 / 985 / 1820 (ratio 2.00, 2.01, 1.98) -- so `x` is stored as 2 x the
reply's value (sheet px, comparable with f61_positions_all.tsv) and the reply's own value is kept in `x_reply`; the join by count does not use x.  [--check]"""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
def main():
    rows = [l.rstrip("\n").split("\t") for l in open(f"{HERE}/h264_reply.tsv") if l[0] == "L"]
    items = [r for r in rows if not (r[3] == "sign" and ("dot" in r[4].lower() or "punctuation" in r[4].lower()))]
    last_word = max((k for k, r in enumerate(items) if r[3] == "word"), default=-1)
    run = [k for k, r in enumerate(items) if r[3] == "sign" and k > last_word]
    frag = [r for r in csv.DictReader((l for l in open(f"{HERE}/fragment_L10.tsv") if not l.startswith("#")), delimiter="\t")]
    words = [r[4] for r in items if r[3] == "word"]
    rep = [f"L10: clear words read: {' '.join(words)}; signs after the last word {len(run)} vs fragment {len(frag)}; signs before it {sum(1 for k, r in enumerate(items) if r[3] == 'sign' and k <= last_word)}"]
    out = ["line\tpos\tclass\tsegment\tx\tprev\tnext\tx_reply\tdesc"]
    if len(run) == len(frag):
        rep.append("L10: joined")
        for p, k in enumerate(run):
            prev = "edge" if k == 0 else items[k - 1][3]; nxt = "edge" if k == len(items) - 1 else items[k + 1][3]
            out.append(f"L10\t{p + 1}\t{frag[p]['class']}\t{items[k][1]}\t{2 * int(items[k][2])}\t{prev}\t{nxt}\t{items[k][2]}\t{items[k][4]}")
        for cls in ("CA", "C6", "SBS", "PHI"):
            c = [l.split("\t") for l in out[1:] if l.split("\t")[2] == cls]; b = sum(1 for r in c if "word" in (r[5], r[6]))
            rep.append(f"{cls}: {len(c)} joined, {b} next to a clear word")
    else: rep.append("L10: count mismatch -> not joined")
    open(f"{HERE}/f61_positions_L10.tsv", "w").write("\n".join(out) + "\n"); txt = "\n".join(rep) + "\n"; p = f"{HERE}/f61positions_L10_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
