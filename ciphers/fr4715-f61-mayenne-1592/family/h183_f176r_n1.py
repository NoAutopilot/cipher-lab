#!/usr/bin/env python3
"""H183 (runner 7, 29 Sept 2026): f.176r against its whole decipherment. H177d-H177f put f.176v's text at fol. 177v V06 (scan and the plain
"In foro conscientie" anchor, about one letter per sign), so f.176r's text is fol. 177r L01 - fol. 177v V05, about 2,957 letters for 3,095
signs. build_f176_key.py (not edited; key_period_f176.tsv is the audited file) trimmed the clear at N = 0.8 x signs = 2,476. This script
reruns the same design (A/B consensus, v4 sets decide only the alignment) with the clear = fol. 177r L01 - fol. 177v V05 and
N = min(letters, signs), control f.184r from word 0 (same N), and reports per class the counts beside key_period_f176.tsv's.
  python3 h183_f176r_n1.py [--check]   writes h183_f176r_n1_result.txt only"""
import glob, os, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import build_f176_key as b, build_f176v_key as v
g = b.g
def main():
    A, B = b.pass_rows("A"), b.pass_rows("B"); rows = [f"L{k:02d}" for k in range(1, 48)]
    seq = [s for l in rows for s in b.consensus(A[l], B[l])]; key = g.load_key()
    lines = {}
    for f in sorted(glob.glob(f"{b.P}/f177v_clearA_*.tsv")):
        for r in g.rd(f): lines.setdefault("V" + r["line"].lstrip("LV"), r["text"])
    text = v.clear177r() + "".join(g.fold(lines[f"V{k:02d}"]) for k in range(1, 6)); N = min(len(text), len(seq))
    w184 = g.fold(" ".join(r["word"] for r in g.rd(f"{b.P}/f184r_clear_rec.tsv")))[:N]
    ct, ft = b.run(seq, text[:N], key, "true"); cw, fw = b.run(seq, w184, key, "wrong")
    old = defaultdict(Counter)
    for r in g.rd(f"{HERE}/key_period_f176.tsv"): old[r["class"]][r["letter"]] += int(r["n"])
    fmt = lambda C: " ".join(f"{x}{n}" for x, n in sorted(C.items(), key=lambda t: (-t[1], t[0]))[:5])
    out = [f"f.176r L01-L47: {len(seq)} signs; clear fol. 177r L01 - fol. 177v V05, {len(text)} letters; N {N} (build_f176_key.py used 2,476)",
           f"match {ft:.3f} vs wrong f.184r {fw:.3f}; margin {ft - fw:+.3f}", "",
           "class\tv4 set\tN1 run: letters (n)\tkey_period_f176.tsv: letters (n)\twrong: letters (n)"]
    for c in sorted(set(ct) | set(old), key=lambda c: (-sum(ct[c].values()), c)):
        out.append(f"{c}\t{'/'.join(key.get(c, ())) or '-'}\t{fmt(ct[c])} ({sum(ct[c].values())})\t{fmt(old[c])} ({sum(old[c].values())})\t{fmt(cw[c])} ({sum(cw[c].values())})")
    txt = "\n".join(out) + "\n"; p = f"{HERE}/h183_f176r_n1_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
