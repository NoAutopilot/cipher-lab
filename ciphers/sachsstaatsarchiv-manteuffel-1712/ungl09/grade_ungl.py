"""MANT-UNGL per-token grades under ungl09/PREREG-MANT-UNGL.md (rule 4), from f<frame>_09/ciphertext.tsv, key.tsv and ungl09/judge_gate.out.
No leaf carries a gloss (both code passes and the worker look), so gate (a) does not apply. Unglossed letter token = S only if the leaf's own
gate (b) line reads PASS (a TEST with power >= 0.80); else M. Name/word codes (key value 4+ letters) = M; low-conf = M at best; not in key = U.
Writes f<frame>_09/grades.tsv; --check exits 1 if any is stale.
Run from the repository root: python3 ciphers/sachsstaatsarchiv-manteuffel-1712/ungl09/grade_ungl.py [--check]"""
import csv, re, sys
from pathlib import Path
D = Path("ciphers/sachsstaatsarchiv-manteuffel-1712")
key = {r["code"]: r["value"] for r in csv.DictReader((l for l in open(D / "key.tsv") if not l.startswith("#")), delimiter="\t") if r["value"].strip()}
j = open(D / "ungl09/judge_gate.out").read(); stale = False
for f in ("0046", "0103", "0233"):
    m = re.search(rf"^leaf_{f}\t.*$", j, re.M); verdict = m.group(0).split("\t")[-2] if m else "missing"
    ok = verdict == "PASS"; rows = []; cnt = {}
    for r in csv.DictReader((l for l in open(D / f"f{f}_09/ciphertext.tsv") if not l.startswith("#")), delimiter="\t"):
        tid = f"{r['line']}.{r['pos']}"; c = r["sign"]; v = key.get(c, "")
        if not v: g, why = "U", "not in key.tsv"
        elif len(re.sub(r"[^a-z]", "", v.split("|")[0].lower())) >= 4: g, why = "M", "name/word code (key value shown)"
        elif r["conf"] == "low": g, why = "M", "low-conf transcription"
        else: g, why = ("S", "unglossed letter token; leaf gate (b) PASS with power") if ok else ("M", f"leaf gate (b): {verdict}")
        cnt[g] = cnt.get(g, 0) + 1; rows.append(f"{tid}\t{c}\t{v}\t{r['conf']}\t{g}\t{why}")
    txt = f"# leaf {f} gate (b): {verdict}; no gloss on the leaf (gate (a) n/a)\n# tokens {len(rows)}: " + ", ".join(f"{k} {cnt.get(k,0)}" for k in "HCSMIU") + "\ntokid\tcode\tkey_value\tconf\tgrade\twhy\n" + "\n".join(rows) + "\n"
    p = D / f"f{f}_09/grades.tsv"
    if "--check" in sys.argv:
        good = p.exists() and p.read_text() == txt; stale |= not good; print(f"{p.name} {f}: {'up to date' if good else 'STALE'}")
    else:
        p.write_text(txt); print(txt.splitlines()[0], "|", txt.splitlines()[1])
sys.exit(1 if stale else 0)
