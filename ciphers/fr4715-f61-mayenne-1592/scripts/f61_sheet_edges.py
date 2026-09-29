#!/usr/bin/env python3
"""H296 (runner 10 session_0148wt8Aokh6aZEdJsXzYiZX, 29 Sept 2026): a guard against the H283 error. images/regen_f61r_sheets.sh builds each span sheet
f61sheet_L*.jpg from a KEEP list of native segments (L01 [4,5], L03 [1,2,3], L05 [2,3,4], L07 [3,4,5], L08 [1,2], L11 [1,2]); a sheet whose first kept
segment is not 1 does not show the line's start, and one whose last is not the line's last segment does not show its end. Writes f61_sheet_edges.tsv:
one row per span-sheet segment (sheet, sheet_segment, native_segment, first_of_line, last_of_line) and, for every 'edge' row of f61_positions_all.tsv /
f61_positions_L10.tsv, whether that edge is the LINE's (true start/end) or only the SHEET's. The native segment count per line is read from the
f61s_L*_s*.jpg files if present, else taken as 5 (the tool spreads 4-5 segments of 900 px over 3320 px; see the regen script) and flagged.  [--check]"""
import csv, glob, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); IM = os.path.abspath(f"{HERE}/../images")
KEEP = {}
for l in open(f"{IM}/regen_f61r_sheets.sh"):
    m = re.search(r'keep = (\{.*\})', l)
    if m: KEEP = eval(m.group(1))
rows = ["sheet\tsheet_segment\tnative_segment\tfirst_of_line\tlast_of_line"]; edge = {}
for L, segs in KEEP.items():
    n = len(glob.glob(f"{IM}/f61s_{L}_s*.jpg")) or 5; flag = "" if glob.glob(f"{IM}/f61s_{L}_s*.jpg") else " (assumed 5)"
    for k, s in enumerate(segs, 1):
        rows.append(f"f61sheet_{L}\t{k}\t{s}\t{'yes' if s == 1 else 'no'}\t{'yes' if s == n else 'no'}{flag}")
        edge[(L, k)] = (s == 1, s == n)
rows.append(""); rows.append("line\tpos\tclass\tsegment\tprev\tnext\tedge_kind")
for f in ("f61_positions_all.tsv", "f61_positions_L10.tsv"):
    for r in csv.DictReader(open(f"{HERE}/{f}"), delimiter="\t"):
        if "edge" not in (r["prev"], r["next"]): continue
        L, k = r["line"], int(r["segment"])
        if L == "L10": kind = "line (sheet B holds the whole line)"
        else:
            first, last = edge.get((L, k), (None, None))
            kind = ("LINE start" if r["prev"] == "edge" and first else "SHEET edge only (not the line's start)" if r["prev"] == "edge" else "LINE end" if last else "SHEET edge only (not the line's end)")
        rows.append(f"{L}\t{r['pos']}\t{r['class']}\t{k}\t{r['prev']}\t{r['next']}\t{kind}")
out = "\n".join(rows) + "\n"; p = f"{HERE}/f61_sheet_edges.tsv"
if "--check" in sys.argv:
    ok = os.path.exists(p) and open(p).read() == out; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(p, "w").write(out); print(out, end="")
