#!/usr/bin/env python3
"""H228 (runner 9 session_012NTadgrCBftz3oRtgw5jFu, 29 Sept 2026), script-only, written before the run, CONDITIONAL on a held gloss: the letters
passes/f106r_align.tsv (f.106r's alignment against its own gloss passes, which agreed under 60%, f106r_gate.txt: HELD) places at the HASH4 positions
H221 shape-read as looped (B) vs 4-head (A), and at the H24 (2#) positions. Mapping: align idx = index among the line's non-DASH draft signs
(passes/recf106r/ciphertext_draft.tsv), as align_period.py builds it. Pre-stated read-out: "looped B leans i/x on f.106r (conditional)" iff >= 6 B
positions carry a letter and >= 0.6 of them are i/x/j/y; else "no lean shown". No key use.  python3 h228_loop_106r_gloss.py [--check]"""
import csv, os, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def main():
    idx = {}; S = defaultdict(list)
    for r in rd(f"{P}/recf106r/ciphertext_draft.tsv"):
        if r["sign"] != "DASH": idx[(r["line"], r["position"])] = (r["line"], str(len(S[r["line"]]))); S[r["line"]].append(r)
    al = {(r["cipher_line"], r["idx"]): r for r in rd(f"{P}/f106r_align.tsv") if r["kind"] == "code"}
    lets = defaultdict(list); miss = 0
    for r in rd(f"{HERE}/h221_positions.tsv"):
        if r["set"] != "h221h": continue
        a = al.get(idx.get((r["line"], r["pos"])))
        if not a or a["value"] != r["code"]: miss += 1; continue
        lets[(r["code"], r["answer"])].append(a["plain_chunk"] or "-")
    out = [f"positions unmapped or code-mismatched: {miss}"]
    for k in sorted(lets): out.append(f"{k[0]} form {k[1]}: " + " ".join(f"{x}{n}" for x, n in Counter(lets[k]).most_common()))
    b = [x for x in lets[("HASH4", "B")] if x != "-"]; ix = sum(1 for x in b if x in "ixjy")
    ok = len(b) >= 6 and ix / max(1, len(b)) >= 0.6
    out.append(f"read-out: looped B lettered {len(b)}, i/x/j/y {ix} -> " + ("looped B leans i/x on f.106r (conditional on a held gloss)" if ok else "no lean shown"))
    txt = "\n".join(out) + "\n"; p = f"{HERE}/h228_loop_106r_gloss_result.txt"
    if "--check" in sys.argv:
        ok2 = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok2 else "STALE"); sys.exit(0 if ok2 else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
