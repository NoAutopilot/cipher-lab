#!/usr/bin/env python3
"""D1411-POOL gate (d1411pool/PREREG-D1411POOL.md): pool the committed independent (copy-masked) numerals of p.4, p.5, p.6 and score
frozen T21r (+ h12/h22, reported) with d1411v/rescore_v.score (200 order shuffles seed 1411, 23 shifted rules, gloss bar).

  python3 d1411pool/score_pool.py            write score_pool.json and decode_T21r.txt; print the verdict
  python3 d1411pool/score_pool.py --counts   print the per-page independent N only (no score)
  python3 d1411pool/score_pool.py --check    exit 1 if committed outputs are stale (rule 7)
"""
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__)); F = os.path.join(H, "..")
sys.path.insert(0, os.path.join(F, "d1411p6")); sys.path.insert(0, os.path.join(F, "d1411v"))
import score_p6 as S  # noqa: E402
import rescore_v as V  # noqa: E402
J = S.J
EXPECT = {"p4": 112, "p5": 136, "p6": 60}


def page(f, pages, prefix=""):
    S.NUMBERS = os.path.join(F, f, "numbers.tsv"); rs = S.rows()
    m, _ = S.copy_mask(rs, pages, prefix)
    return [r for i, r in enumerate(rs) if i not in m]


def material():
    P = S.prior_pages()
    ind = {"p4": page("d1411p4", {k: P[k] for k in ("p1", "p1gloss", "p2", "p3")}),
           "p5": page("d1411p5", S.prior_pages(only_p2=True), "p5L"),
           "p6": page("d1411p6", P)}
    return ind


def main():
    ind = material(); counts = {k: len(v) for k, v in ind.items()}
    if counts != EXPECT:
        print("independent N differs from PREREG", counts, EXPECT); sys.exit(2)
    if "--counts" in sys.argv:
        print(counts, "pooled", sum(counts.values())); return
    pool = ind["p4"] + ind["p5"] + ind["p6"]
    t = S.tabs()["T21r"]; dtxt = S.decode_text(pool, t)
    model = J.NgramModel([J.read_corpus(p) for p in J.LANG_CORPORA["de1600"]])
    g = round(model.cover(open(os.path.join(F, "gaps150", "gloss_text.txt")).read().strip()), 4)
    sc = V.score(pool, model, g); r = sc["T21r"]
    PASS = bool(r["cover"] > r["shuffled_p99"] and r["cover"] >= g)
    res = {"prereg": "d1411pool/PREREG-D1411POOL.md", "counts": counts, "N": len(pool), "gloss_bar": g, "pooled": sc,
           "gate_T21r": {"cover": r["cover"], "shuffled_p99": r["shuffled_p99"], "gloss_bar": g, "PASS": PASS,
                         "verdict": "PASS" if PASS else "FAIL"}}
    txt = json.dumps(res, indent=1, ensure_ascii=False) + "\n"
    pj, pd = os.path.join(H, "score_pool.json"), os.path.join(H, "decode_T21r.txt")
    if "--check" in sys.argv:
        ok = os.path.exists(pj) and open(pj).read() == txt and os.path.exists(pd) and open(pd).read() == dtxt
        print("d1411pool", "current" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(pj, "w").write(txt); open(pd, "w").write(dtxt)
    print(json.dumps(res["gate_T21r"]))
    for k in ("T21r", "T21r_h12", "T21r_h22"):
        print(k, sc[k])
    print("gloss", sc["gloss_T21r"], "real_cover_p05", sc["de1600_real_cover_p05"])


if __name__ == "__main__":
    main()
