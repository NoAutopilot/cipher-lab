#!/usr/bin/env python3
"""Re-derive reading-no2.md from ciphertext-no2.txt and the tables in key-no2.md (Cipher No. 2, mssEC 47).

The entries to Grant's and Canby's headquarters in mssEC 19 are written in the same way as the Cipher No. 1
entries (see decode.py): dictionary-coded plaintext in reading order, a time word and the day in numeral words
at the head, punctuation and the signature replaced by arbitraries. The machinery of decode.py is reused
unchanged; only the three file names differ.

Usage:  python3 decode_no2.py            # print the readings and the grade counts
        python3 decode_no2.py --check    # exit 1 if the block in reading-no2.md differs from what is derived now
        python3 decode_no2.py --write    # rewrite the derived block inside reading-no2.md
"""
import sys
from pathlib import Path

import decode

HERE = Path(__file__).resolve().parent
KEY = HERE / "key-no2.md"
CIPHERTEXT = HERE / "ciphertext-no2.txt"
READING = HERE / "reading-no2.md"


def main(argv):
    key = decode.load_key(KEY)
    blocks = decode.load_ciphertext(CIPHERTEXT)
    derived = decode.derive(key, blocks)
    if "--write" in argv:
        current = READING.read_text(encoding="utf-8") if READING.exists() else f"{decode.START}\n{decode.END}\n"
        if decode.START not in current or decode.END not in current:
            sys.exit("reading-no2.md lacks the derived-block markers")
        head, rest = current.split(decode.START, 1)
        _, foot = rest.split(decode.END, 1)
        READING.write_text(head + decode.START + "\n" + derived + decode.END + foot, encoding="utf-8")
        print("reading-no2.md updated")
        return 0
    if "--check" in argv:
        current = READING.read_text(encoding="utf-8")
        inside = current.split(decode.START, 1)[1].split(decode.END, 1)[0].strip("\n") + "\n"
        if inside != derived:
            sys.stderr.write("reading-no2.md is stale: the derived block differs from decode_no2.py output\n")
            return 1
        print("reading-no2.md is current")
        return 0
    print(derived)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
