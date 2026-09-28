#!/usr/bin/env python3
"""F61-FAMILY step 4 (28 Sept 2026): apply family/key_period.tsv -- the class -> letter pairs read from the period
interlinear decipherments of the sibling leaves, NO refit -- to (a) f.61's five Tomokiyo spans (55 known letters,
scripts/tomokiyo_spans.tsv on the VBAR-split class sequence of scripts/passA_classes.tsv via f61crib4.split_lines)
and (b) f.108r's 84 overlay letters (scripts/tomokiyo_spans_3983.tsv on the reconciled pass108A/B draft), scored by
the F61-CAL DP (f61crib.align: a letter matches when the class's period letter set contains it). Control: 20 keys with
the letter sets permuted across the classes (seed 1), same DP. Pre-registered gate (brief step 5): 0.75 on the 55
known letters. A key class absent from a leaf's classes simply never matches. Reported: fractions, permuted mean/max,
and the share of the leaf's signs whose class the period key covers.
  python3 test_period_key.py [--check]   (from the family folder)
"""
import csv, os, random, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); S = os.path.abspath(f"{HERE}/../scripts"); sys.path.insert(0, S)
from f61crib import align, load_read, load_spans
from f61crib4 import split_lines
from f61joint import f108_lines
MIN = int(sys.argv[sys.argv.index("--min") + 1]) if "--min" in sys.argv else 1
# F61-FAMILY-2 (28 Sept 2026): --key FILE scores another key file (default key_period.tsv; result file named after it);
# --collapse-ebr folds EBR_A/EBR_B rows (the H22 split, read on f.101r) into EBR, the unsplit class of f.61's own passes.
KEYFILE = sys.argv[sys.argv.index("--key") + 1] if "--key" in sys.argv else f"{HERE}/key_period.tsv"
COLLAPSE = {"EBR_A": "EBR", "EBR_B": "EBR"} if "--collapse-ebr" in sys.argv else {}
def load_key():
    key = {}
    for r in csv.DictReader((l for l in open(KEYFILE) if not l.startswith("#")), delimiter="\t"):
        if r["letter"] in ("-", "") or r["class"] in ("PLAIN", "OTHER", "DASH") or int(r["n"]) < MIN: continue
        key.setdefault(COLLAPSE.get(r["class"], r["class"]), set()).add(r["letter"])
    return {c: tuple(sorted(v)) for c, v in key.items()}
def score(key, lines, spans):
    mat = tot = 0
    for s, line, markup in spans:
        mt, _ = align(markup, lines[line], key); mat += mt; tot += sum(1 for c in markup if c != "-")
    return mat, tot
def main():
    key = load_key(); out = [f"{os.path.basename(KEYFILE)} (pairs with n >= {MIN}): {len(key)} classes with letters: " + " ".join(f"{c}={'/'.join(v)}" for c, v in sorted(key.items()))]
    lines = split_lines(load_read()); lines.update(f108_lines())
    spans61 = load_spans()
    spans108 = [(s, "F108_" + ("L02" if s == "T1" else "L03"), m) for s, _, m, _ in (l.rstrip("\n").split("\t") for l in open(f"{S}/tomokiyo_spans_3983.tsv") if l[0] == "T")]
    rng = random.Random(1); labs = sorted(key); vals = [key[l] for l in labs]
    perms = []
    for _ in range(20):
        v = list(vals); rng.shuffle(v); perms.append(dict(zip(labs, v)))
    res = {}
    for tag, spans in (("f.61 five known spans (55)", spans61), ("f.108r overlay letters (84)", spans108)):
        mt, tot = score(key, lines, spans); cs = [score(p, lines, spans)[0] for p in perms]
        used = [l for _, l, _ in spans]; cls = Counter(c for l in used for c in lines[l]); cov = sum(n for c, n in cls.items() if c in key) / max(1, sum(cls.values()))
        per = "; ".join(f"{s}:{align(m, lines[l], key)[0]}/{sum(1 for c in m if c != '-')}" for s, l, m in spans)
        miss = sorted(c for c in cls if c not in key)
        unc = f" (uncovered: {' '.join(miss) or 'none'})" if "--key" in sys.argv else ""
        out.append(f"{tag}: period key {mt}/{tot} = {mt/tot:.3f}; 20 permuted keys mean {sum(cs)/20/tot:.3f} max {max(cs)/tot:.3f}; classes covered {cov:.2f} of signs{unc}; per span {per}")
        res[tag] = mt / tot
    g = res["f.61 five known spans (55)"]
    out.append(f"GATE (brief step 5, 0.75 on the 55 known letters): {'PASS' if g >= 0.75 else 'FAIL'} ({g:.3f})")
    stem = "" if os.path.basename(KEYFILE) == "key_period.tsv" else "_" + os.path.basename(KEYFILE).replace("key_period_", "").replace(".tsv", "")
    txt = "\n".join(out) + "\n"; path = f"{HERE}/test_period_key_result{stem}{'' if MIN == 1 else '_min' + str(MIN)}.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(path) and open(path).read() == txt; print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(path, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    main()
