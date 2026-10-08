#!/usr/bin/env python3
"""D1A-PISG: score the blind f.275v gloss read against the Colbert copy (PREREG-D1A-PISG.md).
python3 pisg/pisg.py [--check]   (run from the target folder or anywhere)"""
import json, random, re, sys, unicodedata
from pathlib import Path
H = Path(__file__).resolve().parent; T = H.parent
ABBR = [(r"\bv\.?\s*m(a)?(te|tes|t)?\b\.?", "vostremajeste"), (r"\bs\.?\s*s\.?\b|\bs\.?\s*ste\b", "sasaintete"),
        (r"\bs\.(?=\s*de\b)", "sieur"), (r"&", "et")]
def norm(s):
    s = unicodedata.normalize("NFD", s.lower()); s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.replace("[?]", " ").replace("[...]", " ").replace("?", " ")
    for a, b in ABBR: s = re.sub(a, b, s)
    s = s.translate(str.maketrans("jyv", "iiu"))
    return re.sub(r"[^a-z]", "", s)
def segments(path):
    segs, cur = {}, None
    for ln in path.read_text().splitlines():
        if ln.startswith("=== "): cur = ln[4:].strip(); segs[cur] = []; continue
        if cur and cur != "notes":
            ln = re.sub(r"\((?:L0|very|\"|fairly|no sep|\?)[^)]*\)", " ", ln)  # reader's own remarks, not transcription
            segs[cur].append(ln)
    return {k: norm(" ".join(v)) for k, v in segs.items() if k != "notes"}
def semiglobal(g, c):
    """gloss end-to-end, free end gaps in copy; returns matched letters on the best path."""
    n, m = len(g), len(c); NEG = -10**9
    prev = [(0, 0)] * (m + 1)
    for i in range(1, n + 1):
        cur = [(prev[0][0] - 1, prev[0][1])] + [None] * m
        gi = g[i - 1]
        for j in range(1, m + 1):
            d = prev[j - 1]; s = (d[0] + (1 if gi == c[j - 1] else -1), d[1] + (gi == c[j - 1]))
            u = prev[j]; s = max(s, (u[0] - 1, u[1]))
            l = cur[j - 1]; s = max(s, (l[0] - 1, l[1]))
            cur[j] = s
        prev = cur
    return max(prev)[1]
def ident(segs, copy):
    tot = sum(len(v) for v in segs.values())
    return sum(semiglobal(v, copy) for v in segs.values() if v) / tot, tot
def p99(xs): xs = sorted(xs); return xs[int(0.99 * (len(xs) - 1))]
def main():
    segs = segments(H / "reader_A.txt"); copy = norm((T / "kp86i/colbert_f275v.txt").read_text())
    pool = norm(" ".join((T / f).read_text() for f in ["kp86/colbert_p49_50.txt", "kp86b/colbert_p51_52.txt",
            "kp86g/colbert_f247r.txt", "kp87a/colbert_p338_339.txt", "kp87b/colbert_p341_342.txt"]))
    tgt, tot = ident(segs, copy)
    r = random.Random(0); n1 = []
    for _ in range(200):
        s = r.randrange(len(pool)); w = (pool + pool)[s:s + len(copy)]; n1.append(ident(segs, w)[0])
    r = random.Random(1); n2 = []
    for _ in range(200):
        sh = {k: "".join(r.sample(v, len(v))) for k, v in segs.items()}; n2.append(ident(sh, copy)[0])
    per = {k: (semiglobal(v, copy) / len(v) if v else None, len(v)) for k, v in segs.items()}
    res = {"gloss_letters": tot, "copy_letters": len(copy), "identity": round(tgt, 4),
           "per_segment": {k: [round(a, 4) if a is not None else None, b] for k, (a, b) in per.items()},
           "N1_span_p99": round(p99(n1), 4), "N1_mean": round(sum(n1) / 200, 4),
           "N2_order_p99": round(p99(n2), 4), "N2_mean": round(sum(n2) / 200, 4),
           "too_short": tot < 150}
    res["G1_witness"] = (not res["too_short"]) and tgt > res["N1_span_p99"] and tgt > res["N2_order_p99"]
    res["G2_agreement_080"] = tgt >= 0.80
    out = H / "pisg_result.json"; txt = json.dumps(res, indent=1) + "\n"
    if "--check" in sys.argv:
        ok = out.exists() and out.read_text() == txt; print("up to date" if ok else "STALE"); sys.exit(0 if ok else 1)
    out.write_text(txt); print(txt)
main()
