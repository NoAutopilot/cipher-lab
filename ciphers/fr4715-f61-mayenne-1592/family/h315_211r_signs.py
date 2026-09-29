#!/usr/bin/env python3
"""H315 (runner 12 session_012eShPsWwW3quuzzUNV7nW5, 29 Sept 2026): the sign half of a held-out period check -- the one cipher run of fr.3983 f.211r
(Mayenne to de Diou, 1 Apr 1593; line 2; ASKS 93's desk pack images/person_pack_211r/f211r_run.jpg, 3180 x 480 at 2x from the native, used in no fit)
cut into two segments under the 2500-px rule (family/sheets/f211r_run_s1.jpg = sheet x 0-1700, _s2.jpg = sheet x 1480-3180; a red bar marks the
overlap). Two independent blind Opus passes (A, B), same prompt (scripts/PROMPTS.md H315), atlas codes; s1 lists signs centred left of its x 1600,
s2 signs centred at or right of its x 120 (sheet x 1600), so each sign is listed once. This script joins each pass to sheet x (s2 + 1480), writes the
long-format passes family/passes/f211r_pass{A,B}.tsv and runs tools/reconcile_passes.py (nw) on them.
Gate, fixed before the calls: identical-column share >= 0.80 (the family gate, H34) -> the reconciled draft stands as the run's sign sequence (agreed
columns at the passes' own grade, disagreements flagged L); below 0.80 the run's signs stay unread and H317 does not run on them.
python3 h315_211r_signs.py [--check]"""
import csv, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(f"{HERE}/../../..")
def load(tag):
    rows = []
    for seg, off in (("s1", 0), ("s2", 1480)):
        f = f"{HERE}/passes/f211r_s{seg[1]}_signs{tag}.tsv"
        for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t"):
            rows.append((int(float(r["x_px"])) + off, r["sign"].strip(), r["conf"].strip(), r.get("note", "").strip()))
    rows.sort(); out = ["line\tpos\tsign\tconf\tx_sheet\tnote"] + [f"L02\t{i}\t{s}\t{c}\t{x}\t{n}" for i, (x, s, c, n) in enumerate(rows, 1)]
    p = f"{HERE}/passes/f211r_pass{tag}.tsv"; open(p, "w").write("\n".join(out) + "\n"); return p, [s for _, s, _, _ in rows]
pa, sa = load("A"); pb, sb = load("B")
od = f"{HERE}/passes/f211r_rec"; os.makedirs(od, exist_ok=True)
rp = subprocess.run([sys.executable, f"{ROOT}/tools/reconcile_passes.py", pa, pb, "--out-dir", od, "--method", "nw"], capture_output=True, text=True)
ag = list(csv.DictReader(open(f"{od}/agreement.tsv"), delimiter="\t")) if os.path.exists(f"{od}/agreement.tsv") else []
summary = [l for l in rp.stdout.splitlines() if l.strip()][-3:]
txt = f"pass A {len(sa)} signs: {' '.join(sa)}\npass B {len(sb)} signs: {' '.join(sb)}\nreconcile_passes (nw): " + " | ".join(summary) + "\n"
open(f"{HERE}/h315_211r_signs_result.txt.tmp", "w").write(txt)
res = f"{HERE}/h315_211r_signs_result.txt"
if "--check" in sys.argv:
    ok = os.path.exists(res) and open(res).read() == txt; os.remove(f"{HERE}/h315_211r_signs_result.txt.tmp"); print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
os.replace(f"{HERE}/h315_211r_signs_result.txt.tmp", res); print(txt, end="")
