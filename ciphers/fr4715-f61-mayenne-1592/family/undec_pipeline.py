#!/usr/bin/env python3
"""F61-FAMILY-4 (28 Sept 2026): pass pipeline for the leaves cut in this job (f124r first). Concatenates the per-chunk pass
files passes/<PREFIX>_<pass>_c<k>.tsv (pass in signsA, signsB and, for a glossed leaf, glossA, glossB) into
passes/<PREFIX>_<pass>.tsv, runs tools/reconcile_passes.py (nw) on the two sign passes into passes/rec<PREFIX>/, reports
per-band and overall sign agreement (identical aligned columns / aligned columns) and gloss word agreement (words both
passes read identically, case-folded, per band, by difflib), and lists the bands under 70% sign agreement (the brief's
re-cut-once threshold). The f101r_pipeline.py logic without its chunk-1 relabel (this job's atlas was the amended one from
the first call).
  python3 undec_pipeline.py PREFIX [--chunks 1,2,...]     (from the family folder)
"""
import csv, difflib, glob, os, re, subprocess, sys
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(f"{HERE}/../../.."); P = f"{HERE}/passes"
pre = sys.argv[1]
want = [int(v) for v in sys.argv[sys.argv.index("--chunks") + 1].split(",")] if "--chunks" in sys.argv else None
def norm_conf(v):
    v = (v or "").strip().lower(); return {"high": "h", "medium": "m", "med": "m", "low": "l"}.get(v, v or "m")[0]
have_gloss = bool(glob.glob(f"{P}/{pre}_glossA_c*.tsv"))
for pas in ("signsA", "signsB") + (("glossA", "glossB") if have_gloss else ()):
    files = sorted((f for f in glob.glob(f"{P}/{pre}_{pas}_c*.tsv") if re.search(r"_c(\d+)\.tsv$", f)), key=lambda f: int(re.search(r"_c(\d+)\.tsv$", f).group(1)))
    if want: files = [f for f in files if int(re.search(r"_c(\d+)\.tsv", f).group(1)) in want]
    rows = []
    for f in files:
        with open(f) as fh:
            for line in fh:
                line = line.rstrip("\n")
                if not line.strip() or line.startswith("#") or line.startswith("line\t"): continue
                cells = line.split("\t")
                if len(cells) < 7: cells += [""] * (7 - len(cells))
                ci = 3 if pas.startswith("signs") else 4; cells[ci] = norm_conf(cells[ci])
                if pas.startswith("gloss") and len(cells) < 8: cells += [""] * (8 - len(cells))
                rows.append("\t".join(cells[:8 if pas.startswith("gloss") else 7]))
    hdr = "line\tpos\tsign\tconf\tsegment\tx_px\tnote" if pas.startswith("signs") else "line\tpos\tkind\tword\tconf\tsegment\tx0_px\tx1_px"
    with open(f"{P}/{pre}_{pas}.tsv", "w") as out: out.write(hdr + "\n" + "\n".join(rows) + "\n")
    print(pas, len(files), "chunks", len(rows), "rows")
os.makedirs(f"{P}/rec{pre}", exist_ok=True)
r = subprocess.run([sys.executable, f"{ROOT}/tools/reconcile_passes.py", f"{P}/{pre}_signsA.tsv", f"{P}/{pre}_signsB.tsv", "--out-dir", f"{P}/rec{pre}", "--method", "nw"], capture_output=True, text=True)
print(r.stdout.strip()[-600:]); print(r.stderr.strip()[-300:])
low = []; tot = n = 0
for row in csv.DictReader(open(f"{P}/rec{pre}/agreement.tsv"), delimiter="\t"):
    a, t = int(row["agree"]), int(row["columns"]); frac = a / t if t else 0; tot += a; n += t
    print(f"{row['line']}: signs {a}/{t} = {frac:.2f}" + ("  <70%" if frac < 0.7 else ""))
    if frac < 0.7: low.append(row["line"])
print(f"SIGN AGREEMENT {tot}/{n} = {tot/n if n else 0:.3f}; bands under 70%: {' '.join(low) or 'none'}")
if have_gloss:
    def words(path):
        d = defaultdict(list)
        for r in csv.DictReader(open(path), delimiter="\t"):
            if r["kind"].strip().lower() == "dash" or r["word"].strip() in ("-", "--", "—", "_") or r["word"].strip().endswith("_struck"): continue
            d[r["line"]].append(re.sub(r"[^a-z0-9?]", "", r["word"].lower()))
        return d
    GA, GB = words(f"{P}/{pre}_glossA.tsv"), words(f"{P}/{pre}_glossB.tsv"); ga = gt = 0
    for ln in sorted(set(GA) | set(GB)):
        a, b = GA.get(ln, []), GB.get(ln, []); m = sum(bl.size for bl in difflib.SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks())
        t = max(len(a), len(b)); ga += m; gt += t; print(f"{ln}: gloss words A {len(a)} B {len(b)} identical {m}")
    print(f"GLOSS AGREEMENT {ga}/{gt} = {ga/gt if gt else 0:.3f}")
