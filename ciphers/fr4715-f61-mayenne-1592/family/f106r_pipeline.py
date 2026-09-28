#!/usr/bin/env python3
"""F61-FAMILY-3 (28 Sept 2026), campaign step H31: fr.3983 f.106r (Mayenne's secretary), first six cipher rows cut at 3x
(sheets/f106r, cut_bands.py, hand-set centres), two blind Opus sign passes (passes/f106r_signsA/B.tsv) and two blind Opus
gloss passes (passes/f106r_glossA/B.tsv), prompts in passes/PROMPTS_f188_f184_f106.md. This pipeline (1) reconciles the sign
passes with tools/reconcile_passes.py (nw) into passes/recf106r/ and reports the agreement, (2) reports the gloss word
agreement per band (words both passes read identically, case-folded, by difflib), (3) applies the brief's gate -- gloss
passes agreeing under 60% on words => the leaf is HELD (no key rows; the reason goes to KEY.md) -- and (4) on a pass runs
align_period.py f106r (the interlinear alignment the other leaves used) whose rows go to key_period_f106.tsv.
  python3 f106r_pipeline.py [--force]   (from the family folder; --force runs the alignment for the record even when held)
"""
import csv, difflib, os, subprocess, sys
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(f"{HERE}/../../.."); P = f"{HERE}/passes"
def norm(path, kind):
    rows = []
    for line in open(path):
        line = line.rstrip("\n")
        if not line.strip() or line.startswith("#") or line.startswith("line\t"): continue
        c = line.split("\t"); n = 7 if kind == "signs" else 8; c += [""] * (n - len(c)); k = 3 if kind == "signs" else 4
        v = c[k].strip().lower(); c[k] = {"high": "h", "medium": "m", "med": "m", "low": "l"}.get(v, v[:1] if v[:1] in "hml" else "m"); rows.append(c[:n])
    hdr = "line\tpos\tsign\tconf\tsegment\tx_px\tnote" if kind == "signs" else "line\tpos\tkind\tword\tconf\tsegment\tx0_px\tx1_px"
    open(path, "w").write(hdr + "\n" + "\n".join("\t".join(r) for r in rows) + "\n"); return rows
for pas in ("signsA", "signsB"): norm(f"{P}/f106r_{pas}.tsv", "signs")
os.makedirs(f"{P}/recf106r", exist_ok=True)
r = subprocess.run([sys.executable, f"{ROOT}/tools/reconcile_passes.py", f"{P}/f106r_signsA.tsv", f"{P}/f106r_signsB.tsv", "--out-dir", f"{P}/recf106r", "--method", "nw"], capture_output=True, text=True)
print(r.stdout.strip()[-400:]); print(r.stderr.strip()[-300:])
agree = tot = 0
for row in csv.DictReader(open(f"{P}/recf106r/agreement.tsv"), delimiter="\t"):
    a, t = int(row["agree"]), int(row["columns"]); agree += a; tot += t; print(f"{row['line']}: signs {a}/{t} = {a/t if t else 0:.2f}")
sign_frac = agree / tot if tot else 0; print(f"SIGN AGREEMENT {agree}/{tot} = {sign_frac:.3f}")
G = {}
for pas in "AB":
    rows = norm(f"{P}/f106r_gloss{pas}.tsv", "gloss"); d = defaultdict(list)
    for c in rows:
        if c[2].strip().lower() == "dash" or c[3].strip() in ("-", "--"): continue
        d[c[0]].append(c[3].strip().lower())
    G[pas] = d
ag = na = nb = 0
for band in sorted(set(G["A"]) | set(G["B"])):
    wa, wb = G["A"].get(band, []), G["B"].get(band, []); sm = difflib.SequenceMatcher(None, wa, wb, autojunk=False)
    m = sum(i2 - i1 for tag, i1, i2, j1, j2 in sm.get_opcodes() if tag == "equal"); ag += m; na += len(wa); nb += len(wb)
    print(f"{band}: gloss words A {len(wa)} B {len(wb)} identical {m}")
gloss_frac = 2 * ag / (na + nb) if na + nb else 0
print(f"GLOSS WORD AGREEMENT {ag} identical of A {na} / B {nb} = {gloss_frac:.3f}")
held = gloss_frac < 0.60
print(f"GATE (brief: gloss passes agree >= 60% on words): {'HELD' if held else 'PASS'} ({gloss_frac:.3f}); sign agreement {sign_frac:.3f}")
open(f"{P}/f106r_gate.txt", "w").write(f"sign_agreement\t{agree}/{tot}\t{sign_frac:.3f}\ngloss_word_agreement\t{ag}/{na}|{nb}\t{gloss_frac:.3f}\ngate_60pct\t{'HELD' if held else 'PASS'}\n")
if held and "--force" not in sys.argv: sys.exit(3)
r = subprocess.run([sys.executable, f"{HERE}/align_period.py", "f106r", "fr.3983 f.106r"], capture_output=True, text=True, cwd=HERE)
print(r.stdout.strip()[-1200:]); print(r.stderr.strip()[-400:])
out = f"{HERE}/key_period_f106.tsv" if not held else f"{HERE}/key_period_f106_held.tsv"
with open(out, "w") as f:
    f.write(f"# {os.path.basename(out)} -- F61-FAMILY-3, 28 Sept 2026: period key rows from the interlinear gloss of fr.3983 f.106r, first six cipher rows at 3x (sheets/f106r); sign passes {sign_frac:.3f}, gloss word agreement {gloss_frac:.3f}, gate {'HELD (kept for the record only, not merged)' if held else 'PASS'}. Key source: period; grade C per pair; nothing fitted.\n")
    f.write(open(f"{P}/f106r_keyrows.tsv").read())
print("wrote", out)
