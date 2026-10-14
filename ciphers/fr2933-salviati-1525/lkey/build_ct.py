#!/usr/bin/env python3
"""SALV-LKEY (14 Oct 2026): lay the per-leaf transcription out as a decode_key.py 'tsv' ciphertext (line, pos, sign, conf).
Same token stream as build_spec.py (ciphertext_<leaf>.tsv, the f57r L17 pos>=15 skip, '?' codes as hapax types '?leaf.line.pos'),
with each sign token as 'code^marks' and each plain box as 'w:<word>' from plain_<leaf>.tsv (or 'w:_' when none).
conf = the transcription's grade column (AB, M, ?). Writes lkey/ciphertext_lasry.tsv; --check exits 1 if it is stale."""
import csv, os, sys
D = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(D)
LEAVES = ("f54r", "f54v", "f55r", "f55v", "f56r", "f56v", "f57r", "f57v")
rows = ["line\tpos\tsign\tconf"]; n = 0
for lf in LEAVES:
    plain = {}
    p = os.path.join(T, f"plain_{lf}.tsv")
    if os.path.exists(p):
        for x in csv.DictReader(open(p, encoding="utf-8"), delimiter="\t"):
            plain[(x["line"], x["pos"])] = (x.get("word") or "_").split("|")[0].replace(" ", "_") or "_"
    for x in csv.DictReader(open(os.path.join(T, f"ciphertext_{lf}.tsv"), encoding="utf-8"), delimiter="\t"):
        if lf == "f57r" and x["line"] == "17" and float(x["pos"]) >= 15:
            continue
        line = f"{lf}_L{int(x['line']):02d}"
        if x["code"] == "_":
            rows.append(f"{line}\t{x['pos']}\tw:{plain.get((x['line'], x['pos']), '_')}\t{x['grade']}")
        else:
            code = f"?{lf}.{x['line']}.{x['pos']}" if x["code"] == "?" else x["code"]
            rows.append(f"{line}\t{x['pos']}\t{code}^{x['marks']}\t{x['grade']}"); n += 1
out = os.path.join(D, "ciphertext_lasry.tsv"); txt = "\n".join(rows) + "\n"
if "--check" in sys.argv:
    sys.exit(0 if open(out, encoding="utf-8").read() == txt else 1)
open(out, "w", encoding="utf-8").write(txt)
print(len(rows) - 1, "rows;", n, "sign tokens")
