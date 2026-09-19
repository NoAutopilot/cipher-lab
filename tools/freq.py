#!/usr/bin/env python3
"""Token frequency analysis for a ciphertext file.

Usage: python3 tools/freq.py FILE [--sep REGEX] [--top N] [--strip-clear]

Tokens are split on ';' and whitespace by default. Lines starting with '#'
are ignored. --strip-clear drops tokens that contain no digit, which removes
interleaved cleartext words from mixed letters (but also drops pure-letter
cipher symbols, so don't use it on symbol ciphers).

Reports: token count, distinct tokens, index of coincidence, the most frequent
tokens, the most frequent bigrams, and the numeric range.
"""
import argparse
import re
import signal
from collections import Counter


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--sep", default=r"[;\s]+", help="regex used to split tokens")
    ap.add_argument("--top", type=int, default=25)
    ap.add_argument("--strip-clear", action="store_true")
    a = ap.parse_args()

    lines = [l for l in open(a.file, encoding="utf-8", errors="replace") if not l.startswith("#")]
    toks = [t for t in re.split(a.sep, "".join(lines)) if t]
    if a.strip_clear:
        toks = [t for t in toks if re.search(r"\d", t)]

    n = len(toks)
    c = Counter(toks)
    print(f"tokens: {n}   distinct: {len(c)}")
    if n > 1:
        ic = sum(v * (v - 1) for v in c.values()) / (n * (n - 1))
        print(f"index of coincidence: {ic:.4f}   (flat over {len(c)} symbols = {1/len(c):.4f})")
    nums = [int(m.group()) for t in toks for m in [re.match(r"\d+", t)] if m]
    if nums:
        print(f"numeric range: {min(nums)}..{max(nums)}")
        widths = Counter(len(str(x)) for x in nums)
        print("digit widths: " + ", ".join(f"{w}-digit={k}" for w, k in sorted(widths.items())))

    print(f"\ntop {a.top} tokens:")
    for t, k in c.most_common(a.top):
        print(f"  {t:>8}  {k:4d}  {100*k/n:5.1f}%")

    bg = Counter(zip(toks, toks[1:]))
    rep = [(p, k) for p, k in bg.most_common(a.top) if k > 1]
    if rep:
        print(f"\nrepeated bigrams:")
        for (x, y), k in rep:
            print(f"  {x} {y}  x{k}")

    once = sum(1 for v in c.values() if v == 1)
    print(f"\nhapax (seen once): {once} of {len(c)} distinct")


if __name__ == "__main__":
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    main()
