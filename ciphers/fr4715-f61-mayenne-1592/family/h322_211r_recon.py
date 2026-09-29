#!/usr/bin/env python3
"""H322 (runner 12 session_012eShPsWwW3quuzzUNV7nW5, 29 Sept 2026): settle H315's two disagreement columns on fr.3983 f.211r's cipher run (col 13
EBR_A/EBR_B, col 17 VBAR_A/EBR_B) by one blind Opus forced choice among the three atlas shapes (scripts/f61_atlas.tsv wording): EBRA, EBRB, VBARA, or
unclear. Tiles from the 2x strip images/person_pack_211r/f211r_run.jpg as H324 (x = the two passes' mean, crop x +-110, y 140-420): the two targets and,
as known answers, the run's own columns both passes agreed: EBR_B at cols 5 and 14, VBAR_A at cols 1 and 18 (EBR_A has no agreed column in the run).
8 tiles would be too few to shuffle usefully, so each known tile appears once and the targets once: 6 tiles, ids R01..R06, seed 322.
Gate, fixed before the call: 4/4 known answers right, else CONTROL FAIL (both columns stay flagged L). Read-out: each target takes the answered code at
grade M; 'unclear' leaves it flagged. The reconciled sequence is written to family/passes/f211r_rec/ciphertext_h322.tsv.
python3 h322_211r_recon.py tiles SCRATCH | score [--check]"""
import csv, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; sys.path.insert(0, HERE)
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
dr = rd(f"{P}/f211r_rec/ciphertext_draft.tsv"); xa = rd(f"{P}/f211r_passA.tsv"); xb = rd(f"{P}/f211r_passB.tsv")
X = {int(r["position"]): (int(a["x_sheet"]) + int(b["x_sheet"])) // 2 for r, a, b in zip(dr, xa, xb)}
ITEMS = [("TARGET", 13), ("TARGET", 17), ("EBRB", 5), ("EBRB", 14), ("VBARA", 1), ("VBARA", 18)]
def tiles(scratch):
    from PIL import Image
    import h302_ll_text as h
    its = ITEMS[:]; random.Random(322).shuffle(its); im = Image.open(f"{HERE}/../images/person_pack_211r/f211r_run.jpg").convert("L")
    os.makedirs(f"{scratch}/h322", exist_ok=True); h.sheet([(k, im.crop((X[c] - 110, 140, X[c] + 110, 420))) for k, c in its], f"{scratch}/h322/sheet_01.jpg", "R")
    open(f"{HERE}/h322_items.tsv", "w").write("item\tkind\tcol\n" + "".join(f"R{n:02d}\t{k}\t{c}\n" for n, (k, c) in enumerate(its, 1))); print(len(its), "tiles")
def score():
    its = rd(f"{HERE}/h322_items.tsv"); a = {r["tile"]: r["answer"].strip().upper() for r in rd(f"{P}/h322_forced.tsv")}
    kn = [(r, a.get(r["item"])) for r in its if r["kind"] != "TARGET"]; ok = sum(ans == r["kind"] for r, ans in kn)
    out = ["known: " + " ".join(f"col{r['col']}={ans} (want {r['kind']})" for r, ans in kn) + f"; right {ok}/4"]
    code = {"EBRA": "EBR_A", "EBRB": "EBR_B", "VBARA": "VBAR_A"}; settle = {}
    if ok < 4: out.append("gate: CONTROL FAIL; cols 13 and 17 stay flagged L")
    else:
        for r in its:
            if r["kind"] == "TARGET": settle[int(r["col"])] = code.get(a.get(r["item"]))
        out.append("gate passes; settled (grade M): " + ", ".join(f"col {c} -> {v or 'unclear (stays L)'}" for c, v in sorted(settle.items())))
    rows = ["line\tposition\tsign\tconfidence\tsource"]
    for r in dr:
        c = int(r["position"]); s = settle.get(c) or r["sign"]; g = "M" if settle.get(c) else ("L" if c in (13, 17) else r["confidence"])
        rows.append(f"L02\t{c}\t{s}\t{g}\t{'H322' if settle.get(c) else 'H315'}")
    out.append("sequence: " + " ".join(x.split("\t")[2] for x in rows[1:]))
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h322_211r_recon_result.txt"
    if "--check" in sys.argv:
        k = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if k else "STALE"); sys.exit(0 if k else 1)
    open(res, "w").write(txt); open(f"{P}/f211r_rec/ciphertext_h322.tsv", "w").write("\n".join(rows) + "\n"); print(txt, end="")
if __name__ == "__main__":
    tiles(sys.argv[2]) if sys.argv[1] == "tiles" else score()
