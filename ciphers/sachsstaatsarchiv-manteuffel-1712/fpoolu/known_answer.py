"""MANT-POOLU known answers (fpoolu/PREREG-MANT-POOLU.md, reported only, never a gate): for each span with writing above, each blind pass's
text (gloss_A.tsv / gloss_B.tsv, as the pass wrote it) beside the key.tsv decode of the codes under it, with a letter-position match count
(both lower-cased, letters only, compared position by position from the start). Writes fpoolu/known_answer.tsv; --check exits 1 if stale.
Run from the repository root: python3 ciphers/sachsstaatsarchiv-manteuffel-1712/fpoolu/known_answer.py [--check]"""
import csv, re, sys
from pathlib import Path
D = Path("ciphers/sachsstaatsarchiv-manteuffel-1712"); F = D / "fpoolu"
key = {r["code"]: r["value"].split("|")[0].strip() for r in csv.DictReader((l for l in open(D / "key.tsv") if not l.startswith("#")), delimiter="\t")}
sign = {f"{r['line']}.{r['pos']}": r["sign"] for r in csv.DictReader((l for l in open(F / "ciphertext.tsv") if not l.startswith("#")), delimiter="\t")}
norm = lambda s: re.sub(r"[^a-z]", "", s.lower())
out = ["note\tpass\ttokids\tcodes\tkey_decode\tpass_text\tletter_matches"]
for p in ("A", "B"):
    for r in csv.DictReader(open(F / f"gloss_{p}.tsv"), delimiter="\t"):
        ts = r["tokids"].split(); cs = [sign[t] for t in ts]
        dec = "".join(key.get(c, "?") if len(norm(key.get(c, ""))) <= 3 else "[" + key[c] + "]" for c in cs)
        a, b = norm(dec), norm(re.sub(r"\(.*?\)", "", r["pass_text"]))
        m = sum(x == y for x, y in zip(a, b))
        out.append(f"{r['note']}\t{p}\t{r['tokids']}\t{'.'.join(cs)}\t{dec}\t{r['pass_text']}\t{m}/{max(len(a), len(b))}")
txt = "\n".join(out) + "\n"
if "--check" in sys.argv:
    good = (F / "known_answer.tsv").exists() and (F / "known_answer.tsv").read_text() == txt
    print("known_answer.tsv " + ("up to date" if good else "STALE")); sys.exit(0 if good else 1)
(F / "known_answer.tsv").write_text(txt); print(txt, end="")
