"""MANT-0453 per-token grades under f0453_08/PREREG-MANT-0453.md (rule 4), from f0453_08/ciphertext.tsv, key.tsv and f0453_08/judge_gate.out
(copy of f0454_08/grade_0454.py). No gloss on the frame (gate (a) n/a). A letter token is S if leaf_0453 (b1) reads PASS, or if pooled_no88 (b2)
reads PASS and leaf_0453's own score is above its own p95; else M. Name/word codes (key value 4+ letters) = M; low-conf = M at best; not in
key = U. Writes f0453_08/grades.tsv; --check exits 1 if stale.
Run from the repository root: python3 ciphers/sachsstaatsarchiv-manteuffel-1712/f0453_08/grade_0453.py [--check]"""
import csv, re, sys
from pathlib import Path
D = Path("ciphers/sachsstaatsarchiv-manteuffel-1712"); F = D / "f0453_08"
key = {r["code"]: r["value"] for r in csv.DictReader((l for l in open(D / "key.tsv") if not l.startswith("#")), delimiter="\t") if r["value"].strip()}
j = open(F / "judge_gate.out").read()
def line(name):
    m = re.search(rf"^{name}\t.*$", j, re.M); return m.group(0).split("\t") if m else ["missing"] * 8
b1, b2 = line("leaf_0453"), line("pooled_no88")
v1, v2 = b1[-2], b2[-2]; own_above = "own score above p95" in v1 or v1 == "PASS"
ok = v1 == "PASS" or (v2 == "PASS" and own_above)
verdict = f"b1 {v1}; b2 {v2}"
rows = []; cnt = {}
for r in csv.DictReader((l for l in open(F / "ciphertext.tsv") if not l.startswith("#")), delimiter="\t"):
    tid = f"{r['line']}.{r['pos']}"; c = r["sign"]; v = key.get(c, "")
    if not v: g, why = "U", "not in key.tsv"
    elif len(re.sub(r"[^a-z]", "", v.split("|")[0].lower())) >= 4: g, why = "M", "name/word code (key value shown, identification I)"
    elif r["conf"] == "low": g, why = "M", "low-conf transcription"
    else: g, why = ("S", "letter token; gate (b) per PREREG passed") if ok else ("M", "gate (b) not a test at this N (PREREG grade rule)")
    cnt[g] = cnt.get(g, 0) + 1; rows.append(f"{tid}\t{c}\t{v}\t{r['conf']}\t{g}\t{why}")
txt = f"# frame 0453 gates: {verdict}; no gloss (gate (a) n/a)\n# tokens {len(rows)}: " + ", ".join(f"{k} {cnt.get(k,0)}" for k in "HCSMIU") + "\ntokid\tcode\tkey_value\tconf\tgrade\twhy\n" + "\n".join(rows) + "\n"
p = F / "grades.tsv"
if "--check" in sys.argv:
    good = p.exists() and p.read_text() == txt; print(f"grades.tsv: {'up to date' if good else 'STALE'}"); sys.exit(0 if good else 1)
p.write_text(txt); print(txt.splitlines()[0], "|", txt.splitlines()[1])
