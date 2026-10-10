#!/usr/bin/env python3
"""Regenerate reading_153.txt by applying key_153.tsv to the sign classes of ciphertext_153.tsv (CLAUDE.md rule 7), and
run w153/recon_153.py --check and w153/controls_153.py --check; exit non-zero if anything committed is stale.

WVO 153 p6 lines 1-9 are a KEY SOURCE: the plaintext survives in two contemporary decipherments (p7 f.5, p8 f.6), so this
is the cipher read back through the key rebuilt from them, not a reading of an unread letter. Classes graded M in
key_153.tsv print in brackets; '.' prints as '.'.

Usage: python3 check_153.py [--check]
"""
import collections, csv, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "reading_153.txt"


def tsv(p):
    with open(p, encoding="utf-8") as f:
        return [r for r in csv.DictReader((l for l in f if not l.startswith("#")), delimiter="\t")]


def regenerate():
    key = {r["sign"]: (r["value"], r["grade"]) for r in tsv(HERE / "key_153.tsv")}
    lines = collections.defaultdict(list)
    grades = collections.Counter()
    for r in tsv(HERE / "ciphertext_153.tsv"):
        if r["sign"] == ".":
            lines[int(r["line"])].append("."); continue
        v, g = key.get(r["sign"], ("?", "?"))
        grades[g] += 1
        v = v if len(v) < 3 or g == "C" and v.isalpha() and len(v) <= 3 else "<" + v + ">"
        lines[int(r["line"])].append(v if g == "C" else "[" + v.strip("<>") + "]")
    body = "\n".join(f"L{ln:02d}: " + "".join(lines[ln]) for ln in sorted(lines))
    head = (f"# WVO 153 p6 (Oranje -> August, 1 Sept 1566) lines 1-9 of 20: ciphertext_153.tsv through key_153.tsv, "
            f"{sum(grades.values())} signs, key-class grades {dict(sorted(grades.items()))}. Key source (two period "
            "decipherments on p7/p8), not a reading of an unread text. WVO-153-KEY-2, 10 Oct 2026.\n")
    return head + body + "\n"


def main():
    s = regenerate()
    rc = 0
    for script in ("w153/recon_153.py", "w153/controls_153.py"):
        r = subprocess.run([sys.executable, str(HERE / script), "--check"], capture_output=True, text=True)
        print(script, "->", r.stdout.splitlines()[0] if r.stdout else r.stderr.strip())
        rc |= r.returncode
    if "--check" in sys.argv:
        if not OUT.exists() or OUT.read_text() != s:
            print("STALE: reading_153.txt"); rc = 1
        else:
            print("reading_153.txt up to date")
        sys.exit(rc)
    OUT.write_text(s); print(s, end=""); sys.exit(rc)


if __name__ == "__main__":
    main()
