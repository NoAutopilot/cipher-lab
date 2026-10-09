"""MANT-0136 per-token grades under PREREG-MANT-0136.md (rule 4) [--a1: PREREG-MANT-0136-A1 inputs gloss_A1A/A1B, gate_A1A/A1B -> grades_A1.tsv], from ciphertext.tsv, key.tsv, gate_A.out, gate_B.out and judge_gate.out.
C = glossed token whose key value matches its gloss in BOTH blind passes; M = matched in one pass only, or glossed but unmatched,
or low-conf transcription, or a name/word code (key value 4+ letters); S = unglossed letter token when gates (a) [both passes] and
(b) PASS; U = code not in key.tsv. Writes grades.tsv; --check exits 1 if it is stale.
Run from the repository root: python3 ciphers/sachsstaatsarchiv-manteuffel-1712/f0136_09/grade_0136.py [--check]"""
import csv, re, sys
from pathlib import Path
D = Path("ciphers/sachsstaatsarchiv-manteuffel-1712"); F = D / "f0136_09"
key = {r["code"]: r["value"] for r in csv.DictReader((l for l in open(D / "key.tsv") if not l.startswith("#")), delimiter="\t") if r["value"].strip()}
def matched(gate):
    txt = open(F / gate).read(); ok = "GATE (S > p99 and S >= 0.5 x keyed): PASS" in txt; m = {}
    for g in GLOSS:
        if gate == "gate_" + g.split("_")[1].split(".")[0] + ".out":
            spans = list(csv.DictReader(open(F / g), delimiter="\t"))
    for ln in txt.splitlines():
        p = ln.split("\t")
        if len(p) == 5 and p[0].startswith("G"):
            sp = next(s for s in spans if s["span_id"] == p[0]); ids = sp["tokids"].split()
            for tid, item in zip(ids, p[4].split()):
                m[tid] = item.split(":")[1] == "match"
    return ok, m
A1 = "--a1" in sys.argv  # PREREG-MANT-0136-A1 (MANT-R07): gate (a) on the widened r07+r08 spans; gate (b) as before
GLOSS = ("gloss_A1A.tsv", "gloss_A1B.tsv") if A1 else ("gloss_A.tsv", "gloss_B.tsv")
OUTF = "grades_A1.tsv" if A1 else "grades.tsv"
okA, mA = matched("gate_A1A.out" if A1 else "gate_A.out"); okB, mB = matched("gate_A1B.out" if A1 else "gate_B.out")
okb = "target_0136_unglossed" in (j := open(F / "judge_gate.out").read()) and re.search(r"target_0136_unglossed.*\tPASS \(real > p95\)", j) is not None
pw = re.search(r"power_0085_r9r10.*\tPASS \(real > p95\)", j) is not None
licensed = okA and okB and okb and pw
rows = []; cnt = {}
for r in csv.DictReader((l for l in open(F / "ciphertext.tsv") if not l.startswith("#")), delimiter="\t"):
    tid = f"{r['line']}.{r['pos']}"; c = r["sign"]; v = key.get(c, "")
    if not v: g, why = "U", "not in key.tsv"
    elif tid in mA or tid in mB:
        a, b = mA.get(tid, False), mB.get(tid, False)
        g, why = ("C", "gloss matches key in both blind passes") if a and b else ("M", "gloss matches in one pass only" if a or b else "glossed, gloss does not match key value")
        if g == "C" and r["conf"] == "low": g, why = "M", why + "; low-conf transcription"
    elif len(re.sub(r"[^a-z]", "", v.split("|")[0].lower())) >= 4: g, why = "M", "name/word code (key value shown, identification I)"
    elif r["conf"] == "low": g, why = "M", "low-conf transcription"
    else: g, why = ("S", "unglossed letter token; gates (a) both passes and (b) PASS") if licensed else ("M", "gates not all PASS")
    cnt[g] = cnt.get(g, 0) + 1; rows.append(f"{tid}\t{c}\t{v}\t{r['conf']}\t{g}\t{why}")
head = f"# {'PREREG-MANT-0136-A1 widened spans; ' if A1 else ''}gate (a) A {'PASS' if okA else 'FAIL'}, B {'PASS' if okB else 'FAIL'}; gate (b) {'PASS' if okb else 'FAIL'} (power control {'PASS' if pw else 'FAIL'})\n# tokens {len(rows)}: " + ", ".join(f"{k} {cnt.get(k,0)}" for k in "HCSMIU") + "\ntokid\tcode\tkey_value\tconf\tgrade\twhy\n"
txt = head + "\n".join(rows) + "\n"
if "--check" in sys.argv:
    good = open(F / OUTF).read() == txt; print(OUTF + " up to date" if good else "STALE"); sys.exit(0 if good else 1)
open(F / OUTF, "w").write(txt); print(head, end="")
