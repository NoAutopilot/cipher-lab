#!/usr/bin/env python3
"""BIR-CCE2 scoring (4 Oct 2026), rule fixed in cce2/PREREG-2.md: same statistic, null and gate as cce/score_cce.py, with the
units taken from cce2/glyph_map.tsv (shuffled K-labels resolved through cce2/ref_ceppo_perm.tsv AFTER the map was pushed),
the no.87 known answer in two counts (occurrences, signs), and step 2 (Ceppo-side off-key signs -> 1572 letters) on the
committed Ceppo readings.   python3 cce2/score_cce2.py [--draws 1000] [--seed 1]  -> cce2/results.tsv, known_no87.tsv, step2.tsv"""
import argparse, csv, json, random, sys
from pathlib import Path
C = Path(__file__).resolve().parent; H = C.parent; HV = H / "harvest"; CE = H.parent / "ceppo-nevers-fr3251-1570s"
sys.path.insert(0, str(H.parents[1] / "tools")); import judge_plaintext as jp  # noqa
ap = argparse.ArgumentParser(); ap.add_argument("--draws", type=int, default=1000); ap.add_argument("--seed", type=int, default=1); a = ap.parse_args()
model = jp.NgramModel([jp.read_corpus(p) if hasattr(jp, "read_corpus") else jp.load_text(p) for p in jp.LANG_CORPORA["it16dip"]])
perm = {r["klabel"]: r for r in csv.DictReader(open(C / "ref_ceppo_perm.tsv"), delimiter="\t")}
def kval(k): return {"null": "null", "et": "et"}.get(perm[k]["column"], perm[k]["column"])
gm = [r for r in csv.DictReader((l for l in open(C / "glyph_map.tsv") if not l.startswith("#")), delimiter="\t")]
M = {e["id"]: e["value"] for e in json.load(open(HV / "sign_id_map_1572_fit.json"))}
pool = {}
for k in ("no71", "no86", "no90"):
    for r in csv.DictReader(open(HV / f"offsheet/pool_{k}.tsv"), delimiter="\t"):
        pool.setdefault((k, r["passage"]), []).append(r["sign_id"])
ct = list(csv.DictReader(open(HV / "ciphertext_f144r.tsv"), delimiter="\t"))
lab = [r["sid"] for r in csv.DictReader(open(H / "sorter/labels.tsv"), delimiter="\t") if r["sid"].startswith("f144r")]
assert len(lab) == len(ct)
TILE = {"f144r_L03_03": "X_NEW-d"}
for sid, r in zip(lab, ct):
    pool.setdefault(("no73", r["line"]), []).append(("TILE:" + sid) if sid in TILE else r["sign"])
units = {}  # unit -> (K, grade, ref_current)
for r in gm:
    s, k, g = r["sign"], r["ref_cell"], r["confidence"]
    if k == "none" or s.startswith("CEPPO-") or s == "X_CE": continue
    if s == "T95": units["T95"] = (k, g, M["T95"])
    elif s == "X_NEW-d": units["TILE:f144r_L03_03"] = (k, g, None)
    elif s.startswith("X_") and not s.startswith("X_NEW"): units[s] = (k, g, None)
def dec(seq, m): return "".join("_" if m.get(s) is None else ("" if m[s] == "null" else m[s]) for s in seq)
def pscore(seq, m):
    tot = n = 0
    for t in dec(seq, m).split("_"):
        if len(t) >= 4: tot += model.score(t) * (len(t) - 3); n += len(t) - 3
    return tot, n
M0 = {k: v for k, v in M.items() if k not in units or k == "T95"}; M = M0
base = {k: pscore(s, M) for k, s in pool.items()}
def total(m, keys):
    T = dict(base)
    for k in keys: T[k] = pscore(pool[k], m)
    return sum(x for x, _ in T.values()) / sum(y for _, y in T.values())
def gain(u, val, ref=None):
    keys = [k for k, s in pool.items() if u in s]
    m0 = dict(M); m0.pop(u, None)
    if ref is not None: m0[u] = ref
    m1 = dict(M); m1[u] = val
    return total(m1, keys) - total(m0, keys), sum(s.count(u) for k, s in pool.items())
cells = [units[u][0] for u in units]; rng = random.Random(a.seed); nulls = {u: [] for u in units}
for _ in range(a.draws):
    sh = cells[:]; rng.shuffle(sh)
    for u, c in zip(units, sh): nulls[u].append(gain(u, kval(c), None)[0])
rows = []
for u, (k, g, ref) in units.items():
    gv, n = gain(u, kval(k)); nl = sorted(nulls[u]); p99 = nl[int(0.99 * len(nl)) - 1]
    gr = gain(u, kval(k), ref)[0] if ref is not None else None; primary = g in ("H", "M")
    verdict = ("PASS" if gv > 0 and gv > p99 else "FAIL") if primary else ("secondary: " + ("above p99" if gv > 0 and gv > p99 else "below"))
    rows.append(dict(unit=u, occ_target=n, klabel=k, ceppo_cell=perm[k]["cce_cell"], grade=g, ceppo_value=kval(k), gain_vs_unread=f"{gv:.4f}",
                     gain_vs_current=("" if gr is None else f"{gr:.4f} (current {ref})"), null_mean=f"{sum(nl)/len(nl):.4f}",
                     null_p99=f"{p99:.4f}", null_spread=f"{nl[-1]-nl[0]:.4f}", verdict=verdict if n else "no occurrence"))
    print(rows[-1])
with open(C / "results.tsv", "w") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(rows)
# known answer, no.87: two counts
cls_k = {r["sign"]: (r["ref_cell"], r["confidence"]) for r in gm if r["ref_cell"] != "none" and not r["sign"].startswith("CEPPO-")}
ka = []
for r in csv.DictReader(open(HV / "offsheet/known_no87.tsv"), delimiter="\t"):
    if r["sign"] in cls_k and r["sheet_value"] not in ("?", ""): ka.append((r["sign"], r["passage"] + "." + r["pos"], r["sheet_value"]))
ka += [("X_CE", f"f178v tile {i}", "s") for i in range(1, 8)]
signs = sorted({s for s, _, _ in ka}); real_a = sum(kval(cls_k[s][0]) == v for s, _, v in ka)
real_b = sum(any(kval(cls_k[s][0]) == v for s2, _, v in ka if s2 == s) for s in signs)
allk = [r["ref_cell"] for r in gm if r["ref_cell"] != "none" and not r["sign"].startswith("CEPPO-")]
ka_null, kb_null = [], []
for _ in range(a.draws):
    sh = {s: kval(rng.choice(allk)) for s in signs}
    ka_null.append(sum(sh[s] == v for s, _, v in ka)); kb_null.append(sum(any(sh[s] == v for s2, _, v in ka if s2 == s) for s in signs))
ka_null.sort(); kb_null.sort(); pa = ka_null[int(0.95 * a.draws) - 1]; pb = kb_null[int(0.95 * a.draws) - 1]
with open(C / "known_no87.tsv", "w") as f:
    f.write("sign\tocc\tsheet_value\tklabel\tceppo_cell\tgrade\tceppo_value\tmatch\n")
    for s, o, v in ka:
        k, g = cls_k[s]; f.write(f"{s}\t{o}\t{v}\t{k}\t{perm[k]['cce_cell']}\t{g}\t{kval(k)}\t{'yes' if kval(k)==v else 'no'}\n")
print(f"KNOWN ANSWER no.87 (a) occurrences: {real_a}/{len(ka)}; null mean {sum(ka_null)/a.draws:.2f}, p95 {pa}, max {ka_null[-1]}")
print(f"KNOWN ANSWER no.87 (b) signs: {real_b}/{len(signs)}; null mean {sum(kb_null)/a.draws:.2f}, p95 {pb}, max {kb_null[-1]}")
control_ok = real_a > pa or real_b > pb
print("CONTROL:", "has power at this N" if control_ok else "no power at this N -> target verdicts are untested-by-this-tool")
# step 2: Ceppo-side off-key signs -> 1572 letters, on the committed Ceppo readings
STEP2 = {"X_THETA2": ("a", "M", "r"), "X_POUND": ("t", "L", None), "X_NEW": ("r", "L", None)}  # resolved in RESULTS.md (N10 row1 = a, N14 row2 = t, N01 row2 = r)
seqs, vals = {}, {}
for fol in ("f21v", "f35", "f87"):
    for r in csv.DictReader(open(CE / "harvest" / f"reading_{fol}_tokens.tsv"), delimiter="\t"):
        key = (fol, r["line"]); sid = r["sign"]
        if sid == "X_NEW" and not (fol == "f21v" and r["line"].startswith("L09") and r["pos"] == "27"): sid = "X_NEW_other"
        seqs.setdefault(key, []).append(sid)
        if r["value"] and sid not in STEP2: vals[sid] = r["value"]
letters = [r["value"] for r in csv.DictReader((l for l in open(H / "keys/key_nevers_birago_1572.tsv") if not l.startswith("#")), delimiter="\t") if r["kind"] == "letter"]
def tot2(m, keys):
    T = {k: pscore(s, m) for k, s in seqs.items()}
    return sum(x for x, _ in T.values()) / max(1, sum(y for _, y in T.values()))
def gain2(u, val, ref=None):
    m0 = dict(vals); m0.pop(u, None)
    if ref is not None: m0[u] = ref
    m1 = dict(vals); m1[u] = val
    return tot2(m1, None) - tot2(m0, None), sum(s.count(u) for s in seqs.values())
with open(C / "step2.tsv", "w") as f:
    f.write("unit\tocc\tvalue_1572\tgrade\tgain_vs_unread\tgain_vs_current\tnull_mean\tnull_p99\tnull_spread\tverdict\n")
    for u, (v, g, ref) in STEP2.items():
        gv, n = gain2(u, v); nl = sorted(gain2(u, rng.choice(letters))[0] for _ in range(a.draws)); p99 = nl[int(0.99 * a.draws) - 1]
        gr = f"{gain2(u, v, ref)[0]:.4f} (current {ref})" if ref else ""
        verdict = ("PASS" if gv > 0 and gv > p99 else "FAIL") if g == "M" else ("secondary: " + ("above p99" if gv > 0 and gv > p99 else "below"))
        line = f"{u}\t{n}\t{v}\t{g}\t{gv:.4f}\t{gr}\t{sum(nl)/len(nl):.4f}\t{p99:.4f}\t{nl[-1]-nl[0]:.4f}\t{verdict if n else 'no occurrence'}"
        print("STEP2", line); f.write(line + "\n")
