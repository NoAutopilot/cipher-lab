#!/usr/bin/env python3
"""Re-derive reading-no9.md from ciphertext-no9.txt and the tables in key-no9.md (the old vocabulary, mssEC 67).

The Jan-Feb 1864 entries of mssEC 19 to the eastern and western posts are written in the older Stager vocabulary
(NOTES.md section 2), whose meanings are the ones handwritten in the Huntington copy mssEC 67 (object 1750,
Tomokiyo: Cipher No. 9). Same layout as the Cipher No. 1 entries (see decode.py); the machinery of decode.py is
reused unchanged; only the three file names differ (R7A-ECK64, 6 Oct 2026, modelled on decode_no2.py).

Usage:  python3 decode_no9.py            # print the readings and the grade counts
        python3 decode_no9.py --check    # exit 1 if the block in reading-no9.md differs from what is derived now
        python3 decode_no9.py --write    # rewrite the derived block inside reading-no9.md
"""
import sys
from pathlib import Path

import decode

HERE = Path(__file__).resolve().parent
KEY = HERE / "key-no9.md"
CIPHERTEXT = HERE / "ciphertext-no9.txt"
READING = HERE / "reading-no9.md"


def main(argv):
    key = decode.load_key(KEY)
    blocks = decode.load_ciphertext(CIPHERTEXT)
    derived = decode.derive(key, blocks)
    if "--write" in argv:
        current = READING.read_text(encoding="utf-8") if READING.exists() else f"{decode.START}\n{decode.END}\n"
        if decode.START not in current or decode.END not in current:
            sys.exit("reading-no9.md lacks the derived-block markers")
        head, rest = current.split(decode.START, 1)
        _, foot = rest.split(decode.END, 1)
        READING.write_text(head + decode.START + "\n" + derived + decode.END + foot, encoding="utf-8")
        print("reading-no9.md updated")
        return 0
    if "--check" in argv:
        current = READING.read_text(encoding="utf-8")
        inside = current.split(decode.START, 1)[1].split(decode.END, 1)[0].strip("\n") + "\n"
        if inside != derived:
            sys.stderr.write("reading-no9.md is stale: the derived block differs from decode_no9.py output\n")
            return 1
        print("reading-no9.md is current")
        return 0
    print(derived)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
