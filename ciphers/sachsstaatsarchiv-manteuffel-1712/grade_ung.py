"""MANT-UNG per-token grades (rule 4) for 694/08 0290 and 0383 under PREREG-MANT-UNG.md. A code matched (op 'match') under a PASSing pooled
gate row = C: 0290 gate (a) deciding row = the LOWER of the two blind gloss passes (gate_gloss_spans_A/B.out); 0383 gate (c) (gate_print_spans.out).
Else S only if gate (b) (judge_gate.out) is a TEST and the leaf PASSes; else M (low-conf always M, even when matched; at best M; word/name code M); not in key.tsv = U.
Writes f<leaf>_08/grades.tsv. Run from the repository root: python3 ciphers/sachsstaatsarchiv-manteuffel-1712/grade_ung.py 0290|0383 [--check]"""
import csv, re, sys
from pathlib import Path
D = Path("ciphers/sachsstaatsarchiv-manteuffel-1712"); LEAF = sys.argv[1]; F = D / f"f{LEAF}_08"
key = {r["code"]: r["value"] for r in csv.DictReader(open(D / "key.tsv"), delimiter="\t") if r["value"].strip()}
outs = ["gate_gloss_spans_A.out", "gate_gloss_spans_B.out"] if LEAF == "0290" else ["gate_print_spans.out"]
ok = True; matched = None
for o in outs:
    t = (F / o).read_text(); m = re.search(r"== pooled[^\n]*\n[^\n]*\nGATE[^:]*: (\S+)", t)
    ok = ok and bool(m) and m.group(1) == "PASS"
    sp = list(csv.DictReader(open(F / o.replace("gate_", "").replace(".out", ".tsv")), delimiter="\t"))
    rowsm = {l.split("\t")[0]: l.split("\t")[-1] for l in t.split("per span")[1].splitlines() if "\t" in l}
    mt = set()
    for s in sp:
        ops = rowsm.get(s["span_id"], "").split(); tids = s["tokids"].split()
        # path lists one op per code consumed (skips are dropped), in code order
        cops = [x.split(":")[1] for x in ops]
        for tid, op in zip(tids, cops):
            if op == "match": mt.add(tid)
    matched = mt if matched is None else matched & mt
j = (F / "judge_gate.out").read_text()
test = bool(re.search(r"^power\t.*\tTEST$", j, re.M)); lf = re.search(rf"^leaf_{LEAF}\t.*$", j, re.M)
bpass = test and lf and lf.group(0).split("\t")[-2] == "PASS"
rows = []; cnt = {}
for r in csv.DictReader((l for l in open(F / "ciphertext.tsv") if not l.startswith("#")), delimiter="\t"):
    tid = f"{r['line']}.{r['pos']}"; c = r["sign"]; v = key.get(c, "")
    if not v: g, why = "U", "not in key.tsv"
    elif r["conf"] == "low": g, why = "M", "low-conf transcription" + (" (matched the known answer)" if ok and tid in matched else "")
    elif ok and tid in matched: g, why = "C", f"matched under PASSing {'gloss gate (a), both blind passes' if LEAF == '0290' else 'print gate (c), BO I pp.257-258'}"
    elif len(re.sub(r"[^a-z]", "", v.split("|")[0].lower())) >= 4: g, why = "M", "name/word code"
    elif bpass: g, why = "S", "gate (b) PASS with power"
    else: g, why = "M", "no passing gate covers it"
    cnt[g] = cnt.get(g, 0) + 1; rows.append(f"{tid}\t{c}\t{v}\t{r['conf']}\t{g}\t{why}")
txt = (f"# leaf {LEAF}: known-answer gate {'PASS' if ok else 'not PASS'}; gate (b) {lf.group(0).split(chr(9))[-2] if lf else 'too-short/unscored'}\n"
       f"# tokens {len(rows)}: " + ", ".join(f"{k} {cnt.get(k,0)}" for k in "HCSMIU") + "\ntokid\tcode\tkey_value\tconf\tgrade\twhy\n" + "\n".join(rows) + "\n")
p = F / "grades.tsv"
if "--check" in sys.argv:
    good = p.exists() and p.read_text() == txt; print(f"grades.tsv: {'up to date' if good else 'STALE'}"); sys.exit(0 if good else 1)
p.write_text(txt); print(txt.splitlines()[0], "|", txt.splitlines()[1])
