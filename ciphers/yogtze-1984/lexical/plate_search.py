#!/usr/bin/env python3
"""Lexical crib search of YOGTZE against licence-plate formats (D2B-YOG, 5-6 Oct 2026).

A search, not a reading. For each variant of the six letters (YOGTZE; YOG'TZE with the
apostrophe as a separator; the T read as struck out, YOGZE) it enumerates:

  German (1956-1994 format "PPP-LL 9999"): every split prefix | 1-2 recognition letters |
  rest, with the prefix taken from Wikipedia's Liste der Kfz-Kennzeichen in Deutschland
  (raw wikitext, fetched 5 Oct 2026, kfz_de_wikipedia_raw_2026-10-05.txt), and the rest
  read as 1-4 digits through common handwriting letter/digit look-alikes
  (O->0, G->6, Z->2, T->7, E->3, Y->4). A hit needs a whole-string fit. Also the
  Bundeswehr "Y-" series (Y-digits) is tested.

  Dutch (series 3, 99-XX-99, 1973-78, and series 4, XX-99-XX, 1978-91, current in 1984):
  letters allowed per nl.wikipedia "Nederlands kenteken" (fetched 5 Oct 2026): series 4
  uses no vowels A E I O U and no C Q W; Y allowed from series 4. Series 3: C I O Q W Y
  not used, vowels allowed per that page.

The 2026 German list includes post-1990 East German codes and post-2012 reintroduced
codes that did not exist in West Germany in 1984; every hit is annotated by hand in
NOTES.md for 1984 validity. Exit 0 always; output is the hit list.
"""
import itertools
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LOOK = {"O": "0", "G": "6", "Z": "2", "T": "7", "E": "3", "Y": "4"}
VARIANTS = {"YOGTZE": "YOGTZE", "YOG'TZE": "YOG|TZE", "YOGZE (T struck)": "YOGZE"}


def german_codes():
    t = (HERE / "kfz_de_wikipedia_raw_2026-10-05.txt").read_text()
    return sorted(set(re.findall(r"^\| '''([A-ZÄÖÜ]{1,3})'''\s*$", t, re.M)))


def as_digits(s):
    if not s or not all(c in LOOK or c.isdigit() for c in s):
        return None
    return "".join(LOOK.get(c, c) for c in s)


def german(v, codes):
    hits = []
    s = v.replace("|", "")
    for i in range(1, 4):
        p = s[:i]
        if p not in codes:
            continue
        for j in (1, 2):
            mid, rest = s[i:i + j], s[i + j:]
            if len(mid) != j or not mid.isalpha():
                continue
            d = as_digits(rest)
            if d and 1 <= len(d) <= 4:
                hits.append(f"{p}-{mid} {d}")
    if s[0] == "Y":
        d = as_digits(s[1:])
        if d:
            hits.append(f"Y-{d} (Bundeswehr series)")
    return hits


def dutch(v):
    s = v.replace("|", "")
    out = []
    # every assignment of each sign to itself or its digit look-alike
    opts = [(c, LOOK[c]) if c in LOOK else (c,) for c in s]
    for combo in itertools.product(*opts):
        r = "".join(combo)
        if len(r) != 6:
            continue
        a, b, c = r[:2], r[2:4], r[4:]
        if a.isalpha() and b.isdigit() and c.isalpha():
            bad = set(a + c) & set("AEIOUCQW")
            out.append((f"{a}-{b}-{c} series 4", "ok" if not bad else "letters not issued: " + "".join(sorted(bad))))
        if a.isdigit() and b.isalpha() and c.isdigit():
            bad = set(b) & set("CIOQWY")
            out.append((f"{a}-{b}-{c} series 3", "ok" if not bad else "letters not issued: " + "".join(sorted(bad))))
    return out


def main():
    codes = set(german_codes())
    print(f"german codes parsed: {len(codes)}")
    subs = sorted({v.replace('|', '')[i:j] for v in VARIANTS.values()
                   for i in range(6) for j in range(i + 1, min(i + 4, 7))})
    print("substrings of length 1-3 that are German district codes (2026 list):",
          ", ".join(x for x in subs if x in codes) or "none")
    for name, v in VARIANTS.items():
        print(f"\n== {name}")
        g = german(v, codes)
        print("  german whole-string fits:", "; ".join(g) if g else "none")
        d = dutch(v)
        print("  dutch 6-sign fits:", "; ".join(f"{x} [{y}]" for x, y in d) if d else
              "none (no letter/digit look-alike assignment gives 99-XX-99 or XX-99-XX)")
    return 0


def control():
    """Matched control: the 720 orderings of the same six letters, same rules. A fit rate
    near the target's says the look-alike freedom, not the string, makes the fit."""
    codes = set(german_codes())
    n = g = d = 0
    for p in set(itertools.permutations("YOGTZE")):
        s = "".join(p)
        n += 1
        g += bool([h for h in german(s, codes) if "Bundeswehr" not in h])
        d += any(y == "ok" for _, y in dutch(s))
    print(f"\ncontrol (all {n} orderings of Y,O,G,T,Z,E): german district fit {g}/{n}, "
          f"dutch issued-letter fit {d}/{n}; Bundeswehr Y-digits fit = every ordering starting with Y "
          f"({sum(1 for p in set(itertools.permutations('YOGTZE')) if p[0]=='Y')}/{n}), by construction")


if __name__ == "__main__":
    main()
    if "--control" in sys.argv:
        control()
