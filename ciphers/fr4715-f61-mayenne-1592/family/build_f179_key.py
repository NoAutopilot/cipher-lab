#!/usr/bin/env python3
"""H184 (runner 7, 29 Sept 2026): is fol. 178r the decipherment of fr.3984 fol. 179's cipher (item 84's last leaf, 21 rows)? Written before the
fol. 179 passes were read. H177f put f.176v's text at fol. 177v V06 at about one letter per sign, so f.176v (2,923 signs) ends near fol. 177v's
foot and fol. 178r (R01-R19) is left over. Design = build_f176_key.py's (A/B consensus, key v4's sets decide only the alignment).
 (1) Location scan (h177d_scan.py's windows and null) of fol. 179's rows over the whole read clear: fol. 177r L01 - fol. 177v V40 - fol. 178r R19.
 (2) Build from fol. 178r R01 (N = min(letters, signs): the one-letter-per-sign rate H177f found), controls (a) f.184r from word 0,
     (b) fol. 177r from L01, (c) fol. 177v from V06 (f.176v's own clear), same N.
GATE (pre-registered, PROMPTS section H184): (1) the scan peak lies at or after fol. 178r R01 minus 300 letters, beats the null p99 and the best
non-overlapping window by >= 0.05; AND (2) match(R01-) - max(a, b, c) >= +0.10. Rows go to key_period_f179.tsv (separate; not merged).
  python3 build_f179_key.py ROWS [--check]   (ROWS e.g. L01-L08; reads passes/f179_signs{A,B}_*.tsv)"""
import glob, os, re, sys
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import build_f176_key as b, build_f176v_key as v, h177d_scan as h
g = b.g; LEAF = "fr.3984 fol. 179/fol. 178r"
def pass_rows(tag):
    rows = defaultdict(list)
    for f in sorted(glob.glob(f"{b.P}/f179_signs{tag}_*.tsv")):
        for r in g.rd(f):
            s = {"EBR_A": "EBR", "EBR_B": "EBR"}.get(r["sign"].strip(), r["sign"].strip())
            if s != "PLAIN": rows[r["line"]].append(s)
    return rows
def main():
    a = sys.argv; lo, hi = [int(x) for x in re.findall(r"\d+", a[1])]; want = [f"L{k:02d}" for k in range(lo, hi + 1)]
    A, B = pass_rows("A"), pass_rows("B"); missing = [l for l in want if l not in A or l not in B]
    if missing: sys.exit(f"missing rows in the passes: {missing}")
    key = g.load_key(); full, marks = h.clear_all(); r01 = dict(marks).get("fol. 178r R01")
    out = [f"clear {len(full)} letters; " + ", ".join(f"{m} at {i}" for m, i in marks)]
    h.scan(f"(1) fol. 179 {want[0]}-{want[-1]}", A, B, want, full, key, out)
    seq = [s for l in want for s in b.consensus(A[l], B[l])]; N = int(0.8 * len(seq))
    res = [(w, h.frac(seq, full[w:w + N], key)) for w in range(0, len(full) - N + 1, 100)]; pw = max(res, key=lambda t: t[1])[0]
    ok1 = "GATE PASS" in out[-2] and r01 is not None and pw >= r01 - 300
    lines = {}
    for f in sorted(glob.glob(f"{b.P}/f178r_clearA_*.tsv")):
        for r in g.rd(f): lines.setdefault("R" + r["line"].lstrip("LR"), r["text"])
    t178 = "".join(g.fold(lines[k]) for k in sorted(lines, key=lambda k: int(k[1:])))
    t177v = full[dict(marks)["fol. 177v V01"]:r01]; t177v = t177v[t177v.index(g.fold(v.clear("V06")[0][:40])):] if g.fold(v.clear("V06")[0][:40]) in t177v else t177v
    N2 = min(len(seq), len(t178)); w184 = g.fold(" ".join(r["word"] for r in g.rd(f"{b.P}/f184r_clear_rec.tsv")))[:N2]
    ct, ft = b.run(seq, t178[:N2], key, "true"); fa = b.run(seq, w184, key, "wrong")[1]; fb = b.run(seq, v.clear177r()[:N2], key, "wrong")[1]
    fc = b.run(seq, t177v[:N2], key, "wrong")[1]; marg = ft - max(fa, fb, fc)
    out += [f"(1) scan peak at letter {pw} (fol. 178r R01 at {r01}): {'PASS' if ok1 else 'FAIL'}",
            f"(2) fol. 178r from R01, N {N2}: {ft:.3f} vs (a) f.184r {fa:.3f}, (b) fol. 177r {fb:.3f}, (c) fol. 177v V06- {fc:.3f}; margin {marg:+.3f}: {'PASS' if marg >= 0.10 else 'FAIL'}",
            f"GATE (1) AND (2): {'PASS' if ok1 and marg >= 0.10 else 'FAIL'}", "", "class\tv4 set\tfol. 178r: letters (n)"]
    fmt = lambda C: " ".join(f"{x}{n}" for x, n in sorted(C.items(), key=lambda t: (-t[1], t[0]))[:6])
    for c in sorted(ct, key=lambda c: (-sum(ct[c].values()), c)): out.append(f"{c}\t{'/'.join(key.get(c, ())) or '-'}\t{fmt(ct[c])} ({sum(ct[c].values())})")
    rows = ["# key_period_f179.tsv -- H184 (runner 7), build_f179_key.py " + a[1] + ": set-anchored DP pairs, consensus signs only; key source period; NOT merged (a verifier's)",
            "class\tletter\tn\tleaf\tbands"] + [f"{c}\t{x}\t{n}\t{LEAF}\tDP stage {want[0]}-{want[-1]}" for c in sorted(ct) for x, n in sorted(ct[c].items(), key=lambda t: (-t[1], t[0]))]
    files = {f"{HERE}/build_f179_key_result.txt": "\n".join(out) + "\n", f"{HERE}/key_period_f179.tsv": "\n".join(rows) + "\n"}
    if "--check" in a:
        bad = [p for p, s in files.items() if not os.path.exists(p) or open(p).read() != s]
        print("stale: " + ", ".join(bad) if bad else "OK"); sys.exit(1 if bad else 0)
    for p, s in files.items(): open(p, "w").write(s)
    print("\n".join(l for l in out if l.startswith(("(", "GATE"))))
if __name__ == "__main__": main()
