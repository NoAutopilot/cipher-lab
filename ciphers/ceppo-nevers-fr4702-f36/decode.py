#!/usr/bin/env python3
"""Decode BnF fr.4702 f.36r with the Ceppo-Nevers key (KH4-A, 7 Oct 2026); --check fails if reading*.txt are stale (rule 7).

Inputs: ciphertext_agreed.tsv (passage, pos, sign_id; '?' where the two blind passes split) and passes/passA.tsv,
passes/passB.tsv; the sign -> value map is ciphers/ceppo-nevers-fr3251-1570s/harvest/sign_id_map.json (cut from
Tomokiyo's printed Ceppo-Nevers table; the transcribers never saw it). The decode itself is that folder's
harvest/decode_control.py decode() (null dropped, '?' -> '_'), imported, not copied.

Writes reading.txt (agreed signs only), reading_passA.txt, reading_passB.txt. Every letter is grade M (machine
transcription, judge FAIL); '_' positions are I (unread). The shuffled-key and power controls are run with
  python3 ../ceppo-nevers-fr3251-1570s/harvest/decode_control.py ciphertext_agreed.tsv --shuffles 200 --windows 20 --err 0.21

Usage: python3 decode.py [--check]
"""
import csv, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "ceppo-nevers-fr3251-1570s" / "harvest"))
import decode_control as dc  # noqa: E402

JOBS = [("ciphertext_agreed.tsv", "reading.txt"), ("passes/passA.tsv", "reading_passA.txt"),
        ("passes/passB.tsv", "reading_passB.txt")]


def render(src):
    m = dc.load_map()
    P = {}
    for r in csv.DictReader(open(HERE / src), delimiter="\t"):
        P.setdefault(r["passage"], []).append(r["sign_id"])
    return "".join(f"{k}\t{dc.decode(v, m)}\n" for k, v in P.items())


def main():
    check = "--check" in sys.argv[1:]
    stale = 0
    for src, out in JOBS:
        text = render(src)
        p = HERE / out
        if check:
            if not p.exists() or p.read_text() != text:
                print(f"STALE: {out}"); stale += 1
        else:
            p.write_text(text); print(f"wrote {out}")
    if check:
        print("OK" if not stale else f"{stale} stale"); sys.exit(1 if stale else 0)


if __name__ == "__main__":
    main()
