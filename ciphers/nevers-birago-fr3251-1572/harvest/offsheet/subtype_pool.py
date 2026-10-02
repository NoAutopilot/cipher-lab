#!/usr/bin/env python3
"""Shape-subtype every off-sheet X_NEW tile of the 1572 pool from the blind readers' own notes, and rebuild the pooled
per-letter sequences with the subtypes (NEVBIR-OFFSHEET, 2 Oct 2026). Generalises harvest/subtype_xnew.py (X_AE only).
Value-blind: reads the readers' shape notes, never a value. For each folder the passC rows are aligned (difflib on sign
ids) to the concatenated agreement rows (merged column), and an X_NEW passC row takes a class when the readers' notes at
the aligned posA/posB match one class pattern (A and B disagreeing -> stays X_NEW). The rebuilt pooled sequences are
checked sign-for-sign against the committed ones (subtype aside) and the script exits 1 on any mismatch.
  python3 offsheet/subtype_pool.py      -> offsheet/pool_<letter>.tsv + offsheet/subtype_counts.tsv"""
import csv, difflib, re, sys
from collections import Counter
from pathlib import Path
H = Path(__file__).resolve().parents[1]; OUT = Path(__file__).resolve().parent
CLASSES = [  # order matters: first match wins within one note
    ("X_AE", r"\bae\b|\boe\b|ae/oe|x with e|ligature|æ|œ|epsilon tail|ae-like"),
    ("X_MA", r"m with (raised|superscript) a|\bm-a\b|raised a"),
    ("X_T3", r"t-stem with 3|t with 3|\+3|3-shaped|cross-tick and 3|bar\+3"),
    ("X_T", r"\bt[- ]shape|lowercase t|small t|cursive t|t with crossbar|^t$|8 or t"),
    ("X_8", r"digit 8|plain 8|\b8-like|8 with|8 struck|^8$|\b8\b"),
    ("X_4", r"digit 4|open 4|numeral 4|^4$|\b4\b"),
    ("X_7", r"digit 7|^7$|\b7\b"),
    ("X_SQ", r"square|\bbox\b"),
    ("X_PCT", r"percent|b/% "),
    ("X_TRI", r"triangle"),
    ("X_OM", r"omega"),
    ("X_STAR", r"star"),
    ("X_EE", r"ЭЄ|Э|Є"),
    ("X_OSC", r"o stem cross"),
    ("X_H", r"h-like"),
    ("X_F2", r"f with two bars"),
    ("X_BB", r"b with cross|barred cross-b|stem sign with crossbar|b with stem and crossbar|Ƀ"),
    ("X_CC", r"c with curl"),
    ("X_Y", r"y-shape"),
    ("X_HX", r"hatched x"),
    ("X_OJ", r"o with j"),
]
def cls(note):
    for c, p in CLASSES:
        if re.search(p, note or "", re.I):
            return c
    return None
# folder -> (passC, [(agreement, passA, passB), ...])
SRC = {
 "f139v": ("f139v/passC.tsv", [("f139v/passC_agreement.tsv", "f139v/passA.tsv", "f139v/passB.tsv")]),
 "f174r": ("f174r/passC.tsv", [("f174r/passC_agreement.tsv", "f174r/passA.tsv", "f174r/passB.tsv")]),
 "f174v": ("f174v/passC.tsv", [("f174v/passC_agreement.tsv", "f174v/passA.tsv", "f174v/passB.tsv")]),
 "f174vB": ("f174vB/passC.tsv", [("f174vB/passC_agreement.tsv", "f174vB/passA.tsv", "f174vB/passB.tsv")]),
 "f175v": ("f175v/passC.tsv", [("f175v/passC_agreement.tsv", "f175v/passA.tsv", "f175v/passB.tsv")]),
 "f184r": ("f184r/passC.tsv", [("f184r/passC_agreement.tsv", "f184r/passA.tsv", "f184r/passB.tsv")]),
 "f185r": ("f185r/passC_rest90.tsv", [("f185r/passC_rest90_agreement.tsv", "f185r/passA_rest90.tsv", "f185r/passB_rest90.tsv")]),
 "f185r2": ("f185r2/passC.tsv", [("f185r2/passC_r_agreement.tsv", "f185r2/passA_r.tsv", "f185r2/passB_r.tsv"),
                                 ("f185r2/passC_v_agreement.tsv", "f185r2/passA_v.tsv", "f185r2/passB_v.tsv")]),
 "f178r": ("f178r/passC.tsv", [("f178r/passC_agreement.tsv", "f178r/passA.tsv", "f178r/passB.tsv")]),
 "f179r": ("f179r/passC.tsv", [("f179r/passC_agreement.tsv", "f179r/passA.tsv", "f179r/passB.tsv")]),
 "f178v": ("f178v/passC_L01-23.tsv", [("f178v/passC_agreement.tsv", "f178v/passA.tsv", "f178v/passB.tsv"),
                                      ("f178v/passC_L11-23_agreement.tsv", "f178v/passA_L11-23.tsv", "f178v/passB_L11-23.tsv")]),
}
def rd(p):
    return list(csv.DictReader(open(H / p), delimiter="\t"))
def notes(p):
    return {(r["passage"], r["pos"]): (r.get("note") or "") + " " + (r.get("alt") or "") for r in rd(p)}
stats = Counter(); sub = {}
for fol, (pc, ags) in SRC.items():
    agrows = []
    for ag, pa, pb in ags:
        NA, NB = notes(pa), notes(pb)
        for r in rd(ag):
            if r["merged"] in ("", "NONE") and r["status"] not in ("split",):
                continue
            if ag.startswith("f178v/passC_agreement") and int(r["passage"].lstrip("L")) > 10:
                continue  # L11-23 come from the second agreement file
            agrows.append((r["merged"] or "?", NA.get((r["passage"], r["posA"]), ""), NB.get((r["passage"], r["posB"]), "")))
    rows = rd(pc)
    a = [x[0] for x in agrows]; b = [r["sign_id"] for r in rows]
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    amap = {}
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal" or (op == "replace" and i2 - i1 == j2 - j1):
            for k in range(j2 - j1):
                amap[j1 + k] = i1 + k
    lab = []
    for j, r in enumerate(rows):
        s = r["sign_id"]
        if s == "X_NEW":
            stats["X_NEW"] += 1
            if j in amap:
                _, na, nb = agrows[amap[j]]
                ca, cb = cls(na), cls(nb)
                c = ca if (ca and (cb is None or cb == ca)) else (cb if ca is None else None)
                if c:
                    s = c; stats["classified"] += 1
                elif ca and cb:
                    stats["A_B_disagree"] += 1
            else:
                stats["unaligned"] += 1
        lab.append(s)
    sub[fol] = (rows, lab)
def piece(fol, rename=lambda p: p, keep=lambda p: True):
    rows, lab = sub[fol]
    return [(rename(r["passage"]), r["pos"], l, r["sign_id"]) for r, l in zip(rows, lab) if keep(r["passage"])]
L = {}
L["no87"] = piece("f178r", lambda p: "R" + p.lstrip("L")) + piece("f178v") + piece("f179r", lambda p: "V" + p.lstrip("L"))
L["no71"] = piece("f139v")
L["no86"] = (piece("f174r", lambda p: "f174r_" + p) + piece("f174v", lambda p: "f174v_" + p)
             + piece("f174vB", lambda p: f"f174v_L{int(p[1:]) + 11:02d}" if p.startswith("L") else "f175r_" + p,
                     lambda p: p[0] in "LR") + piece("f175v", lambda p: "f175v_" + p))
L["no90"] = piece("f184r", lambda p: "f184r_" + p) + piece("f185r") + piece("f185r2")
COMMITTED = {"no87": "passC_no87.tsv", "no71": "f139v/passC.tsv", "no86": "no86/passC_all.tsv", "no90": "no90/passC_all.tsv"}
bad = 0; cnt = Counter()
for k, seq in L.items():
    ref = [(r["passage"], r["sign_id"]) for r in rd(COMMITTED[k])]
    mine = [(p, o) for p, _, _, o in seq]
    if ref != mine:
        bad += 1; print(f"MISMATCH {k}: committed {len(ref)} rebuilt {len(mine)}", file=sys.stderr)
    with open(OUT / f"pool_{k}.tsv", "w") as f:
        f.write("passage\tpos\tsign_id\torig\n")
        for p, pos, l, o in seq:
            f.write(f"{p}\t{pos}\t{l}\t{o}\n")
            if o == "X_NEW" or l.startswith("X_"):
                cnt[(l, k)] += 1
with open(OUT / "subtype_counts.tsv", "w") as f:
    f.write("subtype\tno87\tno71\tno86\tno90\ttotal\n")
    for s in sorted({x for x, _ in cnt}, key=lambda s: -sum(cnt[(s, k)] for k in L)):
        f.write(s + "\t" + "\t".join(str(cnt[(s, k)]) for k in L) + f"\t{sum(cnt[(s, k)] for k in L)}\n")
print(dict(stats)); print(open(OUT / "subtype_counts.tsv").read())
sys.exit(1 if bad else 0)
