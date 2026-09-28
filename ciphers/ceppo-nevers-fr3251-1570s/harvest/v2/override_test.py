#!/usr/bin/env python3
"""VERIFY-CEPPO-2 override challenge (28 Sept 2026): for each I-graded sign class on the blind transcription D,
which letter does an it16dip 4-gram model prefer, per occurrence (window of +-6 letters) and pooled over all
occurrences, and where does the claimed letter rank of 20? Also: the fragments with overrides removed."""
import csv, json, sys
from pathlib import Path
H = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(H.parents[2] / "tools")); import judge_plaintext as jp
m = {e["id"]: e["value"] for e in json.load(open(H / "sign_id_map.json"))}
rows = list(csv.DictReader(open(H / "passD_blind_verify.tsv"), delimiter="\t"))
model = jp.NgramModel([jp.read_corpus(p) for p in jp.LANG_CORPORA["it16dip"]])
L = "acdefghilmnopqrstuz"
def seq(p, over):
    out = []
    for r in rows:
        if r["passage"] != p: continue
        k = (r["passage"], int(r["pos"])); s = r["sign_id"].strip()
        v = over.get(k, m.get(s, "_"))
        out.append((k, "" if v == "null" else v))
    return out
def window(p, k, letter, over, w=6):
    sq = seq(p, {**over, k: letter}); txt = ""; idx = None
    for kk, v in sq:
        if kk == k: idx = len(txt)
        txt += v
    t = txt[max(0, idx - w): idx + w + 1]
    parts = [x for x in t.split("_") if len(x) >= 4]
    return sum(model.score(x) * (len(x) - 3) for x in parts) / max(1, sum(len(x) - 3 for x in parts))
classes = {
 "pound S31 (printed m) claimed l": ("l", [(r["passage"], int(r["pos"])) for r in rows if r["sign_id"] == "S31"]),
 "double-barred oval (no cell) claimed r": ("r", [(r["passage"], int(r["pos"])) for r in rows if r["sign_id"] == "?" and "TWO" in r["note"].upper() or ("two parallel" in r["note"])]),
}
for name, (claim, occ) in classes.items():
    print("==", name, len(occ), "occurrences")
    pooled = {c: 0.0 for c in L}
    for k in occ:
        sc = {c: window(k[0], k, c, {}) for c in L}
        rk = sorted(L, key=lambda c: -sc[c])
        for c in L: pooled[c] += sc[c]
        print(f"  {k}: best {rk[:4]}  claimed '{claim}' rank {rk.index(claim)+1}/19; printed-m rank {rk.index('m')+1}")
    rk = sorted(L, key=lambda c: -pooled[c]); print("  pooled best", rk[:5], "claimed rank", rk.index(claim) + 1)
for p in ["P1", "P2", "P4"]:
    print(p, "no overrides:", "".join(v for _, v in seq(p, {})))
