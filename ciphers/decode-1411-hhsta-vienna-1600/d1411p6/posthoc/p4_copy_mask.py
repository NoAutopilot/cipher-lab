#!/usr/bin/env python3
"""D1411-P6 post-hoc, descriptive only (licenses nothing; not a registered test): the PREREG-D1411P6 copy mask calibration
found the p.4 right page aligning to p.1 and the p.1 gloss lines. This scores p.4's committed numbers (d1411p4/numbers.tsv)
split by score_p6.copy_mask against p.1, p.1 gloss, p.2, p.3 with d1411v/rescore_v.score (the AM-D1411V controls: 200 order
shuffles seed 1411 p99, 23 shifted rules, leaf gloss cover).   python3 d1411p6/posthoc/p4_copy_mask.py [--check]"""
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__)); F = os.path.join(H, "..", "..")
sys.path.insert(0, os.path.join(H, "..")); sys.path.insert(0, os.path.join(F, "d1411v"))
import score_p6 as S  # noqa: E402
import rescore_v as V  # noqa: E402
J = S.J
model = J.NgramModel([J.read_corpus(p) for p in J.LANG_CORPORA["de1600"]])
g = round(model.cover(open(os.path.join(F, "gaps150", "gloss_text.txt")).read().strip()), 4)
P = S.prior_pages(); S.NUMBERS = os.path.join(F, "d1411p4", "numbers.tsv"); rs = S.rows()
m, info = S.copy_mask(rs, {k: P[k] for k in ("p1", "p1gloss", "p2", "p3")})
res = {"gloss_cover": g, "copy_alignment": info, "N_all": len(rs), "N_masked": len(m),
       "all": V.score(rs, model, g), "independent": V.score([r for i, r in enumerate(rs) if i not in m], model, g),
       "copy": V.score([r for i, r in enumerate(rs) if i in m], model, g)}
txt = json.dumps(res, indent=1, ensure_ascii=False) + "\n"; p = os.path.join(H, "p4_copy_mask.json")
if "--check" in sys.argv:
    ok = os.path.exists(p) and open(p).read() == txt; print("p4_copy_mask.json", "current" if ok else "STALE"); sys.exit(0 if ok else 1)
open(p, "w").write(txt)
for k in ("all", "independent", "copy"):
    print(k, res[k]["N"], {t: (res[k][t]["cover"], res[k][t]["shuffled_p99"], res[k][t]["shifted_max"], res[k][t]["verdict"])
                           for t in ("T21r", "T21r_h12", "T21r_h22")}, "gloss", res[k]["gloss_T21r"])
