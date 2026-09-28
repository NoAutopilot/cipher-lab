#!/usr/bin/env python3
"""H59 (28 Sept 2026, runner session_01J8hunWPcE7QYcpCx59CUHV): apply the one reconciliation call's verdict (family/passes/
f108v3z_recon_verdict.tsv: line, position, sign, conf, note) to the aligned draft of the two f.108v sign passes
(family/passes/f108v3z_recon_task.tsv, 315 columns, 136 to settle). Pre-registered gate (CAMPAIGN.md H59): a draft with
<= 10% of its columns still flagged, where a column is still flagged when it was to settle and the reconciler answered
at confidence l or gave no answer; a 'none' answer drops the column. Grades (rule 4): agreed columns keep the passes'
lower confidence (H/M), settled columns are M (one reconciler's reading of the crop), flagged columns L. Output
family/passes/f108v3z_draft_reconciled.tsv and scripts/f61recon108v_result.txt; --check exits 1 when stale.
"""
import csv, os, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); FAM = os.path.abspath(f"{HERE}/../family/passes")
def main():
    task = [r for r in csv.DictReader((l for l in open(f"{FAM}/f108v3z_recon_task.tsv") if not l.startswith("#")), delimiter="\t")]
    ver = {(r["line"], r["position"]): r for r in csv.DictReader((l for l in open(f"{FAM}/f108v3z_recon_verdict.tsv") if not l.startswith("#")), delimiter="\t")}
    out_rows = []; n_settle = n_flag = n_none = 0; conf = Counter()
    for r in task:
        if r["settle"] == "yes":
            n_settle += 1; v = ver.get((r["line"], r["position"]))
            if not v: n_flag += 1; out_rows.append((r["line"], r["position"], r["sign"], "L", "unanswered")); continue
            conf[v["conf"].strip().lower()] += 1
            if v["sign"].strip().lower() == "none": n_none += 1; continue
            if v["conf"].strip().lower() == "l": n_flag += 1; out_rows.append((r["line"], r["position"], v["sign"].strip(), "L", "reconciler l"))
            else: out_rows.append((r["line"], r["position"], v["sign"].strip(), "M", "reconciled"))
        else:
            out_rows.append((r["line"], r["position"], r["sign"], r["confidence"], r["why"]))
    total = len(task); kept = len(out_rows)
    inv = Counter(s for _, _, s, _, _ in out_rows)
    txt = [f"H59: f.108v reconciled draft -- {total} aligned columns, {n_settle} to settle: reconciler answered {sum(conf.values())} (h {conf['h']}, m {conf['m']}, l {conf['l']}), none {n_none}, unanswered {n_settle - sum(conf.values())}",
           f"still flagged (l or unanswered) {n_flag}/{total} = {n_flag/total:.3f}; kept columns {kept}",
           "inventory: " + " ".join(f"{c}:{n}" for c, n in inv.most_common()),
           "ZHOOK per band: " + " ".join(f"{b}:{sum(1 for l, _, s, _, _ in out_rows if l == b and s == 'ZHOOK')}" for b in [f'L0{i}' for i in range(1, 8)]),
           f"GATE H59 (<= 10% still flagged): {'PASS' if n_flag/total <= 0.10 else 'FAIL'} -- grade of every settled column M (one reconciler), never higher; a transcription for a person's gloss reading, not a key"]
    txt = "\n".join(txt) + "\n"
    tsv = "# f108v3z_draft_reconciled.tsv -- H59, 28 Sept 2026: the two-pass NW draft with the 136 disagreement columns settled by one Opus reconciliation call (grade M) or flagged L; see scripts/f61recon108v.py.\nline\tposition\tsign\tgrade\twhy\n" + "".join("\t".join(map(str, r)) + "\n" for r in out_rows)
    rp, dp = f"{HERE}/f61recon108v_result.txt", f"{FAM}/f108v3z_draft_reconciled.tsv"
    if "--check" in sys.argv:
        ok = os.path.exists(rp) and open(rp).read() == txt and os.path.exists(dp) and open(dp).read() == tsv; print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(rp, "w").write(txt); open(dp, "w").write(tsv); print(txt, end="")
if __name__ == "__main__":
    main()
