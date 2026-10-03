#!/usr/bin/env python3
"""F36R-REREAD (3 Oct 2026): reconcile the two blind sign passes of f.36r rows r36n_L09-L14 (re-centred on the row-ink
profile, cut_f36r.py) and splice them into the f.36-37 sign transcription in place of F36-READ's mis-cut r36_L09-L15.

  python3 merge_f36r.py           # writes ciphertext_f36_v2.tsv (decode_key input), recon_r36n.tsv, passD_v2.tsv, reading_key_v2.txt, error.tsv
  python3 merge_f36r.py --check   # exit 1 if the committed outputs are stale (rule 7)

Reconciliation is compare_f36.py's rule: ids aligned per row (difflib); agree -> id; one '?'/absent -> the other
(one-sided); both read and differ -> '?' (split). Two-reader error E = (split + one-sided) / positions, as F36-READ.
The whole-letter E recounts F36-READ's recon.tsv for the kept rows (all but r36_L09-L15) plus the new rows.
"""
import csv, difflib, json, sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
OLD = HERE.parent / "f36"
MAP = HERE.parents[2] / "ceppo-nevers-fr3251-1570s/harvest/sign_id_map.json"
DROP = {f"r36_L{i:02d}" for i in range(9, 16)}


def load(p):
    rows = {}
    for r in csv.DictReader(open(p), delimiter="\t"):
        rows.setdefault(r["passage"].strip(), []).append(r["sign_id"].strip() or "?")
    return rows


def classify(sa, sb, st):
    if sa == sb: st["agree"] += 1; return sa
    if sa in ("", "?"): st["one"] += 1; return sb or "?"
    if sb in ("", "?"): st["one"] += 1; return sa
    st["split"] += 1; return "?"


def main(check):
    m = {e["id"]: e["value"] for e in json.load(open(MAP))}; m["X_THETA2"] = "r"
    A, B = load(HERE / "passA.tsv"), load(HERE / "passB.tsv")
    recon = ["line\tpos\tA\tB\tsign\tprinted"]; new = {}; per = {}; st_new = Counter()
    for line in sorted(set(A) | set(B)):
        a, b = A.get(line, []), B.get(line, []); st = Counter(); pairs = []
        for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
            if op == "equal" or (op == "replace" and i2 - i1 == j2 - j1):
                pairs += list(zip(a[i1:i2], b[j1:j2]))
            else:
                n = max(i2 - i1, j2 - j1)
                pairs += [(a[i1 + k] if i1 + k < i2 else "", b[j1 + k] if j1 + k < j2 else "") for k in range(n)]
        new[line] = []
        for p, (sa, sb) in enumerate(pairs, 1):
            s = classify(sa, sb, st); new[line].append(s)
            recon.append(f"{line}\t{p}\t{sa}\t{sb}\t{s}\t{m.get(s, '?')}")
        per[line] = (len(a), len(b), len(pairs), st["agree"], st["one"], st["split"]); st_new.update(st)
    # kept rows of F36-READ, recounted from its recon.tsv
    st_old = Counter(); old_seq = {}
    for r in csv.DictReader(open(OLD / "recon.tsv"), delimiter="\t"):
        old_seq.setdefault(r["line"], []).append(r["sign"])
        if r["line"] in DROP: continue
        classify(r["A"], r["B"], st_old)
    passd = ["passage\tpos\tsign_id"]; dec = []
    order = list(old_seq)
    for line in order:
        if line == "r36_L09":
            for nl in sorted(new):
                passd += [f"{nl}\t{i}\t{s}" for i, s in enumerate(new[nl], 1)]
                dec.append(nl + "\t" + "".join("" if m.get(s) == "null" else (m[s] if s in m else "_") for s in new[nl]))
        if line in DROP: continue
        passd += [f"{line}\t{i}\t{s}" for i, s in enumerate(old_seq[line], 1)]
        dec.append(line + "\t" + "".join("" if m.get(s) == "null" else (m[s] if s in m else "_") for s in old_seq[line]))
    err = ["scope\tpositions\tagree\tone_sided\tsplit\tE"]
    for line, (na, nb, n, ag, one, sp) in per.items():
        err.append(f"{line} (A {na}, B {nb})\t{n}\t{ag}\t{one}\t{sp}\t{(one + sp) / n:.3f}")
    for name, st in (("r36n_L09-L14", st_new), ("kept F36-READ rows", st_old), ("whole letter", st_new + st_old)):
        n = sum(st.values()); err.append(f"{name}\t{n}\t{st['agree']}\t{st['one']}\t{st['split']}\t{(st['one'] + st['split']) / n:.3f}")
    ct = ["line\tpos\tsign\tconf"] + [f"{a}\t{b}\t{c}\t{'U' if c == '?' else 'M'}" for a, b, c in
                                        (x.split("\t") for x in passd[1:])]
    files = {"ciphertext_f36_v2.tsv": "\n".join(ct) + "\n", "recon_r36n.tsv": "\n".join(recon) + "\n", "passD_v2.tsv": "\n".join(passd) + "\n",
             "reading_key_v2.txt": "\n".join(dec) + "\n", "error.tsv": "\n".join(err) + "\n"}
    stale = [f for f, t in files.items() if not (HERE / f).exists() or (HERE / f).read_text() != t]
    if check:
        print("stale:" if stale else "OK, not stale", " ".join(stale)); sys.exit(1 if stale else 0)
    for f, t in files.items(): (HERE / f).write_text(t)
    print(files["error.tsv"], end="")


if __name__ == "__main__":
    main("--check" in sys.argv)
