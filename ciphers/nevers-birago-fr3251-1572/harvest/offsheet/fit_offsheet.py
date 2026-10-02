#!/usr/bin/env python3
"""Value-fit of the recurring off-sheet shape classes of the 1572 pool, with a random-position control per class, and the
known-answer check on no.87 against the clerk's clear sheet (NEVBIR-OFFSHEET, 2 Oct 2026; rule fixed in PREREG.md).
  python3 offsheet/fit_offsheet.py [--draws 200] [--seed 1] [--min-occ 3] [--min-gain 0.002] [--out offsheet/fits.tsv]
Reads offsheet/pool_*.tsv (subtype_pool.py). Writes fits.tsv (one row per class) and known_no87.tsv (per occurrence)."""
import argparse, csv, difflib, json, random, re, sys
from collections import Counter
from pathlib import Path
H = Path(__file__).resolve().parents[1]; OUT = Path(__file__).resolve().parent
sys.path.insert(0, str(H.parents[2] / "tools")); import judge_plaintext as jp  # noqa
ap = argparse.ArgumentParser(); ap.add_argument("--draws", type=int, default=200); ap.add_argument("--seed", type=int, default=1)
ap.add_argument("--min-occ", type=int, default=3); ap.add_argument("--min-gain", type=float, default=0.002)
ap.add_argument("--out", default=str(OUT / "fits.tsv")); a = ap.parse_args()
M = {e["id"]: e["value"] for e in json.load(open(H / "sign_id_map_1572_fit.json"))}
LET = sorted({v for v in M.values() if len(v) == 1}) + ["null"]
model = jp.NgramModel([jp.read_corpus(p) if hasattr(jp, "read_corpus") else jp.load_text(p) for p in jp.LANG_CORPORA["it16dip"]])
pool = {}  # (letter, passage) -> list of sign ids
for k in ("no87", "no71", "no86", "no90"):
    for r in csv.DictReader(open(OUT / f"pool_{k}.tsv"), delimiter="\t"):
        pool.setdefault((k, r["passage"]), []).append(r["sign_id"])
def dec(seq, m):
    return "".join("_" if m.get(s) is None else ("" if m[s] == "null" else m[s]) for s in seq)
def pscore(seq, m):
    tot = n = 0
    for t in dec(seq, m).split("_"):
        if len(t) >= 4:
            tot += model.score(t) * (len(t) - 3); n += len(t) - 3
    return tot, n
base = {k: pscore(s, M) for k, s in pool.items()}
def total(m, keys, P=pool):
    T = dict(base); [T.__setitem__(k, pscore(P[k], m)) for k in keys]
    tt = sum(x for x, _ in T.values()); nn = sum(y for _, y in T.values()); return tt / nn
def fit(sid, P=pool, m=M):
    keys = [k for k, s in P.items() if sid in s]
    b = total(m, keys, P); res = []
    for v in LET:
        mm = dict(m); mm[sid] = v; res.append((total(mm, keys, P), v))
    res.sort(reverse=True); return b, res
occ = Counter(x for s in pool.values() for x in s if x not in M)
keyed = [(k, i) for k, s in pool.items() for i, x in enumerate(s) if M.get(x) not in (None, "null")]
rng = random.Random(a.seed); rows = []
for sid, n in occ.most_common():
    if sid in ("X_NEW", "?") or n < a.min_occ:
        continue
    b, res = fit(sid); gain = res[0][0] - b
    cg = []
    for _ in range(a.draws):
        pick = rng.sample(keyed, n); P = {k: list(s) for k, s in pool.items()}
        for k, i in pick:
            P[k][i] = "X_CTL"
        keys = sorted({k for k, _ in pick})
        save = {k: base[k] for k in keys}
        for k in keys:
            base[k] = pscore(P[k], M)  # control baseline: positions hidden
        cb, cres = fit("X_CTL", P); cg.append(cres[0][0] - cb)
        base.update(save)
    cg.sort(); p95 = cg[int(0.95 * len(cg)) - 1]; rank = 1 + sum(1 for x in cg if x >= gain)
    acc = n >= a.min_occ and gain >= a.min_gain and gain > p95
    rows.append(dict(sign=sid, occ=n, best=res[0][1], gain=f"{gain:.4f}", second=f"{res[1][1]} {res[1][0]-b:.4f}",
                     third=f"{res[2][1]} {res[2][0]-b:.4f}", ctl_mean=f"{sum(cg)/len(cg):.4f}", ctl_p95=f"{p95:.4f}",
                     ctl_max=f"{cg[-1]:.4f}", rank=f"{rank}/{a.draws+1}", accepted="yes" if acc else "no"))
    print(rows[-1], flush=True)
with open(a.out, "w") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(rows)
# known answer on no.87
sheet = " ".join(r["text"] for r in csv.DictReader(open(H / "f179r_sheet/decipherment_sheet.tsv"), delimiter="\t"))
sheet = re.sub(r"\[[^\]]*\]", "", sheet).replace("car.la", "carmagnola").replace("ma.ta", "maesta")
fold = lambda s: re.sub(r"[^a-z]", "", s.lower().replace("v", "u").replace("j", "i").replace("&", "et"))
clear = fold(sheet)
seq87 = [(r["passage"], r["pos"], r["sign_id"]) for r in csv.DictReader(open(OUT / "pool_no87.tsv"), delimiter="\t")]
def matchcount(ids, m):
    d = fold("".join(m.get(s, "") for s in ids if m.get(s) not in (None, "null")))
    sm = difflib.SequenceMatcher(None, d, clear, autojunk=False)
    return sum(b.size for b in sm.get_matching_blocks() if b.size >= 3)
ids = [s for _, _, s in seq87]; fitted = {r["sign"]: (r["best"], r["accepted"]) for r in rows}
kr = []
for j, (p, pos, s) in enumerate(seq87):
    if s in M:
        continue
    sc = []
    for v in LET:
        ii = list(ids); ii[j] = "X_KA"; sc.append((matchcount(ii, dict(M, X_KA=v)), v))
    sc.sort(reverse=True); top = [v for c, v in sc if c == sc[0][0]]
    ans = top[0] if len(top) == 1 else ("null" if "null" in top and len(top) == 1 else "?")
    if len(top) > 1 and "null" in top and len(top) == len(LET):
        ans = "?"
    fv, acc = fitted.get(s, ("", ""))
    kr.append(dict(passage=p, pos=pos, sign=s, sheet_value=ans, sheet_ties=",".join(top[:5]), sheet_gain=sc[0][0]-dict((v, c) for c, v in sc)["null"],
                   fitted=fv, accepted=acc, right=("" if ans == "?" or not fv else ("yes" if fv == ans else "no"))))
with open(OUT / "known_no87.tsv", "w") as f:
    w = csv.DictWriter(f, fieldnames=list(kr[0]), delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(kr)
for r in kr:
    print(r)
A = [r for r in kr if r["accepted"] == "yes" and r["right"]]; S = [r for r in kr if r["right"]]
pa = sum(r["right"] == "yes" for r in A); ps = sum(r["right"] == "yes" for r in S)
print(f"METHOD CHECK (accepted classes, determinate sheet answer): {pa}/{len(A)}" + (f" = {pa/len(A):.0%}" if A else " (none)"))
print(f"secondary (all fitted classes): {ps}/{len(S)}" + (f" = {ps/len(S):.0%}" if S else ""))
