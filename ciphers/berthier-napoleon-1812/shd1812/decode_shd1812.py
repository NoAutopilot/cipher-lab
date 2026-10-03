#!/usr/bin/env python3
"""GF4d (3 Oct 2026): decode the Vilcoq-plate page (structure/flat.txt, 325 groups) with key_shd1812.tsv.

Writes reading_shd1812.tsv (pos, code, entry as in the table, grade) and reading_shd1812.txt (one line per plate line of
ciphertext_full.tsv, entries' first forms joined by spaces; '_' = unread). Grades (rule 4): H = table entry read H by both
blind passes; M = probable/reconciled reading of the table entry; I = no legible entry. The choice among an entry's
listed endings ("facile, s, ite, ment") is not made here: the .txt shows the first form only. `--check` exits 1 if
either committed file is stale (rule 7).
"""
import csv, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
TGT = HERE.parent


def main():
    key = {}
    with open(HERE / "key_shd1812.tsv", encoding="utf-8") as f:
        for r in csv.DictReader((l for l in f if not l.startswith("#")), delimiter="\t"):
            key[int(r["code"])] = (r["entry"].strip(), r["conf"])
    lines = {}
    with open(TGT / "ciphertext_full.tsv", encoding="utf-8") as f:
        rows = [l.rstrip("\n").split("\t") for l in f if l.strip()]
    flat = [int(x) for x in (TGT / "structure/flat.txt").read_text().split()]
    tsv = ["pos\tcode\tentry\tgrade"]; txt = []; pos = 0; counts = {"H": 0, "M": 0, "I": 0}
    for r in rows:
        if not r[0].strip().isdigit() and r[0] != "": continue
        groups = [int(x) for x in r[-1].split()] if len(r) > 1 else []
        if not groups: continue
        out = []
        for g in groups:
            assert g == flat[pos], (pos, g, flat[pos])
            pos += 1
            e, cf = key.get(g, ("(blank)", "L"))
            blank = e in ("", "(blank)")
            gr = "I" if blank else ("H" if cf == "H" else "M")
            counts[gr] += 1
            tsv.append(f"{pos}\t{g}\t{e}\t{gr}")
            out.append("_" if blank else e.split(",")[0].strip())
        txt.append(" ".join(out))
    assert pos == len(flat), (pos, len(flat))
    t1 = "\n".join(tsv) + "\n"
    t2 = "\n".join(txt) + "\n"
    if "--check" in sys.argv:
        ok = (HERE / "reading_shd1812.tsv").read_text(encoding="utf-8") == t1 and \
             (HERE / "reading_shd1812.txt").read_text(encoding="utf-8") == t2
        print("OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    (HERE / "reading_shd1812.tsv").write_text(t1, encoding="utf-8")
    (HERE / "reading_shd1812.txt").write_text(t2, encoding="utf-8")
    print(counts)


if __name__ == "__main__":
    main()
