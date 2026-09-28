#!/usr/bin/env python3
"""F61-FAMILY-2 (28 Sept 2026): f.101r pass pipeline. Concatenates the per-chunk pass files passes/f101r_<pass>_c<k>.tsv
(pass in signsA, signsB, glossA, glossB; chunks of 8 bands, prompts in passes/prompts_f101r/) into passes/f101r_<pass>.tsv,
runs tools/reconcile_passes.py (nw) on the two sign passes into passes/recf101r/, reports per-band and overall sign agreement
(identical aligned columns / aligned columns) and gloss word agreement (words both passes read identically, case-folded,
per band, by difflib), and lists the bands whose sign agreement is under 70% (the brief's re-cut threshold).
  python3 f101r_pipeline.py [--chunks 1,2,...]     (from the family folder)
"""
import csv, difflib, glob, os, re, subprocess, sys
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(f"{HERE}/../../.."); P = f"{HERE}/passes"
want = [int(v) for v in sys.argv[sys.argv.index("--chunks") + 1].split(",")] if "--chunks" in sys.argv else None
def norm_conf(v):
    v = (v or "").strip().lower(); return {"high": "h", "medium": "m", "med": "m", "low": "l"}.get(v, v or "m")[0]
for pas in ("signsA", "signsB", "glossA", "glossB"):
    files = sorted(glob.glob(f"{P}/f101r_{pas}_c*.tsv"), key=lambda f: int(re.search(r"_c(\d+)\.tsv", f).group(1)))
    if want: files = [f for f in files if int(re.search(r"_c(\d+)\.tsv", f).group(1)) in want]
    rows = []; hdr = None
    for f in files:
        with open(f) as fh:
            for i, line in enumerate(fh):
                line = line.rstrip("\n")
                if not line.strip() or line.startswith("#"): continue
                if line.startswith("line\t"): hdr = line; continue
                cells = line.split("\t")
                if len(cells) < 7: cells += [""] * (7 - len(cells))
                cells[3 if pas.startswith("signs") else 4] = norm_conf(cells[3 if pas.startswith("signs") else 4])
                rows.append("\t".join(cells[:8 if pas.startswith("gloss") else 7]))
    with open(f"{P}/f101r_{pas}.tsv", "w") as out:
        out.write((hdr or ("line\tpos\tsign\tconf\tsegment\tx_px\tnote" if pas.startswith("signs") else "line\tpos\tkind\tword\tconf\tsegment\tx0_px\tx1_px")) + "\n" + "\n".join(rows) + "\n")
    print(pas, len(files), "chunks", len(rows), "rows")
os.makedirs(f"{P}/recf101r", exist_ok=True)
r = subprocess.run([sys.executable, f"{ROOT}/tools/reconcile_passes.py", f"{P}/f101r_signsA.tsv", f"{P}/f101r_signsB.tsv", "--out-dir", f"{P}/recf101r", "--method", "nw"], capture_output=True, text=True)
print(r.stdout.strip()[-1500:]); print(r.stderr.strip()[-500:])
# per-band sign agreement from agreement.tsv / ciphertext_draft.tsv
agree = defaultdict(lambda: [0, 0])
ag = f"{P}/recf101r/agreement.tsv"
if os.path.exists(ag):
    rd = list(csv.DictReader(open(ag), delimiter="\t"))
    if rd:
        cols = rd[0].keys(); print("agreement.tsv columns:", list(cols))
        for row in rd:
            ln = row.get("line") or row.get("row") or ""
            key = "agree" if "agree" in row else ("status" if "status" in row else None)
            if key: agree[ln][1] += 1; agree[ln][0] += 1 if str(row[key]).lower() in ("1", "true", "yes", "agree", "identical", "same") else 0
low = []
for ln in sorted(agree):
    a, t = agree[ln]; frac = a / t if t else 0
    print(f"{ln}: signs {a}/{t} = {frac:.2f}" + ("  <70%" if frac < 0.7 else ""))
    if frac < 0.7: low.append(ln)
tot = sum(v[0] for v in agree.values()); n = sum(v[1] for v in agree.values())
print(f"SIGN AGREEMENT {tot}/{n} = {tot/n if n else 0:.3f}; bands under 70%: {' '.join(low) or 'none'}")
# gloss agreement per band
def words(path):
    d = defaultdict(list)
    for r in csv.DictReader(open(path), delimiter="\t"):
        if r["kind"].strip().lower() == "dash" or r["word"].strip() in ("-", "--", "—", "_"): continue
        d[r["line"]].append(re.sub(r"[^a-z0-9?]", "", r["word"].lower()))
    return d
GA, GB = words(f"{P}/f101r_glossA.tsv"), words(f"{P}/f101r_glossB.tsv"); ga = gt = 0
for ln in sorted(set(GA) | set(GB)):
    a, b = GA.get(ln, []), GB.get(ln, []); m = sum(bl.size for bl in difflib.SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks())
    t = max(len(a), len(b)); ga += m; gt += t; print(f"{ln}: gloss words A {len(a)} B {len(b)} identical {m}")
print(f"GLOSS AGREEMENT {ga}/{gt} = {ga/gt if gt else 0:.3f}")
