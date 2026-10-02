#!/usr/bin/env python3
"""Turn a folio's reconciled blind sequence into tools/decode_key.py inputs (LIKELY-3, 2 Oct 2026; same shape as
ciphers/ceppo-nevers-fr3251-1570s/harvest/build_decode_inputs.py).
  python3 build_decode_inputs.py f178v [--seq f178v/passC.tsv]
Writes ciphertext_<folio>.tsv (line pos sign conf; line = <folio>_<passage>) and adds/replaces the folio's job in
../decode.json: key = key_1572_sheet.tsv (sheet id -> value, from sign_id_map_1572.json, i.e. the printed 1572 table);
X_* and ? stay unkeyed (grade U) unless an exceptions_<folio>.tsv exists.
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
cfgp = HERE.parent / "decode.json"
cfg = json.load(open(cfgp)) if cfgp.exists() else {"jobs": []}
job = {"ciphertext": f"harvest/ciphertext_{a.folio}.tsv", "key": ["harvest/key_1572_sheet.tsv"],
       "format": "tsv", "split_line": "_", "style": "concat", "reading": f"harvest/reading_{a.folio}.txt",
       "tokens": f"harvest/reading_{a.folio}_tokens.tsv", "null_values": ["NULL"], "unknown_values": ["", "?"],
       "uncertain_conf": ["M", "L"]}
if (HERE / f"exceptions_{a.folio}.tsv").exists():
    job["exceptions"] = f"harvest/exceptions_{a.folio}.tsv"
cfg["jobs"] = [j for j in cfg["jobs"] if j["ciphertext"] != job["ciphertext"]] + [job]
json.dump(cfg, open(cfgp, "w"), indent=1)
