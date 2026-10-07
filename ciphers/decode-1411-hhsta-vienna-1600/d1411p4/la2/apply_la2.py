#!/usr/bin/env python3
"""D07-D1411: apply the per-number tile re-read (PREREG-LA2.md item 5) to numbers.tsv -> la2/numbers_la2.tsv, la2/applied.tsv.
Re-reads: la2/reread_pilot.tsv + la2/reread_full.tsv (tile, shapes, conf). X -> 4, R -> 5, O -> committed digit. A firm re-read
(no '?') whose value equals pass A's or pass B's token settles the number at that value; otherwise UNSETTLED, committed value kept.
A settled number whose value changes is graded M.
  python3 d1411p4/la2/apply_la2.py [--check]"""
import csv, os, sys
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.dirname(H)
rd = lambda f: list(csv.DictReader(open(f), delimiter="\t"))
T = {f"{r['line']}_{r['pos']}": r for r in rd(os.path.join(P, "la", "tiles.tsv"))}
R = {}
for f in ("reread_pilot.tsv", "reread_full.tsv"):
    for r in rd(os.path.join(H, f)):
        R[r["tile"]] = r
app = [["tile", "A", "B", "C", "mask", "shapes", "conf", "reread", "status", "new"]]; new = {}
for k, t in T.items():
    r = R.get(k); sh = (r or {}).get("shapes", "?").strip().upper(); C = t["C"]; m = t["mask"]
    firm = r is not None and "?" not in sh and len(sh) == m.count("#")
    val = None
    if firm:
        it = iter(sh); val = "".join({"X": "4", "R": "5", "O": C[i]}[next(it)] if ch == "#" else ch for i, ch in enumerate(m))
    st = "settled" if firm and val in (t["A"], t["B"]) else ("unsettled-firm" if firm else "unsettled-?")
    nv = val if st == "settled" else C
    new[(t["line"], t["pos"])] = nv
    app.append([k, t["A"], t["B"], C, m, sh, (r or {}).get("conf", ""), val or "", st, nv])
out = []
rows = rd(os.path.join(P, "numbers.tsv")); cols = list(rows[0].keys())
for r in rows:
    k = (r["line"], r["pos"])
    if k in new and new[k] != r["token"].rstrip("?"):
        r = dict(r); r["token"] = new[k]; r["grade"] = "M"; r["note"] = (r["note"] + ";" if r["note"] else "") + "la2"
    out.append(r)
txt = "\t".join(cols) + "\n" + "".join("\t".join(r[c] for c in cols) + "\n" for r in out)
atxt = "".join("\t".join(x) + "\n" for x in app)
if "--check" in sys.argv:
    ok = open(os.path.join(H, "numbers_la2.tsv")).read() == txt and open(os.path.join(H, "applied.tsv")).read() == atxt
    print("la2 apply", "current" if ok else "STALE"); sys.exit(0 if ok else 1)
open(os.path.join(H, "numbers_la2.tsv"), "w").write(txt); open(os.path.join(H, "applied.tsv"), "w").write(atxt)
s = [x[8] for x in app[1:]]
print({k: s.count(k) for k in set(s)}, "changed:", sum(1 for x in app[1:] if x[9] != x[3]))
