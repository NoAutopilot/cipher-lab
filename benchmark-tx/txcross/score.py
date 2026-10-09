#!/usr/bin/env python3
"""MQS-TX-CROSSWORD scorer (pushed with the pre-registration, before any answer exists).

Reads positions.tsv and answers_G1.tsv / answers_G2.tsv (qid, label, conf, note; label = a sheet id, OTHER or U).
Calibration: D-arm answers equal to the current sign / 30 (OTHER and U count as disagreement); gate >= 0.80.
Apply rule (crossword + image): a T-arm position takes the reader's label iff label != current sign, conf is H or M,
the label is a single-letter sign of the printed 1572 key, and the it16dip LM scores the label's letter above the
current letter in the same window flag.py used.  The same rule on the R arm gives the null file.  Writes applied_T.tsv,
applied_R.tsv, applied_Timg.tsv (image only: any H/M sheet-id change, no LM check, reported) and changes_T.tsv (the
list for the eye check).  Scoring itself is tools/tx_bench.py --paired against labels.tsv (commands in RESULTS.md).
"""
import csv, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from key_decode_lattice import LM, read_key, load_model  # noqa: E402
sys.path.insert(0, str(Path(__file__).resolve().parent))
from flag import BASE, KEY, RIGHT, A  # noqa: E402

HERE = Path(__file__).resolve().parent


def rd(p):
    return list(csv.DictReader(open(p, encoding="utf-8"), delimiter="\t"))


def main():
    rows = rd(BASE); key = read_key(KEY); lm = LM(load_model(A)); n1 = lm.n - 1
    vals = [key.get(r["sign"], "") for r in rows]
    text, start = "", []
    for v in vals:
        start.append(len(text)); text += v
    idx = {(r["line"], r["pos"]): i for i, r in enumerate(rows)}
    P = {p["qid"]: p for p in rd(HERE / "positions.tsv")}
    ans = {}
    for part in ("G1", "G2"):
        for a in rd(HERE / f"answers_{part}.tsv"):
            ans[a["qid"].strip()] = a
    missing = [q for q in P if q not in ans]
    D = [q for q in P if P[q]["arm"] == "D"]
    calib = sum(ans.get(q, {}).get("label", "").strip() == P[q]["sign"] for q in D) / len(D)

    def lmok(q, lab):
        i = idx[(P[q]["line"], P[q]["pos"])]
        left = text[max(0, start[i] - n1):start[i]]; right = text[start[i] + 1:start[i] + 1 + RIGHT]
        return lm.extend(left, key[lab] + right)[1] > lm.extend(left, vals[i] + right)[1]

    def apply(arm, use_lm):
        new = {}
        for q, p in P.items():
            a = ans.get(q)
            if p["arm"] != arm or not a:
                continue
            lab, conf = a["label"].strip(), a["conf"].strip().upper()
            if lab == p["sign"] or conf not in ("H", "M") or len(key.get(lab, "")) != 1:
                continue
            if use_lm and not lmok(q, lab):
                continue
            new[(p["line"], p["pos"])] = (q, lab)
        return new

    out = {}
    for name, arm, use_lm in (("T", "T", True), ("R", "R", True), ("Timg", "T", False)):
        new = apply(arm, use_lm); out[name] = new
        with open(HERE / f"applied_{name}.tsv", "w") as f:
            f.write("line\tpos\tsign\n")
            for r in rows:
                s = new.get((r["line"], r["pos"]), (None, r["sign"]))[1]
                f.write(f"{r['line']}\t{r['pos']}\t{s}\n")
    with open(HERE / "changes_T.tsv", "w") as f:
        f.write("qid\tline\tpos\tfrom\tto\tconf\tnote\n")
        for (l, p), (q, lab) in out["T"].items():
            f.write(f"{q}\t{l}\t{p}\t{P[q]['sign']}\t{lab}\t{ans[q]['conf']}\t{ans[q].get('note','')}\n")
    arms = {}
    for arm in "TDR":
        qs = [q for q in P if P[q]["arm"] == arm]
        lab = [ans.get(q, {}).get("label", "").strip() for q in qs]
        arms[arm] = dict(n=len(qs), same=sum(l == P[q]["sign"] for q, l in zip(qs, lab)),
                         other_or_u=sum(l in ("OTHER", "U", "") for l in lab))
    print(f"missing answers {len(missing)}; calibration D same {calib:.3f} (gate >= 0.80)")
    print("arms", arms)
    print({k: len(v) for k, v in out.items()}, "changes applied (T crossword+image, R null, Timg image only)")


if __name__ == "__main__":
    main()
