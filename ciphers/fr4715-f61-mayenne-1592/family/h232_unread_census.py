#!/usr/bin/env python3
"""H232 (runner 9 session_012NTadgrCBftz3oRtgw5jFu, 29 Sept 2026), script-only, written before the run: where do f.61's unread classes (CA 10, C6 8,
LOOPBAR 4, CROSS 2, LL 1; f61_decode_period_v4_frac0.1_sbs.tsv) occur on the other leaves on disk? Counts per leaf from each reconciled draft
(passes/rec*/ciphertext_draft.tsv) and, where an alignment exists (passes/*_align_v4.tsv else *_align.tsv), the letters placed at them (the f.106r and
f.124r alignments are held/conditional; f.108vg's are clear-word glosses). f.176r/v drafts are not in rec* form and are not counted. Descriptive,
to aim the next shape step at a leaf that holds each class.  python3 h232_unread_census.py [--check]"""
import csv, glob, os, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; CL = ("CA", "C6", "LOOPBAR", "CROSS", "LL")
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def main():
    out = ["leaf: draft counts | letters at aligned positions"]
    for d in sorted(glob.glob(f"{P}/rec*/ciphertext_draft.tsv")):
        leaf = d.split("/")[-2][3:]; c = Counter(r["sign"] for r in rd(d) if r["sign"] in CL)
        al = next((f for f in (f"{P}/{leaf}_align_v4.tsv", f"{P}/{leaf}_align.tsv") if os.path.exists(f)), None); let = defaultdict(Counter)
        if al:
            for r in rd(al):
                if r["kind"] == "code" and r["value"] in CL: let[r["value"]][r["plain_chunk"] or "-"] += 1
        out.append(f"{leaf}: " + (" ".join(f"{k} {c[k]}" for k in CL if c[k]) or "none") + (" | " + "; ".join(f"{k}: " + " ".join(f"{x}{n}" for x, n in let[k].most_common()) for k in CL if let[k]) if let else "") + ("" if al else " | (no alignment)"))
    txt = "\n".join(out) + "\n"; p = f"{HERE}/h232_unread_census_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
