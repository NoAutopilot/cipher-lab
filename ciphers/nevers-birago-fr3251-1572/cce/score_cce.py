#!/usr/bin/env python3
"""BIR-CCE scoring (4 Oct 2026), rule fixed in cce/PREREG.md: Ceppo-Nevers value vs unread (and vs the current 1572 value
for T95) per mapped unit, against a 1000-draw shuffled glyph-to-cell null; known-answer check on no.87 first.
  python3 cce/score_cce.py [--draws 1000] [--seed 1]  -> cce/results.tsv, cce/known_no87.tsv (stdout: summary)"""
import argparse, csv, json, random, sys
from pathlib import Path
C = Path(__file__).resolve().parent; H = C.parent; HV = H / "harvest"
sys.path.insert(0, str(H.parents[1] / "tools")); import judge_plaintext as jp  # noqa
ap = argparse.ArgumentParser(); ap.add_argument("--draws", type=int, default=1000); ap.add_argument("--seed", type=int, default=1); a = ap.parse_args()
M = {e["id"]: e["value"] for e in json.load(open(HV / "sign_id_map_1572_fit.json"))}
model = jp.NgramModel([jp.read_corpus(p) if hasattr(jp, "read_corpus") else jp.load_text(p) for p in jp.LANG_CORPORA["it16dip"]])
cellval = {}
for r in csv.DictReader(open(C / "ceppo_cells.tsv"), delimiter="\t"):
    cellval[r["cell"]] = {"null": "null", "et": "et"}.get(r["column"], r["column"])
gm = [r for r in csv.DictReader((l for l in open(C / "glyph_map.tsv") if not l.startswith("#")), delimiter="\t")]
# sequences: pools 71/86/90 + f144r (passage = line); each position a token id, unique per occurrence for tiles
pool = {}
for k in ("no71", "no86", "no90"):
    for r in csv.DictReader(open(HV / f"offsheet/pool_{k}.tsv"), delimiter="\t"):
        pool.setdefault((k, r["passage"]), []).append(r["sign_id"])
TILE = {"f144r_L04.2_03": "C08", "f144r_L04.1_10": "C40", "f144r_L03_03": "C39"}
ct = list(csv.DictReader(open(HV / "ciphertext_f144r.tsv"), delimiter="\t"))
lab = [r["sid"] for r in csv.DictReader(open(H / "sorter/labels.tsv"), delimiter="\t") if r["sid"].startswith("f144r")]
assert len(lab) == len(ct)
for sid, r in zip(lab, ct):
    pool.setdefault(("no73", r["line"]), []).append(("TILE:" + sid) if sid in TILE else r["sign"])
# units
units = {}  # unit -> (cell, grade, base_alt) ; base_alt = current value for conflict sign
for r in gm:
    if r["source"] == "text description" and r["ceppo_cell"] != "none" and r["sign_1572"] != "X_CE":
        units[r["sign_1572"]] = (r["ceppo_cell"], r["confidence"], None)
for sid, cell in TILE.items():
    units["TILE:" + sid] = (cell, "M", None)
units["T95"] = ("C39", "M", M["T95"])
for r in gm:  # L-graded tiles in f144r, secondary
    s = r["source"].replace("tile ", "")
    if s.startswith("f144r") and s not in TILE and r["ceppo_cell"] != "none":
        units["TILE:" + s] = (r["ceppo_cell"], r["confidence"], None)
        for k, seq in pool.items():
            if k[0] == "no73":
                pool[k] = ["TILE:" + s if (x == s) else x for x in seq]
# re-tag remaining L tiles by position
for sid, r in zip(lab, ct):
    if "TILE:" + sid in units and sid not in TILE:
        seq = pool[("no73", r["line"])]; i = int(r["pos"]) - 1; seq[i] = "TILE:" + sid
def dec(seq, m):
    return "".join("_" if m.get(s) is None else ("" if m[s] == "null" else m[s]) for s in seq)
def pscore(seq, m):
    tot = n = 0
    for t in dec(seq, m).split("_"):
        if len(t) >= 4:
            tot += model.score(t) * (len(t) - 3); n += len(t) - 3
    return tot, n
base = {k: pscore(s, M) for k, s in pool.items()}
def total(m, keys):
    T = dict(base)
    for k in keys:
        T[k] = pscore(pool[k], m)
    return sum(x for x, _ in T.values()) / sum(y for _, y in T.values())
def gain(u, val, ref=None):
    keys = [k for k, s in pool.items() if u in s]
    m0 = dict(M); m0.pop(u, None)
    if ref is not None:
        m0[u] = ref
    m1 = dict(M); m1[u] = val
    return total(m1, keys) - total(m0, keys), sum(s.count(u) for k, s in pool.items())
# base must have every unit unread: recompute base with units removed (T95 keeps current value in base)
M0 = {k: v for k, v in M.items() if k not in units or k == "T95"}
M = M0; base = {k: pscore(s, M) for k, s in pool.items()}
cells = [units[u][0] for u in units]
rng = random.Random(a.seed)
nulls = {u: [] for u in units}
for _ in range(a.draws):
    sh = cells[:]; rng.shuffle(sh)
    for u, c in zip(units, sh):
        nulls[u].append(gain(u, cellval[c], None)[0])
rows = []
for u, (c, g, ref) in units.items():
    gv, n = gain(u, cellval[c]); nl = sorted(nulls[u]); p99 = nl[int(0.99 * len(nl)) - 1]
    gr = gain(u, cellval[c], ref)[0] if ref is not None else None
    primary = g in ("H", "M")
    verdict = ("PASS" if gv > 0 and gv > p99 else "FAIL") if primary else ("secondary: " + ("above p99" if gv > 0 and gv > p99 else "below"))
    rows.append(dict(unit=u, occ_target=n, ceppo_cell=c, grade=g, ceppo_value=cellval[c], gain_vs_unread=f"{gv:.4f}",
                     gain_vs_current=("" if gr is None else f"{gr:.4f} (current {ref})"), null_mean=f"{sum(nl)/len(nl):.4f}",
                     null_p99=f"{p99:.4f}", null_spread=f"{nl[-1]-nl[0]:.4f}", verdict=verdict if n else "no occurrence"))
    print(rows[-1])
with open(C / "results.tsv", "w") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(rows)
# known answer, no.87
ka = []
cls_cell = {r["sign_1572"]: (r["ceppo_cell"], r["confidence"]) for r in gm if r["source"] == "text description"}
for r in csv.DictReader(open(HV / "offsheet/known_no87.tsv"), delimiter="\t"):
    if r["sign"] in cls_cell and cls_cell[r["sign"]][0] != "none" and r["sheet_value"] not in ("?", ""):
        ka.append((r["sign"], r["passage"] + "." + r["pos"], r["sheet_value"]))
ka += [("X_CE", f"f178v tile {i}", "s") for i in range(1, 8)]
real = sum(cellval[cls_cell[s][0]] == v for s, _, v in ka)
allc = [r["ceppo_cell"] for r in gm if r["ceppo_cell"] != "none"]
kn = []
for _ in range(a.draws):
    sh = {s: cellval[rng.choice(allc)] for s in {x for x, _, _ in ka}}
    kn.append(sum(sh[s] == v for s, _, v in ka))
kn.sort(); p95 = kn[int(0.95 * len(kn)) - 1]
with open(C / "known_no87.tsv", "w") as f:
    f.write("sign\tocc\tsheet_value\tceppo_cell\tgrade\tceppo_value\tmatch\n")
    for s, o, v in ka:
        c, g = cls_cell[s]; f.write(f"{s}\t{o}\t{v}\t{c}\t{g}\t{cellval[c]}\t{'yes' if cellval[c]==v else 'no'}\n")
print(f"KNOWN ANSWER no.87: {real}/{len(ka)} Ceppo value == clerk sheet; null mean {sum(kn)/len(kn):.2f}, p95 {p95}, max {kn[-1]}")
