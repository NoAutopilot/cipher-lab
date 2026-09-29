#!/usr/bin/env python3
"""H348 (runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ, 29 Sept 2026), written before the calls returned: f.106r rows 13-18 sign passes
(passes/f106r_signs{A,B}_c3.tsv, two blind Opus calls) normalised as f106r_pipeline.py does, reconciled with tools/reconcile_passes.py (nw) into
passes/recf106r_c3/, sign agreement reported; rows 1-18 pooled into passes/recf106rall18/ciphertext_draft.tsv (recf106rall + recf106r_c3); then H342's
order statistic (h342_beam_seqgain.py's leaf(), unchanged) on the pooled draft. Pre-stated: 'order signal for v7 in the secretary's hand' iff gain(v7)
> the binned gains' p95; a miss is untestable (not a negative) if the run count is under 50, since H346 measured power 0.63 / 1.00 at 35 runs.
python3 h348_106r_rows18.py [--check]"""
import csv, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(f"{HERE}/../../.."); P = f"{HERE}/passes"; ARGS = sys.argv[1:]; out = []
def norm(path):
    rows = []
    for line in open(path):
        line = line.rstrip("\n")
        if not line.strip() or line.startswith("#") or line.startswith("line\t"): continue
        c = line.split("\t"); c += [""] * (7 - len(c)); v = c[3].strip().lower()
        c[3] = {"high": "h", "medium": "m", "med": "m", "low": "l"}.get(v, v[:1] if v[:1] in "hml" else "m"); rows.append(c[:7])
    open(path, "w").write("line\tpos\tsign\tconf\tsegment\tx_px\tnote\n" + "\n".join("\t".join(r) for r in rows) + "\n")
for pas in "AB": norm(f"{P}/f106r_signs{pas}_c3.tsv")
os.makedirs(f"{P}/recf106r_c3", exist_ok=True)
subprocess.run([sys.executable, f"{ROOT}/tools/reconcile_passes.py", f"{P}/f106r_signsA_c3.tsv", f"{P}/f106r_signsB_c3.tsv", "--out-dir", f"{P}/recf106r_c3", "--method", "nw"], capture_output=True, text=True, check=True)
ag = tot = 0
for row in csv.DictReader(open(f"{P}/recf106r_c3/agreement.tsv"), delimiter="\t"):
    a, t = int(row["agree"]), int(row["columns"]); ag += a; tot += t; out.append(f"{row['line']}: signs A {row['signs_A']} B {row['signs_B']} agree {a}/{t}")
out.append(f"c3 SIGN AGREEMENT {ag}/{tot} = {ag / tot if tot else 0:.3f}")
os.makedirs(f"{P}/recf106rall18", exist_ok=True)
lines = list(open(f"{P}/recf106rall/ciphertext_draft.tsv")) + [l for l in open(f"{P}/recf106r_c3/ciphertext_draft.tsv") if not l.startswith("line\t")]
open(f"{P}/recf106rall18/ciphertext_draft.tsv", "w").write("".join(lines))
h342 = open(f"{HERE}/h342_beam_seqgain.py").read(); h342 = h342[:h342.index("res = {}")]
g = {"__file__": f"{HERE}/h342_beam_seqgain.py", "__name__": "h348"}; sys.argv = [sys.argv[0]]; exec(compile(h342, "h342_prefix", "exec"), g)
gv, p95, null, nr, ns = g["leaf"]("recf106rall18")
out.append(f"rows 1-18 pooled: runs {nr}, signs {ns}; gain(v7) {gv:.4f}; binned gains mean {sum(null) / 100:.4f} p95 {p95:.4f}, >= v7 {sum(x >= gv for x in null)}/100")
out.append("read-out: " + ("order signal for v7 in the secretary's hand" if gv > p95 else ("no order signal; untestable at this N (runs < 50), not a negative" if nr < 50 else "no order signal at >= 50 runs")))
txt = "\n".join(out) + "\n"; rs = f"{HERE}/h348_106r_rows18_result.txt"
if "--check" in ARGS:
    ok = os.path.exists(rs) and open(rs).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(rs, "w").write(txt); print(txt, end="")
