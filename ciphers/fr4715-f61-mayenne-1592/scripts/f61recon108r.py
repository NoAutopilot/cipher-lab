#!/usr/bin/env python3
"""H108 (28 Sept 2026, runner 5 session_01RbeePKZVn83gNfES8yFmhe): a reconciled sign draft of fr.3983 f.108r rows L04-L06,
the rows of the H107 prediction and of ASKS 88's gloss. L04/L05 from the H34 passes (scripts/pass108gA/gB_classes.tsv, crops
images/f108g/); L06 from two fresh blind passes on the whole-row re-cut (scripts/pass108hC/hD_L06.tsv, crops images/f108h/),
since the H34 cut halves L06. PLAIN rows dropped; alignment tools/reconcile_passes.nw (pass 1 the reference).

  python3 scripts/f61recon108r.py task            -> scripts/f61recon108r_task.tsv (settle = yes where the passes differ)
  python3 scripts/f61recon108r.py apply [--check] -> scripts/f61recon108r_draft.tsv, scripts/f61recon108r_result.txt

Pre-registered (scripts/PROMPTS.md "H108", pushed before the calls): the reconciler settles only settle=yes columns; 'none'
drops the column; an answer at confidence l or no answer leaves the column flagged (grade L). Grades (rule 4 style for a
transcription): agreed columns keep the passes' lower confidence, settled columns M (one reconciler), flagged L. Gate
(the H59 gate): <= 10% of the columns still flagged. A shape draft for the H112 judge and the person's gloss, not a reading.
"""
import csv, os, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); TGT = os.path.dirname(HERE)
sys.path.insert(0, os.path.abspath(f"{TGT}/../../tools"))
from reconcile_passes import nw
SRC = {"L04": ("pass108gA_classes.tsv", "pass108gB_classes.tsv", "images/f108g/f108g"),
       "L05": ("pass108gA_classes.tsv", "pass108gB_classes.tsv", "images/f108g/f108g"),
       "L06": ("pass108hC_L06.tsv", "pass108hD_L06.tsv", "images/f108h/f108h")}
CONF = {"h": "H", "m": "M", "l": "L"}
def load(fn, line):
    return [r for r in csv.DictReader((l for l in open(f"{HERE}/{fn}") if not l.startswith("#")), delimiter="\t")
            if r["line"] == line and r["sign"].strip() != "PLAIN"]
def lower(a, b): return max(a, b, key="HML".index)
def task():
    out = []
    for line, (fa, fb, crop) in SRC.items():
        A, B = load(fa, line), load(fb, line); pos = 0
        for i, j in nw([r["sign"].strip() for r in A], [r["sign"].strip() for r in B]):
            pos += 1; a = A[i] if i is not None else None; b = B[j] if j is not None else None
            sa, sb = (a["sign"].strip() if a else "-"), (b["sign"].strip() if b else "-")
            ref = a or b; seg = ref["segment"].strip()
            ca = CONF.get((a or {}).get("conf", "l").strip().lower(), "L") if a else "L"
            cb = CONF.get((b or {}).get("conf", "l").strip().lower(), "L") if b else "L"
            if sa == sb: why, settle = ("agree" if lower(ca, cb) != "L" else "agree-flagged"), "no"
            elif a and b: why, settle = "differ", "yes"
            else: why, settle = ("B:-" if a else "A:-"), "yes"
            out.append([line, pos, sa if a else sb, lower(ca, cb), "" if sa == sb else (f"B:{sb}" if a else f"A:-"), why, settle,
                        a["segment"].strip() if a else "", a["x_px"].strip() if a else "", b["segment"].strip() if b else "",
                        b["x_px"].strip() if b else "", f"ciphers/fr4715-f61-mayenne-1592/{crop}_{line}_{seg}.jpg"])
    hdr = "line\tposition\tsign\tconfidence\talt\twhy\tsettle\tsegA\txA\tsegB\txB\tcrop\n"
    txt = ("# H108 reconciliation task (28 Sept 2026): f.108r L04/L05 (H34 passes A/B) and L06 (H108 passes C/D, whole row), NW-aligned; "
           "sign = the first pass's code (or the other's where the first has none); alt = the other pass's code; settle = yes where they differ.\n" + hdr
           + "".join("\t".join(map(str, r)) + "\n" for r in out))
    open(f"{HERE}/f61recon108r_task.tsv", "w").write(txt)
    n = Counter(r[0] for r in out); s = Counter(r[0] for r in out if r[6] == "yes")
    print("columns per line:", dict(n), "to settle:", dict(s), f"total {len(out)}, settle {sum(s.values())}, agreement {1 - sum(s.values()) / len(out):.3f}")
def apply():
    T = list(csv.DictReader((l for l in open(f"{HERE}/f61recon108r_task.tsv") if not l.startswith("#")), delimiter="\t"))
    V = {(r["line"].strip(), r["position"].strip()): r for r in csv.DictReader((l for l in open(f"{HERE}/f61recon108r_verdict.tsv") if not l.startswith("#")), delimiter="\t")}
    rows, conf, n_set, n_flag, n_none = [], Counter(), 0, 0, 0
    for r in T:
        seg, x = (r["segA"], r["xA"]) if r["segA"] else (r["segB"], r["xB"])
        if r["settle"] == "yes":
            n_set += 1; v = V.get((r["line"], r["position"]))
            if not v: n_flag += 1; rows.append((r["line"], r["sign"], "L", "unanswered", seg, x)); continue
            c = v["conf"].strip().lower(); conf[c] += 1
            if v["sign"].strip().lower() == "none": n_none += 1; continue
            if c == "l": n_flag += 1; rows.append((r["line"], v["sign"].strip(), "L", "reconciler l", seg, x))
            else: rows.append((r["line"], v["sign"].strip(), "M", "reconciled", seg, x))
        else: rows.append((r["line"], r["sign"], r["confidence"], r["why"], seg, x))
    out, k = [], Counter()
    for line, s, g, why, seg, x in rows: k[line] += 1; out.append((line, k[line], s, g, why, seg, x))
    tot = len(T); inv = Counter(r[2] for r in out)
    txt = [f"H108: f.108r L04-L06 reconciled draft -- {tot} aligned columns, {n_set} to settle: reconciler answered {sum(conf.values())} (h {conf['h']}, m {conf['m']}, l {conf['l']}), none {n_none}, unanswered {n_set - sum(conf.values())}",
           f"still flagged (l or unanswered) {n_flag}/{tot} = {n_flag / tot:.3f}; kept columns {len(out)} (" + ", ".join(f"{l} {k[l]}" for l in sorted(k)) + ")",
           "inventory: " + " ".join(f"{c}:{n}" for c, n in inv.most_common()),
           f"GATE H108 draft (<= 10% still flagged): {'PASS' if n_flag / tot <= 0.10 else 'FAIL'} -- settled columns grade M, never higher; a shape draft, not a reading"]
    txt = "\n".join(txt) + "\n"
    tsv = ("# f61recon108r_draft.tsv -- H108, 28 Sept 2026: f.108r L04-L06, two passes per row NW-aligned, disagreements settled by one Opus reconciliation call (M) or flagged L; seg/x from the first pass that has the sign (L04/L05 crops images/f108g/, L06 images/f108h/); see scripts/f61recon108r.py.\n"
           "line\tposition\tsign\tgrade\twhy\tsegment\tx_px\n" + "".join("\t".join(map(str, r)) + "\n" for r in out))
    rp, dp = f"{HERE}/f61recon108r_result.txt", f"{HERE}/f61recon108r_draft.tsv"
    if "--check" in sys.argv:
        ok = os.path.exists(rp) and open(rp).read() == txt and os.path.exists(dp) and open(dp).read() == tsv; print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(rp, "w").write(txt); open(dp, "w").write(tsv); print(txt, end="")
if __name__ == "__main__":
    {"task": task, "apply": apply}[sys.argv[1]]()
