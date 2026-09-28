#!/usr/bin/env python3
"""Turn a folio's reconciled blind sequence into decode_key.py inputs (HARVEST-D2, 28 Sept 2026).
  python3 build_decode_inputs.py f35 [--seq f35/passC.tsv]
Writes ciphertext_<folio>.tsv (line pos sign conf; line = <folio>_<passage>) and adds/replaces the folio's job in
../decode.json: key = key_f11.tsv (the printed Ceppo-Nevers table, one row per sheet id) + key_extra.tsv (X_THETA2 = r
from the fr.3252 witness); X_POUND, X_NEW and ? stay unkeyed (grade U) unless an exceptions_<folio>.tsv exists.
"""
import argparse, csv, json
from pathlib import Path
HERE = Path(__file__).resolve().parent
ap = argparse.ArgumentParser(); ap.add_argument("folio"); ap.add_argument("--seq"); a = ap.parse_args()
seq = a.seq or f"{a.folio}/passC.tsv"
with open(HERE / f"ciphertext_{a.folio}.tsv", "w") as f:
    f.write("line\tpos\tsign\tconf\n")
    for r in csv.DictReader(open(HERE / seq), delimiter="\t"):
        f.write(f"{a.folio}_{r['passage']}\t{r['pos']}\t{r['sign_id']}\t{r['conf']}\n")
cfg = json.load(open(HERE.parent / "decode.json"))
job = {"ciphertext": f"harvest/ciphertext_{a.folio}.tsv", "key": ["harvest/key_f11.tsv", "harvest/key_extra.tsv"],
       "format": "tsv", "split_line": "_", "style": "concat", "reading": f"harvest/reading_{a.folio}.txt",
       "tokens": f"harvest/reading_{a.folio}_tokens.tsv", "null_values": ["NULL"], "unknown_values": ["", "?"],
       "uncertain_conf": ["M", "L"]}
if (HERE / f"exceptions_{a.folio}.tsv").exists():
    job["exceptions"] = f"harvest/exceptions_{a.folio}.tsv"
cfg["jobs"] = [j for j in cfg["jobs"] if j["ciphertext"] != job["ciphertext"]] + [job]
json.dump(cfg, open(HERE.parent / "decode.json", "w"), indent=1)
print("wrote", f"ciphertext_{a.folio}.tsv", "and decode.json job", job["reading"])
