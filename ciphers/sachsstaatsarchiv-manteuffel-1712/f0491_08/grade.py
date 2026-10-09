"""MANT-0491 (PREREG-MANT0491.md): decode f0491_08/ciphertext.tsv under key.tsv and grade per token (rule 4). Gate (b) FAILed
(judge_gate.out), so no S; key.tsv has no H row; keyed tokens M, a page-edge repair (R05.4) I, codes not in key.tsv U. Also writes the
known-answer table (notes vs decode; reported only, N < 5, not a gate). Run from the repository root:
python3 ciphers/sachsstaatsarchiv-manteuffel-1712/f0491_08/grade.py [--check]"""
import csv, sys
from pathlib import Path
D = Path("ciphers/sachsstaatsarchiv-manteuffel-1712"); F = D / "f0491_08"
key = {r["code"]: r["value"] for r in csv.DictReader((l for l in open(D / "key.tsv") if not l.startswith("#")), delimiter="\t")}
rows = list(csv.DictReader((l for l in open(F / "ciphertext.tsv") if not l.startswith("#")), delimiter="\t"))
out = ["tokid\tcode\tvalue\tgrade\tconf"]; cnt = {}
for r in rows:
    v = key.get(r["sign"], "?")
    g = "U" if v == "?" else ("I" if "repaired" in r["note"] else "M")
    cnt[g] = cnt.get(g, 0) + 1; out.append(f"{r['line']}.{r['pos']}\t{r['sign']}\t{v}\t{g}\t{r['conf']}")
out.append("# counts " + " ".join(f"{g} {cnt.get(g, 0)}" for g in "HCSMIU") + f" (of {len(rows)})")
ka = ["note\ttokids\tdecode_first_values\tpass_A\tpass_B"]
A = {r["note"]: r for r in csv.DictReader(open(F / "gloss_A.tsv"), delimiter="\t")}
Bp = {r["note"]: r for r in csv.DictReader(open(F / "gloss_B.tsv"), delimiter="\t")}
sign = {f"{r['line']}.{r['pos']}": r["sign"] for r in rows}
for n in A:
    ids = A[n]["tokids"].split(); dv = ".".join(key.get(sign[i], "?").split("|")[0] for i in ids)
    ka.append(f"{n}\t{' '.join(ids)}\t{dv}\t{A[n]['pass_text']}\t{Bp[n]['pass_text']}")
txt = "\n".join(out) + "\n"; kt = "\n".join(ka) + "\n"
if "--check" in sys.argv:
    ok = open(F / "grades.tsv").read() == txt and open(F / "known_answer.tsv").read() == kt
    print("grades.tsv/known_answer.tsv up to date" if ok else "STALE"); sys.exit(0 if ok else 1)
open(F / "grades.tsv", "w").write(txt); open(F / "known_answer.tsv", "w").write(kt); print(txt + kt)
