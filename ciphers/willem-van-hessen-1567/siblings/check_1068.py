#!/usr/bin/env python3
"""Regenerate reading_1068.txt by applying key_1068.tsv to the sign classes of ciphertext_1068.tsv (CLAUDE.md rule 7);
exit non-zero if the committed reading, or the reconciliation outputs (w1068/reconcile_1068.py --check), are stale.

The reading is the period decipherer's own line read back through the key rebuilt from it (a key source, not a reading of
an unread letter). Tokens whose class is unkeyed ('?') print as '?'; the per-token gloss value is in ciphertext_1068.tsv.

Usage: python3 check_1068.py [--check]
"""
import collections, csv, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent


def tsv(p):
    with open(p, encoding="utf-8") as f:
        return [r for r in csv.DictReader((l for l in f if not l.startswith("#")), delimiter="\t")]


def regenerate():
    key = {r["sign_desc"]: (r["value"], r["grade"]) for r in tsv(HERE / "key_1068.tsv")}
    ct = tsv(HERE / "ciphertext_1068.tsv")
    lines = collections.defaultdict(list)
    grades = collections.Counter()
    agree = 0
    for r in ct:
        v, g = key.get(r["sign_desc"], ("?", "?"))
        tokg = r["grade"] if v != "?" else "?"
        grades[tokg if v == r["value"] else ("M" if v != "?" else "?")] += 1
        agree += v == r["value"]
        lines[int(r["line"])].append(v if not v.startswith("^") else "[" + v.strip("^") + "]")
    body = "\n".join(f"L{ln:02d}: " + "".join(lines[ln]) for ln in sorted(lines))
    head = (f"# briefnr 1068 p.2 (Oranje -> Willem van Hessen, 13 Mar 1563): ciphertext_1068.tsv through key_1068.tsv, "
            f"{len(ct)} signs; key value = the token's own reconciled gloss on {agree} of {len(ct)}; per-token grades "
            f"{dict(sorted(grades.items()))} (H/M from ciphertext_1068.tsv where the key agrees; '?' = class unkeyed). "
            "'-' = no gloss over the sign. WVO-1068-KEY, 10 Oct 2026.\n")
    return head + body + "\n"


def main():
    text = regenerate()
    if "--check" in sys.argv:
        r = subprocess.run([sys.executable, str(HERE / "w1068" / "reconcile_1068.py"), "--check"], capture_output=True,
                           text=True)
        print(r.stdout.strip())
        ok = (HERE / "reading_1068.txt").exists() and (HERE / "reading_1068.txt").read_text(encoding="utf-8") == text
        print("OK: reading_1068.txt current" if ok else "STALE: reading_1068.txt")
        sys.exit(0 if ok and r.returncode == 0 else 1)
    (HERE / "reading_1068.txt").write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
