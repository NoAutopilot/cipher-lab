"""MANT-0181 per-token grades under f0181_08/PREREG-MANT-0181.md (rule 4), from f0181_08/ciphertext.tsv, key.tsv, f0181_08/judge_gate.out and
f0181_08/token_blocks.tsv (copy of f0454_08/grade_0454.py with the PREREG's block rule). Unglossed letter token = S only if gate (b) is a TEST
and every block holding its letters PASSes; tail / failing block / too-short = M. Name/word codes (key value 4+ letters) = M; name-abbreviation
groups = M; low-conf = M at best; not in key = U. Writes f0181_08/grades.tsv; --check exits 1 if stale.
Run from the repository root: python3 ciphers/sachsstaatsarchiv-manteuffel-1712/f0181_08/grade_0181.py [--check]"""
import csv, re, sys
from pathlib import Path
D = Path("ciphers/sachsstaatsarchiv-manteuffel-1712"); F = D / "f0181_08"
key = {r["code"]: r["value"] for r in csv.DictReader((l for l in open(D / "key.tsv") if not l.startswith("#")), delimiter="\t") if r["value"].strip()}
kg = {r["code"]: r["grade"] for r in csv.DictReader((l for l in open(D / "key.tsv") if not l.startswith("#")), delimiter="\t")}
j = open(F / "judge_gate.out").read()
bv = {m.group(1): m.group(2) for m in re.finditer(r"^(block_\d+)\t[^\n]*\t(PASS|FAIL|VOID|too-short[^\t]*)\t", j, re.M)}
pw = re.search(r"^power\t.*\t(TEST|too-short.*)$", j, re.M); test = bool(pw) and pw.group(1) == "TEST"
lf = re.search(r"^leaf_0181\t.*$", j, re.M); leaf = lf.group(0).split("\t")[-2] if lf else "missing"
blk = {r["tokid"]: r["block"] for r in csv.DictReader(open(F / "token_blocks.tsv"), delimiter="\t")}
rows = []; cnt = {}
for r in csv.DictReader((l for l in open(F / "ciphertext.tsv") if not l.startswith("#")), delimiter="\t"):
    tid = f"{r['line']}.{r['pos']}"; c = r["sign"]; v = key.get(c, ""); b = blk.get(tid, "?")
    if not v: g, why = "U", "not in key.tsv"
    elif kg.get(c) == "H": g, why = "H", "key.tsv row graded H"
    elif len(re.sub(r"[^a-z]", "", v.split("|")[0].lower())) >= 4: g, why = "M", "name/word code (key value shown, identification I)"
    elif b == "abbrev": g, why = "M", "name-abbreviation group (PREREG repeated-pair rule)"
    elif r["conf"] == "low": g, why = "M", "low-conf transcription"
    elif test and b.startswith("block_") and all(bv.get(x) == "PASS" for x in b.split("+")):
        g, why = "S", f"unglossed letter token; {b} PASS with power"
    else: g, why = "M", f"{b}: " + ("+".join(bv.get(x, x) for x in b.split("+")) if test else "gate (b) not a TEST")
    cnt[g] = cnt.get(g, 0) + 1; rows.append(f"{tid}\t{c}\t{v}\t{r['conf']}\t{b}\t{g}\t{why}")
txt = f"# leaf 0181+0182 gate (b): {leaf}; gloss: see NOTES (gate (a))\n# tokens {len(rows)}: " + ", ".join(f"{k} {cnt.get(k,0)}" for k in "HCSMIU") + "\ntokid\tcode\tkey_value\tconf\tblock\tgrade\twhy\n" + "\n".join(rows) + "\n"
p = F / "grades.tsv"
if "--check" in sys.argv:
    good = p.exists() and p.read_text() == txt; print(f"grades.tsv: {'up to date' if good else 'STALE'}"); sys.exit(0 if good else 1)
p.write_text(txt); print(txt.splitlines()[0], "|", txt.splitlines()[1])
