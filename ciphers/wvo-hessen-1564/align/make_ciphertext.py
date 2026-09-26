#!/usr/bin/env python3
"""Build ciphertext.tsv (tools/decode_key.py 'tsv' format) from the primary (pass A) blind
transcription, classified against key_174_nomenclator.tsv's shapes via classify.py."""
import sys
sys.path.insert(0, "/home/user/cipher-lab/ciphers/wvo-hessen-1564/align")
from classify import classify, load

D = "/home/user/cipher-lab/ciphers/wvo-hessen-1564/align/"
PASS_FILES = [D + "passA_L01-06.tsv", D + "passA_L07-12.tsv", D + "passA_L13-18.tsv"]

def main():
    rows = [("line", "pos", "sign", "conf")]
    for fn in PASS_FILES:
        for line, idx, typ, val in load(fn):
            if typ == "clear":
                rows.append((line, idx, f"[PLAIN:{val}]", ""))
            else:
                code = classify(val)
                conf = "?" if code == "UNMATCHED" else ""
                sign = code if code != "UNMATCHED" else "UNM"
                rows.append((line, idx, sign, conf))
    with open("/home/user/cipher-lab/ciphers/wvo-hessen-1564/ciphertext.tsv", "w") as f:
        for r in rows:
            f.write("\t".join(r) + "\n")
    print(f"wrote {len(rows)-1} rows")

if __name__ == "__main__":
    main()
