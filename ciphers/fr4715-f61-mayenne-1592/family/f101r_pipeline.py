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
# Chunk 1 ran on the atlas as first written; its two sign passes split one way systematically (A: OTHER with a shape note,
# B: PHI / ZHOOK / BETA) on signs the atlas lacked for this hand, which the amended atlas (PROMPTS_f101r.md, before chunk 2)
# names LOOPS, ZBAR, RSIGN. Chunk 1's raw passes are kept as written (f101r_signs[AB]_c1.tsv); the pipeline relabels them by
# the rule below into f101r_signs[AB]_c1m.tsv (the 'm' files, derived, both passes independently -- A by its own note text,
# B by its own code and note text) and reconciles those. The raw (pre-relabel) agreement is reported alongside.
def relabel_c1(pas, cells):
    sign, note = cells[2], cells[6].lower()
    if pas == "signsA" and sign == "OTHER":
        if "loop chain" in note or "loops no stem" in note: cells[2] = "LOOPS"
        elif "z-like" in note or "z like" in note: cells[2] = "ZBAR"
        elif "r-like" in note or "5-like" in note: cells[2] = "RSIGN"
    if pas == "signsB":
        if sign == "ZHOOK": cells[2] = "ZBAR"
        elif sign == "PHI" and ("loop chain" in note or "double loop" in note): cells[2] = "LOOPS"
    return cells
def norm_conf(v):
    v = (v or "").strip().lower(); return {"high": "h", "medium": "m", "med": "m", "low": "l"}.get(v, v or "m")[0]
for pas in ("signsA", "signsB", "glossC", "glossD"):   # gloss C/D = the Opus passes (A/B, Sonnet, voided after chunk 1)
    files = sorted((f for f in glob.glob(f"{P}/f101r_{pas}_c*.tsv") if re.search(r"_c(\d+)\.tsv$", f)), key=lambda f: int(re.search(r"_c(\d+)\.tsv$", f).group(1)))
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
                if pas.startswith("signs") and f.endswith("_c1.tsv") and "--raw-c1" not in sys.argv: cells = relabel_c1(pas, cells)
                rows.append("\t".join(cells[:8 if pas.startswith("gloss") else 7]))
    if pas.startswith("signs") and "--raw-c1" not in sys.argv and any(f.endswith("_c1.tsv") for f in files):
        with open(f"{P}/f101r_{pas}_c1m.tsv", "w") as out:   # the relabelled chunk-1 pass, for the record
            out.write("line\tpos\tsign\tconf\tsegment\tx_px\tnote\n" + "\n".join(r for r in rows if r.split("\t")[0] in {f"L{b:02d}" for b in range(1, 9)}) + "\n")
    with open(f"{P}/f101r_{pas}.tsv", "w") as out:
        out.write((hdr or ("line\tpos\tsign\tconf\tsegment\tx_px\tnote" if pas.startswith("signs") else "line\tpos\tkind\tword\tconf\tsegment\tx0_px\tx1_px")) + "\n" + "\n".join(rows) + "\n")
    print(pas, len(files), "chunks", len(rows), "rows")
os.makedirs(f"{P}/recf101r", exist_ok=True)
r = subprocess.run([sys.executable, f"{ROOT}/tools/reconcile_passes.py", f"{P}/f101r_signsA.tsv", f"{P}/f101r_signsB.tsv", "--out-dir", f"{P}/recf101r", "--method", "nw"], capture_output=True, text=True)
print(r.stdout.strip()[-1500:]); print(r.stderr.strip()[-500:])
# per-band sign agreement from agreement.tsv (line, signs_A, signs_B, agree, columns, share)
low = []; tot = n = 0
for row in csv.DictReader(open(f"{P}/recf101r/agreement.tsv"), delimiter="\t"):
    a, t = int(row["agree"]), int(row["columns"]); frac = a / t if t else 0; tot += a; n += t
    print(f"{row['line']}: signs {a}/{t} = {frac:.2f}" + ("  <70%" if frac < 0.7 else ""))
    if frac < 0.7: low.append(row["line"])
print(f"SIGN AGREEMENT {tot}/{n} = {tot/n if n else 0:.3f}; bands under 70%: {' '.join(low) or 'none'}")
# gloss agreement per band
def words(path):
    d = defaultdict(list)
    for r in csv.DictReader(open(path), delimiter="\t"):
        if r["kind"].strip().lower() == "dash" or r["word"].strip() in ("-", "--", "—", "_") or r["word"].strip().endswith("_struck"): continue
        d[r["line"]].append(re.sub(r"[^a-z0-9?]", "", r["word"].lower()))
    return d
GA, GB = words(f"{P}/f101r_glossC.tsv"), words(f"{P}/f101r_glossD.tsv"); ga = gt = 0
for ln in sorted(set(GA) | set(GB)):
    a, b = GA.get(ln, []), GB.get(ln, []); m = sum(bl.size for bl in difflib.SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks())
    t = max(len(a), len(b)); ga += m; gt += t; print(f"{ln}: gloss words A {len(a)} B {len(b)} identical {m}")
print(f"GLOSS AGREEMENT {ga}/{gt} = {ga/gt if gt else 0:.3f}")
