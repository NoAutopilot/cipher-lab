#!/usr/bin/env python3
"""H177d (runner 7, 29 Sept 2026): where in the period decipherment does a stretch of f.176r/f.176v lie? Pre-registered in
PROMPTS_f176_f175.md section H177d before the fol. 178r / fol. 177v strips 9-12 reads.
Clear = fol. 177r L01-L34 (salutation dropped), then fol. 177v V.., then fol. 178r R.. (passes/f178r_clearA_*.tsv), folded as h170_gate.py
folds. Sequence = A/B consensus of the named rows (build_f176_key.consensus). For every window start w = 0, 100, 200 ... (window length
N = floor(0.8 x signs)), the F61-CAL DP match fraction under key v4's letter sets. Null: 200 windows drawn at random starts, each
letter-shuffled (seed 177), p99. Positive control: f.176r L01-L08 must peak at w = 0.
GATE for f.176v: its peak window beats the null p99 AND the best window not overlapping the peak by >= 0.05.
  python3 h177d_scan.py [--check]   writes h177d_scan_result.txt"""
import glob, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import build_f176_key as b, build_f176v_key as v
from f61crib import align
g = b.g
def clear_all():
    t177r = v.clear177r(); lines = {}; order = []
    for f in sorted(glob.glob(f"{b.P}/f177v_clearA_*.tsv")):
        for r in g.rd(f): lines.setdefault("V" + r["line"].lstrip("LV"), r["text"])
    order = sorted(lines, key=lambda l: int(l[1:]))
    for f in sorted(glob.glob(f"{b.P}/f178r_clearA_*.tsv")):
        for r in g.rd(f):
            k = "R" + r["line"].lstrip("LR"); lines.setdefault(k, r["text"]); order.append(k)
    order = list(dict.fromkeys(order)); marks = [("fol. 177r L01", 0)]; t = t177r
    for l in order:
        if l in ("V01", "R01"): marks.append((("fol. 177v " if l[0] == "V" else "fol. 178r ") + l, len(t)))
        t += g.fold(lines[l])
    return t, marks
def frac(seq, text, key):
    _, pairs = align(text, seq, key); return sum(text[i] in key.get(seq[j], ()) for i, j in pairs if not seq[j].startswith("?")) / len(text)
def scan(name, A, B, rows, text, key, out):
    seq = [s for l in rows for s in b.consensus(A[l], B[l])]; N = int(0.8 * len(seq))
    res = [(w, frac(seq, text[w:w + N], key)) for w in range(0, len(text) - N + 1, 100)]
    rng = random.Random(177); null = []
    for _ in range(200):
        w = rng.randrange(0, len(text) - N + 1); x = list(text[w:w + N]); rng.shuffle(x); null.append(frac(seq, "".join(x), key))
    null.sort(); p99 = null[int(0.99 * len(null)) - 1]
    pw, pf = max(res, key=lambda t: t[1]); second = max(f for w, f in res if abs(w - pw) >= N)
    out.append(f"{name}: {len(seq)} signs, N {N}, {len(res)} windows; peak at letter {pw} ({pf:.3f}); best non-overlapping {second:.3f}; null p99 {p99:.3f}; "
               f"GATE {'PASS' if pf > p99 and pf - second >= 0.05 else 'FAIL'}")
    out.append("  " + " ".join(f"{w}:{f:.2f}" for w, f in res))
def main():
    key = g.load_key(); text, marks = clear_all(); out = [f"clear {len(text)} letters; " + ", ".join(f"{m} at {i}" for m, i in marks)]
    rows = [f"L{k:02d}" for k in range(1, 9)]
    scan("positive control f.176r L01-L08", b.pass_rows("A"), b.pass_rows("B"), rows, text, key, out)
    scan("f.176v L01-L08", v.pass_rows("A"), v.pass_rows("B"), rows, text, key, out)
    txt = "\n".join(out) + "\n"; p = f"{HERE}/h177d_scan_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
