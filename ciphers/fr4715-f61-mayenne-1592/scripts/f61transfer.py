#!/usr/bin/env python3
"""F61-TRANSFER (campaign step H19, 27 Sept 2026): does the cell map fitted on f.61 read a second letter of the same office?

Pre-registered before the f.108 passes were read. Inputs: scripts/pass108A_classes.tsv and pass108B_classes.tsv (two
blind Opus reads of images/f108sheetB_L02.jpg and L03.jpg -- the two cipher lines under Tomokiyo's overlay -- with the
shape atlas; a sign the atlas lacks is OTHER), reconciled by tools/reconcile_passes.py; the reconciled draft's sign per
column (pass A's where they differ, flagged) is the class sequence. Reference: scripts/tomokiyo_spans_3983.tsv (T1 on
band L02, T2 on band L03; grade H for the test). Map: the f.61 cells with the dash-share null rule (scripts/f61judge.py
CELLS, 9 cells), NOT refitted. Score: scripts/f61cal.py's DP (align() from f61crib.py) between each reference and its
band's class sequence, matched letters pooled over the 84. Controls: 20 maps with the 9 cells permuted across the 9
classes (seed 1), same DP. Gate (H19): pooled match above every one of the 20 permuted-map scores. Reported, not gated:
the pass agreement on the two bands and the share of signs in classes the atlas lacks.

  python3 scripts/f61transfer.py [--check]   (from the target folder)
"""
import csv, os, random, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(f"{HERE}/../../.."); sys.path.insert(0, HERE)
from f61crib import align
from f61judge import CELLS
def main():
    d = tempfile.mkdtemp(prefix="f61transfer_")
    r = subprocess.run([sys.executable, f"{ROOT}/tools/reconcile_passes.py", f"{HERE}/pass108A_classes.tsv", f"{HERE}/pass108B_classes.tsv",
                        "--out-dir", d, "--method", "nw"], capture_output=True, text=True)
    if r.returncode: raise SystemExit(r.stdout + r.stderr)
    out = ["reconcile: " + " | ".join(l for l in r.stdout.strip().splitlines() if not l.startswith("wrote "))]
    seq = {}
    for row in csv.DictReader(open(f"{d}/ciphertext_draft.tsv"), delimiter="\t"):
        seq.setdefault(row["line"], []).append(row["sign"])
    refs = [l.rstrip("\n").split("\t") for l in open(f"{HERE}/tomokiyo_spans_3983.tsv") if l[0] == "T"]
    band = {"T1": "L02", "T2": "L03"}
    cmap = {c: tuple(v.split("/")) for c, v in CELLS.items()}
    def score(m):
        tot = mat = 0
        for s, _, markup, _ in refs:
            mt, _ = align(markup, seq.get(band[s], []), m); mat += mt; tot += len(markup)
        return mat, tot
    mat, tot = score(cmap)
    for s, _, markup, _ in refs:
        sq = seq.get(band[s], []); other = sum(1 for c in sq if c == "OTHER")
        out.append(f"  {s} on {band[s]}: {len(sq)} signs ({other} OTHER), reference {len(markup)} letters, matched {align(markup, sq, cmap)[0]}")
    rng = random.Random(1); labs = sorted(cmap); ctrl = []
    for _ in range(20):
        v = [cmap[l] for l in labs]; rng.shuffle(v); ctrl.append(score(dict(zip(labs, v)))[0] / tot)
    out.append(f"TRANSFER: f.61 map, not refitted, on f.108: {mat}/{tot} = {mat/tot:.3f}; 20 permuted maps mean {sum(ctrl)/20:.3f} max {max(ctrl):.3f}")
    out.append(f"GATE H19 (above every permuted map): {'PASS' if mat/tot > max(ctrl) else 'FAIL'}  (f.61 in-sample with the same cells: 49/55)")
    txt = "\n".join(out) + "\n"; res = f"{HERE}/f61transfer_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt
        print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    main()
